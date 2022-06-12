<template>
    <div>
        <NavbarStyleTwo />
        <PageTitle />
        <Signup />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo.vue'
    import PageTitle from '../SignUp/PageTitle'
    import Signup from '../SignUp/Signup'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SignUpPage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            Signup,
            Footer,
            CopyRight,
        }
    }
</script>