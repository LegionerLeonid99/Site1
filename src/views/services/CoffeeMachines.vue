<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'
import { apiFetch } from '../../config/api.js'

// 🎯 SEO Setup for Coffee Machines Page
useSEO('coffeeMachines')

// Coffee machine types and services
const coffeeMachineTypes = ref([
  {
    icon: '☕',
    name: 'Espresso Machines',
    description: 'Professional espresso machine repair and maintenance',
    services: ['Pump replacement', 'Boiler repair', 'Group head cleaning', 'Pressure adjustment']
  },
  {
    icon: '🚿',
    name: 'Automatic Coffee Makers',
    description: 'Drip coffee maker and automatic machine repair',
    services: ['Heating element', 'Water flow issues', 'Timer problems', 'Carafe replacement']
  },
  {
    icon: '🥛',
    name: 'Bean-to-Cup Machines',
    description: 'Complete bean-to-cup coffee machine service',
    services: ['Grinder calibration', 'Milk frother repair', 'Control panel issues', 'Internal cleaning']
  },
  {
    icon: '💨',
    name: 'Steam Machines',
    description: 'Commercial and home steam coffee machine repair',
    services: ['Steam wand repair', 'Pressure valve replacement', 'Thermostat repair', 'Descaling service']
  },
  {
    icon: '🔥',
    name: 'French Press & Manual',
    description: 'Manual coffee equipment repair and maintenance',
    services: ['Filter replacement', 'Handle repair', 'Glass replacement', 'Spring mechanism']
  },
  {
    icon: '🏢',
    name: 'Commercial Coffee Equipment',
    description: 'Professional commercial coffee machine service',
    services: ['Industrial repair', 'Preventive maintenance', 'Parts replacement', '24/7 service']
  }
])

const supportedBrands = ref([
  'Breville', 'De\'Longhi', 'Keurig', 'Nespresso', 'Cuisinart', 'Mr. Coffee', 'Hamilton Beach',
  'Jura', 'Saeco', 'Gaggia', 'Rancilio', 'La Marzocco', 'Nuova Simonelli', 'Rocket Espresso'
])

const commonIssues = ref([
  {
    issue: 'Not brewing or no water flow',
    solution: 'Usually caused by clogged water lines or pump failure. Our technicians can diagnose and repair quickly.'
  },
  {
    issue: 'Weak or bitter coffee',
    solution: 'Often due to incorrect grind settings or internal calibration. We can optimize your machine\'s performance.'
  },
  {
    issue: 'Steam wand not working',
    solution: 'Common in espresso machines. We repair steam valves, wands, and pressure systems.'
  },
  {
    issue: 'Machine not heating',
    solution: 'Heating element or thermostat issues. We replace faulty components with genuine parts.'
  },
  {
    issue: 'Leaking water',
    solution: 'Seal replacement and pressure system repair. We fix all types of leaks promptly.'
  },
  {
    issue: 'Error codes or display issues',
    solution: 'Control board diagnostics and repair. We handle all electronic component issues.'
  }
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  machineType: '',
  brand: '',
  model: '',
  issue: '',
  message: ''
})

