# Written by deepseek/deepseek-r1-0528-qwen3-8b.
# Running locally.
# As a test of lm studio and the model.
import pygame
import random
import math

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BACKGROUND = (10, 15, 30)
PLAYER_COLOR = (70, 200, 255)
ENEMY_COLORS = [(235, 70, 140), (235, 180, 65), (70, 235, 140)]
LASER_COLOR = (255, 220, 80)
EXPLOSION_COLOR = (255, 140, 0)


# Player class
class Player:
    def __init__(self):
        self.width = 50
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 20
        self.speed = 5
        self.lives = 3
        self.score = 0

    def draw(self):
        # Draw the player ship (triangle)
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height),
        ]
        pygame.draw.polygon(screen, PLAYER_COLOR, points)

        # Draw engine flames
        flame_heights = [10, 7]
        for i in range(2):
            offset_x = self.width // 4 * (i + 1)
            points = [
                (self.x + offset_x, self.y + self.height),
                (
                    self.x + offset_x - 5,
                    self.y + self.height + flame_heights[i] * (1 - i),
                ),
                (
                    self.x + offset_x + 5,
                    self.y + self.height + flame_heights[i] * (1 - i),
                ),
            ]
            pygame.draw.polygon(screen, (255, 100, 30), points)

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed


# Enemy class
class Enemy:
    def __init__(self, x):
        self.width = 35
        self.height = 30
        self.x = x
        self.y = random.randint(-100, -40)
        self.speed_x = 1
        self.speed_y = random.uniform(0.5, 1)
        self.color = random.choice(ENEMY_COLORS)

    def draw(self):
        # Draw enemy ship (rectangle with points at top corners)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # Draw enemy details (small triangles)
        pygame.draw.polygon(
            screen,
            (0, 0, 0),
            [
                (self.x + 5, self.y + 5),
                (self.x + 10, self.y + 5),
                (self.x + 7.5, self.y),
            ],
        )

        pygame.draw.polygon(
            screen,
            (0, 0, 0),
            [
                (self.x + self.width - 10, self.y + 5),
                (self.x + self.width - 5, self.y + 5),
                (self.x + self.width - 7.5, self.y),
            ],
        )

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls (gentler bounce by reversing x direction)
        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.speed_x *= -1

        # Return True if enemy is out of bounds
        return self.y > HEIGHT or self.x + self.width < 0 or self.x > WIDTH


# Bullet class
class Bullet:
    def __init__(self, x, y, is_player_bullet=True):
        self.x = x
        self.y = y
        self.radius = 4 if is_player_bullet else 3
        self.speed = 7 if is_player_bullet else 5
        self.is_player_bullet = is_player_bullet

    def draw(self):
        pygame.draw.circle(screen, LASER_COLOR, (self.x, self.y), self.radius)

    def move(self):
        if self.is_player_bullet:
            self.y -= self.speed
        else:
            self.y += self.speed


# Explosion class
class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.max_radius = 30
        self.growing = True

    def draw(self):
        pygame.draw.circle(screen, EXPLOSION_COLOR, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (255, 180, 60), (self.x, self.y), self.radius - 2)

    def update(self):
        if self.growing:
            self.radius += 1
            if self.radius >= self.max_radius:
                self.growing = False
        else:
            self.radius -= 1

        return self.radius <= 0


# Star background class for parallax effect
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (200, 210, 255), (self.x, self.y), 1)


