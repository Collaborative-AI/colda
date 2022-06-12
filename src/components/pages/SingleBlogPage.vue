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
    import PageTitle from '../SingleBlog/PageTitle'
    import Blog from '../SingleBlog/Blog'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SingleBlogPage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            Blog,
            Footer,
            CopyRight,
        }
    }
</script>