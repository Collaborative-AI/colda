<template>
    <div>
        <Navbar />
        <PageTitle />
        <Protfolio />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../ProjectsTwo/PageTitle'
    import Protfolio from '../ProjectsTwo/Protfolio'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ProjectsPageTwo',
        components: {
            Navbar,
            PageTitle,
            Protfolio,
            Footer,
            CopyRight,
        }
    }
</script>