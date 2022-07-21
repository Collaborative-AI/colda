<template>
  <div>
    <!-- <div class="top-bar-software position-relative">
        <div class="container-fluid">
            <div class="row">
                <div class="col-xl-8 col-lg-8 col-md-8 ">
                    <div class="number-info">
                        <ul class="list-inline">
                            <li class="list-inline-item"><a href="tel:+0123456789">
                                    <i class="fa fa-phone mr-2"></i>+0123456789</a>
                            </li>
                            <li class="list-inline-item"><a href="mailto:support@themes.com">
                                    <i class="fa fa-envelope mr-2"></i>support@themes.com</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-xl-4 col-lg-4  col-md-4 pr-0">
                    <div class="social-icone">
                        <ul class="list-inline">
                            <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
                            <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                            <li><a href="#"><i class="fab fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div> -->
    <HeaderStyle :logo-img="logo"  className="main-header header-software" :styledLogo="styleLogo" :nav-item-list="navItems"/>
  
      <router-view></router-view>
      
    <FooterStyle6>
      <template v-slot:icon>
            <ul class="info-share d-inline list-inline">
              <li class="list-inline-item"><a href="#"><i class="fab fa-facebook-f"></i></a></li>
              <li class="list-inline-item"><a href="#"><i class="fab fa-twitter"></i></a></li>
              <li class="list-inline-item"><a href="#"><i class="fab fa-instagram"></i></a></li>
            </ul>
          </template>
      <!-- <template v-slot:footer-innertop>
        <div class="row algin-self-center footer_top_block">
          <div class="col-md-6">
              <h4 class="footer-title">Subscribe for Newsletter haha</h4>
          </div>
          <div class="col-md-6">
              <div class="mc4wp-form-fields">
                  <input type="email" name="EMAIL" placeholder="Your Email" required="">
                  <input type="submit" value="Sign up">
              </div>
          </div>
      </div>
      </template> -->
    </FooterStyle6>
    <Scrolltop />
  </div>
</template>
<script>
import logo from "../../assets/images/logo.png"
import FooterStyle6 from "../../components/partials/frontend/FooterStyle/FooterStyle6";
import HeaderStyle from "../../components/partials/frontend/HeaderStyle/DefaultStyle";
import Scrolltop from '../../components/frontend/ScrollTop'
import {core} from '../../config/pluginInit'
export default {
  name: 'DefaultLayout',
  components: {
    FooterStyle6,
    HeaderStyle,
     Scrolltop
  },
  mounted(){
    document.body.classList='landing-analytics ', core.onScroll()},
  data(){
    return{
      styleLogo:false,
      logo:logo,
      navItems: [
        // {
        //   href: '#iq-home',
        //   title: 'Home',
        //   _is_active: true
        // },
        // { href: '#iq-about', title: 'About Us' },
        // { href: '#iq-service', title: 'Services' },
        // { href: '#iq-process', title: 'Process' },
        // { href: '#iq-testimonial', title: 'Testimonial' },
        // { href: '#iq-blog', title: 'Blog' },
        // { href: '#iq-contact', title: 'Contact Us' }
        { href: '/', title: 'Home' },
        { href: '/products', title: 'Products' },
        // { href: '/', title: 'Resourses', children: [
        //     { href: '/documentation', title: 'Documentation' },
        //     { href: '/tutorials', title: 'Tutorials' },
        // ]
        //     },
        { href: '/usecases', title: 'Usecases' },
        { href: '/about', title: 'About' },
        { href: '/contact', title: 'Contact' },
      ],
      footerText:
        'It is a long established fact that a reader will be distracted by the readable content.',
    }
  }
}
</script>
