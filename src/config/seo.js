/**
 * SEO CONFIGURATION
 * 
 * ⚠️  MAINTENERS: UPDATE THIS FILE TO IMPROVE SEARCH ENGINE OPTIMIZATION
 * 
 * This file contains all SEO-related information that helps your website
 * rank better in search engines like Google, Bing, and Yahoo.
 */

export const seoConfig = {
  // 🎯 BUSINESS SEO INFORMATION
  business: {
    name: "O-TECH HOME SERVICES",                              // ← CHANGE THIS: Your business name
    legalName: "O-TECH HOME SERVICES LTD",                     // ← CHANGE THIS: Legal business name
    description: "Expert appliance repair services for coffee machines, dishwashers, washing machines, hobs, air conditioners, and all electrical appliances. Fast, reliable, and affordable.",
    
    // 📍 LOCAL SEO - Critical for local businesses
    location: {
      streetAddress: "123 Repair Street",        // ← CHANGE THIS: Your street address
      city: "London",                           // ← CHANGE THIS: Your city
      region: "Greater London",                 // ← CHANGE THIS: Your region/state
      postalCode: "SW1A 1AA",                  // ← CHANGE THIS: Your postcode
      country: "GB",                           // ← CHANGE THIS: Your country code (GB, US, etc.)
      coordinates: {
        latitude: "51.5074",                   // ← CHANGE THIS: Your latitude
        longitude: "-0.1278"                   // ← CHANGE THIS: Your longitude
      }
    },
    
    // 📞 CONTACT SEO
    contact: {
      phone: "+44 7551 656880",                // ← CHANGE THIS: Your phone (with country code)
      email: "otechhomeservices@gmail.com",               // ← CHANGE THIS: Your business email
      website: "https://otechhomeservices.co.uk"       // ← Your website URL (no www)
    },
    
    // 🕒 OPERATING HOURS (for Google My Business integration)
    hours: [
      { day: "Monday", open: "08:30", close: "15:30" },
      { day: "Tuesday", open: "08:30", close: "15:30" },
      { day: "Wednesday", open: "08:30", close: "15:30" },
      { day: "Thursday", open: "08:30", close: "15:30" },
      { day: "Friday", open: "08:30", close: "15:30" },
      { day: "Saturday", open: "08:30", close: "15:30" },
      { day: "Sunday", open: null, close: null } // Closed
    ]
  },

  // 🎯 KEYWORD STRATEGY
  keywords: {
    // 🔥 PRIMARY KEYWORDS (most important)
    primary: [
      "appliance repair London",               // ← CHANGE THIS: Your main service + location
      "washing machine repair",
      "dishwasher repair",
      "coffee machine repair"
    ],
    
    // 🎯 SECONDARY KEYWORDS
    secondary: [
      "kitchen appliance repair",
      "electrical appliance service",
      "hob repair London",
      "commercial appliance repair",
      "appliance installation London",
      "same day appliance repair"
    ],
    
    // 📍 LOCAL KEYWORDS
    local: [
      "appliance repair near me",
      "local appliance repair",
      "London appliance technician",
      "emergency appliance repair London"
    ]
  },

  // 📄 PAGE-SPECIFIC SEO
  pages: {
    home: {
      title: "O-TECH HOME SERVICES - Expert Family Appliance Repair Service London",
      description: "Professional appliance repair services in London. We fix washing machines, dishwashers, coffee machines, hobs & more. Trusted family business. Call now!",
      keywords: "appliance repair London, washing machine repair, dishwasher repair, coffee machine repair, family business"
    },
    
    appliances: {
      title: "General Appliance Repair London | O-TECH HOME SERVICES",
      description: "Expert repair for all household appliances in London. Certified technicians, same-day service, warranty included. Book your appliance repair today!",
      keywords: "appliance repair, household appliances, certified technicians, warranty repair"
    },
    
    coffeeMachines: {
      title: "Coffee Machine Repair London | Espresso & Bean-to-Cup Specialists",
      description: "Professional coffee machine repair in London. We service all brands: Breville, De'Longhi, Sage, Jura. Fast diagnosis, quality parts, expert service.",
      keywords: "coffee machine repair, espresso machine repair, Breville repair, De'Longhi service"
    },
    
    dishwashers: {
      title: "Dishwasher Repair London | All Brands Serviced | O-TECH HOME SERVICES",
      description: "Expert dishwasher repair in London. We fix all brands: Bosch, Miele, AEG, Hotpoint. Not draining? Not cleaning? We'll fix it fast!",
      keywords: "dishwasher repair, Bosch dishwasher, Miele service, dishwasher not draining"
    },
    
    washingMachines: {
      title: "Washing Machine Repair London | Front & Top Loading Specialists",
      description: "Professional washing machine repair in London. All brands serviced: Samsung, LG, Hotpoint, Bosch. Not spinning? Leaking? Call today!",
      keywords: "washing machine repair, Samsung washing machine, LG repair, washing machine not spinning"
    },
    
    hobs: {
      title: "Hob Repair London | Gas, Electric & Induction Specialists | O-TECH HOME SERVICES",
      description: "Expert hob repair in London. Gas, electric, and induction hobs serviced. All brands: Bosch, AEG, Neff. Not heating? Call our certified engineers!",
      keywords: "hob repair London, gas hob repair, electric hob repair, induction hob service"
    },
    
    airConditioners: {
      title: "Air Conditioner Repair London | AC Service & Installation",
      description: "Professional air conditioning repair in London. Split systems, window units, portable AC units. Not cooling? Strange noises? We fix all AC problems!",
      keywords: "air conditioner repair, AC repair London, split system repair, window AC service, cooling problems"
    },
    
    kitchenVentilators: {
      title: "Kitchen Ventilator Repair London | Extractor Fan & Hood Service",
      description: "Expert kitchen ventilator and extractor fan repair in London. Not extracting? Noisy fan? We service all brands and types of kitchen ventilation systems.",
      keywords: "kitchen ventilator repair, extractor fan repair London, cooker hood repair, kitchen ventilation service"
    },
    
    commercialEquipment: {
      title: "Commercial Appliance Repair London | Restaurant Equipment Service",
      description: "Expert commercial appliance repair in London. Restaurant equipment, industrial washing machines, commercial ovens. Fast business service!",
      keywords: "commercial appliance repair, restaurant equipment service, industrial appliance repair"
    },
    
    allElectrical: {
      title: "Electrical Appliance Repair London | All Domestic & Commercial Equipment",
      description: "Complete electrical appliance repair in London. Domestic and commercial equipment serviced. Qualified electricians, all brands, competitive rates.",
      keywords: "electrical appliance repair, domestic appliance service, commercial electrical repair"
    },
    
    faq: {
      title: "Appliance Repair FAQ | Common Questions Answered | O-TECH HOME SERVICES",
      description: "Frequently asked questions about appliance repair in London. Get answers about costs, warranties, service times, and common appliance problems.",
      keywords: "appliance repair FAQ, repair costs, appliance warranty, common appliance problems"
    }
  },

  // 📊 STRUCTURED DATA (Schema.org)
  structuredData: {
    organization: {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "@id": "https://otechhomeservices.co.uk/#organization",
      name: "O-TECH HOME SERVICES",
      legalName: "O-TECH HOME SERVICES LTD",
      description: "Professional appliance repair services",
      url: "https://otechhomeservices.co.uk",
      telephone: "+447398933824",
      email: "otechhomeservices@gmail.com",
      
      address: {
        "@type": "PostalAddress",
        streetAddress: "206 Maritime House, Greens End",
        addressLocality: "London",
        addressRegion: "Greater London", 
        postalCode: "SE18 6HB",
        addressCountry: "GB"
      },
      
      geo: {
        "@type": "GeoCoordinates",
        latitude: "51.5074",
        longitude: "-0.1278"
      },
      
      openingHoursSpecification: [
        {
          "@type": "OpeningHoursSpecification",
          dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          opens: "08:00",
          closes: "18:00"
        },
        {
          "@type": "OpeningHoursSpecification", 
          dayOfWeek: "Saturday",
          opens: "09:00",
          closes: "16:00"
        }
      ],
      
      serviceArea: {
        "@type": "GeoCircle",
        geoMidpoint: {
          "@type": "GeoCoordinates",
          latitude: "51.5074",
          longitude: "-0.1278"
        },
        geoRadius: "25000" // 25km radius
      },
      
      hasOfferCatalog: {
        "@type": "OfferCatalog",
        name: "Appliance Repair Services",
        itemListElement: [
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "Service",
              name: "Washing Machine Repair",
              description: "Professional washing machine repair service"
            }
          },
          {
            "@type": "Offer", 
            itemOffered: {
              "@type": "Service",
              name: "Dishwasher Repair",
              description: "Expert dishwasher repair and maintenance"
            }
          },
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "Service", 
              name: "Coffee Machine Repair",
              description: "Specialized coffee machine repair service"
            }
          }
        ]
      }
    }
  },

  // 🌐 SOCIAL MEDIA & OPEN GRAPH
  social: {
    // Open Graph for Facebook, LinkedIn, etc.
    og: {
      siteName: "O-TECH HOME SERVICES",
      type: "website",
      locale: "en_GB",
      image: "/images/og-image.jpg",           // ← ADD THIS: Create a 1200x630px image
      imageAlt: "O-TECH HOME SERVICES - Professional Appliance Repair London"
    },
    
    // Twitter/X Cards
    twitter: {
      card: "summary_large_image",
      site: "@otechhomeservices",               // ← CHANGE THIS: Your Twitter handle
      creator: "@otechhomeservices"
    },
    
    // Social Media Profiles (helps with entity recognition)
    profiles: [
      "https://www.facebook.com/otechhomeservices",    // ← ADD THIS: Your Facebook page
      "https://www.twitter.com/otechhomeservices",     // ← ADD THIS: Your Twitter profile
      "https://www.linkedin.com/company/otechhomeservices", // ← ADD THIS: Your LinkedIn
      "https://www.instagram.com/otechhomeservices"    // ← ADD THIS: Your Instagram
    ]
  },

  // 🎯 TECHNICAL SEO
  technical: {
    // Canonical URLs (prevents duplicate content)
    canonical: "https://otechhomeservices.co.uk",
    
    // Robots meta
    robots: "index, follow",
    
    // Language and region
    language: "en-GB",
    
    // Performance hints
    preload: [
      "/fonts/main-font.woff2",               // ← ADD THIS: Preload critical fonts
      "/images/hero-bg.jpg"                   // ← ADD THIS: Preload critical images
    ]
  }
}

