<template>
    <div class="two-sidebar sidebar-2">
    <div class="iq-sidebar-small bg-primary rounded">
        <div class="sidebar-top">
            <div class="iq-sidebar-small-logo">
               <router-link to="/">
              <img src="@/assets/images/logo-icon.png" class="img-fluid" alt="logo">
              </router-link>
            </div>
            <div class="sidebar-menu-icon">
                
                 <tab-nav :pills="true "  id="icon-pills-tab" extraclass=" list-inline m-0 p-0" role="tablist">
                        <tab-nav-items :active="true" liClass="nav-item d-block" id="pan" dataToggle="pill" ariaControls="pan-0" role="tab" :ariaSelected="true"  >
                            
                            <template v-slot:title>
                 <i class=" lab la-jira iq-arrow-left"></i>
                 <span>Layouts</span>
                </template>
                            
  
           </tab-nav-items>
                    <tab-nav-items :active="false" id="pan1" liClass="nav-item d-block"  ariaControls="pan-1" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="lab la-patreon iq-arrow-left"></i>
                  <span>App</span>
                </template>      
           </tab-nav-items>
             <tab-nav-items :active="false" id="pan2" liClass="nav-item d-block"  ariaControls="pan-2" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="lab la-elementor iq-arrow-left"></i>
                  <span>Ui kit</span>
                </template>      
           </tab-nav-items>
           <tab-nav-items :active="false" id="pan3" liClass="nav-item d-block"  ariaControls="pan-3" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="las la-pager iq-arrow-left"></i>
                  <span>Auth</span>
                </template>      
           </tab-nav-items>
           
                 </tab-nav>
                 </div>
        </div>
        <div class="sidebar-bottom">
            <div class="sidebar-menu-icon">
                <router-link :to="{  name: 'app.user-privacy-setting',}" class="" data-toggle="tooltip" data-placement="right" title="" data-original-title="Setting"><i class="ri-settings-2-fill"></i></router-link>
                <div class="iq-menu-bt align-self-center">
                <div class="wrapper-menu">
                     <div class="main-circle"><i class="las la-bars"></i></div>
                </div>
                </div>
            </div>
        </div>
    </div>
    <div class="iq-sidebar">
        <div class="data-scrollbar" data-scroll="1" id="sidebar-scrollbar">
            <nav class="iq-sidebar-menu">
                 <tab-content >

                       <tab-content-item :active="true" id="pan-0" aria-labelled-by="pan">
                   <CollapseMenu  :items="Layout" :open="true" /> 
                       </tab-content-item>
                         <tab-content-item :active="false" id="pan-1" aria-labelled-by="pan1">
                   <CollapseMenu  :items="App" :open="true"/> 
                       </tab-content-item>
                       <tab-content-item :active="false" id="pan-2" aria-labelled-by="pan2">
                            <CollapseMenu  :items="Ui" :open="true"/> 
                   
                       </tab-content-item>
                        <tab-content-item :active="false" id="pan-3" aria-labelled-by="pan3">
                  <CollapseMenu  :items="Auth" :open="true"/> 
                       </tab-content-item>
                 </tab-content>
              </nav>
            <div class="p-3"></div>
        </div>
    </div>
</div>
</template>
<script>

import CollapseMenu from "@/components/menustyle/CollapseMenu";
import Auth from "@/JsonData/auth.json"   
import Ui from "@/JsonData/ui.json"
import Layout from "@/JsonData/layoutpage.json"
import App from "@/JsonData/app.json"
import {core} from '@/config/pluginInit'

export default {
    name:"SidebarStyle8",
  components:{
    CollapseMenu
  },
   data () {
    return{
      homeurl:'',
     
      Layout:Layout,
      App:App,
      Auth:Auth,
      Ui:Ui
    }
  },
   mounted () {
    core.SmoothScrollbar()
    core.changesidebar()
  },
}
</script>