<template>
  <div class="testimonial-box">
    <p class="description">
      <slot name="cardBody" />
    </p>
    <div class="author">
      <div class="left">
        <slot name="cardMedia" />
      </div>
      <div class="right">
        <slot name="cardFooter" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'BlackCardStyle5'
}
</script>
