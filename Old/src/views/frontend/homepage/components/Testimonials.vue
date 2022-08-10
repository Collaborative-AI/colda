<template>
  <section class="iq-section-space  iq-bg-over">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 ">
          <div class="title-box wow fadeInUp text-center">
            <span class="title-design">TESTIMONIALS</span>
            <h2>What Our Clients Say</h2>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12  wow fadeInUp">
          <div class="owl-carousel testimonial-style owl-loaded owl-drag" data-dots="true" data-nav="false" data-autoplay="true" data-loop="true" data-items="1" data-items-laptop="1" data-items-tab="1" data-items-mobile="1" data-items-mobile-sm="1" data-margin="30">
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/united-health.jpg')">
                  <div class="testimonial-name">
                      <h5>United Health</h5>
                      <span class="sub-title">Healthcare Insurance</span>
                  </div>
                </div>
                <p>We have more than lots of partners. A few years ago we tried to use blockchain to leverage scattered data, 
                  but not very successful. Anything that can improve the assessment of risk is useful for us. So we collaborate 
                  a lot with other organizations. Everybody does not trust another. For example, payers don’t trust service providers.
                   It would be great if any product can resolve trust issues.</p>
              </div>
            </div>
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/anthem.jpg')">
                  <div class="testimonial-name">
                      <h5>Anthem</h5>
                      <span class="sub-title">Healthcare Insurance</span>
                  </div>
                </div>
                <p>We use API to share data with other insurance companies. There are expensive procedures that require prior 
                  authorization. Agreement for multiple parties must be constantly settled.</p>
              </div>
            </div>
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/cvs.jpg')">
                  <div class="testimonial-name">
                      <h5>CVS Health</h5>
                      <span class="sub-title">Pharmacy</span>
                  </div>
                </div>
                <p>It is not possible to dive into the data market in a short amount of time. We need a recommendation on what 
                  external data would be useful. </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
    name:'Testimonials'
}
</script>