<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'

const hobTypes = ref([
  {
    icon: '🔥',
    name: 'Gas Hobs',
    description: 'Professional gas hob repair and maintenance',
    services: ['Burner replacement', 'Gas valve repair', 'Ignition system', 'Safety controls']
  },
  {
    icon: '⚡',
    name: 'Electric Hobs',
    description: 'Electric and ceramic hob repair service',
    services: ['Element replacement', 'Control switches', 'Temperature sensors', 'Wiring repair']
  },
  {
    icon: '🍳',
    name: 'Induction Hobs',
    description: 'Induction cooktop repair and diagnostics',
    services: ['Induction coil repair', 'Control board issues', 'Touch panel repair', 'Power supply']
  },
  {
    icon: '🏢',
    name: 'Commercial Hobs',
    description: 'Restaurant and commercial cooking equipment',
    services: ['Heavy-duty repair', 'Industrial burners', 'Safety systems', 'Professional maintenance']
  }
])

const supportedBrands = ref([
  'Bosch', 'Samsung', 'LG', 'Electrolux', 'Whirlpool', 'GE', 'Frigidaire', 'KitchenAid',
  'Miele', 'Thermador', 'Viking', 'Wolf', 'Gaggenau', 'Fisher & Paykel', 'Smeg'
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  hobType: '',
  brand: '',
  issue: ''
})

const submitForm = () => {
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  setTimeout(() => {
    alert('🎉 Thank you! We will contact you soon about your hob repair.')
    contactForm.value = { name: '', email: '', phone: '', hobType: '', brand: '', issue: '' }
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
            Hob Repair Service
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert repair for gas, electric, and induction hobs. Get cooking again!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4 bg-white text-blue-600 hover:bg-gray-50">
              Fix My Hob
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Hob Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Hobs We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for all types of cooking hobs
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(hob, index) in hobTypes" :key="hob.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ hob.icon }}</div>
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ hob.name }}</h3>
            <p class="mt-2 text-gray-600 professional-text mb-4">{{ hob.description }}</p>            <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in hob.services" :key="service" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ service }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Hob Not Working?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Our certified technicians specialize in all types of cooking hobs.
            </p>
          </div>
          <div>
            <form @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Hob Service</h3>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.name" type="text" required class="professional-input" placeholder="Your Name" />
                <input v-model="contactForm.email" type="email" required class="professional-input" placeholder="Email" />
              </div>
              
              <input v-model="contactForm.phone" type="tel" required class="professional-input" placeholder="Phone Number" />
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <select v-model="contactForm.hobType" required class="professional-input">
                  <option value="">Hob Type...</option>
                  <option value="gas">Gas Hob</option>
                  <option value="electric">Electric Hob</option>
                  <option value="induction">Induction Hob</option>
                  <option value="commercial">Commercial</option>
                </select>
                <input v-model="contactForm.brand" type="text" class="professional-input" placeholder="Brand" />
              </div>
              
              <textarea v-model="contactForm.issue" required class="professional-input" rows="3" placeholder="Describe the issue..."></textarea>
              
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
