<template>
  <section class="iq-section-space iq-section-space prox-custom-bg iq-bg-over">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 wow fadeInUp">
          <div class="title-box wow fadeInUp text-center">
            <span class="title-design">TESTIMONIALS</span>
            <h2>100+ Companies are Using ProX</h2>
          </div>
        </div>
      </div>
      <div class="row">
          <div class="col-md-12  wow fadeInUp">
            <div class="owl-carousel testimonial-style owl-loaded owl-drag" data-dots="true" data-nav="false" data-autoplay="false" data-loop="true" data-items="1" data-items-laptop="1" data-items-tab="1" data-items-mobile="1" data-items-mobile-sm="1" data-margin="30">
              <div class="item text-center" v-for="(item, index) in list" :key="index" style="width: 1110px; margin-right: 30px;"> 
                <div class="iq-testimonial">
                  <div class="testimonial-info">
                    <img alt="#" class="img-fluid rounded-circle" :src="item.image">
                    <div class="testimonial-name">
                      <h5>{{ item.title }}</h5>
                      <span class="sub-title">{{ item.subtitle }}</span>
                    </div>
                  </div>
                  <p>{{ item.description }}</p>
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
    name:'Testimonials',
    data(){
      return{
        list:[
          {
            title:'Jack White',
            subtitle:'CEO',
            description:'Richard McClintock, a Latin professor at Hampden-Sydney consectetur adip isicing elit, sed dolore magna aliqua hampden. Latin professor at Hampden-Sydney consectetur.',
            image:require('@/assets/images/landing-page/landing-6/37.jpg')
          },
          {
            title:'Walhan Bobe',
            subtitle:'Business Advisor',
            description:'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium incididunt ut labore et dolore Sed ut perspiciatis error. Perspiciatis unde omnis iste.',
            image:require('@/assets/images/landing-page/landing-6/38.jpg')
          },
          {
            title:'Mark McManus',
            subtitle:'COO',
            description:'“Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.”',
            image:require('@/assets/images/landing-page/landing-6/39.jpg')
          }
        ]
      }
    }
}
</script>