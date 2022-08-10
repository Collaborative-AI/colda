<template>
  <footer id="iq-contact" :class="footerClass">
    <img src="../../../../assets/images/landing-page/landing-4/footer-pattern.png" class="img-fluid footer-pattern" alt="#">
    <div class="footer-topbar">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 ">
            <div class="widget mb-0">
              <div class="textwidget">
                <div class="row ">
                  <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
                    <ul class="info-share social-icone d-inline list-inline">
                      <li class="list-inline-item">
                        <a href="#"><i class="fab fa-facebook-f" /></a>
                      </li>
                      <li class="list-inline-item">
                        <a href="#"><i class="fab fa-twitter" /></a>
                      </li>
                      <li class="list-inline-item">
                        <a href="#"><i class="fab fa-google-plus-g" /></a>
                      </li>
                      <li class="list-inline-item">
                        <a href="#"><i class="fab fa-instagram" /></a>
                      </li>
                    </ul>
                  </div>
                  <div class="col-lg-4 col-md-12  mb-4 mb-lg-0 text-lg-center text-lg-left align-self-center">
                    <h4 class="text-white subscribe-title">
                      Subscribe for Newsletter
                    </h4>
                  </div>
                  <div class="col-lg-4   text-center text-lg-right">
                    <form class="mc4wp-form mc4wp-form-517" method="post">
                      <div class="mc4wp-form-fields">
                        <input type="email" name="EMAIL" placeholder="Your email address" required="">
                        <input type="submit" value="Subscribe">
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <slot name="footerContent" />
  </footer>
</template>
<script>
export default {
  name: 'FooterMain',
  props: {
    footerClass:
    {
      type: String,
      required: true
    }
  }
}
</script>
