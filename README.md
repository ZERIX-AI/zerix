# Zerix AI Platform

Zerix AI Platform is a powerful and flexible AI application development platform that enables you to create, deploy, and manage AI applications with ease.

## Overview

The platform consists of several key components:

- **API Service**: Core backend service handling all AI-related operations
- **Web Console**: User-friendly web interface for managing AI applications
- **Middleware Services**: Supporting services including database, cache, and vector store
- **SDK**: Client libraries for multiple programming languages

## Components

### API Service
- RESTful API service for AI operations
- Supports multiple AI model providers
- Handles chat, completion, and workflow operations
- Built with scalability and performance in mind

### Web Console
- Modern web interface for platform management
- Real-time chat and completion testing
- Application configuration and monitoring
- User and team management

### Middleware Services
- PostgreSQL for persistent data storage
- Redis for caching and session management
- Weaviate for vector storage
- Sandbox service for code execution

### SDKs
Available for multiple programming languages:
- Node.js SDK
- Python SDK
- More coming soon...

## Deployment

The platform is containerized and can be deployed using Kubernetes:

```bash
# Create namespace
kubectl apply -f k3s/zerix-ai-middleware.yaml

# Deploy middleware services
kubectl apply -f k3s/zerix-ai-middleware.yaml

# Deploy API service
kubectl apply -f k3s/zerix-ai-api.yaml

# Deploy web console
kubectl apply -f k3s/zerix-ai-web.yaml
```

## Configuration

Key configuration files:
- `k3s/zerix-ai-api-config.yaml`: API service configuration
- `k3s/zerix-ai-middleware.yaml`: Middleware services configuration
- `k3s/zerix-ai-web.yaml`: Web console configuration

## License

MIT License

## Contact

For more information, please contact: business@zerix.io
