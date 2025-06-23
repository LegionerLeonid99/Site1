<template>
  <div class="slider-container">
    <div class="slider-wrapper">
      <div 
        v-for="(image, index) in images" 
        :key="index"
        :class="['slide', { 'active': currentSlide === index }]"
        :style="{ backgroundImage: `url(${image.url})` }"
      >
        <div class="slide-overlay"></div>
      </div>
    </div>
    
    <!-- Slider dots/indicators -->
    <div class="slider-indicators">
      <button 
        v-for="(image, index) in images"
        :key="index"
        :class="['indicator', { 'active': currentSlide === index }]"
        @click="goToSlide(index)"
        :aria-label="`Go to slide ${index + 1}`"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Import images as URLs using Vite's ?url suffix
import image1 from '../assets/images/hero-section/pexels-asphotograpy-213162.jpg?url'
import image2 from '../assets/images/hero-section/pexels-castorlystock-3829549.jpg?url'
import image3 from '../assets/images/hero-section/pexels-melaudelo-32640492.jpg?url'

const props = defineProps({  images: {
    type: Array,
    default: () => [
      {
        url: image1,
        alt: 'Modern kitchen with appliances'
      },
      {
        url: image2,
        alt: 'Professional appliance repair'
      },
      {
        url: image3,
        alt: 'Kitchen appliances installation'
      },
      {
        url: image1,
        alt: 'Home appliances service'
      }
    ]
  },
  autoPlay: {
    type: Boolean,
    default: true
  },
  interval: {
    type: Number,
    default: 5000
  }
})

const currentSlide = ref(0)
let autoPlayTimer = null

const goToSlide = (index) => {
  currentSlide.value = index
}

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % props.images.length
}

const prevSlide = () => {
  currentSlide.value = currentSlide.value === 0 ? props.images.length - 1 : currentSlide.value - 1
}

const startAutoPlay = () => {
  if (props.autoPlay) {
    autoPlayTimer = setInterval(nextSlide, props.interval)
  }
}

const stopAutoPlay = () => {
  if (autoPlayTimer) {
    clearInterval(autoPlayTimer)
    autoPlayTimer = null
  }
}

onMounted(() => {
  startAutoPlay()
})

onUnmounted(() => {
  stopAutoPlay()
})

// Pause autoplay on hover
const handleMouseEnter = () => {
  stopAutoPlay()
}

const handleMouseLeave = () => {
  startAutoPlay()
}
</script>

<style scoped>
.slider-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 0;
}

.slider-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.slide.active {
  opacity: 1;
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%);
}

.slider-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 10;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.5);
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator:hover,
.indicator.active {
  background: white;
  border-color: white;
}

.slider-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10;
  backdrop-filter: blur(10px);
}

.slider-nav:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-50%) scale(1.1);
}

.slider-nav.prev {
  left: 20px;
}

.slider-nav.next {
  right: 20px;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .slider-nav {
    width: 40px;
    height: 40px;
  }
  
  .slider-nav.prev {
    left: 10px;
  }
  
  .slider-nav.next {
    right: 10px;
  }
  
  .slider-indicators {
    bottom: 15px;
  }
  
  .indicator {
    width: 10px;
    height: 10px;
  }
}

/* Pause autoplay on hover */
.slider-container:hover .slide {
  animation-play-state: paused;
}
</style>
