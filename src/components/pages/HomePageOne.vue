<template>
    <div>
        <Navbar />
        <Banner />
        <Features />
        <Creative />
        <Services />
        <Development />
        <Video />
        <Choose />
        <Projects />
        <Clients />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import Navbar from '../Layout/Navbar'
import Banner from '../HomeOne/Banner'
import Features from '../Common/Features'
import Creative from '../Common/Creative'
import Services from '../HomeOne/Services'
import Development from '../HomeOne/Development'
import Video from '../Common/Video'
import Choose from '../HomeOne/Choose'
import Projects from '../Common/Projects'
import Clients from '../Common/Clients'
import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageOne',
    components: {
        Navbar,
        Banner,
        Features,
        Creative,
        Services,
        Development,
        Video,
        Choose,
        Projects,
        Clients,
        Blog,
        Footer,
        CopyRight,
    }
}
</script>
