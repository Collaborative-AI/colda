<template>
    <li class="accordion__item">
        <div 
            class="accordion__trigger"
            :class="{'accordion__trigger_active': visible}"
            @click="open"
        >
            <slot name="accordion-trigger"></slot>
        </div>

        <transition 
            name="accordion"
            @enter="start"
            @after-enter="end"
            @before-leave="start"
            @after-leave="end"
        >
            <div 
                class="accordion__content"
                v-show="visible"
            >
                <ul>
                    <slot name="accordion-content"></slot>
                </ul>
            </div>
        </transition>
    </li>
</template>

<script>
export default {
    name: 'AccordionItem',
    props: {},
    inject: ["Accordion"],
    data() {
        return {
            index: null
        };
    },
    computed: {
        visible() {
            return this.index == this.Accordion.active;
        }
    },
    methods: {
        open() {
            if (this.visible) {
                this.Accordion.active = null;
            } else {
                this.Accordion.active = this.index;
            }
        },
        start(el) {
            el.style.height = el.scrollHeight + "px";
        },
        end(el) {
            el.style.height = "";
        }
    },
    created() {
        this.index = this.Accordion.count++;
    }
}
</script>