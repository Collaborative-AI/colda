<template>
    <span class="counter" ref="counter">{{ value }}</span>
</template>
<script>
import { core } from '../../config/pluginInit'
export default {
  name: 'Counter',
  props: { value: { type: Number, default: 10 } },
  mounted () {
    core.counterInit(this.$refs.counter)
  }
}
</script>
