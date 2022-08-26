<template>
  <FooterMain footer-class="">
    <div slot="footerContent">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-12 pr-lg-5">
            <FooterLogo
              :section-image="navLogo"
              section-text="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
            >
            <template v-slot:patent>
                <p class="mt-5 mb-0">Copyrights 2020 ©<span class="text-warning">iqonic.design</span></p>
            </template>
            </FooterLogo>
          </div>
          <div class="col-lg-2 col-md-6">
            <FooterLinks :content="footerHome" title="Useful links" />
          </div>
          <div class="col-lg-3 col-md-6">
            <FooterAddress
              :address-content="footerText"
              address-title="Contact us"
              class="iq-contact"
            />
          </div>
          <div class="col-lg-3 col-md-6 col-sm-12">
            <h4 class="mb-4">
              Instagram
            </h4>
            <div class="instagram-box">
              <div class="row">
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4/instagram-img1.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4//instagram-img2.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4//instagram-img3.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4//instagram-img4.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4//instagram-img5.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4">
                  <div class="iq-instagram position-relative">
                    <img class="w-100" src="../../../../assets/images/landing-page/landing-4//instagram-img6.png" alt="#">
                    <a href="#"><i class="fa fa-instagram text-white" aria-hidden="true" /></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </FooterMain>
</template>
<script>
import FooterMain from '../FooterComponentss/FooterMain'
import FooterLogo from '../FooterComponentss/FooterLogo'
import FooterAddress from '../FooterComponentss/FooterAddress'
import FooterLinks from '../FooterComponentss/FooterLinks'
import logoImg from '../../../../assets/images/logo.png'

export default {
  name: 'Footer4',
  components: { FooterLogo, FooterLinks, FooterAddress, FooterMain },
  data () {
    return {
      navLogo: logoImg,
      footerText: [
        {
          icon: true,
          iconClass: 'fas fa-phone-alt',
          text: '+0123 456 789'
        },
        {
          icon: true,
          iconClass: 'fas fa-envelope',
          text: 'support@iqnonicthemes.com'
        },
        {
          icon: true,
          iconClass: 'fas fa-home',
          text: '1234 North Luke Lane, South Bend, IN 360001'
        }
      ],
      footerHome: [
        {
          href: 'javascript:void(0)',
          title: 'Home'
        },
        {
          href: 'javascript:void(0)',
          title: 'About Us'
        },
        {
          href: 'javascript:void(0)',
          title: 'FAQ'
        },
        {
          href: 'javascript:void(0)',
          title: 'Clients'
        },
        {
          href: 'javascript:void(0)',
          title: 'Contact Us'
        }
      ]
    }
  }
}
</script>

<style scoped></style>
