<template>
    <div class="about-section">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-6 p-0">
                    <div class="about-image">
                        <img src="../../assets/images/about/about-2.jpg" alt="image">
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="about-tab">
                        <h2>About Our Valzo Agency</h2>
                        <div class="bar"></div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo.</p>

                        <div class="about-list-tab">
                            <div class="tabs">
                                <ul class="tabs__header">
                                    <li 
                                        class="tabs__header-item" 
                                        v-for="tab in tabs" 
                                        v-on:click="selectTab (tab.id)" 
                                        v-bind:class="{ 'active': activeTab == tab.id }"
                                        :key="tab.id"
                                    >
                                        {{tab.name}}
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
                                            <div class="text">
                                                <h3>{{tab.title}}</h3>
                                            </div>

                                            <ul class="list">
                                                <li
                                                    v-for="list in tab.lists"
                                                    :key="list.id"
                                                >
                                                    <i :class="list.icon"></i>
                                                    The Philosophy of Business Analytics
                                                </li>
                                            </ul>

                                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.</p>

                                            <a class="default-btn" href="#">
                                                Discover More
                                            </a>
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
    name: 'About',
    data () {
        return {
            activeTab: 1,
            offsetRight: 0,

            tabs: [
                {
                    id: 1,
                    name: 'Our History',
                    title: 'How To Generate Your Creative Idea With IT Business',
                    lists: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            text: 'The Philosophy of Business Analytics',
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            text: 'Fast Track Your Business',
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            text: 'Lies & Damn Lies About Your Business',
                        },
                        {
                            id: 4,
                            icon: 'flaticon-tick',
                            text: 'The Ultimate Deal on Business',
                        },
                    ],
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    btnText: 'Discover More',
                    // btnLink: '',
                },
                {
                    id: 2,
                    name: 'Our History',
                    title: 'How To Generate Your Creative Idea With IT Business',
                    lists: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            text: 'The Philosophy of Business Analytics',
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            text: 'Fast Track Your Business',
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            text: 'Lies & Damn Lies About Your Business',
                        },
                        {
                            id: 4,
                            icon: 'flaticon-tick',
                            text: 'The Ultimate Deal on Business',
                        },
                    ],
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    btnText: 'Discover More',
                    // btnLink: '',
                },
                {
                    id: 3,
                    name: 'Our History',
                    title: 'How To Generate Your Creative Idea With IT Business',
                    lists: [
                        {
                            id: 1,
                            icon: 'flaticon-tick',
                            text: 'The Philosophy of Business Analytics',
                        },
                        {
                            id: 2,
                            icon: 'flaticon-tick',
                            text: 'Fast Track Your Business',
                        },
                        {
                            id: 3,
                            icon: 'flaticon-tick',
                            text: 'Lies & Damn Lies About Your Business',
                        },
                        {
                            id: 4,
                            icon: 'flaticon-tick',
                            text: 'The Ultimate Deal on Business',
                        },
                    ],
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan facilisis.',
                    btnText: 'Discover More',
                    // btnLink: '',
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