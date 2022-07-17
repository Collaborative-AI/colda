<template>
  <div>
    <div class="wrapper">
         <Loader/>
      <SidebarStyle2/>
      <HeaderStyle2/>
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
import SidebarStyle2 from "@/components/partials/backend/SidebarStyle/SidebarStyle2";
import HeaderStyle2 from "@/components/partials/backend/HeaderStyle/HeaderStyle2";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-2',
  components: {
    HeaderStyle2,
    FooterStyle,
    SidebarStyle2,
    Loader
  },
  mounted(){
    document.body.classList='two-sidebar sidebar-1'
  },
  destroyed () {
    document.body.classList='two-sidebar sidebar-1'
  }
}
</script>
<style>
</style>
