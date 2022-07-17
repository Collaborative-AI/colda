<template>
  <div>
    <Loader/>
    <div class="wrapper">
      <SidebarStyle/>
      <DefaultStyle/>
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
 import {core} from '../../config/pluginInit'
import DefaultStyle from "@/components/partials/backend/HeaderStyle/DefaultStyle";
import SidebarStyle from "@/components/partials/backend/SidebarStyle/SidebarStyle";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
import Loader from '@/components/loader/Loader'
export default {
  name: 'DefaultLayout',
  components: {
    SidebarStyle,
    DefaultStyle,
    FooterStyle,
    Loader
  },
  mounted () {
    document.body.classList='color-light'
    core.fullscreen()
  },
  destroyed () {
    document.body.classList='color-light'
  }
}
</script>
<style>
</style>
