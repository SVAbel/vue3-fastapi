import { createRouter, createWebHistory } from 'vue-router';

import HomePage from '../pages/HomePage.vue';
import BomPage from '../pages/bom/BomPage.vue';
import Calendar from '../pages/calendar/CalendarPage.vue';
import Counsel from '../pages/counsel/CounselPage.vue';
import Dashboard from '../pages/dashboard/DashboardPage.vue';
import Login from '../pages/login/LoginPage.vue';
import Payment from '../pages/payment/PaymentPage.vue';
import Reception from '../pages/reception/ReceptionPage.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/bom', name: 'bom', component: BomPage },
  { path: '/calendar', name: 'calendar', component: Calendar },
  { path: '/counsel', name: 'counsel', component: Counsel },
  { path: '/dashboard', name: 'dashboard', component: Dashboard },
  { path: '/login', name: 'login', component: Login },
  { path: '/payment', name: 'payment', component: Payment },
  { path: '/reception', name: 'reception', component: Reception },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../pages/AboutPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
