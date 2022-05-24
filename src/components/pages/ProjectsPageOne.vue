<template>
    <div>
        <Navbar />
        <PageTitle />
        <Projects />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../ProjectsOne/PageTitle'
    import Projects from '../ProjectsOne/Projects'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ProjectsPageOne',
        components: {
            Navbar,
            PageTitle,
            Projects,
            Footer,
            CopyRight,
        }
    }
</script>