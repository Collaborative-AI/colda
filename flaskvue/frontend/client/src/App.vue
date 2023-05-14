<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
  </div>
</template>

<script>
// import Navbar from './components/Navbar'
const Navbar = require('./components/Navbar.vue').default
export default {
  name: 'App',
  components: {
    navbar: Navbar
  }
}
</script>

<style>
</style>