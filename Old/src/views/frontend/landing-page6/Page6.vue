<template>
    <div>
        <Home />
        <div class="wrapper">
        <div class="main-content">
            <WhyChooseUs />
            <Quality />
            <AboutUs id="iq-about"/>
            <Service id="iq-service"/>
            <Counter />
            <GetStarted />
            <Process id="iq-process"/>
            <Testimonials id="iq-testimonial"/>
            <Blog id="iq-blog"/>
            <Client />
        </div>  
    </div>
    </div>
</template>
<script>
import {core} from '../../../config/pluginInit'
import Home from './components/home'
import AboutUs from './components/aboutus'
import WhyChooseUs from './components/whychooseus'
import Quality from './components/quality'
import Service from './components/services'
import Counter from './components/counter'
import GetStarted from './components/getstarted'
import Process from './components/process'
import Testimonials from './components/testimonials'
import Blog from './components/blog'
import Client from './components/client'

export default {
    name:'Page6',
    components:{
        Home,
        WhyChooseUs,
        Quality,
        AboutUs,
        Service,
        Counter,
        GetStarted,
        Process,
        Testimonials,
        Blog,
        Client
    },
     mounted(){
        core.index()
    }
}
</script>