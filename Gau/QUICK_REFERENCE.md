# 📚 OSACO Website - Quick Reference

## 🔗 Documentation Overview

Your website comes with comprehensive documentation to help you manage and maintain it effectively:

### 📖 Main Documentation Files

| File | Purpose | When to Use |
|------|---------|-------------|
| **DOCUMENTATION.md** | Complete overview and getting started guide | First-time setup and general reference |
| **CONFIGURATION_GUIDE.md** | Business settings and technical configuration | Updating business info, SEO, email setup |
| **CONTENT_MANAGEMENT.md** | Editing website content and adding new pages | Changing text, images, services, FAQ |
| **TROUBLESHOOTING.md** | Solving common problems | When something isn't working |
| **DEPLOYMENT_GUIDE.md** | Publishing your website online | Going live and hosting setup |

---

## ⚡ Quick Actions

### 🏢 Update Business Information
1. Edit `src/config/business.js` - Address, phone, email, hours
2. Edit `src/config/seo.js` - Make sure it matches business.js
3. Restart development server: `npm run dev`

### 📝 Change Website Text
1. Homepage content: Edit `src/views/Home.vue`
2. Service pages: Edit files in `src/views/services/`
3. Save file and changes appear automatically

### 📧 Fix Contact Form
1. Check `backend/config/config.py` - Email settings
2. Ensure backend is running: `cd backend && python app.py`
3. Test form submission

### 🖼️ Replace Images
1. Add new images to `src/assets/images/`
2. Keep same filename for automatic update
3. Or update image path in code

### 🚀 Deploy Website
1. Build: `npm run build`
2. Upload `dist/` folder to hosting
3. Or use Netlify drag-and-drop

---

## 📞 Emergency Quick Fixes

### Website Won't Start
```bash
rm -rf node_modules
npm install
npm run dev
```

### Contact Form Not Working
1. Check if backend is running
2. Verify email settings in `backend/config/config.py`
3. Check browser console for errors

### Images Missing
1. Check file paths in code
2. Verify images exist in `src/assets/images/`
3. Clear browser cache (Ctrl+F5)

---

## 🎯 Most Common Tasks

### 1. **Change Business Hours**
**File**: `src/config/business.js`
```javascript
hours: {
  monday: "8:00 AM - 6:00 PM",    // 👈 Edit these
  tuesday: "8:00 AM - 6:00 PM",
  // ... etc
}
```

### 2. **Update Phone Number**
**Files**: `src/config/business.js` AND `src/config/seo.js`
```javascript
// Both files must match!
phone: "07551656880"  // 👈 Change this
```

### 3. **Add New Service**
1. Copy existing service file from `src/views/services/`
2. Edit content for new service
3. Add route in `src/router/index.js`
4. Add link in navigation

### 4. **Change Service Areas**
**File**: `src/config/business.js`
```javascript
serviceAreas: [
  "Central London",     // 👈 Edit these areas
  "North London",
  // ... etc
]
```

### 5. **Update FAQ**
**File**: `src/views/Home.vue` - Find FAQ section
```vue
<h3>Your question here?</h3>           <!-- 👈 Edit question -->
<p>Your answer here.</p>               <!-- 👈 Edit answer -->
```

---

## 🔧 File Structure Quick Reference

```
Gau/
├── 📁 src/
│   ├── 📁 config/
│   │   ├── business.js          # 👈 Business info (address, phone, etc.)
│   │   └── seo.js              # 👈 SEO settings (must match business.js)
│   ├── 📁 views/
│   │   ├── Home.vue            # 👈 Homepage content
│   │   └── 📁 services/        # 👈 Individual service pages
│   ├── 📁 components/
│   │   └── Layout.vue          # 👈 Navigation and footer
│   └── 📁 assets/images/       # 👈 All website images
├── 📁 backend/
│   ├── app.py                  # 👈 Backend server
│   └── 📁 config/
│       └── config.py           # 👈 Email settings
└── 📄 Documentation files      # 👈 These guide files
```

---

## 🎨 Design Customization

### Colors
**File**: `tailwind.config.js`
```javascript
colors: {
  brand: '#3B82F6',        // 👈 Main blue color
  'brand-dark': '#1D4ED8', // 👈 Darker blue
}
```

### Fonts and Styles
**File**: `src/styles/main.css`
- Look for classes starting with `.professional-`

---

## 📱 Testing Checklist

### Before Making Changes Live:
- [ ] Test on desktop browser
- [ ] Test on mobile phone
- [ ] Submit contact form to test email
- [ ] Check all service page links
- [ ] Verify business information is correct

### Development Commands:
```bash
# Start development (with hot reload)
npm run dev

# Build for production
npm run build

# Start backend
cd backend && python app.py
```

---

## 🆘 When to Get Help

### ✅ You Can Handle:
- Changing text content
- Updating business information
- Replacing images
- Adding FAQ items
- Updating service descriptions

### 🔴 Contact Developer For:
- Adding complex new features
- Database issues
- Server configuration
- Security updates
- Major design changes

---

## 📊 Performance Tips

### Keep Website Fast:
- Optimize images (under 500KB each)
- Don't add too many large images
- Test loading speed regularly
- Clear browser cache when testing

### SEO Best Practices:
- Update content regularly
- Get customer reviews
- Keep business information accurate
- Use location keywords naturally

---

## 🔗 Useful Links

### Learning Resources:
- [Vue.js Guide](https://vuejs.org/guide/) - For template editing
- [TailwindCSS Docs](https://tailwindcss.com/docs) - For styling
- [Google My Business](https://business.google.com/) - Local SEO

### Testing Tools:
- [Google PageSpeed](https://pagespeed.web.dev/) - Test loading speed
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - Test mobile version
- [HTML Validator](https://validator.w3.org/) - Check for errors

---

*💡 **Pro Tip**: Always test changes locally with `npm run dev` before deploying to live website!*

---

**Need more detailed help?** Open the specific documentation file for your task:
- Business setup → `CONFIGURATION_GUIDE.md`
- Content editing → `CONTENT_MANAGEMENT.md`
- Problems → `TROUBLESHOOTING.md`
- Going live → `DEPLOYMENT_GUIDE.md`
