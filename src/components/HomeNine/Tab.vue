
<template>
    <div class="tab-section ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Outstanding Digital Experience</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidiunt  labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.</p>
                <div class="bar"></div>
            </div>

            <div class="schedule-list-tab">
                <div class="tabs">
                    <ul class="tabs__header">
                        <li 
                            class="tabs__header-item" 
                            v-for="tab in tabs" 
                            v-on:click="selectTab (tab.id)" 
                            v-bind:class="{ 'active': activeTab == tab.id }"
                            :key="tab.id"
                        >
                            {{tab.title}}
                        </li>
                    </ul>
                </div>
                <div class="tabs__container">
                    <div 
                        class="tabs__list"
                        ref='tabsList'
                    >
                        <div 
                            class="tabs__list-tab"
                            v-for="tab in tabs"
                            v-bind:class="{ 'active': activeTab == tab.id }"
                            :key="tab.id"
                        >
                            <div class="tabs_item">
                                <div class="row align-items-center">
                                    <div class="col-lg-6">
                                        <div class="tab-content">
                                            <h3>{{tab.title}}</h3>
                                            <p>{{tab.description}}</p>

                                            <div 
                                                class="tab-inner-content"
                                                v-for="inner in tab.inners"
                                                :key="inner.id"
                                            >
                                                <div class="icon">
                                                    <i :class="inner.icon"></i>
                                                    <h3>{{inner.title}}</h3>
                                                    <p>{{inner.desc}}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="col-lg-6">
                                        <div class="tab-image">
                                            <img src="../../assets/images/tab.png" alt="image">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: 'Tab',
    data () {
        return {
            activeTab: 1,
            offsetRight: 0,

            tabs: [
                {
                    id: 1,
                    icon: 'bx bx-flag',
                    title: 'Our Motivation',
                    description: '',
                    inners: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            title: 'Super Responsive',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            title: 'High Security',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            title: 'Optimal Choice',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                    ],
                    image: require('../../assets/images/tab.png')
                },
                {
                    id: 2,
                    icon: 'bx bx-flag',
                    title: 'Pay-Per-Click',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    inners: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            title: 'Super Responsive',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            title: 'High Security',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            title: 'Optimal Choice',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                    ],
                    image: require('../../assets/images/tab.png')
                },
                {
                    id: 3,
                    icon: 'bx bx-flag',
                    title: 'Online Marketing',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    inners: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            title: 'Super Responsive',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            title: 'High Security',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            title: 'Optimal Choice',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                    ],
                    image: require('../../assets/images/tab.png')
                },
                {
                    id: 4,
                    icon: 'bx bx-flag',
                    title: 'Email Marketing',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    inners: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            title: 'Super Responsive',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            title: 'High Security',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            title: 'Optimal Choice',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                    ],
                    image: require('../../assets/images/tab.png')
                },
                {
                    id: 5,
                    icon: 'bx bx-flag',
                    title: 'Social Marketing',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    inners: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            title: 'Super Responsive',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            title: 'High Security',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            title: 'Optimal Choice',
                            desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                        },
                    ],
                    image: require('../../assets/images/tab.png')
                },
            ]
        }
    },
    methods: {
        selectTab (id) {
            let tabsList = this.$refs.tabsList
            this.activeTab = id
            this.offsetRight = tabsList.clientWidth * (id - 1)
            tabsList.style.right = this.offsetRight + 'px'
        }
    },
    mounted () {
        let tabsList = this.$refs.tabsList
        tabsList.style.right = this.offsetRight + 'px'
    },
}
</script>