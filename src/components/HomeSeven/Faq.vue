<template>
    <div class="faq-section pb-100">
        <div class="container">
            <div class="section-title" style = "margin-top:45px">
                <h2 style = "font-size: 45px;">Frequently <span>Asked</span> Questions</h2>
                <p style = "font-size: 20px;">Check some common questions about us!</p>
                <div class="bar"></div>
            </div>

            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="faq-image">
                        <img src="../../assets/images/faq.png" alt="image">
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <div class="faq-accordion">
                        <accordion>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title" style = "font-size: 20px;">
                                        What's The Difference Between IDS And IBS?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>
                                        Synspot provides Distributed Machine Learning as a Service (DMLasS) via Collaborative Data Analysis (ColDA) to form a machine learning community of shared interest. Synspot enables collaborators to conjointly learn machine learning models without sharing their data, models, and objectives with each other. 
                                    </p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title" style = "font-size: 20px;">
                                        What is Collaborative Data Analysis (ColDA)? 
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>
                                        Collaborative Data Analysis (ColDA) is a distributed generalization of the well-known Gradient Boosting algorithm which allows participants to collaboratively optimize the aggregate of local loss functions. Each participant autonomously builds its own model by iteratively fitting the pseudo-residuals.
                                    </p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title" style = "font-size: 20px;">
                                        What are the advantages of Collaborative Data Analysis (ColDA)?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>
                                        ColDA leverages local resources from participants to utilize the predictive power of external data and reduce computation overhead.
                                        ColDA generalizes the classical Gradient Boosting algorithm and allows participants to improve machine learning models without necessarily trusting each other.
                                        ColDA outperforms learning baselines and achieves near-oracle performance on various benchmark datasets. It applies to several real-world use cases such as recommender systems and time-series forecasting.
                                    </p>
                                </template>
                            </accordion-item>
                            <accordion-item>
                                <template v-slot:accordion-trigger>
                                    <button class="accordion-title" style = "font-size: 20px;">
                                        How to get started with Collaborative Data Analysis (ColDA)?
                                        <span></span>
                                        <i class='bx bx-chevron-down'></i>
                                    </button>
                                </template>
                                <template v-slot:accordion-content>
                                    <p>
                                        Sponsor: A sponsor initiates a learning task and asks for assistance from Assistors.
                                        Assistor: An assistor provides assistance for a sponsor by locally fitting the pseudo-residuals of the sponsor’s target.
                                        We provide UI/UX enabled software for quick-start and demonstration. 
                                        Users who are familiar with data science can directly start with our open-source Python API ColDA. We also provide use cases and documentation of ColDA.
                                    </p>
                                </template>
                            </accordion-item>
                        </accordion>
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