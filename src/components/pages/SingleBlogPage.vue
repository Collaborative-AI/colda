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
    import PageTitle from '../SingleBlog/PageTitle'
    import Blog from '../SingleBlog/Blog'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SingleBlogPage',
        components: {
            Navbar,
            PageTitle,
            Blog,
            Footer,
            CopyRight,
        }
    }
</script>