<template>
  <section class="iq-section-space bg-primary">
    <div class="container">
      <div class="row align-items-center  ">
        <div class="col-lg-6 col-md-6 col-sm-12 wow fadeInUp " data-wow-delay=".3s">
          <form method="post" novalidate="novalidate">
          <div class="predict-form  consultab-contact contact-form">
              <div>
                  <h4 class="title mb-4 text-center">Talk With Our Expert</h4>
              </div>
              <div class=""> <input type="text" name="your-name" class="form-control text " placeholder="Your Name"> </div>
              <div class=""> <input type="text" name="your-email" class="form-control text " placeholder="Your Email"> </div>
              <div class=""> <textarea name="your-message" cols="40" rows="5" class="form-control textarea " placeholder="Your Message"></textarea> </div>
              <div> <button id="submit-4" name="submit" type="submit" value="Send" class="landing-button btn-primary d-block w-100">Send Message</button> </div>
          </div>
          </form>
          </div>
          <div class="col-lg-6 col-md-6 col-sm-12 mt-4 mt-lg-0 wow fadeInUp " data-wow-delay=".6s">
            <div class="contact-box d-flex  text- text-white ">
                <i aria-hidden="true" class="fa fa-phone"></i> 
                <div class="service-detail">
                  <h2 class="mb-2  text-white " >Phone Support</h2>
                  <ul class="list-inline mb-0">
                      <li><a href="tel:+0123456789"> +0123456789</a> </li>
                      <li><a href="tel:+0123456789">+0123456789</a></li>
                  </ul>
                </div>
            </div>
            <div class="contact-box d-flex  text- text-white ">
                <i aria-hidden="true" class="fa fa-map-marker"  ></i> 
                <div class="service-detail">
                  <h2 class="mb-2  text-white">Email us</h2>
                  <ul class="list-inline mb-0">
                      <li><a href="mailto:support@iqnonicthemes.com">support@themes.com</a>  </li>
                      <li><a href="mailto:support@iqnonicthemes.com"> support@themes.com</a>  </li>
                  </ul>
                </div>
            </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name:'ContactUs'
}
</script>