<template>
  <section class="position-relative overview-block-pt iq-pb-70">
    <img src="@/assets/images/landing-page/landing-4/fancy-pattern.png" class="img-fluid fancy-back" alt="#">
    <div class="container">
      <TitleSection title=" Some partner who have choose" titleclass="pr-lg-5" mainclass="res-mb">
        <template v-slot:underline>
          <p class="iq-line five" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="text-left">
              <p class="m-0">
                There are many variations of passages of Lorem Ipsum available, but the majority have Category in some form, by injected humour, or randomised words which don't look even slightly believable.
              </p>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row text-center position-relative">
        <div v-for="(partner,index) in partners" :key="index" class="col-lg-3 col-md-6">
          <div class="iq-partner-box">
            <img class="img-fluid client-img" :src="partner.img" alt="image6">
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Partner',
  data () {
    return {
      partners: [
        {
          img: require('@/assets/images/landing-page/landing-4/01.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-4/02.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-4/03.png')
        },
        {
          img: require('@/assets/images/landing-page/landing-4/04.png')
        }
      ]
    }
  }
}
</script>
