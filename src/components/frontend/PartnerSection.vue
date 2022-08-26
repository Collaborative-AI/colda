<template>
  <div :class="mainclass">
    <img :class="subclass" :src="src" alt="image6">
  </div>
</template>
<script>
export default {
  name: 'PartnerSection',
  props: {
    src: {
      type: String,
      default: ' '
    },
    mainclass: {
      type: String,
      default: ' '
    },
    subclass: {
      type: String,
      default: ' '
    }
  }
}
</script>
