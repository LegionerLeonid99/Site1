# Railway Deployment Guide for O-TECH HOME SERVICES

This guide will help you deploy the O-TECH HOME SERVICES website to Railway.

## Prerequisites

1. Railway account (sign up at https://railway.app)
2. GitHub repository connected to Railway
3. Gmail App Password for email service

## Deployment Steps

### 1. Create New Project on Railway

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository `Site1`
5. Railway will automatically detect the project and use Nixpacks builder

### 2. Configure Build Settings (Optional)

Railway should automatically detect and build the project. If needed, you can configure:

**Build Command:**
```bash
npm install && npm run build && pip install -r backend/requirements.txt && pip install gunicorn
```

**Start Command:**
```bash
cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile - app:app
```

### 3. Configure Environment Variables

In Railway project settings, add these environment variables:

```env
# Flask Configuration
SECRET_KEY=your-production-secret-key-generate-random-string
FLASK_ENV=production
FLASK_DEBUG=False

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=otechhomeservices@gmail.com
MAIL_PASSWORD=your-gmail-app-password

# Business Settings
BUSINESS_EMAIL=otechhomeservices@gmail.com
BUSINESS_NAME=O-TECH HOME SERVICES LTD
BUSINESS_PHONE=02030261006

# CORS Settings
ALLOWED_ORIGINS=["https://your-railway-domain.railway.app"]

# Port (automatically set by Railway)
PORT=${{PORT}}
```

### 3. Generate Gmail App Password

1. Go to your Google Account: https://myaccount.google.com
2. Navigate to Security > 2-Step Verification
3. Scroll to "App passwords" at the bottom
4. Generate new app password for "Mail"
5. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)
6. Add it to Railway as `MAIL_PASSWORD`

### 4. Generate Secret Key

Generate a secure secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Add the output to Railway as `SECRET_KEY`

### 5. Deploy

Railway will automatically:
1. Detect the `Dockerfile`
2. Build both frontend (Vue.js) and backend (Flask)
3. Deploy to a Railway domain
4. Provide HTTPS automatically

## Post-Deployment

### 1. Test the Application

Visit your Railway URL:
- `https://your-app.railway.app` - Frontend
- `https://your-app.railway.app/api/health` - API health check

### 2. Update CORS Settings

Once you have your Railway domain:
1. Update `ALLOWED_ORIGINS` in Railway environment variables
2. Replace `your-railway-domain.railway.app` with actual domain
3. Redeploy if needed

### 3. Test Contact Forms

1. Visit the website
2. Fill out a contact form
3. Verify emails are sent/received

## Custom Domain (Optional)

### Add Custom Domain

1. In Railway project settings, go to "Settings" > "Domains"
2. Click "Add Domain"
3. Enter your domain: `www.o-techhomeservices.co.uk`
4. Follow Railway's instructions to update DNS records

### Update Environment Variables

After adding custom domain:

```env
ALLOWED_ORIGINS=["https://www.o-techhomeservices.co.uk","https://o-techhomeservices.co.uk"]
```

## Monitoring

### View Logs

Railway provides real-time logs:
1. Click on your deployment
2. View "Deployments" tab
3. Click on active deployment to see logs

### Health Check

Monitor application health:
```
GET https://your-app.railway.app/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "message": "O-TECH HOME SERVICES API is running"
}
```

## Troubleshooting

### Email Not Sending

1. Verify `MAIL_USERNAME` and `MAIL_PASSWORD` in Railway
2. Check Gmail App Password is correct
3. Ensure 2-Step Verification is enabled in Gmail
4. Review logs for email errors

### Frontend Not Loading

1. Check build logs for frontend compilation errors
2. Verify `dist` folder was created during build
3. Check static file serving in Flask

### CORS Errors

1. Verify `ALLOWED_ORIGINS` includes your Railway domain
2. Check CORS configuration in `backend/app/__init__.py`
3. Ensure `https://` is included in origins

### Port Issues

Railway automatically sets `PORT` environment variable. The app uses:
```python
port = int(os.getenv('PORT', 5000))
```

## Updating the Application

Railway auto-deploys on git push:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update application"
   git push origin main
   ```
3. Railway automatically detects changes and redeploys

## Production Checklist

- [ ] All environment variables set in Railway
- [ ] Gmail App Password configured
- [ ] SECRET_KEY is secure and unique
- [ ] FLASK_DEBUG set to False
- [ ] ALLOWED_ORIGINS configured with actual domain
- [ ] Custom domain configured (if applicable)
- [ ] Email sending tested
- [ ] Contact forms tested
- [ ] All pages loading correctly
- [ ] SSL/HTTPS working
- [ ] Health endpoint responding

## Support

For Railway-specific issues:
- Documentation: https://docs.railway.app
- Discord: https://discord.gg/railway

For application issues:
- Check Railway logs
- Review application error logs
- Test locally with production environment variables
