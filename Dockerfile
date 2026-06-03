FROM python:3.11-slim

WORKDIR /app

COPY requirements-render.txt .

RUN pip install --no-cache-dir -r requirements-render.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]