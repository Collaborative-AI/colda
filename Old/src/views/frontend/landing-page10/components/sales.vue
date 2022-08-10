<template>
  <section class="pt-0 iq-rpb-zero">
    <div class="container">
      <div class="row align-items-center flex-row-reverse">
        <div class="col-lg-6">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
          <div v-for="(list,index) in lists" :key="index" class="fancy-icon wow fadeInUp  text-left" style="visibility: visible; animation-name: fadeInUp;">
            <div class="media">
              <div class="fancy-img">
                <img :src="list.img" alt="fancybox">
              </div>
              <div class="media-body">
                <h5 class="mt-0">
                  {{ list.title }}
                </h5>
                <p class="mb-0">
                  {{ list.subtitle }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="popup-images align-left">
            <div class="img-one wow zoomIn" data-wow-duration="0.6s">
              <img src="@/assets/images/landing-page/landing-10/701.png" alt="image1">
            </div>
            <div class="d-block" />
          </div>
          <div class="layer_wrap iq-objects  style-two left-top">
            <span class="iq-objects-02">
              <img src="@/assets/images/landing-page/landing-10/704.png" alt="drive02">
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Sales',
  data () {
    return {
      titleSectionProp: {
        title: 'Get tips & tricks on how to skyrocket your sales.',
        description: 'Faff about only a quid blower I don’t want no agro bleeding chimney pot burke tosser cras nice one boot fanny.!',
        class: 'text-left'
      },
      lists: [
        {
          img: require('@/assets/images/landing-page/landing-10/702.png'),
          title: 'Virtual Card',
          subtitle: 'There are many variations of passages of Lorem Ipsum available.'
        },
        {
          img: require('@/assets/images/landing-page/landing-10/703.png'),
          title: 'Buyer Protection',
          subtitle: 'There are many variations of passages of Lorem Ipsum available.'
        }
      ]
    }
  }
}
</script>
