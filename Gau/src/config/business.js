/**
 * BUSINESS CONFIGURATION
 * 
 * ⚠️  MAINTAINERS: UPDATE THIS FILE TO CHANGE BUSINESS INFORMATION
 * 
 * This file contains all business-related information that appears on the website.
 * When you need to update the business address, contact info, or location,
 * modify the values in this file and the changes will reflect across the entire website.
 */

export const businessConfig = {
  // 📍 BUSINESS LOCATION INFORMATION
  // Update these values to change the business address throughout the website
  location: {
    // 🏢 BUSINESS ADDRESS - Update this with your actual business address
    address: {
      street: "206 Maritime House",           // ← CHANGE THIS: Street address
      city: "London",                        // ← CHANGE THIS: City name
      postcode: "SE18 6HB",                 // ← CHANGE THIS: Postcode
      country: "United Kingdom"             // ← CHANGE THIS: Country
    },
    
    // 🗺️ MAP COORDINATES - Update these to center the map on your business location
    // To find coordinates: Go to Google Maps → Right-click your location → Copy coordinates
    coordinates: {
      latitude: 51.5074,                    // ← CHANGE THIS: Your business latitude
      longitude: -0.1278                    // ← CHANGE THIS: Your business longitude
    },
    
    // 📱 CONTACT INFORMATION - Update with your real business contact details
    contact: {
      phone: "07551656880",                 // ← CHANGE THIS: Your business phone
      email: "darwinosadcenco@gmail.com",   // ← CHANGE THIS: Your business email
      website: "www.fixitappliances.co.uk" // ← CHANGE THIS: Your website URL
    }
  },

  // 🏢 BUSINESS DETAILS
  business: {
    name: "FixIt Appliances",               // ← CHANGE THIS: Your business name
    description: "Professional appliance repair services in London and surrounding areas",
    tagline: "Fast, Reliable, Professional",
    
    // 🕒 BUSINESS HOURS - Update with your actual operating hours
    hours: {
      monday: "8:00 AM - 6:00 PM",
      tuesday: "8:00 AM - 6:00 PM", 
      wednesday: "8:00 AM - 6:00 PM",
      thursday: "8:00 AM - 6:00 PM",
      friday: "8:00 AM - 6:00 PM",
      saturday: "9:00 AM - 4:00 PM",
      sunday: "Closed"
    },
    
    // 📋 SERVICE AREAS - Update with areas you serve
    serviceAreas: [
      "Central London",                     // ← CHANGE THIS: Add your service areas
      "North London",
      "South London", 
      "East London",
      "West London",
      "Greater London"
    ]
  },

  // 🗺️ MAP CONFIGURATION
  map: {
    // Google Maps embed parameters
    zoom: 15,                               // Map zoom level (10-20 recommended)
    mapType: "roadmap",                     // Map type: roadmap, satellite, hybrid, terrain
    
    // Map styling (you can customize these)
    height: "400px",                        // Map container height
    borderRadius: "12px",                   // Map corner radius
    
    // 🔑 GOOGLE MAPS API KEY - Add your Google Maps API key here for advanced features
    // To get an API key: https://developers.google.com/maps/documentation/embed/get-api-key
    apiKey: "YOUR_GOOGLE_MAPS_API_KEY_HERE" // ← CHANGE THIS: Add your Google Maps API key
  }
}

/**
 * 📝 MAINTENANCE INSTRUCTIONS:
 * 
 * 1. To update business address:
 *    - Modify the `location.address` object above
 *    - Update `location.coordinates` with new latitude/longitude
 * 
 * 2. To change contact information:
 *    - Update `location.contact` object
 * 
 * 3. To modify business hours:
 *    - Update the `business.hours` object
 * 
 * 4. To change service areas:
 *    - Modify the `business.serviceAreas` array
 * 
 * 5. To enable advanced map features:
 *    - Get a Google Maps API key
 *    - Replace "YOUR_GOOGLE_MAPS_API_KEY_HERE" with your actual API key
 * 
 * ⚠️  Remember to restart your development server after making changes!
 */

// 🎯 UTILITY FUNCTIONS FOR COMPONENTS
export const getFullAddress = () => {
  const addr = businessConfig.location.address
  return `${addr.street}, ${addr.city}, ${addr.postcode}, ${addr.country}`
}

export const getGoogleMapsUrl = () => {
  const { latitude, longitude } = businessConfig.location.coordinates
  return `https://www.google.com/maps?q=${latitude},${longitude}`
}

export const getGoogleMapsEmbedUrl = () => {
  const addr = getFullAddress()
  const encodedAddress = encodeURIComponent(addr)
  return `https://www.google.com/maps/embed/v1/place?key=${businessConfig.map.apiKey}&q=${encodedAddress}&zoom=${businessConfig.map.zoom}&maptype=${businessConfig.map.mapType}`
}

// For fallback when no API key is provided
export const getGoogleMapsEmbedUrlBasic = () => {
  const addr = getFullAddress()
  const encodedAddress = encodeURIComponent(addr)
  return `https://maps.google.com/maps?q=${encodedAddress}&t=&z=${businessConfig.map.zoom}&ie=UTF8&iwloc=&output=embed`
}
