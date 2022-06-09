<template>
    <div>
        <NavbarStyleTwo />
        <PageTitle />
        <Pricing />
        <!-- <Tab /> -->
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo.vue'
    import PageTitle from '../Pricing/PageTitle'
    import Pricing from '../Pricing/Pricing'
    // import Tab from '../Pricing/Tab'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'PricingPage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            Pricing,
            // Tab,
            Footer,
            CopyRight,
        }
    }
</script>