<template>
  <div>
    <div class="wrapper">
       <Loader/>
      <HeaderStyle13/>
      <div class="content-page salon2-content">
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
import HeaderStyle13 from "@/components/partials/backend/HeaderStyle/HeaderStyle13";
import FooterStyle from "@/components/partials/backend/FooterStyle/FooterStyle";
export default {
  name: 'Layout-13',
  components: {
    HeaderStyle13,
    FooterStyle,
    Loader
  },
  mounted(){
    document.body.classList='ecommerce-navbar'
  },
  destroyed () {
    document.body.classList='ecommerce-navbar'
  }
}
</script>
<style>
</style>
