<template>
  <div>
    <section class="position-relative pb-0 iq-portfolio-titlebox creative-section">
      <div class="container">
        <TitleSection title=" Check Some Our View Recent Works " subclass="pr-lg-5">
          <template v-slot:rightside>
            <div class="col-lg-6 col-md-6">
              <div class="btn-container">
                <a class="iq-button iq-gradient-btn" href="#"><span>Click Here</span><em /></a>
              </div>
            </div>
          </template>
        </TitleSection>
      </div>
    </section>

    <div class="position-relative  overview-block-pb ">
      <div class="container-fluid p-0 overflow-hidden">
        <div class="row justify-content-sm-center">
          <div class="col-sm-12">
            <Swiper id="post-slider" :option="options">
              <SwiperSlide class="d-flex align-items-center">
                <div class="iq-portfolio-block">
                    <a href="#"><img src="@/assets/images/landing-page/landing-9/portfolio-d2-1.jpg" class="img-fluid" alt="#"></a>
                </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-2.jpg" class="img-fluid" alt="#"></a>
                </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-3.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-1.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-2.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-3.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-1.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-2.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
              <SwiperSlide class="d-flex align-items-center">
                 <div class="iq-portfolio-block">
                    <a href="#"> <img src="@/assets/images/landing-page/landing-9/portfolio-d2-3.jpg" class="img-fluid" alt="#"></a>
                  </div>
              </SwiperSlide>
            </Swiper>
            <div />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Swiper from '../../../../components/slider/Swiper'
import SwiperSlide from '../../../../components/slider/SwiperSlide'
export default {
  name: 'Portfolio',
  components: {
    Swiper,
    SwiperSlide
  },
  data(){
    return{
       options: {
        centeredSlides: false,
        loop: true,
        slidesPerView: 1,
        autoplay: {
          delay: 4000
        },
        spaceBetween: 30,
        breakpoints: {
          320: {
            slidesPerView: 1
            
          },
          
          480: {
            slidesPerView: 1
           
          },
          
          640: {
            slidesPerView: 1
            
          },
          768: {
            slidesPerView: 1
            
          },
          1024: {
            slidesPerView: 2
            
          }
        },
        pagination: {
          el: '.swiper-pagination'
        },

        // Navigation arrows
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        },

        // And if we need scrollbar
        scrollbar: {
          el: '.swiper-scrollbar'
        }
      }
    }
  }
}
</script>
