<template>
    <div>
        <NavbarStyleTwo />
        <Banner />
        <Services />
        <Audience />
        <Solutions />
        <Design />
        <Counter />
        <Team />
        <Pricing />
        <Protfolio />
        <Clients />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeThree/Banner'
import Services from '../HomeThree/Services'
import Audience from '../HomeThree/Audience'
import Solutions from '../HomeThree/Solutions'
import Design from '../HomeThree/Design'
import Counter from '../HomeThree/Counter'
import Team from '../Common/Team'
import Pricing from '../HomeThree/Pricing'
import Protfolio from '../HomeThree/Protfolio'
import Clients from '../Common/Clients'
import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageThree',
    components: {
        NavbarStyleTwo,
        Banner,
        Services,
        Audience,
        Solutions,
        Design,
        Counter,
        Team,
        Pricing,
        Protfolio,
        Clients,
        Blog,
        Footer,
        CopyRight,
    }
}
</script>
