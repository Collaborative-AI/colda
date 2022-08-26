<template>
  <div class="swiper-slide" v-if="tag == 'div'">
    <slot />
  </div>
  <ul class="swiper-slide" v-else-if="tag == 'ul'">
    <slot />
  </ul>
  <li class="swiper-slide" v-else-if="tag == 'li'">
    <slot />
  </li>
</template>
<script>
export default {
  name: 'SwiperSlider',
  props: {
    tag: { type: String, default: 'div' }
  }
}
</script>
