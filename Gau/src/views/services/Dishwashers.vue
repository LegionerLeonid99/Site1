<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'

// 🎯 SEO Setup for Dishwashers Page
useSEO({ page: 'dishwashers' })

// Dishwasher types and services
const dishwasherTypes = ref([
  {
    icon: '🍽️',
    name: 'Built-in Dishwashers',
    description: 'Professional built-in dishwasher repair and installation',
    services: ['Control panel repair', 'Pump replacement', 'Rack adjustment', 'Water inlet valve']
  },
  {
    icon: '📦',
    name: 'Portable Dishwashers',
    description: 'Portable and countertop dishwasher service',
    services: ['Hose connections', 'Wheel replacement', 'Control issues', 'Drainage problems']
  },
  {
    icon: '💧',
    name: 'Drawer Dishwashers',
    description: 'Fisher & Paykel and drawer-style dishwasher repair',
    services: ['Drawer mechanism', 'Seal replacement', 'Electronic controls', 'Water circulation']
  },
  {
    icon: '🏢',
    name: 'Commercial Dishwashers',
    description: 'Restaurant and commercial dishwasher service',
    services: ['High-temp repairs', 'Sanitizer systems', 'Conveyor belts', 'Heavy-duty pumps']
  },
  {
    icon: '🔄',
    name: 'Integrated Dishwashers',
    description: 'Panel-ready and integrated dishwasher service',
    services: ['Door adjustments', 'Panel installation', 'Control board repair', 'Custom fitting']
  },
  {
    icon: '⚡',
    name: 'Smart Dishwashers',
    description: 'WiFi-enabled and smart dishwasher repair',
    services: ['App connectivity', 'Software updates', 'Sensor calibration', 'Smart controls']
  }
])

const supportedBrands = ref([
  'Bosch', 'KitchenAid', 'Whirlpool', 'GE', 'Maytag', 'Samsung', 'LG', 'Frigidaire',
  'Miele', 'Fisher & Paykel', 'Blomberg', 'Thermador', 'Viking', 'Sub-Zero', 'Asko'
])

const commonIssues = ref([
  {
    issue: 'Not draining properly',
    solution: 'Usually caused by clogged filters or garbage disposal issues. We clean and repair drainage systems.',
    icon: '🚰'
  },
  {
    issue: 'Dishes not getting clean',
    solution: 'Often due to clogged spray arms or water temperature issues. We restore proper cleaning performance.',
    icon: '🍽️'
  },
  {
    issue: 'Not starting or powering on',
    solution: 'Control board or door latch problems. We diagnose electrical issues and replace faulty components.',
    icon: '⚡'
  },
  {
    issue: 'Leaking water',
    solution: 'Door seals, pump seals, or hose connections. We identify leak sources and fix them permanently.',
    icon: '💧'
  },
  {
    issue: 'Strange noises during cycle',
    solution: 'Pump motor or wash arm issues. We eliminate annoying noises and restore quiet operation.',
    icon: '🔊'
  },
  {
    issue: 'Error codes on display',
    solution: 'Various sensor and control issues. We interpret error codes and fix the underlying problems.',
    icon: '⚠️'
  }
])

const maintenanceTips = ref([
  'Clean filter monthly to prevent clogs',
  'Run hot water at kitchen sink before starting dishwasher',
  'Use rinse aid for better drying performance',
  'Don\'t overload racks - water needs to circulate',
  'Check and clean spray arms regularly',
  'Use appropriate detergent amount'
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  dishwasherType: '',
  brand: '',
  model: '',
  issue: '',
  urgency: ''
})

const submitForm = () => {
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  setTimeout(() => {
    alert('🎉 Thank you! We will contact you soon about your dishwasher repair.')
    
    contactForm.value = {
      name: '',
      email: '',
      phone: '',
      dishwasherType: '',
      brand: '',
      model: '',
      issue: '',
      urgency: ''
    }
    
    button.classList.remove('professional-loading')
    button.innerHTML = 'Request Service <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
  }, 1500)
}
</script>

