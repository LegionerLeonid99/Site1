import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import FAQ from '../views/FAQ.vue'
import Appliances from '../views/services/Appliances.vue'
import CoffeeMachines from '../views/services/CoffeeMachines.vue'
import Dishwashers from '../views/services/Dishwashers.vue'
import WashingMachines from '../views/services/WashingMachines.vue'
import Hobs from '../views/services/Hobs.vue'
import AirConditioners from '../views/services/AirConditioners.vue'
import AllElectrical from '../views/services/AllElectrical.vue'
import CommercialEquipment from '../views/services/CommercialEquipment.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ
  },
  {
    path: '/services/appliances',
    name: 'Appliances',
    component: Appliances
  },
  {
    path: '/services/coffee-machines',
    name: 'CoffeeMachines',
    component: CoffeeMachines
  },
  {
    path: '/services/dishwashers',
    name: 'Dishwashers',
    component: Dishwashers
  },
  {
    path: '/services/washing-machines',
    name: 'WashingMachines',
    component: WashingMachines
  },
  {
    path: '/services/hobs',
    name: 'Hobs',
    component: Hobs
  },
  {
    path: '/services/air-conditioners',
    name: 'AirConditioners',
    component: AirConditioners
  },
  {
    path: '/services/all-electrical',
    name: 'AllElectrical',
    component: AllElectrical
  },
  {
    path: '/services/commercial-equipment',
    name: 'CommercialEquipment',
    component: CommercialEquipment
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
