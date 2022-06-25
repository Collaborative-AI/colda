<template>
    <div class="clients-section bg-background ptb-100">
        <div class="container">
            <div class="section-title">
                <h2 style = "font-size: 45px;">What Our Clients Say</h2>
                <p></p>
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
                icon: 'flaticon-happy',
                description: 'We have more than lots of partners. A few years ago we tried to use blockchain to leverage scattered data, but not very successful. Anything that can improve the assessment of risk is useful for us. So we collaborate a lot with other organizations. Everybody does not trust another. For example, payers don’t trust service providers. It would be great if any product can resolve trust issues.',
                name: 'UnitedHealth',
                position: 'Healthcare Insurance',
            },
            {
                id: 2,
                icon: 'flaticon-technical-support',
                description: 'We use API to share data with other insurance companies. There are expensive procedures that require prior authorization. Agreement for multiple parties must be constantly settled.',
                name: 'Anthem',
                position: 'Healthcare Insurance',
            },
            {
                id: 3,
                icon: 'flaticon-quality',
                description: 'It is not possible to dive into the data market in a short amount of time. We need a recommendation on what external data would be useful.',
                name: 'CVS Health',
                position: 'Pharmacy',
            },
            {
                id: 4,
                icon: 'flaticon-left-quotes-sign',
                description: 'Data sharing via competitors is difficult but some ‘data exchanges’ have been made.',
                name: 'G&M Health',
                position: 'Health and Life-science Service',
            },
        ],

       
        settings: {
            itemsToShow: 1,
            snapAlign: 'center',
        },
    }),
    
})

</script>
