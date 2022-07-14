<template>
  <div id="main-wrapper" class="show">
      <navbar></navbar>
    

    

    <div class="trade-app section-padding">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-6">
            <div class="section-title text-center">
              <h2>Our Products</h2>
              <p>
                All of our products are ready to go, easy to use and offer great
                value to any kind of business
              </p>
            </div>
          </div>
        </div>
        <div class="row">
          <!-- <div class="col-xl-6 col-lg-6 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-mobile"></i></span>
                <h4 class="card-title">Mobile</h4>
                <p>
                  All the power of Tradio's cryptocurrency exchange, in the palm
                  of your hand. Download the Tradio mobile crypto trading app
                  today
                </p>

                <a href="#"> Know More <i class="la la-arrow-right"></i> </a>
              </div>
            </div>
          </div> -->
          <div class="col-xl-6 col-lg-6 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-connectdevelop"></i></span>
                <h4 class="card-title">API</h4>
                <p>
                  The Synspot API is designed to provide an easy and efficient
                  way to train your model our platform.
                </p>

                <a href="html/index.html"> Know More <i class="la la-arrow-right"></i> </a>
              </div>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-desktop"></i></span>
                <h4 class="card-title">Software</h4>
                <p>
                  Applications for your Windows or MacOS device.
                </p>
                <div>
                    <a href="/file/SynSpot Setup 0.0.2.exe" download class="btn btn-primary text-white" style="float:left; margin: 0px auto">Windows</a>
                    <!-- <router-link to="/pricing" class="default-btn">
                        Download 
                    </router-link> -->
                </div>
                <div>
                    <a href="/file/SynSpot-0.0.2.dmg" download class="btn btn-primary text-white" style="float:right; margin: 0px auto">MacOS</a>
                    <!-- <router-link to="/pricing" class="default-btn">
                        Download
                    </router-link> -->
                </div>

                <!-- <a href="#"> Know More <i class="la la-arrow-right"></i> </a> -->
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>

    <Footer></Footer>
    

    


  </div>
</template>


<script>
// import BtcChart from "../components/Tradio/Charts/BtcChart.vue";
// import CurrencyForm from "../components/Tradio/From/CurrencyForm.vue";
// import Slider from "../components/Tradio/Slider.vue";
import Navbar from './reuse/Navbar.vue'
import Footer from './reuse/Footer.vue'


export default {
  name: 'Products',
  components: { 
    // BtcChart,
    // Slider, 
    // CurrencyForm
    Navbar,
    Footer
     },
  data() {
    return {
      active: 1,
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {

  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
