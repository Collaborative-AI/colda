<template>
  <div id="app">
    <navbar> </navbar>
    <!-- <router-view /> -->
    <!-- <div class="container">
      <div class="row my-4">
        <navbar class="col-3 order-0 bg-light mr-1" ></navbar> 
        <router-view class="col-8" :style="{ backgroundImage: createBackgroundString }" />
      </div>
    </div> -->
    <!-- <h1>hello</h1> -->
  </div>
</template>

<script>
import Navbar from './components/Navbar'
// import Navbar from './components/Navbar.vue';
// const Navbar = require('./components/Navbar.vue').default
// console.log("Navbar", Navbar)

export default {
  name: 'App',
  components: {
   navbar: Navbar
    // Navbar
  },
  data() {
      return {
        angle: '50',
        color1: 'rgb(0, 204, 0)',
        color2: 'rgb(0, 204, 153)'
      }
    },
    computed: {
    createBackgroundString() {
      return `linear-gradient(${this.angle}deg, ${this.color1}, ${this.color2})`;
    }
  }
}
// exports.default = App
</script>

<style>
</style>