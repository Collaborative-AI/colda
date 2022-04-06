<template>
  <div class="container">
    <h1>Sign In</h1>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="loginForm.username" class="form-control" v-bind:class="{'is-invalid': loginForm.usernameError}" id="username" placeholder="">
            <div v-show="loginForm.usernameError" class="invalid-feedback">{{ loginForm.usernameError }}</div>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="loginForm.password" class="form-control" v-bind:class="{'is-invalid': loginForm.passwordError}" id="password" placeholder="">
            <div v-show="loginForm.passwordError" class="invalid-feedback">{{ loginForm.passwordError }}</div>
          </div>

          <div>
            <hua-kuai @verify='verify' @refresh='refresh'></hua-kuai>
          </div>

          <br />
          
          <button type="submit" class="btn btn-primary">Sign In</button>
        </form>
      </div>
    </div>
    <br>
    <p>New User? <router-link to="/register">Click to Register!</router-link></p>
    <p>
        Forgot Your Password?
        <router-link to="/reset">Click to Reset It</router-link>
    </p>
  </div>
</template>

<script>
import store from '../../store.js'
import { execute_unittest_list, add_prefix } from '../../utils.js'
// console.log('window44', window)
// const store = require('../../store').default

export default {
  name: 'Login',  //this is the name of the component
  data () {
    return {
      sharedState: store.state,
      loginForm: {
        username: '',
        password: '',
        submitted: false,  // 是否点击了 submit 按钮
        errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
        usernameError: null,
        passwordError: null
      },
      verification_res: false,
      root: '',
      exe_position: '',
    }
  },
  methods: {
    verify(result){
      console.log(result) // result为true表示验证通过，false表示验证三次都失败了哦
      if (result == true){
        this.verification_res = true;
      }
    },

    refresh(){
      console.log('用户点击了初始化')
    },

    onSubmit (unittest_callbacks) {
      let vm = this
      console.log("submittttt", arguments.length, this.loginForm.username, this.loginForm.password)
      this.loginForm.submitted = true  // 先更新状态
      this.loginForm.errors = 0

      if (!this.loginForm.username) {
        this.loginForm.errors++
        this.loginForm.usernameError = 'Username required.'
      } else {
        this.loginForm.usernameError = null
      }

      if (!this.loginForm.password) {
        this.loginForm.errors++
        this.loginForm.passwordError = 'Password required.'
      } else {
        this.loginForm.passwordError = null
      }

       console.log("!!!", this.loginForm.username)
      if (this.verification_res == false){
        console.log("ggggggg")
        this.loginForm.errors++
        this.$toasted.success("Please move slider into the right place", { icon: 'fingerprint' })
      }
      
      if (this.loginForm.errors > 0) {
        // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }

      // const payload = {
      //   auth: {
      //     'username': this.loginForm.username,
      //     'password': this.loginForm.password
      //   }
      // }
      // // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
      // this.$axios.post('/tokens', payload)
      console.log("!!!", this.loginForm.username)
      const path = `/tokens`
      // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
      this.$axios.post(add_prefix(path, `/auth`), {}, {
        auth: {
          'username': this.loginForm.username,
          'password': this.loginForm.password
        }
      }).then((response) => {
          console.log('4321', this.$route,this.exe_position)
          // handle success
          if (response.data == 'not verify email yet'){
            this.$router.push({path: '/resend', query: {'username': this.loginForm.username}})
            this.$toasted.success(`Please verify your email`, { icon: 'fingerprint' })

          } else{
            console.log('token is' ,response.data.token)
            window.localStorage.setItem('Apollo-token', response.data.token)
            store.loginAction()

            const name = JSON.parse(atob(response.data.token.split('.')[1])).name
            this.$toasted.success(`Welcome ${name}!`, { icon: 'fingerprint' })
            console.log("####")
            
            if (this.$route != undefined){
              if (typeof this.$route.query.redirect == 'undefined') {
              this.$router.push('/')
            } else {
              this.$router.push(this.$route.query.redirect)
            }
            }
            
            console.log('chongfeng ')
            execute_unittest_list(unittest_callbacks, 0, "Login_unittest")
          }
          
        })
        .catch((error) => {
          // handle error
          if (error.response && error.response.status == 401 ) {
            this.loginForm.usernameError = 'Invalid username or password.'
            this.loginForm.passwordError = 'Invalid username or password.'
          } else {
            console.log("666")
            console.log(error)
          }
        })
    }
  },
  created() {
    // let new_root = store.changeroot()
    // this.root = new_root.root;
    // this.exe_position = new_root.exe_position
    // console.log('login_created', this.$route,  this.root, this.exe_position)
  }
}
</script>