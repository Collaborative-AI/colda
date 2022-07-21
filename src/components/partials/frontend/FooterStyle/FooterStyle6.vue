<template>
  <FooterMain class="footer-analytics iq-bg-dark iq-over-dark-90">
    <div slot="footerContent" class="footer-top">
      <slot name="footer-innertop"/>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-6">
          <FooterLogo
            :section-image="navLogo"
            section-text="Synspot for decentralized organizations learning AI models without sharing data, models, or objectives."
          >
          <template v-slot:icons>
            <slot name="icon"/>
          </template>
          </FooterLogo>
        </div>
        <div class="col-lg-2 col-md-6 col-sm-6 mt-4 mt-lg-0 mt-md-0">
          <FooterLinks :content="footerLinks" title="Important Links"/>
        </div>
        <div class="col-lg-2 col-md-6 col-sm-6 mt-lg-0 mt-4">
          <!-- <FooterLinks :content="footerResources" title="Resources"/> -->
          <div>
            <h4 class="footer-title">Resources</h4>
            <div class="menu-footer-menu-container">
              <ul class="menu">
                <li class="menu-item">
                  <a target="_blank" href="html/index.html" >Documentation</a>       
                </li>
                <li class="menu-item">
                  <a target="_blank" href="notebook/User_Guide.html" >Tutorials</a>
                </li>
                <li class="menu-item">
                  <router-link to="/usecases">Use Cases</router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-6 mt-lg-0 mt-4">
          <FooterAddress :address-content="footerText" address-title="Contact Us" class="iq-contact" />
          
        </div>
      </div>    
    </div>
    <div slot="copyright" class="copyright-footer">
      <div class="pt-3 pb-3">
          <div class="row flex-row-reverse justify-content-between">
              <div class="col-lg-12 col-md-12 text-lg-center text-md-center text-center"> <span class="copyright">Copyright 2022 Synspot All Rights Reserved.</span>
              </div>
          </div>
      </div>
    </div>
  </FooterMain>
</template>
<script>
import FooterMain from '../FooterComponent/FooterMain'
import FooterAddress from '../FooterComponents/FooterAddress'
import FooterLogo from '../FooterComponents/FooterLogo'
import FooterLinks from '../FooterComponents/FooterLinks'
import logoImg from '../../../../assets/images/logo1.png'

export default {
  name: 'Footerstyle6',
  components: { FooterLogo, FooterLinks, FooterAddress, FooterMain },
  data () {
    return {
      navLogo: logoImg,
      footerText: [
        {
          icon: true,
          iconClass: 'fas fa-phone-alt',
          text: '+1 4048343911'
        },
        {
          icon: true,
          iconClass: 'fas fa-envelope',
          text: 'support@synspot-ai.com'
        },
        {
          icon: true,
          iconClass: 'fas fa-home',
          text: '1366 Ford Hall, 224 Church Street, Minneapolis, MN 55455'
        }
      ],
      footerLinks: [
        {
          href: '/',
          title: 'Home'
        },
        {
          href: '/products',
          title: 'Products'
        },
        {
          href: '/about',
          title: 'About'
        },
        {
          href: '/contact',
          title: 'Contact'
        },
      ],
      footerResources: [
        {
          href: 'html/index.html',
          title: 'Documentation'
        },
        {
          href: 'notebook/User_Guide.html',
          title: 'Tutorials'
        },
        {
          href: '/usecases',
          title: 'Use Cases'
        }
      ]
    }
  }
}
</script>

<style scoped></style>
