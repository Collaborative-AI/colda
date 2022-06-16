

<template>
    <div class="faq-section pb-100">
        <div class="container">
            <div class="section-title">
                <h2>Frequently <span>Asked</span> Questions</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                <div class="bar"></div>
            </div>


            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="faq-accordion">
                        <accordion>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title">
                                        What Is Distributed Machine Learning And Why It Is Used?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title">
                                        What's The Difference Between Gradient Assistant Learning And Federal Assistant Learning?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title">
                                        How Is Software Different From API?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title">
                                        What Steps Will You Take To Secure Our Data?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                                </template>
                            </accordion-item>
                        </accordion>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="faq-image">
                        <img src="../../assets/images/faq.png" alt="image">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Accordion from "../Common/Accordion";
import AccordionItem from "../Common/AccordionItem";

export default {
    name: 'Faq',
    components: {
        Accordion,
        AccordionItem
    }
}
</script>