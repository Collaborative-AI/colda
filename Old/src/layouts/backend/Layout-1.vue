<template>
  <div>
    <Loader/>
    <div class="wrapper">
      <div class="container hotel-container">
      <HeaderStyle1/>
      <div class="content-page">
        <transition name="router-anim">
          <router-view/>
        </transition>
      </div>
      </div>
    </div>
    <FooterStyle />
  </div>
</template>
<script>
import Loader from '@/components/loader/Loader'
import HeaderStyle1 from "@/components/partials/backend/HeaderStyle/HeaderStyle1";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-1',
  components: {
    HeaderStyle1,
    FooterStyle,
    Loader
  },
 mounted () {
    document.body.classList='box-bg iq-hotel'
  },
  destroyed () {
    document.body.classList='box-bg iq-hotel'
  }
}
</script>
<style>
</style>