const submitForm = async () => {
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  try {
  const response = await apiFetch('/contact/coffee-machines', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contactForm.value)
    })
    
    const result = await response.json()
    
    if (result.success) {
      alert('🎉 Thank you! We will contact you soon about your coffee machine repair.')
      
      contactForm.value = {
        name: '',
        email: '',
        phone: '',
        machineType: '',
        brand: '',
        model: '',
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
            Coffee Machine Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert repair services for all types of coffee machines. Get your daily brew back on track!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Fix My Coffee Machine
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Coffee Machine Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Coffee Machines We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            From home espresso machines to commercial coffee equipment
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(machine, index) in coffeeMachineTypes" :key="machine.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ machine.icon }}</div>
            
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ machine.name }}</h3>
            
            <p class="mt-2 text-gray-600 professional-text mb-4">
              {{ machine.description }}
            </p>
              <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in machine.services" :key="service" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ service }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Common Issues Section -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Common Coffee Machine Issues</h2>
          <p class="mt-6 text-gray-600 professional-text">
            We fix these problems and more - quickly and affordably
          </p>
        </div>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
          <div v-for="(item, index) in commonIssues" :key="item.issue" 
               :class="['professional-card', 'floating-card']"
               :style="{ animationDelay: index * 0.1 + 's' }">
            <h3 class="text-lg font-bold text-red-600 professional-subheading mb-2">
              {{ item.issue }}
            </h3>
            <p class="text-gray-600 professional-text">
              {{ item.solution }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Brands Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Coffee Machine Brands We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Authorized service for home and commercial coffee equipment
          </p>
        </div>

        <div class="grid grid-cols-2 gap-4 md:grid-cols-4 lg:grid-cols-7">
          <div v-for="brand in supportedBrands" :key="brand" 
               class="professional-card text-center py-4">
            <p class="text-gray-700 font-medium text-sm">{{ brand }}</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <p class="text-gray-600">Can't find your brand? <strong>Contact us</strong> - we service most coffee equipment!</p>
        </div>
      </div>
    </section>

    <!-- Service Features Section -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Why Choose Our Coffee Machine Service?</h2>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div class="professional-card text-center">
            <div class="service-icon mx-auto">⚡</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Fast Turnaround</h3>
            <p class="mt-2 text-gray-600 professional-text">Most repairs completed same day</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🔧</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Expert Technicians</h3>
            <p class="mt-2 text-gray-600 professional-text">Specialized in coffee equipment</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🛡️</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Parts Warranty</h3>
            <p class="mt-2 text-gray-600 professional-text">XX-day warranty on parts & labor</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🏠</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">On-Site Service</h3>
            <p class="mt-2 text-gray-600 professional-text">We come to your location</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Coffee Machine Not Working?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Don't let a broken coffee machine ruin your day. Our coffee equipment specialists are here to help.
            </p>

            <div class="mt-8 space-y-6">              <div class="flex items-center gap-4">
                <div class="feature-icon">�</div>
                <div>
                  <h3 class="font-bold professional-subheading">Contact Us</h3>
                  <p class="text-gray-600">Use our contact form below</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">⏰</div>
                <div>
                  <h3 class="font-bold professional-subheading">Rapid Response</h3>
                  <p class="text-gray-600">Same-day service for coffee emergencies</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">🔧</div>
                <div>
                  <h3 class="font-bold professional-subheading">Mobile Service</h3>
                  <p class="text-gray-600">We bring the shop to you</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <form @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Coffee Machine Service</h3>
              
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
                  placeholder="07XXX XXXXXX"
                />
              </div>

              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label for="machineType" class="block text-sm font-medium text-gray-700 mb-2">Machine Type</label>
                  <select
                    v-model="contactForm.machineType"
                    id="machineType"
                    required
                    class="professional-input"
                  >
                    <option value="">Select type...</option>
                    <option value="espresso">Espresso Machine</option>
                    <option value="automatic">Automatic Coffee Maker</option>
                    <option value="bean-to-cup">Bean-to-Cup</option>
                    <option value="steam">Steam Machine</option>
                    <option value="commercial">Commercial Equipment</option>
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
                    placeholder="e.g. Breville, Jura, Keurig"
                  />
                </div>
              </div>

              <div>
                <label for="model" class="block text-sm font-medium text-gray-700 mb-2">Model (if known)</label>
                <input
                  v-model="contactForm.model"
                  type="text"
                  id="model"
                  class="professional-input"
                  placeholder="Model number or name"
                />
              </div>

              <div>
                <label for="issue" class="block text-sm font-medium text-gray-700 mb-2">What's the problem?</label>
                <textarea
                  v-model="contactForm.issue"
                  id="issue"
                  rows="3"
                  required
                  class="professional-input"
                  placeholder="Describe the issue with your coffee machine..."
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
