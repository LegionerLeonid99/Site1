<script setup>
import { ref } from 'vue'

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
            <router-link to="/" class="block text-brand font-bold text-xl">
              🔧 FixIt Appliances
            </router-link>
          </div>

          <div class="hidden md:block">
            <nav aria-label="Global">
              <ul class="flex items-center gap-6 text-sm">
                <li>
                  <router-link to="/" class="text-gray-600 transition hover:text-brand professional-underline">
                    Home
                  </router-link>
                </li>
                <li class="relative group">
                  <button class="text-gray-600 transition hover:text-brand professional-underline flex items-center gap-1">
                    Services
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                  </button>
                  <div class="absolute top-full left-0 mt-1 w-64 bg-white rounded-lg shadow-lg border border-gray-200 invisible group-hover:visible opacity-0 group-hover:opacity-100 transition-all duration-200">
                    <div class="p-2">
                      <router-link to="/services/appliances" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">General Appliances</router-link>
                      <router-link to="/services/coffee-machines" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Coffee Machines</router-link>
                      <router-link to="/services/dishwashers" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Dishwashers</router-link>
                      <router-link to="/services/washing-machines" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Washing Machines</router-link>
                      <router-link to="/services/hobs" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Hobs</router-link>
                      <router-link to="/services/kitchen-ventilators" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Kitchen Ventilators</router-link>
                      <router-link to="/services/all-electrical" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">All Electrical</router-link>
                      <router-link to="/services/commercial-equipment" class="block px-4 py-2 text-sm text-gray-600 hover:text-brand hover:bg-gray-50 rounded-md">Commercial Equipment</router-link>
                    </div>
                  </div>
                </li>                <li>
                  <a href="/#about" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer">
                    About
                  </a>
                </li>
                <li>
                  <router-link to="/faq" class="text-gray-600 transition hover:text-brand professional-underline">
                    FAQ
                  </router-link>
                </li>                <li>
                  <a href="/#testimonials" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer">
                    Testimonials
                  </a>
                </li>
                <li>
                  <a href="/#location" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer">
                    Location
                  </a>
                </li>
                <li>
                  <a href="/#contact" class="text-gray-600 transition hover:text-brand professional-underline cursor-pointer">
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
                class="professional-btn professional-btn-primary cursor-pointer"
              >
                Get Service
              </a>

              <div class="hidden sm:flex">
                <a
                  href="/#services"
                  class="professional-btn professional-btn-secondary cursor-pointer"
                >
                  View Services
                </a>
              </div>
            </div>

            <div class="block md:hidden">
              <button @click="toggleMenu" class="rounded bg-gray-100 p-2 text-gray-600 transition hover:text-gray-600/75">
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
        <div v-if="isMenuOpen" class="md:hidden mt-4 pb-4 bg-white border-t border-gray-200">
          <nav aria-label="Global">
            <ul class="flex flex-col gap-4 text-sm p-4">
              <li><router-link to="/" class="text-gray-600 transition hover:text-brand professional-underline">Home</router-link></li>
              <li><router-link to="/services/appliances" class="text-gray-600 transition hover:text-brand professional-underline">General Appliances</router-link></li>
              <li><router-link to="/services/coffee-machines" class="text-gray-600 transition hover:text-brand professional-underline">Coffee Machines</router-link></li>
              <li><router-link to="/services/dishwashers" class="text-gray-600 transition hover:text-brand professional-underline">Dishwashers</router-link></li>
              <li><router-link to="/services/washing-machines" class="text-gray-600 transition hover:text-brand professional-underline">Washing Machines</router-link></li>
              <li><router-link to="/services/hobs" class="text-gray-600 transition hover:text-brand professional-underline">Hobs</router-link></li>
              <li><router-link to="/services/kitchen-ventilators" class="text-gray-600 transition hover:text-brand professional-underline">Kitchen Ventilators</router-link></li>
              <li><router-link to="/services/all-electrical" class="text-gray-600 transition hover:text-brand professional-underline">All Electrical</router-link></li>
              <li><router-link to="/services/commercial-equipment" class="text-gray-600 transition hover:text-brand professional-underline">Commercial Equipment</router-link></li>              <li><a href="/#about" class="text-gray-600 transition hover:text-brand professional-underline">About</a></li>
              <li><a href="/#location" class="text-gray-600 transition hover:text-brand professional-underline">Location</a></li>
              <li><a href="/#contact" class="text-gray-600 transition hover:text-brand professional-underline">Contact</a></li>
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
    <footer class="professional-footer">
      <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="lg:flex lg:items-start lg:gap-8">
          <div class="text-brand">
            <h2 class="text-2xl font-bold text-brand professional-subheading">🔧 FixIt Appliances</h2>
          </div>

          <div class="mt-8 grid grid-cols-2 gap-8 lg:mt-0 lg:grid-cols-5 lg:gap-y-16">
            <div class="col-span-2">
              <div>
                <h2 class="text-2xl font-bold text-white professional-subheading">Get appliance updates!</h2>
                <p class="mt-4 text-gray-400">
                  Stay informed about maintenance tips and special offers.
                </p>
              </div>
            </div>

            <div class="col-span-2 lg:col-span-3 lg:flex lg:items-end">
              <form class="w-full professional-card p-4">
                <label for="UserEmail" class="block text-sm font-medium text-gray-700 professional-subheading mb-2">Newsletter Signup</label>

                <div class="sm:flex sm:items-center sm:gap-4">
                  <input
                    type="email"
                    id="UserEmail"
                    placeholder="your.email@example.com"
                    class="professional-input flex-1"
                  />

                  <button class="professional-btn professional-btn-primary mt-1 w-full sm:mt-0 sm:w-auto">
                    Sign Up
                  </button>
                </div>
              </form>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-white professional-subheading mb-4">Services</p>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <router-link to="/services/appliances" class="text-gray-400 transition hover:text-brand cursor-pointer">General Appliances</router-link>
                </li>
                <li>
                  <router-link to="/services/coffee-machines" class="text-gray-400 transition hover:text-brand cursor-pointer">Coffee Machines</router-link>
                </li>
                <li>
                  <router-link to="/services/dishwashers" class="text-gray-400 transition hover:text-brand cursor-pointer">Dishwashers</router-link>
                </li>
                <li>
                  <router-link to="/services/commercial-equipment" class="text-gray-400 transition hover:text-brand cursor-pointer">Commercial Equipment</router-link>
                </li>
              </ul>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-white professional-subheading mb-4">Company</p>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <a href="/#about" class="text-gray-400 transition hover:text-brand cursor-pointer">About</a>
                </li>
                <li>
                  <a href="/#testimonials" class="text-gray-400 transition hover:text-brand cursor-pointer">Testimonials</a>
                </li>
                <li>
                  <a href="/#contact" class="text-gray-400 transition hover:text-brand cursor-pointer">Contact</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="mt-8 border-t border-gray-700 pt-8">
          <div class="sm:flex sm:justify-between items-center">
            <div class="professional-card inline-block bg-gray-800">
              <p class="text-xs text-gray-400">© 2025 FixIt Appliances. Made with ❤️ and expert craftsmanship</p>
            </div>

            <ul class="mt-8 flex flex-wrap justify-start gap-4 text-xs sm:mt-0 lg:justify-end">
              <li>
                <a href="#" class="text-gray-400 transition hover:text-brand"> Terms & Conditions </a>
              </li>
              <li>
                <a href="#" class="text-gray-400 transition hover:text-brand"> Privacy Policy </a>
              </li>
              <li>
                <a href="#" class="text-gray-400 transition hover:text-brand"> Cookies </a>
              </li>
            </ul>
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
</style>
