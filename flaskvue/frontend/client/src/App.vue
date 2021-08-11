<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view/>
  </div>
</template>

<script>
// import Navbar from './components/Navbar'
const Navbar = require('./components/Navbar.vue').default
console.log("Navbar", Navbar)
export default {
  name: 'App',
  components: {
   Navbar: Navbar
  }
}
// exports.default = App
</script>

<style>
</style>