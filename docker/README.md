# Docker Guide

## Docker Basics

### Building Docker Images

```bash
# Build an image from a Dockerfile
docker build -t image-name:tag .

# Build with specific Dockerfile
docker build -f Dockerfile.dev -t image-name:dev .
```

### Running Docker Containers

```bash
# Run a container
docker run image-name

# Run with port mapping
docker run -p 8080:80 image-name

# Run in detached mode (background)
docker run -d image-name

# Run with environment variables
docker run -e ENV_VAR=value image-name

# Run with volume mounting
docker run -v /host/path:/container/path image-name

# Run with name
docker run --name my-container image-name
```

### Managing Containers

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop container-id

# Remove a container
docker rm container-id

# View logs
docker logs container-id

# Execute command in running container
docker exec -it container-id /bin/bash
```

### Managing Images

```bash
# List images
docker images

# Remove an image
docker rmi image-id

# Pull image from registry
docker pull image-name:tag

# Push to registry
docker push image-name:tag
```

## Docker Compose

### Basic Commands

```bash
# Start services
docker-compose up

# Start in detached mode
docker-compose up -d

# Build images before starting
docker-compose up --build

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# View logs
docker-compose logs

# View logs for specific service
docker-compose logs service-name

# Execute command in service
docker-compose exec service-name command

# List running services
docker-compose ps
```

### Working with Multiple Compose Files

```bash
# Use specific compose file
docker-compose -f docker-compose.dev.yml up

# Use multiple compose files
docker-compose -f docker-compose.yml -f docker-compose.override.yml up
```

## Project Structure

```
docker/
├── README.md              # This file
├── examples/
│   ├── node-app/         # Node.js example
│   ├── python-app/       # Python example
│   └── multi-service/    # Multi-service example
├── docker-compose.yml    # Main compose file
├── .env.example          # Example environment variables
└── .dockerignore         # Files to ignore in build context
```

## Best Practices

1. **Use .dockerignore** - Exclude unnecessary files from build context
2. **Multi-stage builds** - Reduce final image size
3. **Layer caching** - Order Dockerfile commands for optimal caching
4. **Non-root user** - Run containers as non-root when possible
5. **Environment variables** - Use .env files for configuration
6. **Health checks** - Add health checks to services
7. **Resource limits** - Set memory and CPU limits
8. **Named volumes** - Use named volumes for persistent data

## Common Issues & Solutions

### Permission Issues

```bash
# Fix permission issues with volumes
docker exec container-id chown -R user:group /path
```

### Cleanup Commands

```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove all unused data
docker system prune -a

# Remove unused volumes
docker volume prune
```

### Networking

```bash
# List networks
docker network ls

# Create custom network
docker network create my-network

# Connect container to network
docker network connect my-network container-name
```

## Example Usage

See the `examples/` directory for complete working examples of:

- Single service applications
- Multi-service applications with databases
- Development vs production configurations
