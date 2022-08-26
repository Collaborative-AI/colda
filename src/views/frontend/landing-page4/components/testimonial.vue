<template>
  <section class="bg-warning-light iq-section-space iq-section-pb-70 testimonial position-relative overflow-hidden">
    <img src="@/assets/images/landing-page/landing-4/overlay.png" class="overlay-right-top" alt="#">
    <div class="container">
      <TitleSection title="Check what's our client say about us!" subclass="pr-lg-5 mb-3">
        <template v-slot:underline>
          <p class="iq-line four" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="text-left">
              <p class="m-0">
                There are many variations of passages of Lorem Ipsum available, but the majority have Category in some form, by injected humour, or randomised words which don't look even slightly believable.
              </p>
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
            <div v-for="(testimonial,index) in testimonials" :key="index" class="item">
              <CardStyle2 :text="testimonial.text" :src="testimonial.src" :title="testimonial.title" :position="testimonial.position" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <img src="@/assets/images/landing-page/landing-4/overlay-dot.png" class="overlay-left-bottom-2" alt="#">
  </section>
</template>
<script>
export default {
  name: 'Testimonial',
  data () {
    return {
      testimonials: [
        {
          title: 'Aney Hark',
          src: require('@/assets/images/landing-page/landing-4/testimonial-1.jpg'),
          text: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip. qui blanditiis praesentium vero eos et accus adip.',
          position: 'Trainer'
        },
        {
          title: 'Rooney Mara',
          src: require('@/assets/images/landing-page/landing-4/testimonial-2.jpg'),
          text: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip. qui blanditiis praesentium vero eos et accus adip.',
          position: 'Trainer'
        },
        {
          title: 'Al Pacino',
          src: require('@/assets/images/landing-page/landing-4/testimonial-3.jpg'),
          text: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium vero eos et accus adip. qui blanditiis praesentium vero eos et accus adip.',
          position: 'Trainer'
        }
      ]
    }
  }
}
</script>
