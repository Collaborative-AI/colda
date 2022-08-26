<template>
  <div class="position-relative overview-block-pt iq-clients-section">
    <div class="container">
      <div class="row text-center position-relative">
        <div class="objects-main">
           <span class="banner-objects-02">
                        <img src="@/assets/images/landing-page/landing-9/02.png" class="img-fluid" alt="#">
                    </span>
        </div>
        <div
          class="owl-carousel"
          data-autoplay="true"
          data-loop="true"
          data-nav="false"
          data-dots="true"
          data-items="4"
          data-items-laptop="4"
          data-items-tab="3"
          data-items-mobile="2"
          data-items-mobile-sm="1"
          data-margin="30"
        >
          <div v-for="(partner,index) in partners" :key="index" class="item">
            <PartnerSection subclass="img-fluid client-img" mainclass="iq-partner-box" :src="partner.img" style="width: 262.5px; margin-right: 30px;"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Partner',
  data () {
    return {
      partners: [
        {
          img: require('@/assets/images/landing-page/landing-9/1.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-9/2.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-9/3.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-9/4.png')
        }
      ]
    }
  }
}
</script>
