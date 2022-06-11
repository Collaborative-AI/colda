<template>
  <div class="container">
    <h1>Reset</h1>
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

          <!-- <div>
            <hua-kuai @verify='verify' @refresh='refresh'></hua-kuai>
          </div> -->
           <div>
            <drag-verify 
            :width="width"
            :height="height"
            background="#ccc" 
            progress-bar-bg="#66cc66" 
            completed-bg="#66cc66"
            @passcallback='verify'
            ></drag-verify>
          </div>
          
          <br />

          <button type="submit" class="btn btn-primary">Get set new password Link</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { add_prefix, execute_unittest_list, generate_unittest_parameters} from '../../utils';
// import {request_withdata} from '@/network/request';
// import axios from 'axios'
import dragVerify from 'vue-drag-verify'

export default {
  name: 'Reset', //this is the name of the component
  components:{
    dragVerify
  },
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
      isPassing1: false,
      width:280,
      height:35
    }
  },

  methods: {

    verify(){
      this.isPassing1 = true
      console.log('result is', this.isPassing1) // result为true表示验证通过，false表示验证三次都失败了哦
      if (this.isPassing1 == true){
        this.verifivation_res = true;
      }
    },

    refresh(){
      console.log('用户点击了初始化')
    },

    onSubmit (unittest_callbacks) {
      console.log('jinreset', this.resetForm.username, this.resetForm.email)

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

      console.log('faforgot0')
      if (this.verifivation_res == false){
        console.log("ggggggg")
        this.resetForm.errors++
        this.$toasted.success("Please move slider to the right place", { icon: 'fingerprint' })
      }
      console.log('faforgot1')
      if (this.resetForm.errors > 0) {
        // Stop when the form has error
        console.log('faerror');
        return false
      }
      console.log('faforgot2')
      const payload = {
        username: this.resetForm.username,
        email: this.resetForm.email,
      }
      console.log('faforgot3')
      this.$axios.post(add_prefix('/forgot','/user'), payload)
      .then((res) => {
        // Go to Login Page
        this.$toasted.success('A password reset email has been sent via email.', { icon: 'fingerprint' })
        // console.log('resethui', res.data, typeof(res.data))
        let unittest_parameters = generate_unittest_parameters(res.data)
        console.log('unit1', unittest_parameters)
        execute_unittest_list(unittest_callbacks, 0, 'forgot_password_unittest', unittest_parameters)
        
      }).catch((error) => {
        console.log('jinerror');
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