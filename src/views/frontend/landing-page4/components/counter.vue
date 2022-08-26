<template>
  <div class="iq-counter-block position-relative overflow-hidden">
    <img src="@/assets/images/landing-page/landing-4/overlay-dot2.png" class="overlay-right-top-2 img-fluid" alt="#">
    <div class="auto-container">
      <div class="inner-container">
        <div class="iq-pattern-style">
        </div>
        <div class="row">
          <div v-for="(counter,index) in counters" :key="index" class="col-lg-3 col-md-6 col-sm-12 wow fadeIn">
            <div class="iq-counter  iq-counter-style-1">
              <div class="counter-content">
                <p class="iq-counter-info">
                  <span class="timer counter" :data-to="counter.data" data-speed="5000">{{ counter.data }}</span>
                  <span class="counter-after-content">{{ counter.sign }}</span>
                  <span class="counter-symbol" />
                </p>
                <p class="counter-content-text">
                  {{ counter.title }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <img src="@/assets/images/landing-page/landing-4/overlay.png" class="overlay-left-bottom" alt="#">
  </div>
</template>
<script>
import {core}   from '../../../../config/pluginInit'
export default {
  name: 'Counter',
  mounted(){
  core.index()
  },
  data () {
    return {
      counters: [
        {
          data: '25',
          sign: '+',
          title: 'Years of Experience'
        },
        {
          data: '50',
          sign: ' ',
          title: 'Awards & Recognition'
        },
        {
          data: '1200',
          sign: ' ',
          title: 'Completed Projects'
        },
        {
          data: '90',
          sign: '%',
          title: 'Satisfied Clients'
        }
      ]
    }
  }
}
</script>
