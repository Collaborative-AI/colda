<template>
    <div class="main-banner-area">
        <div class="home-sliders">
            <carousel 
                :autoplay="5000"
                :settings="settings"
                :wrap-around="true"
                :breakpoints="breakpoints"
            >
                <slide 
                    v-for="slide in carouselItems" 
                    :key="slide.id"
                >
                    <div :class="slide.class">
                        <div class="d-table">
                            <div class="d-table-cell">
                                <div class="container">
                                    <div class="main-banner-content">
                                        <h1>{{slide.heading}}</h1>
                                        <p>{{slide.description}}</p>
                                        <div class="banner-btn">
                                            <router-link :to="slide.btnLink" class="default-btn">
                                                {{slide.btnText}}
                                            </router-link>
                                        </div>
                                    </div>

                                    <div class="banner-image">
                                        <img src="../../assets/images/shapes/shape-11.png" alt="image">

                                        <img :src="slide.image" class="banner-img" alt="image">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </slide>

                <template #addons>
                    <Pagination />
                </template>
            </carousel>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { Carousel, Slide, Pagination } from 'vue3-carousel';

import 'vue3-carousel/dist/carousel.css';

export default defineComponent ({
    name: 'Banner',
    components: {
        Carousel,
        Slide,
        Pagination,
    },
    data: () => ({
        carouselItems: [
            {
                id: 1,
                class: 'home-item item-bg1',
                heading: 'Make Real-Life Connections With IT',
                description: 'Lorem ipsum dolor sit amet, consectetur adipiscing incididunt ut laboredolore magna aliqua elsed  tempomet, consectetur adipiscing.',
                btnLink: '/contact',
                btnText: 'Get Started',
                image: require('../../assets/images/image-1.png')
            },
            {
                id: 2,
                class: 'home-item item-bg2',
                heading: 'Make Real-Life Connections With IT',
                description: 'Lorem ipsum dolor sit amet, consectetur adipiscing incididunt ut laboredolore magna aliqua elsed  tempomet, consectetur adipiscing.',
                btnLink: '/contact',
                btnText: 'Get Started',
                image: require('../../assets/images/image-2.png')
            },
            {
                id: 3,
                class: 'home-item item-bg3',
                heading: 'Make Real-Life Connections With IT',
                description: 'Lorem ipsum dolor sit amet, consectetur adipiscing incididunt ut laboredolore magna aliqua elsed  tempomet, consectetur adipiscing.',
                btnLink: '/contact',
                btnText: 'Get Started',
                image: require('../../assets/images/image-3.png')
            },
        ],
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
    }),
})
</script>