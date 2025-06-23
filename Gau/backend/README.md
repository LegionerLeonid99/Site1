# Flask Backend for FixIt Appliances Website

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- pip (Python package manager)

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Configuration
Copy the example environment file and configure it:
```bash
copy .env.example .env
```

Edit `.env` with your actual configuration:
```env
SECRET_KEY=your-secret-key-here
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
BUSINESS_EMAIL=business@fixitappliances.com
BUSINESS_NAME=FixIt Appliances
BUSINESS_PHONE=(555) 123-4567
FRONTEND_URL=http://localhost:5173
```

### 3. Run Development Server

#### Option A: Python directly
```bash
python app.py
```

#### Option B: Use startup scripts
```bash
# Windows Command Prompt
start.bat

# Windows PowerShell
.\start.ps1
```

The API will be available at `http://localhost:5000`

## ✅ Installation Status
- ✅ Flask and dependencies installed
- ✅ Environment configured
- ✅ Server tested and running
- ✅ CORS configured for frontend
- ✅ All API endpoints functional

## API Endpoints

### Contact Forms
- `POST /api/contact` - General contact form
- `POST /api/contact/appliances` - Appliance service form
- `POST /api/contact/coffee-machines` - Coffee machine service form
- `POST /api/contact/dishwashers` - Dishwasher service form
- `POST /api/contact/washing-machines` - Washing machine service form
- `POST /api/contact/hobs` - Hob service form
- `POST /api/contact/kitchen-ventilators` - Kitchen ventilator service form
- `POST /api/contact/all-electrical` - Electrical service form
- `POST /api/contact/commercial-equipment` - Commercial equipment service form

### Newsletter
- `POST /api/newsletter` - Newsletter signup

### Health Check
- `GET /api/health` - API health check

## Features

- CORS enabled for frontend integration
- Email sending with Flask-Mail
- Input validation and sanitization
- Error handling and logging
- Rate limiting (to be implemented)
- Environment-based configuration

## Deployment

The backend can be deployed to:
- Heroku
- AWS EC2
- DigitalOcean
- Vercel (with Python support)
- Railway

See deployment guides in the `docs/` folder.
