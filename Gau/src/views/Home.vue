<script setup>
import { ref, onMounted } from 'vue'
import Layout from '../components/Layout.vue'
import BackgroundSlider from '../components/BackgroundSlider.vue'

// Reactive data
const isMenuOpen = ref(false)
const currentTestimonial = ref(0)

const services = ref([
  {
    icon: '🔧',
    title: 'Appliance Repair',
    description: 'Expert repair services for all major appliance brands and models',
    route: '/services/appliances'
  },
  {
    icon: '☕',
    title: 'Coffee Machines', 
    description: 'Professional coffee machine repair and maintenance services',
    route: '/services/coffee-machines'
  },
  {
    icon: '🍽️',
    title: 'Dishwashers',
    description: 'Dishwasher repair, installation, and maintenance services',
    route: '/services/dishwashers'
  },
  {
    icon: '👕',
    title: 'Washing Machines',
    description: 'Complete washing machine repair and installation services',
    route: '/services/washing-machines'
  },
  {
    icon: '🔥',
    title: 'Hobs',
    description: 'Professional hob repair and installation services',
    route: '/services/hobs'
  },
  {
    icon: '💨',
    title: 'Kitchen Ventilators',
    description: 'Kitchen ventilation system repair and maintenance',
    route: '/services/kitchen-ventilators'
  },
  {
    icon: '⚡',
    title: 'All Electrical',
    description: 'Complete electrical appliance repair and installation',
    route: '/services/all-electrical'
  },
  {
    icon: '🏢',
    title: 'Commercial Equipment',
    description: 'Commercial dishwashers, fridges, ice makers, and mixers',
    route: '/services/commercial-equipment'
  }
])

const testimonials = ref([
  {
    name: 'Jennifer Miller',
    company: 'Happy Homeowner',
    text: 'They fixed my washing machine same day! Professional, affordable, and my laundry is back on track.',
    rating: 5
  },
  {
    name: 'Robert Johnson',
    company: 'Restaurant Owner',
    text: 'When our commercial fridge broke down, they came within hours. Saved our business from major losses!',
    rating: 5
  },
  {
    name: 'Maria Garcia',
    company: 'Busy Mom',
    text: 'Installed our new dishwasher perfectly and cleaned up after themselves. Highly recommend!',
    rating: 5
  }
])

const contactForm = ref({
  name: '',
  email: '',
  service: '',
  message: ''
})

// Methods
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const nextTestimonial = () => {
  currentTestimonial.value = (currentTestimonial.value + 1) % testimonials.value.length
}

const submitForm = () => {
  // Add loading state
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  // Simulate sending (in a real application, you would send this data to a server)
  setTimeout(() => {
    alert('🎉 Thank you for your inquiry! We will contact you soon.')
    
    // Reset form
    contactForm.value = {
      name: '',
      email: '',
      service: '',
      message: ''
    }
    
    // Reset button
    button.classList.remove('professional-loading')
    button.innerHTML = 'Send Message <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
  }, 1500)
}

const scrollToSection = (sectionId) => {
  document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' })
  isMenuOpen.value = false
}

// Auto-rotate testimonials
onMounted(() => {
  setInterval(nextTestimonial, 5000)
})
</script>

