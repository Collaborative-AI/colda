<template>
    <div>
        <home />
         <div class="wrapper">
        <div class="main-content ">
            <howitworks id="iq-about" />
            <feature id="iq-feature" />
            <sales />
             <portfolio />
             <testimonial id="iq-testimonial" />
              <post id="iq-blog" />
        </div>
         </div>
    </div>
</template>
<script>

import {core} from '../../../config/pluginInit'
import home from './components/home'
import  howitworks from './components/howitworks'
import  feature from './components/feature'
import sales from './components/sales' 
import  portfolio from './components/portfolio'
import testimonial   from './components/testimonial'
import  post    from  './components/post'
export default {
    name:'Page10',
    components:{
        home,
        howitworks,
        feature,
        sales,
        portfolio,testimonial,post
    },
      mounted(){
        core.index()
    }
}
</script>