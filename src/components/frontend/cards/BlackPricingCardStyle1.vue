<template>
  <div class="iq-pricing-table ">
    <div class="pricing-header">
      <slot name="cardHeader" />
    </div>
    <ul class="">
      <slot name="cardBody" />
    </ul>
    <slot name="cardFooter" />
  </div>
</template>
<script>
export default {
  name: 'BlackPricingCardStyle1'
}
</script>
