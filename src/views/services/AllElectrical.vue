<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'
import { apiFetch } from '../../config/api.js'

// 🎯 SEO Setup for All Electrical Page
useSEO({ page: 'allElectrical' })

const electricalServices = ref([
  {
    icon: '⚡',
    name: 'Electrical Appliance Repair',
    description: 'Complete electrical appliance diagnostics and repair',
    services: ['Circuit board repair', 'Wiring diagnosis', 'Motor replacement', 'Control panel fixes']
  },
  {
    icon: '🔌',
    name: 'Power & Connection Issues',
    description: 'Electrical connection and power supply problems',
    services: ['Outlet installation', 'Voltage issues', 'Circuit breaker problems', 'GFCI repairs']
  },
  {
    icon: '💡',
    name: 'Control Systems',
    description: 'Digital controls and smart appliance electronics',
    services: ['Touch screen repair', 'WiFi connectivity', 'Sensor calibration', 'Software updates']
  },
  {
    icon: '🔧',
    name: 'Motor & Mechanical',
    description: 'Electric motors and mechanical electrical components',
    services: ['Motor rewinding', 'Bearing replacement', 'Belt adjustments', 'Gear box repair']
  }
])

const initialFormState = {
  name: '',
  email: '',
  phone: '',
  applianceType: '',
  brand: '',
  issue: ''
}

const contactForm = ref({ ...initialFormState })

const resetForm = () => {
  contactForm.value = { ...initialFormState }
}

const submitForm = async () => {
  const button = document.querySelector('#all-electrical-form button[type="submit"]')

  if (button) {
    button.classList.add('professional-loading')
    button.textContent = 'Sending...'
  }
  
  try {
    const payload = {
      name: contactForm.value.name,
      email: contactForm.value.email,
      phone: contactForm.value.phone,
      service: 'All Electrical Appliance Repair',
      message: contactForm.value.issue,
      appliance: contactForm.value.applianceType,
      brand: contactForm.value.brand,
      issue: contactForm.value.issue
    }

    const response = await apiFetch('/contact/enquiry', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })

    const result = await response.json().catch(() => null)

    if (response.ok && result?.success) {
      alert('🎉 Thank you! We will contact you soon about your electrical appliance repair.')
      resetForm()
    } else {
      const message = result?.message ?? `Request failed with status ${response.status}`
      throw new Error(message)
    }
  } catch (error) {
    console.error('Electrical contact form error:', error)
    alert(`❌ Failed to send message. ${error?.message ?? 'Please try again.'}`)
  } finally {
    if (button) {
      button.classList.remove('professional-loading')
      button.innerHTML = 'Request Service <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
    }
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
            All Electrical Appliance Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Complete electrical appliance repair service. From circuits to controls, we fix it all!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Get Electrical Service
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Electrical Services Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Electrical Services We Provide</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Comprehensive electrical appliance repair and maintenance
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(service, index) in electricalServices" :key="service.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ service.icon }}</div>
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ service.name }}</h3>
            <p class="mt-2 text-gray-600 professional-text mb-4">{{ service.description }}</p>            <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="serviceItem in service.services" :key="serviceItem" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ serviceItem }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Safety Notice -->
    <section class="bg-red-50 py-12">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h3 class="text-2xl font-bold text-red-600 professional-subheading">⚠️ Electrical Safety Warning</h3>
          <p class="mt-4 text-red-700">
            Electrical work can be dangerous. Always call licensed professionals for electrical appliance repairs. 
            Never attempt DIY electrical repairs - it could result in injury, fire, or property damage.
          </p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Electrical Problems?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Our licensed electricians specialize in appliance electrical systems. Safe, professional service guaranteed.
            </p>
          </div>
          <div>
            <form id="all-electrical-form" @submit.prevent="submitForm" class="professional-card space-y-6" autocomplete="off">
              <h3 class="text-xl font-bold professional-subheading">Request Electrical Service</h3>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.name" type="text" required class="professional-input" placeholder="Your Name" autocomplete="name" />
                <input v-model="contactForm.email" type="email" required class="professional-input" placeholder="Email" autocomplete="email" />
              </div>
              
              <input v-model="contactForm.phone" type="tel" required class="professional-input" placeholder="07XXX XXXXXX" autocomplete="tel" />
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <select v-model="contactForm.applianceType" required class="professional-input" autocomplete="off">
                  <option value="">Appliance Type...</option>
                  <option value="refrigerator">Refrigerator</option>
                  <option value="washer">Washing Machine</option>
                  <option value="dryer">Dryer</option>
                  <option value="oven">Oven/Range</option>
                  <option value="dishwasher">Dishwasher</option>
                  <option value="other">Other Electrical</option>
                </select>
                <input v-model="contactForm.brand" type="text" class="professional-input" placeholder="Brand" autocomplete="off" />
              </div>
              
              <textarea v-model="contactForm.issue" required class="professional-input" rows="3" placeholder="Describe the electrical issue..." autocomplete="off"></textarea>
              
              <button type="submit" class="professional-btn professional-btn-primary w-full py-3 group">
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
