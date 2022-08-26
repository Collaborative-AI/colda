<template>
  <div class="work-content">
    <div class="iq-work-id  text-center">
      <slot name="cardNumber"></slot>
    </div>
    <div class="iq-work-detail text-center ">
      <slot name="cardContent"></slot>
    </div>
    <slot name="cardLink"></slot>
  </div>
</template>
<script>
export default {
  name: 'BlackCardStyle1'
}
</script>
