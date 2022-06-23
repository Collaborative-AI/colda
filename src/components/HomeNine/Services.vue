<template>
    <div class="services-section">
        <div class="container">
            <div class="section-title">
                <h3>The Perfect Application for Beginners or Professionals</h3>
                <body-1>
                    SynSpot — is a carefully crafted multi-purpose, responsive, and gorgeous application built with Vue.js and Python. It comes with the features you need to quickly start your data analysis, optimize your AI model cooperatively with others without sharing local data.
                </body-1>
                <div class="bar"></div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two">
                        <div class="icon">
                            <i class="flaticon-it"></i>
                        </div>
                        <h3>IT Professionals</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two bg-fc9ba7">
                        <div class="icon">
                            <i class="flaticon-setting"></i>
                        </div>
                        <h3>Web Development</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two bg-2cdcf7">
                        <div class="icon">
                            <i class="flaticon-promotion"></i>
                        </div>
                        <h3>Digital Marketing</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two bg-009af0">
                        <div class="icon">
                            <i class="flaticon-optimize"></i>
                        </div>
                        <h3>Software Engineers</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two bg-f4d62c">
                        <div class="icon">
                            <i class="flaticon-cloud-computing"></i>
                        </div>
                        <h3>Data Analysis</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-services-two bg-1e2d75">
                        <div class="icon">
                            <i class="flaticon-laptop"></i>
                        </div>
                        <h3>SEO & Content</h3>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore facilisis.</p>
                        <router-link to="/single-services" class="read-btn">Read More</router-link>
                    </div>
                </div>
            </div>
        </div>

        <div class="default-shape">
            <div class="shape-1">
                <img src="../../assets/images/shapes/shape-4.png" alt="image">
            </div>

            <div class="shape-2 rotateme">
                <img src="../../assets/images/shapes/shape-5.svg" alt="image">
            </div>

            <div class="shape-3">
                <img src="../../assets/images/shapes/shape-6.svg" alt="image">
            </div>

            <div class="shape-4">
                <img src="../../assets/images/shapes/shape-7.png" alt="image">
            </div>

            <div class="shape-5">
                <img src="../../assets/images/shapes/shape-8.png" alt="image">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Services'
    }
</script>