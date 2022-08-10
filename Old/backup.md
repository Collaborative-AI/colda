{
  "name": "prox-vue",
  "version": "2.0.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
  "dependencies": {
    "@amcharts/amcharts4": "^4.10.11",
    "@amcharts/amcharts4-geodata": "^4.1.19",
    "@fullcalendar/core": "^4.3.1",
    "@fullcalendar/daygrid": "^4.3.0",
    "@fullcalendar/interaction": "^4.3.0",
    "@fullcalendar/timegrid": "^4.3.0",
    "@fullcalendar/vue": "^4.3.1",
    "apexcharts": "^3.22.2",
    "axios": "^0.27.2",
    "bootstrap-vue": "^2.17.3",
    "core-js": "^3.6.5",
    "counterup2": "^1.0.4",
    "datatables": "^1.10.18",
    "datatables.net": "^1.10.23",
    "datatables.net-dt": "^1.10.21",
    "highcharts": "^8.2.2",
    "highcharts-vue": "^1.3.5",
    "ionicons": "^5.2.3",
    "isotope-layout": "^3.0.6",
    "jquery": "^3.5.1",
    "jvectormap-content": "^0.1.0",
    "jvectormap-next": "^3.1.1",
    "line-awesome": "^1.3.0",
    "magnific-popup": "^1.1.0",
    "mapbox-gl": "^1.13.0",
    "mapbox-gl-vue": "^2.0.4",
    "masonry-layout": "^4.2.2",
    "owl.carousel": "^2.3.4",
    "ramda": "^0.27.1",
    "remixicon": "^2.5.0",
    "select2": "~4.0",
    "smooth-scrollbar": "^8.5.2",
    "swiper": "^6.4.5",
    "vue": "^2.6.11",
    "vue-flatpickr-component": "^8.1.5",
    "vue-morris": "^1.1.0",
    "vue-router": "^3.2.0",
    "vue-slick": "^1.1.15",
    "vue2-editor": "^2.10.2",
    "vuelidate": "^0.7.6",
    "vuex": "^3.4.0",
    "waypoints": "^4.0.1"
  },
  "devDependencies": {
    "@fullcalendar/list": "^4.3.0",
    "@babel/polyfill": "^7.10.4",
    "@vue/cli-plugin-babel": "~4.5.0",
    "@vue/cli-plugin-eslint": "~4.5.0",
    "@vue/cli-plugin-pwa": "~4.5.0",
    "@vue/cli-plugin-router": "~4.5.0",
    "@vue/cli-plugin-vuex": "~4.5.0",
    "@vue/cli-service": "~4.5.0",
    "@vue/eslint-config-standard": "^5.1.2",
    "babel-eslint": "^10.1.0",
    "bootstrap": "^5.0.0-alpha1",
    "css-loader": "^5.0.1",
    "eslint": "^6.7.2",
    "eslint-plugin-import": "^2.20.2",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-promise": "^4.2.1",
    "eslint-plugin-standard": "^4.0.0",
    "eslint-plugin-vue": "^6.2.2",
    "less": "^3.12.2",
    "less-loader": "^5.0.0",
    "lint-staged": "^9.5.0",
    "mutationobserver-shim": "^0.3.7",
    "node-sass": "^4.12.0",
    "popper.js": "^1.16.0",
    "portal-vue": "^2.1.6",
    "sass": "^1.26.10",
    "sass-loader": "^8.0.2",
    "stylus": "^0.54.8",
    "stylus-loader": "^3.0.2",
    "vue-cli-plugin-bootstrap-vue": "~0.6.0",
    "vue-loader": "^15.9.3",
    "vue-template-compiler": "^2.6.11"
  }
}


    <!-- <link rel="icon" href="<%= BASE_URL %>favicon.ico"> -->
    <!-- <link rel="icon" type="image/png" sizes="16x16" href="<%= BASE_URL %>favicon1.png" /> -->
    
    <!-- <title><%= htmlWebpackPlugin.options.title %></title> -->






