
#!/Users/danielblessing/github/notes/bin/.benv/bin/python

import random
import pyfiglet

def cowboy_fortune():
    fortunes = [
        "Don't squat with your spurs on.",
        "Never approach a bull from the front, a horse from the rear, or a fool from any direction.",
        "The best way to get a new rope is to need an old one.",
        "If you're ridin' ahead of the herd, take a look back every now and then to make sure it's still there.",
        "When you find yourself in a hole, the first thing to do is stop diggin'.",
        "Lettin' the cat outta the bag is a whole lot easier than puttin' it back in."
    ]

    art = pyfiglet.figlet_format("Howdy!", font="slant")
    print(art)
    print("Your cowboy fortune for the day:")
    print(f"    \__{random.choice(fortunes)}__/")

if __name__ == "__main__":
    cowboy_fortune()
