# FixIt Appliances - Full Stack Web Application

A modern full-stack web application built with Vue.js 3 frontend and Flask backend, featuring Tailwind CSS styling and deployed on Railway.

## 🏗️ Architecture

### Frontend (Vue.js 3 + Vite)
- **Framework**: Vue 3 with Composition API
- **Build Tool**: Vite 6.3.5
- **Styling**: Tailwind CSS 3.4.17
- **Location**: `src/` directory

### Backend (Flask + Python)
- **Framework**: Flask with factory pattern
- **WSGI Server**: Gunicorn
- **Features**: Contact forms, email service, health checks
- **Location**: `backend_temp/` directory

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
cd backend_temp
pip install -r requirements.txt
```

### 3. Development
```bash
# Frontend (from root)
npm run dev

# Backend (from backend_temp/)
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
├── backend_temp/          # Flask backend
│   ├── app/               # Flask application package
│   ├── config/            # Configuration files
│   └── wsgi.py            # WSGI entry point
├── public/                # Static files (robots.txt, sitemap.xml)
├── dist/                  # Built frontend (generated)
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

The application is configured for deployment on Railway with multiple build strategies:

1. **Primary**: Nixpacks (specified in `railway.json`)
2. **Fallback**: Docker (using `Dockerfile`)
3. **Alternative**: Procfile-based deployment

### Environment Variables
- `PORT` - Server port (set by Railway)
- `FLASK_ENV` - Flask environment (production/development)

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
