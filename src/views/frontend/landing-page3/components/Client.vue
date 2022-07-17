<template>
  <section class="iq-clients pt-0">
    <div class="container ">
      <div class="row">
        <div class="col-sm-12">
        <div
          class="owl-carousel owl-theme owl-loaded"
          data-dots="false"
          data-nav="false"
          data-items="5"
          data-items-laptop="5"
          data-items-tab="4"
          data-items-mobile="2"
          data-items-mobile-sm="1"
          data-autoplay="true"
          data-margin="30"
        >
          <div v-for="(option,index) in images" :key="index" class="item">
            <div class="iq-client-info text-center wow fadeInUp" data-wow-delay=".5s">
              <div class="img ">
                <img :src="option.src" class="img-fluid mb-4 default-img" alt="images">
                <img :src="option.hover" class="img-fluid mb-4 hover-img" alt="hover-images">
                <h5 class="text-white">
                  {{ option.title }}
                </h5>
              </div>
            </div>
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
  data () {
    return {
      images: [
        {
          src: require('@/assets/images/landing-page/landing-3/hover-28.png'),
          hover: require('@/assets/images/landing-page/landing-3/28.png'),
          title: 'Sofboost'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-29.png'),
          hover: require('@/assets/images/landing-page/landing-3/29.png'),
          title: 'Sofpress'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-30.png'),
          hover: require('@/assets/images/landing-page/landing-3/30.png'),
          title: 'Sof Plus'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-31.png'),
          hover: require('@/assets/images/landing-page/landing-3/31.png'),
          title: 'sofchemp'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-32.png'),
          hover: require('@/assets/images/landing-page/landing-3/28.png'),
          title: 'Sof Pro'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-28.png'),
          hover: require('@/assets/images/landing-page/landing-3/28.png'),
          title: 'Sofpress'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/hover-29.png'),
          hover: require('@/assets/images/landing-page/landing-3/29.png'),
          title: 'Sof Plus'
        }
      ]
    }
  }
}

</script>
