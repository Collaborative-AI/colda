<template>
    <div class="mt-5 iq-maintenance">
            <div class="container-fluid p-0">
               <b-row class=" no-gutters">
                  <b-col sm="12" class="text-center">
                        <div class="iq-maintenance">
                           <img src="../../../assets/images/error/02.png" class="img-fluid" alt="">
                           <h3 class="mt-4 mb-1">We are Currently Performing Maintenance</h3>
                           <p>Please check back in sometime.</p>
                        </div>
                  </b-col>
               </b-row>
            </div>
            <div class="container mt-3">
               <b-row >
                  <b-col lg="4" >
                        <card class=" text-center">
                          <template v-slot:body>
                              <i class="ri-window-line ri-4x line-height text-primary"></i>
                              <h5 class="card-title mt-1">Why is the Site Down?</h5>
                              <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                          </template>
                        </card>
                  </b-col>
                   <b-col lg="4" >
                        <card class=" text-center">
                           <template v-slot:body>
                              <i class="ri-time-line ri-4x line-height text-primary"></i>
                              <h5 class="card-title mt-1">What is the Downtime?</h5>
                              <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                           </template>
                        </card>
                   </b-col>
                   <b-col lg="4" >
                        <card class=" text-center">
                           <template v-slot:body>
                              <i class="ri-information-line ri-4x line-height text-primary"></i>
                              <h5 class="card-title mt-1">Do you need Support?</h5>
                              <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                           </template>
                        </card>
                   </b-col>
               </b-row>
            </div>
         </div>
</template>
<script>
export default {
    name:'Maintainance'
}
</script>
