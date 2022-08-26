<template>
    <div class="iq-sidebar sidebar-bg-box">
    <div class="iq-fitness-info bg-primary mb-3">
        <div class="iq-sidebar-logo d-flex align-items-center justify-content-between">
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
        <div class="user-background text-left">
            <a href="javascript:void(0);" class="collapsed" data-toggle="collapse"
                aria-expanded="false">
                <div class="d-flex align-items-center justify-content-between">
                    <div class="user-text d-flex align-items-center">
                        <img src="@/assets/images/layouts/layout-3/user-2.jpg" class="img-fluid rounded avatar-40 mr-3"
                            alt="user-2">
                            <div class="user-text-info line-height">
                                <span>Steve K</span>
                                <div class="iq-progress-bar-linear d-inline-block w-80">
                                    <Progressbar :value="60" color="warning" />
                                </div>
                            </div>

                    </div>
                    <i class="las la-angle-right iq-arrow-right text-right"></i>
                </div>
            </a>
        </div>
    </div>
    <div id="sidebar-scrollbar" class="data-scrollbar" data-scroll="1">
        <nav class="iq-sidebar-menu">
            <CollapseMenu  :items="Header" :open="true"/>
            </nav>
        <div id="sidebar-bottom" class="position-relative">
                <div class="card bg-primary rounded">
                   <div class="card-body">
                       <div class="sidebarbottom-content">
                          <div class="image"><img src="@/assets/images/layouts/layout-3/side-bkg.png" alt="side-bkg"></div>
                          <h5 class="mb-3 text-white">Upgrade to PRO</h5>
                          <p class="mb-0 text-white">Become a pro user & enjoy more.</p>
                      </div>
                  </div>
                </div>
        </div>
    </div>
</div>
</template>
<script>
import CollapseMenu from "@/components/menustyle/CollapseMenu";
import Header  from "@/JsonData/header3.json"
import { mapGetters } from 'vuex'
import {core} from '@/config/pluginInit'
export default {
    name:"SidebarStyle3",
      components:{
    CollapseMenu
  },
    mounted () {
    core.SmoothScrollbar()
    core.changesidebar()
  },
    computed : {
        ...mapGetters({
            logo:'darklogo'
        })
    },
      data () {
    return{
      homeurl:'',
      Header:Header
    }
  },

}
</script>