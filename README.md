# ALRP Local

This repository contains the Docker configuration for running the ALRP application locally.

## Docker Setup

This project includes Docker configuration for building and running the application in containers.

### Prerequisites

- Docker installed on your local machine
- GitHub account with access to this repository

### Building Locally

To build the Docker image locally:

```bash
docker build -t alrp-local .
```

To run the container:

```bash
docker run -p 8080:8080 alrp-local
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment.

### GitHub Container Registry

The Docker image is automatically built and pushed to GitHub Container Registry (GHCR) when:
- Changes are pushed to the `main` branch
- A new release tag is created

### Using the Pre-built Image

To use the pre-built image from GHCR:

```bash
docker pull ghcr.io/[owner]/alrp-local:latest
docker run -p 8080:8080 ghcr.io/[owner]/alrp-local:latest
```

Replace `[owner]` with your GitHub username or organization name.

## Testing

To run the Docker image tests:

```bash
npm install # Install test dependencies
npm test
```

## Development

### .dockerignore

The `.dockerignore` file excludes unnecessary files and directories when building the Docker image, keeping it lean and secure.

### GitHub Actions Workflow

The workflow in `.github/workflows/docker-build-push.yml` handles:
- Building the Docker image
- Pushing to GitHub Container Registry
- Tagging based on semantic versioning and git references
