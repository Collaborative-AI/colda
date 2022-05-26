<template>
    <div class="footer-section pt-100 pb-70">
        <div class="container">
            <!-- <div class="subscribe-area">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-6">
                        <div class="subscribe-content">
                            <h2>Join Our Newsletter</h2>
                            <p>News letter dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                        </div>
                    </div>

                    <div class="col-lg-6 col-md-6">
                        <form class="newsletter-form">
                            <input type="email" class="input-newsletter" placeholder="Enter your email" name="EMAIL" required>
                            <button type="submit">
                                Subscribe Now
                            </button>
                        </form>
                    </div>
                </div>
            </div> -->

            <div class="row">
                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <div class="footer-heading">
                            <h3>Follow Us</h3>
                             <h3>On Social Media</h3>
                        </div>
                        
                        <!-- <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt</p> -->

                        <ul class="footer-social">
                            <li>
                                <a href="#" target="_blank">
                                    <i class="flaticon-facebook"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#" target="_blank">
                                    <i class="flaticon-twitter"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#" target="_blank">
                                    <i class="flaticon-pinterest"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#" target="_blank">
                                    <i class="flaticon-instagram"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <div class="footer-heading">
                            <h3>Important Links</h3>
                        </div>

                        <ul class="footer-quick-links">
                             <li>
                                <router-link to="/home-seven">Home</router-link>
                            </li>
                             <li>
                                <router-link to="/products">Products</router-link>
                            </li>
                            <li>
                                <router-link to="/about">About Us</router-link>
                            </li>
                             <li>
                                <router-link to="/contact">Contact</router-link>
                            </li>
                           
                            <!-- <li>
                                <router-link to="/services-one">Services</router-link>
                            </li>
                            <li>
                                <router-link to="/blog-one">Blog</router-link>
                            </li>
                            <li>
                                <router-link to="/contact">Contact</router-link>
                            </li> -->
                        </ul>
                    </div>    
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <div class="footer-heading">
                            <!-- <h3>Featured Service</h3> -->
                            <h3>Resources</h3>
                        </div>
                        <ul class="footer-quick-links">
                            <li>
                                <a href="html/index.html">Docs</a>
                            </li>
                            <li>
                                <a href="notebook/Sponsor_User_Guide.html">Tutorials</a>
                            </li>
                            <li>
                                <router-link to="/use-cases">Use Cases</router-link>
                            </li>
                            <!-- <li>
                                <a href="#">IT Management</a>
                            </li>
                            <li>
                                <a href="#">Development</a>
                            </li>
                            <li>
                                <router-link to="/services-two">Services</router-link>
                            </li>
                            <li>
                                <a href="#">UI/UX Design</a>
                            </li>
                            <li>
                                <a href="#">Support Engineer</a>
                            </li> -->
                        </ul>
                    </div>    
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <div class="footer-heading">
                            <h3>Contact</h3>
                        </div>

                        <div class="footer-info-contact">
                            <i class="flaticon-phone-call"></i>
                            <h3>Phone</h3>
                            <span><a href="tel:+882-569-756">+123(456)123</a></span>
                        </div>

                        <div class="footer-info-contact">
                            <i class="flaticon-envelope"></i>
                            <h3>Email</h3>
                            <span><a href="mailto:hello@valzo.com">hello@valzo.com</a></span>
                        </div>

                        <div class="footer-info-contact">
                            <i class="flaticon-pin"></i>
                            <h3>Address</h3>
                            <span>32 st Kilda Road, Melbourne VIC, 3004 Australia</span>
                        </div>
                    </div>
                </div>

                
            </div>
        </div>

        <div class="lines">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Footer'
    }
</script>