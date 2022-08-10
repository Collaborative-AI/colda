<template>
   <section class="iq-pricing pt-0" id="pricing">
            <div class="container ">
                <div class="row no-gutters">
                    <div class="col-sm-12">
                        <div class="title-box text-center">
                            <h6 class="title text-white">Pricing</h6>
                            <h2 class="text-white">Our Pricing</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12 text-center">
                        <div class="pricing-tab">
                            <span>Monthly</span>



                             <tab-nav :pills="true "   id="Pills-tab" extraclass="iq-mt-40" role="tablist" >
                           
                                  <tab-nav-items :active="true" id="monthly" ariaControls="monthly-tab" role="tab" :ariaSelected="true"  dataToggle="pill"  >
                                
                                  </tab-nav-items>
                                    <tab-nav-items :active="false" id="yearly" ariaControls="yearly-tab" role="tab" dataToggle="pill" :ariaSelected="false"  >
                             
                                    </tab-nav-items>
                          
                             </tab-nav>
                            <span>Yearly</span>
                        </div>
                      
                         <tab-content id="pills-tabContent">
                               <tab-content-item :active="true" id="monthly-tab" aria-labelled-by="monthly" role="tabpanel">
                            
                                <div class="row">
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Personal</h4>
                                                <h2>19$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-times-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Business</h4>
                                                <h2>49$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-times-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Enterprice</h4>
                                                <h2>99$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-check-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                </div>
                           
                               </tab-content-item>
                                 <tab-content-item :active="false" id="yearly-tab" aria-labelled-by="yearly" role="tabpanel">
                            
                                <div class="row">
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Personal</h4>
                                                <h2>19$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-times-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Business</h4>
                                                <h2>49$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-times-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-times-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                    <div class="col-lg-4 col-md-6 col-sm-12 ">
                                        <div class="iq-pricing-table ">
                                            <div class="pricing-header">
                                                <h4 class=" mb-5">Enterprice</h4>
                                                <h2>99$<span>/ Per Month</span></h2>
                                            </div>
                                            <ul class="list-unstyled">
                                                <li class=""><i class="fas fa-check-circle"></i>Ut eu lectus consequat.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean a neque.</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Aenean lacinia porttitor.
                                                </li>
                                                <li class=""><i class="fas fa-check-circle"></i>Unknown printer took</li>
                                                <li class=""><i class="fas fa-check-circle"></i>Embarrassing hidden</li>
                                            </ul>
                                            <a class="landing-button btn-primary mt-5" href="#">Choose Plan</a>
                                        </div>
                                    </div>
                                </div>
                           
                                 </tab-content-item>
                         </tab-content>
                       
                    </div>
                </div>
            </div>
        </section>
  
</template>
<script>


export default {
  name: 'Pricing',
 
}
</script>
