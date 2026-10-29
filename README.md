# GitHub Actions CI/CD Demo

![CI/CD Pipeline](https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY/actions/workflows/ci-cd.yml/badge.svg)

A beginner-friendly example of a CI/CD pipeline using GitHub Actions.

## What it does

- Runs Ruff lint checks.
- Runs unit tests with pytest.
- Builds a Docker image after linting and tests pass.
- On pushes to `main`, publishes the image to GitHub Container Registry (GHCR).
- Uses the automatically provided `GITHUB_TOKEN`; no Docker password is stored in source code.

## Run locally

```bash
python -m pip install -r requirements.txt
ruff check .
pytest -v
python app.py
docker build -t github-actions-cicd-demo .
```

## GitHub Actions

The workflow is `.github/workflows/ci-cd.yml`. It runs for pull requests targeting `main` and pushes to `main`.

After uploading this repository to GitHub, replace `YOUR-GITHUB-USERNAME` and `YOUR-REPOSITORY` in the badge URL with your GitHub username and repository name.

For image publishing, the workflow uses GitHub Container Registry and `secrets.GITHUB_TOKEN`. The repository workflow permissions include package publishing only in the build job.
