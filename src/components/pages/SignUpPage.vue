<template>
    <div>
        <Navbar />
        <PageTitle />
        <Signup />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar.vue'
    import PageTitle from '../SignUp/PageTitle'
    import Signup from '../SignUp/Signup'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SignUpPage',
        components: {
            Navbar,
            PageTitle,
            Signup,
            Footer,
            CopyRight,
        }
    }
</script>