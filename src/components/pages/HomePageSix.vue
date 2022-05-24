<template>
    <div>
        <NavbarStyleTwo />
        <Banner />
        <MoreFeatures />
        <Work />
        <Digital />
        <Services />
        <Experience />
        <Projects />
        <Team />
        <Skills />
        <Contact />
        <Clients />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeSix/Banner'
import MoreFeatures from '../HomeSix/MoreFeatures'
import Work from '../HomeSix/Work'
import Digital from '../HomeSix/Digital'
import Services from '../HomeSix/Services'
import Experience from '../HomeSix/Experience'
import Projects from '../Common/Projects'
import Team from '../HomeSix/Team'
import Skills from '../HomeSix/Skills'
import Contact from '../HomeSix/Contact'
import Clients from '../HomeSix/Clients'
import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageSix',
    components: {
        NavbarStyleTwo,
        Banner,
        MoreFeatures,
        Work,
        Digital,
        Services,
        Experience,
        Projects,
        Team,
        Skills,
        Contact, 
        Clients,
        Blog,
        Footer,
        CopyRight,
    }
}
</script>
