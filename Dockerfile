# Stage 1: Build the frontend# Multi-stage Dockerfile for O-TECH HOME SERVICES

FROM node:18-alpine AS frontend-builder# This builds both frontend (Vue.js) and backend (Flask) in a single container

WORKDIR /app

FROM node:18-alpine AS frontend-builder

# Copy all frontend related files

COPY package*.json ./# Build frontend

COPY vite.config.js ./WORKDIR /app/frontend

COPY postcss.config.js ./COPY package*.json ./

COPY tailwind.config.js ./COPY vite.config.js ./

COPY index.html ./COPY postcss.config.js ./

COPY src ./srcCOPY tailwind.config.js ./

COPY public ./publicCOPY index.html ./

RUN npm install

# Install dependencies and build

RUN npm installCOPY src ./src

RUN npm run buildCOPY public ./public

RUN npm run build

# Stage 2: Setup the backend

FROM node:18-alpine AS backend# Python stage

WORKDIR /appFROM python:3.10-slim



# Copy package files and install dependencies# Set working directory

COPY package*.json ./WORKDIR /app

RUN npm install --production

# Install system dependencies

# Copy server fileRUN apt-get update && apt-get install -y \

COPY server.js ./    gcc \

    && rm -rf /var/lib/apt/lists/*

# Copy the built frontend from the builder stage

COPY --from=frontend-builder /app/dist ./dist# Copy backend requirements and install Python dependencies

COPY requirements.txt ./

# Expose the port the app runs onRUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

# Install gunicorn for production

# Start the serverRUN pip install gunicorn

CMD ["node", "server.js"]

# Copy backend code
COPY app ./app
COPY config ./config
COPY wsgi.py ./
COPY gunicorn.conf.py ./
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

# Run the application with gunicorn using config file
CMD ["/bin/sh", "-c", "FLASK_ENV=production gunicorn --config gunicorn.conf.py wsgi:app"]
