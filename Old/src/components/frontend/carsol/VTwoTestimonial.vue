<template>
  <section :id="sectionProp.id" :class="sectionProp.class">
    <div class="container">
      <div class="row align-items-center test-shadow">
        <div class="col-lg-6">
          <slot name="imageList1" />
          <slot name="testimonialTitle" />
        </div>
        <div class="col-lg-6">
          <slot name="imageList2" />

          <slot name="testimonialList" />

          <div class="layer_wrap iq-objects style-two right-top">
            <span class="iq-objects-02">
              <img src="../../../../src/assets/images/landing-page/landing-10/29.png" alt="drive02">
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'VTwoTestimonial',
  // eslint-disable-next-line vue/require-prop-types
  props: ['sectionProp']
}
</script>
