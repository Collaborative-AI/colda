<template>
<div>
       <home />
      <div class="wrapper">
        <div class="main-content pt-5" >
           <about id="iq-about" />
           <getteam />
           <feature  id="iq-feature" />
           <pricing id="iq-pricing" />
             <testimonial id="iq-testimonials" />
             <blog id="iq-blog" />
        </div>
      </div>
</div>
    
</template>
<script>
import about   from './components/about'
import   getteam     from './components/getteam'
import  feature from './components/feature'
import pricing  from './components/pricing'
import testimonial  from './components/testimonial'
import blog from './components/blog'
import  home     from  './components/home'
import {core} from '../../../config/pluginInit'

export default {
    name:'Page2',
    components:{
        about,
        getteam,
        feature,
        pricing,testimonial,blog,home
        
    
          
    },
    mounted(){
        core.index()
    }
}
</script>