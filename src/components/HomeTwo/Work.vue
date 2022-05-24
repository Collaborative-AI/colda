<template>
    <div>
        <div class="work-section pb-100">
            <div class="container-fluid">
                <div class="row align-items-center">
                    <div class="col-lg-6">
                        <div class="work-content">
                            <h3>Brainstorming, <span>Researching</span> Planning, Strategizing Work</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed dood tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas.</p>

                            <div class="row">
                                <div class="col-lg-6">
                                    <div class="work-status">
                                        <h3>
                                            50K
                                        </h3>
                                        <h4>Completed Project</h4>
                                        <p>Lorem ipsum dolor sit amet consectetur do eiusmod tempor incididunt ut labore et dolore.</p>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="work-status">
                                        <h3>
                                            98%
                                        </h3>
                                        <h4>Customer Satisfaction</h4>
                                        <p>Lorem ipsum dolor sit amet consectetur do eiusmod tempor incididunt ut labore et dolore.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-6 pr-0">
                        <div class="work-image">
                            <img src="../../assets/images/work-bg.jpg" alt="image">

                            <div class="work-video">
                                <div
                                    class="video-btn popup-youtube"
                                    v-on:click="isPopupMethod(isPopup)"
                                    style="cursor: pointer"
                                >
                                    <i class="flaticon-play"></i>
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
    name: 'Work',
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