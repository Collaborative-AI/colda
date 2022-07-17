<template>
  <div
    class="owl-carousel"
    data-autoplay="true"
    data-loop="true"
    data-nav="false"
    data-dots="false"
    data-items="3"
    data-items-laptop="3"
    data-items-tab="2"
    data-items-mobile="2"
    data-items-mobile-sm="1"
  >
    <div v-for="(list,index) in postList" :key="index" class="item">
      <div class="iq-blog-box ">
        <div class="iq-blog-image clearfix">
          <img :src=" list.image " class="img-fluid center-block" alt="blogimage1">
          <div class="iq-blog-detail">
            <div class="iq-blog-meta">
              <ul>
                <li class="list-inline-item">
                  <span class="screen-reader-text">Posted on</span> <a
                    href="#"
                    rel="bookmark"
                  >{{ list.datetime }}</a>
                </li>
              </ul>
            </div>
            <div class="blog-title">
              <a href="#">
                <h5 class="mb-2">{{ list.title }}</h5>
              </a>
            </div>
            <p class="mb-0">
              {{ list.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'VTwoPost',
  props: {
    // eslint-disable-next-line vue/require-default-prop
    postList: {
      type: Array
    }
  }

}
</script>
