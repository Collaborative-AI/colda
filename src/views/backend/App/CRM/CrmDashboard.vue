<template>
     <div class="container-fluid crm1">
         <b-row >
            <b-col lg="2" md="6">
               <card class=" card-block card-stretch card-height">
                   <template v-slot:body>
                     <div class="top-block ">
                        <div class="bg-primary-light icon iq-icon-box-2 mr-2 rounded mb-3">
                           <i class="las la-golf-ball"></i>
                        </div>
                        <span>New Sales</span>
                        <h4 class="mt-1">Equipments</h4>
                        <p class="mb-0 text-success increse"><i class="ri-arrow-right-up-line"></i> 20% Increased</p>
                     </div>
                   </template>
               </card>
            </b-col>
            <b-col lg="2" md="6">
               <card class=" card-block card-stretch card-height">
                  <template v-slot:body>
                     <div class="top-block ">
                        <div class="bg-danger-light icon iq-icon-box-2 mr-2 rounded mb-3">
                           <i class="las la-hand-holding-usd"></i>
                        </div>
                        <span>Shares</span>
                        <h4 class="mt-1">Accessories</h4>
                        <p class="mb-0 text-danger increse"><i class="ri-arrow-left-down-line"></i>6% Decreased</p>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="2" md="6">
               <card class=" card-block card-stretch card-height">
                   <template v-slot:body>
                     <div class="top-block ">
                        <div class="bg-info-light icon iq-icon-box-2 mr-2 rounded mb-3">
                           <i class="las la-dharmachakra"></i>
                        </div>
                        <span>Partners</span>
                        <h4 class="mt-1">Project Name</h4>
                        <p class="mb-0 text-success increse"><i class="ri-arrow-right-up-line"></i>12.5% Increased</p>
                     </div>
                   </template>
               </card>
            </b-col>
           <b-col lg="2" md="6">
               <card class=" card-block card-stretch card-height">
                   <template v-slot:body>
                     <div class="top-block ">
                        <div class="bg-warning-light icon iq-icon-box-2 mr-2 rounded mb-3">
                           <i class="las la-funnel-dollar"></i>
                        </div>
                        <span>Regular Sales</span>
                        <h4 class="mt-1">Project Name</h4>
                        <p class="mb-0 text-danger increse"><i class="ri-arrow-right-down-line"></i>3.5% Decreased</p>
                     </div>
                   </template>
               </card>
            </b-col>
            <b-col lg="4" >
               <card class=" card-block card-stretch card-height bg-danger">
                  <template v-slot:body>
                     <div class="d-flex justify-content-between">
                        <div class="bg-warning-light icon iq-icon-box-2 rounded mb-3">
                           <i class="las la-signal"></i>
                        </div>
                        <div class="card-header-toolbar d-flex align-items-center">
                           <div class="bg-danger-light icon iq-icon-box-3 rounded-circle">
                             <a href="#" id="dropdownMenuReport" data-toggle="dropdown">
                                 <i class="ri-more-2-fill font-size-20"></i>
                             </a> 
                           <div class="dropdown-menu shadow-none" aria-labelledby="dropdownMenuReport">
                              <a class="dropdown-item" href="#"><i class="ri-eye-fill mr-2"></i>View</a>
                              <a class="dropdown-item" href="#"><i class="ri-delete-bin-6-fill mr-2"></i>Delete</a>
                              <a class="dropdown-item" href="#"><i class="ri-pencil-fill mr-2"></i>Edit</a>
                           </div>
                           </div>
                        </div>
                     </div>
                     <div class="top-block-danger ">
                        <h4 class="mb-1">Weekly Report</h4>
                        <p class="mb-0">Today, December 08th</p>
                        <p class="mb-0">10:30 - 12:00 am</p>
                        <div class="d-flex justify-content-between align-items-center mt-3">
                           <div class="iq-media-group d-flex align-items-center">
                              <a href="#" class="iq-media">
                                 <img class="img-fluid avatar-30 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                              </a>
                              <a href="#" class="iq-media">
                                 <img class="img-fluid avatar-30 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                              </a>
                              <a href="#" class="iq-media">
                                 <img class="img-fluid avatar-30 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                              </a>
                           </div>
                           <div class="d-flex align-items-end">
                              <span class="mr-3"><i class="las la-paperclip"></i> 12</span>
                              <span class="badge badge-pill bg-danger-light"><i class="las la-exclamation-triangle"></i>
                                 Low</span>
                           </div>
                        </div>
                     </div>
                  </template>
               </card>
            </b-col>
         </b-row>
         <b-row >
            <b-col lg="6" >
               <card class=" card-block card-stretch card-height" headerClass="align-items-center">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Sales Leads and Campaigns</h4>
                  </template>
                      <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle dropdown-bg bg-primary-light p-2" id="dropdownMenuButton5"
                              data-toggle="dropdown" aria-expanded="false" role="button">
                              This Year<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                           </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                      </template>
                  
                   <template v-slot:body>
                       <ApexChart element="crm1-chart-01" :chartOption="chart1" />
                     
                   </template>
               </card>
            </b-col>
             <b-col lg="6" >
               <card class=" card-block bg-primary-light card-stretch card-height" headerClass="light-title">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Sales Forecast</h4>
                 </template>
                  <template v-slot:headerAction>
                     <p class="mb-0 text-primary">More <i class="ri-arrow-right-line"></i></p>
                  </template>
                   <template v-slot:body>
                     <b-row >
                        <b-col lg="6" md="6" >
                           <card>
                             <template v-slot:body>
                                 <div class="top-block ">
                                    <div class="bg-primary icon iq-icon-box-3 badge-primary mr-2">
                                       <i class="las la-users-cog"></i>
                                    </div>
                                 </div>
                                 <div class="d-flex justify-content-between align-items-center forcast-graph">
                                    <div class="">
                                       <p class="mb-1">Revenue</p>
                                       <h4>+32.6%</h4>
                                    </div>
                                    <div class="d-flex align-items-end">
                                        <ApexChart element="crm1-chart-02" :chartOption="chart2" />
                                      
                                    </div>
                                 </div>
                             </template>
                           </card>
                        </b-col>
                        <b-col lg="6" md="6" >
                           <card>
                             <template v-slot:body>
                                 <div class="top-block ">
                                    <div class="bg-success icon iq-icon-box-3 mr-2">
                                       <i class="las la-chart-bar"></i>
                                    </div>
                                 </div>
                                 <div class="d-flex justify-content-between align-items-center forcast-graph">
                                    <div class="">
                                       <p class="mb-1">Net Profit</p>
                                       <h4>+12.4%</h4>
                                    </div>
                                    <div class="d-flex align-items-end">
                                       <ApexChart element="crm1-chart-03" :chartOption="chart3" />
                                    </div>
                                 </div>
                             </template>
                           </card>
                        </b-col>
                        <b-col lg="6" md="6" >
                           <card class=" mb-lg-0 mb-md-0">
                              <template v-slot:body>
                                 <div class="top-block ">
                                    <div class="bg-danger icon iq-icon-box-3 mr-2">
                                       <i class="lab la-first-order-alt"></i>
                                    </div>
                                 </div>
                                 <div class="d-flex justify-content-between align-items-center forcast-graph">
                                    <div class="">
                                       <p class="mb-1">Orders</p>
                                       <h4>-2.4%</h4>
                                    </div>
                                    <div class="d-flex align-items-end">
                                       <ApexChart element="crm1-chart-04" :chartOption="chart4" />
                                       
                                    </div>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                        <b-col lg="6" md="6">
                           <card class=" mb-md-0 mb-sm-0 mb-0 mb-lg-0">
                              <template v-slot:body>
                                 <div class="top-block ">
                                    <div class="bg-warning icon iq-icon-box-3 mr-2">
                                       <i class="lar la-user"></i>
                                    </div>
                                 </div>
                                 <div class="d-flex justify-content-between align-items-center forcast-graph">
                                    <div class="">
                                       <p class="mb-1">Visitors</p>
                                       <h4>+24.8%</h4>
                                    </div>
                                    <div class="d-flex align-items-end">
                                        <ApexChart element="crm1-chart-05" :chartOption="chart5" />
                                    </div>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                     </b-row>
                   </template>
               </card>
            </b-col>
         </b-row>
         <b-row>
            <b-col lg="4" md="6" >
               <card class=" card-block card-stretch card-height" headerClass="align-items-center">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Recap Stat</h4>
                  </template>
                     <template v-slot:headerAction>
                       <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg bg-primary-light p-2" id="dropdownMenuButton6"
                              data-toggle="dropdown" aria-expanded="false" role="button">
                              Year<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                           </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                     </template>
                 <template v-slot:body>
                     <ApexChart element="crm1-chart-06" :chartOption="chart6" />
                     
                 </template>
               </card>
            </b-col>
             <b-col lg="2" md="6" >
               <card class=" card-block card-stretch card-height bg-danger progress-first">
                  <h4 class="card-title text-center mt-3">Progress</h4>
                 <template v-slot:body>
                     <div>
                        <div class="progress-round income-progress m-auto" data-value="50">
                           <span class="progress-left">
                              <span class="progress-bar border-white" style="transform: rotate(108deg);"></span>
                           </span>
                           <span class="progress-right">
                              <span class="progress-bar border-white" style="transform: rotate(180deg);"></span>
                           </span>
                           <div class="progress-value w-100 h-100 rounded d-flex align-items-center justify-content-center text-center">
                              <div class="h4 mb-0">50</div>
                           </div>
                        </div>
                     </div>
                     <hr class="border-transparent">
                     <h3>30%</h3>
                     <p class="mb-0">Last week</p>
                     <div class="d-flex justify-content-between align-items-center  mt-3">
                        <span>Status</span>
                        <div class="d-flex align-items-end">
                           <span><i class="ri-bar-chart-grouped-fill ic-size line-height"></i></span>
                        </div>
                     </div>
                 </template>
               </card>
            </b-col>
             <b-col lg="2" md="6" >
               <card class=" card-block card-stretch card-height-half">
                  <template v-slot:body>
                     <h3>60+</h3>
                     <p class="mb-0">Projects</p>
                     <div class="d-flex justify-content-between align-items-center mt-3">
                        <span class="text-primary">Status</span>
                        <div class="d-flex align-items-end">
                           <span><i class="ri-bar-chart-grouped-fill ic-size line-height text-primary"></i></span>
                        </div>
                     </div>
                  </template>
               </card>
               <card class=" card-block card-stretch card-height-half">
                  <template v-slot:body>
                     <h3>45+</h3>
                     <p class="mb-0">Clients</p>
                     <div class="d-flex justify-content-between align-items-center mt-3">
                        <span class="text-danger">Status</span>
                        <span class="d-flex align-items-end">
                           <i class="ri-bar-chart-grouped-fill ic-size line-height text-danger"></i>
                        </span>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="4" md="6" >
               <card class=" card-block card-stretch bg-primary card-height sold-back" headerClass="border-none">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">6,548</h4>
                        <p class="mb-0">Sold this month</p>
                  </template>
                    <template v-slot:body>
                     <ApexChart element="crm1-chart-07" :chartOption="chart7" />
                     
                    </template>
               </card>
            </b-col>
            <b-col sm="12" >
               <card class=" card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Reports </h4>
                  </template>
                      <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-primary-light p-2" id="dropdownMenuButton7"
                              data-toggle="dropdown" aria-expanded="false" role="button">
                              All Reports<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                           </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                      </template>
                  <template v-slot:body>
                     <div class="table-responsive">
                        <table class="data-tables table table-borderless" style="width:100%">
                           <thead>
                              <tr>
                                 <th>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck1">
                                       <label class="custom-control-label" for="customCheck1"></label>
                                    </div>
                                 </th>
                                 <th scope="col">Name</th>
                                 <th scope="col">Owner</th>
                                 <th scope="col">Created</th>
                                 <th scope="col">Modified</th>
                                 <th scope="col">Category</th>
                                 <th scope="col">Status</th>
                                 <th scope="col">action</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck2">
                                       <label class="custom-control-label" for="customCheck2"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Hot Deals</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-primary-light rounded-circle mr-2"><i class="las la-crown"></i></div>
                                       <span>Johnson Doe</span>
                                    </div>                                   
                                 </td>
                                 <td>12 Days ago</td>
                                 <td>6 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-primary-light">Deals & Contract</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                          <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck3">
                                       <label class="custom-control-label" for="customCheck3"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Email Activity Report</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-warning-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Karly Latisca</span>
                                    </div>
                                 </td>
                                 <td>10 Days ago</td>
                                 <td>7 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-warning-light">Emails</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle1" id="dropdownMenuButton9" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck4">
                                       <label class="custom-control-label" for="customCheck4"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Phone Activity Report</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                    <div class="ic-25 bg-info-light rounded-circle mr-2"><i
                                          class="las la-crown"></i></div>
                                          <span>Parley Janithan</span>
                                    </div>
                                 </td>
                                 <td>13 Days ago</td>
                                 <td>10 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-info-light">Phone calls</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle1" id="dropdownMenuButton10" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck5">
                                       <label class="custom-control-label" for="customCheck5"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Sales by Customer</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                    <div class="ic-25 bg-danger-light rounded-circle mr-2"><i
                                          class="las la-crown"></i></div>
                                          <span>Karly Latisca</span>
                                    </div>
                                 </td>
                                 <td>14 Days ago</td>
                                 <td>8 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-danger-light">Deals & Contract</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                          <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                        <span class="dropdown-toggle1" id="dropdownMenuButton11" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck7">
                                       <label class="custom-control-label" for="customCheck7"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Appointment Activity...</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-dark-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Larry hatson</span>
                                    </div>
                                 </td>
                                 <td>10 Days ago</td>
                                 <td>7 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-dark-light">Appointment</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                        <span class="dropdown-toggle1" id="dropdownMenuButton12" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck8">
                                       <label class="custom-control-label" for="customCheck8"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Task Activity Report</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-success-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Larry hatson</span>
                                    </div>
                                 </td>
                                 <td>13 Days ago</td>
                                 <td>10 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Tasks</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                       <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle1" id="dropdownMenuButton13" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck9">
                                       <label class="custom-control-label" for="customCheck9"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>New customers</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-danger-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>laouser Kary</span>
                                    </div>
                                 </td>
                                 <td>14 Days ago</td>
                                 <td>8 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-danger-light">Accounts</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                         <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle1" id="dropdownMenuButton14" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck10">
                                       <label class="custom-control-label" for="customCheck10"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Phone Activity Report</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-warning-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Janithan</span>
                                    </div>
                                 </td>
                                 <td>13 Days ago</td>
                                 <td>10 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-warning-light">Phone calls</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle1" id="dropdownMenuButton15" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck11">
                                       <label class="custom-control-label" for="customCheck11"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Sales by Customer</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-info-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Karly Latisca</span>
                                    </div>
                                 </td>
                                 <td>14 Days ago</td>
                                 <td>8 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-info-light">Deals & Contract</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle1" id="dropdownMenuButton16" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="custom-control custom-checkbox text-center">
                                       <input type="checkbox" class="custom-control-input" id="customCheck12">
                                       <label class="custom-control-label" for="customCheck12"></label>
                                    </div>
                                 </td>
                                 <td>
                                    <h6>Email Activity Report</h6>
                                 </td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <div class="ic-25 bg-primary-light rounded-circle mr-2"><i
                                             class="las la-crown"></i></div>
                                             <span>Latisca</span>
                                    </div>
                                 </td>
                                 <td>10 Days ago</td>
                                 <td>7 Days ago</td>
                                 <td>
                                    <div class="badge badge-pill bg-primary-light">Emails</div>
                                 </td>
                                 <td>
                                    <div class="badge badge-pill bg-success-light">Shared</div>
                                 </td>
                                 <td>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle1" id="dropdownMenuButton17" data-toggle="dropdown">
                                          <i class="ri-more-2-fill"></i>
                                       </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                  </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
