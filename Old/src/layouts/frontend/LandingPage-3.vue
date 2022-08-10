<template>
  <div>
    <HeaderStyle :logo-img="logo"  className="main-header l-header-2 header-saas-dark" :styledLogo="styleLogo" :nav-item-list="navItems"/>
    
     
      <router-view />
     
    <FooterStyle3/>
    <Scrolltop/>
  </div>
</template>
<script>
import logo from "../../assets/images/logo-white.png"
import FooterStyle3 from "../../components/partials/frontend/FooterStyle/FooterStyle3";
import HeaderStyle from "../../components/partials/frontend/HeaderStyle/DefaultStyle";
import Scrolltop from '../../components/frontend/ScrollTop'
import {core} from '../../config/pluginInit'
export default {
  name: 'DefaultLayout',
  components: {
    FooterStyle3,
    HeaderStyle,Scrolltop
  },
  mounted(){
    document.body.classList='landing-saas-dark main-bg'
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
        { href: '#iq-service', title: 'Service' },
        { href: '#iq-about', title: 'About Us' },
        { href: '#iq-feature', title: 'Feature' },
        { href: '#iq-team', title: 'Team' },
        { href: '#iq-testimonial', title: 'Testimonial' },
        { href: '#iq-pricing', title: 'Pricing' },
        { href: '#iq-blog', title: 'Blog' },
        { href: '#iq-contact', title: 'Contact Us' }
      ],
      footerText:
        'It is a long established fact that a reader will be distracted by the readable content.',
    }
  }
}
</script>
