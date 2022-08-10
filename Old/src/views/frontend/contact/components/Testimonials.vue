<template>
  <section class="iq-section-space  iq-bg-over">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 ">
          <div class="title-box wow fadeInUp text-center">
            <span class="title-design">TESTIMONIALS</span>
            <h2>100+ Companies are Using Xamin</h2>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12  wow fadeInUp">
          <div class="owl-carousel testimonial-style owl-loaded owl-drag" data-dots="true" data-nav="false" data-autoplay="true" data-loop="true" data-items="1" data-items-laptop="1" data-items-tab="1" data-items-mobile="1" data-items-mobile-sm="1" data-margin="30">
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/37.jpg')">
                  <div class="testimonial-name">
                      <h5>Jack White</h5>
                      <span class="sub-title">CEO</span>
                  </div>
                </div>
                <p>Richard McClintock, a Latin professor at Hampden-Sydney consectetur adip isicing elit, sed dolore magna aliqua hampden. Latin professor at Hampden-Sydney consectetur. </p>
              </div>
            </div>
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/38.jpg')">
                  <div class="testimonial-name">
                      <h5>Walhan Bobe</h5>
                      <span class="sub-title">Business Advisor</span>
                  </div>
                </div>
                <p>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium incididunt ut labore et dolore Sed ut perspiciatis error. Perspiciatis unde omnis iste."</p>
              </div>
            </div>
            <div class="item text-center">
              <div class="iq-testimonial">
                <div class="testimonial-info">
                  <img alt="#" class="img-fluid rounded-circle" :src="require('@/assets/images/landing-page/landing-8/39.jpg')">
                  <div class="testimonial-name">
                      <h5>Mark McManus</h5>
                      <span class="sub-title">COO</span>
                  </div>
                </div>
                <p>“Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.” </p>
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