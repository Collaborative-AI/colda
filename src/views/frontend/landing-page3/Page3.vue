<template>
    <div>
        <Home />
        <div class="wrapper">
        <div class="main-content " >
            <HowItWork id="iq-service" />
            <AboutUs id="iq-about" />
            <AboutFeature />
            <WhyChooseUs />
            <Feature id="iq-feature" />
            <Screenshotslider />
            <Team id="iq-team" />
            <Testimonial id="iq-testimonial" />
            <Pricing id="iq-pricing" />
            <Blog id="iq-blog" />
            <Clients />
        </div>
        </div>
    </div>
</template>
<script>
import {core} from '../../../config/pluginInit'
import Home from './components/Home'
import HowItWork from './components/HowItWork'
import AboutUs from './components/AboutUs'
import AboutFeature from './components/AboutFeature'
import WhyChooseUs from './components/WhyChooseUs'
import Feature from './components/Feature'
import Screenshotslider from './components/screenshotslider'
import  Team from './components/Team'
import  Testimonial from './components/Testimonial'
import Pricing from './components/Pricing'
import Blog from './components/Blogs'
import Clients  from './components//Client'
export default {
  
    name:'Page3',
    components: { Home,HowItWork,AboutUs,AboutFeature,WhyChooseUs,Feature,Screenshotslider ,Team ,Testimonial,Pricing,Blog,Clients },mounted(){
        core.index()
    }
}
</script>