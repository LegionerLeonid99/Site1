# Railway Deployment Fix

## Problem
Railway's Railpack couldn't determine how to build the app because it was looking for a `start.sh` script.

## Solution
Multiple configuration files have been created to support different Railway build methods:

### Files Created:

1. **`nixpacks.toml`** ⭐ (Primary - Railway's default)
   - Configures Nixpacks builder
   - Installs Node.js 18 and Python 3.10
   - Runs npm install and pip install
   - Builds frontend with `npm run build`
   - Copies dist to backend/static
   - Starts with Gunicorn

2. **`railway.json`**
   - Specifies Nixpacks builder
   - Defines build and start commands
   - Configures restart policy

3. **`Procfile`**
   - Alternative configuration
   - Defines web process with Gunicorn

4. **`start.sh`**
   - Backup shell script
   - Manual build and start process

5. **`Dockerfile`**
   - Docker-based deployment option
   - Multi-stage build

6. **Updated `package.json`**
   - Added `postbuild` script
   - Automatically copies dist to backend/static after build

## Quick Deploy Steps

### Option 1: Auto-Deploy (Recommended)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Railway deployment configuration"
   git push origin main
   ```

2. **Railway will automatically:**
   - Detect `nixpacks.toml`
   - Install Node.js and Python
   - Run `npm install && npm run build`
   - Install Python dependencies
   - Copy frontend build to backend/static
   - Start with Gunicorn

### Option 2: Manual Configuration in Railway Dashboard

If auto-deploy doesn't work, configure manually:

1. Go to Railway project → Settings
2. Under "Build", set:
   - **Build Command:**
     ```bash
     npm install && npm run build && pip install -r backend/requirements.txt && pip install gunicorn
     ```
   - **Start Command:**
     ```bash
     cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app
     ```

### Option 3: Use Dockerfile

In Railway project settings:
1. Go to Settings → Builder
2. Select "Dockerfile"
3. Enter path: `Dockerfile`
4. Redeploy

## Environment Variables Required

Set these in Railway dashboard under Variables:

```env
SECRET_KEY=<generate-random-secret-key>
FLASK_ENV=production
FLASK_DEBUG=False

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=otechhomeservices@gmail.com
MAIL_PASSWORD=<your-gmail-app-password>

BUSINESS_EMAIL=otechhomeservices@gmail.com
BUSINESS_NAME=O-TECH HOME SERVICES LTD
BUSINESS_PHONE=02030261006

PYTHONUNBUFFERED=1
```

## Generate Required Values

### Secret Key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Gmail App Password:
1. Go to https://myaccount.google.com/apppasswords
2. Create new app password for "Mail"
3. Copy the 16-character code

## Verify Deployment

After deployment, test:

1. **Homepage:**
   ```
   https://your-app.railway.app
   ```

2. **API Health:**
   ```
   https://your-app.railway.app/api/health
   ```
   Expected response:
   ```json
   {
     "status": "healthy",
     "message": "O-TECH HOME SERVICES API is running"
   }
   ```

3. **Contact Form:**
   - Fill out form on website
   - Check if email is sent

## Troubleshooting

### Build Fails

**Check Railway logs for:**
- Node.js installation errors
- npm install failures
- Python package installation issues
- Build command errors

**Solutions:**
- Ensure `package.json` has valid dependencies
- Check `backend/requirements.txt` syntax
- Verify Node.js 18 compatibility

### Frontend Not Loading

**Check:**
- `dist` folder created during build
- Files copied to `backend/static`
- Flask serving static files correctly

**Solution:**
In Railway logs, verify:
```
Building frontend...
✓ built in XXXms
Copying to backend/static...
```

### Email Not Working

**Check:**
- `MAIL_USERNAME` is correct email
- `MAIL_PASSWORD` is App Password (not regular password)
- Gmail 2-Step Verification enabled
- App Password generated for "Mail"

**Test Gmail settings:**
```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('otechhomeservices@gmail.com', 'your-app-password')
print("Success!")
```

### Port Issues

Railway automatically sets `$PORT`. Application uses:
```python
port = int(os.getenv('PORT', 5000))
```

Gunicorn binds to: `0.0.0.0:$PORT`

### CORS Errors

Add Railway domain to CORS:
```env
ALLOWED_ORIGINS=["https://your-app.railway.app"]
```

## Configuration Files Priority

Railway checks in this order:
1. `nixpacks.toml` ⭐ (Used)
2. `railway.json` ⭐ (Used)
3. `Dockerfile` (If specified)
4. `Procfile` (Backup)
5. Auto-detection (Fallback)

## What Gets Deployed

✅ Vue.js Frontend (built, optimized)
✅ Flask Backend API
✅ Email Service (Gmail SMTP)
✅ Contact Forms
✅ All Service Pages
✅ Static Assets
✅ Health Monitoring
✅ HTTPS (automatic)

## Post-Deployment Tasks

1. **Test all forms**
2. **Verify email sending**
3. **Check all pages load**
4. **Test mobile responsiveness**
5. **Add custom domain** (optional)
6. **Set up monitoring**

## Adding Custom Domain

1. Railway → Settings → Domains
2. Add: `www.o-techhomeservices.co.uk`
3. Update DNS records as instructed
4. Update environment variable:
   ```env
   ALLOWED_ORIGINS=["https://www.o-techhomeservices.co.uk","https://o-techhomeservices.co.uk"]
   ```

## Support Resources

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Railway Status: https://status.railway.app

## Success Checklist

- [ ] Repository pushed to GitHub
- [ ] Railway project created
- [ ] All environment variables set
- [ ] Build completed successfully
- [ ] Deployment active
- [ ] Health endpoint responding
- [ ] Homepage loads
- [ ] Contact form works
- [ ] Emails sending/receiving
- [ ] All pages accessible
- [ ] HTTPS active

Your site will be live at: `https://your-app.railway.app` 🚀
