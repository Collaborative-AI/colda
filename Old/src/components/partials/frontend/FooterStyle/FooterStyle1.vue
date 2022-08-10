<template>
  <footer
    id="iq-contact"
    :class="footerClass !== undefined && footerClass ? ' footer-shap footer-one position-relative'+' '+footerClass : ' footer-shap footer-one iq-over-dark-90 position-relative'"
  >
    <div class="container">
      <div class="footer-top">
        <div class="row align-items-center prox-subscribe">
          <div class="col-lg-5   col-sm-12 title-fancy mb-5 mb-lg-0 wow fadeInUp" data-wow-delay=".3s" style="visibility: visible; animation-delay: 0.3s; animation-name: F;">
            <h4 class="footer-title">
              {{ footerTitle }}
            </h4>
            <p class="mb-0">
              {{ footerDescription }}
            </p>
          </div>
          <div class="col-lg-7 col-sm-12 text-center wow fadeInUp" data-wow-delay=".3s" style="visibility: visible; animation-delay: 0.3s; animation-name: F;">
            <input id="inputEmail" type="Email" class="form-control" placeholder="Your Email">
            <a :class="'landing-button sign-up-btn'+' '+ buttonClass" href>Sign up</a>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-5 col-md-6 col-sm-6">
          <div class="logo">
            <a href="#">
              <img :src="footerLogo" class="img-fluid mb-3" width="100" alt="img">
            </a>
            <div :class="'iq-font-black mt-2'+' '+ textClass">
              {{ footerText }}
            </div>
            <div :class="'iq-copyright mt-5'+' '+ textClass">
              Copyright @ 2018
              <a href="#" :class="textClass">{{appName}}</a>
            </div>
          </div>
        </div>
        <div class="col-lg-2 col-md-6 col-sm-6 mt-4 mt-lg-0 mt-md-0">
          <h5 :class="'mb-4' +' '+ textClass">
            Menu
          </h5>
          <ul class="menu">
            <slot name="menu" />
          </ul>
        </div>
        <div class="col-lg-2 col-md-6 col-sm-6 mt-lg-0 mt-4">
          <h5 :class="'mb-4' +' '+ textClass">
            About Us
          </h5>
          <ul class="menu">
            <slot name="aboutus" />
          </ul>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6 mt-lg-0 mt-4 testimonail-widget-menu">
          <slot name="testimonial" />
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'FooterStyle1',
  props: {
    footerLogo: { type: String, default: '' },
    footerText: { type: String, default: '' },
    footerTitle: { type: String, default: '' },
    footerDescription: { type: String, default: '' },
    footerClass: { type: String, default: '' },
    buttonClass: { type: String, default: '' },
    textClass: { type: String, default: '' }
  },
  computed : {
        ...mapGetters({
            appName: 'appName'
        })
    }
}
</script>
