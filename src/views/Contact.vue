<template>
    <div id="main-wrapper" class="show">
        <Navbar></Navbar>
        
        <Footer></Footer>
    </div> 
</template>

<script>
// 标准模板
import Navbar from './reuse/Navbar.vue'
import Footer from './reuse/Footer.vue'
export default {
  name: 'Contact',
  data() {
    return {
      active: 1,
      dark: window.location.pathname.includes("dark"),
    };
  },
  components: {
      Navbar,
      Footer
  },
  methods: {

  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
