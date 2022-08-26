<template>
  <footer id="iq-contact" :class="footerClass">
    <div class="container">
      <slot name="footerContent"></slot>
      <slot name="copyright"></slot>
    </div>
  </footer>
</template>
<script>
export default {
  name: 'FooterMain',
  props: ['footerClass']
}
</script>
