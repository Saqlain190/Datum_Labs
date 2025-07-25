FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .
COPY .dlt /app/.dlt

ENV PYTHONPATH=/app/my_source/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["dagster", "dev", "-m", "my_source.definitions", "-h", "0.0.0.0", "-p", "3000"]
