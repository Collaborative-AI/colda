<template>
  <section id="iq-pricing" class="pb-0">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-5">
          <div class="title-box text-left">
            <h2>What can we help you?</h2>
            <p>Choose a suitable packagefor you website and join innovative minds</p>
          </div>
        </div>
        <div class="col-lg-7">
          <div class="custom-tab horizontaltab-demo15 ">
             <tab-nav :pills="true "   id="Pills-tab" extraclass="mb-5" role="tablist" >
                <tab-nav-items :active="true" id="monthly" ariaControls="tab-monthly" role="tab" :ariaSelected="true"  dataToggle="pill" >
                   <template v-slot:title>
                  <h6 class="tab-title"> Monthly</h6>
                  </template>
                </tab-nav-items>
                <tab-nav-items  id="yearly" ariaControls="tab-yearly" role="tab" dataToggle="pill" :ariaSelected="false"  >
                 <template v-slot:title>
                  <h6 class="tab-title"> Yearly</h6>
                </template>
              </tab-nav-items>
                </tab-nav>

             <tab-content >
               <tab-content-item :active="true" id="tab-monthly" aria-labelled-by="monthly">
                <div class="row">
                  <div class="col-lg-6">
                    <div class="vc_column-inner">
                      <div class="wpb_wrapper">
                        <div class="iq-best-pricing active wow fadeInUp  purple-hover"  data-wow-delay="0.6s" >
                          <div class="price-title iq-parallax">
                            <div class="month-circle">
                              <div class="month-price">
                                <h2>
                                  <small>$</small>59.99<small />
                                </h2>
                                <span class="duration">Monthly</span>
                              </div>
                            </div>
                            <h5 class="title">
                              Professional Plan
                            </h5>
                          </div>
                          <ul class="pricing-list">
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Customer Experience
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              24/7 phones & email settings
                            </li>
                          </ul>
                          <div class="price-footer">
                             <a class="landing-button btn-purple" href="#">Explore More</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6">
                    <div class="vc_column-inner">
                      <div class="wpb_wrapper">
                        <div class="iq-best-pricing wow fadeInUp purple-hover"  data-wow-delay="0.6s" >
                          <div class="price-title iq-parallax">
                            <div class="month-circle">
                              <div class="month-price">
                                <h2><small>$</small>39.99<small /></h2>
                                <span class="duration">Monthly</span>
                              </div>
                            </div>
                            <h5 class="title">
                              Standard Plan
                            </h5>
                          </div>
                          <ul class="pricing-list">
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              customer experience
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                          </ul>
                          <div class="price-footer">
                             <a class="landing-button btn-purple" href="#">Explore More</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
               </tab-content-item>
               <tab-content-item :active="false" id="tab-yearly" aria-labelled-by="yearly" >
                <div class="row">
                  <div class="col-lg-6">
                    <div class="vc_column-inner">
                      <div class="wpb_wrapper">
                        <div class="iq-best-pricing active  wow fadeInUp purple-hover  " data-wow-delay="0.6s" >
                          <div class="price-title iq-parallax">
                            <div class="month-circle">
                              <div class="month-price">
                                <h2>
                                  <small>$</small>59.99<small />
                                </h2>
                                <span class="duration">yearly</span>
                              </div>
                            </div>
                            <h5 class="title">
                              Professional Plan
                            </h5>
                          </div>
                          <ul class="pricing-list">
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Customer Experience
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              24/7 phones & email settings
                            </li>
                          </ul>
                          <div class="price-footer">
                            <a class="landing-button btn-purple" href="#">Explore More</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6">
                    <div class="vc_column-inner">
                      <div class="wpb_wrapper">
                        <div class="iq-best-pricing wow fadeInUp purple-hover  "  data-wow-delay="0.6s">
                          <div class="price-title iq-parallax">
                            <div class="month-circle">
                              <div class="month-price">
                                <h2><small>$</small>39.99<small /></h2>
                                <span class="duration">Yearly</span>
                              </div>
                            </div>
                            <h5 class="title">
                              Standard Plan
                            </h5>
                          </div>
                          <ul class="pricing-list">
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              customer experience
                            </li>
                            <li>
                              <span class="mr-2 ">
                                <i class="fa fa-check-circle" /></span>
                              Power And Predictive Dialing
                            </li>
                          </ul>
                          <div class="price-footer">
                           <a class="landing-button btn-purple" href="#">Explore More</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
               </tab-content-item>
             </tab-content>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Pricing'
}
</script>
