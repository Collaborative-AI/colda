<template>
    <div class="iq-top-navbar border-navbar">
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
                     <img :src="logo" class="img-fluid rounded-normal" alt="logo">
                  </router-link> 
                  <div class="iq-menu-bt-sidebar">
                     <i class="las la-bars wrapper-menu"></i>
                  </div>
            </div>
            <HoverMenu :items="sidebarItems" :sidebarGroupTitle="sidebarGroupTitle" className="iq-menu d-flex" />
         </nav>
      </div>
   
      <nav class="navbar navbar-expand-lg navbar-light p-0">
         <ModeSwitch/>
           <b-navbar-toggle target="nav-collapse" class="mr-2 text-primary">
         <i class="ri-menu-3-line"></i>
           </b-navbar-toggle>
         <b-collapse id="nav-collapse" is-nav>
            <ul class="navbar-nav ml-auto navbar-list align-items-center">
               
               <li class="nav-item nav-icon search-content" v-nav-toggle>
                  <a href="#" class="search-toggle dropdown-toggle" id="dropdownSearch" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="ri-search-line"></i>
                  </a>
                  <div class="iq-search-bar iq-sub-dropdown dropdown-menu" aria-labelledby="dropdownSearch">
                     <form action="#" class="searchbox p-2">
                        <div class="form-group mb-0 position-relative">
                           <input type="text" class="text search-input font-size-12" placeholder="type here to search...">
                           <a href="#" class="search-link"><i class="ri-search-line"></i></a>
                        </div>
                     </form>
                  </div>
               </li>
               <li class="nav-item nav-icon dropdown" v-nav-toggle>
                  <a href="#" class="search-toggle dropdown-toggle" id="dropdownMenuButton2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="ri-mail-line"></i>
                  <span class="bg-primary count-mail"></span>
                  </a>
                  <div class="iq-sub-dropdown dropdown-menu" aria-labelledby="dropdownMenuButton2">
                     <div class="card shadow-none m-0">
                        <div class="card-body p-0 ">
                           <div class="cust-title p-3">
                              <h5 class="mb-0">All Messages</h5>
                           </div>
                           <div class="p-3">
                              <a href="#" class="iq-sub-card">
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/01.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0">Barry Emma Watson <small class="badge badge-success float-right">New</small></h6>
                                       <small class="float-left font-size-12">12:00 PM</small>
                                    </div>
                                 </div>
                              </a>
                              <a href="#" class="iq-sub-card">
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/02.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0 ">Lorem Ipsum Watson</h6>
                                       <small class="float-left font-size-12">20 Apr</small>
                                    </div>
                                 </div>
                              </a>
                              <a href="#" class="iq-sub-card">
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/03.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0 ">Why do we use it? <small class="badge badge-success float-right">New</small></h6>
                                       <small class="float-left font-size-12">1:24 PM</small>
                                    </div>
                                 </div>
                              </a>
                              <a href="#" class="iq-sub-card" >
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/04.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0">Variations Passages <small class="badge badge-success float-right">New</small></h6>
                                       <small class="float-left font-size-12">5:45 PM</small>
                                    </div>
                                 </div>
                              </a>
                              <a href="#" class="iq-sub-card" >
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/05.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0 ">Lorem Ipsum generators</h6>
                                       <small class="float-left font-size-12">1 day ago</small>
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
                  <a href="#" class="search-toggle dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
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
                              <a href="#" class="iq-sub-card" >
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/01.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0">Emma Watson Barry <small class="badge badge-success float-right">New</small></h6>                                             
                                       <p class="mb-0">95 MB</p>
                                    </div>
                                 </div>
                              </a>
                              <a href="#" class="iq-sub-card" >
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
                              <a href="#" class="iq-sub-card" >
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
                              <a href="#" class="iq-sub-card" >
                                 <div class="media align-items-center">
                                    <div class="">
                                       <img class="avatar-40 rounded-small" src="@/assets/images/user/04.jpg" alt="">
                                    </div>
                                    <div class="media-body ml-3">
                                       <h6 class="mb-0 ">New Mail from Fenny <small class="badge badge-success float-right">New</small></h6>                                             
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
   <div class="box-ecommerce mt-3">
      <div class="row">
         <div class="col-lg-12 col-xl-4 box-ecommerce-list">
            <div class="card card-block card-stretch card-height  card-transparent">
               <div class="mb-4">
                  <h2>Campaigns</h2>
                  <p class="mb-0 line-height">Hello Tam, welcome back !</p>
               </div>               
               <div class="card-body p-0">
                  <div class="user-data-block media align-items-center mb-3">
                     <img src="@/assets/images/user/03.jpg" class="img-fluid avatar-120 rounded"
                           alt="">
                     <div class="media-body ml-3">                                 
                        <h4 class="mb-1">Tam Jaguar</h4>
                        <p class="text-break line-height mb-2">tamjague001@example.com</p>
                        <div class="d-flex doc-social">
                           <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                           <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                           <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                        </div>
                     </div> 
                  </div>  
                     <p class="mb-0 line-height">Lorem Ipsum is simply dummy text of the printing and<br> typesetting industry.</p>
                  <div class="ecomm-p d-flex flex-md-row flex-column mt-4">                              
                     <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-warning-light rounded-small svg-warning">
                           <svg width="32" height="32" class="svg-white" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path
                                 d="M32 32L30.7692 6.65181H25.723V5.04528C25.7231 2.26327 23.0856 0 19.8437 0C16.6019 0 13.9645 2.26327 13.9645 5.04528V6.65187H8.91839L8.57951 13.6215H0V31.9967L32 32ZM19.8435 30.125V28.0876H29.6232L29.7221 30.125H19.8435ZM16.1494 5.04528C16.1494 3.29719 17.8067 1.87496 19.8437 1.87496C21.8808 1.87496 23.5381 3.29712 23.5381 5.04528V6.65187H16.1494V5.04528ZM11.0141 8.52677H13.9645V10.2854H16.1494V8.52677H23.5381V10.2854H25.723V8.52677H28.6733L29.5322 26.2126H19.8435V13.6214H10.7664L11.0141 8.52677ZM6.96334 15.4964H12.8801V17.6653C12.8801 19.0651 11.553 20.204 9.92169 20.204C8.29045 20.204 6.96334 19.0651 6.96334 17.6653V15.4964ZM17.6586 30.1217H2.1849V15.4964H4.77844V17.6653C4.77844 20.099 7.08569 22.0789 9.92176 22.0789C12.7578 22.0789 15.065 20.099 15.065 17.6653V15.4964H17.6586V30.1217Z"
                                    />
                           </svg>
                        </div>
                        <div class="media-body ml-1">
                           <h3>20 K</h3>
                           <p class="mb-0 line-height">Item Buy</p>
                        </div>
                     </div> 
                     <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-info-light rounded-small svg-info">
                           <svg width="32" height="32" viewBox="0 0 32 32" class="svg-white" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M30.0134 17.1011V29.9089H6.66935V17.1011H30.0134ZM32.0001 15.01H4.68262V32H32.0001V15.01Z" />
                              <path
                                 d="M24.5498 15.01L27.3461 17.9532C27.325 18.0617 27.284 18.1623 27.284 18.2773C27.284 19.2144 28.0055 19.9724 28.8958 19.9724C29.005 19.9724 29.0994 19.9293 29.2025 19.9084L32 22.8515V15.01H24.5498Z" />
                              <path
                                 d="M26.4125 25.2014C27.3027 25.2014 28.0243 24.4419 28.0243 23.505C28.0243 22.5682 27.3027 21.8087 26.4125 21.8087C25.5224 21.8087 24.8008 22.5682 24.8008 23.505C24.8008 24.4419 25.5224 25.2014 26.4125 25.2014Z" />
                              <path
                                 d="M18.3412 27.9669C21.0336 27.9669 23.2162 25.9693 23.2162 23.505C23.2162 21.0408 21.0336 19.0432 18.3412 19.0432C15.6489 19.0432 13.4663 21.0408 13.4663 23.505C13.4663 25.9693 15.6489 27.9669 18.3412 27.9669Z" />
                              <path
                                 d="M10.2702 25.2001C11.1596 25.2001 11.8807 24.4412 11.8807 23.505C11.8807 22.5688 11.1596 21.8099 10.2702 21.8099C9.38071 21.8099 8.65967 22.5688 8.65967 23.505C8.65967 24.4412 9.38071 25.2001 10.2702 25.2001Z" />
                              <path
                                 d="M4.68262 22.8515L7.47894 19.9084C7.582 19.9306 7.67761 19.9737 7.78688 19.9737C8.67718 19.9737 9.39737 19.2144 9.39737 18.2773C9.39737 18.1623 9.3564 18.063 9.33529 17.9545L12.1329 15.01H4.68262V22.8515Z" />
                              <path
                                 d="M9.39862 28.7327C9.39862 27.7956 8.67718 27.0376 7.78688 27.0376C7.67761 27.0376 7.58324 27.0807 7.48018 27.1016L4.68262 24.1584V32H12.1329L9.33653 29.0568C9.35764 28.9483 9.39862 28.8464 9.39862 28.7327Z" />
                              <path
                                 d="M28.8958 27.0363C28.0055 27.0363 27.2853 27.7956 27.2853 28.7327C27.2853 28.8477 27.3263 28.947 27.3474 29.0555L24.5498 32H32V24.1584L29.2037 27.1016C29.1007 27.0794 29.005 27.0363 28.8958 27.0363Z" />
                              <path
                                 d="M22.9381 11.97C23.8276 11.97 24.5486 11.2111 24.5486 10.2749C24.5486 9.33878 23.8276 8.57986 22.9381 8.57986C22.0487 8.57986 21.3276 9.33878 21.3276 10.2749C21.3276 11.2111 22.0487 11.97 22.9381 11.97Z" />
                              <path
                                 d="M2.81991 15.01C2.81991 13.9279 3.65434 13.0496 4.68247 13.0496H5.70067L5.74661 12.8823L20.1218 4.59645L21.2208 4.93363C21.2518 5.03819 21.263 5.14797 21.3164 5.2486C21.7435 6.07196 22.722 6.37125 23.5042 5.92167C23.5986 5.86678 23.6632 5.78183 23.7414 5.70994L24.8428 6.04974L27.3473 10.8618L27.0257 12.0198C26.9276 12.0511 26.8233 12.0629 26.7277 12.1178C26.3639 12.3269 26.1218 12.6693 25.9939 13.0496H30.7508L27.5398 6.87703H27.541L23.9612 0L17.4249 3.76655H17.4261L6.5351 10.0437L0 13.8103L2.81991 19.2301V15.01Z" />
                              <path
                                 d="M13.8216 10.4437C12.74 11.0658 11.9615 12.0094 11.5244 13.0497H20.5057C20.4337 12.6511 20.3256 12.2603 20.1344 11.8931C19.0082 9.73143 16.1833 9.0832 13.8216 10.4437Z" />
                           </svg>
                        </div>
                        <div class="media-body ml-1">
                           <h3>$ 123</h3>
                           <p class="mb-0 line-height">Spend in Total</p>
                        </div>
                     </div>                                
                  </div>                      
               </div>
            </div>                     
         </div>
         <div class="col-md-6 col-xl-4 box-ecommerce-list">
            <div class="card card-block card-stretch card-height card-transparent">
               <div class="card-header d-flex justify-content-between">
                  <div class="header-title mr-md-0 mr-2">
                     <h4 class="card-title">Progress</h4>
                  </div>
               </div>
               <div class="card-body p-0">
                  <ApexChart element="ecommerce2-chart-03" :chartOption="chart11" />
               </div>
            </div>
         </div> 
         <div class="col-md-6 col-xl-4 box-ecommerce-list">
            <div class="card card-block card-stretch card-height card-transparent">
               <div class="card-header d-flex justify-content-between">
                  <div class="header-title mr-md-0 mr-2">
                     <h4 class="card-title">Top Sell Product List</h4>
                  </div>
               </div>
               <div class="card-body p-0">
                  <ul class="list-inline p-0 m-0">
                     <li class="mb-3">
                        <div class="d-flex align-items-center justify-content-between" style="">
                           <div class="d-flex align-items-center">
                              <a href="JavaScript:Void(0);"><img src="@/assets/images/layouts/layout-13/product/1.png" class="img-fluid avatar-60 rounded-small"
                                    alt=""></a>
                              <div class="ml-4">
                                 <h5>Nike Shoes</h5>
                                 <p class="mb-0">257 Product Sold</p>
                              </div>
                           </div>
                           <div class="icon-arrow bg-success-light rounded"><i class="las la-long-arrow-alt-up text-success"></i></div>
                        </div>
                     </li>
                     <li class="mb-3">
                        <div class="d-flex align-items-center justify-content-between" style="">
                           <div class="d-flex align-items-center">
                              <a href="JavaScript:Void(0);"><img src="@/assets/images/layouts/layout-13/product/2.png" class="img-fluid avatar-60 rounded-small"
                                    alt=""></a>
                              <div class="ml-4">
                                 <h5>Adidas Shoes</h5>
                                 <p class="mb-0">255 Product Sold</p>
                              </div>
                           </div>
                           <div class="icon-arrow bg-success-light rounded"><i class="las la-long-arrow-alt-up text-success"></i></div>
                        </div>
                     </li>
                     <li class="mb-3">
                        <div class="d-flex align-items-center justify-content-between" style="">
                           <div class="d-flex align-items-center">
                              <a href="JavaScript:Void(0);"><img src="@/assets/images/layouts/layout-13/product/3.png" class="img-fluid avatar-60 rounded-small"
                                    alt=""></a>
                              <div class="ml-4">
                                 <h5>Caprese Bag</h5>
                                 <p class="mb-0">230 Product Sold</p>
                              </div>
                           </div>
                           <div class="icon-arrow bg-danger-light rounded"><i class="las la-long-arrow-alt-down text-danger"></i></div>
                        </div>
                     </li>
                     <li class="mb-3">
                        <div class="d-flex align-items-center justify-content-between" style="">
                           <div class="d-flex align-items-center">
                              <a href="JavaScript:Void(0);"><img src="@/assets/images/layouts/layout-13/product/4.png"
                                    class="img-fluid avatar-60 rounded-small" alt=""></a>
                              <div class="ml-4">
                                 <h5>Swank Watch</h5>
                                 <p class="mb-0">200 Product Sold</p>
                              </div>
                           </div>
                           <div class="icon-arrow bg-danger-light rounded"><i class="las la-long-arrow-alt-down text-danger"></i></div>
                        </div>
                     </li>
                     <li class="">
                        <div class="d-flex align-items-center justify-content-between" style="">
                           <div class="d-flex align-items-center">
                              <a href="JavaScript:Void(0);"><img src="@/assets/images/layouts/layout-13/product/5.png" class="img-fluid avatar-60 rounded-small"
                                    alt=""></a>
                              <div class="ml-4">
                                 <h5>wallet wear</h5>
                                 <p class="mb-0">200 Product Sold</p>
                              </div>
                           </div>
                           <div class="icon-arrow bg-success-light rounded"><i class="las la-long-arrow-alt-up text-success"></i></div>
                        </div>
                     </li>
                  </ul>
               </div>
            </div>
         </div>
      </div>                
   </div>
</div>
</template>
<script>
import Fullscreen    from '../../../fullscreen/Fullscreen'
import ApexChart from '../../../../components/charts/ApexChart'
import sideBarItem from "@/JsonData/header.json"
import { core } from '@/config/pluginInit'
import { mapGetters } from 'vuex'
export default {
    name:"HeaderStyle13",
    components:{
Fullscreen,
       ApexChart
    },
    data () {
        return{
          
          sidebarItems:sideBarItem,
          sidebarGroupTitle: true,
          chart11: {
            series: [{
      name: 'Week',
      data: [80, 50, 30, 40, 100, 20],
    }, {
      name: 'Month',
      data: [20, 30, 40, 80, 20, 80],
    }, {
      name: 'Year',
      data: [44, 76, 78, 13, 43, 10],
    }],
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      height: 350,
      type: 'radar',
      dropShadow: {
        enabled: true,
        blur: 1,
        left: 1,
        top: 1
      }
    },
    
    stroke: {
      width: 2
    },
    fill: {
      opacity: 0.1
    },
    markers: {
      size: 0
    },
    xaxis: {
      categories: ['2011', '2012', '2013', '2014', '2015', '2016']
    }
        },
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