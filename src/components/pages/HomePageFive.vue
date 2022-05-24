<template>
    <div>
        <NavbarStyleTwo />
        <Banner />
        <Learn />
        <App />
        <Data />
        <Services />
        <Customer />
        <Review />
        <Team />
        <Clients />
        <Blog />
        <Footer />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleTwo from '../Layout/NavbarStyleTwo'
import Banner from '../HomeFive/Banner'
import Learn from '../HomeFive/Learn'
import App from '../HomeFive/App'
import Data from '../HomeFive/Data'
import Services from '../HomeFive/Services'
import Customer from '../HomeFive/Customer'
import Review from '../HomeFive/Review'
import Team from '../Common/Team'
import Clients from '../HomeFive/Clients'
import Blog from '../Common/Blog'
import Footer from '../Layout/Footer'
import CopyRight from '../Layout/CopyRight'

export default {
    name: 'HomePageFive',
    components: {
        NavbarStyleTwo,
        Banner,
        Learn,
        App,
        Data,
        Services,
        Customer,
        Review,
        Team,
        Clients,
        Blog,
        Footer,
        CopyRight,
    }
}
</script>
