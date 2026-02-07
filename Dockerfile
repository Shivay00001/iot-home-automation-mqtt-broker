FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 1883

ENTRYPOINT ["python", "src/main.py"]
