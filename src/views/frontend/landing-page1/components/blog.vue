<template>
  <section id="iq-blog" class="pb-70">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
        </div>
        <div class="col-lg-12">
          <VTwoPost :postList="List" />
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
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-1/20.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-1/19.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-1/18.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-1/17.jpg') },
        // { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('../../assets/sofbox-v2/images/home-1/20.jpg') }
      ]
    }
  }
}
</script>
