<template>
  <section class="pt-0 iq-section-space iq-section-pb-70 position-relative overflow-hidden">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="title-box wow fadeInUp text-center" data-wow-delay=".3s">
                  <span class="title-design"></span>
                  <h2>Frequently Asked Questions</h2>
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
                                    <h5 class="mb-2 active-title">What unique products and services do we provide?</h5>
                                    <p class="mb-0">Synspot provides Distributed Machine Learning as a Service (DMLasS) via Collaborative 
                                      Data Analysis (ColDA) to form a machine learning community of shared interest. Synspot enables collaborators 
                                      to conjointly learn machine learning models without sharing their data, models, and objectives with each other. </p>
                                </div>
                              </div>
                            </template>
                        
                       </tab-nav-items>
                         <tab-nav-items :active="false" id="services"     ariaControls="tab-application-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                              <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/07.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">What is our motivation?</h5>
                                    <p class="mb-0">It is potentially beneficial to improve machine learning models with external data.</p>
                                    <p class="mb-0">It is difficult to leverage external data due to various constraints, i.e. commercial, regulatory, and ethical restrictions.</p>
                                    <p class="mb-0">The machine learning community lacks a trustworthy third-party platform to collaboratively analyze data.</p>
                                </div>
                              </div>
                              </template>
                        
                         </tab-nav-items>
                           <tab-nav-items :active="false" id="analytics"     ariaControls="tab-data-analytics" role="tab" dataToggle="pill" :ariaSelected="false" >
                     
                             <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/08.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">What is Collaborative Data Analysis (ColDA)?</h5>
                                    <p class="mb-0">Collaborative Data Analysis (ColDA) is a distributed generalization of the well-known Gradient Boosting 
                                      algorithm which allows participants to collaboratively optimize the aggregate of local loss functions. Each participant 
                                      autonomously builds its own model by iteratively fitting the pseudo-residuals.</p>
                                </div>
                              </div>
                             </template>
                         
                           </tab-nav-items>
                           <tab-nav-items :active="false" id="services"     ariaControls="tab-help-desk-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                             <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/09.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">What are the advantages of Collaborative Data Analysis (ColDA)?</h5>
                                    <p class="mb-0">ColDA leverages local resources from participants to utilize the predictive power of external data and reduce computation overhead.</p>
                                    <p class="mb-0">ColDA generalizes the classical Gradient Boosting algorithm and allows participants to improve machine learning models without necessarily trusting each other.</p>
                                    <p class="mb-0">ColDA outperforms learning baselines and achieves near-oracle performance on various benchmark datasets. It applies to several real-world use cases such as recommender systems and time-series forecasting.</p>
                                </div>
                              </div>
                             </template>
                         
                           </tab-nav-items>
                           <tab-nav-items :active="false" id="services"     ariaControls="tab-help-desk-services" role="tab" dataToggle="pill" :ariaSelected="false" >
                       
                             <template v-slot:title>
                              <div class="media">
                                <img :src="require('@/assets/images/landing-page/landing-8/09.png')" alt="tab-image" class="img-fluid">
                                <div class="media-body">
                                    <h5 class="mb-2 active-title">How to get started with Collaborative Data Analysis (ColDA)?</h5>
                                    <p class="mb-0">Sponsor: A sponsor initiates a learning task and asks for assistance from Assistors.</p>
                                    <p class="mb-0">Assistor: An assistor provides assistance for a sponsor by locally fitting the pseudo-residuals of the sponsor’s target.</p>
                                    <p class="mb-0">We provide UI/UX enabled software for quick-start and demonstration. Users who are familiar with data science can 
                                      directly start with our open-source Python API ColDA. We also provide use cases and documentation of ColDA.</p>
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