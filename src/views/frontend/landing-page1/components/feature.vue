<template>
  <section id="iq-feature" class="popup-images align-left pt-0 pb-4">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <div class="popup-images align-left  ">
            <div class="img-one wow zoomIn" data-wow-duration="0.6s">
              <img src="@/assets/images/landing-page/landing-1/401.png" alt="image1">
            </div>
            <div class="d-block" />
          </div>
          <div class="layer_wrap iq-objects  style-two left-top">
            <span class="iq-objects-02">
              <img src="@/assets/images/landing-page/landing-1/07.png" alt="drive02">
            </span>
            <span class="iq-objects-03">
              <img src="@/assets/images/landing-page/landing-1/08.png" alt="drive02">
            </span>
          </div>
        </div>
        <div class="col-lg-6">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
          <div class="row">
            <div class="col-lg-6">
              <div class="text-left">
                <ul class="iq-list wow fadeInUp">
                  <li v-for="(service,index) in service1" :key="index">
                    <i class="fa fa-check" /><span>{{ service.title }} </span>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="text-left">
                <ul class="iq-list wow fadeInUp">
                  <li v-for="(service,index) in service2" :key="index">
                    <i class="fa fa-check" /><span>{{ service.title }} </span>
                  </li>
                </ul>
              </div>
            </div>
            <div class="layer_wrap iq-objects  style-one right-top">
              <span class="iq-objects-01">
                <img src="@/assets/images/landing-page/landing-1/400.png" alt="drive02">
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Feature',
  data () {
    return {
      titleSectionProp: {
        class: 'text-left',
        title: 'Plan & Run a Dream Event with prox.',
        description: 'Faff about only a quid blower I don’t want no agro bleeding chimney pot burke tosser cras nice one boot fanny.!'
      },

      service1: [
        { title: 'Boost SEO ranking' },
        { title: 'Marketing' },
        { title: 'Visual Reviews' }
      ],

      service2: [
        { title: 'Social Sharing' },
        { title: 'Retention' },
        { title: 'Reviews Generation' }
      ]
    }
  }
}
</script>
