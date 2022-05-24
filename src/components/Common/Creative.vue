<template>
    <div>
        <div class="creative-section pb-100">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6">
                        <div class="creative-content">
                            <h3>How to Generate <span>Creative</span> Ideas for your IT Business</h3>
                            <div class="bar"></div>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt  labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus do  umsan lacus vel facilisis.Lorem Ipsum is simply dummy text of the industry. Lorem Ipsum has been the industry's.</p>
                        </div>

                        <div class="progress-content">
                            <div class="progress-text">
                                <span>Development</span>
                                <p>75%</p>
                            </div>

                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 75%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>

                        <div class="progress-content">
                            <div class="progress-text">
                                <span>Branding Design</span>
                                <p>45%</p>
                            </div>

                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 45%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>

                        <div class="progress-content">
                            <div class="progress-text">
                                <span>SEO & Digital Marketing</span>
                                <p>80%</p>
                            </div>

                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 80%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>

                        <div class="progress-content">
                            <div class="progress-text">
                                <span>SEO & Digital Marketing</span>
                                <p>70%</p>
                            </div>

                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 70%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>

                        <div class="progress-content">
                            <div class="progress-text">
                                <span>SEO & Digital Marketing</span>
                                <p>90%</p>
                            </div>

                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 90%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-6">
                        <div class="creative-image">
                            <img src="../../assets/images/about/about.jpg" alt="image">

                            <div class="creative-video">
                                <div
                                    class="video-btn popup-youtube"
                                    v-on:click="isPopupMethod(isPopup)"
                                    style="cursor: pointer"
                                >
                                    <i class="bx bx-play"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div 
            class="popup-video" 
            v-if="isPopup"
        >
            <div class="d-table">
                <div class="d-table-cell">
                    <div 
                        class="popup-overlay-close"
                        v-on:click="isPopupMethod(isPopup)"
                    >
                        <div class="popup-overlay-close-line"></div>
                        <div class="popup-overlay-close-line"></div>
                    </div>
                    <div class="play-video">
                        <iframe src="https://www.youtube.com/embed/bk7McNUjWgw"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Creative',
    data (){
        return {
            isPopup: false,
        }
    },
    methods: {
        isPopupMethod(isPopup){
            return this.isPopup = !isPopup
        },
    },
}
</script>