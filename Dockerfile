FROM python:3.13-alpine

WORKDIR /app

# Install system dependencies using Alpine's apk instead of apt-get
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-client \
    postgresql-dev

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .



CMD gunicorn -k uvicorn.workers.UvicornWorker app.main:app --host 0.0.0.0 --port $PORT
