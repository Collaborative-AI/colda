<template>
  <div>
    <section class="position-relative iq-gradient-bg bg-dark creative-section">
      <div class="container">
        <TitleSection title="Brand innovation And Multimedia Digital Agency" titleclass="text-white">
          <template v-slot:rightside>
            <div class="col-lg-6 col-md-6">
              <div class="btn-container">
                <a class="iq-button btn-white" href="#"><span>Explore More</span><em /></a>
              </div>
            </div>
          </template>
        </TitleSection>
      </div>
    </section>
    <div class="position-relative pt-0 overview-block-pb iq-vedio-section">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="iq-vedio-box">
              <div class="iq-asked-img position-relative">
                <img src="@/assets/images/landing-page/landing-9/video.png" class="img-fluid" alt="#">
              </div>
              <div class="play-video-two" style="visibility: visible; animation-name: rotateIn;">
                <a href="https://www.youtube.com/watch?v=0O2aH4XLbto" class="iq-video-two popup-youtube">
                <ion-icon name="play-outline"></ion-icon></a>
                <div class="iq-waves">
                    <div class="waves wave-1"></div>
                    <div class="waves wave-2"></div>
                    <div class="waves wave-3"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Brand'
}
</script>
