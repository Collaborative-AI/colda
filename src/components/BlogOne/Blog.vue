<template>
    <div class="blog-section ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Our <span>Latest</span> News</h2>
                <p>Check our new use cases!</p>
                <div class="bar"></div>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/weather.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>24 May 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Weather Forecast
                                </router-link>
                            </h3>
                            <p>Forecasting time series weather data with Synspot packages</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/ride.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>25 May 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Uber & Lyft Ride Price Prediction
                                </router-link>
                            </h3>
                            <p>Improve the ride price prediction accuracy by combining the Uber and Lyft ride history during a certain time period</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/earthquake.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>27 May 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Earthquake Forecast
                                </router-link>
                            </h3>
                            <p>Forecast earthquake by using other locations earthquake data</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/blog-4.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>24 March 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Startup Marketing Solution for Business Owner
                                </router-link>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/blog-5.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>20 March 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Web Developement Best Work in Future World
                                </router-link>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/blog-6.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>17 March 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Instagram Feed Add To Your WordPress Site
                                </router-link>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-12 col-md-12">
                    <div class="pagination-area">
                        <a href="#" class="prev page-numbers">
                            <i class="flaticon-left"></i>
                        </a>
                        <a href="#" class="page-numbers">1</a>
                        <span class="page-numbers current" aria-current="page">2</span>
                        <a href="#" class="page-numbers">3</a>
                        <a href="#" class="page-numbers">4</a>
                        <a href="#" class="next page-numbers">
                            <i class="flaticon-right"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Blog'
    }
</script>