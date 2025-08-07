# Dockerfile

FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/src

WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Download TextBlob corpora
RUN python -m textblob.download_corpora

# Copy project code
COPY . .

# Default command
CMD ["sh", "-c", "PYTHONPATH=src uvicorn main.api:app --reload"]



