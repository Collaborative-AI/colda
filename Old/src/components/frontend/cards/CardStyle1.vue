<template>
  <div :class="'iq-portfolio iq-'+mainclass+'-15'">
    <div class="iq-portfolio-img">
      <img class="img-fluid" :src="src" alt="image">
    </div>
    <div class="portfolio-title">
      <h4 class="iq-title">
        {{ title }}
      </h4>
    </div>
    <div class="iq-portfolio-info text-left">
      <a href="#"><h4 class="portfolio-text">{{ text }}</h4></a>
    </div>
    <a href="#">
      <div class="iq-portfolio-icon">
        <i class="fa fa-arrows-alt" />
      </div></a>
    <div class="iq-image">
      <img :src="pattern" class="img-fluid" alt="#">
    </div>
  </div>
</template>
<script>
export default {
  name: 'CardStyle1',
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
    pattern: {
      type: String,
      default: ''
    },
    mainclass: {
      type: String,
      default: ''
    }
  }
}
</script>
