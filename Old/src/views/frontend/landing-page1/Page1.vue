<template>
    <div>
           <home /> 
        <div class="main-content pt-5" id="iq-about">  
        <about id="iq-about" />
         <feature id="iq-feature" />
          <testimonial  />
          <pricing />
          <blog />
          <contact id="iq-contact" />
        </div>
    </div>
</template>
<script>

import about from "./components/about"
import feature from './components/feature'
import testimonial from './components/testimonial'
import pricing from './components/pricing'
import blog  from './components/blog'
import contact from  './components/contact'
import home  from './components/home'
import {core} from '../../../config/pluginInit'
export default {
    name:'Page1',
    components:{
        home,
        about,
        feature,
        testimonial,
        pricing,
        blog,
        contact,
   
       
       
    },
         mounted(){
        core.index()
    }
}
</script>