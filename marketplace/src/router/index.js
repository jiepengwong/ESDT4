import { createRouter, createWebHashHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue';
// import Login from "../views/Login.vue";


const routes = [

  {
    path: '/',
    name: 'catalogue',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CatalogueViewCopy.vue')
  }, 
  
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
