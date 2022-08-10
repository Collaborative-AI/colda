<template>
  <div class="iq-service-style1 bg-white text-left">
    <div class="inner-wrapper">
    <div class="iq-iconbg">
      <i :class="icon" aria-hidden="true" />
    </div>
    <div class="iq-image">
      <img alt="#" :src="src">
    </div>
    <div class="iq-content">
      <div class="iq-title">
        <h4>{{ title }}</h4>
      </div>
      <p class="m-0">
        {{ description }}
      </p>
    </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ServiceStyle',
  props: {
    icon: {
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
    description: {
      type: String,
      default: ''
    }
  }
}
</script>
