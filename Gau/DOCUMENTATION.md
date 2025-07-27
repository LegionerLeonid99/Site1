# 📚 OSACO Website Documentation

## 🚀 Quick Start Guide

Welcome to your OSACO appliance repair website! This documentation will help you understand, maintain, and customize your website.

### 📋 Table of Contents
- [Website Overview](#website-overview)
- [Getting Started](#getting-started)
- [Configuration Guide](#configuration-guide)
- [Content Management](#content-management)
- [SEO Management](#seo-management)
- [Maintenance Tasks](#maintenance-tasks)
- [Troubleshooting](#troubleshooting)
- [Deployment Guide](#deployment-guide)

---

## 🌐 Website Overview

Your website is built with modern web technologies:
- **Frontend**: Vue.js 3 with Vite build tool
- **Styling**: TailwindCSS for responsive design
- **Backend**: Flask (Python) for contact forms and API
- **Features**: Responsive design, SEO optimized, contact forms, service pages

### 🎯 Key Features
- ✅ Professional appliance repair business website
- ✅ Responsive design (works on all devices)
- ✅ Contact forms with email integration
- ✅ SEO optimized for search engines
- ✅ Service-specific pages
- ✅ Google Maps integration
- ✅ Professional animations and effects

---

## 🚀 Getting Started

### Prerequisites
- Node.js (version 16 or higher)
- Python 3.8+ (for backend)
- Git (for version control)

### 🔧 Installation
```bash
# 1. Navigate to project directory
cd e:\Site1\Gau

# 2. Install frontend dependencies
npm install

# 3. Install backend dependencies
cd backend
pip install -r requirements.txt
cd ..

# 4. Start development servers
npm run dev  # Frontend (usually http://localhost:5173)
# In another terminal:
cd backend && python app.py  # Backend (usually http://localhost:5000)
```

### 📁 Project Structure
```
Gau/
├── src/                    # Frontend source code
│   ├── components/         # Reusable components
│   ├── views/             # Page components
│   ├── config/            # Configuration files
│   └── styles/            # CSS styles
├── backend/               # Python Flask backend
│   ├── app.py            # Main backend application
│   ├── routes/           # API endpoints
│   └── config/           # Backend configuration
├── public/               # Static files
└── DOCUMENTATION.md      # This file
```

---

## ⚙️ Configuration Guide

### 🏢 Business Information
All business information is centralized in configuration files:

#### 📍 Primary Configuration: `src/config/business.js`
This file controls all business-related information displayed on your website.

**Key sections to update:**
- **Address**: Update your actual business location
- **Contact Info**: Your phone, email, website URL
- **Business Hours**: Your operating schedule
- **Service Areas**: Locations you serve

#### 🔍 SEO Configuration: `src/config/seo.js`
This file manages search engine optimization.

**Important sections:**
- **Business Info**: Must match your business.js info
- **Keywords**: Terms people search for to find you
- **Page Titles**: What appears in browser tabs and search results
- **Meta Descriptions**: Snippets shown in search results

### 🎨 Styling Configuration
- **Colors**: Defined in `tailwind.config.js`
- **Components**: Styled in `src/styles/main.css`
- **Responsive Design**: Built into TailwindCSS classes

---

## 📝 Content Management

### 🏠 Homepage Content
**File**: `src/views/Home.vue`

**Editable sections:**
- Hero section text and buttons
- Services description
- About/family business content
- FAQ questions and answers
- Contact form fields

### 📄 Service Pages
**Location**: `src/views/services/`

Each service has its own page:
- `Appliances.vue` - General appliances
- `CoffeeMachines.vue` - Coffee machine repair
- `Dishwashers.vue` - Dishwasher services
- `WashingMachines.vue` - Washing machine repair
- `Hobs.vue` - Hob repair services
- And more...

### 🖼️ Images
**Location**: `src/assets/images/`
- Replace images in respective folders
- Maintain same filenames for automatic updates
- Recommended formats: JPG, PNG, WebP

---

## 🔍 SEO Management

### 📊 Current SEO Setup
Your website is pre-configured with:
- ✅ Optimized page titles and descriptions
- ✅ Local business schema markup
- ✅ Mobile-friendly responsive design
- ✅ Fast loading times
- ✅ Social media integration ready

### 🎯 SEO Best Practices
1. **Regular Content Updates**: Add new content monthly
2. **Local Citations**: List your business in local directories
3. **Google My Business**: Keep your listing updated
4. **Customer Reviews**: Encourage and respond to reviews
5. **Page Speed**: Monitor loading times

### 📈 SEO Monitoring Tools
- Google Search Console
- Google Analytics
- Google My Business insights
- Local SEO tools

---

## 🔧 Maintenance Tasks

### 📅 Weekly Tasks
- [ ] Check contact form submissions
- [ ] Update business hours if changed
- [ ] Monitor website performance
- [ ] Backup important data

### 📅 Monthly Tasks
- [ ] Review and update service descriptions
- [ ] Check for broken links
- [ ] Update seasonal content
- [ ] Review SEO performance
- [ ] Update service areas if expanded

### 📅 Quarterly Tasks
- [ ] Update business information
- [ ] Review and optimize images
- [ ] Update contact information
- [ ] Analyze competitor websites
- [ ] Plan content updates

---

## 🚨 Troubleshooting

### Common Issues and Solutions

#### 🔴 Website Won't Start
```bash
# Check if dependencies are installed
npm install

# Clear cache and restart
npm run dev --force
```

#### 🔴 Contact Form Not Working
1. Check backend server is running
2. Verify email configuration in `backend/config/config.py`
3. Check browser console for errors

#### 🔴 Images Not Loading
1. Verify image paths in code
2. Check image files exist in `src/assets/images/`
3. Clear browser cache

#### 🔴 SEO Issues
1. Verify meta tags are loading
2. Check Google Search Console for errors
3. Validate structured data

### 🆘 Getting Help
- Check browser console for error messages
- Review network tab for failed requests
- Validate HTML/CSS using online tools
- Test website on multiple devices

---

## 🚀 Deployment Guide

### 📋 Pre-Deployment Checklist
- [ ] Test all contact forms
- [ ] Verify all links work
- [ ] Check mobile responsiveness
- [ ] Validate SEO setup
- [ ] Test loading speed
- [ ] Backup current version

### 🌐 Frontend Deployment (Netlify/Vercel)
```bash
# Build production version
npm run build

# Deploy dist/ folder to your hosting provider
```

### ⚙️ Backend Deployment (Heroku/VPS)
```bash
# Deploy Flask backend to your server
# Configure environment variables
# Set up SSL certificate
```

### 🔐 Security Considerations
- Use HTTPS (SSL certificate)
- Keep dependencies updated
- Secure API endpoints
- Regular backups
- Monitor for security issues

---

## 📞 Support Information

### 🛠️ Technical Support
For technical issues:
1. Check this documentation first
2. Review error messages carefully
3. Test in different browsers
4. Contact your developer if needed

### 📈 Business Growth Tips
- Regularly update content
- Collect customer testimonials
- Optimize for local search
- Use social media integration
- Monitor competitor websites

---

## 📋 File Quick Reference

### 🔧 Configuration Files
- `src/config/business.js` - Business information
- `src/config/seo.js` - SEO settings
- `tailwind.config.js` - Styling configuration
- `backend/config/config.py` - Backend settings

### 📄 Key Content Files
- `src/views/Home.vue` - Homepage
- `src/components/Layout.vue` - Site layout
- `src/views/services/` - Service pages
- `backend/routes/` - API endpoints

### 🎨 Styling Files
- `src/styles/main.css` - Main styles
- `src/styles/components.css` - Component styles

---

*Last updated: July 27, 2025*
*Website: OSACO Appliance Repair Services*
