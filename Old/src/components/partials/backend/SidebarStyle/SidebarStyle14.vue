<template>
<div class="iq-sidebar">
    <div class="iq-sidebar-logo">
        <div class="iq-menu-bt-sidebar">
            <i class="las la-bars wrapper-menu float-right"></i>
        </div>
    </div>
    <div class="p-pt">               
        <img src="@/assets/images/layouts/layout-14/profile.png" class="img-fluid avatar-60 rounded d-block mx-auto profile-img" alt="user">
        <div class="profile-detail mt-3 text-center">
            <h4>John Doe</h4>
            <p class="text-primary mb-0">M.B.B.S</p>
        </div>
        <div class="seprator"></div>
    </div>                    
    <div class="data-scrollbar" data-scroll="1">
        <nav class="iq-sidebar-menu" id="sidebar-scrollbar">
            <ul id="iq-sidebar-toggle" class="iq-menu">
                <li class="">
                <router-link to="/" class=""><i
                        class="las la-home iq-arrow-left"></i><span>Dashboard</span>
                </router-link>                        
                </li>
                <li class="active">
                <router-link :to="{ name: 'backend.layout-14'}" class=""><i
                        class="lab la-jira iq-arrow-left"></i><span>Layout</span>
                </router-link>                        
                </li>
                <li class="">
                <router-link :to="{ name: 'Ui.colors'}" class=""><i
                        class="lab la-elementor iq-arrow-left"></i><span>UI Elements</span>
                </router-link>                        
                </li>
                <li class="">
                <router-link :to="{name: 'controls.form-layout',}" class=""><i
                        class="lab la-wpforms iq-arrow-left"></i><span>Forms</span>                        
                </router-link>                   
                </li>
                <li class="">
                <router-link :to="{name: 'auth.login',}" class="collapsed" data-toggle="collapse"
                    aria-expanded="false"><i class="las la-pager iq-arrow-left"></i><span>Authentication</span>                           
                </router-link>                        
                </li>
            </ul>
        </nav>
        <div class="p-3"></div>
    </div>
</div>
</template>
<script>
import {core} from '@/config/pluginInit'
export default {
    name:"SidebarStyle14",
   
    mounted () {
    core.SmoothScrollbar(),
    core.changesidebar()
  },
}
</script>