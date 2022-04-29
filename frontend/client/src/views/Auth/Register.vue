<template>
  <div class="container">
    <h1>Register</h1>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">

          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="registerForm.username" class="form-control" v-bind:class="{'is-invalid': registerForm.usernameError}" id="username" placeholder="">
            <div v-show="registerForm.usernameError" class="invalid-feedback">{{ registerForm.usernameError }}</div>
          </div>

          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" v-model="registerForm.email" class="form-control" v-bind:class="{'is-invalid': registerForm.emailError}" id="email" aria-describedby="emailHelp" placeholder="">
            <small v-if="!registerForm.emailError" id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            <div v-show="registerForm.emailError" class="invalid-feedback">{{ registerForm.emailError }}</div>
          </div>

          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="registerForm.password" class="form-control" v-bind:class="{'is-invalid': registerForm.passwordError}" id="password" placeholder="">
            <small v-if="!registerForm.passwordError" id="passwordHelp1" class="form-text text-muted">At least 8 characters. At most 25 characters</small>
            <small v-if="!registerForm.passwordError" id="passwordHelp2" class="form-text text-muted">A mixture of both uppercase and lowercase letters</small>
            <small v-if="!registerForm.passwordError" id="passwordHelp3" class="form-text text-muted">A mixture of letters and numbers</small>
            <small v-if="!registerForm.passwordError" id="passwordHelp4" class="form-text text-muted">Inclusion of at least one special character, e.g., ! @ # ? ]</small>

            <div v-show="registerForm.passwordError" class="invalid-feedback">{{ registerForm.passwordError }}</div>
          </div>

          <div>
            <hua-kuai @verify='verify' @refresh='refresh'></hua-kuai>
          </div>
          
          <br />

          <button type="submit" class="btn btn-primary">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// import {request_withdata} from '@/network/request';
// import axios from 'axios'
import { add_prefix } from '../../utils'

export default {
  name: 'Register', //this is the name of the component
  data () {
    return {
      registerForm: {
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
      this.registerForm.submitted = true  // 先更新状态
      this.registerForm.errors = 0

      if (!this.registerForm.username) {
        this.registerForm.errors++
        this.registerForm.usernameError = 'Username required.'
      } else {
        this.registerForm.usernameError = null
      }

      if (!this.registerForm.email) {
        this.registerForm.errors++
        this.registerForm.emailError = 'Email required.'
      } else if (!this.validEmail(this.registerForm.email)) {
        this.registerForm.errors++
        this.registerForm.emailError = 'Valid email required.'
      } else {
        this.registerForm.emailError = null
      }

      if (!this.registerForm.password) {
        this.registerForm.errors++
        this.registerForm.passwordError = 'Password required.'
      } else {
        this.registerForm.passwordError = null
      }

      if (this.verifivation_res == false){
        console.log("ggggggg")
        this.registerForm.errors++
        this.$toasted.success("Please move into the right place", { icon: 'fingerprint' })
      }

      if (this.registerForm.errors > 0) {
        // Stop when the form has error
        return false
      }

      const payload = {
        username: this.registerForm.username,
        email: this.registerForm.email,
        password: this.registerForm.password
      }

      this.$axios.post(add_prefix(`/users`, `/user`), payload)
      .then((res) => {
        // Go to Login Page
        this.$toasted.success('Please verify your email.', { icon: 'fingerprint' })
        console.log('please verify email')
        this.$router.push({path: '/resend', query: {'username': this.registerForm.username}})
        
      }).catch((error) => {
        console.log('error is', error)
        console.log('error end')
        for (var field in error.response.data.message) {
          if (field == 'username') {
            this.registerForm.usernameError = error.response.data.message.username
          } else if (field == 'email') {
            this.registerForm.emailError = error.response.data.message.email
          } else if (field == 'password') {
            this.registerForm.passwordError = error.response.data.message.password
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