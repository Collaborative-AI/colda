<template>
     <div class="container-fluid">
         <b-row >
            <div class="pricing-custom-tab w-100">
               <div class="tab-title-info position-relative">
                  <b-col sm="12" class=" p-0">
                        <tab-nav :pills="true "  id="pricing-pills-tab" extraclass=" d-flex nav mb-5 align-items-center justify-content-center" role="tablist" >
                           <tab-nav-items :active="true" id="data1" ariaControls="pricing-data1" dataToggle="pill" role="tab" :ariaSelected="true" title="Daily"/>
                           <li class="nav-item">
                              <div class="avatar-30 star-circle"><i class="ri-star-fill"></i>
                              </div>
                           </li>
                           <tab-nav-items :active="false" id="services"  ariaControls="pricing-data2" role="tab" dataToggle="pill" :ariaSelected="false" title="Monthly" />
                        </tab-nav>
                  </b-col>
               </div>
                <tab-content >
                   <tab-content-item :active="true" id="pricing-data1" aria-labelled-by="data1">
                     <b-row class=" m-0">
                        <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details" bodyClass="border text-center rounded">
                             <template v-slot:body>
                                 <div class="pricing-header">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder">$26<small class="font-size-14 text-muted">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Max Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-primary mt-5">Start Starter</a>
                             </template>
                           </card>
                        </b-col>
                        <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details" bodyClass="border text-center rounded">
                              <template v-slot:body>
                                 <div class="pricing-header">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder">$39<small class="font-size-14 text-muted">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Average Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-primary mt-5">Start Starter</a>
                              </template>
                           </card>
                         </b-col>
                        <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details" bodyClass="border text-center rounded">
                               <template v-slot:body>
                                 <div class="pricing-header">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder">$48<small class="font-size-14 text-muted">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Minimum Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-primary mt-5">Start Starter</a>
                              </template>
                           </card>
                       </b-col>
                     </b-row>
                   </tab-content-item>
                   <tab-content-item :active="false" id="pricing-data2" aria-labelled-by="data2">
                     <div class="d-flex align-items-center">
                         <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details" bodyClass="border text-center rounded">
                             <template v-slot:body>
                                 <div class="pricing-header bg-primary text-white">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder text-white">$26<small class="font-size-14">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Max Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-primary mt-5">Start Starter</a>
                             </template>
                           </card>
                        </b-col>
                         <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details " bodyClass="border text-center rounded">
                              <template v-slot:body>
                                 <div class="pricing-header bg-success text-white">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder text-white">$26<small class="font-size-14">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Max Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-success mt-5">Start Starter</a>
                               </template>
                           </card>
                        </b-col>
                         <b-col lg="4" sm="6" >
                           <card class=" card-block card-stretch card-height blog pricing-details" bodyClass="border text-center rounded">
                              <template v-slot:body>
                                 <div class="pricing-header bg-danger text-white">
                                    <div class="icon-data"><i class="ri-star-line"></i>
                                    </div>
                                    <h2 class="mb-4 display-5 font-weight-bolder text-white">$26<small class="font-size-14">/ Month</small></h2>
                                 </div>
                                 <h3 class="mb-3">Max Usage</h3>
                                 <ul class="list-unstyled mb-0">
                                    <li>Lorem ipsum dolor sit amet</li>
                                    <li>Consectetur adipiscing elit</li>
                                    <li>Integer molestie at massa</li>
                                    <li>Facilisis in pretium nisl aliquet</li>
                                    <li>Nulla volutpat aliquam velit</li>
                                 </ul> <a href="#" class="btn btn-danger mt-5">Start Starter</a>
                              </template>
                           </card>
                        </b-col>
                     </div>
                   </tab-content-item>
                </tab-content>
            </div>
         </b-row>
      </div>
</template>
<script>
export default {
    name:'Pricing4'
}
</script>