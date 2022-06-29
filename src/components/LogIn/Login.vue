<template>
    <div class="login-section ptb-100">
        <div class="container">
            <div class="login-form">
                <div class="login-title">
                    <h3>Welcome Back!</h3>
                    <p>Please sign in to your account.</p>
                </div>
                    
                <form @submit.prevent="onSubmit">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="form-group">
                                <input type="text" v-model="loginForm.username" class="form-control" placeholder="Username">
                                <div v-if="loginForm.usernameError">{{ loginForm.usernameError }}</div>
                                
                            </div>
                        </div>

                        <div class="col-lg-12">
                            <div class="form-group">
                                <input type="password" v-model="loginForm.password" class="form-control" placeholder="Password">
                                <div v-if="loginForm.passwordError">{{ loginForm.passwordError }}</div>
                                
                            </div>
                        </div>

                        <div class="col-lg-12">
                            <div class="form-check">
                                <input type="checkbox" class="form-check-input" id="checkme">
                                <label class="form-check-label" for="checkme">Keep Me Sign In</label>
                            </div>
                        </div>

                        <div class="col-lg-12 text-right">
                            <p class="forgot-password"><a href="#">Forgot Password?</a></p>
                        </div>

                        <div class="col-lg-12">
                            <div class="send-btn">
                                <button type="submit" class="default-btn">
                                    Sign In Now
                                    <span></span>
                                </button>
                            </div>
                            <br>
                            <span>Don't have account? <router-link to="/sign-up">Sign Up!</router-link></span>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <div class="default-shape">
            <div class="shape-1">
                <img src="../../assets/images/shapes/shape-4.png" alt="image">
            </div>

            <div class="shape-2 rotateme">
                <img src="../../assets/images/shapes/shape-5.svg" alt="image">
            </div>

            <div class="shape-3">
                <img src="../../assets/images/shapes/shape-6.svg" alt="image">
            </div>

            <div class="shape-4">
                <img src="../../assets/images/shapes/shape-7.png" alt="image">
            </div>

            <div class="shape-5">
                <img src="../../assets/images/shapes/shape-8.png" alt="image">
            </div>
        </div>
    </div>
</template>

<script>
import {add_prefix} from '../../utils.js'
// import {request} from '../../network/request.js'
export default {
    name: 'Login',
    data () {
        return {
            loginForm: {
                username: 'xie2',
                password: 'Xie20123',
                submitted: false,  // 是否点击了 submit 按钮
                errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
                usernameError: null,
                passwordError: null
            },
        }
    },
    components: {

    },
    methods: {
        onSubmit() {
            let vm = this
            console.log('r is', vm.$axios);
            console.log('form is', vm.loginForm.username, vm.loginForm.password)
            vm.loginForm.submitted = true  // 先更新状态
            vm.loginForm.errors = 0

            if (!vm.loginForm.username) {
                vm.loginForm.errors++
                vm.loginForm.usernameError = 'Username required.'
            } else {
                vm.loginForm.usernameError = null
            }

            if (!vm.loginForm.password) {
                vm.loginForm.errors++
                vm.loginForm.passwordError = 'Password required.'
            } else {
                vm.loginForm.passwordError = null
            }                
            if (this.loginForm.errors > 0) {
                // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
                return false
            }
            const path = `/tokens`
            // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
            vm.$axios.post(add_prefix(path, `/auth`), {}, {
                auth: {
                'username': vm.loginForm.username,
                'password': vm.loginForm.password
                }
            }).then((response) => {
                // console.log('4321', this.$route,this.exe_position)
                // handle success
                if (response.data == 'not verify email yet'){
                    // this.$router.push({path: '/resend', query: {'username': this.loginForm.username}})
                    // this.$toasted.success(`A verification link has been sent. Please check your email`, { icon: 'fingerprint' })
                    console.log('email not verify');

                } else{
                    console.log('token is' ,response.data.token)
                    window.localStorage.setItem('Apollo-token', response.data.token)
                    // console.log('store user id is', vm.$store.state.user_id);
                    let user_id = JSON.parse(atob(window.localStorage.getItem('Apollo-token').split('.')[1])).user_id
                    vm.$store.state.user_id = user_id

                    // store.loginAction()

                    // const name = JSON.parse(atob(response.data.token.split('.')[1])).name
                    // vm.$toasted.success(`Welcome ${name}!`, { icon: 'fingerprint' })
                    console.log("####", window.localStorage.getItem('Apollo-token'))
                    vm.$router.push('dashboard1')
                    
                    // if (this.$route != undefined){
                    //     if (typeof this.$route.query.redirect == 'undefined') {
                    //         this.$router.push('/')
                    //     } else {
                    //         this.$router.push(this.$route.query.redirect)
                    //     }
                    // }
                    
                    // console.log('chongfeng ', unittest_callbacks)
                    // execute_unittest_list(unittest_callbacks, 0, "Login_unittest")
                }
                
                })
            .catch((error) => {
            // handle error
                if (error.response && error.response.status == 401 ) {
                    vm.loginForm.usernameError = 'Invalid username or password.'
                    vm.loginForm.passwordError = 'Invalid username or password.'
                    console.log('user error is', vm.loginForm.usernameError);
                } else {
                    console.log("666")
                    console.log(error)
                }
            })
        }
    }
}

</script>