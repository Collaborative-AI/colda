<template>
    <div class="signup-section ptb-100">
            <div class="container">
                <div class="signup-form">
                    <h3>Create your Account</h3>
                    <form @submit.prevent="onSubmit">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="text" v-model="registerForm.username" class="form-control" placeholder="Username">
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="email" v-model="registerForm.email" class="form-control" placeholder="Email">
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="password" v-model="registerForm.password" class="form-control" placeholder="Password">
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="form-check">
                                    <input type="checkbox" class="form-check-input" id="checkme">
                                    <label class="form-check-label" for="checkme">Keep Me Sign Up</label>
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="send-btn">
                                    <button type="submit" class="default-btn">
                                        Sign Up Now
                                        <span></span>
                                    </button>
                                </div>
                                <br>
                                <span>Already a registered user? <router-link to="/sign-in">Sign In!</router-link></span>
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
    export default {
        name: 'Signup',
        data () {
            return {
                registerForm: {
                    username: 'xie2',
                    email: 'xxie43@asu.edu',
                    password: 'Xie20123',
                    submitted: false,  // 是否点击了 submit 按钮
                    errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
                    usernameError: null,
                    emailError: null,
                    passwordError: null
                },
            }
        },
        components: {

        },
        methods: {
            onSubmit() {
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
                } 
                // else if (!this.validEmail(this.registerForm.email)) {
                //     this.registerForm.errors++
                //     this.registerForm.emailError = 'Valid email required.'
                // } 
                else {
                    this.registerForm.emailError = null
                }

                if (!this.registerForm.password) {
                    this.registerForm.errors++
                    this.registerForm.passwordError = 'Password required.'
                } else {
                    this.registerForm.passwordError = null
                }

                // if (this.verifivation_res == false){
                //     console.log("ggggggg")
                //     this.registerForm.errors++
                //     this.$toasted.success("Please move slider to the right place", { icon: 'fingerprint' })
                // }

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
                .then(() => {
                    // Go to Login Page
                    // this.$toasted.success('A verification link has been sent. Please check your email', { icon: 'fingerprint' })
                    console.log('please verify email')
                    // this.$router.push({path: '/resend', query: {'username': this.registerForm.username, 'email': this.registerForm.email}})
                    
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

            }
        
            
        }
    }
</script>