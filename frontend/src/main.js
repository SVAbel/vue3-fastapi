import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

import PrimeVue from 'primevue/config';

import 'primevue/resources/themes/saga-blue/theme.css'; // theme
import 'primevue/resources/primevue.min.css'; // core css
import 'primeicons/primeicons.css'; // icons

const app = createApp(App);
app.use(PrimeVue);
app.use(router);
app.use(store);
app.use(ElementPlus);
app.mount('#app');
