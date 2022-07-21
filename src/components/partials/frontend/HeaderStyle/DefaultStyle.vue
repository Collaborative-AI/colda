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
      <h2 style="color:black; font-family: Helvetica; margin:10px; float:left ">Synspot</h2>
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/products">Products</b-nav-item>
        

        <span class="nav-item dropdown">
                      
                        <a href="#" class="nav-link" ><p style="color:black">Resources</p></a>
                        <div class="dropdown-content">
                            <a target="_blank" href="html/index.html" >Documentation</a>
                            <a target="_blank" href="notebook/User_Guide.html">Tutorials</a>
                            <router-link  to="/usecases">
                                Use Cases
                            </router-link>
                        </div>
                      
                    </span>
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
        <b-nav-item to="/about">About</b-nav-item>
        <b-nav-item to="/contact">Contact</b-nav-item>
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

.dropdown {
  position: relative;
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