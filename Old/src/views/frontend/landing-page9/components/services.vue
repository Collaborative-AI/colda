<template>
  <section class="position-relative iq-section-pb-70 creative-section">
    <div class="container">
      <TitleSection title=" Service for Creative Agency Investor " titleclass="pr-lg-5">
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6 ">
            <div class="btn-container">
              <a class="iq-button iq-gradient-btn d-inline-block" href="#"><span>Click Here</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row text-center position-relative ">
        <div v-for="(group,index) in groups" :key="index" class="col-lg-3 col-md-6 ">
          <div class="iq-service-style2 text-left">
            <div class="iq-iconbg">
              <i :class="group.icon" aria-hidden="true" />
            </div>
            <div class="iq-content">
              <div class="iq-title">
                <h4>{{ group.title }}</h4>
              </div>
              <p class="m-0">
                {{ group.desc }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Services',
  data () {
    return {
      groups: [ {
        title: 'Creative Always',
        icon: 'fas fa-expand-alt',
        desc: 'Contrary to popular belief, Lorem Ipsum is not simply.'
      },
      {
        title: 'Express Custom',
        icon: 'fas fa-file-video',
        desc: 'Contrary to popular belief, Lorem Ipsum is not simply.'
      },
      {
        title: 'Premium Integrations',
        icon: 'far fa-file-alt',
        desc: 'Contrary to popular belief, Lorem Ipsum is not simply.'
      },
      {
        title: 'Real-Time Editing',
        icon: 'fas fa-pencil-alt',
        desc: 'Contrary to popular belief, Lorem Ipsum is not simply.'
      }
      ]
    }
  }
}
</script>
