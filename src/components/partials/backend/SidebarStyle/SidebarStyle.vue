<template>
  <div class="iq-sidebar  sidebar-default ">
    <div class="iq-sidebar-logo d-flex align-items-center justify-content-between">
      <router-link :to="homeurl" class="header-logo">
        <img :src="logo" class="img-fluid rounded-normal" alt="logo">
      </router-link>
      <div class="iq-menu-bt-sidebar">
        <i class="las la-bars wrapper-menu"></i>
      </div>
    </div>
    <div class="data-scrollbar" data-scroll="1" id="sidebar-scrollbar">
      <nav class="iq-sidebar-menu">
          <CollapseMenu  :items="sidebarItems" :open="true"/>
      </nav>
    </div>
  </div>
</template>
<script>
import CollapseMenu from "@/components/menustyle/CollapseMenu";
import sideBarItem from "@/JsonData/sidebar.json"
import { mapGetters } from 'vuex'
import {core} from '@/config/pluginInit'
export default {
  name:"SidebarStyle",
  data () {
    return{
      homeurl:'',
      sidebarItems:sideBarItem
    }
  },
  mounted () {
    core.SmoothScrollbar()
    core.changesidebar()
  },
  components:{
    CollapseMenu
  },
  computed : {
        ...mapGetters({
            appName: 'appName',
            logo:'logo'
        })
    }

}
</script>
