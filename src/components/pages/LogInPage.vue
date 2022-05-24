<template>
    <div>
        <Navbar />
        <PageTitle />
        <Login />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../LogIn/PageTitle'
    import Login from '../LogIn/Login'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'LogInPage',
        components: {
            Navbar,
            PageTitle,
            Login,
            Footer,
            CopyRight,
        }
    }
</script>