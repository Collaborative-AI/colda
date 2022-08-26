<template>
  <div>
    <div class="widget">
      <img class="footer-logo img-fluid" :src="sectionImage" width="100" alt="#">
      <p :class=" 'mt-4 mr-lg-4' +' '+textclass ">
        {{ sectionText }}
      </p>
      <slot name="patent" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'FooterLogo',
  
  props: ['sectionImage', 'sectionText','textclass']
}
</script>
