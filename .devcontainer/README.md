# Development Container Configuration

This directory contains configuration files for Visual Studio Code Development Container, which provides a consistent development environment for the project.

## Files Overview

- `devcontainer.json`: Main configuration file for VS Code Dev Container
- `Dockerfile`: Container image definition based on Python 3.10
- `post_create_command.sh`: Setup script run after container creation
- `post_start_command.sh`: Setup script run when container starts
- `noop.txt`: Placeholder file for Docker build process

## Development Environment Features

- **Base Image**: Python 3.10 (Microsoft Dev Container)
- **Node.js**: LTS version with node-gyp dependencies
- **TypeScript**: Latest version
- **Docker-in-Docker**: Enabled with Docker Compose v2
- **VS Code Extensions**:
  - Python Pylint
  - GitHub Copilot
  - Python Extension

## Quick Start Commands

The environment provides several useful aliases:

```bash
start-api      # Start API server (Flask)
start-worker   # Start Celery worker
start-web      # Start frontend development server
start-containers # Start Docker middleware services
```

## Environment Setup Process

1. **Container Creation**:
   - Installs Poetry package manager
   - Sets up Node.js dependencies
   - Configures development aliases

2. **Container Start**:
   - Installs Python dependencies using Poetry
   - Initializes API environment

## Development Workflow

1. The container automatically sets up when opening in VS Code
2. Python dependencies are managed through Poetry
3. Frontend dependencies are managed through npm
4. Docker services can be started using the provided alias

## Important Notes

1. Ensure Docker is running on your host machine
2. VS Code Dev Containers extension must be installed
3. All paths are configured relative to workspace root
4. Poetry is used for Python dependency management
5. Node.js LTS is included for frontend development

## Port Configuration

Default service ports:
- API Server: 5001
- Web Development Server: 3000
- Docker Services: As configured in docker-compose files
