<template>
  <div class="logo">
    <a class=""><img :src="sectionImage" width="100" alt="#" class="img-fluid"></a>
    <p class=" mb-4 mt-4">{{ sectionText }}</p>
    <slot name="icons"/>
  </div>
</template>
<script>
export default {
  name: 'FooterLogo',
 
  props: ['sectionImage', 'sectionText']
}
</script>
