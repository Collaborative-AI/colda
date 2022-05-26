<template>
    <div>
        <NavbarStyleTwo />
        <PageTitle />
        <ContactBox />
        <Contact />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
    import NavbarStyleTwo from '../Layout/NavbarStyleTwo.vue'
    import PageTitle from '../Contact/PageTitle'
    import ContactBox from '../Contact/ContactBox'
    import Contact from '../Contact/Contact'
    import Footer from '../Layout/Footer'
    import CopyRight from '../Layout/CopyRight'

    export default {
        name: 'ContactPage',
        components: {
            NavbarStyleTwo,
            PageTitle,
            ContactBox,
            Contact,
            Footer,
            CopyRight,
        }
    }
</script>