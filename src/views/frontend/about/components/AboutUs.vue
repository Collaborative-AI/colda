<template>
  <section class="pt-0 iq-section-space postion-relative overflow-hidden">
    <div class="container">
        <div class="row">
          <div class="col-lg-6 wow fadeInUp align-items-center" data-wow-delay=".3s">
              <div class="row">
                <div class="col-md-12">
                    <div class="title-box  text-center">
                      <span class="title-design">ABOUT US OUR COMPANY</span>
                      <h2>What is Data Analytics?</h2>
                    </div>
                </div>
              </div>
              <div class="row custom-tab verticaltab2 text-left  ">
                <div class="col-lg-4 col-md-12 ">
                   <tab-nav :pills="true "   id="Pills-tab" extraclass=" mb-5 " role="tablist" aria="vertical">
                       <tab-nav-items :active="true" id="about" ariaControls="tab-about-us" role="tab" :ariaSelected="true" dataToggle="pill">
                      <template v-slot:title>
                  <h5 class="tab-title text-dark">About Us</h5>
                </template>
                       </tab-nav-items>
                        <tab-nav-items :active="false" id="vision"  ariaControls="tab-our-vision" role="tab" dataToggle="pill" :ariaSelected="false" title="Application Services" liClass=" nav-item w-inherit"  widthclass="w-100" >
              <template v-slot:title>
                  <h5 class="tab-title text-dark">Our Vision</h5>
                </template>
                </tab-nav-items>
                       <tab-nav-items :active="false" id="mission"  ariaControls="tab-our-mission" role="tab" dataToggle="pill" :ariaSelected="false" title="Application Services" liClass=" nav-item w-inherit"  widthclass="w-100" >
              <template v-slot:title>
                  <h5 class="tab-title text-dark">Our Mission</h5>
                </template>
                </tab-nav-items>
                   </tab-nav>
                </div>
        
                <div class="col-lg-8 col-md-12 ">
                    <tab-content >
         <tab-content-item :active="true" id="tab-about-us" aria-labelled-by="about">
                   
                      <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
                      <p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for ‘lorem ipsum’ will uncover many web sites still in their infancy.</p>
                      <div class=" text-left  "><a class="landing-button btn-primary" href="#"> View Details</a></div>
                    
         </tab-content-item>
           <tab-content-item :active="false" id="tab-our-vision" aria-labelled-by="vision">
                   
                      <p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for ‘lorem ipsum’ will uncover many web sites still in their infancy.</p>
                      <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. rem ipsum’ will uncover many web sites still in their infancy. </p>
                      <div class=" text-left  "><a class="landing-button btn-primary" href="#"> View Details</a></div>
                    
           </tab-content-item>
            <tab-content-item :active="false" id="tab-our-mission" aria-labelled-by="mission">
                    
                      <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. Many desktop publishing packages and web page editors now use.</p>
                      <p>Lorem Ipsum as their default model text, and a search for ‘lorem ipsum’ will uncover many web sites still in their infancy. </p>
                      <div class=" text-left  "><a class="landing-button btn-primary" href="#"> View Details</a></div>
                  
            </tab-content-item>
                    </tab-content>
                </div>
              </div>
          </div>
          <div class="col-lg-6  wow fadeInUp prox-right-img" data-wow-delay=".6s">
              <img :src="require('@/assets/images/landing-page/landing-8/05.png')" alt="about">
          </div>
        </div>
    </div>
  </section>
</template>
<script>
export default {
    name:'AboutUs'
}
</script>