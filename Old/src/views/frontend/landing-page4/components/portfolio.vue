<template>
  <section class="position-relative iq-section-space iq-section-pb-40 iq-portfolio-section overflow-hidden">
    <img src="@/assets/images/landing-page/landing-4/overlay.png" class="overlay-right-bottom" alt="#">
    <img src="@/assets/images/landing-page/landing-4/overlay-dot.png" class="overlay-right-bottom-2" alt="#">
    <div class="container">
      <TitleSection title=" We work in the fields of UI/UX design, photography" subclass="pr-lg-6">
        <template v-slot:underline> 
          <p class="iq-line two" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6 wow fadeIn">
            <div class="btn-container">
              <a class="iq-button d-inline-block" href="#"><span>Explore More</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row text-center position-relative">
        <div v-for="(portfolio,index) in portfolios" :key="index" class="col-lg-6 col-md-6 wow fadeIn">
          <CardStyle1 :text="portfolio.text" :title="portfolio.title" :src="portfolio.src" :pattern="portfolio.pattern" :mainclass="portfolio.mainclass" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Portfolio',
  data () {
    return {
      portfolios: [{
        text: 'Design Concept',
        title: 'Category',
        src: require('@/assets/images/landing-page/landing-4/portfolio-1.jpg'),
        pattern: require('@/assets/images/landing-page/landing-4/pattern.png'),
        mainclass: 'mr'
      },
      {
        text: 'Bussiness Growth',
        title: 'Category',
        src: require('@/assets/images/landing-page/landing-4/portfolio-2.jpg'),
        pattern: require('@/assets/images/landing-page/landing-4/pattern.png'),
        mainclass: 'ml'
      },
      {
        text: 'Creative Design',
        title: 'Category',
        src: require('@/assets/images/landing-page/landing-4/portfolio-3.jpg'),
        pattern: require('@/assets/images/landing-page/landing-4/pattern.png'),
        mainclass: 'mr'
      },
      {
        text: 'Concept Design',
        title: 'Category',
        src: require('@/assets/images/landing-page/landing-4/portfolio-4.png'),
        pattern: require('@/assets/images/landing-page/landing-4/pattern.png'),
        mainclass: 'ml'
      }
      ]
    }
  }
}
</script>