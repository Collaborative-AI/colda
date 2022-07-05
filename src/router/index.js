// import { createWebHistory, createRouter } from "vue-router";

import Vue from 'vue';
import Router from 'vue-router';
Vue.use(Router);

// All Pages
// import HomePageOne from '../components/pages/HomePageOne'
import HomePageTwo from '../components/pages/HomePageTwo'
import HomePageThree from '../components/pages/HomePageThree'
import HomePageFour from '../components/pages/HomePageFour'
import HomePageFive from '../components/pages/HomePageFive'
import HomePageSix from '../components/pages/HomePageSix'
import HomePageSeven from '../components/pages/HomePageSeven'
import HomePageEight from '../components/pages/HomePageEight' 
import HomePageNine from '../components/pages/HomePageNine'
import AboutPage from '../components/pages/AboutPage'
import ServicesOnePage from '../components/pages/ServicesOnePage'
import ServicesTwoPage from '../components/pages/ServicesTwoPage'
import SingleServicesPage from '../components/pages/SingleServicesPage'
import ProjectsPageOne from '../components/pages/ProjectsPageOne'
import ProjectsPageTwo from '../components/pages/ProjectsPageTwo'
import SingleProjectsPage from '../components/pages/SingleProjectsPage'
import BlogOnePage from '../components/pages/BlogOnePage'
import BlogTwoPage from '../components/pages/BlogTwoPage'
import SingleBlogPage from '../components/pages/SingleBlogPage'
import ContactPage from '../components/pages/ContactPage'
import TeamPage from '../components/pages/TeamPage'
import PricingPage from '../components/pages/PricingPage'
import FaqPage from '../components/pages/FaqPage'
import LogInPage from '../components/pages/LogInPage'
import SignUpPage from '../components/pages/SignUpPage'
import TermsConditionsPage from '../components/pages/TermsConditionsPage'
import PrivacyPolicyPage from '../components/pages/PrivacyPolicyPage'
import ErrorPage from '../components/pages/ErrorPage'

import Dashboard1 from "../components/Dash/Dashboard";

import Admin from "../components/mdbvue/Admin"

import Dashboard from '../components/mdbvue/Dashboard'
import Profile from '../components/mdbvue/Profile'
import Tables from '../components/mdbvue/Tables'
// import Maps from '../components/mdbvue/Maps'
import BadGateway from '../components/mdbvue/BadGateway'


const routes = [
    {path: '/', component: HomePageSeven},
    {path: '/home-two', component: HomePageTwo},
    {path: '/home-three', component: HomePageThree},
    {path: '/home-four', component: HomePageFour},
    {path: '/home-five', component: HomePageFive},
    {path: '/home-six', component: HomePageSix},
    {path: '/home', component: HomePageSeven},
    {path: '/home-eight', component: HomePageEight},
    {path: '/home-nine', component: HomePageNine},
    {path: '/about', component: AboutPage},
    {path: '/services-one', component: ServicesOnePage},
    {path: '/services-two', component: ServicesTwoPage},
    {path: '/single-services', component: SingleServicesPage},
    {path: '/projects-one', component: ProjectsPageOne},
    {path: '/projects-two', component: ProjectsPageTwo},
    {path: '/single-projects', component: SingleProjectsPage},
    {path: '/use-cases', component: BlogOnePage},
    {path: '/blog-two', component: BlogTwoPage},
    {path: '/single-blog', component: SingleBlogPage},
    {path: '/contact', component: ContactPage},
    {path: '/team', component: TeamPage},
    {path: '/products', component: PricingPage},
    {path: '/faq', component: FaqPage},
    {path: '/sign-in', component: LogInPage},
    {path: '/sign-up', component: SignUpPage},
    {path: '/terms-condition', component: TermsConditionsPage},
    {path: '/privacy-policy', component: PrivacyPolicyPage},
    {path: '/error-404', component: ErrorPage},
    {path: '/dashboard1', component: Dashboard1},

    // {
    //   path: '/dashboard',
    //   name: 'Dashboard',
    //   component: Dashboard,
    //   props: { page: 1 },
    //   alias: '/'
    // },
    // {
    //   path: '/profile',
    //   name: 'Profile',
    //   props: { page: 2 },
    //   component: Profile
    // },
    // {
    //   path: '/tables',
    //   name: 'Tables',
    //   props: { page: 3 },
    //   component: Tables
    // },

    {
      path: '/admin', 
      component: Admin,
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard,
          props: { page: 1 },
        },
        {
          path: 'profile',
          name: 'Profile',
          props: { page: 2 },
          component: Profile
        },
        {
          path: 'tables',
          name: 'Tables',
          props: { page: 3 },
          component: Tables
        },
        {
          path: '404',
          name: 'BadGateway',
          props: { page: 5 },
          component: BadGateway
        }
      ]
    }
]
    
// const router = createRouter({
//     history: createWebHistory(),
//     linkExactActiveClass: "active",
//     routes,
//     scrollBehavior() {
//       return { top: 0 };
//     },
//   });
const router = new Router({
  routes,
  mode: 'history'
})
  
export default router;