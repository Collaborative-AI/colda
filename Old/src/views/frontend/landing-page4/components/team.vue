<template>
  <section class="iq-section-space creative-section">
    <img src="@/assets/images/landing-page/landing-4/overlay-dot2.png" class="overlay-right-top-2" alt="#">
    <div class="container">
      <TitleSection title="Meet Our team of Professional" subclass="pr-lg-6">
        <template v-slot:underline>
          <p class="iq-line three" />
        </template>
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="btn-container">
              <a class="iq-button d-inline-block" href="#"><span>Explore More</span><em /></a>
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
            data-nav="false"
            data-dots="true"
            data-items="3"
            data-items-laptop="3"
            data-items-tab="2"
            data-items-mobile="1"
            data-items-mobile-sm="1"
            data-margin="30"
          >
            <div v-for="(team,index) in teams" :key="index" class="item" style="width: 350px; margin-right: 30px;">
              <div class="iq-team-blog text-left">
                <div class="iq-team">
                  <div class="iq-team-img">
                    <img class="img-fluid" :src="team.src" alt="image">
                  </div>
                  <div class="iq-team-social">
                    <ul>
                      <li><a href="#"><i class="fa fa-facebook" /></a></li>
                      <li><a href="#"><i class="fa fa-twitter" /></a></li>
                      <li><a href="#"><i class="fa fa-google" /></a></li>
                    </ul>
                  </div>
                  <div class="iq-team-info text-left">
                    <h4 class="member-text">
                      {{ team.title }}
                    </h4>
                    <span class="designation-text">{{ team.designation }}</span>
                  </div>
                  <div class="iq-image">
                    <img :src="team.pattern" class="img-fluid" alt="#">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <img src="@/assets/images/landing-page/landing-4/overlay.png" class="overlay-left-bottom" alt="#">
  </section>
</template>
<script>
export default {
  name: 'Team',
  data () {
    return {
      teams: [
        {
          src: require('@/assets/images/landing-page/landing-4/team-1.jpg'),
          title: 'Farid Amini',
          designation: 'Manager',
          pattern: require('@/assets/images/landing-page/landing-4/team-hover-pattern.png')
        },
        {
          src: require('@/assets/images/landing-page/landing-4/team-2.jpg'),
          title: 'Eva Mendes',
          designation: 'CEO',
          pattern: require('@/assets/images/landing-page/landing-4/team-hover-pattern.png')
        },
        {
          src: require('@/assets/images/landing-page/landing-4/team-3.jpg'),
          title: ' Martin Luther',
          designation: 'Assistant',
          pattern: require('@/assets/images/landing-page/landing-4/team-hover-pattern.png')
        }
      ]
    }
  }
}
</script>