import { core } from '../../../../config/pluginInit'
import ApexChart from '../../../../components/charts/ApexChart'
export default {
   components:{
     ApexChart

    },
    name:'CrmDashboard',
     mounted () {
   core.initDataTable()
   },
    
    data(){
       return{
          chart1:{
          series: [{
      name: 'series1',
      data: [70, 110, 60, 85, 40, 60, 90, 60]
    }],
    colors: ["#4788ff"],
    chart: {
      height: 300,
      type: 'area',
      sparkline: {
        enabled: false,
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep'],
      labels: {
        offsetX: 0,
        offsetY: -5
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },},
    chart2:{
       series: [{
      name: "Desktops",
      data: [5, 30, 6, 20, 5, 18, 10]
    }],
    colors: ['#4788ff'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    },
    chart3:{
 series: [{
      name: "Desktops",
      data: [5, 20, 4, 18, 3, 15, 10]
    }],
    colors: ['#37e6b0'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    },
    chart4:{
        series: [{
      name: "Desktops",
      data: [5, 15, 3, 20, 5, 18, 13]
    }],
    colors: ['#ff4b4b'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }

    },
    chart5:{
series: [{
      name: "Desktops",
      data: [5, 15, 3, 20, 5, 18, 13]
    }],
    colors: ['#fe721c'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    },
    chart6:{
      series: [{
      name: 'series1',
      data: [50, 30, 20, 80, 40, 109, 100]
    }],

    chart: {
      height: 200
    },
    colors: ['#ff4b4b'],
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
        left: -5,
        right: 0
      }
    },

    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },

    },
    tooltip: {

      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    },
    chart7:{
   series: [{
      name: 'series1',
      data: [60, 80, 60, 90, 60, 109, 100]
    }],

    chart: {
      height: 180
    },
    colors: ['#ffffff'],
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"],
      labels: {
        style: {
          colors: ['#fff', '#fff', '#fff', '#fff', '#fff', '#fff']
        }
        
      },
      axisBorder: {
        show: false,
      },
    },
    grid: {
      borderColor: '#e7e7e7',
      show: false,
      padding: {
        left: -5,
        right: 0,
      }
    },

    yaxis: {
      title: {
        text: '',
        color: ['#ffffff']
      },
      labels: {
        offsetX: -50,
        offsetY: 0
      },

    },
    tooltip: {

      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    }
       }
    }
}

</script>