<template>
  <div>
    <div class="wrapper">
       <Loader/>
      <SidebarStyle8/>
      <HeaderStyle8/>
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
import SidebarStyle8 from "@/components/partials/backend/SidebarStyle/SidebarStyle8";
import HeaderStyle8 from "@/components/partials/backend/HeaderStyle/HeaderStyle8";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-8',
  components: {
    HeaderStyle8,
    FooterStyle,
    SidebarStyle8,
    Loader
  },
  mounted(){
    document.body.classList='icon-sidebar sidebar-2'
  },
  destroyed () {
    document.body.classList='icon-sidebar sidebar-2'
  }
}
</script>
<style>
</style>
