<script setup>
import { ref } from 'vue'
import Layout from '../components/Layout.vue'

// FAQ data structure - add your FAQ items here
const faqs = ref([
  // Add FAQ items like this:
  // {
  //   question: "Your question here?",
  //   answer: "Your detailed answer here. You can include multiple paragraphs and formatting."
  // },
  
  // Example FAQ structure (remove these comments and add real content):
  // {
  //   question: "How quickly can you repair my appliance?",
  //   answer: "Most repairs are completed the same day. Our technicians carry common parts and tools to fix most issues on the first visit."
  // },
  // {
  //   question: "Do you provide warranty on repairs?",
  //   answer: "Yes, we provide a comprehensive 90-day warranty on all parts and labor for your peace of mind."
  // }
])

// Categories for organizing FAQs (optional)
const faqCategories = ref([
  // Add categories like this:
  // {
  //   name: "General Questions",
  //   faqs: [
  //     // Reference to FAQ items by index or create separate arrays
  //   ]
  // },
  // {
  //   name: "Service & Repairs",
  //   faqs: [
  //     // Reference to FAQ items
  //   ]
  // }
])

// Function to toggle FAQ answers
const toggleFaq = (index) => {
  // Add functionality to show/hide FAQ answers
  // You can use Vue's reactivity to manage open/closed state
}
</script>

<template>
  <Layout>
    <!-- Hero Section -->
    <section class="hero-gradient py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-4xl font-bold sm:text-6xl professional-heading text-white">
            Frequently Asked Questions
          </h1>
          <p class="mt-6 text-xl text-white opacity-90">
            Find answers to common questions about our appliance repair services
          </p>
          <!-- Uncomment to add a search box -->
          <!--
          <div class="mt-8 max-w-md mx-auto">
            <input 
              type="text" 
              placeholder="Search FAQs..." 
              class="professional-input bg-white"
            />
          </div>
          -->
        </div>
      </div>
    </section>

    <!-- FAQ Content Section -->
    <section class="bg-white py-24">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        
        <!-- Uncomment to add Quick Links Section -->
        <!--
        <div class="mb-16">
          <h2 class="text-2xl font-bold professional-heading mb-8 text-center">Quick Links</h2>
          <div class="grid grid-cols-2 gap-4 md:grid-cols-4">
            <a href="#general" class="professional-card text-center py-4 hover:bg-blue-50">
              <div class="text-2xl mb-2">❓</div>
              <p class="font-medium">General Questions</p>
            </a>
            <a href="#service" class="professional-card text-center py-4 hover:bg-blue-50">
              <div class="text-2xl mb-2">🔧</div>
              <p class="font-medium">Service & Repairs</p>
            </a>
            <a href="#emergency" class="professional-card text-center py-4 hover:bg-blue-50">
              <div class="text-2xl mb-2">🚨</div>
              <p class="font-medium">Emergency Service</p>
            </a>
          </div>
        </div>
        -->

        <!-- Main FAQ Section -->
        <div class="space-y-8">
          
          <!-- 
          
          TO ADD FAQ CONTENT:
          
          1. Uncomment the sections below and customize them
          2. Add your FAQ items following the example structure
          3. You can add multiple sections for different categories
          
          EXAMPLE FAQ SECTION:
          
          <div id="general" class="scroll-mt-20">
            <h2 class="text-3xl font-bold professional-heading mb-8">General Questions</h2>
            <div class="space-y-4">
              
              <div class="professional-card">
                <button class="w-full text-left p-6 flex justify-between items-center">
                  <h3 class="text-lg font-semibold professional-subheading">
                    How quickly can you repair my appliance?
                  </h3>
                  <svg class="w-5 h-5 transform transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </button>
                <div class="px-6 pb-6">
                  <p class="text-gray-600 professional-text">
                    Most repairs are completed the same day. Our technicians carry common parts and tools to fix most issues on the first visit.
                  </p>
                  <p class="text-gray-600 professional-text mt-4">
                    For more complex repairs, we'll provide you with a clear timeline and keep you updated throughout the process.
                  </p>
                </div>
              </div>
              
              Add more FAQ items here...
              
            </div>
          </div>
          
          AVAILABLE SECTION CATEGORIES:
          - General Questions (#general)
          - Service & Repairs (#service)
          - Emergency Service (#emergency)
          
          -->
          
          <!-- Add your FAQ sections here when ready -->
          
        </div>

        <!-- Contact Section for Unanswered Questions -->
        <div class="mt-16 text-center">
          <div class="professional-card max-w-lg mx-auto">
            <h3 class="text-xl font-bold professional-subheading mb-4">
              Still Have Questions?
            </h3>
            <p class="text-gray-600 professional-text mb-6">
              Can't find the answer you're looking for? Our customer service team is here to help.
            </p>            <div class="space-y-4 sm:space-y-0 sm:flex sm:gap-4 sm:justify-center">
              <router-link to="/#contact" class="professional-btn professional-btn-primary">
                💬 Contact Form
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </section>
  </Layout>
</template>

<style scoped>
/* Add any FAQ-specific styles here */

/* Smooth scrolling for anchor links */
html {
  scroll-behavior: smooth;
}

/* Animation for FAQ toggles */
.faq-answer {
  transition: max-height 0.3s ease-in-out;
}

/* Custom scrollbar for long FAQ sections */
.faq-content {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 #f1f5f9;
}

.faq-content::-webkit-scrollbar {
  width: 6px;
}

.faq-content::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.faq-content::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}
</style>
