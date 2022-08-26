<template>
  <section  class="iq-section-space pt-0 iq-section-pb-70">
    <div class="container">
      <div class="row">
          <div class="col-md-12">
            <div class="title-box wow fadeInUp text-center" data-wow-delay=".3s">
              <span class="title-design">OUR SERVICES</span>
              <h2>We Provide Useful Services</h2>
            </div>
          </div>
      </div>
      <div class="row">
          <div class="col-md-3 col-sm-6">
              <div class="prox-services prox-square right wow fadeInUp  text-left" data-wow-delay=".6s" >
              <div class="square-effect bg">
                  <img :src="require('@/assets/images/landing-page/landing-8/12.png')" alt="fancybox">
              </div>
              <h5 class="mb-2">Privacy-Preserving</h5>
              <p class="mb-0">Preserves the privacy of data, model and objectives for building decentralized AI models.</p>
              </div>
          </div>
          <div class="col-md-3 col-sm-6">
              <div class="prox-services prox-square right wow fadeInUp  text-left" >
              <div class="square-effect bg">
                  <img :src="require('@/assets/images/landing-page/landing-8/13.png')" alt="fancybox">
              </div>
              <h5 class="mb-2">Efficient</h5>
              <p class="mb-0">Reduces communication overhead and leverages local data and computation resources.</p>
              </div>
          </div>
          <div class="col-md-3 col-sm-6">
            <div class="prox-services prox-square right wow fadeInUp  text-left" >
              <div class="square-effect bg">
                  <img :src="require('@/assets/images/landing-page/landing-8/14.png')" alt="fancybox">
              </div>
              <h5 class="mb-2">Collaborative</h5>
              <p class="mb-0">Enables collaboration and coorporation across organizations from various industries.</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6">
            <div class="prox-services   prox-square wow fadeInUp  text-left" >
              <div class="square-effect bg">
                <img :src="require('@/assets/images/landing-page/landing-8/15.png')" alt="fancybox">
              </div>
              <h5 class="mb-2">Mutually Beneficial</h5>
              <p class="mb-0">Forms a community of shared interest by building a market of trading predictive power.</p>
            </div>
          </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name:'WeProvide'
}
</script>