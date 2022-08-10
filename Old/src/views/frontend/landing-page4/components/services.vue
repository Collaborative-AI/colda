<template>
  <div class="position-relative iq-section-space iq-section-pb-70 iq-investor overflow-hidden">
    <div class="container">
      <TitleSection title="Service for Creative Agency Investor" titleclass="pr-lg-5">
        <template v-slot:underline>
          <p class="iq-line one" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6 wow fadeIn">
            <div class="btn-container">
              <a class="iq-button d-inline-block" href="#"><span>Click Here</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row text-center position-relative">
        <div v-for="(service,index) in services" :key="index" class="col-lg-3 col-md-6 wow fadeIn ">
          <ServiceStyle :icon="service.icon" :src="service.src" :title="service.title" :description="service.desc" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Service',
  data () {
    return {
      services: [
        {
            
          src: require('@/assets/images/landing-page/landing-4/fancy-pattern.png'),
          title: 'Digital Advice',
          desc: 'Contrary to popular belief, Lorem Ipsum is not simply.',
          icon: 'fa fa-globe'
        },
        {
          src: require('@/assets/images/landing-page/landing-4/fancy-pattern.png'),
          title: 'Leadership',
          desc: 'Contrary to popular belief, Lorem Ipsum is not simply.',
          icon: 'fa fa-users'
        },
        {
          src: require('@/assets/images/landing-page/landing-4/fancy-pattern.png'),
          title: 'Improvement',
          desc: 'Contrary to popular belief, Lorem Ipsum is not simply.',
          icon: 'fas fa-chart-line'
        },
        {
          src: require('@/assets/images/landing-page/landing-4/fancy-pattern.png'),
          title: 'Finance management',
          desc: 'Contrary to popular belief, Lorem Ipsum is not simply.',
          icon: 'fa fa-object-group'
        }
      ]
    }
  }
}
</script>
