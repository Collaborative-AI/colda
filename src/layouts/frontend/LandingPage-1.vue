<template>
  <div>
    <HeaderStyle :logo-img="logo"  className="main-header l-header-2 header-saas" :styledLogo="styleLogo" :nav-item-list="navItems"/>
    <div class="wrapper">
      <router-view />
    </div>
    <FooterStyle1
       buttonClass="btn-purple"
      :footer-logo="logo"
      :footer-text="footerText"
      :footer-title="footerTitle"
      :footer-description="footerDescription"
      text-class="text-white"
    >
      <template v-slot:menu>
        <ul>
          <li>
            <a class="text-white" href="javascript:void(0)">About Us</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Theme</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Features</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Pricing</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Blog</a>
          </li>
        </ul>
      </template>
      <template v-slot:aboutus>
        <ul>
          <li>
            <a class="text-white" href="javascript:void(0)">About Sofbox</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Roadmap</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">How it Work</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">Team</a>
          </li>
          <li>
            <a class="text-white" href="javascript:void(0)">News</a>
          </li>
        </ul>
      </template>
      <template v-slot:testimonial>
        <div>
          <VTwoTestimonialCarousel :testimonial-list="List" />
        </div>
      </template>
    </FooterStyle1>
    <Scrolltop/>
  </div>
</template>
<script>
import logo from "../../assets/images/logo-white.png"
import FooterStyle1 from "../../components/partials/frontend/FooterStyle/FooterStyle1";
import HeaderStyle from "../../components/partials/frontend/HeaderStyle/DefaultStyle";
import VTwoTestimonialCarousel from '../../components/frontend/carsol/VTwoTestimonialCarousel'
import Scrolltop from '../../components/frontend/ScrollTop'
import {core} from '../../config/pluginInit'
export default {
  name: 'DefaultLayout',
  components: {
    FooterStyle1,
    HeaderStyle,
    VTwoTestimonialCarousel,
    Scrolltop
  },
   mounted(){
    document.body.classList='landing-saas'
    core.onScroll()
  },
  
  data(){
    return{
      styleLogo:false,
      logo:logo,
      navItems: [
        {
          href: '#iq-home',
          title: 'Home',
          _is_active: true
        },
        { href: '#iq-about', title: 'About Us' },
        { href: '#iq-feature', title: 'Feature' },
        { href: '#iq-blog', title: 'Blog' },
        { href: '#iq-contact', title: 'Contact Us' }
      ],
      footerText:
        'It is a long established fact that a reader will be distracted by the readable content.',
      footerTitle: 'Ready to get started?',
      footerDescription:
        'It is a long established fact that a page when looking at its layout.',
      List: [
        {
          name: 'Walhan Bobe',
          design: 'CEO Prox',
          image: require('../../assets/images/landing-page/landing-1/215.jpeg'),
          description:
            'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium incididunt ut labore et dolore Sed omnis iste ut perspiciatis.'
        },
        {
          name: 'Walhan Bobe',
          design: 'CEO Prox',
          image: require('../../assets/images/landing-page/landing-1/216.jpeg'),
          description:
            'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium incididunt ut labore et dolore Sed omnis iste ut perspiciatis.'
        },
        {
          name: 'Walhan Bobe',
          design: 'CEO Prox',
          image: require('../../assets/images/landing-page/landing-1/217.jpeg'),
          description:
            'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium incididunt ut labore et dolore Sed omnis iste ut perspiciatis.'
        }
      ]
    }
  }
  
}
</script>
