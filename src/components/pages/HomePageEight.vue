<template>
    <div>
        <NavbarStyleTwo />
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
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeEight/Banner'
import Features from '../HomeEight/Features'
import Creative from '../Common/Creative'
import Services from '../HomeEight/Services'
import Development from '../HomeEight/Development'
import Video from '../Common/Video'
import Choose from '../HomeEight/Choose'
import Projects from '../Common/Projects'
import Clients from '../Common/Clients'
import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageEight',
    components: {
        NavbarStyleTwo,
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