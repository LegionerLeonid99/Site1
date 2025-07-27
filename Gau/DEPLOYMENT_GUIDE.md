# 🚀 Deployment Guide

## 📋 Pre-Deployment Checklist

### ✅ Content Review
- [ ] All business information is accurate and up-to-date
- [ ] Contact forms tested and working
- [ ] All images optimized and loading correctly
- [ ] Text content proofread and spell-checked
- [ ] Service descriptions are complete
- [ ] FAQ section addresses common questions

### ✅ Technical Testing
- [ ] Website works on desktop browsers (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness tested on multiple devices
- [ ] All internal links work correctly
- [ ] Contact forms submit successfully
- [ ] Email notifications are received
- [ ] Loading speed is acceptable (< 3 seconds)

### ✅ SEO Preparation
- [ ] Meta titles and descriptions are optimized
- [ ] Google My Business profile created/updated
- [ ] Social media profiles linked
- [ ] Sitemap generated and accessible
- [ ] Analytics tracking code added (Google Analytics)

---

## 🌐 Frontend Deployment Options

### Option 1: Netlify (Recommended for beginners)

#### Benefits:
- ✅ Free tier available
- ✅ Automatic deployments from Git
- ✅ Built-in SSL certificates
- ✅ Global CDN
- ✅ Form handling

#### Setup Steps:

1. **Prepare your build**:
   ```bash
   npm run build
   ```

2. **Sign up for Netlify**:
   - Go to [netlify.com](https://netlify.com)
   - Create account (can use GitHub)

3. **Deploy via drag & drop**:
   - Drag your `dist/` folder to Netlify
   - Your site is live immediately!

4. **Set up custom domain** (optional):
   - Buy domain from registrar
   - Add domain in Netlify settings
   - Update DNS records

#### Advanced Netlify Setup:

1. **Connect to Git repository**:
   ```bash
   # Push your code to GitHub first
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin main
   ```

2. **Auto-deploy from GitHub**:
   - In Netlify: New site from Git
   - Connect GitHub repository
   - Build settings:
     - Build command: `npm run build`
     - Publish directory: `dist`

3. **Environment variables** (if needed):
   - Site settings → Environment variables
   - Add any API keys or config

### Option 2: Vercel

#### Setup Steps:
1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   npm run build
   vercel --prod
   ```

3. **Follow prompts** to configure deployment

### Option 3: Traditional Web Hosting

#### For shared hosting (cPanel, etc.):

1. **Build your site**:
   ```bash
   npm run build
   ```

2. **Upload files**:
   - Upload entire `dist/` folder contents
   - Use FTP client or file manager
   - Upload to `public_html/` or equivalent

3. **Configure redirects**:
   ```apache
   # Create .htaccess file in root
   RewriteEngine On
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteCond %{REQUEST_FILENAME} !-d
   RewriteRule . /index.html [L]
   ```

---

## ⚙️ Backend Deployment Options

### Option 1: Heroku (Beginner-friendly)

#### Setup Steps:

1. **Install Heroku CLI**:
   - Download from [heroku.com](https://heroku.com)

2. **Prepare backend for Heroku**:
   ```bash
   cd backend
   
   # Create Procfile
   echo "web: python app.py" > Procfile
   
   # Ensure requirements.txt is up to date
   pip freeze > requirements.txt
   
   # Create runtime.txt (optional)
   echo "python-3.9.16" > runtime.txt
   ```

3. **Deploy**:
   ```bash
   # Login to Heroku
   heroku login
   
   # Create app
   heroku create your-app-name
   
   # Set environment variables
   heroku config:set MAIL_USERNAME=your-email@gmail.com
   heroku config:set MAIL_PASSWORD=your-app-password
   
   # Deploy
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

4. **Update frontend API URL**:
   ```javascript
   // In your frontend code, update API calls to use Heroku URL
   const API_URL = 'https://your-app-name.herokuapp.com'
   ```

### Option 2: DigitalOcean/VPS

#### For experienced users:

1. **Set up server**:
   ```bash
   # Create droplet/VPS
   # Install Python, pip, nginx
   sudo apt update
   sudo apt install python3 python3-pip nginx
   ```

2. **Deploy Flask app**:
   ```bash
   # Upload code
   # Install dependencies
   pip3 install -r requirements.txt
   
   # Set up systemd service
   # Configure nginx
   # Set up SSL with Let's Encrypt
   ```

### Option 3: Railway/Render

#### Modern alternatives to Heroku:

1. **Railway**:
   - Connect GitHub repository
   - Automatic deployments
   - Built-in database options

2. **Render**:
   - Similar to Heroku
   - Free tier available
   - Automatic SSL

---

## 🔧 Configuration for Production

### Environment Variables

#### Frontend (.env file):
```env
VITE_API_URL=https://your-backend-domain.com
VITE_GOOGLE_MAPS_API_KEY=your-maps-api-key
```

#### Backend (Heroku config vars or .env):
```env
FLASK_ENV=production
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
SECRET_KEY=your-secret-key-here
```

### Security Considerations

1. **Use HTTPS everywhere**:
   - Both frontend and backend
   - Update all API calls to use https://

2. **Secure environment variables**:
   - Never commit secrets to Git
   - Use platform environment variables

3. **CORS configuration**:
   ```python
   # In Flask backend
   from flask_cors import CORS
   
   CORS(app, origins=['https://yourdomain.com'])
   ```

4. **Rate limiting**:
   ```python
   # Add rate limiting to contact forms
   from flask_limiter import Limiter
   ```

---

## 📊 Post-Deployment Setup

### Analytics Setup

1. **Google Analytics**:
   ```html
   <!-- Add to index.html -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_MEASUREMENT_ID');
   </script>
   ```

2. **Google Search Console**:
   - Add and verify your website
   - Submit sitemap: `yoursite.com/sitemap.xml`

### Performance Monitoring

1. **Test website speed**:
   - [Google PageSpeed Insights](https://pagespeed.web.dev/)
   - [GTmetrix](https://gtmetrix.com/)

2. **Monitor uptime**:
   - [UptimeRobot](https://uptimerobot.com/)
   - [Pingdom](https://pingdom.com/)

### SEO Setup

1. **Google My Business**:
   - Create/claim business listing
   - Add photos and business info
   - Encourage customer reviews

2. **Local directories**:
   - Yelp, Yellow Pages
   - Local business directories
   - Industry-specific directories

---

## 📋 Deployment Commands Reference

### Build and Deploy (Netlify)
```bash
# Build
npm run build

# Deploy to Netlify (if using CLI)
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### Build and Deploy (Vercel)
```bash
# Build and deploy
npm run build
npx vercel --prod
```

### Backend Deploy (Heroku)
```bash
# One-time setup
heroku create your-app-name
heroku config:set KEY=value

# Deploy updates
git add .
git commit -m "Update"
git push heroku main
```

### Domain Setup
```bash
# Netlify
netlify domains:add yourdomain.com

# Heroku
heroku domains:add yourdomain.com
```

---

## 🚨 Troubleshooting Deployment

### Common Issues:

#### Build Fails
```bash
# Clear cache and rebuild
rm -rf node_modules dist
npm install
npm run build
```

#### API Calls Fail After Deployment
- Check CORS settings
- Verify API URLs are correct
- Confirm environment variables are set

#### Images Not Loading
- Verify image paths are correct
- Check if images are in build output
- Ensure images are optimized for web

#### Contact Form Not Working
- Verify backend is deployed and running
- Check email configuration
- Test API endpoints directly

### Rollback Strategy
```bash
# Netlify - rollback to previous deploy
netlify rollback

# Heroku - rollback to previous release
heroku rollback v123

# Manual - redeploy from Git
git reset --hard HEAD~1
# Then redeploy
```

---

## 📞 Going Live Checklist

### Final Steps:
- [ ] Custom domain configured
- [ ] SSL certificate active (https://)
- [ ] All forms tested on live site
- [ ] Analytics tracking confirmed
- [ ] Search Console verification complete
- [ ] Business listings updated with new URL
- [ ] Social media profiles updated
- [ ] Email signatures updated
- [ ] Marketing materials updated

### Launch Day:
- [ ] Announce on social media
- [ ] Send email to existing customers
- [ ] Update Google My Business
- [ ] Monitor for any issues
- [ ] Celebrate! 🎉

---

*Your website is now live! Monitor performance and user feedback for any adjustments needed.*
