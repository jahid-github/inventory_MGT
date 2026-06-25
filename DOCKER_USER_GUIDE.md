# Docker User Guide

This guide lets another person run the Django project locally without installing Python, Django, or project dependencies on their machine.

## Required Software

Install only Docker Desktop:

- Windows/macOS: https://www.docker.com/products/docker-desktop/
- Linux: install Docker Engine and Docker Compose

After installation, open Docker Desktop and make sure it is running.

## Run The Project

Open a terminal in the project folder:

```powershell
cd C:\Users\meher\Documents\GitHub\inventory_MGT
```

Build and start the app:

```powershell
docker compose up --build
```

Open the project in a browser:

```text
http://localhost:8000
```

## Stop The Project

Press `Ctrl + C` in the terminal where Docker is running.

To stop containers from another terminal:

```powershell
docker compose down
```

## Run Again Later

After the first build, start it with:

```powershell
docker compose up
```

If dependencies change, rebuild:

```powershell
docker compose up --build
```

## Common Problems

If Docker says the port is already in use, another app is using port `8000`. Stop that app or edit `docker-compose.yml` and change:

```yaml
ports:
  - "8001:8000"
```

Then open:

```text
http://localhost:8001
```

If Docker cannot find `requirements.txt`, make sure you are running the command from the project root folder, the same folder that contains `manage.py`.

If the browser does not load immediately, wait a few seconds and refresh. Django starts after migrations finish.

## Useful Docker Commands

Run Django checks:

```powershell
docker compose run --rm web python manage.py check
```

Run migrations manually:

```powershell
docker compose run --rm web python manage.py migrate
```

Create an admin user:

```powershell
docker compose run --rm web python manage.py createsuperuser
```

View logs:

```powershell
docker compose logs -f web
```

## What Docker Handles

Docker installs and manages the project environment inside a container:

- Python
- Django
- Python packages from `requirements.txt`
- Django startup command
- Local development server

Other users do not need to create a virtual environment or run `pip install` manually.
