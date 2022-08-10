<template>
  <section class="pt-0 iq-section-space iq-section-pb-70 position-relative overflow-hidden">
    <div style="margin-top:100px" class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="title-box wow fadeInUp text-center" data-wow-delay=".3s">
                  <!-- <span class="title-design">Our Products</span> -->
                  <h2>Our Products</h2>


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
                                    <h5 class="mb-2 active-title">API</h5>
                                    <p class="mb-0">The Synspot API is designed to provide an easy and efficient
                  way to train your model our platform</p>
                                                              <div class="btn-container mt-4 wow fadeInUp" data-wow-delay=".9s">
                            <!-- <a target="_blank" href="html/index.html">Learn More</a>
                                          <a target="_blank" href="html/index.html" style="text-decoration: none">Documentation</a> -->

                        </div>
                                </div>
                              </div>
                            </template>
                        
                       </tab-nav-items>
                         <tab-nav-items :active="false" id="services" ariaControls="tab-application-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                              <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/07.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">Application</h5>
                                    <p class="mb-0">Applications for your Windows or MacOS device</p>
                                                            <div class="btn-container mt-4 wow fadeInUp" data-wow-delay=".9s">
                            <!-- <button class="landing-button btn-primary" style="float:left" ><span>Windows</span><em></em></button> -->
                                  <a href="/file/SynSpot Setup 0.0.2.exe" download class="btn btn-primary text-white" style="float:left; margin: 0px auto">Windows</a>

                                  &nbsp; &nbsp; &nbsp; &nbsp;
                                  <a href="/file/SynSpot-0.0.2.dmg" download class="btn btn-primary text-white" style="float:left; margin: 0px 20px">MacOS</a>
                        </div>

                                </div>
                              </div>
                              </template>
                        
                         </tab-nav-items>
                           <!-- <tab-nav-items :active="false" id="analytics"     ariaControls="tab-data-analytics" role="tab" dataToggle="pill" :ariaSelected="false" >
                     
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
                         
                           </tab-nav-items> -->

                  </tab-nav>
                  <!-- <a href="/file/SynSpot Setup 0.0.2.exe" download class="btn btn-primary text-white" style="float:left; margin: 0px auto; position:relative; top:-150px; left: 150px">Windows</a>
                  <a href="/file/SynSpot-0.0.2.dmg" download class="btn btn-primary text-white" style="float:left; margin: 0px 20px; position:relative; top:-150px; left: 150px">MacOS</a> -->

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