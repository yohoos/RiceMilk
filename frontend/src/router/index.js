import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home/Home'
import WifiMap from '@/components/wifi/WifiMap'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      icon: 'dashboard'
    },
    {
      path: '/wifi',
      name: 'WifiMap',
      component: WifiMap,
      icon: 'assignment'
    },
    {
      path: '/wifi/notebook',
      name: 'WifiNotebook',
      icon: 'assignment',
      html: true
    }
  ]
})
