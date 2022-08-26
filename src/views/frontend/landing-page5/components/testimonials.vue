<template>
         <section id="iq-testimonial" class="iq-section-space">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="iq-title-box text-center mb-5 wow fadeInUp" data-wow-delay=".3s">
                            <span class="iq-subtitle text-uppercase font-weight-bold text-danger position-relative">Client
                                Feedback</span>
                            <h2 class="iq-title text-dark"> Testimonial </h2>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-sm-center">
                    <div class="col-sm-10">
                        <div class="owl-carousel" data-autoplay="true" data-loop="true" data-nav="false" data-dots="true"
                            data-items="1" data-items-laptop="1" data-items-tab="1" data-items-mobile="1"
                            data-items-mobile-sm="1" data-margin="30">
                            <div class="item">
                                <div class="iq-testimonial text-center wow fadeInUp" data-wow-delay=".6s">
                                    <h5>The point of using Lorem Ipsum is that it has a more-or-less normal distribution of
                                        letters, as opposed to using 'Content here, content here', making it look like
                                        readable English.</h5>
                                    <div class="d-inline-block">
                                        <div class="d-flex mt-4 align-items-center">
                                            <div class="testimonial-img">
                                                <img class="rounded-circle"
                                                    src="@/assets/images/landing-page/landing-5/testimonial-img1.jpg"
                                                    alt="#">
                                            </div>
                                            <div class="testimonial-name ml-3 text-left">
                                                <h5 class="text-dark">John Deo</h5>
                                                <p class="mb-0 text-danger">CEO - {{ appName }}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="iq-testimonial text-center wow fadeInUp" data-wow-delay=".9s">
                                    <h5>The point of using Lorem Ipsum is that it has a more-or-less normal distribution of
                                        letters, as opposed to using 'Content here, content here', making it look like
                                        readable English.</h5>
                                    <div class="d-inline-block">
                                        <div class="d-flex mt-4 align-items-center">
                                            <div class="testimonial-img">
                                                <img class="rounded-circle"
                                                    src="@/assets/images/landing-page/landing-5/testimonial-img2.jpg"
                                                    alt="#">
                                            </div>
                                            <div class="testimonial-name ml-3 text-left">
                                                <h5 class="text-dark">Marcash Dane</h5>
                                                <p class="mb-0 text-danger">CEO - {{ appName }}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="iq-testimonial text-center wow fadeInUp" data-wow-delay="1.2s">
                                    <h5>The point of using Lorem Ipsum is that it has a more-or-less normal distribution of
                                        letters, as opposed to using 'Content here, content here', making it look like
                                        readable English.</h5>
                                    <div class="d-inline-block">
                                        <div class="d-flex mt-4 align-items-center">
                                            <div class="testimonial-img">
                                                <img class="rounded-circle"
                                                    src="@/assets/images/landing-page/landing-5/testimonial-img3.jpg"
                                                    alt="#">
                                            </div>
                                            <div class="testimonial-name ml-3 text-left">
                                                <h5 class="text-dark">Greta Life</h5>
                                                <p class="mb-0 text-danger">CEO - {{ appName }}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="iq-testimonial text-center wow fadeInUp" data-wow-delay="1.5s">
                                    <h5>The point of using Lorem Ipsum is that it has a more-or-less normal distribution of
                                        letters, as opposed to using 'Content here, content here', making it look like
                                        readable English.</h5>
                                    <div class="d-inline-block">
                                        <div class="d-flex mt-4 align-items-center">
                                            <div class="testimonial-img">
                                                <img class="rounded-circle"
                                                    src="@/assets/images/landing-page/landing-5/testimonial-img4.jpg"
                                                    alt="#">
                                            </div>
                                            <div class="testimonial-name ml-3 text-left">
                                                <h5 class="text-dark">Petey Cruiser</h5>
                                                <p class="mb-0 text-danger">CEO - {{ appName }}</p>
                                            </div>
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
    name:'Testimonials',
    data(){
        return{
        appName:'ProX',
   } },
}
</script>