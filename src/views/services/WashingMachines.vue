<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'
import { apiFetch } from '../../config/api.js'

// 🎯 SEO Setup for Washing Machines Page
useSEO('washingMachines')

// Washing machine types and services
const washingMachineTypes = ref([
  {
    icon: '🌀',
    name: 'Top Load Washers',
    description: 'Traditional top-loading washing machine repair',
    services: ['Agitator repair', 'Lid switch replacement', 'Water level sensor', 'Transmission issues']
  },
  {
    icon: '🚪',
    name: 'Front Load Washers',
    description: 'Front-loading washer repair and maintenance',
    services: ['Door seal replacement', 'Drain pump repair', 'Bearing replacement', 'Control board issues']
  },
  {
    icon: '📱',
    name: 'Smart Washers',
    description: 'WiFi-enabled and smart washing machine service',
    services: ['App connectivity', 'Software updates', 'Smart sensors', 'Remote diagnostics']
  },
  {
    icon: '⚡',
    name: 'High-Efficiency Washers',
    description: 'HE washer repair and optimization',
    services: ['HE detergent issues', 'Water efficiency', 'Spin cycle problems', 'Energy optimization']
  },
  {
    icon: '🏢',
    name: 'Commercial Washers',
    description: 'Laundromat and commercial washing machines',
    services: ['Coin mechanisms', 'Heavy-duty repairs', 'Industrial parts', 'High-volume service']
  },
  {
    icon: '🔄',
    name: 'Washer/Dryer Combos',
    description: 'All-in-one washer dryer combination units',
    services: ['Dual function repair', 'Ventilation issues', 'Condensation problems', 'Cycle optimization']
  }
])

const supportedBrands = ref([
  'Whirlpool', 'Maytag', 'GE', 'Samsung', 'LG', 'Frigidaire', 'Electrolux', 'Kenmore',
  'Bosch', 'Miele', 'Speed Queen', 'Amana', 'Hotpoint', 'Haier', 'Roper'
])

const commonIssues = ref([
  {
    issue: 'Won\'t start or turn on',
    solution: 'Usually electrical issues, door latch problems, or control board failure. We diagnose and fix power issues.',
    icon: '⚡'
  },
  {
    issue: 'Not spinning or agitating',
    solution: 'Motor coupling, belt, or transmission problems. We restore proper washing action.',
    icon: '🌀'
  },
  {
    issue: 'Water not filling or draining',
    solution: 'Water inlet valves, drain pumps, or hose blockages. We fix all water flow issues.',
    icon: '💧'
  },
  {
    issue: 'Excessive vibration or noise',
    solution: 'Unbalanced loads, worn bearings, or loose parts. We eliminate noise and vibration.',
    icon: '📳'
  },
  {
    issue: 'Leaking water',
    solution: 'Door seals, hose connections, or pump seals. We locate and repair all leaks.',
    icon: '🚰'
  },
  {
    issue: 'Clothes still dirty after wash',
    solution: 'Agitator problems, water temperature, or detergent issues. We optimize cleaning performance.',
    icon: '👕'
  }
])

const washingTips = ref([
  'Sort clothes by color and fabric type',
  'Don\'t overload the machine - clothes need room to move',
  'Use the correct amount of detergent for load size',
  'Clean the lint filter and door seals regularly',
  'Leave door open after use to air dry',
  'Check pockets for items before washing'
])

const initialFormState = {
  name: '',
  email: '',
  phone: '',
  washerType: '',
  brand: '',
  model: '',
  issue: '',
  when: ''
}

const contactForm = ref({ ...initialFormState })

const resetForm = () => {
  contactForm.value = { ...initialFormState }
}

