<template>
    <div class="salon-samall-saidbar">
   <div class="iq-sidebar-logo d-flex justify-content-between">
      <router-link to="/" class="header-logo">
        <img src="@/assets/images/logo-icon.png" class="img-fluid rounded-normal" alt="logo">
     </router-link>
      <div class="iq-menu-bt-sidebar">
            <div class="iq-menu-bt align-self-center">
                  <div class="wrapper-menu open">
                        <div class="main-circle"><i class="las la-bars"></i></div>
                  </div>
            </div>
      </div>
   </div>
   <div  class="data-scrollbar  salon-scroll">
      <nav class="iq-sidebar-menu" >
            <HoverMenu  :items="Header" className="iq-menu" :open="true" :enableIcon="false"/>
         
      </nav> 
     
   </div> 
<div id="sidebar-bottom" class="sidebar-bottom position-relative">
      <div class="sidebar-menu-icon">
            <router-link :to="{name: 'app.user-privacy-setting'}" class="set-text" data-toggle="tooltip" data-placement="right"
                  title="" data-original-title="Setting"><i class="ri-settings-2-fill"></i>
            </router-link>
            <div class="small-profl">
                  <router-link :to="{name: 'app.user-privacy-setting'}" class="iq-user-toggle">
                        <img src="@/assets/images/user/1.jpg" class="img-fluid rounded avatar-40" alt="user">
                  </router-link>
            </div>
      </div>
</div>
</div>

</template>
<script>



import Header  from "@/JsonData/header4.json"
import {core} from '@/config/pluginInit'
export default {
    name:"SidebarStyle4",
      
  mounted () {
        
    core.changesidebar()
  },

  data () {
    return{
      homeurl:'',
      Header:Header
    }
  },
}
</script>