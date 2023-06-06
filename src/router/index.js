import Vue from 'vue'
import VueRouter from 'vue-router'
// import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import VueAxios from 'vue-axios'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView.vue
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  // {
  //   path: '/Prediction',
  //   name: 'Prediction',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/PredictionView.vue')
  // }
]

const router =createRouter({
// const router =new VueRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
