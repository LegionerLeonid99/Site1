/**
 * SEO COMPOSABLE
 * 
 * Vue 3 composable for managing SEO meta tags dynamically
 * This automatically updates page titles, descriptions, and meta tags
 */

import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { seoConfig, generateMetaTags, generateStructuredData } from '../config/seo.js'

export function useSEO(pageKey = 'home', customMeta = {}) {
  const route = useRoute()
  const currentPageKey = ref(pageKey)
  
  // Generate meta tags for current page
  const getMetaData = (key = currentPageKey.value) => {
    const defaultMeta = generateMetaTags(key)
    return { ...defaultMeta, ...customMeta }
  }

  // Update document title
  const updateTitle = (title) => {
    if (typeof document !== 'undefined') {
      document.title = title
    }
  }

  // Update meta tag
  const updateMetaTag = (name, content, property = false) => {
    if (typeof document === 'undefined') return
    
    const selector = property ? `meta[property="${name}"]` : `meta[name="${name}"]`
    let meta = document.querySelector(selector)
    
    if (!meta) {
      meta = document.createElement('meta')
      if (property) {
        meta.setAttribute('property', name)
      } else {
        meta.setAttribute('name', name)
      }
      document.head.appendChild(meta)
    }
    
    meta.setAttribute('content', content)
  }

  // Update link tag (for canonical, etc.)
  const updateLinkTag = (rel, href) => {
    if (typeof document === 'undefined') return
    
    let link = document.querySelector(`link[rel="${rel}"]`)
    
    if (!link) {
      link = document.createElement('link')
      link.setAttribute('rel', rel)
      document.head.appendChild(link)
    }
    
    link.setAttribute('href', href)
  }

  // Add structured data JSON-LD
  const addStructuredData = () => {
    if (typeof document === 'undefined') return
    
    // Remove existing structured data
    const existing = document.querySelector('script[type="application/ld+json"]')
    if (existing) {
      existing.remove()
    }
    
    // Add new structured data
    const script = document.createElement('script')
    script.type = 'application/ld+json'
    script.textContent = generateStructuredData()
    document.head.appendChild(script)
  }

  // Apply all SEO meta tags
  const applySEO = (key = currentPageKey.value, custom = {}) => {
    const meta = getMetaData(key)
    const finalMeta = { ...meta, ...custom }
    
    // Update title
    updateTitle(finalMeta.title)
    
    // Update basic meta tags
    updateMetaTag('description', finalMeta.description)
    updateMetaTag('keywords', finalMeta.keywords)
    updateMetaTag('robots', seoConfig.technical.robots)
    updateMetaTag('language', seoConfig.technical.language)
    
    // Update Open Graph tags
    updateMetaTag('og:title', finalMeta.ogTitle, true)
    updateMetaTag('og:description', finalMeta.ogDescription, true)
    updateMetaTag('og:url', finalMeta.ogUrl, true)
    updateMetaTag('og:type', seoConfig.social.og.type, true)
    updateMetaTag('og:site_name', seoConfig.social.og.siteName, true)
    updateMetaTag('og:locale', seoConfig.social.og.locale, true)
    updateMetaTag('og:image', `${seoConfig.business.contact.website}${seoConfig.social.og.image}`, true)
    updateMetaTag('og:image:alt', seoConfig.social.og.imageAlt, true)
    
    // Update Twitter tags
    updateMetaTag('twitter:card', seoConfig.social.twitter.card)
    updateMetaTag('twitter:site', seoConfig.social.twitter.site)
    updateMetaTag('twitter:creator', seoConfig.social.twitter.creator)
    updateMetaTag('twitter:title', finalMeta.twitterTitle)
    updateMetaTag('twitter:description', finalMeta.twitterDescription)
    updateMetaTag('twitter:image', `${seoConfig.business.contact.website}${seoConfig.social.og.image}`)
    
    // Update canonical link
    updateLinkTag('canonical', finalMeta.canonical)
    
    // Add structured data
    addStructuredData()
  }

  // Initialize SEO on mount
  onMounted(() => {
    applySEO()
  })

  // Watch for route changes
  watch(() => route.path, () => {
    // Determine page key from route
    const pathToPageKey = {
      '/': 'home',
      '/services/appliances': 'appliances',
      '/services/coffee-machines': 'coffeeMachines',
      '/services/dishwashers': 'dishwashers',
      '/services/washing-machines': 'washingMachines'
    }
    
    const newPageKey = pathToPageKey[route.path] || 'home'
    currentPageKey.value = newPageKey
    applySEO(newPageKey)
  })

  // Return functions for manual control
  return {
    currentPageKey,
    applySEO,
    updateTitle,
    updateMetaTag,
    updateLinkTag,
    getMetaData
  }
}

/**
 * SERVICE-SPECIFIC SEO DATA
 * 
 * Enhanced SEO data for specific services
 */
export const serviceSEO = {
  appliances: {
    title: "General Appliance Repair London | FixIt Appliances",
    description: "Expert repair for all household appliances in London. Certified technicians, same-day service, warranty included. Book your appliance repair today!",
    keywords: "appliance repair London, household appliances, certified technicians, warranty repair, same day service",
    schema: {
      "@type": "Service",
      name: "General Appliance Repair",
      description: "Professional repair service for all household appliances",
      serviceType: "Appliance Repair",
      areaServed: "London, UK"
    }
  },
  
  coffeeMachines: {
    title: "Coffee Machine Repair London | Espresso & Bean-to-Cup Specialists",
    description: "Professional coffee machine repair in London. We service all brands: Breville, De'Longhi, Sage, Jura. Fast diagnosis, quality parts, expert service.",
    keywords: "coffee machine repair London, espresso machine repair, Breville repair, De'Longhi service, Sage coffee machine, Jura repair",
    schema: {
      "@type": "Service",
      name: "Coffee Machine Repair",
      description: "Specialized repair service for all coffee machine brands",
      serviceType: "Coffee Machine Repair",
      areaServed: "London, UK"
    }
  },
  
  dishwashers: {
    title: "Dishwasher Repair London | All Brands Serviced | FixIt Appliances",
    description: "Expert dishwasher repair in London. We fix all brands: Bosch, Miele, AEG, Hotpoint. Not draining? Not cleaning? We'll fix it fast!",
    keywords: "dishwasher repair London, Bosch dishwasher repair, Miele dishwasher service, dishwasher not draining, dishwasher not cleaning",
    schema: {
      "@type": "Service",
      name: "Dishwasher Repair",
      description: "Professional dishwasher repair and maintenance service",
      serviceType: "Dishwasher Repair",
      areaServed: "London, UK"
    }
  },
  
  washingMachines: {
    title: "Washing Machine Repair London | Front & Top Loading Specialists",
    description: "Professional washing machine repair in London. All brands serviced: Samsung, LG, Hotpoint, Bosch. Not spinning? Leaking? Call today!",
    keywords: "washing machine repair London, Samsung washing machine repair, LG washing machine service, washing machine not spinning, washing machine leaking",
    schema: {
      "@type": "Service",
      name: "Washing Machine Repair", 
      description: "Expert washing machine repair for all brands and models",
      serviceType: "Washing Machine Repair",
      areaServed: "London, UK"
    }
  }
}
