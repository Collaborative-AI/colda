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
    import PageTitle from '../BlogOne/PageTitle'
    import Blog from '../BlogOne/Blog'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'BlogOnePage',
        components: {
            Navbar,
            PageTitle,
            Blog,
            Footer,
            CopyRight,
        }
    }
</script>