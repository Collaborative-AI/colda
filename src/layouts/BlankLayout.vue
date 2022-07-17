<template>
  <div>
<!--    <Loader />-->
    <div class="wrapper">
      <router-view/>
    </div>
  </div>
</template>
<script>
// import Loader from '../components/core/loader/Loader'
import { core } from '../config/pluginInit'
export default {
  name: 'BlankLayout',
  components: {
    // Loader
  },
  mounted () {
    core.index()
  }
}
</script>
<style>
  @import url("../assets/css/custom.css");
  .modal-backdrop {
    opacity: .5;
  }
</style>
