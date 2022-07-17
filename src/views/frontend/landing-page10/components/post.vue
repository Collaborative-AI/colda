<template>
  <section class="pb-70 pt-0 iq-rpt-zero">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
        </div>
        <div class="col-lg-12">
          <VTwoPost :postList="postList" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import VTwoPost from '../../../../components/frontend/VTwoPost'
export default {
  name: 'Post',
  components:{
    VTwoPost
  },
  data () {
    return {
      titleSectionProp: {
        title: 'Latest Posts',
        description: 'If you are planning on developing a product landing.'
      },

      postList: [
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-10/20.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-10/19.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-10/18.jpg') },
        { title: 'Life Lack Meaning', description: 'It is a long established fact that a reader will be distracted by the readable.', datetime: 'November 28, 2019', image: require('@/assets/images/landing-page/landing-10/17.jpg') },
        
      ]
    }
  }
}
</script>
