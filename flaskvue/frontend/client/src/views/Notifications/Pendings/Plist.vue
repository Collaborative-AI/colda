<template>
  <div class="container">
    pending
    {{unread}}
    
  </div>
</template>

<script>
import store from '../../../store.js'

export default {
  name: 'Plist',  // Name of the component
  // props: ['log'],
  
  data () {
    return {
      unread: "",
    }
  },

  methods:  {
      unread_request(value) {
      this.unread = value
    },
  },

  beforeCreate() {
        this.unread=store.unread
    }


  
}
// exports.default = Home
</script>