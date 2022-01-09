import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: "home",
      component: () => import(/* webpackChunkName: "home" */ "@/views/Home.vue")
    },
    {
      path: '/result',
      name: "result",
      component: () => import(/* webpackChunkName: "home" */ "@/views/Result.vue")
    }
  ]
})

export default router;