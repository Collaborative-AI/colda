<template>
    <div>
        <Navbar />
        <PageTitle />
        <AgencyServices />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../ServicesTwo/PageTitle'
    import AgencyServices from '../ServicesTwo/AgencyServices'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ServicesTwoPage',
        components: {
            Navbar,
            PageTitle,
            AgencyServices,
            Footer,
            CopyRight,
        }
    }
</script>