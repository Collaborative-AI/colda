<template>
    <accordion>
        <accordion-item>
            <template v-slot:accordion-trigger>
                <button class="accordion-title">
                    <i class="bx bx-plus"></i>
                    Which material types can you work with?
                </button>
            </template>
            <template v-slot:accordion-content>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
            </template>
        </accordion-item>
        <accordion-item>
            <template v-slot:accordion-trigger>
                <button class="accordion-title">
                    <i class="bx bx-plus"></i>
                    Is Smart Lock required for instant apps?
                </button>
            </template>
            <template v-slot:accordion-content>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
            </template>
        </accordion-item>
        <accordion-item>
            <template v-slot:accordion-trigger>
                <button class="accordion-title">
                    <i class="bx bx-plus"></i>
                    Why Choose Our Services In Your Business?
                </button>
            </template>
            <template v-slot:accordion-content>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
            </template>
        </accordion-item>
    </accordion>
</template>

<script>
import Accordion from "../Common/Accordion";
import AccordionItem from "../Common/AccordionItem";

export default {
    name: 'ServicesAccordion',
    components: {
        Accordion,
        AccordionItem
    }
}
</script>