<template>
    <div class="container-fluid">
         <b-row>
            <b-col lg="4">
               <card class=" card-block p-card">
                  <div class="profile-box">
                     <div class="profile-card rounded">
                        <img src="../../../../assets/images/user/12.jpg" alt="profile-bg" class="avatar-100 rounded d-block mx-auto img-fluid mb-3">
                        <h3 class="font-600 text-white text-center mb-0">John Doe</h3>
                        <p class="text-white text-center mb-5">Web Developer</p>
                     </div>
                     <div class="pro-content rounded">
                        <div class="d-flex align-items-center mb-3">
                           <div class="p-icon mr-3">
                              <i class="las la-envelope-open-text"></i>
                           </div>
                           <p class="mb-0 eml">johndoe9891@gmail.com</p>
                        </div>
                        <div class="d-flex align-items-center mb-3">
                           <div class="p-icon mr-3">
                              <i class="las la-phone"></i>
                           </div>
                           <p class="mb-0">(123) 123 1234</p>
                        </div>
                        <div class="d-flex align-items-center mb-3">
                           <div class="p-icon mr-3">
                              <i class="las la-map-marked"></i>
                           </div>
                           <p class="mb-0">USA</p>
                        </div>
                        <div class="d-flex justify-content-center">
                           <div class="social-ic d-inline-flex rounded">
                              <a href="#"><i class="fab fa-facebook-f"></i></a>
                              <a href="#"><i class="fab fa-twitter"></i></a>
                              <a href="#"><i class="fab fa-youtube"></i></a>
                              <a href="#"><i class="fab fa-pinterest-p"></i></a>
                           </div>
                        </div>
                     </div>
                  </div>
               </card>
            </b-col>
            <b-col lg="8" >
               <card class=" card-block mb-3">
                  <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">About Me</h4>
                  </template>
                  <template v-slot:body>
                     <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
                        dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
                        book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially
                        unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more
                        recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                     </p>
                     <h5 class="mb-2">Personal Skills</h5>
                     <ul class="list-unstyled mb-0">
                        <li class="mb-3"><i class="fa fa-check-circle text-primary fa-lg mr-2"></i>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                        <li class="mb-3"><i class="fa fa-check-circle text-primary fa-lg mr-2"></i>Aliquam ultrices tellus in auctor blandit.</li>
                        <li class="mb-3"><i class="fa fa-check-circle text-primary fa-lg mr-2"></i>Etiam tincidunt erat non ante sagittis bibendum.</li>
                        <li class="mb-3"><i class="fa fa-check-circle text-primary fa-lg mr-2"></i>Nunc malesuada massa ut nisl sollicitudin semper.</li>
                        <li><i class="fa fa-check-circle text-primary fa-lg mr-2"></i>Fusce et arcu in dui feugiat finibus.</li>
                     </ul>
                     <h5 class="mb-2 mt-4">Professional Skills</h5>
                           <span>PHP</span>
                              <span class="float-right">90%</span>
                           <Progressbar :value="90" color="primary" class="iq-progress-bar-linear pro-skill d-inline-block w-100 mb-3" />
                           <span>MySQl</span>
                              <span class="float-right">85%</span>
                           <Progressbar :value="85" color="danger" class="iq-progress-bar-linear pro-skill d-inline-block w-100 mb-3" />
                           <span>Node Js</span>
                              <span class="float-right">70%</span>
                           <Progressbar :value="70" color="warning"  class="iq-progress-bar-linear pro-skill d-inline-block w-100 mb-3" />
                           <span>Angular Js</span>
                              <span class="float-right">55%</span>
                           <Progressbar :value="55" color="info"  class="iq-progress-bar-linear pro-skill d-inline-block w-100 mb-3" />
                     </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
export default {
    name:'ContactDetails'
}
</script>