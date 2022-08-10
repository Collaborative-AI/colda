<template>
  <div
    :class="'owl-carousel'+' '+ text "
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
      <div class="testimonial-info">
        <p>{{ list.description }}</p>
        <div class="post-img">
          <img :src="list.image" class="img-fluid" alt="img">
          <div class="testimonial-name">
            <h5>{{ list.name }}</h5>
            <span class="sub-title">{{ list.design }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'VTwoTestimonialCarousel',
  // eslint-disable-next-line vue/require-prop-types
  props: ['testimonialList', 'text']

}
</script>
