# FixIt Appliances - Full Stack Web Application

A modern full-stack web application built with Vue.js 3 frontend and Flask backend, featuring Tailwind CSS styling and deployed on Railway.

## 🏗️ Architecture

### Frontend (Vue.js 3 + Vite)
- **Framework**: Vue 3 with Composition API
- **Build Tool**: Vite 6.3.5
- **Styling**: Tailwind CSS 3.4.17
- **Location**: `src/` directory

### Backend (Flask + Python)
- **Framework**: Flask with application factory pattern
- **WSGI Server**: Gunicorn
- **Features**: Contact forms, email service, health checks, SPA static serving
- **Location**: `app/` package with root-level `wsgi.py`

### Deployment
- **Platform**: Railway
- **Builder**: Nixpacks
- **Container**: Docker (fallback)

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- npm or yarn

### 1. Install Frontend Dependencies
```bash
npm install
```

### 2. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 3. Development
```bash
# Frontend (from root)
npm run dev

# Backend (from root)
python wsgi.py
```

### 4. Build for Production
```bash
npm run build
```

## 📁 Project Structure

```
├── src/                    # Vue.js frontend source
│   ├── components/         # Reusable Vue components
│   ├── views/             # Page components
│   ├── router/            # Vue Router configuration
│   └── assets/            # Static assets
├── app/                   # Flask application package
│   ├── routes/            # API blueprints
│   ├── services/          # Domain services (email, etc.)
│   └── __init__.py        # Application factory
├── config/                # Backend configuration classes
├── static/                # Built frontend copied for production serving
├── public/                # Static files (robots.txt, sitemap.xml)
├── dist/                  # Built frontend (generated)
├── .env.example           # Sample environment variables
└── *.config.js            # Build configurations
```

## 🔧 Configuration Files

- `package.json` - Frontend dependencies and scripts
- `vite.config.js` - Vite build configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `railway.json` - Railway deployment configuration
- `nixpacks.toml` - Nixpacks build configuration
- `Dockerfile` - Docker container configuration
- `Procfile` - Heroku-style process definition

## 🚢 Deployment
- Create a `.env` file based on `.env.example` for local development.
- In Railway, add the same keys under **Variables** to avoid runtime 502 errors.

## 🔐 Environment Setup

Copy the `.env.example` file to `.env` and adjust values for local development:

```bash
cp .env.example .env
```

Key values to update:

- `SECRET_KEY`: generate a random string (use `python -c "import secrets; print(secrets.token_urlsafe(32))"`).
- `MAIL_*` variables: use an SMTP provider with an app password.
- `BUSINESS_EMAIL` / `BUSINESS_PHONE`: shown in outbound email templates.
- `VITE_API_BASE_URL`: keep as `/api` to target the backend in production; set to `http://localhost:5000/api` only if not using the Vite dev proxy.

When running `npm run dev`, Vite proxies `/api` requests to `http://127.0.0.1:5000`, so the default `/api` value works for both development and production.


The application is configured for deployment on Railway with multiple build strategies:

1. **Primary**: Nixpacks (specified in `railway.json`)
2. **Fallback**: Docker (using `Dockerfile`)
3. **Alternative**: Procfile-based deployment

### Environment Variables
- `PORT` - Server port (set by Railway)
- `FLASK_ENV` - Flask environment (production/development)
- `SECRET_KEY` - Flask session secret (generate a strong value)
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD` - SMTP credentials for outbound email
- `BUSINESS_EMAIL`, `BUSINESS_NAME`, `BUSINESS_PHONE` - Business contact info used in emails
- `FRONTEND_URL`, `ALLOWED_ORIGINS` - Origins allowed for CORS
- `VITE_API_BASE_URL` - (Frontend) API root, defaults to `/api` when unset

## 📧 Features

- Modern responsive UI with Tailwind CSS
- Contact forms with email integration
- SEO optimization with sitemap generation
- Health check endpoints
- Production-ready deployment configuration

## 🛠️ Development Scripts

```bash
# Frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build

# Backend
cd backend_temp
python wsgi.py       # Start Flask development server
python test_api.py   # Test API endpoints
```

## 📄 License

This project is private and proprietary.
