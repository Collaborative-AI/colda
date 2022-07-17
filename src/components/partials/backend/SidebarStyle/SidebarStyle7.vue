<template>
   <div class="iq-sidebar sidebar-double-icon">
    <div class="iq-sidebar-logo d-flex align-items-center justify-content-between">
         <router-link to="/" class="header-logo mx-auto">
        <img :src="logo" class="img-fluid rounded-normal" alt="logo">
        </router-link>
        <div class="iq-menu-bt-sidebar">                       
            <i class="las la-bars wrapper-menu"></i>
        </div>
    </div>
    <div id="sidebar-scrollbar" class="data-scrollbar" data-scroll="1">
        <div class="d-block user-info mb-3">
            <div class="text-center mb-4">
                <div class="d-inline-block doc-img user-image mb-3 rounded position-relative">
                    <img src="@/assets/images/user/user-1.jpg" class="img-fluid d-inline-block avatar-110 rounded" alt="logo">
                </div>
                <h4>Cliff Hanger</h4>
                <p>cliff@admin.com</p>
            </div>
        </div>
        <div class="double-icon-height">
            <nav class="iq-sidebar-menu">
                <ul id="iq-sidebar-toggle" class="iq-menu">
                <li>
                    <div class="d-flex align-items-center">
                        <a href="#index.html" class="collapsed" data-toggle="collapse" aria-expanded="false"><i class="las la-home iq-arrow-left"></i><span>Dashboard</span></a>
                        <a href="#layout-school.html" class="collapsed active" data-toggle="collapse" aria-expanded="true"><i class="las la-school"></i><span>School</span></a>
                    </div>
                </li>
                <li>
                    <div class="d-flex align-items-center">
                        <a href="#layout-hospital.html" class="collapsed" data-toggle="collapse" aria-expanded="false"><i class="las la-hospital"></i><span>Hospital</span></a>
                        <a href="#layout-hotel.html" class="collapsed" data-toggle="collapse" aria-expanded="false"><i class="las la-hotel"></i><span>Hotel</span></a>
                    </div>
                </li>
                <li>
                    <div class="d-flex align-items-center">
                        <a href="#layout-payment.html" class="collapsed" data-toggle="collapse" aria-expanded="false"><i class="las la-file-invoice-dollar"></i><span>Payment</span></a>
                        <a href="#layout-restaurant.html" class="collapsed" data-toggle="collapse" aria-expanded="false"><i class="las la-concierge-bell"></i><span>Restaurant</span></a>
                    </div>
                </li>
                </ul>
            </nav>
        </div>
        <div class="sidebar-bottom-menu">
            <nav class="iq-sidebar-menu">
                <ul class="iq-menu-bottom list-inline">
                    <li><router-link :to="{ name: 'app.email-listing'}"><i class="las la-envelope-open iq-arrow-left"></i><span>Email </span><span class="float-right badge badge-warning rounded-circle menu-icon-right">18</span></router-link></li>
                    <li><router-link :to="{name: 'app.chat'}"><i class="las la-bell iq-arrow-left"></i><span>Chat</span><span class="float-right badge badge-warning rounded-circle menu-icon-right">18</span></router-link></li>
                </ul>
                <div class="text-center mt-3">
                    <router-link :to="{name: 'auth.login'}" class="btn btn-primary"><i class="las la-sign-out-alt"></i>Logout</router-link>
                </div>
            </nav>
        </div>
    </div>
</div>
</template>
<script>
import { mapGetters } from 'vuex'
import {core} from '@/config/pluginInit'
export default {
    name:"SidebarStyle7",
    computed : {
        ...mapGetters({
            logo:'logo'
        })
    },
     mounted () {
    core.SmoothScrollbar()
      core.changesidebar()
  },

}
</script>