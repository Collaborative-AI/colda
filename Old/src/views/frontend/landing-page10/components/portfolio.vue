<template>
  <section id="iq-portfolio" class="prox-gradient-bg-top"   :style= "`background: url(${require('@/assets/images/landing-page/landing-10/15.png')});background-repeat: no-repeat !important;background-position: 0 0 !important;`">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
        </div>
        <div class="col-lg-12">
          <VTwoCaseStudies :lists="List" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import VTwoCaseStudies from '../../../../components/frontend/carsol/VTwoCaseStudies'
export default {
  name: 'Portfolio',
  components:{
VTwoCaseStudies
  },
  data () {
    return {
      titleSectionProp: {
        title: 'Our Case Studies',
        description: 'If you are planning on developing a product landing app or website, take a look at this beautiful-crafted'
      },

      List: [
        { title: 'Dignissimos wisi cillum', description: 'Wordpress — eCommerce', image: require('@/assets/images/landing-page/landing-10/16.jpg') },
        { title: 'Dignissimos wisi cillum', description: 'Wordpress — eCommerce', image: require('@/assets/images/landing-page/landing-10/17.jpg') },
        { title: 'Dignissimos wisi cillum', description: 'Wordpress — eCommerce', image: require('@/assets/images/landing-page/landing-10/18.jpg') },
        { title: 'Dignissimos wisi cillum', description: 'Wordpress — eCommerce', image: require('@/assets/images/landing-page/landing-10/19.jpg') },
        { title: 'Dignissimos wisi cillum', description: 'Wordpress — eCommerce', image: require('@/assets/images/landing-page/landing-10/20.jpg') }
      ]
    }
  }
}
</script>

