import { createApp } from 'vue'
import App from './App.vue'
import Prediction from './views/AboutView.vue'
import About from './views/HomeView.vue'

const app = createApp(App)
app.component('About',  About);
app.component('Prediction', Prediction);

app.mount('#app')
