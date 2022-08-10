<template>
    <section class="login-content">
         <img src="../../../assets/images/login/02.png" class="lb-img" alt="">
         <img src="../../../assets/images/login/03.png" class="rb-img" alt="">
         <div class="container h-100">
            <b-row class=" align-items-center justify-content-center h-100">
               <div class="col-12">
                  <b-row class=" align-items-center">
                     <b-col lg="6" class=" rmb-30">
                        <img src="../../../assets/images/login/01.png" class="img-fluid w-80" alt="">
                     </b-col>
                     <b-col lg="6">
                        <h2 class="mb-2">Reset Password</h2>
                        <p>Enter your email address and we'll send you an email with instructions to reset your password.</p>
                        <form>
                           <b-row >
                              <b-col lg="12" >
                                 <div class="floating-label form-group">
                                    <input class="floating-input form-control" type="email" placeholder=" ">
                                    <label>Email</label>
                                 </div>
                              </b-col>
                           </b-row>
                           <button type="submit" class="btn btn-primary">Reset</button>
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
    name:'RecoverPassword'
}
</script>