import Vue from 'vue'
import VueRouter from 'vue-router'
import MeasurementsData   from '../views/MeasurementsData.vue'
import SensorDataTableView from '../views/SensorDataTableView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Sensors',
    component: SensorDataTableView,
  },
  {
    path: '/sensor/:id',
    name: 'SensorData',
    component: MeasurementsData
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
