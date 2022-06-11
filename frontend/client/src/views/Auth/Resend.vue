<template>

  <b-container>
    <b-row align-v="center">
      <b-col>
          <button @click="resend" class="btn btn-success ">Resend Verification Link</button>
      </b-col>
    </b-row>
  </b-container>

<!-- <div class="container-fluid min-vh-100"> 
  <div class="row align-items-start" style="border:1px solid red; height: 30%">
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-center" style="border:1px solid red; height: 30%" >
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
  <div class="row align-items-end" style="border:1px solid red; height: 30%" >
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
    <div class="col">
      One of three columns
    </div>
  </div>
</div> -->



   
  
  
</template>

<script>
import { add_prefix } from '../../utils'
// import {request_withdata} from '@/network/request';
// import axios from 'axios'

export default {
  name: 'Resend', //this is the name of the component
  data () {
    return {
      username: '',
      email: '',
    }
  },

  methods: {
    resend() {
    
      const resend_data = {
        username: this.username,
        email: this.email,
        key_indicator: 'username'
      }

      this.$axios.post(add_prefix(`/resend`,`/user`), resend_data) 
        .then((response) => {
          // handle success
          console.log("resend successfully", response.data)
          this.$toasted.success(`Resend successfully`, { icon: 'fingerprint' })
        })
        .catch((error) => {
          // handle error
          console.log(error)
          this.$toasted.success(`Resend failed`, { icon: 'fingerprint' })
          // console.log(error.response.data)
          // this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
        })

    }
  },
  created () {
    this.username = this.$route.query.username
    this.email = this.$route.query.email
    // this.username = this.$route.params.task_id
    // this.username = this.$route.params.task_name




  }
}
</script>

<style>
.heng {
  display: flex;
  justify-content:center;
  align-items: center;
}
/* .shu {
  display: flex;
  justify-content:center;
  
} */
</style>