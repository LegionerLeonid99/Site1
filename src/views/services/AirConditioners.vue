<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'
import { apiFetch } from '../../config/api.js'

// 🎯 SEO Setup for Air Conditioners Page
useSEO({ page: 'airConditioners' })

const acTypes = ref([
  {
    icon: '❄️',
    name: 'Split Systems',
    description: 'Indoor and outdoor unit air conditioning repair',
    services: ['Refrigerant leaks', 'Compressor repair', 'Fan motor replacement', 'Thermostat issues']
  },
  {
    icon: '🏠',
    name: 'Window Units',
    description: 'Window-mounted air conditioning systems',
    services: ['Installation service', 'Cooling problems', 'Filter replacement', 'Electrical issues']
  },
  {
    icon: '🌀',
    name: 'Portable AC',
    description: 'Portable and mobile air conditioning units',
    services: ['Drainage issues', 'Cooling capacity', 'Remote controls', 'Hose connections']
  },
  {
    icon: '🏢',
    name: 'Commercial AC',
    description: 'Commercial air conditioning systems',
    services: ['Central systems', 'Ductwork repair', 'Maintenance contracts', 'Emergency service']
  }
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  acType: '',
  brand: '',
  issue: ''
})

const submitForm = async () => {
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  try {
  const response = await apiFetch('/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ...contactForm.value,
        service: 'air-conditioners',
        message: `AC Type: ${contactForm.value.acType}, Brand: ${contactForm.value.brand}, Issue: ${contactForm.value.issue}`
      })
    })
    
    const result = await response.json()
    
    if (result.success) {
      alert('🎉 Thank you! We will contact you soon about your air conditioner repair.')
      contactForm.value = { name: '', email: '', phone: '', acType: '', brand: '', issue: '' }
    } else {
      alert('❌ Failed to send message: ' + result.message)
    }
  } catch (error) {
    console.error('Error sending form:', error)
    alert('❌ Failed to send message. Please try again.')
  } finally {
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
            Air Conditioner Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert air conditioning repair, maintenance, and installation services. Stay cool!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Fix My AC
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- AC Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Air Conditioning Systems We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for all types of air conditioning systems
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(ac, index) in acTypes" :key="ac.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ ac.icon }}</div>
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ ac.name }}</h3>
            <p class="mt-2 text-gray-600 professional-text mb-4">{{ ac.description }}</p>
            <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in ac.services" :key="service" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ service }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Common Problems Section -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Common AC Problems We Fix</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Don't let AC problems leave you hot and bothered
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">🔥</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Not Cooling</h3>
                <p class="mt-1 text-gray-600 professional-text">Unit running but not producing cold air</p>
              </div>
            </div>
          </div>

          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">💧</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Water Leaks</h3>
                <p class="mt-1 text-gray-600 professional-text">Condensation or refrigerant leaking</p>
              </div>
            </div>
          </div>

          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">🔊</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Strange Noises</h3>
                <p class="mt-1 text-gray-600 professional-text">Grinding, squealing, or rattling sounds</p>
              </div>
            </div>
          </div>

          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">⚡</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Electrical Issues</h3>
                <p class="mt-1 text-gray-600 professional-text">Won't turn on or frequent tripping</p>
              </div>
            </div>
          </div>

          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">🌡️</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Thermostat Problems</h3>
                <p class="mt-1 text-gray-600 professional-text">Temperature control not working properly</p>
              </div>
            </div>
          </div>

          <div class="professional-card">
            <div class="flex items-start space-x-4">
              <div class="feature-icon">
                <div class="text-2xl">🧊</div>
              </div>
              <div>
                <h3 class="text-lg font-medium professional-subheading">Frozen Unit</h3>
                <p class="mt-1 text-gray-600 professional-text">Ice buildup on coils or outdoor unit</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Form Section -->
    <section id="contact" class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Get Your AC Fixed Today</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Fill out this form and we'll contact you within hours to schedule your air conditioner repair
          </p>
        </div>

        <div class="mx-auto max-w-xl">
          <form @submit.prevent="submitForm" class="professional-card space-y-6 p-8">
            <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div>
                <label for="name" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Your Name</label>
                <input
                  v-model="contactForm.name"
                  type="text"
                  id="name"
                  required
                  class="professional-input"
                  placeholder="Enter your name..."
                />
              </div>

              <div>
                <label for="phone" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Phone Number</label>
                <input
                  v-model="contactForm.phone"
                  type="tel"
                  id="phone"
                  required
                  class="professional-input"
                  placeholder="07XXX XXXXXX"
                />
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Email Address</label>
              <input
                v-model="contactForm.email"
                type="email"
                id="email"
                required
                class="professional-input"
                placeholder="your.email@example.com"
              />
            </div>

            <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div>
                <label for="acType" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">AC Type</label>
                <select
                  v-model="contactForm.acType"
                  id="acType"
                  required
                  class="professional-input"
                >
                  <option value="">Select AC type...</option>
                  <option value="split-system">Split System</option>
                  <option value="window-unit">Window Unit</option>
                  <option value="portable">Portable AC</option>
                  <option value="commercial">Commercial AC</option>
                  <option value="central">Central Air</option>
                  <option value="other">Other</option>
                </select>
              </div>

              <div>
                <label for="brand" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Brand</label>
                <input
                  v-model="contactForm.brand"
                  type="text"
                  id="brand"
                  class="professional-input"
                  placeholder="e.g. Daikin, LG, Samsung..."
                />
              </div>
            </div>

            <div>
              <label for="issue" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Describe the Problem</label>
              <textarea
                v-model="contactForm.issue"
                id="issue"
                rows="4"
                required
                class="professional-input"
                placeholder="Tell us what's wrong with your air conditioner..."
              ></textarea>
            </div>

            <button
              type="submit"
              class="professional-btn professional-btn-primary w-full text-lg py-4 group"
            >
              Request Service
              <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>
            </button>
          </form>
        </div>
      </div>
    </section>
  </Layout>
</template>