# Create game objects
player = Player()
enemies = [Enemy(random.randint(50, WIDTH - 150)) for _ in range(8)]
bullets = []
explosions = []
stars = [Star(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(150)]
font = pygame.font.Font(None, 36)

# Game variables
game_over = False
level = 1


# Auto-fire variables
FIRE_RATE = 40  # bullets per second
fire_delay = 1000 // FIRE_RATE  # milliseconds between shots
last_shot_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_over:
            # Restart game on space key after game over
            if event.key == pygame.K_SPACE:
                player = Player()
                enemies = [
                    Enemy(random.randint(50, WIDTH - 150)) for _ in range(level * 2)
                ]
                bullets = []
                explosions = []
                game_over = False
    # Auto-fire bullets for player if not game over
    if not game_over:
        now = pygame.time.get_ticks()
        if now - last_shot_time >= fire_delay:
            bullets.append(Bullet(player.x + player.width // 2, player.y))
            last_shot_time = now

    # Handle continuous key presses for movement (arrow keys and WASD)
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move("right")

    # Draw everything
    screen.fill(BACKGROUND)

    # Update and draw stars (parallax effect for background layers)
    for star in stars:
        if random.random() < 0.1:  # Update position occasionally for twinkling effect
            star.x += random.uniform(-0.5, 0.5)
        pygame.draw.circle(
            screen,
            (200, random.randint(180, 220), 255),
            (star.x, star.y),
            random.randint(1, 2),
        )

    # Draw player
    player.draw()

    # Update and draw enemies if game is not over
    if not game_over:
        for enemy in enemies[:]:
            # Draw and update enemy
            enemy.draw()

            # Remove enemy if it goes out of bounds
            if enemy.move():
                enemies.remove(enemy)
                continue

            # Enemy shooting logic
            if random.random() < 0.01:
                bullets.append(
                    Bullet(enemy.x + enemy.width // 2, enemy.y + enemy.height, False)
                )

        # Check bullet collisions
        for bullet in bullets[:]:
            # Check if player bullet hits enemy
            if bullet.is_player_bullet:
                for enemy in enemies[:]:
                    # Collision detection between bullet and enemy
                    if (
                        bullet.x > enemy.x
                        and bullet.x < enemy.x + enemy.width
                        and bullet.y > enemy.y
                        and bullet.y < enemy.y + enemy.height
                    ):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        explosions.append(
                            Explosion(
                                enemy.x + enemy.width // 2, enemy.y + enemy.height // 2
                            )
                        )
                        player.score += 10
                        break
            else:
                # Check collision with player
                if (
                    bullet.x > player.x
                    and bullet.x < player.x + player.width
                    and bullet.y > player.y
                    and bullet.y < player.y + player.height
                ):
                    bullets.remove(bullet)
                    player.lives -= 1
                    explosions.append(Explosion(player.x + player.width // 2, player.y))

                    if player.lives <= 0:
                        game_over = True

    # Update and draw explosions (remove when done growing/shrinking)
    to_remove_explosions = []
    for explosion in explosions[:]:
        explosion.draw()
        if explosion.update():
            to_remove_explosions.append(explosion)

    for explosion in to_remove_explosions:
        explosions.remove(explosion)

    # Update and draw bullets
    for bullet in bullets[:]:
        bullet.move()
        if 0 <= bullet.y <= HEIGHT:  # Only draw visible bullets
            bullet.draw()
        else:
            bullets.remove(bullet)

    # Draw score and lives
    score_text = font.render(f"Score: {player.score}", True, (200, 255, 255))
    screen.blit(score_text, (10, 10))

    lives_text = font.render(f"Lives: {player.lives}", True, PLAYER_COLOR)
    screen.blit(lives_text, (WIDTH - 100, 10))

    level_text = font.render(f"Level: {level}", True, (255, 200, 100))
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))

    # Check if all enemies are gone
    if len(enemies) == 0:
        level += 1
        # Add new enemies with increased speed based on current level
        for _ in range(level * 2):
            enemies.append(Enemy(random.randint(50, WIDTH - 150)))
        # Add star background elements for visual effect
        explosions.append(Explosion(WIDTH // 2, HEIGHT // 2))

    # Check if enemy reaches player level
    for enemy in enemies:
        if enemy.y + enemy.height > player.y:
            game_over = True
            break

    if game_over:
        # Draw game over screen
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        game_over_text = font.render("GAME OVER", True, (255, 100, 100))
        screen.blit(
            game_over_text,
            (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50),
        )

        final_score = font.render(f"Final Score: {player.score}", True, (200, 255, 255))
        screen.blit(
            final_score, (WIDTH // 2 - final_score.get_width() // 2, HEIGHT // 2)
        )

        restart_text = font.render("Press SPACE to Restart", True, (100, 255, 180))
        screen.blit(
            restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50)
        )
        pygame.display.flip()

    # Update display
    pygame.display.flip()

    # Control frame rate (60 FPS)
    clock.tick(60)

# Quit the game
pygame.quit()
