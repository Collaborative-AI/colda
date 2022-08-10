<template>
    <div>
        <Home />
        <div class="wrapper">
        <Partner />
        <About id="iq-about"/>
        <Services id="iq-service"/>
        <Subscribe />
        <Testimonial id="iq-testimonial"/>
        <Portfolio />
        <Background />
        <Team id="iq-team"/>
        <Brand />
        <Blog id="iq-blog"/>
        </div>
    </div>
</template>
<script>

import {core} from '../../../config/pluginInit'
import Home from './components/home'
import Partner from './components/partner'
import About from './components/about'
import Services from './components/services'
import Subscribe from './components/subscribe'
import Testimonial from './components/testimonial'
import Portfolio from './components/portfolio'
import Background from './components/background'
import Brand from './components/brand'
import Blog from './components/blog'
import Team from './components/team'
export default {
    name:'Page9',
    components:{
        Home,
        Partner,
        About,
        Services,
        Subscribe,
        Testimonial,
        Portfolio,
        Background,
        Brand,
        Blog,
        Team
    },
     mounted(){
        core.index()
    }
}
</script>