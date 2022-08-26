<template>
  <section class="iq-section-pb-70" >
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
        </div>
        <div class="col-lg-12">
          <VTwoPost :post-list="List" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Blog',
  data () {
    return {
      titleSectionProp: {
        title: 'Latest Posts',
        description: 'If you are planning on developing a product landing.'
      },

      List: [
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-2/20.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-2/19.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-2/18.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-2/17.jpg') },
        
      ]
    }
  }
}
</script>
