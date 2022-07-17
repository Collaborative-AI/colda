<template>
  <footer id="iq-client" :class="footerClass">
    <slot name="footerContent" />
  </footer>
</template>
<script>
export default {
  name: 'FooterMain',
  props: {
    footerClass:
    {
      type: String,
      required: true
    }
  }
}
</script>
