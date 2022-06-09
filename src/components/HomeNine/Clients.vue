<template>
    <div class="clients-section pb-100">
        <div class="container">
            <div class="section-title">
                <h2>What Our Clients Say</h2>
                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p> -->
                <div class="bar"></div>
            </div>

            <div class="clients-slider">
                <!-- <carousel 
                    :autoplay="5000"
                    :settings="settings"
                    :wrap-around="true"
                    :breakpoints="breakpoints"
                > -->
                <carousel 
                    :autoplay="5000"
                    :settings="settings"
                    :wrap-around="true"
                >
                    <slide 
                        v-for="slide in carouselItems" 
                        :key="slide.id"
                    >
                        <div class="clients-item">
                            <div class="icon">
                                <i :class="slide.icon"></i>
                            </div>

                            <p>{{slide.description}}</p>

                            <div class="clients-content">
                                <h3>{{slide.name}}</h3>
                                <span>{{slide.position}}</span>
                            </div>
                        </div>
                    </slide>
                    
                    <template #addons>
                        <Pagination />
                    </template>
                </carousel>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { Carousel, Slide, Pagination } from 'vue3-carousel';

import 'vue3-carousel/dist/carousel.css';

export default defineComponent ({
    name: 'Clients',
    components: {
        Carousel,
        Slide,
        Pagination,
    },
    data: () => ({
        carouselItems: [
            {
                id: 1,
                icon: 'flaticon-left-quotes-sign',
                description: 'Don’t see a need for large corporations, many big companies will have their software developers make tools for data ingesting, sharing and analysis. They have or they can buy data. (Run out of time here for full answer).Large companies have data scientist team that could incorporate SynSpot Python API but also for small/medium size companies that have no data science teams.',
                name: 'UMN Alumni',
                position: 'CVS - Data Scientist',
            },
            {
                id: 2,
                icon: 'flaticon-left-quotes-sign',
                description: 'Internal Data is shared within the Data Analytics team and within the organization. Reports are given to coaches directly as well as R and PowerBI Reports. Data sharing via competitors is difficult but some ‘data exchanges’ have been made. These have to be negotiated by the higher ups and need to be like for like. Any models cannot be a black box, need to be explainable to the end users as well as have insight into the data',
                name: 'UMN Alumni',
                position: 'Minnesota Twins - Sports Science Analyst',
            },
            {
                id: 3,
                icon: 'flaticon-left-quotes-sign',
                description: 'Sharing data is a data governance and IT issue as well (He currently only works with internal data). Although sharing data between departments and doing a cross-functional model may be of use. ',
                name: 'UMN Alumni',
                position: 'Disney Hulu - Data Analyst',
            },
        ],
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
    }),
})
</script>
