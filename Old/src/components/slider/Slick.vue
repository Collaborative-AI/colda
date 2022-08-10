<template>
  <vue-slick ref="slick" :options="option" :class="classname" :id="id">
    <slot />
  </vue-slick>
</template>
<script>
import VueSlick from 'vue-slick'
export default {
  name: 'Slick',
  components: {
    VueSlick
  },
  props: {
    id: {type: String, default: 'id'},
    option: {
      type: Object,
      default: () => {
        return {
          centerMode: false,
          centerPadding: '60px',
          slidesToShow: 2,
          slidesToScroll: 1,
          focusOnSelect: true,
          responsive: [
            {
              breakpoint: 992,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '30',
                slidesToShow: 1
              }
            },
            {
              breakpoint: 480,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '15',
                slidesToShow: 1
              }
            }
          ],
          // nextArrow: '<a href="#" class="ri-arrow-left-s-line left"></a>',
          // prevArrow: '<a href="#" class="ri-arrow-right-s-line right"></a>'
        }
      }
    },
    classname:{
      type:String,
      default: ''
    }
  },
  methods: {
    reInit () {
      // Helpful if you have to deal with v-for to update dynamic lists
      this.$nextTick(() => {
        this.$refs.slick.reSlick()
      })
    }
  }
}
</script>
