<template>
    <div class="pricing-section pt-100 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Our <span>Pricing</span> Plan</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                <div class="bar"></div>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="single-pricing two">
                        <div class="pricing-header">
                            <h3>Basic</h3>
                            <p>Business Up</p>
                        </div>

                        <div class="price">
                            <sup>$</sup>29<sub>/mo</sub>
                        </div>
                
                        <ul class="pricing-list">
                            <li>
                                <i class="flaticon-checked"></i> 
                                10 GB Hosting 
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                2 Unique Users 
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                12 GB Capacity
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Any Where Access</del>
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Weekly Backup</del>
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Support 24/Hour</del>
                            </li>
                        </ul>

                        <div class="price-btn">
                            <router-link to="/pricing" class="default-btn">
                                Buy Now
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-pricing two">
                        <div class="pricing-header">
                            <h3>Standard</h3>
                            <p>Business Up</p>
                        </div>

                        <div class="price">
                            <sup>$</sup>79<sub>/mo</sub>
                        </div>
                
                        <ul class="pricing-list">
                            <li>
                                <i class="flaticon-checked"></i> 
                                Visitor Info
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                Quick Responses
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                12 GB Capacity
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                Any Where Access
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Weekly Backup</del>
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Support 24/Hour</del>
                            </li>
                        </ul>

                        <div class="price-btn">
                            <router-link to="/pricing" class="default-btn">
                                Buy Now
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 offset-lg-0 offset-md-3">
                    <div class="single-pricing two">
                        <div class="pricing-header">
                            <h3>Premium</h3>
                            <p>Business Up</p>
                        </div>

                        <div class="price">
                            <sup>$</sup>99<sub>/mo</sub>
                        </div>
                
                        <ul class="pricing-list">
                            <li>
                                <i class="flaticon-checked"></i> 
                                10 GB Hosting 
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                2 Unique Users 
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                12 GB Capacity
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                Any Where Access
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                Weekly Backup
                            </li>

                            <li>
                                <i class="flaticon-checked"></i> 
                                <del>Support 24/Hour</del>
                            </li>
                        </ul>

                        <div class="price-btn">
                            <router-link to="/pricing" class="default-btn">
                                Buy Now
                            </router-link>
                        </div>
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
        name: 'Pricing'
    }
</script>

