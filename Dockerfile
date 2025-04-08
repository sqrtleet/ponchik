FROM python:3.12

WORKDIR /litestar-app

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . .


# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["litestar", "run"]