<template>
  <Layout>
    <!-- Hero Section -->
    <section id="home" class="relative overflow-hidden h-screen">
      <!-- Background Slider -->
      <BackgroundSlider />
      
      <!-- Hero Content -->
      <div class="absolute inset-0 z-10 flex items-center justify-center">
        <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
          <div class="mx-auto max-w-xl text-center relative">
            <h1 class="text-3xl font-extrabold sm:text-5xl professional-heading text-white drop-shadow-lg">
              Fix Your Appliances
              <strong class="font-extrabold text-white sm:block"> with Expert Local Service </strong>
            </h1>

            <div class="mt-8 relative">
              <p class="sm:text-xl/relaxed text-white opacity-95 drop-shadow-md">
                Fast, reliable appliance repair and installation services for your home and business. We fix it right the first time!
              </p>
            </div>

            <div class="mt-8 flex flex-wrap justify-center gap-4">
              <button
                class="professional-btn professional-btn-primary text-lg px-8 py-4 cursor-pointer bg-white text-white-600 hover:bg-red-50-50 shadow-lg"
                @click="scrollToSection('services')"
              >
                Our Services
              </button>

              <button
                class="professional-btn professional-btn-secondary text-lg px-8 py-4 cursor-pointer border-white text-blue hover:bg-white hover:text-blue-600 shadow-lg backdrop-blur-sm"
                @click="scrollToSection('contact')"
              >
                Emergency Repair
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section-gray py-24 relative">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Our Appliance Services</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Professional appliance repair, installation, and maintenance services for your home and business
          </p>
        </div>

        <div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div v-for="(service, index) in services" :key="service.title" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            <div class="service-icon">{{ service.icon }}</div>
            
            <h2 class="mt-4 text-xl font-bold text-gray-900 professional-subheading">{{ service.title }}</h2>
              <p class="mt-1 text-sm text-gray-600 mb-4 professional-text">
              {{ service.description }}
            </p>
            
            <router-link :to="service.route" class="mt-4 professional-btn professional-btn-secondary text-sm cursor-pointer block text-center">
              Learn More
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="bg-white py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
          <div class="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full">
            <div class="absolute inset-0 bg-gradient-to-r from-blue-500 to-green-600 flex items-center justify-center rounded-lg">              <div class="text-center text-white">
                <div class="text-6xl mb-4">🔧</div>
                <h3 class="text-2xl font-bold professional-subheading text-white">Expertise</h3>
                <p class="text-lg opacity-90">XX+ Years of Appliance Repair</p>
              </div>
            </div>
          </div>

          <div class="lg:py-24">
            <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Why Choose FixIt Appliances?</h2>

            <div class="mt-6">
              <p class="text-gray-600 professional-text">
                We are your trusted local appliance experts, providing fast, reliable, and affordable repair services for all major brands!
              </p>
            </div>

            <div class="mt-8 grid grid-cols-1 gap-8 sm:grid-cols-2">
              <div class="professional-card">
                <div class="flex items-center gap-4">
                  <span class="feature-icon">
                    <div class="text-2xl">👨‍🔧</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl professional-subheading">Certified Technicians</h3>
                    <p class="mt-1 text-gray-600 professional-text">Our experienced technicians are certified to work on all major appliance brands</p>
                  </div>
                </div>
              </div>

              <div class="professional-card">
                <div class="flex items-center gap-4">
                  <span class="feature-icon">
                    <div class="text-2xl">⚡</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl professional-subheading">Same-Day Service</h3>
                    <p class="mt-1 text-gray-600 professional-text">Most repairs completed same day with our mobile service units</p>
                  </div>
                </div>
              </div>

              <div class="professional-card">
                <div class="flex items-center gap-4">
                  <span class="feature-icon">
                    <div class="text-2xl">🛡️</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl professional-subheading">Warranty Coverage</h3>
                    <p class="mt-1 text-gray-600 professional-text">All repairs backed by our comprehensive parts and labor warranty</p>
                  </div>
                </div>
              </div>

              <div class="professional-card">
                <div class="flex items-center gap-4">
                  <span class="feature-icon">
                    <div class="text-2xl">📞</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl professional-subheading">24/7 Emergency</h3>
                    <p class="mt-1 text-gray-600 professional-text">Emergency service available for critical appliance breakdowns</p>
                  </div>
                </div>
              </div>
            </div>            <!-- Stats -->
            <div class="mt-12 grid grid-cols-3 gap-4">
              <div class="stat-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl professional-heading">XXX+</dt>
                <dd class="text-sm text-gray-500">Repairs Completed</dd>
              </div>
              <div class="stat-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl professional-heading">XX%</dt>
                <dd class="text-sm text-gray-500">Customer Satisfaction</dd>
              </div>
              <div class="stat-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl professional-heading">XX+</dt>
                <dd class="text-sm text-gray-500">Years Experience</dd>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="section-gray py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-center text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl professional-heading">
          What Our Clients Say
        </h2>

        <div class="mt-12 grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-8">
          <div v-for="(testimonial, index) in testimonials" :key="index" 
               :class="['testimonial-card', 'floating-card']"
               :style="{ animationDelay: index * 0.3 + 's' }">
            <div class="flex items-center gap-4">
              <div class="feature-icon">
                <div class="text-2xl">👤</div>
              </div>
              <div>
                <div class="flex justify-center gap-0.5 text-yellow-400 mb-2">
                  <span v-for="star in testimonial.rating" :key="star" class="text-xl">⭐</span>
                </div>

                <p class="mt-0.5 text-lg font-medium text-gray-900 professional-subheading">{{ testimonial.name }}</p>
                <p class="text-sm text-gray-500">{{ testimonial.company }}</p>
              </div>
            </div>

            <p class="mt-4 text-gray-700 font-medium professional-text">
              "{{ testimonial.text }}"
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="bg-white py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h1 class="text-2xl font-bold sm:text-3xl professional-heading">Need Appliance Service?</h1>
          <div class="mt-6">
            <p class="text-gray-500 professional-text">
              Ready to fix your appliances? Contact us today for fast, reliable service!
            </p>
          </div>
        </div>

        <div class="mx-auto mt-16 max-w-xl">
          <form @submit.prevent="submitForm" class="professional-card mb-0 mt-6 space-y-6 p-6">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Your Name</label>
              <div class="relative">
                <input
                  v-model="contactForm.name"
                  type="text"
                  id="name"
                  required
                  class="professional-input"
                  placeholder="Enter your name..."
                />
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Email Address</label>
              <div class="relative">
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
              <label for="service" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Service Needed</label>
              <select
                v-model="contactForm.service"
                id="service"
                required
                class="professional-input"
              >
                <option value="">Select a service...</option>
                <option value="appliances">General Appliances</option>
                <option value="coffee-machines">Coffee Machines</option>
                <option value="dishwashers">Dishwashers</option>
                <option value="washing-machines">Washing Machines</option>
                <option value="hobs">Hobs</option>
                <option value="kitchen-ventilators">Kitchen Ventilators</option>
                <option value="all-electrical">All Electrical</option>
                <option value="commercial">Commercial Equipment</option>
              </select>
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Service Details</label>
              <textarea
                v-model="contactForm.message"
                id="message"
                rows="4"
                required
                class="professional-input"
                placeholder="Tell us about your appliance issue or service needed..."
              ></textarea>
            </div>

            <button
              type="submit"
              class="professional-btn professional-btn-primary w-full text-lg py-4 group"
            >
              Send Message
              <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>
            </button>
          </form>        </div>
      </div>
    </section>
  </Layout>
</template>

<style scoped>
/* Component-specific styles */
</style>
