<template>

<div :class="`tab-scrollbar-data ` + miniClass ">
    <a href="#" class="iq-tab-toggle" @click="toggleMini" :class="toggleClass">
        <span class="arrow arr-next arr-one"></span>
        <span class="arrow  arr-next arr-two"></span>
    </a>
    <div class="card-header d-flex justify-content-between align-items-center mb-0 p-0 bg-primary">
        <div class="tab-header">
            <div class="tab-container text-center">
                 <tab-nav :pills="true "  id="side-Pills-tab" extraclass="text-center d-flex" role="tablist" >
                    
                        <tab-nav-items :active="true" id="data1" dataToggle="pill" ariaControls="tab-data1" role="tab" :ariaSelected="true">
                            <template v-slot:title>
                            <i  class="ri-wechat-line pr-2"></i>Chats
                             </template>
                         </tab-nav-items>
                        <tab-nav-items :active="false" id="data2"  ariaControls="tab-data2" role="tab" dataToggle="pill" :ariaSelected="false"  >
                             <template v-slot:title>
                                <i  class="ri-chat-settings-line pr-2"></i>Settings
                              </template>
                          </tab-nav-items>

                        <tab-nav-items :active="false" id="data3"  ariaControls="tab-data3" role="tab" dataToggle="pill" :ariaSelected="false"  >
                            <template v-slot:title>
                            <i  class="ri-notification-3-line pr-2"></i>Updates
                            </template>
                        </tab-nav-items>
                 </tab-nav>
            </div>
        </div>
    </div>
    <div id="sidebar-scrollbar" class="data-scrollbar" data-scroll="1">
        <div class="card-body">
            <div class="tab-details">
                <div class="tabs-content">
                    <div id="tab-data1" class="tab-pane fade active show">
                        <div class="chat-info">
                            <ul class="list-inline m-0 p-0">
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/01.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Paige Turner</h5>
                                                <p class="mb-0">7:15<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Hello</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/02.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Anna Mull</h5>
                                                <p class="mb-0">7:30<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Good luck</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/03.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Greta Life</h5>
                                                <p class="mb-0">8:00<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Best theme ever</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/04.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Kusti Franti</h5>
                                                <p class="mb-0">8:30<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Hi</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/05.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>David King</h5>
                                                <p class="mb-0">9:00<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Greate theme ever</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/06.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Jules Boutin</h5>
                                                <p class="mb-0">9:05<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Hello</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/07.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Paul Molive</h5>
                                                <p class="mb-0">9:10<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">How are u?</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/08.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Monty Carlo</h5>
                                                <p class="mb-0">9:30<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Good Work</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="mb-4 pb-2 border-bottom">
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/09.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>Pete Sariya</h5>
                                                <p class="mb-0">10:00<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Hi</p>
                                        </div>
                                    </div>
                                </li>
                                <li>
                                    <div class="d-flex align-items-center">
                                        <div class="user-img">
                                            <img src="@/assets/images/user/10.jpg" alt="user-img"
                                                class="rounded img-fluid avatar-40">
                                        </div>
                                        <div class="media-body ml-3">
                                            <div
                                                class="d-flex align-items-center justify-content-between">
                                                <h5>John Smith</h5>
                                                <p class="mb-0">10:30<span
                                                        class="font-size-12 pl-1">am</span></p>
                                            </div>
                                            <p class="mb-0">Good Luck</p>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div id="tab-data2" class="tab-pane fade">
                        <div class="setting-info">
                            <div class="setting-title">
                                <h5><i class="lab la-dashcube mr-2"></i> Theme Settings</h5>
                            </div>
                            <ul class="list-unstyled">
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Dark Mode</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch1">
                                        <label class="custom-control-label" for="customSwitch1"></label>
                                    </div>
                                </li>
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">RTL</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch2">
                                        <label class="custom-control-label" for="customSwitch2"></label>
                                    </div>
                                </li>
                            </ul>
                            <div class="setting-title">
                                <h5><i class="las la-envelope mr-2"></i> Email Settings</h5>
                            </div>
                            <ul class="list-unstyled">
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Receive Notification</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch3" checked="">
                                        <label class="custom-control-label" for="customSwitch3"></label>
                                    </div>
                                </li>
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Receive Alerts</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch4">
                                        <label class="custom-control-label" for="customSwitch4"></label>
                                    </div>
                                </li>
                            </ul>                           
                            <div class="setting-title">
                                <h5>
                                    <i class="las la-user mr-2"></i> User Settings
                                </h5>
                            </div>
                            <ul class="list-unstyled">
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Receive Updates</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch5">
                                        <label class="custom-control-label" for="customSwitch5"></label>
                                    </div>
                                </li>
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Followers</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch6" checked="">
                                        <label class="custom-control-label" for="customSwitch6"></label>
                                    </div>
                                </li>
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Share</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch7" checked="">
                                        <label class="custom-control-label" for="customSwitch7"></label>
                                    </div>
                                </li>
                                <li class="d-flex justify-content-between set-swtich">
                                    <h6 class="text-body">Likes</h6>
                                    <div class="custom-control custom-switch custom-control-inline mr-0">
                                        <input type="checkbox" class="custom-control-input" id="customSwitch8">
                                        <label class="custom-control-label" for="customSwitch8"></label>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div id="tab-data3" class="tab-pane fade">                        
                        <div class="card bg-success-light">
                            <div class="card-body">
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-success rounded">
                                        <i class="las la-user-friends success"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h3 class="mb-0 text-success">150</h3>
                                        <h5>Good Luck</h5>
                                    </div>
                                </div>
                                <div
                                    class="d-flex align-items-center justify-content-between mt-5 position-relative">
                                  
                                       <Progressbar :value="85" marginclass="bg-white mt-2"  color="success" midclass="iq-progress progress-1" >
                                            <template v-slot:text>
                                            <span
                                                class="progress-text-one bg-success">85%</span>
                                            </template>
                                       </Progressbar>
                                </div>
                            </div>
                        </div>                                                                     
                        <ul class="list-unstyled">
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>India</h6>
                                    <h6>75%</h6>
                                </div>
                               
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                      <Progressbar :value="75"  color="success" /> 
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>U.S.A</h6>
                                    <h6>55%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                     <Progressbar :value="55"  color="primary" /> 
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>Canada</h6>
                                    <h6>85%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                     <Progressbar :value="85"  color="warning" /> 
                                    
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>London</h6>
                                    <h6>50%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                       <Progressbar :value="50"  color="info" /> 
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>Europe</h6>
                                    <h6>60%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                     <Progressbar :value="60"  color="primary" /> 
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>Japan</h6>
                                    <h6>65%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                       <Progressbar :value="65"  color="danger" /> 
                                   
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex justify-content-between">
                                    <h6>Australia</h6>
                                    <h6>30%</h6>
                                </div>
                                <div class="iq-progress-bar-linear d-inline-block mt-1 w-100">
                                     <Progressbar :value="30"  color="black" />
                                    
                                </div>
                            </li>   
                        </ul>                              
                    </div>
                </div>
            </div>
        </div>
        <div class="p-3"></div>
    </div>
</div>
</template>
<script>
import { core } from '../../../../config/pluginInit'
export default {
    name: 'RightChatPanel',
    mounted(){
     core.SmoothScrollbar()
    },
    data () {
    return {
      rightSideBarMini: false,
      miniClass: ' tab-sidebar-close',
      toggleClass : ''
    }
  },
  methods: {
    toggleMini () {
      this.rightSideBarMini = !this.rightSideBarMini
      this.checkRightSideBar()
    },
    checkRightSideBar () {
      if (this.rightSideBarMini) {
        this.miniClass = 'tab-sidebar-close',
        this.toggleClass = ''
      } else {
        this.miniClass = '',
        this.toggleClass = ' active'
      }
    }
    }
}
</script>