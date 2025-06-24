/**
 * SITEMAP GENERATOR
 * 
 * 🎯 MAINTAINERS: Run this script to generate sitemap.xml for better SEO
 * 
 * This script generates a sitemap.xml file that helps search engines
 * discover and index all pages on your website.
 * 
 * HOW TO USE:
 * 1. Update the baseUrl below to your actual website URL
 * 2. Add/remove pages as needed in the pages array
 * 3. Run: node generate-sitemap.js
 * 4. The sitemap.xml will be created in the public folder
 */

import { writeFileSync } from 'fs'
import { join } from 'path'

// 🌐 CHANGE THIS: Your website's base URL
const baseUrl = 'https://www.fixitappliances.co.uk'

// 📄 WEBSITE PAGES
const pages = [
  {
    url: '/',
    changefreq: 'weekly',
    priority: '1.0',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/appliances',
    changefreq: 'monthly',
    priority: '0.9',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/coffee-machines',
    changefreq: 'monthly',
    priority: '0.9',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/dishwashers',
    changefreq: 'monthly',
    priority: '0.9',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/washing-machines',
    changefreq: 'monthly',
    priority: '0.9',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/hobs',
    changefreq: 'monthly',
    priority: '0.8',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/kitchen-ventilators',
    changefreq: 'monthly',
    priority: '0.8',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/all-electrical',
    changefreq: 'monthly',
    priority: '0.8',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/services/commercial-equipment',
    changefreq: 'monthly',
    priority: '0.8',
    lastmod: new Date().toISOString().split('T')[0]
  },
  {
    url: '/faq',
    changefreq: 'monthly',
    priority: '0.7',
    lastmod: new Date().toISOString().split('T')[0]
  }
]

// 🔧 GENERATE SITEMAP XML
function generateSitemap() {
  const xmlHeader = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`

  const xmlUrls = pages.map(page => `
  <url>
    <loc>${baseUrl}${page.url}</loc>
    <lastmod>${page.lastmod}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`).join('')

  const xmlFooter = `
</urlset>`

  return xmlHeader + xmlUrls + xmlFooter
}

// 💾 SAVE SITEMAP
function saveSitemap() {
  try {
    const sitemapContent = generateSitemap()
    const sitemapPath = join(process.cwd(), 'public', 'sitemap.xml')
    
    writeFileSync(sitemapPath, sitemapContent, 'utf8')
    
    console.log('✅ Sitemap generated successfully!')
    console.log(`📁 Location: ${sitemapPath}`)
    console.log(`🌐 URL: ${baseUrl}/sitemap.xml`)
    console.log('')
    console.log('🔍 SEO TIP: Submit this sitemap to:')
    console.log('   • Google Search Console')
    console.log('   • Bing Webmaster Tools')
    console.log('   • Yandex Webmaster')
    
  } catch (error) {
    console.error('❌ Error generating sitemap:', error)
  }
}

// 🚀 RUN GENERATOR
saveSitemap()