/**
 * 📝 MAINTENANCE INSTRUCTIONS:
 * 
 * 🔍 SEO CHECKLIST:
 * 
 * 1. ✅ Update business information above
 * 2. ✅ Add your Google My Business listing
 * 3. ✅ Create social media profiles
 * 4. ✅ Set up Google Analytics & Search Console
 * 5. ✅ Submit XML sitemap
 * 6. ✅ Optimize page loading speed
 * 7. ✅ Add customer reviews/testimonials
 * 8. ✅ Create location-specific landing pages
 * 9. ✅ Build local citations (directories)
 * 10. ✅ Get customer reviews on Google
 * 
 * 🎯 PRIORITY ACTIONS:
 * 
 * HIGH PRIORITY:
 * - Update all business details above
 * - Set up Google My Business
 * - Add structured data to pages
 * - Optimize page titles and descriptions
 * 
 * MEDIUM PRIORITY:
 * - Create social media profiles
 * - Set up review collection system
 * - Add blog for content marketing
 * - Optimize images with alt text
 * 
 * LOW PRIORITY:
 * - Advanced schema markup
 * - Multilingual SEO
 * - Voice search optimization
 */

// 🛠️ UTILITY FUNCTIONS
export const generateMetaTags = (pageKey) => {
  const page = seoConfig.pages[pageKey] || seoConfig.pages.home
  const business = seoConfig.business
  
  return {
    title: page.title,
    description: page.description,
    keywords: page.keywords,
    canonical: `${business.contact.website}${pageKey === 'home' ? '' : '/' + pageKey}`,
    ogTitle: page.title,
    ogDescription: page.description,
    ogUrl: `${business.contact.website}${pageKey === 'home' ? '' : '/' + pageKey}`,
    twitterTitle: page.title,
    twitterDescription: page.description
  }
}

export const generateStructuredData = () => {
  return JSON.stringify(seoConfig.structuredData.organization, null, 2)
}
