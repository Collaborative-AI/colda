<template>
    <div>
        <NavbarStyleTwo />
        <PageTitle />
        <!-- <About /> -->
        <Team />
        <Faq />
        <Clients />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
    import PageTitle from '../About/PageTitle'
    // import About from '../About/About'
    import Faq from '../About/Faq'
    import Team from '../HomeNine/Team'
    import Clients from '../HomeNine/Clients'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'AboutPage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            // About,
            Faq,
            Team,
            Clients,
            Footer,
            CopyRight,
        }
    }
</script>