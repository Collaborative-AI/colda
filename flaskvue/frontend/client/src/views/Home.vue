<template>
  <div class="container">
    <alert 
      v-for="(alert, index) in alerts" :key="index"
      v-bind:variant="alert.variant"
      v-bind:message="alert.message">
    </alert>
    <button type="button" class="btn btn-primary">HomePage</button>
  </div>
</template>

<script>
import Alert from '@/components/Alert'

export default {
  name: 'Home',  // Name of the component
  components: {
    alert: Alert
  },
  data () {
    return {
      alerts: [
        {
          variant: 'info',
          message: 'Hi'
        },
        {
          variant: 'danger',
          message: 'Oops..'
        },
        {
          variant: 'success',
          message: 'OK'
        }
      ]
    }
  }
}
</script>