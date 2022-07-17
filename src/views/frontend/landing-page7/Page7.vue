<template>
    <div>
        <Home />
        <div class="wrapper">
        <div class="main-content">
        <EduVideo />
        <Specializing1 />
        <Specializing2 />
        <AboutMe />
        <Categories id="iq-categories"/>
        <Team id="iq-team"/>
        <Partner />
        <Testimonials id="iq-testimonial"/>
        <Blog id="iq-blog"/>
        </div>
        </div>
    </div>
</template>
<script>
import {core} from '../../../config/pluginInit'
import Home from './components/home'
import Specializing1 from './components/specializing1'
import Specializing2 from './components/specializing2'
import EduVideo from './components/eduvideo'
import AboutMe from './components/aboutme'
import Categories from './components/categories'
import Team from './components/team'
import Partner from './components/partner'
import Testimonials from './components/testimonials'
import Blog from './components/blog'
export default {
    name:'Page7',
    components:{
        Home,
        EduVideo,
        Specializing1,
        Specializing2,
        AboutMe,
        Categories,
        Team,
        Partner,
        Testimonials,
        Blog,
    },
    mounted(){
        core.index()
    }
}
</script>