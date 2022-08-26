<template>
    <div>
        <Home />
        <div classs="wrapper">
            <div class="main-content">
            <Speakers />
            <About id="iq-about"/>
            <EventSchedule />
            <Event id="iq-event"/>
            <Package id="iq-pricing"/>
            <Testimonials id="iq-testimonial"/>
            <Clients id="iq-client"/>
            </div>
        </div>
    </div>
</template>
<script>
import {core} from '../../../config/pluginInit'
import Home from './components/home'
import Speakers from './components/speakers'
import About from './components/about'
import EventSchedule from './components/eventschedule'
import Event from './components/event'
import Package from './components/package'
import Testimonials from './components/testimonials'
import Clients from './components/clients'

export default {
    name:'Page5',
    components:{
        Home,
        Speakers,
        About,
        EventSchedule,
        Event,
        Package,
        Testimonials,
        Clients
    },
    mounted(){
        core.index()
    }
}
</script>