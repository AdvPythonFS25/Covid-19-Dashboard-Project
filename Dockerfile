FROM python:3.11-slim

WORKDIR /app

# install Poetry
RUN apt-get update && apt-get install -y curl \
 && curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# copy metadata first (better layer-caching)
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

# copy source code
COPY src/ ./src

ENV PYTHONPATH=/app/src

EXPOSE 8501
CMD ["poetry", "run", "streamlit", "run", "src/streamlitApp.py", "--server.address=0.0.0.0"]