import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CombinationView from '../views/CombinationView.vue'
import NetAssetValueView from '../views/NetAssetValueView.vue'
import UserView from '../views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/combination',
      name: 'combination',
      component: CombinationView
    },
    {
      path: '/net-asset-value',
      name: 'net-asset-value',
      component: NetAssetValueView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
