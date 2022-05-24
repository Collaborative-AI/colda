<template>
    <div>
        <Navbar />
        <PageTitle />
        <Conditions />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../TermsConditions/PageTitle'
    import Conditions from '../TermsConditions/Conditions'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'TermsConditionsPage',
        components: {
            Navbar,
            PageTitle,
            Conditions,
            Footer,
            CopyRight,
        }
    }
</script>