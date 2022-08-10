<template>
  <div :id="id">
    <slot name="nav" v-if="navTop" />
    <div class="swiper-container" v-if="tag == 'div'" >
      <!-- Additional required wrapper -->
      <div class="swiper-wrapper">
        <!-- Slides -->
        <slot />
      </div>
      <!-- If we need pagination -->
      <div class="swiper-pagination" v-if="pagination">
        <slot name="pagination" />
      </div>
      <!-- If we need scrollbar -->
      <div class="swiper-scrollbar" v-if="scrollbar">
        <slot name="scrollbar" />
      </div>
    </div>
    <ul class="swiper-container" v-else-if="tag == 'ul'" >
      <!-- Additional required wrapper -->
      <div class="swiper-wrapper">
        <!-- Slides -->
        <slot />
      </div>
      <!-- If we need pagination -->
      <div class="swiper-pagination" v-if="pagination">
        <slot name="pagination" />
      </div>
      <!-- If we need scrollbar -->
      <div class="swiper-scrollbar" v-if="scrollbar">
        <slot name="scrollbar" />
      </div>
    </ul>
    <slot name="nav" v-if="!navTop" />
  </div>
</template>
<script>
import Swiper, { Navigation, Pagination, Parallax, Autoplay } from 'swiper'
import 'swiper/swiper.scss'
Swiper.use([Navigation, Pagination, Parallax, Autoplay])
let swiper
export default {
  name: 'Swiper',
  props: {
    className: { type: String, default: 'vue-swiper-class' },
    id: { type: String, default: 'vue-swiper-id' },
    options: {
      type: Object,
      default: () => {
        return {
          centeredSlides: false,
          loop: true,
          slidesPerView: 2,
          spaceBetween: 30,
          autoplay: false,
          breakpoints: {
            // when window width is >= 480px
            480: {
              slidesPerView: 1,
              spaceBetween: 15
            },
            // when window width is >= 640px
            640: {
              slidesPerView: 2,
              spaceBetween: 30
            }
          },
          // If we need pagination
          pagination: {
            el: '.swiper-pagination'
          },

          // Navigation arrows
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },

          // And if we need scrollbar
          scrollbar: {
            el: '.swiper-scrollbar'
          }
        }
      }
    },
    navTop: { type: Boolean, default: false },
    pagination: { type: Boolean, default: false },
    scrollbar: { type: Boolean, default: false },
    tag: { type: String, default: 'div' }
  },
  data () {
    return {
      swiper: {}
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      swiper = new Swiper('.swiper-container', this.options)
    },
    reInit () {
      swiper.destroy(true, true)
      setTimeout(() => {
        this.init()
      }, 500)
    }
  }
}
</script>

<style scoped>

    [dir="rtl"] .swiper-slide {
      text-align: right !important;
      /* Center slide text vertically */
      display: -webkit-box !important;
      display: -ms-flexbox !important;
      display: -webkit-flex !important;
      display: flex !important;
      -webkit-box-pack: right !important;
      -ms-flex-pack: right !important;
      -webkit-justify-content: right !important;
      justify-content: right !important;
      -webkit-box-align: right !important;
      -ms-flex-align: right !important;
      -webkit-align-items: right !important;
      align-items: right !important;
    }
</style>
