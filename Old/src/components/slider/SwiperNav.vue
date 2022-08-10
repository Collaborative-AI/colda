<template>
  <div>
    <!-- If we need navigation buttons -->
    <div :class="`swiper-button-prev ${defaultClass ? leftClass : ''}`" style="cursor: pointer;">
      <slot name="left" />
    </div>
    <div :class="`swiper-button-next ${defaultClass ? rightClass : ''}`" style="cursor: pointer;">
      <slot name="right" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'SwiperNav',
  props: {
    leftClass: { type: String, default: 'left slick-arrow ri-arrow-left-s-line' },
    rightClass: { type: String, default: 'right slick-arrow ri-arrow-right-s-line' },
    defaultClass: { type: Boolean, default: true }
  }
}
</script>
