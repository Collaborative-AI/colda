<template>
  <div>
    <HeaderStyle :logo-img="logo"  className="main-header l-header-2 header-saas" :styledLogo="styleLogo" :nav-item-list="navItems"/>
  
      
      <router-view />
      
    <FooterStyle2 :footerText="footerText" :footerLogo="logocolor">
      <template v-slot:menu>
        <ul>
          <li><a href="javascript:void(0)">About Us</a></li>
          <li><a href="javascript:void(0)">Theme</a></li>
          <li><a href="javascript:void(0)">Features</a></li>
          <li><a href="javascript:void(0)">Pricing</a></li>
          <li><a href="javascript:void(0)">Blog</a></li>
        </ul>
      </template>
      <template v-slot:aboutus>
        <ul>
          <li><a href="javascript:void(0)">About Sofbox</a></li>
          <li><a href="javascript:void(0)">Roadmap</a></li>
          <li><a href="javascript:void(0)">How it Work</a></li>
          <li><a href="javascript:void(0)">Team</a></li>
          <li><a href="javascript:void(0)">News</a></li>
        </ul>
      </template>
      <template v-slot:quicklink>
        <ul>
          <li><a href="javascript:void(0)">About Us</a></li>
          <li><a href="javascript:void(0)">Theme</a></li>
          <li><a href="javascript:void(0)">Features</a></li>
          <li><a href="javascript:void(0)">Pricing</a></li>
          <li><a href="javascript:void(0)">Blog</a></li>
        </ul>
      </template>
    </FooterStyle2>
     <Scrolltop/>
  </div>
</template>
<script>
import logocolor from "../../assets/images/logo.png"
import logo from "../../assets/images/logo-white.png"
import FooterStyle2 from "../../components/partials/frontend/FooterStyle/FooterStyle2";
import HeaderStyle from "../../components/partials/frontend/HeaderStyle/DefaultStyle";
import Scrolltop from '../../components/frontend/ScrollTop'
import {core} from '../../config/pluginInit'
export default {
  name: 'DefaultLayout',
  components: {
    FooterStyle2,
    HeaderStyle,
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
      logocolor:logocolor,
      navItems: [
        {
          href: '#iq-home',
          title: 'Home',
          _is_active: true
        },
        { href: '#iq-about', title: 'About us' },
        { href: '#iq-feature', title: 'Features' },
        { href: '#iq-pricing', title: 'Pricing' },
        { href: '#iq-testimonial', title: 'Testimonial' },
        { href: '#iq-blog', title: 'Blog' },
      ],
      footerText:
        'It is a long established fact that a reader will be distracted by the readable content.',
    }
  }
}
</script>
