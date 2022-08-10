<template>
   
<div class="iq-sidebar iq-sidebar-primary" :style="`background:  url(${require('@/assets/images/layouts/layout-9/saidbar.png')});background-position: center center;background-color:#01041b;
	background-size: cover;`">
    <div class="iq-sidebar-logo d-flex justify-content-between">
       <router-link to="/" class="header-logo">
        <img :src="logo" class="img-fluid rounded-normal" alt="logo">
        </router-link>
        <div class="iq-menu-bt-sidebar">
            <div class="iq-menu-bt align-self-center">
                <div class="wrapper-menu">
                <div class="main-circle"><i class="las la-bars"></i></div>
                </div>
            </div>
        </div>
    </div>
    <div class="data-scrollbar" data-scroll="1"  id="sidebar-scrollbar">
        <nav class="iq-sidebar-menu">
            <CollapseMenu  :items="Header" :open="true"/>
     
               
        </nav>
        <div class="p-3"></div>
    </div>
    </div>
</template>
<script>
import CollapseMenu from "@/components/menustyle/CollapseMenu";
import {core} from '@/config/pluginInit'
import Header  from "@/JsonData/header9.json"
import { mapGetters } from 'vuex'
export default {
    name:"SidebarStyle9",
    computed : {
        ...mapGetters({
            logo:'logo'
        }),
      
    },
      components:{
    CollapseMenu
  },
     mounted () {
    core.SmoothScrollbar()
    core.changesidebar()
  }, data () {
    return{
      homeurl:'',
      Header:Header,
     
    }
  },
   methods: {
    
    }

}
</script>