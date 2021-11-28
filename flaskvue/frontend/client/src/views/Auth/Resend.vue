<template>
  <div class="container">
    <h1>Register</h1>
    <div class="row">
      <div class="col-md-4">
          <button @click="resend">Resend Verification Link</button>
      </div>
    </div>
  </div>
</template>

<script>
// import {request_withdata} from '@/network/request';
// import axios from 'axios'

export default {
  name: 'Resend', //this is the name of the component
  data () {
    return {
      username: '',
    }
  },

  methods: {
    resend() {
    
      const resend_data = {
        username: this.username,
      }

      this.$axios.post('/resend/', resend_data)
        .then((response) => {
          // handle success
          console.log("resend successfully", response.data)
          this.$toasted.success(`resend successfully`, { icon: 'fingerprint' })
        })
        .catch((error) => {
          // handle error
          console.log(error)
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    }
  },
  created () {
    this.username = this.$route.query.username
    // this.username = this.$route.params.task_id
    // this.username = this.$route.params.task_name




  }
}
</script>