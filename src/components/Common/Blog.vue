<template>
    <div class="blog-section pt-100 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Our <span>Latest</span> News</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                <div class="bar"></div>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/blog-1.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>20 March 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Great Tips To Earn More Money From Digital Industry
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
                                <img src="../../assets/images/blog/blog-2.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>25 April 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    The Billionaire Guide On Design That will Get You Rich
                                </router-link>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 offset-lg-0 offset-md-3">
                    <div class="single-blog">
                        <div class="image">
                            <router-link to="/single-blog">
                                <img src="../../assets/images/blog/blog-3.jpg" alt="image">
                            </router-link>
                        </div>

                        <div class="content">
                            <span>30 July 2022</span>
                            <h3>
                                <router-link to="/single-blog">
                                    Making Peace With The Feast Or Famine Of Freelancing
                                </router-link>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor</p>
                            <router-link to="/single-blog" class="read-more">Read More</router-link>
                        </div>
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