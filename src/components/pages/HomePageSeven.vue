<template>
    <div>
        <Navbar />
        <Banner />  <!-- build your model with our service -->    
        <MoreFeatures />    <!-- privacy-preserving -->
        <Tech />    <!-- perfect app for beninner -->
        <!-- our motivation -->
        <Faq />  
        <!-- <Digital /> -->
        <!-- <AgencyServices /> -->
        <!-- <Experience />
        <Tab /> -->
        <!-- <Team /> -->
        <Clients />   <!-- start your journey with us -->
        <!-- <Blog /> -->
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import Navbar from '../Layout/Navbar.vue'
import Banner from '../HomeSeven/Banner'
import MoreFeatures from '../HomeSeven/MoreFeatures'
import Tech from '../HomeSeven/Tech'
import Faq from '../HomeSeven/Faq'
// import Digital from '../HomeSeven/Digital'
// import AgencyServices from '../HomeSeven/AgencyServices'
// import Experience from '../HomeSeven/Experience'
// import Tab from '../HomeSeven/Tab'
// import Team from '../Common/Team'
import Clients from '../HomeSeven/Clients'
// import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageSeven',
    components: {
        Navbar,
        Banner,
        MoreFeatures,
        Tech,
        Faq,
        // Digital,
        // AgencyServices,
        // Experience,
        // Tab,
        // Team,
        Clients,
        // Blog,
        Footer,
        CopyRight,
    }
}
</script>