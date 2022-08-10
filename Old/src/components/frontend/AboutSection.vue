<template>
  <section :class="mainclass">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-12 mb-5 mb-lg-0 text-center">
          <div class="iq-image-expert">
            <img :src="image" class="img-fluid" alt="#">
            <img src="@/assets/images/landing-page/landing-9/banner-pattern.png" class="img-fluid iq-pattern" alt="#">
          </div>
        </div>
        <div class="col-lg-6 col-md-12">
          <div class="iq-title-box mb-0 text-left">
            <h2 class="title mb-4">
              {{ title }}
            </h2>
            <p>{{ para1 }}</p>
          </div>
          <p>{{ para2 }}</p>

          <div class="iq-sign-box">
            <div class="iq-image mr-5">
              <img :src="signimage" class="img-fluid" alt="#">
            </div>
            <div class="iq-name mt-3">
              <h5 class="title">
                {{ signtitle }}
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'AboutSection',
  props: {
    image: {
      type: String,
      default: ' '
    },
    title: {
      type: String,
      default: ' '
    },
    para1: {
      type: String,
      default: ' '
    },
    para2: {
      type: String,
      default: ' '
    },
    signimage: {
      type: String,
      default: ' '
    },
    signtitle: {
      type: String,
      default: ' '
    },
    mainclass: {
      type: String,
      default: ' '
    }
  }
}
</script>
