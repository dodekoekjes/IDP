import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import 'bulma/css/bulma.css'
// components
import ErrorPage from '@/components/ErrorPage'

// Pages
import HomePage from '@/pages/HomePage'
import About from '@/pages/About'
import progress from '@/pages/Progress'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'is-active',
  routes: [
    {
      path: '/test',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/404',
      name: 'ErrorPage',
      component: ErrorPage
    },
    {
      path: '/home',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/progress',
      name: 'Progress',
      component: progress
    },
    {
      path: '/', redirect: '/home'
    },
    {
      path: '*', redirect: '/404'
    },
    {
      path: '/HelloWorld', redirect: '/test'
    }
  ]
})
