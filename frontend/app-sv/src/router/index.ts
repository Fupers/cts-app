import { createRouter, createWebHistory } from 'vue-router'
import Register from '../views/Register.vue'
import VerifyAccount from '../views/VerifyAccount.vue'
import AdminLogin from '../views/AdminLogin.vue'
import AdminContestants from '../views/AdminContestants.vue'
import AdminWinner from '../views/AdminWinner.vue'
import Success from "../views/Success.vue"

// Rutas de las vistas
const routes = [
  { path: '/', name: 'Register', component: Register },
  { path: '/verify', name: 'VerifyAccount', component: VerifyAccount },
  { path: '/verify/:token', name: 'VerifyAccountToken', component: VerifyAccount },
  { path: '/success', name: 'Success', component: Success },
  { path: '/admin/login', name: 'AdminLogin', component: AdminLogin },
  { 
    path: '/admin/contestants', 
    name: 'AdminContestants', 
    component: AdminContestants,
    meta: { requiresAuth: true }
  },
  { 
    path: '/admin/winner', 
    name: 'AdminWinner', 
    component: AdminWinner,
    meta: { requiresAuth: true }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Guard para proteger rutas de admin
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('adminToken')
  if (to.meta.requiresAuth && !token) {
    next('/admin/login')
  } else {
    next()
  }
})

export default router

