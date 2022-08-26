<template>
    <div>
        <Home id="iq-about"/>
        <div class="wrapper">   
        <Services id="iq-service"/>
        <Portfolio />
        <Counter />
        <Team id="iq-team"/>
        <Testimonial id="iq-testimonial"/>
        <Partner />
        <Blog id="iq-blog"/>
        </div>
    </div>
</template>
<script>

import Home from './components/home'
import Services from './components/services'
import Portfolio from './components/portfolio'
import Counter from './components/counter'
import Team from './components/team'
import Testimonial from './components/testimonial'
import Partner from './components/partner'
import Blog from './components/blog'
import {core} from '../../../config/pluginInit'
export default {
    name:'Page4',
    components:{
        Home,
        Services,
        Portfolio,
        Counter,
        Team,
        Testimonial,
        Partner,
        Blog,
    },
    mounted(){
        core.index()
    }
}
</script>