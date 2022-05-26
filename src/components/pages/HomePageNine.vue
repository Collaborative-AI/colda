<template>
    <div>
        <NavbarStyleTwo />
        <Banner />
        <MoreFeatures />
        <!-- <About />
        <Services />
        <Pricing />
        <Tab />
        <Team />
        <Portfolio />
        <Subscribe />
        <Blog />
        <Faq />
        <Clients /> -->
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
    import Banner from '../HomeNine/Banner'
    import MoreFeatures from '../HomeNine/MoreFeatures'
    // import About from '../HomeNine/About'
    // import Services from '../HomeNine/Services'
    // import Pricing from '../HomeNine/Pricing'
    // import Tab from '../HomeNine/Tab'
    // import Team from '../HomeNine/Team'
    // import Portfolio from '../HomeNine/Portfolio'
    // import Subscribe from '../HomeNine/Subscribe'
    // import Blog from '../Common/Blog'
    // import Faq from '../HomeNine/Faq'
    // import Clients from '../HomeNine/Clients'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'HomePageNine',
        components: {
            NavbarStyleTwo,
            Banner,
            MoreFeatures,
            // About,
            // Services,
            // Pricing,
            // Tab,
            // Team,
            // Portfolio,
            // Subscribe,
            // Blog,
            // Faq,
            // Clients,
            Footer,
            CopyRight,
        }
    }
</script>