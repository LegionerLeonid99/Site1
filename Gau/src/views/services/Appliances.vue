<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'

// 🎯 SEO Setup for Appliances Page
useSEO({ page: 'appliances' })

// Appliance types and brands we service
const applianceTypes = ref([
  {
    icon: '❄️',
    name: 'Refrigerators',
    description: 'Complete refrigerator repair services for all major brands',
    services: ['Cooling issues', 'Ice maker repair', 'Seal replacement', 'Thermostat repair']
  },
  {
    icon: '🍳',
    name: 'Ovens & Ranges',
    description: 'Expert oven and range repair and maintenance',
    services: ['Temperature issues', 'Igniter replacement', 'Door repairs', 'Burner fixes']
  },
  {
    icon: '🌀',
    name: 'Microwaves',
    description: 'Professional microwave repair and installation',
    services: ['Not heating', 'Turntable issues', 'Door problems', 'Control panel repair']
  },
  {
    icon: '❄️',
    name: 'Freezers',
    description: 'Freezer repair and maintenance services',
    services: ['Temperature problems', 'Defrost issues', 'Seal replacement', 'Compressor repair']
  },
  {
    icon: '🔥',
    name: 'Dryers',
    description: 'Complete dryer repair and maintenance',
    services: ['Not heating', 'Lint buildup', 'Drum issues', 'Vent cleaning']
  },
  {
    icon: '🗑️',
    name: 'Garbage Disposals',
    description: 'Garbage disposal repair and installation',
    services: ['Jammed disposal', 'Leaks', 'Strange noises', 'Installation']
  }
])

const supportedBrands = ref([
  'Whirlpool', 'GE', 'Samsung', 'LG', 'Maytag', 'Frigidaire', 'KitchenAid', 'Bosch',
  'Electrolux', 'Amana', 'Kenmore', 'Sub-Zero', 'Viking', 'Thermador', 'Miele'
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  appliance: '',
  brand: '',
  issue: '',
  message: ''
})

const submitForm = async () => {
  // Add loading state
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  try {
    const response = await fetch('http://localhost:5000/api/contact/appliances', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contactForm.value)
    })
    
    const result = await response.json()
    
    if (result.success) {
      alert('🎉 Thank you for your inquiry! We will contact you soon about your appliance repair.')
      
      // Reset form
      contactForm.value = {
        name: '',
        email: '',
        phone: '',
        appliance: '',
        brand: '',
        issue: '',
        message: ''
      }
    } else {
      alert('❌ Failed to send message: ' + result.message)
    }
  } catch (error) {
    console.error('Error sending form:', error)
    alert('❌ Failed to send message. Please try again.')
  } finally {
    // Reset button
    button.classList.remove('professional-loading')
    button.innerHTML = 'Request Service <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
  }
}
</script>

<template>
  <Layout>
    <!-- Hero Section -->
    <section class="hero-gradient py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-4xl font-bold sm:text-6xl professional-heading text-white">
            General Appliance Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert repair services for all your home appliances. Fast, reliable, and affordable solutions.
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4 bg-white text-blue-600 hover:bg-gray-50">
              Get Free Quote
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Appliance Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Appliances We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Comprehensive repair services for all major home appliances
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(appliance, index) in applianceTypes" :key="appliance.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ appliance.icon }}</div>
            
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ appliance.name }}</h3>
            
            <p class="mt-2 text-gray-600 professional-text mb-4">
              {{ appliance.description }}
            </p>
              <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in appliance.services" :key="service" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ service }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Brands Section -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Brands We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Authorized service for all major appliance brands
          </p>
        </div>

        <div class="grid grid-cols-3 gap-4 md:grid-cols-5 lg:grid-cols-5">
          <div v-for="brand in supportedBrands" :key="brand" 
               class="professional-card text-center py-4">
            <p class="text-gray-700 font-medium">{{ brand }}</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <p class="text-gray-600">Don't see your brand? <strong>Contact us</strong> - we likely service it too!</p>
        </div>
      </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Why Choose Our Appliance Service?</h2>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🚀</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Same-Day Service</h3>
            <p class="mt-2 text-gray-600 professional-text">Most repairs completed the same day</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🛡️</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Parts Warranty</h3>
            <p class="mt-2 text-gray-600 professional-text">XX-day warranty on all parts and labor</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">👨‍🔧</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Certified Techs</h3>
            <p class="mt-2 text-gray-600 professional-text">Factory-trained technicians</p>
          </div>          <div class="professional-card text-center">
            <div class="service-icon mx-auto">�</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Fast Service</h3>
            <p class="mt-2 text-gray-600 professional-text">Quick response and same-day repairs</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Need Appliance Repair?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Get your appliances working like new again. Our expert technicians are ready to help.
            </p>            <div class="mt-8 space-y-6">
              <div class="flex items-center gap-4">
                <div class="feature-icon">�</div>
                <div>
                  <h3 class="font-bold professional-subheading">Contact Us</h3>
                  <p class="text-gray-600">Use our contact form below</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">⚡</div>
                <div>
                  <h3 class="font-bold professional-subheading">Emergency Service</h3>
                  <p class="text-gray-600">24/7 emergency repairs available</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">🕐</div>
                <div>
                  <h3 class="font-bold professional-subheading">Service Hours</h3>
                  <p class="text-gray-600">Mon-Fri: 8am-6pm, Sat: 9am-4pm</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <form @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Service</h3>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label for="name" class="block text-sm font-medium text-gray-700 mb-2">Your Name</label>
                  <input
                    v-model="contactForm.name"
                    type="text"
                    id="name"
                    required
                    class="professional-input"
                    placeholder="Enter your name"
                  />
                </div>

                <div>
                  <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                  <input
                    v-model="contactForm.email"
                    type="email"
                    id="email"
                    required
                    class="professional-input"
                    placeholder="your.email@example.com"
                  />
                </div>
              </div>

              <div>
                <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
                <input
                  v-model="contactForm.phone"
                  type="tel"
                  id="phone"
                  required
                  class="professional-input"
                  placeholder="(555) 123-4567"
                />
              </div>

              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label for="appliance" class="block text-sm font-medium text-gray-700 mb-2">Appliance Type</label>
                  <select
                    v-model="contactForm.appliance"
                    id="appliance"
                    required
                    class="professional-input"
                  >
                    <option value="">Select appliance...</option>
                    <option value="refrigerator">Refrigerator</option>
                    <option value="oven">Oven/Range</option>
                    <option value="microwave">Microwave</option>
                    <option value="freezer">Freezer</option>
                    <option value="dryer">Dryer</option>
                    <option value="disposal">Garbage Disposal</option>
                    <option value="other">Other</option>
                  </select>
                </div>

                <div>
                  <label for="brand" class="block text-sm font-medium text-gray-700 mb-2">Brand</label>
                  <input
                    v-model="contactForm.brand"
                    type="text"
                    id="brand"
                    class="professional-input"
                    placeholder="e.g. Whirlpool, GE, Samsung"
                  />
                </div>
              </div>

              <div>
                <label for="issue" class="block text-sm font-medium text-gray-700 mb-2">What's the problem?</label>
                <textarea
                  v-model="contactForm.issue"
                  id="issue"
                  rows="3"
                  required
                  class="professional-input"
                  placeholder="Describe the issue with your appliance..."
                ></textarea>
              </div>

              <button
                type="submit"
                class="professional-btn professional-btn-primary w-full py-3 group"
              >
                Request Service
                <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </Layout>
</template>

<style scoped>
/* Component-specific styles */
</style>
