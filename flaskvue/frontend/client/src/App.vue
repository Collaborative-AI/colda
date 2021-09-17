<template>
  <div id="app">
    <navbar></navbar> 
    <router-view/>
    <!-- <h1>hello</h1> -->
  </div>
</template>

<script>
import Navbar from './components/Navbar'
// const Navbar = require('./components/Navbar.vue').default
// console.log("Navbar", Navbar)

export default {
  name: 'App',
  components: {
   navbar: Navbar
  }
}
// exports.default = App
</script>

<style>
</style>