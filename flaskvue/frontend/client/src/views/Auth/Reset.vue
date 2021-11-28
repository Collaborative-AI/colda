<template>
  <div class="container">
    <h1>Register</h1>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">

          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="resetForm.username" class="form-control" v-bind:class="{'is-invalid': resetForm.usernameError}" id="username" placeholder="">
            <div v-show="resetForm.usernameError" class="invalid-feedback">{{ resetForm.usernameError }}</div>
          </div>

          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" v-model="resetForm.email" class="form-control" v-bind:class="{'is-invalid': resetForm.emailError}" id="email" aria-describedby="emailHelp" placeholder="">
            <small v-if="!resetForm.emailError" id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            <div v-show="resetForm.emailError" class="invalid-feedback">{{ resetForm.emailError }}</div>
          </div>

          <div>
            <hua-kuai @verify='verify' @refresh='refresh'></hua-kuai>
          </div>
          
          <br />

          <button type="submit" class="btn btn-primary">Get set new password Link</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// import {request_withdata} from '@/network/request';
// import axios from 'axios'

export default {
  name: 'Reset', //this is the name of the component
  data () {
    return {
      resetForm: {
        username: '',
        email: '',
        password: '',
        submitted: false,  // 是否点击了 submit 按钮
        errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
        usernameError: null,
        emailError: null,
        passwordError: null
      },
      verifivation_res: false,
    }
  },

  methods: {

    verify(result){
      console.log(result) // result为true表示验证通过，false表示验证三次都失败了哦
      if (result == true){
        this.verifivation_res = true;
      }
    },

    refresh(){
      console.log('用户点击了初始化')
    },

    onSubmit (e) {
      this.resetForm.submitted = true  // 先更新状态
      this.resetForm.errors = 0

      if (!this.resetForm.username) {
        this.resetForm.errors++
        this.resetForm.usernameError = 'Username required.'
      } else {
        this.resetForm.usernameError = null
      }

      if (!this.resetForm.email) {
        this.resetForm.errors++
        this.resetForm.emailError = 'Email required.'
      } else if (!this.validEmail(this.resetForm.email)) {
        this.resetForm.errors++
        this.resetForm.emailError = 'Valid email required.'
      } else {
        this.resetForm.emailError = null
      }


      if (this.verifivation_res == false){
        console.log("ggggggg")
        this.resetForm.errors++
        this.$toasted.success("Please move into the right place", { icon: 'fingerprint' })
      }

      if (this.resetForm.errors > 0) {
        // Stop when the form has error
        return false
      }

      const payload = {
        username: this.resetForm.username,
        email: this.resetForm.email,
      }

      this.$axios.post('/forgot', payload)
      .then((res) => {
        // Go to Login Page
        this.$toasted.success('A password reset email has been sent via email.', { icon: 'fingerprint' })
        console.log(res.data)
        
      }).catch((error) => {
        for (var field in error.response.data.message) {
          if (field == 'username') {
            this.resetForm.usernameError = error.response.data.message.username
          } else if (field == 'email') {
            this.resetForm.emailError = error.response.data.message.email
          } 
        }
      });
    },

    validEmail: function (email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }
    
  }
}
</script>