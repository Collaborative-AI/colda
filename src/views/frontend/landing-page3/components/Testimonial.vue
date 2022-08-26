<template>
  <section id="testimonial" class="iq-testimonial pt-0">
    <div class="container p-0">
      <div class="row no-gutters">
        <div class="col-sm-12">
          <div class="title-box text-center">
            <h6 class="title text-white">
              Testimonial
            </h6>
            <h2 class="text-white">
              What Client Say
            </h2>
          </div>
        </div>
      </div>
      <div class="row no-gutters">
        <div
          class="owl-carousel owl-theme owl-loaded"
          data-dots="true"
          data-nav="false"
          data-items="1"
          data-xs-items="1"
          data-sm-items="1"
          data-md-items="1"
          data-lg-items="1"
          data-autoplay="true"
        >
          <BlackCardStyle5>
            <template v-slot:cardBody>
              "Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat.Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat."
            </template>
            <template v-slot:cardMedia>
              <img src="@/assets/images/landing-page/landing-3/16.jpg" class="img-fluid mb-5 img-shap " alt="">
            </template>
            <template v-slot:cardFooter>
              <h4>Kips Leo</h4>
              <p>CEO - prox</p>
            </template>
          </BlackCardStyle5>
          <BlackCardStyle5>
            <template v-slot:cardBody>
              "Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat.Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat."
            </template>
            <template v-slot:cardMedia>
              <img src="@/assets/images/landing-page/landing-3/17.jpg" class="img-fluid mb-5 img-shap " alt="">
            </template>
            <template v-slot:cardFooter>
              <h4>Kips Leo</h4>
              <p>CEO - prox</p>
            </template>
          </BlackCardStyle5>
          <BlackCardStyle5>
            <template v-slot:cardBody>
              "Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat.Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat."
            </template>
            <template v-slot:cardMedia>
              <img src="@/assets/images/landing-page/landing-3/18.jpg" class="img-fluid mb-5 img-shap " alt="">
            </template>
            <template v-slot:cardFooter>
              <h4>Kips Leo</h4>
              <p>CEO - prox</p>
            </template>
          </BlackCardStyle5>
          <BlackCardStyle5>
            <template v-slot:cardBody>
              "Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat.Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat."
            </template>
            <template v-slot:cardMedia>
              <img src="@/assets/images/landing-page/landing-3/19.jpg" class="img-fluid mb-5 img-shap " alt="">
            </template>
            <template v-slot:cardFooter>
              <h4>Kips Leo</h4>
              <p>CEO - prox</p>
            </template>
          </BlackCardStyle5>
          <BlackCardStyle5>
            <template v-slot:cardBody>
              "Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat.Progravida nibh vel velit auctor alinean sollicitudin, lorem quis bibendum auctor, nisi elit consequat."
            </template>
            <template v-slot:cardMedia>
              <img src="@/assets/images/landing-page/landing-3/20.jpg" class="img-fluid mb-5 img-shap " alt="">
            </template>
            <template v-slot:cardFooter>
              <h4>Kips Leo</h4>
              <p>CEO - prox</p>
            </template>
          </BlackCardStyle5>
        </div>
      </div>
    </div>
  </section>
</template>
<script>

import BlackCardStyle5 from '../../../../components/frontend/cards/BlackCardStyle5'
export default {
  name: 'Testimonial',
  components:{BlackCardStyle5}
}
</script>
