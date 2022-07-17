<template>
  <div class="iq-testimonial position-relative">
    <p>{{ text }}</p>
    <span class="iq-border" />
    <div class="testimonial-info ">
      <img alt="#" class="img-fluid rounded-circle" :src="src">
      <div class="testimonial-name align-self-center">
        <h5>{{ title }}</h5>
        <span class="sub-title">{{ position }}</span>
      </div>
    </div>
    <div class="iq-icon">
      <i class="fa fa-quote-right" aria-hidden="true" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'CardStyle2',
  props: {
    text: {
      type: String,
      default: ''
    },
    src: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    position: {
      type: String,
      default: ''
    }
  }
}
</script>
