<template>
     <section class="login-content">
         <img src="../../../assets/images/login/02.png" class="lb-img" alt="">
         <img src="../../../assets/images/login/03.png" class="rb-img" alt="">
         <div class="container h-100">
            <b-row class=" align-items-center justify-content-center h-100">
               <div class="col-12">
                  <b-row class=" align-items-center">
                     <b-col lg="6"  class=" mb-lg-0 mb-4 mt-lg-0 mt-4">
                        <img src="../../../assets/images/login/01.png" class="img-fluid w-80" alt="">
                     </b-col>
                     <b-col lg="6" >
                        <h2 class="mb-2">Sign Up</h2>
                        <p>Enter your personal details and start journey with us.</p>
                        <form>
                           <b-row >
                              <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="text" placeholder=" ">
                                    <label>Full Name</label>
                                 </div>
                              </b-col>
                               <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="text" placeholder=" ">
                                    <label>Last Name</label>
                                 </div>
                             </b-col>
                              <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="email" placeholder=" ">
                                    <label>Email</label>
                                 </div>
                               </b-col>
                               <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="text" placeholder=" ">
                                    <label>Phone No.</label>
                                 </div>
                               </b-col>
                                <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="password" placeholder=" ">
                                    <label>Password</label>
                                 </div>
                             </b-col>
                              <b-col lg="6" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="password" placeholder=" ">
                                    <label>Confirm Password</label>
                                 </div>
                              </b-col>
                               <b-col lg="12" >
                                 <div class="custom-control custom-checkbox mb-3">
                                    <input type="checkbox" class="custom-control-input" id="customCheck1">
                                    <label class="custom-control-label" for="customCheck1">I agree with the terms of use</label>
                                 </div>
                              </b-col>
                           </b-row>
                           <button type="submit" class="btn btn-primary">Sign Up</button>
                           <p class="mt-3">
                              Already have an Account <router-link to="/sign-in" class="text-primary">Sign In</router-link>
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
    name:'SignUp'
}
</script>