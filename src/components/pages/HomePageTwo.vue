<template>
    <div>
        <Navbar />
        <Banner />
        <Features />
        <Work />
        <Services />
        <Support />
        <Overview />
        <Choose />
        <FunFacts />
        <Projects />
        <Team />
        <Skills />
        <Blog />
        <Clients />
        <Partner />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import Navbar from '../Layout/Navbar'
import Banner from '../HomeTwo/Banner'
import Features from '../HomeTwo/Features'
import Work from '../HomeTwo/Work'
import Services from '../HomeTwo/Services'
import Support from '../HomeTwo/Support'
import Overview from '../HomeTwo/Overview'
import Choose from '../HomeTwo/Choose'
import FunFacts from '../HomeTwo/FunFacts'
import Projects from '../HomeTwo/Projects'
import Team from '../HomeTwo/Team'
import Skills from '../HomeTwo/Skills'
import Blog from '../Common/Blog'
import Clients from '../HomeTwo/Clients'
import Partner from '../HomeTwo/Partner'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageTwo',
    components: {
        Navbar,
        Banner,
        Features,
        Work,
        Services,
        Support,
        Overview,
        Choose,
        FunFacts,
        Projects,
        Team,
        Skills,
        Blog,
        Clients,
        Partner,
        Footer,
        CopyRight,
    }
}
</script>
