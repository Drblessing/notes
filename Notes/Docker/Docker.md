# Docker

1. Creating a python environment from a specific version of python

```bash
docker run --rm -v $(pwd):/app -w /app python:3.10.5 bash -c "python3 -m venv .venv"
```

Might have some problems.
