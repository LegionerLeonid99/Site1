# 📍 Business Location & Contact Information Guide

## 🎯 Quick Update Instructions

**To change your business address and contact information, follow these simple steps:**

### Step 1: Update Business Configuration
Open the file: `src/config/business.js`

Look for the clearly marked sections with `← CHANGE THIS:` comments:

```javascript
// 🏢 BUSINESS ADDRESS - Update this with your actual business address
address: {
  street: "123 Repair Street",           // ← CHANGE THIS: Street address
  city: "London",                        // ← CHANGE THIS: City name
  postcode: "SW1A 1AA",                 // ← CHANGE THIS: Postcode
  country: "United Kingdom"             // ← CHANGE THIS: Country
},

// 🗺️ MAP COORDINATES - Update these to center the map on your business location
coordinates: {
  latitude: 51.5074,                    // ← CHANGE THIS: Your business latitude
  longitude: -0.1278                    // ← CHANGE THIS: Your business longitude
}
```

### Step 2: Find Your Coordinates
1. Go to [Google Maps](https://maps.google.com)
2. Search for your business address
3. Right-click on the exact location
4. Select "Copy coordinates" 
5. Paste the latitude and longitude values into the config file

### Step 3: Restart Development Server
After making changes:
```bash
# Stop the server (Ctrl+C)
# Then restart:
npm run dev
```

---

## 📋 What Gets Updated Automatically

When you update the business configuration, these sections will automatically reflect your changes:

### 🏠 Location Section (Home Page)
- **Business address display**
- **Interactive map centered on your location**
- **"Get Directions" link**
- **Contact information (phone, email, website)**
- **Business hours display**
- **Service areas list**

### 📧 Email Communications
The same contact information is used in:
- Email signatures
- Contact form responses
- Newsletter emails

### 🔍 SEO & Schema Markup
Your business information automatically updates:
- Local business schema markup
- Meta tags with location data
- Open Graph data for social sharing

---

## 🗺️ Map Configuration Options

### Basic Map (No API Key Required)
The default setup uses Google Maps embed without requiring an API key. This provides:
- ✅ Basic map display
- ✅ Location marker
- ✅ Zoom and pan functionality
- ✅ Mobile responsive

### Advanced Map Features (API Key Required)
To enable advanced features, get a Google Maps API key:

1. **Get API Key:**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project or select existing
   - Enable "Maps Embed API"
   - Create credentials (API Key)
   - Restrict API key to your domain

2. **Add API Key:**
   ```javascript
   // In src/config/business.js
   map: {
     apiKey: "YOUR_ACTUAL_API_KEY_HERE" // ← Replace with your key
   }
   ```

3. **Advanced Features Enabled:**
   - Custom map styling
   - Multiple markers
   - Custom info windows
   - Street View integration

---

## 🔧 Customization Options

### Map Appearance
```javascript
// In src/config/business.js
map: {
  zoom: 15,                    // 1-20 (higher = closer)
  mapType: "roadmap",          // roadmap, satellite, hybrid, terrain
  height: "400px",             // Any CSS height value
  borderRadius: "12px"         // Rounded corners
}
```

### Business Hours Format
```javascript
hours: {
  monday: "8:00 AM - 6:00 PM",     // Standard format
  tuesday: "8:00 AM - 6:00 PM",
  // ... or use 24-hour format:
  wednesday: "08:00 - 18:00",
  // ... or custom text:
  sunday: "Closed",
  // ... or emergency hours:
  saturday: "Emergency calls only"
}
```

### Service Areas
```javascript
serviceAreas: [
  "Central London",              // Add your coverage areas
  "North London",               // Remove areas you don't serve
  "South London",               // Add new areas as you expand
  "Within 25 miles of London"   // Or use distance-based descriptions
]
```

---

## 🚨 Troubleshooting

### Map Not Loading
1. **Check internet connection**
2. **Verify coordinates format** (decimal degrees, e.g., 51.5074)
3. **Ensure address is properly formatted**
4. **Check browser console for errors**

### Incorrect Location
1. **Double-check latitude/longitude values**
2. **Ensure coordinates are not swapped** (latitude first, longitude second)
3. **Use positive/negative values correctly:**
   - North = positive latitude
   - South = negative latitude  
   - East = positive longitude
   - West = negative longitude

### Address Not Found
1. **Verify address spelling and format**
2. **Include postcode/zip code**
3. **Try searching the address on Google Maps first**

---

## 📱 Mobile Responsiveness

The location section is fully responsive:
- **Desktop:** Side-by-side layout (info + map)
- **Tablet:** Stacked layout with full-width map
- **Mobile:** Single column, touch-friendly interface

---

## 🔄 Future Updates

When you move locations or change contact information:

1. **Update `src/config/business.js`** with new information
2. **Test the map loads correctly**
3. **Verify all contact links work**
4. **Update any printed materials** to match
5. **Notify customers** of the change

---

## 💡 Pro Tips

### SEO Benefits
- Consistent NAP (Name, Address, Phone) across all pages
- Schema markup for local search
- Google My Business integration ready

### User Experience
- Click-to-call phone numbers on mobile
- One-click directions via Google Maps
- Clear business hours prevent confusion

### Maintenance
- Single source of truth for all business info
- Easy updates without touching multiple files
- Automatic propagation across the entire website

---

**Need help?** Check the comments in `src/config/business.js` for detailed instructions, or refer to this guide for step-by-step directions.
