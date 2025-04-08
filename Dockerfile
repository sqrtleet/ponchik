FROM python:3.12

WORKDIR /litestar-app

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry update

COPY . .

CMD ["litestar", "run"]
