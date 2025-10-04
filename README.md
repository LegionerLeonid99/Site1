# O-TECH Home Services - Full Stack Web Application

A modern full-stack web application built with Vue.js 3 frontend and Express.js backend, featuring Tailwind CSS styling and deployed on Railway.

## 🏗️ Architecture

### Frontend (Vue.js 3 + Vite)
- **Framework**: Vue 3 with Composition API
- **Build Tool**: Vite 6.3.5
- **Styling**: Tailwind CSS 3.4.17
- **Location**: `src/` directory

### Backend (Express.js + Node.js)
- **Framework**: Express.js
- **Features**: Contact forms, email service, health checks, SPA static serving
- **Location**: `server.js`

### Deployment
- **Platform**: Railway
- **Container**: Docker

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn

### 1. Install Dependencies
```bash
npm install
```

### 2. Development
```bash
# Frontend
npm run dev

# Backend
npm run server:dev
```

### 3. Build for Production
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
├── public/                # Static files (robots.txt, sitemap.xml)
├── dist/                  # Built frontend (generated)
├── server.js              # Express backend
├── .env.example           # Sample environment variables
└── *.config.js            # Build configurations
```

## 🔧 Configuration Files

- `package.json` - Dependencies and scripts
- `vite.config.js` - Vite build configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `Dockerfile` - Docker container configuration

## 🚢 Deployment

### Railway
1. Connect your GitHub repository to Railway
2. Set the following environment variables in Railway dashboard:
   - `MAIL_SERVER=smtp.gmail.com`
   - `MAIL_PORT=587`
   - `MAIL_USERNAME=otechhomeservices@gmail.com`
   - `MAIL_PASSWORD=your-email-app-password`
   - `BUSINESS_EMAIL=otechhomeservices@gmail.com`
   - `BUSINESS_NAME=O-TECH HOME SERVICES LTD`
   - `BUSINESS_PHONE=02030261006`
   - `FRONTEND_URL=https://your-railway-app-url.railway.app`

Railway will automatically detect the Dockerfile and build the application.

## 📧 Email Service

The application includes an email service for contact forms and newsletters using Nodemailer. Configure the email settings in the environment variables above.

## 🐳 Docker

To build and run locally with Docker:

```bash
docker build -t otech-app .
docker run -p 3001:3001 otech-app
```

## � Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run server` - Start production server
- `npm run server:dev` - Start server with nodemon
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
