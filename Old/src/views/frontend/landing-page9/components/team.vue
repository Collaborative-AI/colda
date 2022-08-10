<template>
  <section class="iq-section-pb-55  creative-section">
    <div class="container">
      <TitleSection title="  Meet Our Team of Professional " subclass="pr-lg-5">
        <template v-slot:rightside>
          <div class="col-lg-6 col-md-6">
            <div class="btn-container">
              <a class="iq-button iq-gradient-btn" href="#"><span>Explore More</span><em /></a>
            </div>
          </div>
        </template>
      </TitleSection>
      <div class="row justify-content-sm-center">
        <div class="col-sm-12">
          <div
            class="owl-carousel"
            data-autoplay="false"
            data-loop="true"
            data-nav="false"
            data-dots="true"
            data-items="4"
            data-items-laptop="3"
            data-items-tab="2"
            data-items-mobile="1"
            data-items-mobile-sm="1"
            data-margin="30"
          >
            <div v-for="(team,index) in teams" :key="index" class="item">
              <div class="iq-team2 wow fadeInUp">
                <div class="img-pattern position-relative">
                  <div class="iq-team-img">
                    <img :src="team.src" class="img-fluid rounded-circle" alt="#3">
                  </div>
                  <div class="img-pattern-1">
                    <img src="@/assets/images/landing-page/landing-9/team-pattern-1.png" class="img-fluid" alt="#3">
                  </div>
                  <div class="img-pattern-2">
                    <img src="@/assets/images/landing-page/landing-9/team-pattern-2.png" class="img-fluid" alt="#3">
                  </div>
                </div>
                <div class="iq-team-info text-center">
                  <a href="#">
                    <h4>{{ team.title }}</h4>
                  </a>
                  <span class="team-post">{{ team.post }}</span>
                  <div class="share">
                    <ul>
                      <li><a href="#"><i class="fab fa-facebook-f" /></a></li>
                      <li><a href="#"><i class="fab fa-google" /></a></li>
                      <li><a href="#"><i class="fab fa-github" /></a></li>
                      <li><a href="#"><i class="fab fa-instagram" /></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'Team',
  data () {
    return {
      teams: [
        {
          src: require('@/assets/images/landing-page/landing-9/team2-1.jpg'),
          title: 'Letha Soares',
          post: 'Manager'

        },
        {
          src: require('@/assets/images/landing-page/landing-9/team2-2.jpg'),
          title: 'James Adames',
          post: 'CTO'

        },
        {
          src: require('@/assets/images/landing-page/landing-9/team2-3.jpg'),
          title: 'Janet Norris',
          post: 'Jr. Manager'

        },
        {
          src: require('@/assets/images/landing-page/landing-9/team2-4.jpg'),
          title: 'Farid Amini',
          post: 'CFO'

        }
      ]
    }
  }
}
</script>
