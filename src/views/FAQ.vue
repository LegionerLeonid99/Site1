<script setup>
import { ref } from 'vue'
import Layout from '../components/Layout.vue'
import { useSEO } from '../composables/useSEO.js'

// 🎯 SEO Setup for FAQ Page
useSEO('faq')

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
  //   answer: "Yes, we provide a comprehensive XX-day warranty on all parts and labor for your peace of mind."
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
  <Layout>    <!-- Hero Section -->
    <section class="hero-gradient py-12 sm:py-16 md:py-20 lg:py-24 relative overflow-hidden">
      <div class="mx-auto max-w-screen-xl px-3 sm:px-4 md:px-6 lg:px-8">
        <div class="text-center">
          <h1 class="text-2xl font-bold sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl professional-heading text-white leading-tight">
            Frequently Asked Questions
          </h1>
          <p class="mt-4 sm:mt-6 text-base sm:text-lg md:text-xl text-white opacity-90 max-w-3xl mx-auto">
            Find answers to common questions about our appliance repair services
          </p>
          <!-- Uncomment to add a search box -->
          <!--
          <div class="mt-6 sm:mt-8 max-w-sm sm:max-w-md mx-auto px-2 sm:px-0">
            <input 
              type="text" 
              placeholder="Search FAQs..." 
              class="professional-input bg-white w-full text-sm sm:text-base"
            />
          </div>
          -->
        </div>
      </div>
    </section>    <!-- FAQ Content Section -->
    <section class="bg-white py-12 sm:py-16 md:py-20 lg:py-24">
      <div class="mx-auto max-w-4xl px-3 sm:px-4 md:px-6 lg:px-8">
        
        <!-- Uncomment to add Quick Links Section -->
        <!--
        <div class="mb-12 sm:mb-16">
          <h2 class="text-xl sm:text-2xl font-bold professional-heading mb-6 sm:mb-8 text-center">Quick Links</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
            <a href="#general" class="professional-card text-center py-3 sm:py-4 hover:bg-blue-50 transition-colors">
              <div class="text-xl sm:text-2xl mb-2">❓</div>
              <p class="font-medium text-sm sm:text-base">General Questions</p>
            </a>
            <a href="#service" class="professional-card text-center py-3 sm:py-4 hover:bg-blue-50 transition-colors">
              <div class="text-xl sm:text-2xl mb-2">🔧</div>
              <p class="font-medium text-sm sm:text-base">Service & Repairs</p>
            </a>
            <a href="#emergency" class="professional-card text-center py-3 sm:py-4 hover:bg-blue-50 transition-colors">
              <div class="text-xl sm:text-2xl mb-2">🚨</div>
              <p class="font-medium text-sm sm:text-base">Emergency Service</p>
            </a>
          </div>
        </div>
        -->        <!-- Main FAQ Section -->
        <div class="space-y-6 sm:space-y-8">
          
          <!-- 
          
          TO ADD FAQ CONTENT:
          
          1. Uncomment the sections below and customize them
          2. Add your FAQ items following the example structure
          3. You can add multiple sections for different categories
          
          EXAMPLE FAQ SECTION:
          
          <div id="general" class="scroll-mt-16 sm:scroll-mt-20">
            <h2 class="text-2xl sm:text-3xl font-bold professional-heading mb-6 sm:mb-8">General Questions</h2>
            <div class="space-y-3 sm:space-y-4">
              
              <div class="professional-card">
                <button class="w-full text-left p-4 sm:p-6 flex justify-between items-center">
                  <h3 class="text-base sm:text-lg font-semibold professional-subheading pr-4">
                    How quickly can you repair my appliance?
                  </h3>
                  <svg class="w-4 h-4 sm:w-5 sm:h-5 transform transition-transform flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </button>
                <div class="px-4 sm:px-6 pb-4 sm:pb-6">
                  <p class="text-gray-600 professional-text text-sm sm:text-base">
                    Most repairs are completed the same day. Our technicians carry common parts and tools to fix most issues on the first visit.
                  </p>
                  <p class="text-gray-600 professional-text text-sm sm:text-base mt-3 sm:mt-4">
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
          
        </div>        <!-- Contact Section for Unanswered Questions -->
        <div class="mt-12 sm:mt-16 text-center">
          <div class="professional-card max-w-lg mx-auto">
            <h3 class="text-lg sm:text-xl font-bold professional-subheading mb-3 sm:mb-4">
              Still Have Questions?
            </h3>
            <p class="text-gray-600 professional-text text-sm sm:text-base mb-4 sm:mb-6 px-2 sm:px-0">
              Can't find the answer you're looking for? Our customer service team is here to help.
            </p>            <div class="space-y-3 sm:space-y-4 md:space-y-0 md:flex md:gap-3 lg:gap-4 md:justify-center">
              <router-link to="/#contact" class="professional-btn professional-btn-primary text-sm sm:text-base w-full md:w-auto">
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
/* Mobile-first responsive design improvements */

/* Smooth scrolling for anchor links */
html {
  scroll-behavior: smooth;
}

/* Mobile touch-friendly button sizing */
@media (max-width: 640px) {
  .professional-btn {
    padding: 0.875rem 1.5rem;
    min-height: 44px; /* iOS touch target size */
    font-size: 0.9rem;
  }
  
  .professional-card {
    border-radius: 0.5rem;
    margin: 0 -0.25rem; /* Extend to screen edges on mobile */
  }
  
  /* FAQ item mobile optimizations */
  .faq-item-button {
    touch-action: manipulation; /* Disable double-tap zoom */
    min-height: 60px;
  }
  
  /* Improved text readability on mobile */
  .professional-text {
    line-height: 1.6;
    word-spacing: 0.05em;
  }
  
  .professional-heading {
    line-height: 1.2;
    word-break: break-word;
  }
  
  /* Better spacing for mobile cards */
  .professional-card {
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  }
}

/* Tablet optimizations */
@media (min-width: 641px) and (max-width: 1024px) {
  .professional-card {
    padding: 1.25rem;
  }
}

/* Animation for FAQ toggles */
.faq-answer {
  transition: max-height 0.3s ease-in-out;
}

/* Enhanced focus states for accessibility */
.professional-btn:focus,
button:focus {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
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

/* Mobile-specific hover states */
@media (hover: hover) {
  .professional-card:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: all 0.2s ease-in-out;
  }
}

/* Remove hover effects on touch devices */
@media (hover: none) {
  .professional-card:hover {
    transform: none;
    box-shadow: inherit;
  }
}

/* Improved spacing for different screen sizes */
@media (max-width: 375px) {
  /* Extra small phones */
  .hero-gradient {
    padding-top: 2rem;
    padding-bottom: 2rem;
  }
  
  .text-2xl {
    font-size: 1.375rem;
  }
}

@media (min-width: 376px) and (max-width: 414px) {
  /* Standard mobile phones */
  .professional-card {
    padding: 1rem;
  }
}

/* Landscape phone optimization */
@media (max-height: 500px) and (orientation: landscape) {
  .hero-gradient {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
  }
  
  .py-12 {
    padding-top: 2rem;
    padding-bottom: 2rem;
  }
}
</style>
