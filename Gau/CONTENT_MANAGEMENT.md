# 📝 Content Management Guide

## 🏠 Homepage Content

### Hero Section
**File**: `src/views/Home.vue`

**What you can edit**:
- Main headline text
- Subtitle/description
- Call-to-action button text
- Background images

**How to edit**:
```vue
<!-- Look for this section in Home.vue -->
<h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl professional-heading">
  Your Main Headline Here  <!-- 👈 EDIT THIS -->
</h1>
<p class="mt-6 text-lg leading-8 text-gray-300 professional-text">
  Your business description here  <!-- 👈 EDIT THIS -->
</p>
```

### About Section
**What you can edit**:
- "Why Choose Our Family Business?" heading
- Feature descriptions
- Benefits and selling points

**Example**:
```vue
<h2 class="text-4xl font-bold text-gray-900 mb-8">
  Why Choose Our Family Business?  <!-- 👈 EDIT THIS -->
</h2>
```

### Services Section
**What you can edit**:
- Service titles
- Service descriptions
- Service icons/images

**Location in code**:
```vue
const services = ref([
  {
    title: 'Your Service Name',        // 👈 EDIT THIS
    description: 'Service description', // 👈 EDIT THIS
    route: '/services/your-service'     // 👈 UPDATE ROUTE
  }
])
```

## 📄 Service Pages

### Individual Service Pages
**Location**: `src/views/services/`

Each service has its own file:
- `Appliances.vue` - General appliances
- `CoffeeMachines.vue` - Coffee machines
- `Dishwashers.vue` - Dishwashers
- `WashingMachines.vue` - Washing machines
- `Hobs.vue` - Hobs
- `AirConditioners.vue` - AC units
- `CommercialEquipment.vue` - Commercial
- `AllElectrical.vue` - All electrical

### Editing Service Pages

**Structure of each service page**:
```vue
<template>
  <Layout>
    <!-- Hero Section -->
    <section class="hero-bg py-24">
      <h1>Service Name</h1>              <!-- 👈 EDIT THIS -->
      <p>Service description</p>         <!-- 👈 EDIT THIS -->
    </section>
    
    <!-- Features Section -->
    <section>
      <!-- What we repair -->
      <!-- Brands we service -->
      <!-- Common problems -->
    </section>
    
    <!-- Contact Section -->
  </Layout>
</template>
```

### Adding New Services

1. **Create new service file**:
   ```bash
   # Copy existing service file
   cp src/views/services/Appliances.vue src/views/services/YourNewService.vue
   ```

2. **Add route** in `src/router/index.js`:
   ```javascript
   {
     path: '/services/your-new-service',
     component: () => import('../views/services/YourNewService.vue')
   }
   ```

3. **Update navigation** in `src/components/Layout.vue`

## 🔧 FAQ Section

### Adding/Editing FAQ Items
**File**: `src/views/Home.vue`

**Find the FAQ section**:
```vue
<div class="professional-card p-4 lg:p-6">
  <h3 class="text-base lg:text-lg font-bold">
    Your question here?  <!-- 👈 EDIT THIS -->
  </h3>
  <p class="text-gray-600">
    Your answer here.    <!-- 👈 EDIT THIS -->
  </p>
</div>
```

### Common FAQ Topics
- Response times
- Service areas
- Pricing
- Warranties
- Emergency services
- Payment methods
- Appointment scheduling

## 📧 Contact Forms

### Main Contact Form
**File**: `src/views/Home.vue`

**Editable elements**:
- Form fields
- Placeholder text
- Button text
- Validation messages

**Form structure**:
```vue
<form @submit.prevent="submitForm">
  <input
    v-model="contactForm.name"
    placeholder="Enter your name..."  <!-- 👈 EDIT PLACEHOLDER -->
    required
  />
  
  <select v-model="contactForm.service">
    <option value="service1">Service 1</option>  <!-- 👈 EDIT OPTIONS -->
    <option value="service2">Service 2</option>
  </select>
  
  <button type="submit">
    Send Message  <!-- 👈 EDIT BUTTON TEXT -->
  </button>
</form>
```

### Adding Form Fields

1. **Add to data model**:
   ```javascript
   const contactForm = ref({
     name: '',
     email: '',
     service: '',
     message: '',
     newField: ''  // 👈 ADD NEW FIELD
   })
   ```

2. **Add HTML input**:
   ```vue
   <input
     v-model="contactForm.newField"
     type="text"
     placeholder="New field placeholder"
   />
   ```

3. **Update backend** to handle new field

## 🖼️ Images and Media

### Homepage Images
**Location**: `src/assets/images/`

**Directory structure**:
```
images/
├── hero-section/          # Background images
├── services/             # Service-related images
└── social/              # Social media images
```

### Replacing Images

1. **Keep same filename** for automatic updates:
   ```bash
   # Replace hero image
   # Old: pexels-asphotograpy-213162.jpg
   # New: your-new-hero-image.jpg (rename to match)
   ```

2. **Update image paths** if changing filenames:
   ```vue
   <img src="/src/assets/images/your-folder/your-image.jpg" alt="Description" />
   ```

### Image Guidelines
- **Hero images**: 1920x1080px or larger
- **Service images**: 800x600px minimum
- **Logo**: SVG or PNG with transparent background
- **File formats**: JPG (photos), PNG (graphics), SVG (logos)
- **File size**: Under 500KB for web performance

## 🎨 Styling and Appearance

### Colors
**File**: `src/styles/main.css` and `tailwind.config.js`

**Main brand colors**:
- Primary blue: `#3B82F6`
- Dark blue: `#1D4ED8`
- Gray variants for text and backgrounds

### Typography
**Defined in**: `src/styles/main.css`

**Available classes**:
- `.professional-heading` - Main headings
- `.professional-subheading` - Sub headings
- `.professional-text` - Body text

### Buttons
**Available button styles**:
- `.professional-btn-primary` - Main action buttons
- `.professional-btn-secondary` - Secondary buttons

## 📱 Mobile Responsiveness

### Responsive Classes
Your website uses TailwindCSS responsive classes:

```vue
<!-- Desktop: 4 columns, Tablet: 2 columns, Mobile: 1 column -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
```

### Testing Responsiveness
1. **Browser dev tools** - Toggle device toolbar
2. **Real devices** - Test on actual phones/tablets
3. **Responsive design tools** - Online testing tools

## 📋 Content Checklist

### Before Publishing
- [ ] All business information is accurate
- [ ] Contact forms work properly
- [ ] Images load correctly
- [ ] Text is spell-checked
- [ ] Links work and go to correct pages
- [ ] Mobile version looks good
- [ ] Loading speed is acceptable

### Regular Content Updates
- [ ] Update seasonal promotions
- [ ] Add new services when available
- [ ] Update business hours for holidays
- [ ] Refresh FAQ based on customer questions
- [ ] Add customer testimonials
- [ ] Update service area coverage

### SEO Content Tips
- Use location keywords naturally in text
- Include service keywords in headings
- Write for users first, search engines second
- Keep meta descriptions under 160 characters
- Use descriptive alt text for images

---

*For technical implementation help, see CONFIGURATION_GUIDE.md*
