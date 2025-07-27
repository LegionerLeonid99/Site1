# 🔧 Configuration Guide

## 📍 Business Information Setup

### Step 1: Update Business Details

**File to edit**: `src/config/business.js`

```javascript
export const businessConfig = {
  location: {
    address: {
      street: "YOUR_STREET_ADDRESS",     // 👈 CHANGE THIS
      city: "YOUR_CITY",                 // 👈 CHANGE THIS
      postcode: "YOUR_POSTCODE",         // 👈 CHANGE THIS
      country: "YOUR_COUNTRY"            // 👈 CHANGE THIS
    },
    contact: {
      phone: "YOUR_PHONE_NUMBER",        // 👈 CHANGE THIS
      email: "YOUR_EMAIL@domain.com",    // 👈 CHANGE THIS
      website: "www.yourwebsite.com"     // 👈 CHANGE THIS
    }
  },
  business: {
    name: "YOUR_BUSINESS_NAME",          // 👈 CHANGE THIS
    serviceAreas: [                      // 👈 CHANGE THESE
      "Area 1",
      "Area 2", 
      "Area 3"
    ]
  }
}
```

### Step 2: Update SEO Information

**File to edit**: `src/config/seo.js`

⚠️ **Important**: Make sure this matches your business.js information!

```javascript
export const seoConfig = {
  business: {
    name: "YOUR_BUSINESS_NAME",          // Must match business.js
    location: {
      streetAddress: "YOUR_STREET",      // Must match business.js
      city: "YOUR_CITY",                 // Must match business.js
      postalCode: "YOUR_POSTCODE",       // Must match business.js
    },
    contact: {
      phone: "+COUNTRY_CODE_PHONE",      // Include country code
      email: "YOUR_EMAIL@domain.com",    // Must match business.js
      website: "https://www.yoursite.com" // Include https://
    }
  }
}
```

## 🎨 Customization Options

### Colors and Branding

**File to edit**: `tailwind.config.js`

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: '#3B82F6',        // 👈 Your primary brand color
        'brand-dark': '#1D4ED8', // 👈 Darker version
      }
    }
  }
}
```

### Logo and Branding

1. **Replace logo/favicon**: Add your logo to `public/` folder
2. **Update page title**: Edit `index.html` title tag
3. **Update brand text**: Modify `src/components/Layout.vue`

### Service Areas

**File to edit**: `src/config/business.js`

```javascript
serviceAreas: [
  "Central London",      // 👈 Replace with your areas
  "North London",
  "South London",
  "East London",
  "West London",
  "Surrounding Areas"
]
```

## 📧 Email Configuration

### Backend Email Setup

**File to edit**: `backend/config/config.py`

```python
# Email settings
MAIL_SERVER = 'smtp.gmail.com'           # Your SMTP server
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'   # 👈 CHANGE THIS
MAIL_PASSWORD = 'your-app-password'      # 👈 CHANGE THIS
MAIL_DEFAULT_SENDER = 'your-email@gmail.com'
```

### Gmail Setup Instructions

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in config.py

3. **Update recipient email** in `backend/routes/contact.py`

## 🗺️ Google Maps Setup

### Basic Maps (Current Setup)
Your website currently uses basic Google Maps embeds (no API key required).

### Advanced Maps (Optional)

1. **Get Google Maps API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Maps Embed API
   - Create credentials → API Key

2. **Update configuration**:
   ```javascript
   // In src/config/business.js
   map: {
     apiKey: "YOUR_GOOGLE_MAPS_API_KEY"  // 👈 ADD YOUR KEY
   }
   ```

## 🎯 SEO Optimization

### Google My Business

1. **Create/claim** your Google My Business listing
2. **Verify** your business address
3. **Add photos** of your business
4. **Encourage customer reviews**

### Search Console Setup

1. **Sign up** for Google Search Console
2. **Verify ownership** of your website
3. **Submit sitemap**: `yourwebsite.com/sitemap.xml`
4. **Monitor performance** regularly

### Local SEO

**Update these in `src/config/seo.js`**:

```javascript
keywords: {
  primary: [
    "your-service your-city",    // 👈 Main service + location
    "your-specialty-service",    // 👈 What you specialize in
  ],
  local: [
    "your-service near me",      // 👈 Local search terms
    "local your-service",
    "your-city your-service"
  ]
}
```

## 📱 Social Media Integration

### Open Graph Setup

**File to edit**: `src/config/seo.js`

```javascript
social: {
  og: {
    siteName: "YOUR_BUSINESS_NAME",
    image: "/images/your-og-image.jpg",    // 👈 Create 1200x630px image
  },
  twitter: {
    site: "@your_twitter_handle",          // 👈 Your Twitter
  },
  profiles: [
    "https://www.facebook.com/yourpage",   // 👈 Your social profiles
    "https://www.instagram.com/yourpage",
    "https://www.linkedin.com/company/yourcompany"
  ]
}
```

## 🔧 Development vs Production

### Development Mode
```bash
npm run dev  # Hot reload, debugging enabled
```

### Production Build
```bash
npm run build  # Optimized, minified build
```

### Environment Variables

Create `.env` file in project root:
```
VITE_API_URL=http://localhost:5000  # Development
# VITE_API_URL=https://yourapi.com  # Production
```

## 📋 Quick Setup Checklist

### Essential Updates (Required)
- [ ] Business name in `business.js`
- [ ] Address in `business.js`
- [ ] Phone number in `business.js`
- [ ] Email in `business.js`
- [ ] Service areas in `business.js`
- [ ] SEO info in `seo.js` (must match business.js)
- [ ] Email configuration in `backend/config/config.py`

### Recommended Updates
- [ ] Page titles in `seo.js`
- [ ] Meta descriptions in `seo.js`
- [ ] Keywords in `seo.js`
- [ ] Social media profiles in `seo.js`
- [ ] Google My Business setup
- [ ] Custom logo/branding
- [ ] Professional photos

### Optional Enhancements
- [ ] Google Maps API key
- [ ] Advanced analytics
- [ ] Custom domain
- [ ] SSL certificate
- [ ] CDN setup

---

*Need help? Check the main DOCUMENTATION.md file or contact your developer.*
