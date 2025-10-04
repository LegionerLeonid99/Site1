# Multi-stage Dockerfile for O-TECH HOME SERVICES
# This builds both frontend (Vue.js) and backend (Flask) in a single container

FROM node:18-alpine AS frontend-builder

# Build frontend
WORKDIR /app/frontend
COPY package*.json ./
COPY vite.config.js ./
COPY postcss.config.js ./
COPY tailwind.config.js ./
COPY index.html ./
RUN npm install

COPY src ./src
COPY public ./public
RUN npm run build

# Python stage
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production
RUN pip install gunicorn

# Copy backend code
COPY app ./app
COPY config ./config
COPY wsgi.py ./
COPY .env* ./

# Copy built frontend from builder stage
COPY --from=frontend-builder /app/frontend/dist ./static

# Set working directory to root (where backend files are)
WORKDIR /app

# Set environment variables
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose port (Railway will set PORT env variable)
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/health')"

# Run the application with gunicorn (using shell form for env var expansion)
CMD ["/bin/sh", "-c", "FLASK_ENV=production gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120 --access-logfile - --error-logfile - --log-level debug wsgi:app"]
