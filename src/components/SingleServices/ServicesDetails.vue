<template>
    <div>
        <div class="services-details-area ptb-100">
            <div class="container">
                <div class="services-details-video">
                    <div class="details-image">
                        <img src="../../assets/images/services-details-bg.jpg" alt="image">
                    </div>

                    <div class="details-video">
                        <div
                            class="video-btn popup-youtube"
                            v-on:click="isPopupMethod(isPopup)"
                            style="cursor: pointer"
                        >
                            <i class="bx bx-play"></i>
                        </div>
                    </div>

                    <div class="text">
                        <h3>We Provide Useful Services</h3>
                        <p>Quuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quia non numquam eius modi tempora incidunt ut labore et dolore magnam dolor sit amet, consectetur.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                    </div>
                </div>

                <div class="services-details-overview">
                    <div class="row align-items-center">
                        <div class="col-lg-6 col-md-12">
                            <div class="services-details-desc">
                                <h3>Exceptional Best Products</h3>
                                <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.</p>

                                <div class="features-text">
                                    <h4>Reasons to Go with vegetables</h4>
                                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's.</p>
                                </div>

                                <div class="features-text">
                                    <h4>Summer Vegetables Fruits Collection</h4>
                                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's.</p>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6 col-md-12">
                            <div class="services-details-image">
                                <img src="../../assets/images/services-details-1.jpg" alt="image">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="services-details-overview">
                    <div class="row align-items-center">
                        <div class="col-lg-6 col-md-12">
                            <div class="services-details-image">
                                <img src="../../assets/images/services-details-2.jpg" alt="image">
                            </div>
                        </div>

                        <div class="col-lg-6 col-md-12">
                            <div class="services-details-desc">
                                <h3>We Provide Useful Services</h3>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's.</p>

                                <div class="services-details-accordion">
                                    <ServicesAccordion />
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
import ServicesAccordion from '../SingleServices/ServicesAccordion'

export default {
    name: 'ServicesDetails',
    components: { 
        ServicesAccordion
    },
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