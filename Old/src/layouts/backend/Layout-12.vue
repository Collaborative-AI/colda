<template>
  <div>
    <div class="wrapper l-horizontal">
      <Loader/>
      <HeaderStyle12/>
      <div class="content-page salon2-content">
        <transition name="router-anim">
          <router-view/>
        </transition>
      </div>
    </div>
    <FooterStyle />
  </div>
</template>
<script>
import Loader from '@/components/loader/Loader'
import HeaderStyle12 from "@/components/partials/backend/HeaderStyle/HeaderStyle12";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-12',
  components: {
    HeaderStyle12,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='salon-2-saidbar-main'
  },
  destroyed () {
    document.body.classList='salon-2-saidbar-main'
  }
}
</script>
<style>
</style>
