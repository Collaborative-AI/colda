<template>
  <section id="feature" class="iq-features iq-rpt-0">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="title-box text-center">
               <h6 class="title text-white">Features</h6>
                 <h2 class="text-white">Great Feature</h2>
           </div>
        </div>
      </div>
      <div class="row">
        <div v-for="(feature,index) in features" :key="index" class="col-lg-4 col-md-6">
          <BlackCardStyle2>
            <template v-slot:cardImage>
              <img :src="feature.src" class="img-fluid" alt="images">
            </template>
            <template v-slot:cardTitle>
              <h5 class="mb-3">
                {{ feature.title }}
              </h5>
            </template>
            <template v-slot:cardContent>
              <p class="mb-0">
                It is a long established fact that a reader will be distracted by the readable content.
              </p>
            </template>
          </BlackCardStyle2>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import  BlackCardStyle2 from '../../../../components/frontend/cards/BlackCardStyle2'
export default {
  name: 'Feature',
  components:{ BlackCardStyle2},
  data () {
    return {
      features: [
        {
          src: require('@/assets/images/landing-page/landing-3/04.png'),
          title: ' Calculate Your Work'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/05.png'),
          title: ' Expenses & Reporting'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/04.png'),
          title: '  Mail Management'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/05.png'),
          title: ' Fast Performance'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/04.png'),
          title: ' Fully Responsive'
        },
        {
          src: require('@/assets/images/landing-page/landing-3/05.png'),
          title: ' Awesome Design'
        }
      ]
    }
  }
}
</script>
