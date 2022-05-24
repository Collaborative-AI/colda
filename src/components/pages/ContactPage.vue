<template>
    <div>
        <Navbar />
        <PageTitle />
        <ContactBox />
        <Contact />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import Navbar from '../Layout/Navbar'
    import PageTitle from '../Contact/PageTitle'
    import ContactBox from '../Contact/ContactBox'
    import Contact from '../Contact/Contact'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ContactPage',
        components: {
            Navbar,
            PageTitle,
            ContactBox,
            Contact,
            Footer,
            CopyRight,
        }
    }
</script>