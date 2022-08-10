<template>
  <section id="iq-testimonial" class="creative-section testimonial">
    <img src="@/assets/images/landing-page/landing-9/fancy-pattern-2.png" class="img-fluid fancy-back" alt="#">
    <div class="container">
      <TitleSection title="  Our Testimonial " subclass="pr-lg-5">
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="btn-container">
              <a class="iq-button iq-gradient-btn" href="#"><span>Click Here</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row justify-content-sm-center">
        <div class="col-sm-12">
          <div
            class="owl-carousel"
            data-autoplay="true"
            data-loop="true"
            data-nav="true"
            data-dots="false"
            data-items="2"
            data-items-laptop="2"
            data-items-tab="1"
            data-items-mobile="1"
            data-items-mobile-sm="1"
            data-margin="30"
          >
            <div v-for="(item,index) in items" :key="index" class="item">
              <CardStyle4 :title="item.title" :desc="item.desc" :src="item.src" :designation="item.designation" style="width: 540px; margin-right: 30px;"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Testimonial',
  data () {
    return {
      items: [
        {
          desc: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip.',
          src: require('@/assets/images/landing-page/landing-9/testimonial-d21.png'),
          title: 'Aney Hark',
          designation: 'Designer'
        },
        {
          desc: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip.',
          src: require('@/assets/images/landing-page/landing-9/testimonial-d22.png'),
          title: 'Rooney Mara',
          designation: 'Developer'
        },
        {
          desc: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip.',
          src: require('@/assets/images/landing-page/landing-9/testimonial-d23.png'),
          title: 'Al Pacino',
          designation: 'Trainer'
        }
      ]
    }
  }
}
</script>
