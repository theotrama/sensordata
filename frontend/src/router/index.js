import Vue from 'vue'
import VueRouter from 'vue-router'
import SensorData from '../views/SensorData.vue'
import HumidityData from '../views/HumidityData.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Temperature',
    component: SensorData
  },
  {
    path: '/humidity',
    name: 'Humidity',
    component: HumidityData,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
console.log(process.env.API_BASE_URL)

export default router
