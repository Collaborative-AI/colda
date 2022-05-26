<template>
    <div class="clients-section bg-background ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Start Your Data Journey With<span> SynSpot</span> </h2>
                <p></p>
                <div class="bar"></div>
            </div>

            <div class="clients-slider">
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
                description: 'All participants collaboratively optimize the aggregate of local loss functions, and each participant autonomously builds its own model by iteratively fitting the gradients of the objective function',
                name: 'Software Developer',
                position: '',
            },
            {
                id: 2,
                icon: 'flaticon-left-quotes-sign',
                description: 'SynSpot is an open-source innovation which can keep pace with your needs and business challenges.',
                name: 'Software Developer',
                position: '',
            },
            {
                id: 3,
                icon: 'flaticon-left-quotes-sign',
                description: 'You will ready to solve problems in your daily life',
                name: 'Software Developer',
                position: '',
            },
        ],

       
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
    }),
    
})

</script>
