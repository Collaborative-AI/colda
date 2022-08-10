<template>
  <div id="back-to-top" style="display: none;">
    <a id="top" href="javascript:void(0)" class="top" @click="scrollTop()"> <ion-icon name="chevron-up-outline" role="img" class="md hydrated" aria-label="chevron up outline"></ion-icon> </a>
  </div>
</template>
<script>
export default {
  name: 'ScrollTop',
  methods: {
    scrollTop () {
      window.jQuery('body,html').animate({
        scrollTop: 0
      }, 800)
    }
  }
}
</script>
