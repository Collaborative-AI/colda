<template>
    <div>
        <Navbar />
        <PageTitle />
        <Services />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../ServicesOne/PageTitle'
    import Services from '../ServicesOne/Services'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ServicesOnePage',
        components: {
            Navbar,
            PageTitle,
            Services,
            Footer,
            CopyRight,
        }
    }
</script>