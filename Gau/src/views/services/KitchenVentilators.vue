<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'

const ventilatorTypes = ref([
  {
    icon: '💨',
    name: 'Range Hoods',
    description: 'Under-cabinet and wall-mount range hood repair',
    services: ['Fan motor repair', 'Light replacement', 'Filter cleaning', 'Duct connections']
  },
  {
    icon: '🌪️',
    name: 'Island Hoods',
    description: 'Island and ceiling-mount ventilation systems',
    services: ['Suspension repair', 'Remote controls', 'Variable speed fans', 'LED lighting']
  },
  {
    icon: '🔄',
    name: 'Downdraft Ventilators',
    description: 'Pop-up and built-in downdraft ventilation',
    services: ['Motor replacement', 'Lifting mechanism', 'Duct cleaning', 'Control panels']
  },
  {
    icon: '🏢',
    name: 'Commercial Kitchen Ventilation',
    description: 'Restaurant and commercial kitchen systems',
    services: ['Heavy-duty fans', 'Fire suppression', 'Duct maintenance', 'Safety compliance']
  }
])

const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  ventilatorType: '',
  brand: '',
  issue: ''
})

const submitForm = () => {
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  setTimeout(() => {
    alert('🎉 Thank you! We will contact you soon about your kitchen ventilator repair.')
    contactForm.value = { name: '', email: '', phone: '', ventilatorType: '', brand: '', issue: '' }
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
            Kitchen Ventilator Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Expert repair for range hoods and kitchen ventilation systems. Clear the air!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4 bg-white text-blue-600 hover:bg-gray-50">
              Fix My Ventilator
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Ventilator Types Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Kitchen Ventilation We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for all types of kitchen ventilation systems
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(ventilator, index) in ventilatorTypes" :key="ventilator.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ ventilator.icon }}</div>
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ ventilator.name }}</h3>
            <p class="mt-2 text-gray-600 professional-text mb-4">{{ ventilator.description }}</p>            <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in ventilator.services" :key="service" class="flex items-center">
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
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Ventilation Not Working?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Poor kitchen ventilation can affect air quality and cooking comfort. Let our experts help.
            </p>
          </div>
          <div>
            <form @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Ventilator Service</h3>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.name" type="text" required class="professional-input" placeholder="Your Name" />
                <input v-model="contactForm.email" type="email" required class="professional-input" placeholder="Email" />
              </div>
              
              <input v-model="contactForm.phone" type="tel" required class="professional-input" placeholder="Phone Number" />
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <select v-model="contactForm.ventilatorType" required class="professional-input">
                  <option value="">Ventilator Type...</option>
                  <option value="range-hood">Range Hood</option>
                  <option value="island-hood">Island Hood</option>
                  <option value="downdraft">Downdraft</option>
                  <option value="commercial">Commercial</option>
                </select>
                <input v-model="contactForm.brand" type="text" class="professional-input" placeholder="Brand" />
              </div>
              
              <textarea v-model="contactForm.issue" required class="professional-input" rows="3" placeholder="Describe the ventilation issue..."></textarea>
              
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
