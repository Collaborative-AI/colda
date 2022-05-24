<template>
    <div>
        <Navbar />
        <PageTitle />
        <Pricing />
        <Tab />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../Faq/PageTitle'
    import Pricing from '../Faq/Faq'
    import Tab from '../Faq/Tab'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'FaqPage',
        components: {
            Navbar,
            PageTitle,
            Pricing,
            Tab,
            Footer,
            CopyRight,
        }
    }
</script>