<template>
  <div class="container">
    <alert 
      v-for="(alert, index) in alerts" :key="index"
      v-bind:variant="alert.variant"
      v-bind:message="alert.message">
    </alert>

    <!-- <ul class="content">
       <li v-for="(msg, index) in $store.state.msg" :key="index">
         {{ msg }}
       </li>
    </ul> -->


    <button type="button" class="btn btn-primary">HomePage</button>
  </div>
</template>

<script>
import Alert from '../components/Alert.vue'
// const Alert = require('../components/Alert.vue').default

export default {
  name: 'Home',  // Name of the component
  // props: ['log'],
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
      ],
    }
  }
}
// exports.default = Home
</script>