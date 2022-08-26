<template>
  <div class="iq-testimonial2 box-shadow">
    <p>{{ desc }}</p>
    <span class="iq-border" />
    <div class="testimonial-info ">
      <img alt="#" class="img-fluid rounded-circle" :src="src">
      <div class="testimonial-name align-self-center">
        <h5>{{ title }}</h5>
        <span class="sub-title">{{ designation }}</span>
      </div>
      <div class="iq-icon">
        <i class="fa fa-quote-left" aria-hidden="true" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CardStyle4',
  props: {
    desc: {
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
    designation: {
      type: String,
      default: ''
    }
  }
}
</script>
