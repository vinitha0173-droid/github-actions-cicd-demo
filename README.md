# Automated CI/CD Pipeline with GitHub Actions

![CI/CD Pipeline](https://github.com/vinitha0173-droid/github-actions-cicd-demo/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project demonstrates an automated CI/CD pipeline using GitHub Actions.

## Features

- Automated code linting with Ruff.
- Unit testing with Pytest.
- Docker image building.
- Automatic workflow execution on pushes and pull requests to the main branch.

## Technologies Used

- Python 3.12
- GitHub Actions
- Ruff
- Pytest
- Docker

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run linting:

```bash
ruff check .
```

Run unit tests:

```bash
pytest -v
```

Build the Docker image:

```bash
docker build -t trustlens-demo:latest .
```

## Workflow

1. Code is pushed to the main branch.
2. GitHub Actions installs Python dependencies.
3. Ruff checks the code.
4. Pytest executes unit tests.
5. Docker builds the image after the tests pass.
