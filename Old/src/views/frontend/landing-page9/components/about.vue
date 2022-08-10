<template>
  <AboutSection
    :image="image"
    title="We are the largest bussiness expert in europe and asia"
    para1="Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Ornare aenean euismod elementum nisi quis eleifend quam."
    para2="Vitae congue eu consequat ac felis donec et odio. Eget felis eget nunc lobortis. At lectus urna duis convallis convallis tellus id interdum. Tellus in hac habitasse platea dictumst vestibulum rhoncus est."
    :signimage="signimage"
    signtitle="-Founder Of Cretic"
    mainclass="iq-aboutus overview-block-pt"
  />
</template>
<script>
import image from '@/assets/images/landing-page/landing-9/about-1.png'
import signimage from '@/assets/images/landing-page/landing-9/sign-d2.png'
export default {
  name: 'About',
  data () {
    return {
      image,
      signimage
    }
  }
}
</script>