const submitForm = async () => {
  const button = document.querySelector('#washing-machine-service-form button[type="submit"]')

  if (button) {
    button.classList.add('professional-loading')
    button.textContent = 'Sending...'
  }
  
  try {
    const payload = {
      name: contactForm.value.name,
      email: contactForm.value.email,
      phone: contactForm.value.phone,
      washerType: contactForm.value.washerType,
      brand: contactForm.value.brand,
      model: contactForm.value.model,
      issue: contactForm.value.issue,
      message: contactForm.value.issue,
      urgency: contactForm.value.when
    }

    const response = await apiFetch('/contact/washing-machines', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })

    const result = await response.json().catch(() => null)

    if (response.ok && result?.success) {
      alert('🎉 Thank you! We will contact you soon about your washing machine repair.')
      resetForm()
    } else {
      const message = result?.message ?? `Request failed with status ${response.status}`
      throw new Error(message)
    }
  } catch (error) {
    console.error('Washing machine contact form error:', error)
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
            Washing Machine Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert washing machine repair service. Get your laundry routine back on track!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Fix My Washer
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Washing Machine Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Washing Machines We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for all types of washing machines - top load, front load, and commercial
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(washer, index) in washingMachineTypes" :key="washer.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ washer.icon }}</div>
            
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ washer.name }}</h3>
            
            <p class="mt-2 text-gray-600 professional-text mb-4">
              {{ washer.description }}
            </p>
              <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in washer.services" :key="service" class="flex items-center">
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
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Common Washing Machine Problems</h2>
          <p class="mt-6 text-gray-600 professional-text">
            We fix these problems and get your laundry routine back to normal
          </p>
        </div>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(item, index) in commonIssues" :key="item.issue" 
               :class="['professional-card', 'floating-card']"
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="text-4xl mb-4">{{ item.icon }}</div>
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

    <!-- Tips Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Washing Machine Care Tips</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Extend your washing machine's life with proper care:
            </p>

            <ul class="mt-8 space-y-4">
              <li v-for="tip in washingTips" :key="tip" class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                <span class="text-gray-700">{{ tip }}</span>
              </li>
            </ul>
          </div>

          <div class="professional-card">
            <h3 class="text-xl font-bold professional-subheading mb-4">When to Call for Repair</h3>
            <p class="text-gray-600 professional-text mb-4">
              Don't ignore these warning signs:
            </p>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-center">
                <span class="text-red-500 mr-2">🚨</span>
                Strange noises during operation
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">🚨</span>
                Water pooling around machine
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">🚨</span>
                Clothes coming out still dirty
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">🚨</span>
                Excessive shaking or vibration
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">🚨</span>
                Won't start or complete cycles
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
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Washing Machine Brands We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Expert service for all major washing machine manufacturers
          </p>
        </div>

        <div class="grid grid-cols-3 gap-4 md:grid-cols-5 lg:grid-cols-5">
          <div v-for="brand in supportedBrands" :key="brand" 
               class="professional-card text-center py-4">
            <p class="text-gray-700 font-medium">{{ brand }}</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <p class="text-gray-600">Other brand? <strong>No problem!</strong> We service nearly all washing machine brands.</p>
        </div>
      </div>
    </section>

    <!-- Service Features -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Why Choose Our Washer Repair Service?</h2>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🚀</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Same-Day Service</h3>
            <p class="mt-2 text-gray-600 professional-text">Most repairs completed same day</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🛡️</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Warranty Coverage</h3>
            <p class="mt-2 text-gray-600 professional-text">XX-day parts and labor warranty</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">👨‍🔧</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Expert Technicians</h3>
            <p class="mt-2 text-gray-600 professional-text">Factory-trained specialists</p>
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
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Washing Machine Broken?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Don't let laundry pile up! Our washing machine experts will get your appliance working like new.
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
                  <h3 class="font-bold professional-subheading">Quick Response</h3>
                  <p class="text-gray-600">Same-day and emergency service available</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">🏠</div>
                <div>
                  <h3 class="font-bold professional-subheading">Mobile Service</h3>
                  <p class="text-gray-600">We come to your home with all tools and parts</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <form id="washing-machine-service-form" @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Washing Machine Service</h3>
              
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
                  <label for="washerType" class="block text-sm font-medium text-gray-700 mb-2">Washer Type</label>
                  <select
                    v-model="contactForm.washerType"
                    id="washerType"
                    required
                    class="professional-input"
                  >
                    <option value="">Select type...</option>
                    <option value="top-load">Top Load</option>
                    <option value="front-load">Front Load</option>
                    <option value="smart">Smart/WiFi</option>
                    <option value="he">High-Efficiency (HE)</option>
                    <option value="commercial">Commercial</option>
                    <option value="combo">Washer/Dryer Combo</option>
                  </select>
                </div>

                <div>
                  <label for="brand" class="block text-sm font-medium text-gray-700 mb-2">Brand</label>
                  <input
                    v-model="contactForm.brand"
                    type="text"
                    id="brand"
                    class="professional-input"
                    placeholder="e.g. Whirlpool, Samsung"
                  />
                </div>
              </div>

              <div>
                <label for="when" class="block text-sm font-medium text-gray-700 mb-2">When did the problem start?</label>
                <select
                  v-model="contactForm.when"
                  id="when"
                  class="professional-input"
                >
                  <option value="">Select timeframe...</option>
                  <option value="today">Today</option>
                  <option value="this-week">This week</option>
                  <option value="this-month">This month</option>
                  <option value="longer">Longer than a month</option>
                  <option value="gradual">Gradual over time</option>
                </select>
              </div>

              <div>
                <label for="issue" class="block text-sm font-medium text-gray-700 mb-2">What's the problem?</label>
                <textarea
                  v-model="contactForm.issue"
                  id="issue"
                  rows="3"
                  required
                  class="professional-input"
                  placeholder="Describe what's happening with your washing machine..."
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
