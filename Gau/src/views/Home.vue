<script setup>
import { ref, onMounted } from 'vue'
import Layout from '../components/Layout.vue'
import BackgroundSlider from '../components/BackgroundSlider.vue'
import { businessConfig, getFullAddress, getGoogleMapsUrl, getGoogleMapsEmbedUrlBasic } from '../config/business.js'
import { useSEO } from '../composables/useSEO.js'

// 🎯 SEO Setup for Home Page
useSEO({
  page: 'home',
  customMeta: {
    'google-site-verification': '', // Add your Google Search Console verification code here
    'msvalidate.01': '' // Add your Bing Webmaster verification code here
  }
})

// Reactive data
const isMenuOpen = ref(false)

const services = ref([
  {
    icon: '',
    title: 'Appliance Repair',
    description: 'Expert repair services for all major appliance brands and models',
    route: '/services/appliances'
  },
  {
    icon: '',
    title: 'Coffee Machines', 
    description: 'Professional coffee machine repair and maintenance services',
    route: '/services/coffee-machines'
  },
  {
    icon: '',
    title: 'Dishwashers',
    description: 'Dishwasher repair, installation, and maintenance services',
    route: '/services/dishwashers'
  },
  {
    icon: '',
    title: 'Washing Machines',
    description: 'Complete washing machine repair and installation services',
    route: '/services/washing-machines'
  },
  {
    icon: '',
    title: 'Hobs',
    description: 'Professional hob repair and installation services',
    route: '/services/hobs'
  },
  {
    icon: '',
    title: 'Air Conditioners',
    description: 'Air conditioning system repair, maintenance, and installation',
    route: '/services/air-conditioners'
  },
  {
    icon: '',
    title: 'All Electrical',
    description: 'Complete electrical appliance repair and installation',
    route: '/services/all-electrical'
  },
  {
    icon: '',
    title: 'Commercial Equipment',
    description: 'Commercial dishwashers, fridges, ice makers, and mixers',
    route: '/services/commercial-equipment'
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

const submitForm = async () => {
  // Add loading state
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('professional-loading')
  button.textContent = 'Sending...'
  
  try {
  const response = await fetch('http://localhost:5000/api/contact/enquiry', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contactForm.value)
    })
    
    const result = await response.json()
    
    if (result.success) {
      alert('🎉 Thank you for your inquiry! We will contact you soon.')
      
      // Reset form
      contactForm.value = {
        name: '',
        email: '',
        service: '',
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
    button.innerHTML = 'Send Message <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
  }
}

const scrollToSection = (sectionId) => {
  document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' })
  isMenuOpen.value = false
}
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
            <h1 class="text-2xl font-extrabold sm:text-4xl lg:text-5xl professional-heading text-white drop-shadow-lg">
              <span class="bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent block text-3xl sm:text-5xl lg:text-6xl mb-2">{{ businessConfig.business.name }}</span>
              Fix Your Appliances
              <strong class="font-extrabold text-white sm:block"> with Our Expert Family Service </strong>
            </h1>

            <div class="mt-6 lg:mt-8 relative">
              <p class="text-lg sm:text-xl lg:text-xl/relaxed text-white opacity-95 drop-shadow-md">
                Fast, reliable appliance repair and installation services from a trusted family business. We fix it right the first time!
              </p>
            </div>

            <div class="mt-6 lg:mt-8 flex flex-col sm:flex-row justify-center gap-3 sm:gap-4">
              <button
                class="professional-btn professional-btn-primary text-base sm:text-lg px-6 sm:px-8 py-3 sm:py-4 cursor-pointer shadow-lg w-full sm:w-auto"
                @click="scrollToSection('services')"
              >
                Our Services
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

        <div class="mt-16 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <div v-for="(service, index) in services" :key="service.title" 
               :class="['professional-card', 'floating-card']" 
               :style="{ animationDelay: index * 0.1 + 's' }">
            
            <h2 class="mt-4 text-lg sm:text-xl font-bold text-gray-900 professional-subheading">{{ service.title }}</h2>
              <p class="mt-2 text-sm text-gray-600 mb-4 professional-text">
              {{ service.description }}
            </p>
            
            <router-link :to="service.route" class="mt-auto professional-btn professional-btn-secondary text-sm cursor-pointer block text-center">
              Learn More
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="bg-gray-50 py-24 relative overflow-hidden">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-16 lg:grid-cols-2 lg:gap-24 items-center">
          <!-- Content Side -->
          <div class="order-2 lg:order-1">
            <h2 class="text-4xl font-bold text-gray-900 mb-8 professional-heading">
              Why Choose Our Family Business?
            </h2>
            
            <p class="text-lg text-gray-600 mb-12 leading-relaxed">
              We're your trusted local <span class="text-brand font-semibold">family-run appliance repair business</span>, providing fast, reliable, and affordable repair services for all major brands. With generations of hands-on experience, our family personally handles every repair to ensure quality workmanship and customer satisfaction.
            </p>

            <!-- Feature Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <!-- Family-Run Business -->
              <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all duration-300 group">
                <div class="flex items-start gap-4">
                  <div class="w-12 h-12 bg-blue-100 border-2 border-blue-200 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-blue-200 group-hover:border-blue-300 transition-colors">
                    <span class="text-xl font-bold text-brand">F</span>
                  </div>
                  <div>
                    <h3 class="font-semibold text-gray-900 mb-2">Family-Run Business</h3>
                    <p class="text-sm text-gray-600 leading-relaxed">Our family has been serving the community for generations with trusted, reliable appliance repair services</p>
                  </div>
                </div>
              </div>

              <!-- Family Guarantee -->
              <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all duration-300 group">
                <div class="flex items-start gap-4">
                  <div class="w-12 h-12 bg-blue-100 border-2 border-blue-200 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-blue-200 group-hover:border-blue-300 transition-colors">
                    <span class="text-xl font-bold text-brand">G</span>
                  </div>
                  <div>
                    <h3 class="font-semibold text-gray-900 mb-2">Family Guarantee</h3>
                    <p class="text-sm text-gray-600 leading-relaxed">Our family name is on every repair with comprehensive parts and labor warranty you can trust</p>
                  </div>
                </div>
              </div>

              <!-- Fair Family Pricing -->
              <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all duration-300 group">
                <div class="flex items-start gap-4">
                  <div class="w-12 h-12 bg-blue-100 border-2 border-blue-200 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-blue-200 group-hover:border-blue-300 transition-colors">
                    <span class="text-xl font-bold text-brand">P</span>
                  </div>
                  <div>
                    <h3 class="font-semibold text-gray-900 mb-2">Fair Family Pricing</h3>
                    <p class="text-sm text-gray-600 leading-relaxed">As a family business, we offer competitive prices and honest value for quality service</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Image Side -->
          <div class="order-1 lg:order-2">
            <div class="relative">
              <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl">
                <img 
                  src="/src/assets/images/hero-section/pexels-asphotograpy-213162.jpg" 
                  alt="Professional appliance repair expertise"
                  class="w-full h-full object-cover"
                />
                <div class="absolute inset-0 bg-gradient-to-tr from-black/50 via-transparent to-transparent blur-xl"></div>
                <div class="absolute bottom-6 left-6 text-white">
                  <div class="bg-white/10 backdrop-blur-sm rounded-lg px-4 py-3 border border-white/20">
                    <h3 class="text-xl font-bold mb-1">Our Engineer's Expertise</h3>
                    <p class="text-sm opacity-90">20+ Years of Appliance Repair</p>
                  </div>
                </div>
              </div>
              
              <!-- Decorative elements -->
              <div class="absolute -top-6 -right-6 w-20 h-20 bg-blue-100 rounded-full opacity-70"></div>
              <div class="absolute -bottom-8 -left-8 w-32 h-32 bg-blue-50 rounded-full opacity-50"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Location Section -->
    <section id="location" class="section-gray py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Visit Our Location</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Find us easily or contact us for on-site repair services
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">
          <!-- Business Information -->
          <div class="space-y-6">
            <!-- Address Card -->
            <div class="professional-card p-6">
              <div class="flex items-start space-x-4">
                <div class="feature-icon">
                  <div class="text-2xl font-bold text-brand">L</div>
                </div>
                <div>
                  <h3 class="text-xl font-bold professional-subheading mb-2">Our Address</h3>
                  <p class="text-gray-600 professional-text">{{ getFullAddress() }}</p>
                  <a 
                    :href="getGoogleMapsUrl()" 
                    target="_blank"
                    class="inline-flex items-center mt-3 text-brand hover:text-blue-700 font-medium"
                  >
                    Get Directions
                    <span class="ml-1">↗</span>
                  </a>
                </div>
              </div>
            </div>

            <!-- Contact Information -->
            <div class="professional-card p-6">
              <h3 class="text-xl font-bold professional-subheading mb-4">Contact Information</h3>
              <div class="space-y-3">
                <!-- Phone -->
                <div class="flex items-center space-x-4">
                  <div class="feature-icon-small">
                    <div class="text-lg font-bold text-brand">P</div>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">Phone</p>
                    <a 
                      :href="`tel:${businessConfig.location.contact.phone}`"
                      class="text-brand hover:text-blue-700 font-medium"
                    >
                      {{ businessConfig.location.contact.phone }}
                    </a>
                  </div>
                </div>

                <!-- Email -->
                <div class="flex items-center space-x-4">
                  <div class="feature-icon-small">
                    <div class="text-lg font-bold text-brand">E</div>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">Email</p>
                    <a 
                      :href="`mailto:${businessConfig.location.contact.email}`"
                      class="text-brand hover:text-blue-700 font-medium"
                    >
                      {{ businessConfig.location.contact.email }}
                    </a>
                  </div>
                </div>

                <!-- Website -->
                <div class="flex items-center space-x-4">
                  <div class="feature-icon-small">
                    <div class="text-lg font-bold text-brand">W</div>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">Website</p>
                    <p class="text-gray-600">{{ businessConfig.location.contact.website }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Business Hours -->
            <div class="professional-card p-6">
              <h3 class="text-xl font-bold professional-subheading mb-4">Business Hours</h3>
              <div class="space-y-2">
                <div v-for="(hours, day) in businessConfig.business.hours" :key="day" 
                     class="flex justify-between items-center">
                  <span class="capitalize font-medium text-gray-900">{{ day }}</span>
                  <span class="text-gray-600">{{ hours }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Map -->
          <div class="lg:sticky lg:top-8">
            <div class="professional-card p-1 overflow-hidden">
              <iframe
                :src="getGoogleMapsEmbedUrlBasic()"
                :style="{ 
                  height: businessConfig.map.height, 
                  borderRadius: businessConfig.map.borderRadius 
                }"
                width="100%"
                style="border:0;"
                allowfullscreen=""
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
                class="w-full"
              ></iframe>
            </div>
            
            <!-- Map Notice -->
            <div class="mt-4 p-4 bg-blue-50 rounded-lg border border-blue-200">
              <p class="text-sm text-blue-800">
                <strong>Note:</strong> We provide on-site repair services throughout our service areas. 
                Contact us to schedule an appointment at your location.
              </p>
            </div>

            <!-- Service Areas - Moved below the note -->
            <div class="professional-card p-6 mt-6">
              <h3 class="text-xl font-bold professional-subheading mb-4">Service Areas</h3>
              <div class="grid grid-cols-2 gap-2">
                <div v-for="area in businessConfig.business.serviceAreas" :key="area"
                     class="flex items-center space-x-2">
                  <span class="text-green-500 font-bold">✓</span>
                  <span class="text-gray-600 text-sm">{{ area }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq" class="bg-white py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold sm:text-4xl professional-heading">Frequently Asked Questions</h2>
          <p class="mt-6 text-gray-600 professional-text">
            Quick answers to common questions about our appliance repair services
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
          <!-- FAQ Items -->
          <div class="space-y-4 lg:space-y-6">
            <div class="professional-card p-4 lg:p-6">
              <h3 class="text-base lg:text-lg font-bold professional-subheading mb-3">How quickly can you repair my appliance?</h3>
              <p class="text-gray-600 professional-text text-sm lg:text-base">Most repairs are completed the same day. Our family team carries common parts in our van and can diagnose issues quickly to get your appliances working again.</p>
            </div>

            <div class="professional-card p-4 lg:p-6">
              <h3 class="text-base lg:text-lg font-bold professional-subheading mb-3">Do you provide warranties on repairs?</h3>
              <p class="text-gray-600 professional-text text-sm lg:text-base">Yes! Our family business provides comprehensive warranties on all parts and labor. You can have confidence that your repair will last.</p>
            </div>

            <div class="professional-card p-4 lg:p-6">
              <h3 class="text-base lg:text-lg font-bold professional-subheading mb-3">What brands do you service?</h3>
              <p class="text-gray-600 professional-text text-sm lg:text-base">Our family services all major appliance brands including Bosch, Samsung, LG, Whirlpool, Hotpoint, AEG, and many more.</p>
            </div>

            <div class="professional-card p-4 lg:p-6">
              <h3 class="text-base lg:text-lg font-bold professional-subheading mb-3">How much does a repair cost?</h3>
              <p class="text-gray-600 professional-text text-sm lg:text-base">We provide upfront pricing before starting any work. No hidden fees or surprises - you'll know the cost before we begin.</p>
            </div>
          </div>

          <!-- Contact Form -->
          <div class="professional-card p-6 lg:p-8">
            <h3 class="text-lg lg:text-xl font-bold professional-subheading mb-4 lg:mb-6">Still Have Questions?</h3>
            <p class="text-gray-600 professional-text mb-4 lg:mb-6 text-sm lg:text-base">Contact our family directly and we'll get back to you quickly with answers.</p>
            
            <form @submit.prevent="submitForm" class="space-y-4">
              <div>
                <label for="faq-name" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Your Name</label>
                <input
                  v-model="contactForm.name"
                  type="text"
                  id="faq-name"
                  required
                  class="professional-input"
                  placeholder="Enter your name..."
                />
              </div>

              <div>
                <label for="faq-email" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Email Address</label>
                <input
                  v-model="contactForm.email"
                  type="email"
                  id="faq-email"
                  required
                  class="professional-input"
                  placeholder="your.email@example.com"
                />
              </div>

              <div>
                <label for="faq-service" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Service Needed</label>
                <select
                  v-model="contactForm.service"
                  id="faq-service"
                  required
                  class="professional-input"
                >
                  <option value="">Select a service...</option>
                  <option value="Appliance Repair">Appliance Repair</option>
                  <option value="Coffee Machines">Coffee Machines</option>
                  <option value="Dishwashers">Dishwashers</option>
                  <option value="Washing Machines">Washing Machines</option>
                  <option value="Hobs">Hobs</option>
                  <option value="Air Conditioners">Air Conditioners</option>
                  <option value="All Electrical">All Electrical</option>
                  <option value="Commercial Equipment">Commercial Equipment</option>
                </select>
              </div>

              <div>
                <label for="faq-message" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Your Question or Issue</label>
                <textarea
                  v-model="contactForm.message"
                  id="faq-message"
                  rows="3"
                  required
                  class="professional-input"
                  placeholder="Ask your question or describe your appliance issue..."
                ></textarea>
              </div>

              <button
                type="submit"
                class="professional-btn professional-btn-primary w-full py-3 group"
              >
                Send Question
                <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>
              </button>
            </form>
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
              Ready to fix your appliances? Contact our family today for fast, reliable service!
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
                <option value="Appliance Repair">Appliance Repair</option>
                <option value="Coffee Machines">Coffee Machines</option>
                <option value="Dishwashers">Dishwashers</option>
                <option value="Washing Machines">Washing Machines</option>
                <option value="Hobs">Hobs</option>
                <option value="Air Conditioners">Air Conditioners</option>
                <option value="All Electrical">All Electrical</option>
                <option value="Commercial Equipment">Commercial Equipment</option>
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

/* Feature icon small for contact info */
.feature-icon-small {
  @apply w-12 h-12 bg-brand/10 rounded-lg flex items-center justify-center;
}

/* Enhanced card hover effects for location section */
.professional-card:hover {
  @apply shadow-lg transform -translate-y-1;
  transition: all 0.3s ease;
}

/* Business hours styling */
.business-hours-item {
  @apply py-2 border-b border-gray-100 last:border-b-0;
}

/* Map container responsive styling */
@media (max-width: 1024px) {
  .lg\:sticky {
    position: static !important;
  }
}
</style>
