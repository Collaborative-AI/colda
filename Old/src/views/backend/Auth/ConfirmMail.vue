<template>
    <section class="login-content">
         <img src="../../../assets/images/login/02.png" class="lb-img" alt="">
         <img src="../../../assets/images/login/03.png" class="rb-img" alt="">
         <div class="container-fluid h-100">
            <b-row class=" align-items-center justify-content-center h-100">
               <div class="col-12">
                  <b-row class=" align-items-center">
                     <b-col lg="6" class=" rmb-30">
                        <img src="../../../assets/images/login/01.png" class="img-fluid w-80" alt="">
                     </b-col>
                     <b-col lg="6">
                        <img src="../../../assets/images/login/mail.png" class="img-fluid" width="80" alt="">
                        <h2 class="mt-3 mb-0">Success !</h2>
                        <p class="cnf-mail mb-1">A email has been send to youremail@domain.com. Please check for an
                           email from company and click
                           on the included link to reset your password.</p>
                        <div class="d-inline-block w-100">
                           <button type="submit" class="btn btn-primary mt-3">Back to Home</button>
                        </div>
                     </b-col>
                  </b-row>
               </div>
            </b-row>
         </div>
      </section>
</template>
<script>
export default {
    name:'ConfirmMail'
}
</script>