

  



<template>
<div class="row">
    <vue-navigation-bar :options="navbarOptions" @vnb-item-clicked="openUrl" />
</div>
</template>

<script>
import vueNavigationBar from 'vue-navigation-bar'
import brandImage from '../../../../assets/images/logotext.png'

export default {
    name: 'DefaultStyle',
    components: {
    vueNavigationBar
    },
    methods: {
      openUrl(url){
        console.log('url is',url);
        if(url=="Documentation") {
          window.open('/html/index.html', '_blank')
        }
        else if(url=="Tutorials") {
          window.open('/notebook/User_Guide.html', '_blank')
        }
        else if(url=="Sign In") {
          window.open('/sign-in', '_blank')
        }
        else if(url=="Sign Up") {
          window.open('/sign-up', '_blank')
        }
        else {
          console.log('doumeijin');
        }
        // window.open('/notebook/User_Guide.html', '_blank')
      }
    },
    data() {
      return {
        navbarOptions: {
          elementId: "main-navbar",
          isUsingVueRouter: true,
          mobileBreakpoint: 992,
          brandImagePath: "./",
          brandImage,
          brandImageAltText: "brand-image",
          collapseButtonOpenColor: "#661c23",
          collapseButtonCloseColor: "#661c23",
          showBrandImageInMobilePopup: true,
          ariaLabelMainNav: "Main Navigation",
          tooltipAnimationType: "shift-away",
          tooltipPlacement: "bottom",
          menuOptionsLeft: [
            // {
            //   type: "link",
            //   text: "Why Dunder Mifflin",
            //   arrowColor: "#659CC8",
            //   subMenuOptions: [
            //     {
            //       isLinkAction: true,
            //       type: "link",
            //       text: "About",
            //       subText: "Stupid corporate wet blankets. Like booze ever killed anyone.",
            //       path: { name: "about" },
            //       iconLeft: '<i class="fa fa-star fa-fw"></i>'
            //     },
            //     {
            //       type: "hr",
            //     },
            //     {
            //       type: "link",
            //       text: "Locations",
            //       subText: "You're a presentation tool!",
            //       path: { name: "locations" },
            //       arrowColor: "#659CC8",
            //     },
            //     {
            //       type: "hr",
            //     },
            //     {
            //       type: "link",
            //       text: "Blog",
            //       subText: "I enjoy having breakfast in bed. I like waking up to the smell of bacon. Sue me.",
            //       path: { name: "blog" }
            //     },
            //   ]
            // },
            // {
            //   type: "link",
            //   text: "Contact",
            //   subMenuOptions: [
            //     {
            //       type: "link",
            //       text: "Customer Service",
            //       path: { name: "customer-service" },
            //     },
            //     {
            //       type: "link",
            //       text: "Accounting",
            //       path: { name: "accounting" },
            //     },
            //     {
            //       type: "hr",
            //     },
            //     {
            //       type: "link",
            //       text: "Reception",
            //       path: "products",
            //       iconLeft: '<svg id="i-telephone" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"> <path d="M3 12 C3 5 10 5 16 5 22 5 29 5 29 12 29 20 22 11 22 11 L10 11 C10 11 3 20 3 12 Z M11 14 C11 14 6 19 6 28 L26 28 C26 19 21 14 21 14 L11 14 Z" /> <circle cx="16" cy="21" r="4" /> </svg>',
            //     },
            //   ]
            // },
            // {
            //   type: "link",
            //   text: "Pricing",
            //   path: "about",
            //   iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
            //   class: "right"
            // },
          ],
          menuOptionsRight: [
            {
              type: "link",
              text: "Home",
              path: "/",
              iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
            },
            {
              type: "link",
              text: "Products",
              path: "/products",
              iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
            },
            {
              type: "link",
              text: "Resources",
              subMenuOptions: [
                {
                  type: "link",
                  text: "Documentation",
                  path: "",
                },
                {
                  type: "hr",
                },
                {
                  type: "link",
                  text: "Tutorials",
                  path: "",
                },
                {
                  type: "hr",
                },
                {
                  type: "link",
                  text: "Use Cases",
                  path: "/usecases",
                },
              ]
            },
            {
              type: "link",
              text: "About",
              path: "/about",
              iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
            },
            {
              type: "link",
              text: "Contact",
              path: "/contact",
              iconRight: '<i class="fa fa-long-arrow-right fa-fw"></i>',
            },
            {
              type: "button",
              text: "Sign Up",
              path: "",
              class: "button-red"
            },
            {
              type: "button",
              text: "Sign In",
              path: "",
              // iconRight: '<svg id="i-arrow-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"> <path d="M22 6 L30 16 22 26 M30 16 L2 16" /> </svg>'
            }
          ]
        }
      }
    }
    
}
</script>

<style lang="css">

.row{
  margin: 0px 0px;
  /* font-size:100px !important */
  /* height: 100px */
}
.vnb__menu-options__option__link{
  font-size: 1.2rem;
}
.vnb__menu-options__option__button{
  font-size: 1.2rem
}

  /* .vnb .button-red {
  background: #ff3b30;
}

.vnb .button-red:hover {
  background: #fc0d00;
} */

  .vnb__brand-image-wrapper__link__image{
    max-height: 60px;
    margin-left: 80px
  }
</style>