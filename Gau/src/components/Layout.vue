<script setup>
import { ref } from 'vue'
import { businessConfig } from '../config/business.js'

// Reactive data
const isMenuOpen = ref(false)

// Methods
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const scrollToSection = (sectionId) => {
  if (location.pathname === '/') {
    document.getElementById(sectionId)?.scrollIntoView({ behavior: 'smooth' })
  } else {
    // If we're not on home page, navigate to home first
    this.$router.push('/' + (sectionId ? '#' + sectionId : ''))
  }
  isMenuOpen.value = false
}
</script>

<template>
  <div class="app">
    <!-- Navigation - Professional Header -->
    <header class="professional-nav bg-white shadow-sm fixed w-full top-0 z-50">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="md:flex md:items-center md:gap-12">
            <router-link to="/" class="block text-brand font-bold text-2xl bg-gradient-to-r from-blue-600 to-blue-800 bg-clip-text text-transparent hover:scale-105 transition-transform duration-300 animate-pulse">
              {{ businessConfig.business.name }}
            </router-link>
          </div>

          <div class="hidden md:block">
            <nav aria-label="Global">
              <ul class="flex items-center gap-6 text-sm">
                <li>
                  <router-link to="/" class="text-gray-600 transition hover:text-brand professional-underline hover:scale-110 transform duration-200">
                    Home
                  </router-link>
                </li>
                <li class="relative group">
                  <button class="text-gray-600 transition hover:text-brand professional-underline flex items-center gap-1 hover:scale-110 transform duration-200">
                    Services
                    <svg class="w-4 h-4 group-hover:rotate-180 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                  </button>
                  <div class="absolute top-full left-0 mt-1 w-64 bg-white rounded-lg shadow-lg border border-gray-200 invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-300 transform scale-95 group-hover:scale-100">
                    <div class="p-2">
                      <router-link to="/services/appliances" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">General Appliances</router-link>
                      <router-link to="/services/coffee-machines" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Coffee Machines</router-link>
                      <router-link to="/services/dishwashers" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Dishwashers</router-link>
                      <router-link to="/services/washing-machines" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Washing Machines</router-link>
                      <router-link to="/services/hobs" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Hobs</router-link>
                      <router-link to="/services/air-conditioners" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Air Conditioners</router-link>
                      <router-link to="/services/all-electrical" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">All Electrical</router-link>
                      <router-link to="/services/commercial-equipment" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md hover:translate-x-2 transition-all duration-200">Commercial Equipment</router-link>
                    </div>
                  </div>
                </li>                <li>
                  <a href="/#about" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:scale-110 transform duration-200">
                    About
                  </a>
                </li>
                <li>
                  <a href="/#faq" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:scale-110 transform duration-200">
                    FAQ
                  </a>
                </li>                <li>
                  <a href="/#location" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:scale-110 transform duration-200">
                    Location
                  </a>
                </li>
                <li>
                  <a href="/#contact" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:scale-110 transform duration-200">
                    Contact
                  </a>
                </li>
              </ul>
            </nav>
          </div>

          <div class="flex items-center gap-4">
            <div class="sm:flex sm:gap-4">
              <a
                href="/#contact"
                class="professional-btn professional-btn-primary cursor-pointer hover:scale-105 transform transition-all duration-300 hover:shadow-lg"
              >
                Get Service
              </a>

              <div class="hidden sm:flex">
                <a
                  href="/#services"
                  class="professional-btn professional-btn-secondary cursor-pointer hover:scale-105 transform transition-all duration-300 hover:shadow-lg"
                >
                  View Services
                </a>
              </div>
            </div>

            <div class="block md:hidden">
              <button @click="toggleMenu" class="rounded bg-gray-100 p-2 text-gray-600 transition hover:text-gray-600/75 hover:scale-110 transform duration-200 hover:rotate-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="size-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Mobile Menu -->
        <div v-if="isMenuOpen" class="md:hidden mt-4 pb-4 bg-white border-t border-gray-200 animate-slideDown">
          <nav aria-label="Global">
            <ul class="flex flex-col gap-4 text-sm p-4">
              <li><router-link to="/" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Home</router-link></li>
              <li><router-link to="/services/appliances" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">General Appliances</router-link></li>
              <li><router-link to="/services/coffee-machines" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Coffee Machines</router-link></li>
              <li><router-link to="/services/dishwashers" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Dishwashers</router-link></li>
              <li><router-link to="/services/washing-machines" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Washing Machines</router-link></li>
              <li><router-link to="/services/hobs" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Hobs</router-link></li>
              <li><router-link to="/services/air-conditioners" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Air Conditioners</router-link></li>
              <li><router-link to="/services/all-electrical" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">All Electrical</router-link></li>
              <li><router-link to="/services/commercial-equipment" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Commercial Equipment</router-link></li>              <li><a href="/#about" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">About</a></li>
              <li><a href="/#faq" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:translate-x-2 transform duration-200">FAQ</a></li>
              <li><a href="/#location" class="text-gray-600 transition hover:text-brand professional-underline hover:translate-x-2 transform duration-200">Location</a></li>
              <li><a href="/#contact" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer hover:translate-x-2 transform duration-200">Contact</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="pt-16">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="professional-footer relative overflow-hidden">
      <!-- Remove bubble decorations but keep overflow hidden for future use -->
      
      <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="lg:flex lg:items-start lg:gap-8">
          <!-- Main Footer Content -->
          <div class="mt-8 grid grid-cols-1 gap-8 lg:mt-0 lg:grid-cols-4 lg:gap-x-8 lg:gap-y-8">
            
            <!-- Company Information -->
            <div class="col-span-1 lg:col-span-2 animate-fadeInUp" style="animation-delay: 0.1s;">
              <div class="flex items-center space-x-3 mb-6">
                <div class="bg-gradient-to-r from-blue-600 to-blue-700 text-white px-3 py-2 rounded-lg font-bold text-lg">
                  {{ businessConfig.business.name }}
                </div>
              </div>
              
              <p class="text-gray-400 mb-6 max-w-md leading-relaxed">
                {{ businessConfig.business.description }}
              </p>
              
              <!-- Contact Information -->
              <div class="space-y-3">
                <div class="flex items-center space-x-3">
                  <div class="w-5 h-5 bg-blue-100 rounded flex items-center justify-center">
                    <span class="text-xs font-bold text-blue-600">📞</span>
                  </div>
                  <a :href="`tel:${businessConfig.location.contact.phone}`" 
                     class="text-gray-400 hover:text-brand transition duration-200">
                    {{ businessConfig.location.contact.phone }}
                  </a>
                </div>
                
                <div class="flex items-center space-x-3">
                  <div class="w-5 h-5 bg-blue-100 rounded flex items-center justify-center">
                    <span class="text-xs font-bold text-blue-600">✉️</span>
                  </div>
                  <a :href="`mailto:${businessConfig.location.contact.email}`" 
                     class="text-gray-400 hover:text-brand transition duration-200">
                    {{ businessConfig.location.contact.email }}
                  </a>
                </div>
                
                <div class="flex items-start space-x-3">
                  <div class="w-5 h-5 bg-blue-100 rounded flex items-center justify-center mt-1">
                    <span class="text-xs font-bold text-blue-600">📍</span>
                  </div>
                  <span class="text-gray-400 text-sm leading-relaxed">
                    {{ businessConfig.location.address.street }}<br>
                    {{ businessConfig.location.address.city }}, {{ businessConfig.location.address.postcode }}
                  </span>
                </div>
              </div>
            </div>

            <!-- Services -->
            <div class="col-span-1 animate-fadeInUp" style="animation-delay: 0.2s;">
              <p class="font-medium text-white professional-subheading mb-4 hover:scale-105 transform transition-all duration-300">Services</p>

              <ul class="mt-6 space-y-3 text-sm">
                <li>
                  <router-link to="/services/appliances" class="text-gray-400 transition hover:text-brand cursor-pointer hover:translate-x-2 transform duration-200">General Appliances</router-link>
                </li>
                <li>
                  <router-link to="/services/coffee-machines" class="text-gray-400 transition hover:text-brand cursor-pointer hover:translate-x-2 transform duration-200">Coffee Machines</router-link>
                </li>
                <li>
                  <router-link to="/services/dishwashers" class="text-gray-400 transition hover:text-brand cursor-pointer hover:translate-x-2 transform duration-200">Dishwashers</router-link>
                </li>
                <li>
                  <router-link to="/services/washing-machines" class="text-gray-400 transition hover:text-brand cursor-pointer hover:translate-x-2 transform duration-200">Washing Machines</router-link>
                </li>
                <li>
                  <router-link to="/services/hobs" class="text-gray-400 transition hover:text-brand cursor-pointer hover:translate-x-2 transform duration-200">Hobs</router-link>
                </li>
              </ul>
            </div>

            <!-- Business Hours & Service Areas -->
            <div class="col-span-1 animate-fadeInUp" style="animation-delay: 0.3s;">
              <p class="font-medium text-white professional-subheading mb-4 hover:scale-105 transform transition-all duration-300">Business Hours</p>
              
              <div class="mt-6 space-y-2 text-sm">
                <div class="flex justify-between">
                  <span class="text-gray-400">Mon - Fri</span>
                  <span class="text-gray-300">8:00 AM - 6:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-400">Saturday</span>
                  <span class="text-gray-300">9:00 AM - 4:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-400">Sunday</span>
                  <span class="text-gray-300">Closed</span>
                </div>
              </div>

              <p class="font-medium text-white professional-subheading mb-4 mt-8 hover:scale-105 transform transition-all duration-300">Service Areas</p>
              <div class="mt-4 flex flex-wrap gap-2">
                <span v-for="area in businessConfig.business.serviceAreas.slice(0, 3)" :key="area"
                      class="text-xs px-2 py-1 bg-gray-700 text-gray-300 rounded">
                  {{ area }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-12 border-t border-gray-700 pt-8">
          <div class="flex flex-col sm:flex-row sm:justify-between items-center gap-4">
            <div class="professional-card inline-block bg-gray-800 hover:scale-105 transform transition-all duration-300">
              <p class="text-xs text-gray-400">© 2025 {{ businessConfig.business.name }}. Licensed & Insured Family Business</p>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Component-specific styles */
.group:hover .group-hover\:visible {
  visibility: visible;
}

.group:hover .group-hover\:opacity-100 {
  opacity: 1;
}

/* Custom Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-5px);
  }
  60% {
    transform: translateY(-3px);
  }
}

.animate-fadeInUp {
  animation: fadeInUp 0.8s ease-out forwards;
}

.animate-slideDown {
  animation: slideDown 0.3s ease-out;
}

.animate-bounce-hover:hover {
  animation: bounce 1s infinite;
}

/* Enhanced hover effects */
.professional-btn:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

/* Gradient background animation for brand text */
.bg-gradient-to-r {
  background-size: 200% 200%;
  animation: gradientShift 3s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Smooth transitions for all interactive elements */
* {
  transition: all 0.2s ease;
}
</style>
