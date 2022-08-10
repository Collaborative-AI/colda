<template>
  <div>
    <div class="wrapper l-horizontal">
      <Loader />
      <HeaderStyle10/>
      <div class="content-page c-payment-block">
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
import HeaderStyle10 from "@/components/partials/backend/HeaderStyle/HeaderStyle10";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-10',
  components: {
    HeaderStyle10,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='home-payment'
  },
  destroyed () {
    document.body.classList='home-payment'
  }
}
</script>
<style>
</style>
