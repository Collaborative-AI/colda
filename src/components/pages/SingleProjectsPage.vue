<template>
    <div>
        <Navbar />
        <PageTitle />
        <ProjectDetails />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../SingleProjects/PageTitle'
    import ProjectDetails from '../SingleProjects/ProjectDetails'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'SingleProjectsPage',
        components: {
            Navbar,
            PageTitle,
            ProjectDetails,
            Footer,
            CopyRight,
        }
    }
</script>