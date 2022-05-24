<template>
    <div>
        <Navbar />
        <PageTitle />
        <Team />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../Team/PageTitle'
    import Team from '../Team/Team'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'TeamPage',
        components: {
            Navbar,
            PageTitle,
            Team,
            Footer,
            CopyRight,
        }
    }
</script>