<template>
  <Layout>
    <!-- Hero Section -->
    <section class="hero-gradient py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-4xl font-bold sm:text-6xl professional-heading text-white">
            Dishwasher Repair Service
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert dishwasher repair and installation. Get your dishes sparkling clean again!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Fix My Dishwasher
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Dishwasher Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Dishwashers We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for all types of dishwashers - built-in, portable, and commercial
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(dishwasher, index) in dishwasherTypes" :key="dishwasher.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ dishwasher.icon }}</div>
            
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ dishwasher.name }}</h3>
            
            <p class="mt-2 text-gray-600 professional-text mb-4">
              {{ dishwasher.description }}
            </p>
              <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in dishwasher.services" :key="service" class="flex items-center">
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
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Common Dishwasher Problems</h2>
          <p class="mt-6 text-gray-600 professional-text">
            We diagnose and fix these issues quickly and affordably
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

    <!-- Maintenance Tips Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Dishwasher Maintenance Tips</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Keep your dishwasher running efficiently with these expert tips:
            </p>

            <ul class="mt-8 space-y-4">
              <li v-for="tip in maintenanceTips" :key="tip" class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                <span class="text-gray-700">{{ tip }}</span>
              </li>
            </ul>
          </div>

          <div class="professional-card">
            <h3 class="text-xl font-bold professional-subheading mb-4">Emergency Signs</h3>
            <p class="text-gray-600 professional-text mb-4">
              Call us immediately if you notice:
            </p>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-center">
                <span class="text-red-500 mr-2">⚠️</span>
                Water pooling on kitchen floor
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">⚠️</span>
                Burning smell during operation
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">⚠️</span>
                Sparks or electrical issues
              </li>
              <li class="flex items-center">
                <span class="text-red-500 mr-2">⚠️</span>
                Extremely loud grinding noises
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
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Dishwasher Brands We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Authorized service for all major dishwasher manufacturers
          </p>
        </div>

        <div class="grid grid-cols-3 gap-4 md:grid-cols-5 lg:grid-cols-5">
          <div v-for="brand in supportedBrands" :key="brand" 
               class="professional-card text-center py-4">
            <p class="text-gray-700 font-medium">{{ brand }}</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <p class="text-gray-600">Need service for a different brand? <strong>Call us</strong> - we likely service it!</p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Dishwasher Not Working?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Don't wash dishes by hand! Our dishwasher repair experts will get your appliance back to perfect working order.
            </p>

            <div class="mt-8 space-y-6">              <div class="flex items-center gap-4">
                <div class="feature-icon">�</div>
                <div>
                  <h3 class="font-bold professional-subheading">Contact Us</h3>
                  <p class="text-gray-600">Use our contact form below</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">🚨</div>
                <div>
                  <h3 class="font-bold professional-subheading">Emergency Service</h3>
                  <p class="text-gray-600">Same-day repairs for urgent issues</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <div class="feature-icon">🛡️</div>
                <div>
                  <h3 class="font-bold professional-subheading">Warranty</h3>
                  <p class="text-gray-600">XX-day parts and labor warranty</p>
                </div>
              </div>              <div class="flex items-center gap-4">
                <div class="feature-icon">�</div>
                <div>
                  <h3 class="font-bold professional-subheading">Fast Service</h3>
                  <p class="text-gray-600">Quick response and same-day repairs</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <form @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Dishwasher Service</h3>
              
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
                  <label for="dishwasherType" class="block text-sm font-medium text-gray-700 mb-2">Dishwasher Type</label>
                  <select
                    v-model="contactForm.dishwasherType"
                    id="dishwasherType"
                    required
                    class="professional-input"
                  >
                    <option value="">Select type...</option>
                    <option value="built-in">Built-in</option>
                    <option value="portable">Portable</option>
                    <option value="drawer">Drawer Style</option>
                    <option value="commercial">Commercial</option>
                    <option value="integrated">Integrated</option>
                    <option value="smart">Smart/WiFi</option>
                  </select>
                </div>

                <div>
                  <label for="brand" class="block text-sm font-medium text-gray-700 mb-2">Brand</label>
                  <input
                    v-model="contactForm.brand"
                    type="text"
                    id="brand"
                    class="professional-input"
                    placeholder="e.g. Bosch, KitchenAid"
                  />
                </div>
              </div>

              <div>
                <label for="urgency" class="block text-sm font-medium text-gray-700 mb-2">Service Urgency</label>
                <select
                  v-model="contactForm.urgency"
                  id="urgency"
                  required
                  class="professional-input"
                >
                  <option value="">Select urgency...</option>
                  <option value="emergency">Emergency (same day)</option>
                  <option value="urgent">Urgent (within 24 hours)</option>
                  <option value="standard">Standard (2-3 days)</option>
                  <option value="scheduled">Schedule at convenience</option>
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
                  placeholder="Describe the issue with your dishwasher..."
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
