<template>
  <div>
    <div class="wrapper">
       <Loader/>
      <HeaderStyle6/>
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
import HeaderStyle6 from "@/components/partials/backend/HeaderStyle/HeaderStyle6";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-6',
  components: {
    HeaderStyle6,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='resto-bg collapse-menu'
  },
  destroyed () {
    document.body.classList='resto-bg collapse-menu'
  }
}
</script>
<style>
</style>
