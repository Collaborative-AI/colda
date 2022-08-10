<template>
  <section class="iq-section-space iq-section-space pt-0 iq-clients">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="owl-carousel owl-loaded owl-drag" data-dots="false" data-nav="false" data-items="6" data-items-laptop="4" data-items-tab="3" data-items-mobile="2" data-items-mobile-sm="1" data-autoplay="true" data-loop="true" data-margin="30">
            <div class="item" v-for="(item, index) in list" :key="index" >
              <div class="clients-box"> <img class="img-fluid client-img" :src="item.image" alt="client-image"> </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Client',
  data(){
    return{
      list:[
        {
           image : require('../../../../assets/images/landing-page/landing-6/32.png')
        },
        {
           image : require('../../../../assets/images/landing-page/landing-6/33.png')
        },
        {
           image : require('../../../../assets/images/landing-page/landing-6/34.png')
        },
        {
           image : require('../../../../assets/images/landing-page/landing-6/35.png')
        },
        {
           image : require('../../../../assets/images/landing-page/landing-6/36.png')
        },
        {
           image : require('../../../../assets/images/landing-page/landing-6/32.png')
        }
      ]
    }
  }
}
</script>