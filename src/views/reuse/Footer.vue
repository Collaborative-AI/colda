<template>
<div>
        <!-- <div class="bottom section-padding" style="background-color: white"> -->
        <div class="bottom section-padding">
      <div class="container" >
        <div class="row">
          <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6">
            <div class="bottom-logo">
              <img class="pb-3" src="../../assets/images/logo1.png" height="68px" alt="" />

              <!-- <p>The Perfect Application For Beginners Or Professionals</p> -->
            </div>
          </div>
          <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Important Links</h4>
              <ul>
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/products">Products</router-link></li>
                <li><router-link to="/about">About</router-link></li>
                <li><router-link to="/contact">Contact</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Resources</h4>
              <ul>
                <li><router-link to="#">Documentation</router-link></li>
                <li><router-link to="#">Tutorials</router-link></li>
                <li><router-link to="#">Use Cases</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Contact</h4>
              <div class="row">
                <!-- <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6"> -->
                  <ul>
                    <li><router-link to="#"><span>Phone <br> <a href="tel:+1 4048343911">+1 4048343911</a></span></router-link></li>
                    <li><router-link to="#"><span>Email <br> <a href="mailto:support@synspot-ai.com">support@synspot-ai.com</a></span></router-link></li>
                    <li><router-link to="#"><span>Address</span> <br> <span>366 Ford Hall 224, Church Street, Minneapolis, MN 55455</span></router-link></li>
                  </ul>
                <!-- </div> -->
                <!-- <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                  <ul>
                    <li><router-link to="#">BTC to USDT</router-link></li>
                    <li><router-link to="#">LTC to BTC</router-link></li>
                    <li><router-link to="#">XMR to BTC</router-link></li>
                    <li><router-link to="#">ETC to DASH</router-link></li>
                  </ul>
                </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="container">
        <div class="row">
          <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
            <div class="copyright">
              <p>
                © Copyright {{ new Date().getFullYear() }}
                <a href="#">Synspot</a> I All Rights Reserved
              </p>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
            <div class="footer-social">
              <ul>
                <li>
                  <a href="#"><i class="fa fa-facebook"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-twitter"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-linkedin"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-youtube"></i></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

</div>
</template>

<script>

export default {
  name: 'Footer',
  data () {
    return {
      msg: 'this is profile page'
    }
  },
  components: {
    
  },
  methods: {

  }

}

</script>

<style scoped>

</style>
