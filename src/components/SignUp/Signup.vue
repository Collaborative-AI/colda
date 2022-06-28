<template>
    <div class="signup-section ptb-100">
            <div class="container">
                <div class="signup-form">
                    <h3>Create your Account</h3>
                    <form>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="Username">
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="email" class="form-control" placeholder="Email">
                                </div>
                            </div>

                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="Password">
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
    export default {
        name: 'Signup',
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
            
        }
    }
</script>