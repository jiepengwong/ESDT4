import { createRouter, createWebHashHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue';
// import login from "../views/Login.vue";


const routes = [
  {
    path: "/",
    name: "login",
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue'),
    meta: {
      requiresAuth: false
    }
  },

  {
    path: '/catalogue',
    name: 'catalogue',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CatalogueViewCopy.vue'),
    meta: {
      requiresAuth: false
    }
  }, 

  {
    path: '/catalogue/item/:id',
    name: 'CatalogueItemDetails',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/CataloguePageComponent/CatalogueItemDetails.vue'),
    props: true,
    meta: {
      requiresAuth: true
    }
  }, 
  {
    path: '/SellerView',
    name: 'SellerView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SellerView.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/payment',
    name: 'payment',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Payments.vue'),
    meta: {
      requiresAuth: true
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// To means where you are going
// From means where you are coming currently
// Next 
router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const checker = localStorage.getItem("id")
    if (checker) {
      next()
    }
    else{
      router.push({name: 'login'})
    }
  }
})

export default router
