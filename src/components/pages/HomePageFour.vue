<template>
    <div>
        <NavbarStyleTwo />
        <Banner />
        <Process />
        <About />
        <Services />
        <Protfolio />
        <Review />
        <Team />
        <Subscribe />
        <Blog />
        <Faq />
        <Clients />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeFour/Banner'
import Process from '../HomeFour/Process'
import About from '../HomeFour/About'
import Services from '../HomeFour/Services'
import Protfolio from '../HomeFour/Protfolio'
import Review from '../HomeFour/Review'
import Team from '../Common/Team'
import Subscribe from '../HomeFour/Subscribe'
import Blog from '../Common/Blog'
import Faq from '../HomeFour/Faq'
import Clients from '../HomeFour/Clients'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageFour',
    components: {
        NavbarStyleTwo,
        Banner,
        Process,
        About,
        Services,
        Protfolio,
        Review,
        Team,
        Subscribe,
        Blog,
        Faq,
        Clients,
        Footer,
        CopyRight,
    }
}
</script>
