<template>
  <section class=" iq-section-space ">
    <div class="container">
        <div class="row layer-fly-one ">
            <div class="col-md-12">
                <div class="title-box wow fadeInUp title-shadow  text-center">
                    <span class="title-design">Blog</span>
                    <h2>Recent Blog</h2>
                </div>
                <div class="prox-recentblog v1">
                    <div class="owl-carousel owl-loaded owl-drag" data-dots="false" data-nav="false" data-items="3" data-items-laptop="3" data-items-tab="2" data-items-mobile="1" data-items-mobile-sm="1" data-autoplay="true" data-loop="true">
                        <div class="item">
                            <div class="iq-blog-box mb-0">
                                <div class="iq-blog-image clearfix">
                                    <img :src="require('@/assets/images/landing-page/landing-8/21.png')" class="img-fluid center-block" alt="blogimage1">
                                    <ul class="iq-blogtag">
                                        <li><a href="#">HTML</a> </li>
                                    </ul>
                                </div>
                                <div class="iq-blog-detail">
                                    <div class="iq-blog-meta">
                                        <ul>
                                            <li class="list-inline-item">
                                                <a href="#" rel="bookmark">
                                                    <time class="entry-date published updated" datetime="2019-09-26T06:49:49+00:00" >September 26, 2019 </time>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="blog-title">
                                        <a href="#">
                                            <h4>Build Construction</h4>
                                        </a>
                                    </div>
                                    <p>They bring to you a host of beautifully created infographics that contain the latest digital marketing.</p>
                                    <div class="blog-button"><a class="landing-button-link" href="#">Read More<i class="fa fa-angle-right" aria-hidden="true"></i></a></div>
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="iq-blog-box mb-0">
                                <div class="iq-blog-image clearfix">
                                    <img :src="require('@/assets/images/landing-page/landing-8/22.png')" class="img-fluid center-block" alt="blogimage2">
                                    <ul class="iq-blogtag">
                                        <li><a href="#">Design</a> </li>
                                    </ul>
                                </div>
                                <div class="iq-blog-detail">
                                    <div class="iq-blog-meta">
                                        <ul>
                                            <li class="list-inline-item">
                                                <a href="#" rel="bookmark">
                                                    <time class="entry-date published updated" datetime="2019-09-26T06:49:49+00:00" >September 26, 2019 </time>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="blog-title">
                                        <a href="#">
                                            <h4>Life Lack Meaning</h4>
                                        </a>
                                    </div>
                                    <p>They bring to you a host of beautifully created infographics that contain the latest digital marketing.</p>
                                    <div class="blog-button"><a class="landing-button-link" href="#">Read More<i class="fa fa-angle-right" aria-hidden="true"></i></a></div>
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="iq-blog-box mb-0">
                                <div class="iq-blog-image clearfix">
                                    <img :src="require('@/assets/images/landing-page/landing-8/23.png')" class="img-fluid center-block" alt="blogimage3">
                                    <ul class="iq-blogtag">
                                        <li><a href="#">HTML</a> </li>
                                    </ul>
                                </div>
                                <div class="iq-blog-detail">
                                    <div class="iq-blog-meta">
                                        <ul>
                                            <li class="list-inline-item">
                                                <a href="#" rel="bookmark">
                                                    <time class="entry-date published updated"  datetime="2019-09-26T06:49:49+00:00">September 26, 2019 </time>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="blog-title">
                                        <a href="#">
                                            <h4>Construction industry</h4>
                                        </a>
                                    </div>
                                    <p>They bring to you a host of beautifully created infographics that contain the latest digital marketing.</p>
                                    <div class="blog-button"><a class="landing-button-link" href="#">Read More<i class="fa fa-angle-right" aria-hidden="true"></i></a></div>
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="iq-blog-box mb-0">
                                <div class="iq-blog-image clearfix">
                                    <img :src="require('@/assets/images/landing-page/landing-8/23.png')" class="img-fluid center-block" alt="blogimage4">
                                    <ul class="iq-blogtag">
                                        <li><a href="#">CSS</a> </li>
                                    </ul>
                                </div>
                                <div class="iq-blog-detail">
                                    <div class="iq-blog-meta">
                                        <ul>
                                            <li class="list-inline-item">
                                                <a href="#" rel="bookmark">
                                                    <time class="entry-date published updated"  datetime="2019-09-26T06:49:49+00:00">September 26, 2019 </time>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="blog-title">
                                        <a href="#">
                                            <h4>Content Marketing</h4>
                                        </a>
                                    </div>
                                    <p>They bring to you a host of beautifully created infographics that contain the latest digital marketing.</p>
                                    <div class="blog-button"><a class="landing-button-link" href="#">Read More<i class="fa fa-angle-right" aria-hidden="true"></i></a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </section>
</template>
<script>
export default {
  name:'Blog'
}
</script>