<template>
  <header id="main-header" :class="className">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <!-- <nav class="navbar navbar-expand-lg navbar-light">
            <router-link class="navbar-brand" to="/landingpage-1">
              <img :id="styledLogo ? 'logo_img' : ''" :src=" logoImg " class="img-fluid logo" alt="img">
            </router-link>
            <button
              class="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span id="menu-btn" class="menu-btn d-inline-block" @click="toggleClass">
                <span class="line" />
                <span class="line" />
                <span class="line" />
              </span>
              <span class="ion-navicon" />
            </button>
            <div id="navbarSupportedContent" class="collapse navbar-collapse">
              <ul class="navbar-nav mr-auto w-100 justify-content-end">
                <template v-for="(option,index) in navItemList">
                  <li v-if="option.children" :key="index" class="nav-item dropdown">
                    <a
                      :id="'navbarDropdown' + index "
                      class="nav-link dropdown-toggle"
                      href="#"
                      role="button"
                      data-toggle="dropdown"
                      aria-haspopup="true"
                      aria-expanded="false"
                    >
                      {{ option.title }}
                    </a>
                    <div class="dropdown-menu" :aria-labelledby="'navbarDropdown' + index">
                      <router-link class="dropdown-item" v-for="(child, index1) in option.children" :key="index1" :to="child.href">
                        {{ child.title }}
                      </router-link>
                    </div>
                  </li>
                    <li v-if="option.children" :key="index" class="nav-item dropdown">
                      
                        <a href="#" class="nav-link" ><p>Resources</p></a>
                        <div class="dropdown-content">
                            <a target="_blank" href="html/index.html" >Documentation</a>
                            <a target="_blank" href="notebook/User_Guide.html">Tutorials</a>
                            <router-link  to="/usecases">
                                Use Cases
                            </router-link>
                        </div>
                      
                    </li>
                  <li v-else :key="index" class="nav-item">
                    <a v-if="!option.redirect" :class="`nav-link ${option._is_active !== undefined && option._is_active ? 'active' : '' }`" :href="option.href" @click="jumpTo(option.href)">
                      {{ option.title }}
                    </a>
                    <router-link v-else :to="option.href" class="nav-link">
                      {{ option.title }}
                    </router-link>
                   
                    <router-link :to="option.href" class="nav-link">
                      {{ option.title }}
                    </router-link>
                  </li>
                </template>
              </ul>
            </div>
          </nav> -->
          <b-navbar toggleable="lg" type="light">
              <!-- <a target="_blank" href="html/index.html" style="text-decoration: none">Documentation</a>
              <a target="_blank" href="notebook/User_Guide.html" style="text-decoration: none">Tutorials</a> -->


    <b-navbar-brand to="/">
      <img class="logo" src="../../../../assets/images/logo1.png" alt=""/>
      <h2 style="color:black; font-family: Helvetica; margin:5px 1px; float:left ">Synspot</h2>
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse" style="border: 1px solid black"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav style="border: 1px solid red">
      <b-navbar-nav class="navbar" style="border: 1px solid yellow; width:80%">
        <b-nav-item class="nav-item" to="/" style="border: 1px solid green; width:15%">Home</b-nav-item>
        <b-nav-item class="nav-item" to="/products" style="border: 1px solid green; width:15%">Products</b-nav-item>
        

        <div class="nav-item dropdown" style="border: 1px solid green; width:15%; height:32px">
                      
                        <a href="#" class="nav-link" ><p style="color:black">Resources</p></a>
                        <div class="dropdown-content">
                            <a target="_blank" href="html/index.html" >Documentation</a>
                            <a target="_blank" href="notebook/User_Guide.html">Tutorials</a>
                            <router-link  to="/usecases">
                                Use Cases
                            </router-link>
                        </div>
                      
                    </div>
        <!-- <b-nav-item-dropdown text="Resources">
          <b-dropdown-item target="_blank" href="html/index.html">Documentation</b-dropdown-item>
          <b-dropdown-item target="_blank" href="notebook/User_Guide.html">Tutorials</b-dropdown-item>
          <b-dropdown-item><a target="_blank" href="html/index.html" >Documentation</a></b-dropdown-item>
          <b-dropdown-item><a target="_blank" href="notebook/User_Guide.html">Tutorials</a></b-dropdown-item>
          <a target="_blank" href="html/index.html" style="text-decoration: none">Documentation</a>
          <a target="_blank" href="notebook/User_Guide.html" style="text-decoration: none">Tutorials</a>
          <b-dropdown-item to="/usecases">Use Cases</b-dropdown-item>
        </b-nav-item-dropdown> -->
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <b-nav-item class="nav-item" to="/about" style="border: 1px solid green; width:15%">About</b-nav-item>
        <b-nav-item class="nav-item" to="/contact" style="border: 1px solid green; width:15%">Contact</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
const $ = require('jquery')
export default {
  name: 'DefaultStyle',
  props: {
    className: { type: String, default: '' },
    logoImg: { type: String, default: '' },
    logoWhite: { type: String, default: '' },
    navItemList: { type: Array, default: () => [] },
    styledLogo: { type: Boolean, default: false }
  },
  created () {
    this.$root.$on('bv::scrollspy::activate', this.onActivate)
  },
  methods: {
    onActivate () {
    },
    jumpTo (href) {
      $('html, body').stop().animate({
        scrollTop: $(href).offset().top
      }, 1500)
    },

    toggleClass () {
      $('.menu-btn').click(function () {
        $(this).toggleClass('is-active')
      })
    }
  }
}
</script>

<style scoped>
.logo {
  object-fit: contain;
  /* width: 10%; */
  height: 50px;
  float:left
}

.dropbtn {
  /* background-color: #04AA6D; */
  color: rgb(1, 1, 1);
  padding: 16px;
  font-size: 16px;
  border: none;
}

.navbar{
  /* position: relative;
  top: 0px; */
  /* margin: 0px auto; */
  /* padding:0 */
}

.nav-item{
  display: block;
  margin: 0;
  padding:0
  /* width: 15%; */
  /* margin: 0px 50px */
}

.dropdown {
  position: relative;
  top: 1px;
  display: inline-block;

}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

/* .dropdown:hover .dropbtn {background-color: #3e8e41;} */



</style>