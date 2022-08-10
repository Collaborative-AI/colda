<template>
  <section class="iq-about-us position-relative iq-rpt-0">
    <div class="container ">
      <div class="row">
        <div class="col-lg-6 align-self-center">
          <BlackSectionTitle2 title="About Us" subtitle="Why Choose Us?" titlecontent="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or " />

          <div class="row">
           <a class="landing-button btn-primary" href="#">Read More</a>
          </div>
        </div>
        <div class="col-lg-6" />
      </div>
      <div class="right-image wow slideInRight">
        <img src="@/assets/images/landing-page/landing-3/03.png" class="img-fluid" alt="images">
      </div>
    </div>
  </section>
</template>
<script>
import BlackSectionTitle2 from '../../../../components/frontend/title/BlackSectionTitle'
export default {
  name: 'WhyChooseUs',
   components:{
    BlackSectionTitle2
  },
}
</script>
