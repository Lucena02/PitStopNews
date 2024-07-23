import { createRouter, createWebHistory } from 'vue-router'
import SportsView from '../views/SportsView.vue'
import ScienceView from '../views/ScienceView.vue'
import WorldView from '../views/WorldView.vue'
import PoliticsView from '../views/PoliticsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/sports',
      name: 'sports',
      component: SportsView
    },
    {
      path: '/politics',
      name: 'politics',
      component: PoliticsView
    },
    {
      path: '/world',
      name: 'world',
      component: WorldView
    },
    {
      path: '/science',
      name: 'science',
      component: ScienceView
    }
  ]
})

export default router
