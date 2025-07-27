# 🚨 Troubleshooting Guide

## 🔧 Common Issues and Solutions

### 🔴 Website Won't Start

#### Issue: `npm run dev` fails
```bash
Error: Cannot find module '@vitejs/plugin-vue'
```

**Solution**:
```bash
# Delete node_modules and reinstall
rm -rf node_modules
npm install

# Try force reinstall
npm install --force

# Clear npm cache
npm cache clean --force
```

#### Issue: Port already in use
```bash
Error: Port 5173 is already in use
```

**Solution**:
```bash
# Kill process using the port
# Windows:
netstat -ano | findstr :5173
taskkill /PID <PID_NUMBER> /F

# Mac/Linux:
lsof -ti:5173 | xargs kill -9

# Or start on different port
npm run dev -- --port 3000
```

### 🔴 Backend Issues

#### Issue: Flask server won't start
```bash
Error: ModuleNotFoundError: No module named 'flask'
```

**Solution**:
```bash
# Install Python dependencies
cd backend
pip install -r requirements.txt

# If using virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

#### Issue: Email not sending
**Symptoms**: Contact form submits but no email received

**Solutions**:
1. **Check email configuration**:
   ```python
   # In backend/config/config.py
   MAIL_USERNAME = 'your-email@gmail.com'  # ✅ Correct email
   MAIL_PASSWORD = 'your-app-password'     # ✅ App password, not regular password
   ```

2. **Gmail App Password Setup**:
   - Enable 2-Factor Authentication
   - Generate App Password (not regular password)
   - Use 16-character app password in config

3. **Check spam folder** - emails might be filtered

4. **Test with curl**:
   ```bash
   curl -X POST http://localhost:5000/api/contact \
   -H "Content-Type: application/json" \
   -d '{"name":"Test","email":"test@test.com","message":"Test"}'
   ```

### 🔴 Display Issues

#### Issue: Images not loading
**Symptoms**: Broken image icons or missing pictures

**Solutions**:
1. **Check file paths**:
   ```vue
   <!-- Correct path -->
   <img src="/src/assets/images/hero-section/your-image.jpg" />
   
   <!-- Common mistakes -->
   <img src="src/assets/images/hero-section/your-image.jpg" />  <!-- Missing / -->
   <img src="/assets/images/hero-section/your-image.jpg" />     <!-- Missing src -->
   ```

2. **Verify file exists**:
   ```bash
   ls src/assets/images/hero-section/
   ```

3. **Check file permissions** (Linux/Mac):
   ```bash
   chmod 644 src/assets/images/hero-section/*
   ```

4. **Clear browser cache**: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

#### Issue: Styling looks broken
**Symptoms**: No colors, layout issues, missing fonts

**Solutions**:
1. **Check TailwindCSS build**:
   ```bash
   npm run build:css
   ```

2. **Verify CSS imports**:
   ```javascript
   // In src/main.js
   import './style.css'  // ✅ Should be present
   ```

3. **Clear browser cache** and hard refresh

4. **Check for CSS conflicts** in browser dev tools

### 🔴 Routing Issues

#### Issue: 404 on service pages
**Symptoms**: Direct links to `/services/coffee-machines` return 404

**Solutions**:
1. **Check router configuration**:
   ```javascript
   // In src/router/index.js
   {
     path: '/services/coffee-machines',
     component: () => import('../views/services/CoffeeMachines.vue')
   }
   ```

2. **Verify component file exists**:
   ```bash
   ls src/views/services/CoffeeMachines.vue
   ```

3. **For production deployment**, configure server redirects:
   ```apache
   # .htaccess for Apache
   RewriteEngine On
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteCond %{REQUEST_FILENAME} !-d
   RewriteRule . /index.html [L]
   ```

### 🔴 Performance Issues

#### Issue: Website loads slowly
**Solutions**:
1. **Optimize images**:
   ```bash
   # Compress images online or use tools
   # Recommended: Use WebP format for better compression
   ```

2. **Check network tab** in browser dev tools for large files

3. **Enable compression** in production server

4. **Use CDN** for static assets

#### Issue: JavaScript errors in console
**Common errors and solutions**:

```javascript
// Error: Cannot read property 'name' of undefined
// Solution: Add null checks
{{ businessConfig?.business?.name || 'Loading...' }}

// Error: Hydration mismatch
// Solution: Ensure server and client render same content

// Error: Module not found
// Solution: Check import paths
import Layout from '../components/Layout.vue'  // ✅ Correct
import Layout from './components/Layout.vue'   // ❌ Wrong path
```

### 🔴 Mobile Issues

#### Issue: Website doesn't work on mobile
**Solutions**:
1. **Check viewport meta tag** in `index.html`:
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

2. **Test responsive classes**:
   ```vue
   <!-- Mobile-first approach -->
   <div class="text-sm sm:text-base lg:text-lg">
   ```

3. **Use browser dev tools** mobile simulator

4. **Test on real devices** - simulators aren't always accurate

## 🛠️ Debugging Tools

### Browser Developer Tools
1. **Console tab**: Check for JavaScript errors
2. **Network tab**: Monitor failed requests
3. **Elements tab**: Inspect HTML/CSS
4. **Performance tab**: Analyze loading speed

### Vue.js Debugging
```javascript
// Add temporary debugging
console.log('businessConfig:', businessConfig)

// Use Vue dev tools browser extension
```

### Backend Debugging
```python
# In Flask routes, add logging
import logging
logging.basicConfig(level=logging.DEBUG)

app.logger.debug(f"Received form data: {request.json}")
```

## 📋 Health Check Checklist

### Website Health Check
Run through this checklist regularly:

#### Frontend
- [ ] Homepage loads without errors
- [ ] All service pages accessible
- [ ] Contact form submits successfully
- [ ] Images load properly
- [ ] Mobile version works
- [ ] No console errors

#### Backend
- [ ] API endpoints respond
- [ ] Email sending works
- [ ] Database connections (if applicable)
- [ ] Server logs show no errors

#### SEO
- [ ] Page titles load correctly
- [ ] Meta descriptions present
- [ ] Structured data validates
- [ ] Sitemap accessible
- [ ] No broken links

### Quick Tests
```bash
# Test frontend build
npm run build

# Test backend endpoints
curl http://localhost:5000/api/health

# Validate HTML
# Use online HTML validator

# Test mobile responsiveness
# Use Google Mobile-Friendly Test
```

## 🆘 When to Get Help

### Contact Developer If:
- Database corruption or data loss
- Security vulnerabilities discovered
- Major feature additions needed
- Server configuration issues
- SSL certificate problems

### Self-Service Issues:
- Content updates
- Image replacements
- Contact information changes
- Basic styling adjustments
- FAQ updates

### Emergency Contacts
- **Website down**: Check hosting provider status first
- **Email not working**: Verify email settings
- **Security concerns**: Change passwords immediately

## 📚 Additional Resources

### Learning Resources
- [Vue.js Documentation](https://vuejs.org/)
- [TailwindCSS Docs](https://tailwindcss.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Testing Tools
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)
- [HTML Validator](https://validator.w3.org/)
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

### Backup Strategy
1. **Regular backups** of entire project folder
2. **Version control** with Git
3. **Database backups** (if applicable)
4. **Email configuration backups**

---

*Still having issues? Document the exact error message and steps to reproduce, then contact your developer.*
