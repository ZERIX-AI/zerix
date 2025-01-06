# Docker Deployment Guide

## Directory Structure
```
docker/
├── certbot/                    # SSL certificate automation
├── nginx/                      # Nginx configuration
├── ssrf_proxy/                 # SSRF proxy configuration
├── startupscripts/            # Database initialization scripts
├── volumes/                    # Data volumes
│   ├── myscale/              # MyScale configuration
│   ├── opensearch/           # OpenSearch configuration
│   └── sandbox/              # Sandbox configuration
├── docker-compose.zerixai.yaml # Docker Compose main configuration
├── middleware.env.example      # Middleware environment variables example
└── .env.example               # Environment variables example
```

## Quick Start

1. Copy environment variable example files
```bash
cp middleware.env.example middleware.env
cp .env.example .env
```

2. Modify environment variables
- Update database passwords and other configurations in middleware.env
- Update application settings in .env

3. Start services
```bash
docker compose -f docker-compose.zerixai.yaml up -d
```

## SSL Certificate Configuration

For HTTPS setup, refer to certbot/README.md. Main steps:

1. Set environment variables
```properties
NGINX_SSL_CERT_FILENAME=fullchain.pem
NGINX_SSL_CERT_KEY_FILENAME=privkey.pem
NGINX_ENABLE_CERTBOT_CHALLENGE=true
CERTBOT_DOMAIN=your_domain.com
CERTBOT_EMAIL=example@your_domain.com
```

2. Obtain certificate
```bash
docker network prune
docker compose --profile certbot up --force-recreate -d
docker compose exec -it certbot /bin/sh /update-cert.sh
```

3. Enable HTTPS
```properties
NGINX_HTTPS_ENABLED=true
```

4. Restart Nginx
```bash
docker compose --profile certbot up -d --no-deps --force-recreate nginx
```

## Service Description

- **API**: REST API service
- **Web**: Frontend web application
- **Sandbox**: Code execution sandbox
- **SSRF Proxy**: Proxy service to prevent SSRF attacks
- **Database**: PostgreSQL database
- **Redis**: Cache and message queue
- **Weaviate**: Vector database

## Environment Variables

Key configuration items:

- `POSTGRES_PASSWORD`: Database password, default zerixai123456
- `POSTGRES_DB`: Database name, default zerix
- `REDIS_PASSWORD`: Redis password, default zerixai123456
- `SANDBOX_API_KEY`: Sandbox API key, default zerix-sandbox

For more configuration options, refer to middleware.env.example file.

## Important Notes

1. Database initialization required for first deployment
2. Recommended to change all default passwords
3. HTTPS recommended for production environment
4. Ensure sufficient disk space for data directories
