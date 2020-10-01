import Vue from 'vue'
import VueRouter from 'vue-router'
import TemperatureData   from '../views/TemperatureData.vue'
import HumidityData from '../views/HumidityData.vue'
import SensorDataTableView from '../views/SensorDataTableView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/temperature',
    name: 'Temperature',
    component: TemperatureData
  },
  {
    path: '/humidity',
    name: 'Humidity',
    component: HumidityData,
  },
  {
    path: '/',
    name: 'Sensors',
    component: SensorDataTableView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
