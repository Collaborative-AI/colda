<template>
  <div>
    <Loader />
    <div class="wrapper bg-h-full l-horizontal overflow-hidden ">
       
      <HeaderStyle11/>
      <div class="content-page hospi-content">
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
import HeaderStyle11 from "@/components/partials/backend/HeaderStyle/HeaderStyle11";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-11',
  components: {
    HeaderStyle11,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='hospi-wrapper'
  },
  destroyed () {
    document.body.classList='hospi-wrapper'
  }
}
</script>
<style>
</style>
