<template>
  <section>
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
          <div class="text-left  ">
            <ul class="iq-list wow fadeInUp" style="visibility: visible; animation-name: fadeInUp;">
              <li><i class="fa fa-check" /><span>  Boost SEO ranking   </span></li>
              <li><i class="fa fa-check" /><span>Marketing</span></li>
              <li><i class="fa fa-check" /><span>Visual Reviews</span></li>
            </ul>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="popup-images align-right">
            <div class="img-one wow zoomIn" data-wow-duration="0.6s">
              <img src="@/assets/images/landing-page/landing-10/700.png" alt="image1">
            </div><div class="d-block" />
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
        title: 'Get tips & tricks on how to skyrocket your sales.',
        description: 'Faff about only a quid blower I don’t want no agro bleeding chimney pot burke tosser cras nice one boot fanny.!',
        class: 'text-left'
      }
    }
  }
}
</script>
