<template>
  <div>
    <div class="wrapper">
        <Loader/>
      <SidebarStyle14/>
      <HeaderStyle14/>
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
import SidebarStyle14 from "@/components/partials/backend/SidebarStyle/SidebarStyle14";
import HeaderStyle14 from "@/components/partials/backend/HeaderStyle/HeaderStyle14";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-14',
  components: {
    HeaderStyle14,
    FooterStyle,
    SidebarStyle14,
    Loader
  },
  mounted(){
    document.body.classList='box-sidebar'
  },
  destroyed () {
    document.body.classList='box-sidebar'
  }
}
</script>
<style>
</style>
