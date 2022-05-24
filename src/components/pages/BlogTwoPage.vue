<template>
    <div>
        <Navbar />
        <PageTitle />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../BlogTwo/PageTitle'
    import Blog from '../BlogTwo/Blog'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'BlogTwoPage',
        components: {
            Navbar,
            PageTitle,
            Blog,
            Footer,
            CopyRight,
        }
    }
</script>