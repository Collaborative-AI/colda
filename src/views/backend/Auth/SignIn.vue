<template>
     <section class="login-content">
         <img src="../../../assets/images/login/02.png" class="lb-img" alt="">
         <img src="../../../assets/images/login/03.png" class="rb-img" alt="">
         <div class="container h-100">
            <b-row class=" align-items-center justify-content-center h-100">
               <div class="col-12">
                  <b-row class=" align-items-center">
                     <div class="col-lg-6 mb-lg-0 mb-4 mt-lg-0 mt-4">
                        <img src="../../../assets/images/login/01.png" class="img-fluid w-80" alt="">
                     </div>
                     <b-col lg="6">
                        <h2 class="mb-2">Sign In</h2>
                        <p>To Keep connected with us please login with your personal info.</p>
                        <form>
                           <b-row>
                              <b-col lg="12" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="email" placeholder=" ">
                                    <label>Email</label>
                                 </div>
                              </b-col>
                              <b-col lg="12" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="password" placeholder=" ">
                                    <label>Password</label>
                                 </div>
                              </b-col>
                              <b-col lg="6" >
                                 <div class="custom-control custom-checkbox mb-3">
                                    <input type="checkbox" class="custom-control-input" id="customCheck1">
                                    <label class="custom-control-label" for="customCheck1">Remember Me</label>
                                 </div>
                              </b-col>
                              <b-col lg="6" >
                                 <router-link to="/auth/recover-password" class="text-primary float-right">Forgot Password?</router-link>
                              </b-col>
                           </b-row>
                           <button type="submit" class="btn btn-primary">Sign In</button>
                           <p class="mt-3">
                              Create an Account <router-link to="/sign-up" class="text-primary">Sign Up</router-link>
                           </p>
                        </form>
                     </b-col>
                  </b-row>
               </div>
            </b-row>
         </div>
      </section>
</template>
<script>
export default {
    name:'SignIn'
}
</script>