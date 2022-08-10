<template>
  <div>
    <div class="wrapper">
       <Loader/>
      <SidebarStyle7/>
      <HeaderStyle7/>
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
import SidebarStyle7 from "@/components/partials/backend/SidebarStyle/SidebarStyle7";
import HeaderStyle7 from "@/components/partials/backend/HeaderStyle/HeaderStyle7";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-7',
  components: {
    SidebarStyle7,
    HeaderStyle7,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='sidebar-double-icon'
  },
  destroyed () {
    document.body.classList='sidebar-double-icon'
  }
}
</script>
<style>
</style>
