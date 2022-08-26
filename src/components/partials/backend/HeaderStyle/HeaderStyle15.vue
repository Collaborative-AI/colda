<template>
    <div class="iq-top-navbar p-0">
    <div class="top-menu">
        <div class="iq-navbar-custom">
            <div class="iq-navbar-logo d-flex align-items-center justify-content-between">
                <i class="ri-menu-line wrapper-menu"></i>
               <router-link to="/" class="header-logo">
                <img :src="logo" class="img-fluid rounded-normal" alt="logo">
                </router-link>
            </div>
            <div class="iq-menu-horizontal">
                  <nav class="iq-sidebar-menu">
                     <div class="iq-sidebar-logo d-flex align-items-center justify-content-between">
                           <router-link to="/" class="header-logo">
                              <img :src="sidelogo" class="img-fluid rounded-normal" alt="logo">
                           </router-link> 
                           <div class="iq-menu-bt-sidebar">
                              <i class="las la-bars wrapper-menu"></i>
                           </div>
                     </div>
                     <HoverMenu :items="sidebarItems" :sidebarGroupTitle="sidebarGroupTitle" className="iq-menu d-flex mn-center"/>
                  </nav>
               </div>
            <nav class="navbar navbar-expand-lg navbar-light p-0">
                <ModeSwitch/>
                 <b-navbar-toggle target="nav-collapse" class="mr-2 text-primary">
                    <i class="ri-menu-3-line"></i>
                 </b-navbar-toggle>
                  <b-collapse id="nav-collapse" is-nav>
                    <ul class="navbar-nav ml-auto navbar-list align-items-center">
                       
                        <li class="nav-item nav-icon">
                            <div class="iq-search-bar">
                                <form action="#" class="searchbox">
                                    <input type="text" class="text search-input font-size-12 form-control"
                                        placeholder="Type here to search...">
                                    <a class="search-link text-white" href="#"><i class="ri-search-line"></i></a>
                                </form>
                            </div>
                        </li>
                        <li class="nav-item nav-icon dropdown" v-nav-toggle>
                            <a href="#" class="search-toggle dropdown-toggle" id="dropdownMenuButton"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="ri-notification-line"></i>
                                <span class="bg-white dots"></span>
                            </a>
                            <div class="iq-sub-dropdown dropdown-menu" aria-labelledby="dropdownMenuButton">
                                <div class="card shadow-none m-0">
                                    <div class="card-body p-0 ">
                                        <div class="cust-title p-3">
                                            <h5 class="mb-0">All Notifications</h5>
                                        </div>
                                        <div class="p-3">
                                            <a href="#" class="iq-sub-card">
                                                <div class="media align-items-center">
                                                    <div class="">
                                                        <img class="avatar-40 rounded-small"
                                                            src="@/assets/images/user/01.jpg" alt="01">
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0">Emma Watson Barry <small
                                                                class="badge badge-success float-right">New</small></h6>
                                                        <p class="mb-0">95 MB</p>
                                                    </div>
                                                </div>
                                            </a>
                                            <a href="#" class="iq-sub-card">
                                                <div class="media align-items-center">
                                                    <div class="">
                                                        <img class="avatar-40 rounded-small"
                                                            src="@/assets/images/user/02.jpg" alt="02">
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">New customer is join</h6>
                                                        <p class="mb-0">Cyst Barry</p>
                                                    </div>
                                                </div>
                                            </a>
                                            <a href="#" class="iq-sub-card">
                                                <div class="media align-items-center">
                                                    <div class="">
                                                        <img class="avatar-40 rounded-small"
                                                            src="@/assets/images/user/03.jpg" alt="03">
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">Two customer is left</h6>
                                                        <p class="mb-0">Cyst Barry</p>
                                                    </div>
                                                </div>
                                            </a>
                                            <a href="#" class="iq-sub-card">
                                                <div class="media align-items-center">
                                                    <div class="">
                                                        <img class="avatar-40 rounded-small"
                                                            src="@/assets/images/user/04.jpg" alt="04">
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">New Mail from Fenny <small
                                                                class="badge badge-success float-right">New</small></h6>
                                                        <p class="mb-0">Cyst Barry</p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <a class="right-ic btn btn-primary btn-block position-relative p-2" href="#"
                                            role="button">
                                            <div class="dd-icon"><i class="las la-arrow-right mr-0"></i></div>
                                            View All
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </li>
                         <li class="caption-content" v-sidebar-toggle>
                            <a href="#" class="iq-user-toggle">
                                <img src="@/assets/images/user/1.jpg" class="img-fluid rounded" alt="user">
                            </a>
                            <div class="iq-user-dropdown">
                                <div class="card">
                                    <div class="card-header d-flex justify-content-between align-items-center mb-0">
                                    <div class="header-title">
                                        <h4 class="card-title mb-0">Profile</h4>
                                    </div>
                                    <div class="close-data text-right badge badge-primary cursor-pointer"><i class="ri-close-fill"></i></div>
                                    </div>
                                    <div class="data-scrollbar" data-scroll="2">
                                    <div class="card-body">
                                        <div class="profile-header">
                                            <div class="cover-container text-center">
                                                <img :src="image1" alt="profile-bg" class="rounded img-fluid avatar-80">
                                                <div class="profile-detail mt-3">
                                                <h3>{{name}}</h3>
                                                <p class="mb-1">Web designer</p>
                                                </div>
                                               <router-link :to="{name: 'auth.login'}" class="btn btn-primary">Sign Out</router-link>
                                            </div>
                                            <div class="profile-details my-4">
                                                 <router-link :to="{name: 'app.user-profile'}" class="iq-sub-card bg-primary-light rounded-small p-2">
                                                <div class="media align-items-center">
                                                    <div class="rounded iq-card-icon-small">
                                                        <i class="ri-file-user-line"></i>
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">My Profile</h6>
                                                        <p class="mb-0 font-size-12">View personal profile details.</p>
                                                    </div>
                                                </div>
                                                </router-link>
                                               <router-link :to="{ name: 'app.user-profile-edit'}" class="iq-sub-card bg-danger-light rounded-small p-2">
                                                <div class="media align-items-center">
                                                    <div class="rounded iq-card-icon-small">
                                                        <i class="ri-profile-line"></i>
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">Edit Profile</h6>
                                                        <p class="mb-0 font-size-12">Modify your personal details.</p>
                                                    </div>
                                                </div>
                                                </router-link>
                                              <router-link :to="{ name: 'app.user-Account-setting'}" class="iq-sub-card bg-success-light rounded-small p-2">
                                                <div class="media align-items-center">
                                                    <div class="rounded iq-card-icon-small">
                                                        <i class="ri-account-box-line"></i>
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">Account settings</h6>
                                                        <p class="mb-0 font-size-12">Manage your account parameters.</p>
                                                    </div>
                                                </div>
                                                </router-link>
                                               <router-link :to="{ name: 'app.user-privacy-setting'}" class="iq-sub-card bg-info-light rounded-small p-2">
                                                <div class="media align-items-center">
                                                    <div class="rounded iq-card-icon-small">
                                                        <i class="ri-lock-line"></i>
                                                    </div>
                                                    <div class="media-body ml-3">
                                                        <h6 class="mb-0 ">Privacy Settings</h6>
                                                        <p class="mb-0 font-size-12">Control your privacy parameters.</p>
                                                    </div>
                                                </div>
                                                </router-link>
                                            </div>
                                            <div class="personal-details">
                                                <h5 class="card-title mb-3 mt-3">Personal Details</h5>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Birthday</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">3rd March</p>
                                                </div>
                                                </div>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Address</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">Landon</p>
                                                </div>
                                                </div>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Phone</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">(010)987 543 201</p>
                                                </div>
                                                </div>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Email</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">Barry@example.com</p>
                                                </div>
                                                </div>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Twitter</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">@Barry</p>
                                                </div>
                                                </div>
                                                <div class="row align-items-center mb-2">
                                                <div class="col-sm-6">
                                                    <h6>Facebook</h6>
                                                </div>
                                                <div class="col-sm-6">
                                                    <p class="mb-0">@Barry_Tech</p>
                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="p-3"></div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </li>
                    </ul>
                  </b-collapse>
            </nav>
        </div>
    </div>
    <div class="tab-second-menu">
        <div class="d-flex align-items-center justify-content-between">
            <div class="invoice-info">
                <a href="javascript:void(0);" class=" text-body collapsed" data-toggle="collapse"
                    aria-expanded="true">
                    <div class="invoice-text d-flex align-items-center">
                        <div class="avatar-30 border-color rounded"><i class="ri-add-line"></i></div>
                        <span>New Invoice</span>
                    </div>
                </a>
            </div>
            <div class="iq-bottom-horizontal">
                <nav class="iq-sidebar-menu">
                    <ul id="iq-sidebar-toggle1" class="iq-menu d-flex">
                        <li><router-link :to="{ name: 'map.google'}"><i class="las la-map-signs"></i>Google Map</router-link></li>
                        <li><router-link :to="{  name: 'Ui.badges',}"><i class="lab la-atlassian"></i>Badges</router-link></li>
                        <li><router-link :to="{ name: 'Ui.notifications'}"><i class="las la-bell"></i>Notifications</router-link></li>
                        <li><router-link :to="{name: 'controls.form-layout'}"><i class="las la-book"></i>Form Elements</router-link></li>
         
                    </ul>
                </nav>
            </div>
            <div class="follower-info">
                <div class="d-flex align-items-center">
                    <a href="#" class="text-body"><i class="las la-users pr-2"></i>Follwers List</a>
                    <div class="ml-2"><span class="text-success">56 </span>of 426</div>
                </div>
            </div>
            
        </div>
    </div>
</div>
</template>
<script>
import sideBarItem from "@/JsonData/header.json"
import { core } from '@/config/pluginInit'
import { mapGetters } from 'vuex'
export default {
    name:"HeaderStyle15",
    
    data () {
        return{
   
          sidebarItems:sideBarItem,
          sidebarGroupTitle: true,
        }
    },
    computed : {
        ...mapGetters({
            appName: 'appName',
            logo:'darklogo',
            sidelogo:'logo',
             name:'name',
            image1:'image1'
        })
    },
    mounted(){
        core.changesidebar()
    }
}
</script>