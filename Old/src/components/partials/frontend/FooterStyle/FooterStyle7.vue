<template>
  <FooterMain2 footer-class="footer2">
    <div slot="footerContent">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-12 pr-lg-5">
            <FooterLogo
              :section-image="navLogo"
              section-text="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
            />
          </div>
          <div class="col-lg-2 col-md-6">
            <FooterLinks :content="footerHome" title="Useful links" />
          </div>
          <div class="col-lg-3 col-md-6 col-sm-12">
                    <div class="widget">
                        <h4 class="mb-4 footer-title">Latest News</h4>
                        <div class="iq-blog-content bdr-bottom">
                            <div class="iq-blog-meta">
                                <ul class="iq-postdate">
                                    <li class="list-inline-item">
                                        <i class="far fa-calendar-alt mr-1"></i> <a href="#">1 Feb 2020</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="blog-title">
                                <a href="#">
                                    <h5 class="mb-3">Fully dedicated to finding.</h5>
                                </a>
                            </div>
                        </div>
                        <div class="iq-blog-content">
                            <div class="iq-blog-meta">
                                <ul class="iq-postdate">
                                    <li class="list-inline-item">
                                        <i class="far fa-calendar-alt mr-1"></i> <a href="#">1 Feb 2020</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="blog-title">
                                <a href="#">
                                    <h5 class="mb-3">Fully dedicated to finding.</h5>
                                </a>
                            </div>
                        </div>
                    </div>
          </div>
          <div class="col-lg-3 col-md-6">
            <FooterAddress
              :address-content="footerText"
              address-title="Headquarter"
              class="iq-contact"
            />
          </div>
        </div>
        <div class="copyright-footer pb-3 pt-3">
            <div class="row">
                <div class="col-lg-6 col-md-6 mb-2 mb-lg-0">
                    <span class="copyright">Copyright 2020 ©iqonic.design</span>
                </div>
                <div class="col-lg-6 col-md-6">
                    <div class="social-icone">
                        <ul>
                            <li class="d-inline"><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                            <li class="d-inline"><a href="#"><i class="fab fa-google"></i></a></li>
                            <li class="d-inline"><a href="#"><i class="fab fa-github"></i></a></li>
                            <li class="d-inline"><a href="#"><i class="fab fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  </FooterMain2>
</template>
<script>
import FooterMain2 from '../FooterComponentss/FooterMain2'
import FooterLogo from '../FooterComponentss/FooterLogo'
import FooterLinks from '../FooterComponentss/FooterLinks'
import FooterAddress from '../FooterComponentss/FooterAddress'
import logoImg from '../../../../assets/images/logo.png'

export default {
  name: 'Footerstyle7',
  components: { FooterLogo, FooterMain2, FooterLinks, FooterAddress },
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
