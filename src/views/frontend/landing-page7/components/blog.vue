<template>
  <section class="iq-section-space iq-section-space">
    <div class="container">
      <div class="row layer-fly-one ">
        <div class="col-md-12">
          <div class="title-box wow fadeInUp title-shadow  text-center">
            <span class="title-design">Blog</span>
            <h2>Recent Blog</h2>
          </div>
          <div class="ProX-recentblog v1">
            <div
              class="owl-carousel owl-loaded owl-drag"
              data-dots="false"
              data-nav="false"
              data-items="3"
              data-items-laptop="3"
              data-items-tab="2"
              data-items-mobile="1"
              data-items-mobile-sm="1"
              data-autoplay="true"
              data-loop="true"
            >
              <div v-for="(item,index) in items" :key="index" class="item" >
                <div class="iq-blog-box">
                  <div class="iq-blog-image clearfix">
                    <img :src="item.src" class="img-fluid center-block" alt="blogimage" >
                    <ul class="iq-blogtag">
                      <li><a href="#">{{ item.tag }}</a> </li>
                    </ul>
                  </div>
                  <div class="iq-blog-detail">
                    <div class="iq-blog-meta">
                      <ul>
                        <li class="list-inline-item"> <span class="screen-reader-text">Posted on</span> <a href="#" rel="bookmark"> <time class="entry-date published updated" datetime="2019-09-26T06:51:19+00:00">{{ item.date }} </time> </a> </li>
                      </ul>
                    </div>
                    <div class="blog-title">
                      <a href="#">
                        <h4>{{ item.title }}</h4>
                      </a>
                    </div>
                    <p>{{ item.description }}</p>
                    <div class="blog-button"><a class="button-link" href="#">Read More<i class="fa fa-angle-right" aria-hidden="true"></i></a></div>
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
  name: 'Blog',
  data () {
    return {
      items: [
        {
          title: 'Build Construction',
          tag: 'HTML',
          date: 'September 26, 2019',
          description: 'They bring to you a host of beautifully created infographics that contain the latest digital marketing.',
          src: require('@/assets/images/landing-page/landing-7/23.png')
        },
        {
          title: 'Life Lack Meaning',
          tag: 'Design',
          date: 'September 26, 2019',
          description: 'They bring to you a host of beautifully created infographics that contain the latest digital marketing.',
          src: require('@/assets/images/landing-page/landing-7/21.png')
        },
        {
          title: 'Construction industry',
          tag: 'HTML',
          date: 'September 26, 2019',
          description: 'They bring to you a host of beautifully created infographics that contain the latest digital marketing.',
          src: require('@/assets/images/landing-page/landing-7/22.png')
        },
        {
          title: 'Content Marketing',
          tag: 'CSS',
          date: 'September 26, 2019',
          description: 'They bring to you a host of beautifully created infographics that contain the latest digital marketing.',
          src: require('@/assets/images/landing-page/landing-7/23.png')
        }
      ]
    }
  }
}
</script>
