<script setup>
import { ref, onMounted } from 'vue'

// Reactive data
const isMenuOpen = ref(false)
const currentTestimonial = ref(0)

const services = ref([
  {
    icon: '💻',
    title: 'Web Development',
    description: 'Custom websites and web applications built with modern technologies',
    price: 'Starting at $2,500'
  },
  {
    icon: '📱',
    title: 'Mobile App Development',
    description: 'Native and cross-platform mobile applications for iOS and Android',
    price: 'Starting at $5,000'
  },
  {
    icon: '🎨',
    title: 'UI/UX Design',
    description: 'Beautiful and intuitive user interfaces and user experience design',
    price: 'Starting at $1,500'
  },
  {
    icon: '🚀',
    title: 'Digital Marketing',
    description: 'SEO, social media marketing, and online advertising campaigns',
    price: 'Starting at $800/month'
  },
  {
    icon: '☁️',
    title: 'Cloud Solutions',
    description: 'Cloud migration, hosting, and infrastructure management services',
    price: 'Starting at $1,200'
  },
  {
    icon: '🔧',
    title: 'Maintenance & Support',
    description: '24/7 technical support and website maintenance services',
    price: 'Starting at $300/month'
  }
])

const testimonials = ref([
  {
    name: 'Sarah Johnson',
    company: 'TechStart Inc.',
    text: 'Exceptional service! They delivered our project on time and exceeded our expectations.',
    rating: 5
  },
  {
    name: 'Mike Chen',
    company: 'Digital Solutions',
    text: 'Professional team with great communication. Highly recommend their services.',
    rating: 5
  },
  {
    name: 'Emily Rodriguez',
    company: 'Creative Agency',
    text: 'Outstanding results! Our website traffic increased by 300% after their work.',
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
  // In a real application, you would send this data to a server
  alert('Thank you for your inquiry! We will contact you soon.')
  // Reset form
  contactForm.value = {
    name: '',
    email: '',
    service: '',
    message: ''
  }
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
  <div class="app">
    <!-- Navigation - HyperUI Inspired Header -->
    <header class="bg-white shadow-sm">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="md:flex md:items-center md:gap-12">
            <a class="block text-brand font-bold text-xl" href="#">
              🚀 TechServices
            </a>
          </div>

          <div class="hidden md:block">
            <nav aria-label="Global">
              <ul class="flex items-center gap-6 text-sm">
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('home')">
                    Home
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('services')">
                    Services
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('about')">
                    About
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('testimonials')">
                    Testimonials
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('contact')">
                    Contact
                  </a>
                </li>
              </ul>
            </nav>
          </div>

          <div class="flex items-center gap-4">
            <div class="sm:flex sm:gap-4">
              <a
                class="rounded-md bg-brand px-5 py-2.5 text-sm font-medium text-white shadow transition hover:bg-indigo-700 cursor-pointer"
                @click="scrollToSection('contact')"
              >
                Get Started
              </a>

              <div class="hidden sm:flex">
                <a
                  class="rounded-md px-5 py-2.5 text-sm font-medium text-brand border border-brand transition hover:bg-brand hover:text-white cursor-pointer"
                  @click="scrollToSection('services')"
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
        <div v-if="isMenuOpen" class="md:hidden mt-4 pb-4">
          <nav aria-label="Global">
            <ul class="flex flex-col gap-4 text-sm">
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('home')">Home</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('services')">Services</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('about')">About</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('testimonials')">Testimonials</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer" @click="scrollToSection('contact')">Contact</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>

    <!-- Hero Section - HyperUI Inspired -->
    <section id="home" class="bg-gray-50">
      <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
        <div class="mx-auto max-w-xl text-center">
          <h1 class="text-3xl font-extrabold sm:text-5xl">
            Transform Your Business
            <strong class="font-extrabold text-brand sm:block"> with Professional Tech Services </strong>
          </h1>

          <p class="mt-4 sm:text-xl/relaxed">
            We provide cutting-edge web development, mobile apps, and digital solutions to help your business thrive in the digital age.
          </p>

          <div class="mt-8 flex flex-wrap justify-center gap-4">
            <a
              class="block w-full rounded bg-brand px-12 py-3 text-sm font-medium text-white shadow hover:bg-indigo-700 focus:outline-none focus:ring active:bg-red-500 sm:w-auto cursor-pointer"
              @click="scrollToSection('services')"
            >
              Our Services
            </a>

            <a
              class="block w-full rounded px-12 py-3 text-sm font-medium text-brand shadow hover:text-indigo-700 focus:outline-none focus:ring active:text-red-500 sm:w-auto border border-brand hover:bg-brand hover:text-white transition-colors cursor-pointer"
              @click="scrollToSection('contact')"
            >
              Get Quote
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section - HyperUI Inspired Cards -->
    <section id="services" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h2 class="text-3xl font-bold sm:text-4xl">Our Services</h2>
          <p class="mt-4 text-gray-600">
            We offer comprehensive digital solutions tailored to your business needs
          </p>
        </div>

        <div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="service in services" :key="service.title" class="block rounded-xl border border-gray-100 p-8 shadow-xl transition hover:border-brand/10 hover:shadow-brand/10">
            <div class="text-4xl mb-4">{{ service.icon }}</div>
            
            <h2 class="mt-4 text-xl font-bold text-gray-900">{{ service.title }}</h2>
            
            <p class="mt-1 text-sm text-gray-600">
              {{ service.description }}
            </p>

            <div class="mt-4 text-lg font-bold text-brand">{{ service.price }}</div>

            <a class="mt-4 inline-flex items-center gap-1 text-sm font-medium text-blue-600 cursor-pointer hover:text-blue-700">
              Learn More
              <span aria-hidden="true" class="block transition-all group-hover:ms-0.5 rtl:rotate-180">
                &rarr;
              </span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section - HyperUI Inspired -->
    <section id="about" class="bg-gray-50 py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
          <div class="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full">
            <div class="absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center">
              <div class="text-center text-white">
                <div class="text-6xl mb-4">🚀</div>
                <h3 class="text-2xl font-bold">Innovation</h3>
                <p class="text-lg opacity-90">Driving Digital Transformation</p>
              </div>
            </div>
          </div>

          <div class="lg:py-24">
            <h2 class="text-3xl font-bold sm:text-4xl">Why Choose Us?</h2>

            <p class="mt-4 text-gray-600">
              We are dedicated to delivering exceptional results through cutting-edge technology and unmatched expertise.
            </p>

            <div class="mt-8 grid grid-cols-1 gap-8 sm:grid-cols-2">
              <div>
                <div class="flex items-center gap-4">
                  <span class="shrink-0 rounded-lg bg-gray-50 p-4">
                    <div class="text-2xl">🎯</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl">Expert Team</h3>
                    <p class="mt-1 text-gray-600">Our team of experienced developers and designers deliver exceptional results</p>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex items-center gap-4">
                  <span class="shrink-0 rounded-lg bg-gray-50 p-4">
                    <div class="text-2xl">⚡</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl">Fast Delivery</h3>
                    <p class="mt-1 text-gray-600">We pride ourselves on delivering projects on time without compromising quality</p>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex items-center gap-4">
                  <span class="shrink-0 rounded-lg bg-gray-50 p-4">
                    <div class="text-2xl">🔒</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl">Secure & Reliable</h3>
                    <p class="mt-1 text-gray-600">All our solutions are built with security and reliability as top priorities</p>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex items-center gap-4">
                  <span class="shrink-0 rounded-lg bg-gray-50 p-4">
                    <div class="text-2xl">📞</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl">24/7 Support</h3>
                    <p class="mt-1 text-gray-600">Round-the-clock support to ensure your business never stops running</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Stats -->
            <div class="mt-12 grid grid-cols-3 gap-4">
              <div class="text-center">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl">500+</dt>
                <dd class="text-sm text-gray-500">Projects Completed</dd>
              </div>
              <div class="text-center">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl">98%</dt>
                <dd class="text-sm text-gray-500">Client Satisfaction</dd>
              </div>
              <div class="text-center">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl">5+</dt>
                <dd class="text-sm text-gray-500">Years Experience</dd>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section - HyperUI Inspired -->
    <section id="testimonials" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-center text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
          What Our Clients Say
        </h2>

        <div class="mt-12 grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-8">
          <blockquote v-for="(testimonial, index) in testimonials" :key="index" class="rounded-lg bg-gray-50 p-6 shadow-sm sm:p-8">
            <div class="flex items-center gap-4">
              <div>
                <div class="flex justify-center gap-0.5 text-green-500 mb-4">
                  <svg v-for="star in testimonial.rating" :key="star" class="size-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                </div>

                <p class="mt-0.5 text-lg font-medium text-gray-900">{{ testimonial.name }}</p>
                <p class="text-sm text-gray-500">{{ testimonial.company }}</p>
              </div>
            </div>

            <p class="mt-4 text-gray-700">
              "{{ testimonial.text }}"
            </p>
          </blockquote>
        </div>
      </div>
    </section>

    <!-- Contact Section - HyperUI Inspired -->
    <section id="contact" class="bg-white py-24">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h1 class="text-2xl font-bold sm:text-3xl">Get In Touch</h1>
          <p class="mt-4 text-gray-500">
            Ready to start your project? Contact us today for a free consultation
          </p>
        </div>

        <div class="mx-auto mt-16 max-w-xl">
          <form @submit.prevent="submitForm" class="mb-0 mt-6 space-y-4 rounded-lg p-4 shadow-lg sm:p-6 lg:p-8">
            <div>
              <label for="name" class="sr-only">Name</label>
              <div class="relative">
                <input
                  v-model="contactForm.name"
                  type="text"
                  id="name"
                  required
                  class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
                  placeholder="Your Name"
                />
                <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="size-4 text-gray-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    />
                  </svg>
                </span>
              </div>
            </div>

            <div>
              <label for="email" class="sr-only">Email</label>
              <div class="relative">
                <input
                  v-model="contactForm.email"
                  type="email"
                  id="email"
                  required
                  class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm"
                  placeholder="Your Email"
                />
                <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="size-4 text-gray-400"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                    />
                  </svg>
                </span>
              </div>
            </div>

            <div>
              <label for="service" class="sr-only">Service</label>
              <select
                v-model="contactForm.service"
                id="service"
                required
                class="w-full rounded-lg border-gray-200 p-4 text-sm shadow-sm"
              >
                <option value="">Select a Service</option>
                <option v-for="service in services" :key="service.title" :value="service.title">
                  {{ service.title }}
                </option>
              </select>
            </div>

            <div>
              <label for="message" class="sr-only">Message</label>
              <textarea
                v-model="contactForm.message"
                id="message"
                rows="6"
                required
                class="w-full rounded-lg border-gray-200 p-4 text-sm shadow-sm resize-none"
                placeholder="Tell us about your project"
              ></textarea>
            </div>

            <button
              type="submit"
              class="block w-full rounded-lg bg-brand px-5 py-3 text-sm font-medium text-white hover:bg-indigo-700 transition-colors"
            >
              Send Message
            </button>
          </form>

          <!-- Contact Info -->
          <div class="mt-12 grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div class="text-center">
              <div class="text-2xl mb-2">📧</div>
              <h3 class="text-sm font-medium text-gray-900">Email</h3>
              <p class="text-sm text-gray-600">hello@techservices.com</p>
            </div>
            <div class="text-center">
              <div class="text-2xl mb-2">📞</div>
              <h3 class="text-sm font-medium text-gray-900">Phone</h3>
              <p class="text-sm text-gray-600">+1 (555) 123-4567</p>
            </div>
            <div class="text-center">
              <div class="text-2xl mb-2">📍</div>
              <h3 class="text-sm font-medium text-gray-900">Location</h3>
              <p class="text-sm text-gray-600">Digital City, DC</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer - HyperUI Inspired -->
    <footer class="bg-gray-50">
      <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="lg:flex lg:items-start lg:gap-8">
          <div class="text-teal-600">
            <h2 class="text-2xl font-bold text-brand">🚀 TechServices</h2>
          </div>

          <div class="mt-8 grid grid-cols-2 gap-8 lg:mt-0 lg:grid-cols-5 lg:gap-y-16">
            <div class="col-span-2">
              <div>
                <h2 class="text-2xl font-bold text-gray-900">Get the latest updates!</h2>

                <p class="mt-4 text-gray-500">
                  Stay informed about our latest services and industry insights.
                </p>
              </div>
            </div>

            <div class="col-span-2 lg:col-span-3 lg:flex lg:items-end">
              <form class="w-full">
                <label for="UserEmail" class="sr-only"> Email </label>

                <div class="border border-gray-100 p-2 focus-within:ring sm:flex sm:items-center sm:gap-4">
                  <input
                    type="email"
                    id="UserEmail"
                    placeholder="john@rhcp.com"
                    class="w-full border-none focus:border-transparent focus:ring-transparent sm:text-sm"
                  />

                  <button
                    class="mt-1 w-full bg-brand px-6 py-3 text-sm font-bold uppercase tracking-wide text-white transition-none hover:bg-indigo-700 sm:mt-0 sm:w-auto sm:shrink-0"
                  >
                    Sign Up
                  </button>
                </div>
              </form>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-gray-900">Services</p>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('services')"> Web Development </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('services')"> Mobile Apps </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('services')"> UI/UX Design </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('services')"> Digital Marketing </a>
                </li>
              </ul>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-gray-900">Company</p>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('about')"> About </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('testimonials')"> Testimonials </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer" @click="scrollToSection('contact')"> Contact </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="mt-8 border-t border-gray-100 pt-8">
          <div class="sm:flex sm:justify-between">
            <p class="text-xs text-gray-500">&copy; 2025. TechServices. All rights reserved.</p>

            <ul class="mt-8 flex flex-wrap justify-start gap-4 text-xs sm:mt-0 lg:justify-end">
              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75"> Terms & Conditions </a>
              </li>

              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75"> Privacy Policy </a>
              </li>

              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75"> Cookies </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Only component-specific styles that can't be achieved with Tailwind */
</style>
