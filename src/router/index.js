import { createWebHistory, createRouter } from "vue-router";

// All Pages
import HomePageOne from '../components/pages/HomePageOne'
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

const routes = [
    {path: '/', component: HomePageOne},
    {path: '/home-two', component: HomePageTwo},
    {path: '/home-three', component: HomePageThree},
    {path: '/home-four', component: HomePageFour},
    {path: '/home-five', component: HomePageFive},
    {path: '/home-six', component: HomePageSix},
    {path: '/home-seven', component: HomePageSeven},
    {path: '/home-eight', component: HomePageEight},
    {path: '/home-nine', component: HomePageNine},
    {path: '/about', component: AboutPage},
    {path: '/services-one', component: ServicesOnePage},
    {path: '/services-two', component: ServicesTwoPage},
    {path: '/single-services', component: SingleServicesPage},
    {path: '/projects-one', component: ProjectsPageOne},
    {path: '/projects-two', component: ProjectsPageTwo},
    {path: '/single-projects', component: SingleProjectsPage},
    {path: '/blog-one', component: BlogOnePage},
    {path: '/blog-two', component: BlogTwoPage},
    {path: '/single-blog', component: SingleBlogPage},
    {path: '/contact', component: ContactPage},
    {path: '/team', component: TeamPage},
    {path: '/pricing', component: PricingPage},
    {path: '/faq', component: FaqPage},
    {path: '/log-in', component: LogInPage},
    {path: '/sign-up', component: SignUpPage},
    {path: '/terms-condition', component: TermsConditionsPage},
    {path: '/privacy-policy', component: PrivacyPolicyPage},
    {path: '/error-404', component: ErrorPage},
]
    
const router = createRouter({
    history: createWebHistory(),
    linkExactActiveClass: "active",
    routes,
    scrollBehavior() {
      return { top: 0 };
    },
  });
  
export default router;