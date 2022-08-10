<template>
  <FooterMain footer-class="">
    <template v-slot:footerContent>
      <div class="row">
        <div class="col-md-12">
          <div class="footer-top">
            <div class="row">
              <div class="col-lg-3 col-md-6 iq-rmb-50 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
                <FooterLogo
                  :section-image="navLogo"
                  section-color="white iq-font-black mb-4 mt-4"
                  section-text="Simply dummy text of the printing and typesetting industry."
                >
                   <template v-slot:icons>
                     <ul class="social-links p-0 m-0">
                      <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                      <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                      <li><a href="#"><i class="fab fa-google-plus-g"></i></a></li>
                      <li><a href="#"><i class="fab fa-dribbble"></i></a></li>
                    </ul>
                   </template>
                </FooterLogo>
              </div>
              <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
                <FooterLinks title="Menu" color="white mb-4" :content="footerHome"  :content1="footerHome1" />
              </div>
              <div class="col-lg-3 col-md-6 iq-rmt-50 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
                <FooterAddress :address-content="footerText" address-color="white mb-4" address-title="Contact Us" />
              </div>
              <div class="col-lg-3 col-md-6 iq-rmt-50 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
                <h4 class="mb-4">
                  Get Started
                </h4>
                <form class="subscribe-form">
                  <input type="email" name="email" class="form-control subscription-email " placeholder="Email">
                  <button type="button" class="landing-button btn-primary  mt-3">Sign Up</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6 col-md-6 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;" >
          <ul class="links list-unstyled">
            <li class="list-inline">
              <a href="#">{{appName}} Terms</a>
            </li>
            <li class="list-inline">
              <a href="#">Privacy Policy</a>
            </li>
          </ul>
        </div>
        <div class="col-lg-6 col-md-6 text-right wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
          <div class="copyright">
            Copyright 2019 <a href="#" class="text-orange">{{appName}}</a> All Rights Reserved.
          </div>
        </div>
      </div>
    </template>
  </FooterMain>
</template>
<script>
import { mapGetters } from 'vuex'
import FooterMain from '../FooterComponent/FooterMain'
import FooterAddress from '../FooterComponent/FooterAddress'
import FooterLogo from '../FooterComponent/FooterLogo'
import FooterLinks from '../FooterComponent/FooterLinks'
import logoImg from '../../../../assets/images/logo-white.png'
export default {
  name: 'FooterStyle3',
  components:{
      FooterMain,
      FooterAddress,
      FooterLogo,
      FooterLinks
  },
  data () {
    return {
      navLogo: logoImg,
      footerText: [
        {
          icon: true,
          iconClass: 'ion-ios-location-outline',
          text: '1234 North Luke Lane, South Bend, IN 360001'
        },
        {
          icon: true,
          iconClass: 'ion-ios-telephone-outline',
          text: '+0123 456 789'
        },
        {
          icon: true,
          iconClass: 'ion-ios-email-outline',
          text: 'mail@sofbox.com'
        }
      ],
      footerHome: [
            {
              href: 'javascript:void(0)',
              title: 'Home'
            },
            {
              href: 'javascript:void(0)',
              title: 'About us'
            },
            {
              href: 'javascript:void(0)',
              title: 'Pages'
            },
            {
              href: 'javascript:void(0)',
              title: 'Services'
            },
            {
              href: 'javascript:void(0)',
              title: 'Contact'
            }
          ],
    footerHome1: [
            {
              href: 'javascript:void(0)',
              title: 'Team'
            },
            {
              href: 'javascript:void(0)',
              title: 'Blog'
            },
            {
              href: 'javascript:void(0)',
              title: 'Partner'
            },
            {
              href: 'javascript:void(0)',
              title: 'Features'
            },
             {
              href: 'javascript:void(0)',
              title: 'Testimonial'
            }
      ]

    }
  },
   computed : {
        ...mapGetters({
            appName: 'appName'
        })
    }
}
</script>
