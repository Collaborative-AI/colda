<template>
  <div
    class="owl-carousel testimonial-style"
    data-autoplay="true"
    data-loop="true"
    data-nav="false"
    data-dots="true"
    data-items="1"
    data-items-laptop="1"
    data-items-tab="1"
    data-items-mobile="2"
    data-items-mobile-sm="1"
    data-margin="30"
  >
    <div v-for="(list,index) in testimonialList" :key="index" class="item">
      <div class="iq-testimonial">
        <div class="testimonial-info">
          <img :src="list.image" alt="#" class="img-fluid rounded-circle">
          <div class="testimonial-name">
            <h5 class="content">
              {{ list.name }}
            </h5>
            <span class="sub-title"><span class="content-sub mr-2 ml-2">-</span>{{ list.designation }}</span>
          </div>
        </div>
        <p>{{ list.description }}</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'VTwoTestimonialCarousel2',
  // eslint-disable-next-line vue/require-prop-types
  props: ['testimonialList']
}
</script>
