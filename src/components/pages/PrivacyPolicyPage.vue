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
    import PageTitle from '../PrivacyPolicy/PageTitle'
    import Conditions from '../PrivacyPolicy/Conditions'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'PrivacyPolicyPage',
        components: {
            Navbar,
            PageTitle,
            Conditions,
            Footer,
            CopyRight,
        }
    }
</script>