<template>
  <section  class="iq-about-us position-relative iq-rpt-0">
    <div class="container ">
      <div class="row">
        <div class="col-lg-6 align-self-center wow fadeInUp" data-wow-delay=".5s">
          <BlackSectionTitle
            title="About Us"
            subtitle="About Sofbox"
            titlecontent="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words
          which don't look even slightly believable."
          />
          <div class="row mb-5">
            <div v-for="(about,index) in abouts" :key="index" :class="about.class">
              <div class="iq-counter brd text-left ">
                <div class="right">
                  <h2 class="counter">
                    <span class="timer text-white">{{ about.value }}</span><sup class=" d-inline-block">+</sup>
                  </h2>
                  <div class="iq-lead">
                    {{ about.title }}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
              <a class="landing-button btn-primary" href="#">Read More</a>
          </div>
        </div>
        <div class="col-lg-6" />
      </div>
      <div class="right-image wow slideInRight">
        <img src="@/assets/images/landing-page/landing-3/01.png" class="img-fluid" alt="images" style="max-width: 95%">
      </div>
    </div>
  </section>
</template>
<script>
import BlackSectionTitle from '../../../../components/frontend/title/BlackSectionTitle'

export default {
  name: 'AboutUs',
  components:{
    BlackSectionTitle
  },
  
  data () {
    return {
      abouts: [
        {
          class: 'col-lg-4 col-md-4 col-sm-4  iq-rmb-50 ',
          value: '1520',
          title: 'App Downloads'
        },
        {
          class: 'col-lg-4 col-md-4 col-sm-4  iq-rmb-50 ',
          value: '500',
          title: 'Happy Clients'
        },
        {
          class: 'col-lg-4 col-md-4 col-sm-4 ',
          value: '110',
          title: ' Active Accounts'
        }
      ]
    }
  }
}
</script>
