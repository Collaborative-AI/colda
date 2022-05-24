<template>
    <div class="main-banner-area-nine">
        <div class="container-fluid">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="main-banner-content">
                        <span>Digital Marketing</span>
                        <h1>Digital Service With Excellent Quality</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing incididunt ut laboredolore magna aliqua elsed  tempomet, consectetur adipiscing.</p>
                        <div class="banner-btn">
                            <a href="#" class="default-btn">Get Started</a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6 pr-0">
                    <div class="image-sliders">
                        <carousel 
                            :autoplay="5000"
                            :settings="settings"
                            :wrap-around="true"
                            :breakpoints="breakpoints"
                        >
                            <slide v-for="slide in carouselItems" :key="slide.id">
                                <div class="image-item">
                                    <img :src="slide.image" alt="image">
                                </div>
                            </slide>
                            
                            <template #addons>
                                <Navigation />
                            </template>
                        </carousel>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { Carousel, Slide, Navigation } from 'vue3-carousel';

import 'vue3-carousel/dist/carousel.css';

export default defineComponent ({
    name: 'Banner',
    components: {
        Carousel,
        Slide,
        Navigation,
    },
    data: () => ({
        carouselItems: [
            {
                id: 1,
                image: require('../../assets/images/slider1.jpg'),
            },
            {
                id: 2,
                image: require('../../assets/images/slider2.jpg'),
            },
            {
                id: 3,
                image: require('../../assets/images/slider3.jpg'),
            },
        ],
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
    }),
})
</script>