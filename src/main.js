// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')


// ###############################

import { createApp } from 'vue'

import App from './App.vue'
import FoodItems from './views/AboutView.vue'
// ../views/AboutView.vue'
import AnimalCollection from './views/HomeView.vue'

const app = createApp(App)
app.component('food-items', FoodItems);
app.component('animal-collection', AnimalCollection);

app.mount('#app')
