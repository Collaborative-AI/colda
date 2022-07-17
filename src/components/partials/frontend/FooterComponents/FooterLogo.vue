<template>
  <div>
    <p class="footer-logo"><img :src="sectionImage" width="100" alt="#"></p>
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
