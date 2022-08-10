<template>
  <div>
      <Loader/>
    <div class="wrapper">
    
      <HeaderStyle16/>
      <div class="content-page">
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
import HeaderStyle16 from "@/components/partials/backend/HeaderStyle/HeaderStyle16";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-16',
  components: {
    HeaderStyle16,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='dobule-navbar'
  },
  destroyed () {
    document.body.classList='dobule-navbar'
  }
}
</script>
<style>
</style>
