<template>
  <div>
    <p class="footer-logo"><img class="logo" :src="sectionImage" width="250" alt="#"></p>
    <p class="footer-logo">{{ sectionText }}</p>
    <slot name="icons"/>
  </div>
</template>
<script>
export default {
  name: 'FooterLogo',
  
  props: ['sectionImage', 'sectionText']
}
</script>

<style scoped>
.logo {
  object-fit: contain;
  /* width: 10%; */
  height: 80px;
  
}
</style>
