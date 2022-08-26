<template>
     <div class="header-style-4">
   <div class="iq-top-navbar">
      <div class="container">            
         <div class="iq-navbar-custom d-flex align-items-center justify-content-between">
            <div class="iq-navbar-logo d-flex align-items-center justify-content-between">
               <i class="ri-menu-line wrapper-menu"></i>
                <router-link to="/" class="header-logo">
                <img :src="logo" class="img-fluid rounded-normal" alt="logo">
                </router-link>              
               <div class="iq-search-bar device-search">
                  <form action="#" class="searchbox">
                     <input type="text" class="text search-input" placeholder="Type here to search...">
                     <a class="search-link" href="#"><i class="ri-search-line"></i></a>
                  </form>
               </div>
            </div>
            <div class="iq-sidebar-top">
                <div class="top-menu-icon">
                    <ul class="list-inline d-flex align-items-center justify-content-between m-0 p-0">
                        <li class="menu-icon">
                           <router-link to="/" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Home"><i class="las la-home"></i></router-link>
                        </li>
                        <li class="menu-icon">
                                <router-link :to="{ name: 'app.user-profile',}" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Profile"><i class="las la-user-circle"></i></router-link>
                        </li>
                        <li class="menu-icon">
                                <router-link :to="{name: 'app.email-listing'}" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Email"><i class="las la-envelope-open"></i></router-link>
                        </li>
                        <li class="menu-icon">
                                <router-link :to="{ name: 'app.chat'}" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Chat"><i class="lab la-rocketchat"></i></router-link>
                        </li>
                        <li class="menu-icon">
                                <router-link :to="{ name: 'contact.list'}" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Contact"><i class="las la-file-alt"></i></router-link>
                        </li>
                    </ul>
                </div>
            </div>
            <nav class="navbar navbar-expand-lg navbar-light px-0">
               <ModeSwitch/>
               <b-navbar-toggle target="nav-collapse" class="mr-2 text-primary">
               <i class="ri-menu-3-line"></i>
               </b-navbar-toggle>                        
                <b-collapse id="nav-collapse" is-nav>
                  <ul class="navbar-nav ml-auto navbar-list align-items-center">                     
                     <li class="nav-item nav-icon search-content">
                        <a href="#" class="search-toggle rounded" id="dropdownSearch" data-toggle="dropdown"
                           aria-haspopup="true" aria-expanded="false">
                        <i class="ri-search-line"></i>
                        </a>
                        <div class="iq-search-bar iq-sub-dropdown dropdown-menu" aria-labelledby="dropdownSearch">
                           <form action="#" class="searchbox p-2">
                              <div class="form-group mb-0 position-relative">
                                 <input type="text" class="text search-input" placeholder="type here to search...">
                                 <a href="#" class="search-link"><i class="ri-search-line"></i></a>
                              </div>
                           </form>
                        </div>
                     </li>
                     <li class="nav-item nav-icon dropdown" v-nav-toggle>
                        <a href="#" class="search-toggle dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown"
                           aria-haspopup="true" aria-expanded="false">
                        <i class="ri-notification-line"></i>
                        <span class="bg-primary dots"></span>
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
                                             <img class="avatar-40 rounded-small" src="@/assets/images/user/01.jpg" alt="">
                                          </div>
                                          <div class="media-body ml-3">
                                             <h6 class="mb-0">Emma Watson Barry <small class="badge badge-success float-right">New</small>
                                             </h6>
                                             <p class="mb-0">95 MB</p>
                                          </div>
                                       </div>
                                    </a>
                                    <a href="#" class="iq-sub-card">
                                       <div class="media align-items-center">
                                          <div class="">
                                             <img class="avatar-40 rounded-small" src="@/assets/images/user/02.jpg" alt="">
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
                                             <img class="avatar-40 rounded-small" src="@/assets/images/user/03.jpg" alt="">
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
                                             <img class="avatar-40 rounded-small" src="@/assets/images/user/04.jpg" alt="">
                                          </div>
                                          <div class="media-body ml-3">
                                             <h6 class="mb-0 ">New Mail from Fenny <small class="badge badge-success float-right">New</small>
                                             </h6>
                                             <p class="mb-0">Cyst Barry</p>
                                          </div>
                                       </div>
                                    </a>
                                 </div>
                                 <a class="right-ic btn btn-primary btn-block position-relative p-2" href="#" role="button">
                                    <div class="dd-icon"><i class="las la-arrow-right mr-0"></i></div>
                                    View All
                                 </a>
                              </div>
                           </div>
                        </div>
                     </li>
                     <li class="nav-item nav-icon dropdown" v-nav-toggle>
                        <a href="#" class="search-toggle rounded dropdown-toggle" id="dropdownMenuButton3"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="ri-shopping-cart-2-line"></i>
                        <span class="badge badge-danger count-cart rounded">3</span>
                        </a>
                        <div class="iq-sub-dropdown dropdown-menu" aria-labelledby="dropdownMenuButton3">
                           <div class="card shadow-none m-0">
                              <div class="card-body p-0 toggle-cart-info">
                                 <div class="cust-title d-flex align-items-center justify-content-between p-3">
                                    <h5 class="mb-0">Your Cart</h5>
                                    <h5 class="badge bg-primary-light text-primary p-2">Total: <strong>$214</strong></h5>
                                 </div>
                                 <div class="p-3">
                                    <a href="#" class="iq-sub-card">
                                       <div class="media align-items-center">
                                          <div class="crt-img">
                                             <img class="rounded-small avatar-40" src="@/assets/images/layouts/layout-9/05.png" alt="">
                                          </div>
                                          <div class="media-body ml-3">
                                             <h6 class="mb-0 ">Night People book</h6>
                                             <p class="mb-0">$32</p>
                                          </div>
                                          <div class="float-right font-size-24 text-danger"><i class="las la-trash-alt"></i></div>
                                       </div>
                                    </a>
                                    <a href="#" class="iq-sub-card">
                                       <div class="media align-items-center">
                                          <div class="crt-img">
                                             <img class="rounded-small" src="@/assets/images/layouts/layout-9/08.png" alt="">
                                          </div>
                                          <div class="media-body ml-3">
                                             <h6 class="mb-0 ">The Sin Eater Book</h6>
                                             <p class="mb-0">$40</p>
                                          </div>
                                          <div class="float-right font-size-24 text-danger"><i class="las la-trash-alt"></i></div>
                                       </div>
                                    </a>
                                    <a href="#" class="iq-sub-card">
                                       <div class="media align-items-center">
                                          <div class="crt-img">
                                             <img class="rounded-small" src="@/assets/images/layouts/layout-9/06.png" alt="">
                                          </div>
                                          <div class="media-body ml-3">
                                             <h6 class="mb-0 ">the Orange Tree</h6>
                                             <p class="mb-0">$30</p>
                                          </div>
                                          <div class="float-right font-size-24 text-danger"><i class="las la-trash-alt"></i></div>
                                       </div>
                                    </a>
                                 </div>
                                 <div class="d-flex align-items-center text-center">
                                    <a class="right-ic btn btn-primary btn-block position-relative p-2" href="#" role="button">
                                       <div class="dd-icon"><i class="las la-arrow-right mr-0"></i></div>
                                       Checkout
                                    </a>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </li>
                     <Fullscreen />
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
                                                <img src="image1" alt="profile-bg" class="rounded img-fluid avatar-80">
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
      <div class="pay-horizontal">
         <div class="container">           
            <div class="white-bg-menu">
               <div class="iq-menu-horizontal">
                  <nav class="iq-sidebar-menu">
                     <div class="iq-sidebar-logo d-flex align-items-center justify-content-between">
                           <router-link to="/" class="header-logo">
                              <img :src="logo" class="img-fluid rounded-normal" alt="logo">
                           </router-link> 
                           <div class="iq-menu-bt-sidebar"> 
                              <i class="las la-bars wrapper-menu"></i>
                           </div>
                     </div>
                     <HoverMenu :items="sidebarItems" :sidebarGroupTitle="sidebarGroupTitle" className="iq-menu d-flex mn-center"  :enableCustomIcon="true" />
                  </nav>
               </div>
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
import Fullscreen    from '../../../fullscreen/Fullscreen'
export default {
    name:"HeaderStyle16",
   components:{Fullscreen},
    data () {
        return{
          sidebarItems:sideBarItem,
          sidebarGroupTitle: true,
        }
    },
    computed : {
        ...mapGetters({
            appName: 'appName',
            logo:'logo',
            name:'name',
            image1:'image1'
        })
    },
    mounted(){
       core.changesidebar()
    }
}
</script>