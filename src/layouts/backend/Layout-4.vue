<template>
  <div>
    <div class="wrapper">
       <Loader/>
       <SidebarStyle4/>
      <HeaderStyle4/>
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
import SidebarStyle4 from "@/components/partials/backend/SidebarStyle/SidebarStyle4";
import HeaderStyle4 from "@/components/partials/backend/HeaderStyle/HeaderStyle4";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-4',
  components: {
    HeaderStyle4,
    FooterStyle,
    SidebarStyle4,Loader
  },
  mounted(){
    document.body.classList='iq-salon1-saidbar'
  },
  destroyed () {
    document.body.classList='iq-salon1-saidbar'
  }
}
</script>
<style>
</style>
