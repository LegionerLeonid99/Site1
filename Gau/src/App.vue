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
    <!-- Navigation -->
    <nav class="bg-white shadow-lg fixed top-0 w-full z-50">
      <div class="max-w-6xl mx-auto px-5">
        <div class="flex justify-between items-center h-16">
          <div class="flex items-center">
            <h2 class="text-2xl font-bold text-brand">🚀 TechServices</h2>
          </div>
          <div class="nav-menu" :class="{ active: isMenuOpen }">
            <a href="#home" @click="scrollToSection('home')" class="text-gray-800 hover:text-brand font-medium transition-colors duration-300">Home</a>
            <a href="#services" @click="scrollToSection('services')" class="text-gray-800 hover:text-brand font-medium transition-colors duration-300">Services</a>
            <a href="#about" @click="scrollToSection('about')" class="text-gray-800 hover:text-brand font-medium transition-colors duration-300">About</a>
            <a href="#testimonials" @click="scrollToSection('testimonials')" class="text-gray-800 hover:text-brand font-medium transition-colors duration-300">Testimonials</a>
            <a href="#contact" @click="scrollToSection('contact')" class="text-gray-800 hover:text-brand font-medium transition-colors duration-300">Contact</a>
          </div>
          <div class="nav-toggle" @click="toggleMenu">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-gradient min-h-screen flex items-center text-white px-5 pt-16">
      <div class="max-w-6xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h1 class="text-4xl lg:text-6xl font-bold mb-6 leading-tight">Transform Your Business with Professional Tech Services</h1>
            <p class="text-lg lg:text-xl mb-8 opacity-90">We provide cutting-edge web development, mobile apps, and digital solutions to help your business thrive in the digital age.</p>
            <div class="flex flex-col sm:flex-row gap-5">
              <button @click="scrollToSection('services')" class="btn-primary-custom">Our Services</button>
              <button @click="scrollToSection('contact')" class="btn-secondary-custom">Get Quote</button>
            </div>
          </div>
          <div class="flex justify-center items-center">
            <div class="floating-card backdrop-blur-custom rounded-3xl p-8 text-center">
              <div class="text-4xl mb-4">💡</div>
              <h3 class="text-2xl font-bold mb-2">Innovation</h3>
              <p class="text-lg opacity-90">Latest Technologies</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-5">
        <h2 class="text-4xl lg:text-5xl font-bold text-center mb-6 text-gray-900">Our Services</h2>
        <p class="text-center text-gray-600 mb-16 text-lg max-w-3xl mx-auto">We offer comprehensive digital solutions tailored to your business needs</p>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="service in services" :key="service.title" class="service-card">
            <div class="text-5xl mb-6">{{ service.icon }}</div>
            <h3 class="text-2xl font-bold mb-4 text-gray-900">{{ service.title }}</h3>
            <p class="text-gray-600 mb-6 leading-relaxed">{{ service.description }}</p>
            <div class="text-xl font-bold text-brand mb-6">{{ service.price }}</div>
            <button class="btn-outline-custom">Learn More</button>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-20">
      <div class="max-w-6xl mx-auto px-5">
        <div class="grid lg:grid-cols-3 gap-16 items-center">
          <div class="lg:col-span-2">
            <h2 class="text-4xl lg:text-5xl font-bold mb-12 text-gray-900">Why Choose Us?</h2>
            <div class="grid md:grid-cols-2 gap-8">
              <div class="space-y-4">
                <h3 class="text-2xl font-bold text-gray-900">🎯 Expert Team</h3>
                <p class="text-gray-600 leading-relaxed">Our team of experienced developers and designers deliver exceptional results</p>
              </div>
              <div class="space-y-4">
                <h3 class="text-2xl font-bold text-gray-900">⚡ Fast Delivery</h3>
                <p class="text-gray-600 leading-relaxed">We pride ourselves on delivering projects on time without compromising quality</p>
              </div>
              <div class="space-y-4">
                <h3 class="text-2xl font-bold text-gray-900">🔒 Secure & Reliable</h3>
                <p class="text-gray-600 leading-relaxed">All our solutions are built with security and reliability as top priorities</p>
              </div>
              <div class="space-y-4">
                <h3 class="text-2xl font-bold text-gray-900">📞 24/7 Support</h3>
                <p class="text-gray-600 leading-relaxed">Round-the-clock support to ensure your business never stops running</p>
              </div>
            </div>
          </div>
          <div class="flex flex-col gap-8">
            <div class="bg-gray-50 p-8 rounded-2xl text-center">
              <h3 class="text-4xl font-bold text-brand mb-3">500+</h3>
              <p class="text-gray-600 font-medium">Projects Completed</p>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl text-center">
              <h3 class="text-4xl font-bold text-brand mb-3">98%</h3>
              <p class="text-gray-600 font-medium">Client Satisfaction</p>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl text-center">
              <h3 class="text-4xl font-bold text-brand mb-3">5+</h3>
              <p class="text-gray-600 font-medium">Years Experience</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-5">
        <h2 class="text-4xl lg:text-5xl font-bold text-center mb-16 text-gray-900">What Our Clients Say</h2>
        <div class="testimonial-slider max-w-4xl mx-auto">
          <div class="testimonial text-center" v-for="(testimonial, index) in testimonials" :key="index" 
               :class="{ active: index === currentTestimonial }">
            <div class="flex justify-center gap-1 mb-6">
              <span v-for="star in testimonial.rating" :key="star" class="text-2xl">⭐</span>
            </div>
            <p class="text-xl lg:text-2xl text-gray-900 mb-8 italic leading-relaxed">"{{ testimonial.text }}"</p>
            <div>
              <h4 class="text-xl font-bold text-brand mb-2">{{ testimonial.name }}</h4>
              <span class="text-gray-600">{{ testimonial.company }}</span>
            </div>
          </div>
        </div>
        <div class="flex justify-center gap-3 mt-12">
          <button v-for="(testimonial, index) in testimonials" :key="index"
                  @click="currentTestimonial = index"
                  :class="{ active: index === currentTestimonial }"
                  class="testimonial-dot"></button>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-20">
      <div class="max-w-6xl mx-auto px-5">
        <h2 class="text-4xl lg:text-5xl font-bold text-center mb-6 text-gray-900">Get In Touch</h2>
        <p class="text-center text-gray-600 mb-16 text-lg max-w-3xl mx-auto">Ready to start your project? Contact us today for a free consultation</p>
        <div class="grid lg:grid-cols-2 gap-16">
          <div class="space-y-8">
            <div class="flex items-start space-x-4">
              <div class="text-3xl">📧</div>
              <div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">Email</h3>
                <p class="text-gray-600">hello@techservices.com</p>
              </div>
            </div>
            <div class="flex items-start space-x-4">
              <div class="text-3xl">📞</div>
              <div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">Phone</h3>
                <p class="text-gray-600">+1 (555) 123-4567</p>
              </div>
            </div>
            <div class="flex items-start space-x-4">
              <div class="text-3xl">📍</div>
              <div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">Location</h3>
                <p class="text-gray-600">123 Tech Street, Digital City, DC 12345</p>
              </div>
            </div>
          </div>
          <form @submit.prevent="submitForm" class="bg-gray-50 p-8 lg:p-12 rounded-2xl">
            <div class="space-y-6">
              <div>
                <input v-model="contactForm.name" type="text" placeholder="Your Name" required class="form-input">
              </div>
              <div>
                <input v-model="contactForm.email" type="email" placeholder="Your Email" required class="form-input">
              </div>
              <div>
                <select v-model="contactForm.service" required class="form-input">
                  <option value="">Select a Service</option>
                  <option v-for="service in services" :key="service.title" :value="service.title">
                    {{ service.title }}
                  </option>
                </select>
              </div>
              <div>
                <textarea v-model="contactForm.message" placeholder="Tell us about your project" rows="5" required class="form-input"></textarea>
              </div>
              <button type="submit" class="w-full bg-brand text-white py-4 px-8 rounded-lg font-semibold hover:bg-indigo-700 transition-colors duration-300">Send Message</button>
            </div>
          </form>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-16">
      <div class="max-w-6xl mx-auto px-5">
        <div class="grid md:grid-cols-3 gap-12 mb-12">
          <div>
            <h3 class="text-2xl font-bold text-brand mb-6">🚀 TechServices</h3>
            <p class="text-gray-400 leading-relaxed">Transforming businesses through innovative technology solutions.</p>
          </div>
          <div>
            <h4 class="text-xl font-bold mb-6">Quick Links</h4>
            <div class="space-y-3">
              <a href="#home" @click="scrollToSection('home')" class="block text-gray-400 hover:text-brand transition-colors duration-300">Home</a>
              <a href="#services" @click="scrollToSection('services')" class="block text-gray-400 hover:text-brand transition-colors duration-300">Services</a>
              <a href="#about" @click="scrollToSection('about')" class="block text-gray-400 hover:text-brand transition-colors duration-300">About</a>
              <a href="#contact" @click="scrollToSection('contact')" class="block text-gray-400 hover:text-brand transition-colors duration-300">Contact</a>
            </div>
          </div>
          <div>
            <h4 class="text-xl font-bold mb-6">Follow Us</h4>
            <div class="flex space-x-4">
              <a href="#" class="text-gray-400 hover:text-brand transition-colors duration-300">Facebook</a>
              <a href="#" class="text-gray-400 hover:text-brand transition-colors duration-300">Twitter</a>
              <a href="#" class="text-gray-400 hover:text-brand transition-colors duration-300">LinkedIn</a>
              <a href="#" class="text-gray-400 hover:text-brand transition-colors duration-300">Instagram</a>
            </div>
          </div>
        </div>
        <div class="border-t border-gray-700 pt-8 text-center">
          <p class="text-gray-400">&copy; 2025 TechServices. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Only component-specific styles that can't be achieved with Tailwind */
</style>
