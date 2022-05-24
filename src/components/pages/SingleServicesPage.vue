<template>
    <div>
        <Navbar />
        <PageTitle />
        <ServicesDetails />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../SingleServices/PageTitle'
    import ServicesDetails from '../SingleServices/ServicesDetails'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SingleServicesPage',
        components: {
            Navbar,
            PageTitle,
            ServicesDetails,
            Footer,
            CopyRight,
        }
    }
</script>