<template>
  <div :class="right ? 'team team-right ' + className: 'team ' + className">
    <div class="left">
      <slot name="cardMedia" />
    </div>
    <div class="right">
      <slot name="cardContent" />
    </div>
  </div>
</template>
<script>
export default {
  name: 'BlackCardStyle3',
  props: {
    right: {
      type: Boolean,
      default: true
    },
    className: {
      type: String,
      default: ''
    }
  }
}
</script>
