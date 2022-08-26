<template>
  <div>
    <div class="wrapper">
      <Loader/>
       <SidebarStyle9/>
      <HeaderStyle9/>
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
import SidebarStyle9 from "@/components/partials/backend/SidebarStyle/SidebarStyle9";
import HeaderStyle9 from "@/components/partials/backend/HeaderStyle/HeaderStyle9";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-9',
  components: {
    HeaderStyle9,
    FooterStyle,
    SidebarStyle9,
    Loader
  },
  mounted(){
    document.body.classList='iq-saidbar-primary'
  },
  destroyed () {
    document.body.classList='iq-saidbar-primary'
  }
}
</script>
<style>
</style>
