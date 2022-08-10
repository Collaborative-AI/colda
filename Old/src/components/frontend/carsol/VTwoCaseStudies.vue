<template>
  <div
    class="owl-carousel"
    data-autoplay="true"
    data-loop="true"
    data-nav="true"
    data-dots="false"
    data-items="3"
    data-items-laptop="3"
    data-items-tab="2"
    data-items-mobile="2"
    data-items-mobile-sm="1"
    data-margin="30"
  >
    <div v-for="(list,index) in lists" :key="index" class="item">
      <div class="iq-masonry-item">
        <div class="iq-portfolio">
          <a href="#" class="portfolio-img"><img :src="list.image" class="img-fluid" alt="img">
            <div class="portfolio-link">
              <div class="icon">
                <i class="fa fa-link" aria-hidden="true" />
              </div>
            </div>
          </a>
          <div class="iq-portfolio-content text-left">
            <div class="details-box clearfix">
              <div class="consult-details">
                <a href="#">
                  <h5 class="text-hover">{{ list.title }}</h5>
                </a>
                <p class="mb-0">
                  {{ list.description }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'VTwoCaseStudies',
  // eslint-disable-next-line vue/require-prop-types
  props: ['lists']

}
</script>
