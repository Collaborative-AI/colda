<template>
  <div>
    <div class="wrapper">
      <Loader/>
      <SidebarStyle5/>
      <HeaderStyle5/>
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
import SidebarStyle5 from "@/components/partials/backend/SidebarStyle/SidebarStyle5";
import HeaderStyle5 from "@/components/partials/backend/HeaderStyle/HeaderStyle5";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-5',
  components: {
    HeaderStyle5,
    FooterStyle,
    SidebarStyle5,
    Loader
  },
  mounted(){
    document.body.classList='fixed-top-navbar'
  },
  destroyed () {
    document.body.classList='fixed-top-navbar'
  }
}
</script>
<style>
</style>
