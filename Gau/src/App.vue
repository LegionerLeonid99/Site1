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
  // Add loading state
  const button = document.querySelector('button[type="submit"]')
  button.classList.add('doodle-loading')
  button.textContent = 'Sending...'
  
  // Simulate sending (in a real application, you would send this data to a server)
  setTimeout(() => {
    alert('🎉 Thank you for your inquiry! We will contact you soon. 🚀')
    
    // Reset form
    contactForm.value = {
      name: '',
      email: '',
      service: '',
      message: ''
    }
    
    // Reset button
    button.classList.remove('doodle-loading')
    button.innerHTML = 'Send Message 🚀 <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>'
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
  <div class="app">
    <!-- Navigation - Doodle Style Header -->
    <header class="doodle-nav bg-white shadow-sm">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="md:flex md:items-center md:gap-12">
            <a class="block text-brand font-bold text-xl text-doodle doodle-wiggle" href="#">
              🚀 TechServices
              <span class="doodle-star" style="top: -10px; right: -15px;">✨</span>
            </a>
          </div>

          <div class="hidden md:block">
            <nav aria-label="Global">
              <ul class="flex items-center gap-6 text-sm">
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('home')">
                    Home 🏠
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('services')">
                    Services 🛠️
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('about')">
                    About 👥
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('testimonials')">
                    Testimonials 💬
                  </a>
                </li>
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('contact')">
                    Contact 📞
                  </a>
                </li>
              </ul>
            </nav>
          </div>

          <div class="flex items-center gap-4">
            <div class="sm:flex sm:gap-4">
              <button
                class="doodle-btn doodle-btn-primary cursor-pointer"
                @click="scrollToSection('contact')"
              >
                Get Started 🎯
              </button>

              <div class="hidden sm:flex">
                <button
                  class="doodle-btn doodle-btn-secondary cursor-pointer"
                  @click="scrollToSection('services')"
                >
                  View Services 🔍
                </button>
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
        <div v-if="isMenuOpen" class="md:hidden mt-4 pb-4 doodle-border bg-white">
          <nav aria-label="Global">
            <ul class="flex flex-col gap-4 text-sm">
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('home')">🏠 Home</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('services')">🛠️ Services</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('about')">👥 About</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('testimonials')">💬 Testimonials</a></li>
              <li><a class="text-gray-500 transition hover:text-gray-500/75 cursor-pointer doodle-underline" @click="scrollToSection('contact')">📞 Contact</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>

    <!-- Hero Section - Doodle Style -->
    <section id="home" class="bg-gray-50 bg-doodle-lines relative overflow-hidden">
      <div class="absolute top-10 left-10 doodle-star text-4xl">⭐</div>
      <div class="absolute top-20 right-20 doodle-star text-2xl" style="animation-delay: 1s;">🌟</div>
      <div class="absolute bottom-20 left-1/4 doodle-star text-3xl" style="animation-delay: 2s;">✨</div>
      
      <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
        <div class="mx-auto max-w-xl text-center relative">
          <div class="doodle-squiggle absolute -top-10 left-1/2 transform -translate-x-1/2"></div>
          
          <h1 class="text-3xl font-extrabold sm:text-5xl text-doodle text-doodle-large">
            <span class="doodle-highlight">Transform Your Business</span> 🚀
            <strong class="font-extrabold text-brand sm:block doodle-bounce"> with Professional Tech Services </strong>
          </h1>

          <div class="doodle-thought mt-8 relative">
            <p class="sm:text-xl/relaxed text-doodle">
              We provide cutting-edge web development, mobile apps, and digital solutions to help your business thrive in the digital age! ✨
            </p>
            <div class="absolute -top-5 -right-5 doodle-emoji-float">🎯</div>
          </div>

          <div class="mt-8 flex flex-wrap justify-center gap-4">
            <button
              class="doodle-btn doodle-btn-primary text-lg px-8 py-4 cursor-pointer"
              @click="scrollToSection('services')"
            >
              Our Services 🎯
            </button>

            <button
              class="doodle-btn doodle-btn-secondary text-lg px-8 py-4 cursor-pointer"
              @click="scrollToSection('contact')"
            >
              Get Quote 💰
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section - Doodle Style Cards -->
    <section id="services" class="bg-white py-24 bg-doodle-dots relative">
      <div class="absolute top-10 right-10 doodle-star text-3xl">🎨</div>
      <div class="absolute bottom-10 left-10 doodle-star text-2xl" style="animation-delay: 1.5s;">🔧</div>
      
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h2 class="text-3xl font-bold sm:text-4xl text-doodle">Our Services 🛠️</h2>
          <div class="doodle-squiggle mx-auto mt-4"></div>
          <p class="mt-6 text-gray-600 text-doodle">
            We offer comprehensive digital solutions tailored to your business needs
          </p>
        </div>

        <div class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div v-for="(service, index) in services" :key="service.title" 
               :class="['doodle-card', 'floating-card', 'relative', 'doodle-interactive', 'doodle-stamp']" 
               :style="{ animationDelay: index * 0.2 + 's' }">
            <div class="text-4xl mb-4 doodle-bounce">{{ service.icon }}</div>
            
            <h2 class="mt-4 text-xl font-bold text-gray-900 text-doodle doodle-underline">{{ service.title }}</h2>
            
            <p class="mt-1 text-sm text-gray-600 mb-4">
              {{ service.description }}
            </p>
            
            <div class="mt-4 p-3 bg-yellow-100 rounded-lg border-2 border-dashed border-yellow-400 doodle-confetti">
              <p class="text-lg font-bold text-green-600 text-doodle">{{ service.price }}</p>
            </div>
            
            <div class="absolute -top-2 -right-2 doodle-star text-yellow-400">⭐</div>
            <div class="absolute top-5 right-5 doodle-scribble"></div>

            <button class="mt-4 doodle-btn text-sm cursor-pointer hover:scale-105 transition-transform doodle-arrow">
              Learn More 👀
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section - Doodle Style -->
    <section id="about" class="bg-gray-50 py-24 bg-doodle-lines relative overflow-hidden">
      <div class="absolute top-5 left-5 doodle-star text-4xl">🎨</div>
      <div class="absolute top-5 right-5 doodle-star text-3xl" style="animation-delay: 0.5s;">🚀</div>
      <div class="absolute bottom-5 left-1/3 doodle-star text-2xl" style="animation-delay: 1s;">⚡</div>
      
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
          <div class="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full">
            <div class="doodle-border absolute inset-0 bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center">
              <div class="text-center text-white">
                <div class="text-6xl mb-4 doodle-bounce">🚀</div>
                <h3 class="text-2xl font-bold text-doodle">Innovation</h3>
                <p class="text-lg opacity-90">Driving Digital Transformation ✨</p>
              </div>
            </div>
          </div>

          <div class="lg:py-24">
            <h2 class="text-3xl font-bold sm:text-4xl text-doodle">Why Choose Us? 🤔</h2>
            <div class="doodle-squiggle mt-4"></div>

            <div class="doodle-speech mt-6">
              <p class="text-gray-600 text-doodle">
                We are dedicated to delivering exceptional results through cutting-edge technology and unmatched expertise! 💪
              </p>
            </div>

            <div class="mt-8 grid grid-cols-1 gap-8 sm:grid-cols-2">
              <div class="doodle-card">
                <div class="flex items-center gap-4">
                  <span class="shrink-0 doodle-border p-4 bg-yellow-100">
                    <div class="text-2xl doodle-wiggle">🎯</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl text-doodle">Expert Team</h3>
                    <p class="mt-1 text-gray-600">Our team of experienced developers and designers deliver exceptional results</p>
                  </div>
                </div>
              </div>

              <div class="doodle-card">
                <div class="flex items-center gap-4">
                  <span class="shrink-0 doodle-border p-4 bg-blue-100">
                    <div class="text-2xl doodle-bounce">⚡</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl text-doodle">Fast Delivery</h3>
                    <p class="mt-1 text-gray-600">We pride ourselves on delivering projects on time without compromising quality</p>
                  </div>
                </div>
              </div>

              <div class="doodle-card">
                <div class="flex items-center gap-4">
                  <span class="shrink-0 doodle-border p-4 bg-green-100">
                    <div class="text-2xl doodle-wiggle">🔒</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl text-doodle">Secure & Reliable</h3>
                    <p class="mt-1 text-gray-600">All our solutions are built with security and reliability as top priorities</p>
                  </div>
                </div>
              </div>

              <div class="doodle-card">
                <div class="flex items-center gap-4">
                  <span class="shrink-0 doodle-border p-4 bg-purple-100">
                    <div class="text-2xl doodle-bounce">📞</div>
                  </span>
                  <div>
                    <h3 class="text-lg font-medium sm:text-xl text-doodle">24/7 Support</h3>
                    <p class="mt-1 text-gray-600">Round-the-clock support to ensure your business never stops running</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Stats -->
            <div class="mt-12 grid grid-cols-3 gap-4">
              <div class="text-center doodle-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl text-doodle doodle-bounce">500+ 🎯</dt>
                <dd class="text-sm text-gray-500">Projects Completed</dd>
              </div>
              <div class="text-center doodle-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl text-doodle doodle-wiggle">98% 😊</dt>
                <dd class="text-sm text-gray-500">Client Satisfaction</dd>
              </div>
              <div class="text-center doodle-card">
                <dt class="text-3xl font-extrabold text-brand md:text-4xl text-doodle doodle-bounce">5+ 🚀</dt>
                <dd class="text-sm text-gray-500">Years Experience</dd>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section - Doodle Style -->
    <section id="testimonials" class="bg-white py-24 bg-doodle-dots relative overflow-hidden">
      <div class="absolute top-10 left-10 doodle-star text-3xl">💬</div>
      <div class="absolute top-10 right-10 doodle-star text-2xl" style="animation-delay: 0.8s;">🌟</div>
      <div class="absolute bottom-10 left-1/2 doodle-star text-4xl" style="animation-delay: 1.5s;">❤️</div>
      
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-center text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl text-doodle">
          What Our Clients Say 💭
        </h2>
        <div class="doodle-squiggle mx-auto mt-6"></div>

        <div class="mt-12 grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-8">
          <div v-for="(testimonial, index) in testimonials" :key="index" 
               :class="['doodle-speech', 'floating-card', 'relative', 'doodle-interactive', 'doodle-paper']"
               :style="{ animationDelay: index * 0.3 + 's' }">
            <div class="flex items-center gap-4">
              <div class="doodle-border p-3 bg-gradient-to-r from-pink-200 to-blue-200 doodle-wiggle">
                <div class="text-2xl">👤</div>
              </div>
              <div>
                <div class="flex justify-center gap-0.5 text-yellow-400 mb-2">
                  <span v-for="star in testimonial.rating" :key="star" class="text-xl doodle-star">⭐</span>
                </div>

                <p class="mt-0.5 text-lg font-medium text-gray-900 text-doodle doodle-highlight">{{ testimonial.name }}</p>
                <p class="text-sm text-gray-500">{{ testimonial.company }} 🏢</p>
              </div>
            </div>

            <p class="mt-4 text-gray-700 font-medium">
              "{{ testimonial.text }}" 
            </p>
            <div class="absolute -top-3 -right-3 doodle-star text-yellow-400">✨</div>
            <div class="absolute bottom-5 left-5 doodle-emoji-float">💖</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section - Doodle Style -->
    <section id="contact" class="bg-white py-24 bg-doodle-lines relative overflow-hidden">
      <div class="absolute top-5 left-5 doodle-star text-4xl">📧</div>
      <div class="absolute top-5 right-5 doodle-star text-3xl" style="animation-delay: 0.7s;">📞</div>
      <div class="absolute bottom-5 right-1/4 doodle-star text-2xl" style="animation-delay: 1.2s;">✉️</div>
      
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="mx-auto max-w-lg text-center">
          <h1 class="text-2xl font-bold sm:text-3xl text-doodle">Get In Touch 📞</h1>
          <div class="doodle-squiggle mx-auto mt-4"></div>
          <div class="doodle-speech mt-6">
            <p class="text-gray-500 text-doodle">
              Ready to start your project? Contact us today for a free consultation! 🚀
            </p>
          </div>
        </div>

        <div class="mx-auto mt-16 max-w-xl">
          <form @submit.prevent="submitForm" class="doodle-border mb-0 mt-6 space-y-6 p-6 bg-gradient-to-r from-blue-50 to-purple-50">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 text-doodle mb-2">Your Name 👤</label>
              <div class="relative">
                <input
                  v-model="contactForm.name"
                  type="text"
                  id="name"
                  required
                  class="doodle-input w-full"
                  placeholder="Enter your awesome name..."
                />
                <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
                  <div class="text-gray-400 text-xl">😊</div>
                </span>
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 text-doodle mb-2">Email Address 📧</label>
              <div class="relative">
                <input
                  v-model="contactForm.email"
                  type="email"
                  id="email"
                  required
                  class="doodle-input w-full"
                  placeholder="your.email@example.com"
                />
                <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
                  <div class="text-gray-400 text-xl">📬</div>
                </span>
              </div>
            </div>

            <div>
              <label for="service" class="block text-sm font-medium text-gray-700 text-doodle mb-2">Service Needed 🛠️</label>
              <select
                v-model="contactForm.service"
                id="service"
                required
                class="doodle-input w-full"
              >
                <option value="">Select a service...</option>
                <option value="web">Web Development 💻</option>
                <option value="mobile">Mobile App Development 📱</option>
                <option value="design">UI/UX Design 🎨</option>
                <option value="marketing">Digital Marketing 🚀</option>
                <option value="cloud">Cloud Solutions ☁️</option>
                <option value="support">Maintenance & Support 🔧</option>
              </select>
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 text-doodle mb-2">Project Details 📝</label>
              <textarea
                v-model="contactForm.message"
                id="message"
                rows="4"
                required
                class="doodle-input w-full"
                placeholder="Tell us about your amazing project idea..."
              ></textarea>
            </div>

            <button
              type="submit"
              class="doodle-btn doodle-btn-primary w-full text-lg py-4 group"
            >
              Send Message 🚀
              <span class="ml-2 group-hover:translate-x-1 transition-transform inline-block">→</span>
            </button>
          </form>
        </div>
      </div>
    </section>

    <!-- Footer - Doodle Style -->
    <footer class="bg-gray-50 bg-doodle-lines relative overflow-hidden">
      <div class="absolute top-5 left-5 doodle-star text-3xl">🌟</div>
      <div class="absolute top-5 right-5 doodle-star text-2xl" style="animation-delay: 0.5s;">💫</div>
      <div class="absolute bottom-5 left-1/3 doodle-star text-4xl" style="animation-delay: 1s;">⭐</div>
      
      <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="lg:flex lg:items-start lg:gap-8">
          <div class="text-teal-600">
            <h2 class="text-2xl font-bold text-brand text-doodle doodle-wiggle">🚀 TechServices</h2>
            <div class="doodle-squiggle mt-2"></div>
          </div>

          <div class="mt-8 grid grid-cols-2 gap-8 lg:mt-0 lg:grid-cols-5 lg:gap-y-16">
            <div class="col-span-2">
              <div class="doodle-speech">
                <h2 class="text-2xl font-bold text-gray-900 text-doodle">Get the latest updates! 📬</h2>

                <p class="mt-4 text-gray-500">
                  Stay informed about our latest services and industry insights. ✨
                </p>
              </div>
            </div>

            <div class="col-span-2 lg:col-span-3 lg:flex lg:items-end">
              <form class="w-full doodle-border p-4 bg-white">
                <label for="UserEmail" class="block text-sm font-medium text-gray-700 text-doodle mb-2">Newsletter Signup 📰</label>

                <div class="sm:flex sm:items-center sm:gap-4">
                  <input
                    type="email"
                    id="UserEmail"
                    placeholder="your.email@example.com"
                    class="doodle-input flex-1"
                  />

                  <button
                    class="doodle-btn doodle-btn-primary mt-1 w-full sm:mt-0 sm:w-auto"
                  >
                    Sign Up 📧
                  </button>
                </div>
              </form>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-gray-900 text-doodle mb-4">Services 🛠️</p>
              <div class="doodle-squiggle mb-4"></div>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('services')"> 💻 Web Development </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('services')"> 📱 Mobile Apps </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('services')"> 🎨 UI/UX Design </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('services')"> 🚀 Digital Marketing </a>
                </li>
              </ul>
            </div>

            <div class="col-span-1">
              <p class="font-medium text-gray-900 text-doodle mb-4">Company 🏢</p>
              <div class="doodle-squiggle mb-4"></div>

              <ul class="mt-6 space-y-4 text-sm">
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('about')"> 👥 About </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('testimonials')"> 💬 Testimonials </a>
                </li>
                <li>
                  <a href="#" class="text-gray-700 transition hover:opacity-75 cursor-pointer hover:text-brand" @click="scrollToSection('contact')"> 📞 Contact </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="mt-8 border-t border-gray-100 pt-8">
          <div class="sm:flex sm:justify-between items-center">
            <div class="doodle-card inline-block">
              <p class="text-xs text-gray-500 text-doodle">© 2025 TechServices. Made with ❤️ and lots of ☕</p>
            </div>

            <ul class="mt-8 flex flex-wrap justify-start gap-4 text-xs sm:mt-0 lg:justify-end">
              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75 hover:text-brand"> 📜 Terms & Conditions </a>
              </li>

              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75 hover:text-brand"> 🔒 Privacy Policy </a>
              </li>

              <li>
                <a href="#" class="text-gray-500 transition hover:opacity-75 hover:text-brand"> 🍪 Cookies </a>
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
