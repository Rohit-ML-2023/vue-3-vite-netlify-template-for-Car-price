<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <HelloWorld msg="Hello Vue 3 + Vite" /> -->
  <!-- <template> -->
    <!-- <p>Choose what part of this page you want to see:</p> -->
    <button @click="activeComp = 'About'">About</button> |  
    
    <button @click="activeComp = 'Prediction'">Prediction</button><br>
    <div>
      <component :is="activeComp"></component>
     </div>

  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/Prediction"> Prediction </router-link>
  </nav>
  <router-view/> -->
<!-- </template> -->
</template>

<script>
export default {
  data() {
      return {
        activeComp: ''
      }
    }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
