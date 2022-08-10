<template>
  <section id="iq-feature" class="pb-0">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="title-box">
            <h2>Tool for teams, from startup</h2>
            <p>If you are planning on developing a product landing</p>
          </div>
        </div>
        <div v-for="(list,index) in lists" :key="index" class="col-lg-4">
          <div class="feature-flip-box flip-right wow fadeInUp  text-center" data-wow-delay="0.6s" style="visibility: visible; animation-delay: 0.6s; animation-name: fadeInUp;">
            <div class="flipbox-wrapper">
              <div class="front-side" :style="`background: url(${require('../../../../assets/images/landing-page/landing-2/services-bg.jpg')})`">
                <div class="flip-icon">
                  <i aria-hidden="true" :class="list.icon" />
                </div>
                <h3 class="flipbox-title text-white">
                  {{ list.title }}
                </h3>
                <div class="flipbox-details text-white">
                  {{ list.desc }}
                </div>
              </div>
              <div class="back-side" :style="`background: url(${require('../../../../assets/images/landing-page/landing-2/services-bg.jpg')})`">
                <div class="flipbox-content">
                  <a class="landing-button btn-success" href="#">{{ list.btntext }}</a>
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
  name: 'Feature',
  data () {
    return {
      lists: [
        {
          icon: 'fas fa-chart-line  text-white',
          title: 'Organisation Chart',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        },
        {
          icon: 'fas fa-calculator text-white',
          title: 'Employee Directory',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        },
        {
          icon: 'far fa-lightbulb  text-white',
          title: 'Employee Profiles',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        },
        {
          icon: 'far fa-file-alt text-white',
          title: 'Leave Application',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        },
        {
          icon: 'fas fa-wifi  text-white',
          title: 'Custom Reporting',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        },
        {
          icon: 'far fa-paper-plane text-white',
          title: 'Company Calendar',
          desc: 'Established fact that a reader will be distracted by the readable.',
          btntext: 'Learn More'
        }
      ]
    }
  }
}
</script>
<style scoped>


</style>
