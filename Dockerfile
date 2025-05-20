FROM python:3.13-alpine AS install

WORKDIR /my_app

RUN apk add curl && curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock ./
RUN poetry sync --no-cache --no-root

FROM install AS run

COPY my_app/ my_app/

ENTRYPOINT [ "poetry", "run", "python", "-m", "my_app.main" ]

FROM install AS debug

COPY my_app/ my_app

ENTRYPOINT [ "poetry", \
    "run", \
    "debugpy", \
    "--listen", "0.0.0.0:5678", \
    "--wait-for-client", \
    "-m", \
    "uvicorn", \
    "--host", "0.0.0.0", \
    "--port", "8080", \
    "--reload", \
    "--factory", "my_app.setup:setup_app"  ]
