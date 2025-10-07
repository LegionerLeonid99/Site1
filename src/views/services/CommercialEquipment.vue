<script setup>
import { ref } from 'vue'
import Layout from '../../components/Layout.vue'
import { useSEO } from '../../composables/useSEO.js'
import { apiFetch } from '../../config/api.js'

// 🎯 SEO Setup for Commercial Equipment Page
useSEO('commercialEquipment')

const commercialEquipment = ref([
  {
    icon: '🍽️',
    name: 'Commercial Dishwashers',
    description: 'Restaurant and industrial dishwasher repair',
    services: ['High-temp sanitizing', 'Conveyor systems', 'Chemical dispensers', 'Rack washers']
  },
  {
    icon: '❄️',
    name: 'Commercial Refrigeration',
    description: 'Walk-in coolers, freezers, and display cases',
    services: ['Compressor repair', 'Temperature control', 'Door seals', 'Evaporator coils']
  },
  {
    icon: '🧊',
    name: 'Ice Makers',
    description: 'Commercial ice machine repair and maintenance',
    services: ['Ice production issues', 'Water filtration', 'Cleaning cycles', 'Bin systems']
  },
  {
    icon: '🥄',
    name: 'Commercial Mixers',
    description: 'Industrial food mixers and processors',
    services: ['Motor repair', 'Bowl attachments', 'Speed controls', 'Safety guards']
  }
])

const initialFormState = {
  name: '',
  email: '',
  phone: '',
  businessType: '',
  equipmentType: '',
  brand: '',
  issue: '',
  urgency: ''
}

const contactForm = ref({ ...initialFormState })

const resetForm = () => {
  contactForm.value = { ...initialFormState }
}

const submitForm = async () => {
  const button = document.querySelector('#commercial-equipment-form button[type="submit"]')

  if (button) {
    button.classList.add('professional-loading')
    button.textContent = 'Sending...'
  }
  
  try {
    const payload = {
      name: contactForm.value.name,
      email: contactForm.value.email,
      phone: contactForm.value.phone,
      businessType: contactForm.value.businessType,
      equipmentType: contactForm.value.equipmentType,
      brand: contactForm.value.brand,
      issue: contactForm.value.issue,
      urgency: contactForm.value.urgency,
      message: contactForm.value.issue
    }

    const response = await apiFetch('/contact/commercial-equipment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })

    const result = await response.json().catch(() => null)

    if (response.ok && result?.success) {
      alert('🎉 Thank you! We will contact you soon about your commercial equipment repair.')
      resetForm()
    } else {
      const message = result?.message ?? `Request failed with status ${response.status}`
      throw new Error(message)
    }
  } catch (error) {
    console.error('Commercial equipment contact form error:', error)
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
            Commercial Equipment Repair
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Professional repair for commercial dishwashers, fridges, ice makers, and mixers. Keep your business running!
          </p>
          <div class="mt-8">
            <a href="#contact" class="professional-btn professional-btn-primary text-lg px-8 py-4">
              Emergency Service
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Commercial Equipment Section -->
    <section class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Commercial Equipment We Service</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional repair for restaurant and commercial kitchen equipment
          </p>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(equipment, index) in commercialEquipment" :key="equipment.name" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ equipment.icon }}</div>
            <h3 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ equipment.name }}</h3>
            <p class="mt-2 text-gray-600 professional-text mb-4">{{ equipment.description }}</p>            <ul class="text-sm text-gray-500 space-y-1">
              <li v-for="service in equipment.services" :key="service" class="flex items-center">
                <span class="text-green-500 mr-2">✓</span>
                {{ service }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Business Benefits -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Why Businesses Choose Us</h2>
        </div>

        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🚨</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">24/7 Emergency</h3>
            <p class="mt-2 text-gray-600 professional-text">Round-the-clock service for critical equipment</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">⏰</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Rapid Response</h3>
            <p class="mt-2 text-gray-600 professional-text">Minimize downtime with fast service</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">🔧</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Commercial Experts</h3>
            <p class="mt-2 text-gray-600 professional-text">Specialized in commercial equipment</p>
          </div>

          <div class="professional-card text-center">
            <div class="service-icon mx-auto">💼</div>
            <h3 class="mt-4 text-lg font-bold professional-subheading">Business Insurance</h3>
            <p class="mt-2 text-gray-600 professional-text">Fully licensed and insured</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section-gray py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div>
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Commercial Equipment Down?</h2>
            <p class="mt-6 text-gray-600 professional-text">
              Equipment failure can cost your business money every minute. Our commercial specialists respond quickly to get you back in operation.
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
                  <h3 class="font-bold professional-subheading">24/7 Service</h3>
                  <p class="text-gray-600">Emergency repairs available anytime</p>
                </div>
              </div>
            </div>
          </div>
          
          <div>
            <form id="commercial-equipment-form" @submit.prevent="submitForm" class="professional-card space-y-6">
              <h3 class="text-xl font-bold professional-subheading">Request Commercial Service</h3>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.name" type="text" required class="professional-input" placeholder="Contact Name" />
                <input v-model="contactForm.email" type="email" required class="professional-input" placeholder="Business Email" />
              </div>
              
              <input v-model="contactForm.phone" type="tel" required class="professional-input" placeholder="07XXX XXXXXX" />
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.businessType" type="text" required class="professional-input" placeholder="Business Type (Restaurant, etc.)" />
                <select v-model="contactForm.equipmentType" required class="professional-input">
                  <option value="">Equipment Type...</option>
                  <option value="dishwasher">Commercial Dishwasher</option>
                  <option value="refrigeration">Commercial Fridge/Freezer</option>
                  <option value="ice-maker">Ice Maker</option>
                  <option value="mixer">Commercial Mixer</option>
                  <option value="other">Other Equipment</option>
                </select>
              </div>
              
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <input v-model="contactForm.brand" type="text" class="professional-input" placeholder="Brand/Model" />
                <select v-model="contactForm.urgency" required class="professional-input">
                  <option value="">Urgency Level...</option>
                  <option value="emergency">EMERGENCY - Equipment Down</option>
                  <option value="urgent">Urgent - Same Day</option>
                  <option value="standard">Standard Service</option>
                  <option value="maintenance">Preventive Maintenance</option>
                </select>
              </div>
              
              <textarea v-model="contactForm.issue" required class="professional-input" rows="3" placeholder="Describe the equipment problem..."></textarea>
              
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
