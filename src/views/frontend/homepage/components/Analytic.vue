<template>
  <section class="iq-section-space iq-feture-bg overflow-hidden">
    <div class="container ">
      <div class="row align-items-center ">
        <div class="col-md-6">
          <div class="title-box wow fadeInUp pr-lg-5 text-left" data-wow-delay=".3s" >
            <span class="title-design"></span>
            <h2>The Perfect Application for Beginners or Professionals</h2>
            <p>Synspot is a carefully crafted multi-purpose, responsive, and gorgeous application built with Vue.js and Python. It comes with the features you need to quickly start your data analysis, optimize your AI model cooperatively with others without sharing local data.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="prox-feature-circle wow zoomIn postion-relative">
            <div class="prox-img">
              <ul class="list-inline mb-0">
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/16.png')" alt="image0"></div>
                    <h6>Business performance</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/17.png')" alt="image1"></div>
                    <h6>Predict behavior</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/18.png')" alt="image2"></div>
                    <h6>Drive strategic</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/19.png')" alt="image3"></div>
                    <h6>Business performance</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/18.png')" alt="image4"></div>
                    <h6>Understand customers</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/19.png')" alt="image5"></div>
                    <h6>Predict behavior</h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/18.png')" alt="image6"></div>
                    <h6>Identify trends </h6>
                  </div>
                </li>
                <li class="list-inline-item">
                  <div class="feature-info">
                    <div class="feature-img"><img class="img-fluid client-img" :src="require('@/assets/images/landing-page/landing-8/16.png')" alt="image7"></div>
                    <h6>insights into data</h6>
                  </div>
                </li>
              </ul>
              <div class="dot-circle">
                <div class="effect-circle"></div>
              </div>
              <div class="main-circle">
                <div class="circle-bg">
                  <img :src="require('@/assets/images/logo-white.png')" alt="image">
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
  name: 'Analytic',
}
</script>