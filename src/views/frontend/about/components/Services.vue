<template>
  <section class="pt-0 iq-section-space iq-section-pb-70 position-relative overflow-hidden">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="title-box wow fadeInUp text-center" data-wow-delay=".3s">
                  <span class="title-design">OUR SERVICES</span>
                  <h2>Our Exclusive Offerings</h2>
                </div>
            </div>
          </div>
          <div class="row custom-tab verticaltab3">
            <div class="col-md-6">
                <div class="col-lg-12 col-md-12 ">
                  <tab-nav :pills="true " :vertical="true"  id="Pills-tab" extraclass="nav-pills-style-3 mb-5" role="tablist" aria="vertical">
                    
                       <tab-nav-items :active="true" id="development"  dataToggle="pill" ariaControls="tab-software-development" role="tab" :ariaSelected="true" >
                       
                            <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/06.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">Software Development</h5>
                                    <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                                </div>
                              </div>
                            </template>
                        
                       </tab-nav-items>
                         <tab-nav-items :active="false" id="services"     ariaControls="tab-application-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                              <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/07.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">Application Services</h5>
                                    <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                                </div>
                              </div>
                              </template>
                        
                         </tab-nav-items>
                           <tab-nav-items :active="false" id="analytics"     ariaControls="tab-data-analytics" role="tab" dataToggle="pill" :ariaSelected="false" >
                     
                             <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/08.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">Data Analytics</h5>
                                    <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                                </div>
                              </div>
                             </template>
                         
                           </tab-nav-items>
                           <tab-nav-items :active="false" id="services"     ariaControls="tab-help-desk-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                             <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/09.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">Help Desk Services</h5>
                                    <p class="mb-0">It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                                </div>
                              </div>
                             </template>
                         
                           </tab-nav-items>
                   
                  </tab-nav>
                  </div>
            </div>
            <div class="col-md-6 ">
               <tab-content >
                 <tab-content-item :active="true" id="tab-software-development" aria-labelled-by="development">
                
                    <div class="prox-right-img-wm">
                          <img width="863" height="528" :src="require('@/assets/images/landing-page/landing-8/10.png')" class="attachment-full"  sizes="100vw">
                    </div>
              
                 </tab-content-item>
                   <tab-content-item :active="false" id="tab-application-services" aria-labelled-by="services">
                
                    <div class=" prox-right-img-wm">
                          <img width="863" height="528" :src="require('@/assets/images/landing-page/landing-8/11.png')" class="attachment-full"  sizes="100vw">
                    </div>
               
                   </tab-content-item>
                   <tab-content-item :active="false" id="tab-data-analytics" aria-labelled-by="analytics">
               
                    <div class=" prox-right-img-wm">
                          <img width="863" height="528" :src="require('@/assets/images/landing-page/landing-8/10.png')" class="attachment-full"  sizes="100vw">
                    </div>
                
                   </tab-content-item>
                    <tab-content-item :active="false" id="tab-help-desk-services" aria-labelled-by="desk-services">
               
                    <div class=" prox-right-img-wm">
                          <img width="863" height="528" :src="require('@/assets/images/landing-page/landing-8/11.png')" class="attachment-full"  sizes="100vw">
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
    name:'Services'
}
</script>