<template>
  <div>
    <div class="wrapper">
      <Loader/>
      <HeaderStyle15/>
      <RightChatPanel />
      <div class="content-page social-content">
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
import RightChatPanel from "@/components/partials/backend/RightSideBar/right-chat-panel";
import HeaderStyle15 from "@/components/partials/backend/HeaderStyle/HeaderStyle15";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-15',
  components: {
    HeaderStyle15,
    FooterStyle,
    RightChatPanel,
    Loader
  },
  mounted(){
    document.body.classList='tab-horizontal'
  },
  destroyed () {
    document.body.classList='tab-horizontal'
  }
}
</script>
<style>
</style>
