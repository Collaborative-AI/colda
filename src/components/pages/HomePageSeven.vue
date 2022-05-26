<template>
    <div>
        <NavbarStyleTwo />
        <Banner />  <!-- build your model with our service -->    
        <MoreFeatures />    <!-- privacy-preserving -->
        <Tech />    <!-- perfect app for beninner -->
        <Digital /> <!-- our motivation -->
        <!-- <AgencyServices /> -->
        <!-- <Experience />
        <Tab /> -->
        <!-- <Team /> -->
        <!-- <Faq /> -->  
        <Clients />   <!-- start your journey with us -->
        <!-- <Blog /> -->
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeSeven/Banner'
import MoreFeatures from '../HomeSeven/MoreFeatures'
import Tech from '../HomeSeven/Tech'
import Digital from '../HomeSeven/Digital'
// import AgencyServices from '../HomeSeven/AgencyServices'
// import Experience from '../HomeSeven/Experience'
// import Tab from '../HomeSeven/Tab'
// import Team from '../Common/Team'
// import Faq from '../HomeSeven/Faq'
import Clients from '../HomeSeven/Clients'
// import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageSeven',
    components: {
        NavbarStyleTwo,
        Banner,
        MoreFeatures,
        Tech,
        Digital,
        // AgencyServices,
        // Experience,
        // Tab,
        // Team,
        // Faq,
        Clients,
        // Blog,
        Footer,
        CopyRight,
    }
}
</script>