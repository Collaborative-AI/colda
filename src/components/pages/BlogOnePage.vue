<template>
    <div>
        <NavbarStyleTwo />
        <PageTitle />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo.vue'
    import PageTitle from '../BlogOne/PageTitle'
    import Blog from '../BlogOne/Blog'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'BlogOnePage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            Blog,
            Footer,
            CopyRight,
        }
    }
</script>