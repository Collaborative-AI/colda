<template>
  <div class="iq-blog-box">
    <div class="iq-blog-image clearfix">
      <img :src="src" alt="#">
    </div>
    <div class="iq-blog-detail">
      <div class="blog-title">
        <a href="#">
          <h4 class="mb-3">{{ title }}</h4>
        </a>
      </div>
      <p class="iq-desc">
        {{ description }}
      </p>
      <div class="blog-footer">
        <div class="iq-blog-meta">
          <ul class="iq-postdate">
            <li class="list-inline-item">
              <i class="fa fa-calendar mr-1" aria-hidden="true" /> <a href="#">{{ date }}</a>
            </li>
          </ul>
        </div>
        <div class="blog-button">
          <a class="iq-link-button" href="#">{{ text }}</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CardStyle3',
  props: {
    text: {
      type: String,
      default: ''
    },
    src: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    date: {
      type: String,
      default: ''
    }
  }
}
</script>
