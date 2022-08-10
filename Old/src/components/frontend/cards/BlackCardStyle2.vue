<template>
  <div class="iq-services text-center wow slideInUp" data-wow-duration="0.5s">
    <div class="iq-icon mb-4">
      <slot name="cardImage" />
    </div>
    <slot name="cardTitle" />
    <slot name="cardContent" />
  </div>
</template>
<script>
export default {
  name: 'BlackCardStyle2'
}
</script>
