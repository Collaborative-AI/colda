<template>
    <div class="protfolio-section bg-color pt-100 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Our <span>Impressive</span> Portfolio</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                <div class="bar"></div>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-1.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Creative Web Develop</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>Web Design</span>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-2.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Digital Services</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>App Development</span>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-3.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Complex Design</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>Software Development</span>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-4.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Creative Web Develop</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>React Development</span>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-5.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Digital Services</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>E-commerce Development</span>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-protfolio">
                        <div class="image">
                            <router-link to="/single-projects">
                                <img src="../../assets/images/portfolio/portfolio-6.png" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <router-link to="/single-projects">
                                <h3>Complex Design</h3>
                            </router-link>
                            <router-link to="/single-projects">
                                <span>Software Engineering</span>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Protfolio'
    }
</script>