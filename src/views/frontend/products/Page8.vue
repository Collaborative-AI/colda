<template>
    <div>
        <!-- <home id="iq-home" /> -->
          <div class="wrapper">
        <div class="main-content " >
           <!-- <Counter />
            <AboutUs id="iq-about" /> -->
            <Services id="iq-service"  />
            <!-- <Analytic />
            <WeProvide />
            <CaseStudies id="iq-process"  />
             <Partner />
              <Testimonials id="iq-testimonial"  />
            <Blog   id="iq-blog"/>
            <ContactUs id="iq-contact" />
            <Package id="iq-pricing"/> -->
        </div>
          </div>
    </div>
</template>
<script>
import {core} from '../../../config/pluginInit'
// import home from './components/home'
// import Counter  from './components/Counter'
// import  AboutUs from './components/AboutUs'
import  Services  from './components/Services'
// import      Analytic  from './components/Analytic'
// import   WeProvide from './components/WeProvide'
// import CaseStudies    from './components/CaseStudies'
// import  Partner from './components/Partner'
// import  Testimonials   from './components/Testimonials'
// import  Blog from './components/Blog'
// import  ContactUs  from './components/ContactUs'
// import Package from './components/package'
export default {
    name:'Page8',
     components:{
        //  home,
        //  Counter,
        //  AboutUs,
         Services,
        //  Analytic,
        //  WeProvide,
        //  CaseStudies,
        //  Partner,
        //  Testimonials,
        //  Blog,
        //  ContactUs,
        // Package
     },
     mounted(){
        core.index()
    }
}
</script>