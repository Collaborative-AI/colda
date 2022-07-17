<template>
    <div class="two-sidebar sidebar-1">
    <div class="iq-sidebar-small">
        <div class="sidebar-top">
            <div class="iq-sidebar-small-logo">
                <router-link to="/">
                <img src="@/assets/images/logo-icon.png" class="img-fluid rounded-normal" alt="logo">
                </router-link>
            </div>
            <div class="sidebar-menu-icon">
                  <tab-nav :pills="true "  id="icon-pills-tab" extraclass=" list-inline m-0 p-0" role="tablist" aria="vertical">
                        <tab-nav-items :active="true" liClass="nav-item d-block" id="pan" dataToggle="pill" ariaControls="pan-0" role="tab" :ariaSelected="true"  >
                            
                            <template v-slot:title>
                 <i class="lab la-jira iq-arrow-left"></i>
                </template>
                            
  
           </tab-nav-items>
                    <tab-nav-items :active="false" id="pan1" liClass="nav-item d-block"  ariaControls="pan-1" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="lab la-patreon iq-arrow-left" ></i>
                </template>      
           </tab-nav-items>
             <tab-nav-items :active="false" id="pan2" liClass="nav-item d-block"  ariaControls="pan-2" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="lab la-elementor iq-arrow-left"></i>
                </template>      
           </tab-nav-items>
           <tab-nav-items :active="false" id="pan3" liClass="nav-item d-block"  ariaControls="pan-3" role="tab" dataToggle="pill" :ariaSelected="false">       
              <template v-slot:title>
                 <i class="las la-pager "></i>
                </template>      
           </tab-nav-items>
                  </tab-nav>
            </div>
        </div>
        <div class="sidebar-bottom">
            <div class="sidebar-menu-icon">
                <router-link  :to="{name: 'app.user-Account-setting'}" class="" data-toggle="tooltip" data-placement="right" title="" data-original-title="Setting"><i class="ri-settings-2-fill"></i></router-link>
                <div class="iq-menu-bt align-self-center">
                <div class="wrapper-menu">
                     <div class="main-circle"><i class="las la-angle-double-left"></i></div>
                     <div class="main-circle close-btn"><i class="las la-angle-double-right"></i></div>
                </div>
                </div>
            </div>
        </div>
    </div>
    <div class="iq-sidebar">
        <div class="iq-sidebar-top">
            <div class="top-menu-icon">
                <ul class="list-inline d-flex align-items-center justify-content-between m-0 p-0">
                    <li class="menu-icon">
                            <router-link :to="{ name: 'app.user-profile',}" class="bg-info-light" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Profile"><i class="las la-user-circle"></i></router-link>
                    </li>
                    <li class="menu-icon">
                            <router-link :to="{name: 'app.email-listing'}" class="bg-warning-light" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Email"><i class="las la-envelope-open"></i></router-link>
                    </li>
                    <li class="menu-icon">
                            <router-link :to="{name: 'app.chat'}" class="bg-info-light" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Chat"><i class="lab la-rocketchat"></i></router-link>
                    </li>
                    <li class="menu-icon">
                            <router-link :to="{name: 'contact.list'}" class="bg-warning-light" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Contact"><i class="las la-file-alt"></i></router-link>
                    </li>
                </ul>
            </div>
        </div>
        <div class="data-scrollbar" data-scroll="1" id="sidebar-scrollbar">
            <nav class="iq-sidebar-menu">
                  
                   <tab-content   >
                   
                       <tab-content-item :active="true" id="pan-0" aria-labelled-by="pan">
                   <CollapseMenu  :items="Layout" :open="true"  /> 
                       </tab-content-item>
                         <tab-content-item :active="false" id="pan-1" aria-labelled-by="pan1">
                   <CollapseMenu  :items="App" :open="true"   /> 
                       </tab-content-item>
                       <tab-content-item :active="false" id="pan-2" aria-labelled-by="pan2">
                            <CollapseMenu  :items="Ui" :open="true" /> 
                   
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
    name:"SidebarStyle2",
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