<template>
  <b-container >
        <b-row >  
            <b-col lg="6" xl="3" >
                <card>
               <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <ApexChart element="property3-chart-01" :chartOption="chart1" />
                        <div class="pl-3">
                            <h2>$4,020</h2>
                            <p>Avg Buyers</p>
                        </div>
                    </div>
               </template>
                </card>
                <card>
               <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <div class="progress progress-round m-0 primary">
                            <span class="progress-left">
                                <span class="progress-bar"></span>
                            </span>
                            <span class="progress-right">
                                <span class="progress-bar"></span>
                            </span>
                            <div class="progress-value text-primary">46%</div>
                        </div>
                        <div class="pl-3">
                            <h2>$8,548</h2>
                            <p>Avg Selling</p>
                        </div>
                    </div>
               </template>
               </card>
               <card>
                <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <ApexChart element="property3-chart-02" :chartOption="chart2" />
                        <div class="pl-3">
                            <h2>$2,586</h2>
                            <p>Avg Per Day</p>
                        </div>
                    </div>
                </template>
               </card>
            </b-col>                
            <b-col lg="6" xl="3" >
                <card class=" card-block card-stretch card-height">
               <template v-slot:body>
                    <div class="d-flex align-items-center mb-4">
                        <img src="../../../assets/images/user/08.jpg" class="img-fluid avatar-90 rounded" alt="">
                        <div class="d-flex doc-social ml-4">
                            <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                            <a href="#"><i class="lab la-twitter text-primary"></i></a>
                            <a href="#"><i class="lab la-google-plus text-primary"></i></a>
                        </div>
                    </div>
                    <h3>Angie O. Plasty</h3>
                    <p class="font-size-16">Agent Of Property</p>
                    <div class="d-flex align-items-center pt-4 border-top">
                        <span class="bg-primary-light rounded-small iq-card-icon-small mr-3">
                            <i class="las la-phone-volume"></i>
                        </span>
                        <h5>+91 01234 56789</h5>
                    </div>
                    <div class="d-flex align-items-center pt-4">
                        <span class="bg-primary-light rounded-small iq-card-icon-small mr-3">
                            <i class="las la-envelope"></i>
                        </span>
                        <h5>Angie@property.com</h5>
                    </div>
                    <div class="d-flex align-items-center pt-4">
                        <span class="bg-primary-light rounded-small iq-card-icon-small mr-3">
                            <i class="lab la-twitter"></i>
                        </span>
                        <h5>Social@property.com</h5>
                    </div>
               </template>                       
                </card>
            </b-col>
            <b-col lg="12" xl="6" >
                <card class=" card-block card-stretch card-height adv-card text-center" :style="`background: rgba(71,136,255,.1) url(${require('../../../assets/images/layouts/layout-16/property-bg.png')}) no-repeat  top center; background-size: contain;`" bodyClass="p-4">
                    <template v-slot:body>
                        <h3 class="text-primary text-uppercase">Find The Best Properties</h3>
                    </template>
                </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-primary-light">
               <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary rounded">
                            <i class="fas fa-laptop-house"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h3 class="mb-0 text-primary">130</h3>
                            <h5>Property</h5>
                        </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between mt-5 position-relative">
                        <Progressbar :value="55" color="primary" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-primary">55%</span>
                              </template>
                           </Progressbar>
                    </div>
               </template>
                </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-primary-light">
                 <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary rounded">
                            <i class="fas fa-hand-holding-usd"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h3 class="mb-0 text-primary">130</h3>
                            <h5>Profit</h5>
                        </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between mt-5 position-relative">
                        <Progressbar :value="40" color="primary" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-primary">40%</span>
                              </template>
                           </Progressbar>
                    </div>
                 </template>
                </card>
            </b-col>
           <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-primary-light">
                 <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary rounded">
                            <i class="fas fa-cloud-upload-alt"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h3 class="mb-0 text-primary">150</h3>
                            <h5>Seller</h5>
                        </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between mt-5 position-relative">
                         <Progressbar :value="85" color="primary" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-primary">85%</span>
                              </template>
                           </Progressbar>
                    </div>
                 </template>
                </card>
           </b-col>
           <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-primary-light">
                 <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary rounded">
                            <i class="far fa-credit-card"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h3 class="mb-0 text-primary">600</h3>
                            <h5>Buyer's</h5>
                        </div>
                    </div>
                    <div class="d-flex align-items-center justify-content-between mt-5 position-relative">
                         <Progressbar :value="65" color="primary" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-primary">65%</span>
                              </template>
                           </Progressbar>
                    </div>
                 </template>
                </card>
           </b-col>
            <b-col lg="6" xl="3" >
                <card class=" card-block card-stretch card-height" headerClass="align-items-center mb-0">
              <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Request Enquiry</h4>
              </template>
                <template v-slot:body>
                    <form>
                        <div class="col mb-4 p-0">
                            <input type="text" class="form-control" placeholder="Name *">
                        </div>
                        <div class="col mb-4 p-0">
                            <input type="text" class="form-control" placeholder="Email *">
                        </div>
                        <div class="col mb-4 p-0">
                            <textarea class="form-control" id="exampleFormControlTextarea1" rows="2" placeholder="Message *"></textarea>
                        </div>
                        <div class="float-right">
                            <button type="submit" class="btn btn-outline-primary">Submit</button>
                        </div>
                    </form>
                </template>
                </card>
            </b-col>
             <b-col lg="6" xl="3" >
                <card class=" card-block card-stretch card-height"  headerClass="align-items-center mb-0">
               <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Agent</h4>
                  </template>
                <template v-slot:body>
                    <ul class="list-inline m-0 p-0">
                        <li class="mb-4">
                            <div class="d-flex align-items-center">
                            <div class="user-img">
                                <img src="../../../assets/images/layouts/layout-16/user1.png" alt="user-img" class="rounded img-fluid avatar-60">
                            </div>                                   
                            <div class="pl-3">
                                <div class="d-flex align-items-center">
                                    <h5>Gayri Williams</h5>
                                </div>
                                <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                            </div>
                            </div>
                        </li>
                    // eslint-disable-next-line vue/require-valid-default-prop     <li class="mb-4">
                            <div class="d-flex align-items-center">
                            <div class="user-img">
                                <img src="../../../assets/images/layouts/layout-16/user2.png" alt="user-img" class="rounded img-fluid avatar-60">
                            </div>                                   
                            <div class="pl-3">
                                <div class="d-flex align-items-center">
                                    <h5>Alice Mathew</h5>
                                </div>
                                <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                            </div>
                            </div>
                        </li>
                        <li class="mb-4">
                            <div class="d-flex align-items-center">
                            <div class="user-img">
                                <img src="../../../assets/images/layouts/layout-16/user3.png" alt="user-img" class="rounded img-fluid avatar-60">
                            </div>                                   
                            <div class="pl-3">
                                <div class="d-flex align-items-center">
                                    <h5>Milie Watson</h5>
                                </div>
                                <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                            </div>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center">
                            <div class="user-img">
                                <img src="../../../assets/images/layouts/layout-16/user4.png" alt="user-img" class="rounded img-fluid avatar-60">
                            </div>                                   
                            <div class="pl-3">
                                <div class="d-flex align-items-center">
                                    <h5>John Williams</h5>
                                </div>
                                <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                            </div>
                            </div>
                        </li>
                    </ul>
                </template>
                </card>
             </b-col>
            <b-col lg="12" xl="6">
                <card class=" card-block card-stretch card-height">
               <template v-slot:headerTitle>
                        <h4 class="card-title">Income</h4>
               </template>
                    <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-primary rounded p-1" id="dropdownMenuButton1" data-toggle="dropdown">
                            Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                    </template>
                 <template v-slot:body>
                    <ApexChart element="property3-chart-03" :chartOption="chart3" />
                 </template>
                </card>
            </b-col>
            <b-col sm="6" md="6" lg="4">
                <card class=" card-block card-stretch card-height-half">
                 <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary-light rounded">
                            <i class="fas fa-hand-holding-usd"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h6>Payment Received</h6>
                            <p class="mb-0">05 Hours Ago, Lorem Ipsum 15</p>
                            <a href="#">See Details</a>
                        </div>
                    </div>
                 </template>
                </card>
                <card class=" card-block card-stretch card-height-half bg-primary-light">
                <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary rounded">
                            <i class="fas fa-question"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h6>New Inquiry</h6>
                            <p class="mb-0 text-body">08 Hours Ago, Lorem Ipsum 15</p>
                            <a href="#">See Details</a>
                        </div>
                    </div>
                </template>
                </card>
            </b-col>
           <b-col sm="6" md="6" lg="4">
                <card class=" card-block card-stretch card-height-half">
                <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary-light rounded">
                            <i class="fas fa-house-damage"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h6>Item Damaged</h6>
                            <p class="mb-0">07 Hours Ago, Lorem Ipsum 15</p>
                            <a href="#">See Details</a>
                        </div>
                    </div>
                </template>
                </card>
                <card class=" card-block card-stretch card-height-half">
                 <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="icon iq-icon-box bg-primary-light rounded">
                            <i class="fas fa-copy"></i>
                        </div>
                        <div class="media-body ml-3">
                            <h6>Property Documentation</h6>
                            <p class="mb-0">07 Hours Ago, Lorem Ipsum 15</p>
                            <a href="#">See Details</a>
                        </div>
                    </div>
                 </template>
                </card>
            </b-col>
           <b-col sm="6" md="6" lg="4">
                <card class=" card-block card-stretch card-height bg-primary-light" style="background: url(../../../assets/images/layouts/layout-4/welcome-bg.png);background-repeat:no-repeat;
	background-position: center right;background-size: contain;">
                <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="media-body ml-3">
                            <h3>Mega Auction</h3>
                            <h6>20/9/2020</h6>
                            <p class="text-body">Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Edit Pretium, A Nam Proin.</p>
                            <div class="group-member d-flex align-items-center mb-2">
                            <div class="iq-media-group mr-3">
                                <a href="#" class="iq-media">
                                <img class="img-fluid avatar-40 rounded-circle" src="../../../assets/images/user/05.jpg" alt="">
                                </a>
                                <a href="#" class="iq-media">
                                <img class="img-fluid avatar-40 rounded-circle" src="../../../assets/images/user/06.jpg" alt="">
                                </a>
                                <a href="#" class="iq-media">
                                <img class="img-fluid avatar-40 rounded-circle" src="../../../assets/images/user/07.jpg" alt="">
                                </a>
                            </div>
                            <p class="mb-0 text-body">35 Members Joining</p>
                            </div>
                            <button class="btn btn-sm btn-primary">More Details</button>
                        </div>
                    </div>
                </template>
                </card>
           </b-col>
            <b-col lg="8" >
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Recent Property</h4>
                   </template>
                         <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle text-primary" id="dropdownMenuButton2" data-toggle="dropdown">
                                    <i class="ri-more-2-fill"></i>
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
                            <table class="table mb-0 data-table table-borderless tbl-property-info text-body">
                                <thead>
                                    <tr class="text-dark">
                                        <th>
                                            <div class="checkbox d-inline-block mr-3">
                                                <input type="checkbox" class="checkbox-input">
                                            </div>
                                        </th>
                                        <th scope="col">Photo</th>
                                        <th scope="col">Date</th>
                                        <th scope="col">Order Id</th>
                                        <th scope="col">Customer</th>
                                        <th scope="col">Property</th>
                                        <th scope="col">Type</th>
                                        <th scope="col">Status</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            <div class="checkbox d-inline-block mr-3">
                                                <input type="checkbox" class="checkbox-input">
                                            </div>
                                        </td>
                                        <td>
                                            <div class="avatar-70">
                                                <a href="JavaScript:Void(0);">
                                                    <img src="../../../assets/images/layouts/layout-16/property-image/01.png" class="img-fluid rounded-small avatar-50" alt="">
                                                </a>
                                            </div>
                                        </td>
                                        <td>20/08/2020</td>
                                        <td>#12345</td>
                                        <td>Fleece</td>
                                        <td>Eaton Street</td>
                                        <td>
                                            <div class="text-primary"><b>On Rent</b></div>
                                        </td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Delete"
                                                    href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="checkbox d-inline-block mr-3">
                                                <input type="checkbox" class="checkbox-input">
                                            </div>
                                        </td>
                                        <td>
                                            <div class="avatar-70">
                                                <a href="JavaScript:Void(0);">
                                                    <img src="../../../assets/images/layouts/layout-16/property-image/02.png" class="img-fluid rounded-small avatar-50" alt="">
                                                </a>
                                            </div>
                                        </td>
                                        <td>12/07/2020</td>
                                        <td>#76787</td>
                                        <td>Alexender</td>
                                        <td>Lorem Place</td>
                                        <td>
                                            <div class="text-warning"><b>Sold</b></div>
                                        </td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Delete"
                                                    href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="checkbox d-inline-block mr-3">
                                                <input type="checkbox" class="checkbox-input">
                                            </div>
                                        </td>
                                        <td>
                                            <div class="avatar-70">
                                                <a href="JavaScript:Void(0);">
                                                    <img src="../../../assets/images/layouts/layout-16/property-image/03.png" class="img-fluid rounded-small avatar-50" alt="">
                                                </a>
                                            </div>
                                        </td>
                                        <td>30/08/2020</td>
                                        <td>#34544</td>
                                        <td>Jhon</td>
                                        <td>Prince Court</td>
                                        <td>
                                            <div class="text-primary"><b>On Rent</b></div>
                                        </td>
                                        <td>
                                            <div class="badge badge-danger">Pending</div>
                                        </td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Delete"
                                                    href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr class="border-0">
                                        <td>
                                            <div class="checkbox d-inline-block mr-3">
                                                <input type="checkbox" class="checkbox-input">
                                            </div>
                                        </td>
                                        <td>
                                            <div class="avatar-70">
                                                <a href="JavaScript:Void(0);">
                                                    <img src="../../../assets/images/layouts/layout-16/property-image/04.png" class="img-fluid rounded-small avatar-50" alt="">
                                                </a>
                                            </div>
                                        </td>
                                        <td>07/07/2020</td>
                                        <td>#23235</td>
                                        <td>Alice</td>
                                        <td>Abrian Hall</td>
                                        <td>
                                            <div class="text-primary"><b>On Rent</b></div>
                                        </td>
                                        <td>
                                            <div class="badge badge-danger">Pending</div>
                                        </td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Delete"
                                                    href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                     </template>
                </card>
            </b-col>
            <b-col sm="12" md="6" lg="4">
                <card class=" card-block card-stretch">
                  <template v-slot:body>
                    <div class="d-flex align-items-center">
                        <div class="avatar-70">
                            <a href="JavaScript:Void(0);">
                            <img src="../../../assets/images/layouts/layout-16/overview-image/01.png" class="img-fluid rounded-small" alt="">
                            </a>
                        </div>                                    
                        <div class="overview-content pl-3">
                            <h5 class="mb-1">Luxurious Villa Sea Facing</h5>
                            <p class="mb-1">05 sep 2020, 12 Days Left</p>
                            <div class="badge badge-warning">SALE</div>
                        </div>
                    </div>
                  </template>
                </card>
                <card class=" card-block card-stretch">
                  <template v-slot:body>
                    <div class="d-flex align-items-center">
                        <div class="avatar-70">
                            <a href="JavaScript:Void(0);">
                            <img src="../../../assets/images/layouts/layout-16/overview-image/02.png" class="img-fluid rounded-small" alt="">
                            </a>
                        </div>                                    
                        <div class="overview-content pl-3">
                            <h5 class="mb-1">4BHK Appartment Top Floor</h5>
                            <p class="mb-1">07 jul 2020, 12 Days Left</p>
                            <div class="badge badge-primary">RENT</div>
                        </div>
                    </div>
                  </template>
                </card>
                <card class=" card-block card-stretch">
                  <template v-slot:body>
                    <div class="d-flex align-items-center">
                        <div class="avatar-70">
                            <a href="JavaScript:Void(0);">
                            <img src="../../../assets/images/layouts/layout-16/overview-image/03.png" class="img-fluid rounded-small" alt="">
                            </a>
                        </div>                                    
                        <div class="overview-content pl-3">
                            <h5 class="mb-1">Beach Cottage</h5>
                            <p class="mb-1">15 aug 2020, 12 Days Left</p>
                            <div class="badge badge-warning">SALE</div>
                        </div>
                    </div>
                  </template>
                </card>
                <card class=" card-block card-stretch">
                 <template v-slot:body>
                    <div class="d-flex align-items-center">
                        <div class="avatar-70">
                            <a href="JavaScript:Void(0);">
                            <img src="../../../assets/images/layouts/layout-16/overview-image/04.png" class="img-fluid rounded-small" alt="">
                            </a>
                        </div>                                    
                        <div class="overview-content pl-3">
                            <h5 class="mb-1">Grand Home - The Villa</h5>
                            <p class="mb-1">09 oct 2020, 12 Days Left</p>
                            <div class="badge badge-warning">SALE</div>
                        </div>
                    </div>
                 </template>
                </card>
            </b-col>
        </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart
  },
  mounted () {
      core.fullscreen()
   
   core.initDataTable()
  },
  data () {
    return{
      chart1:{
          series: [{
   name: 'Net Profit',
   data: [50, 35, 45, 80, 65, 50]
  }, {
   name: 'Revenue',
   data: [76, 85, 101, 98, 50, 80]
  }],
    colors: ["#4788ff", "#c9dcff"],
   chart: {
   type: 'bar',
   height: 70,
   width: 100,
     sparkline: {
       enabled: true,
     }
  },
  legend: {
   show: false
  },
  plotOptions: {
   bar: {
     horizontal: false,
     columnWidth: '55%',
     endingShape: 'rounded'
   },
  },
  dataLabels: {
   enabled: false
  },
  stroke: {
   show: true,
   width: 2,
   colors: ['transparent']
  },
  xaxis: {
   categories: ['02:30', '02:45', '03:00', '03:15'],
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
   right: 0
  }
  },
  fill: {
   opacity: 1
  },
  tooltip: {
   y: {
     formatter: function (val) {
       return "$ " + val + " thousands"
     }
   }
  }
      },
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
    grid: {
     row: {
       colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
       opacity: 0.5
     },
    },
    xaxis: {
     categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
      },
      chart3:{
          series: [
    {
      name: "High Time",
      data: [20, 15, 21, 18, 30, 18, 15, 20, 10, 28, 15]
    },
    {
      name: "Low Time",
      data: [7, 10, 23, 10, 19, 25, 18, 25, 30, 15, 31]
    }
  ],
    chart: {
    height: 300,
    type: 'line',
    dropShadow: {
      enabled: false,
      color: '#000',
      top: 18,
      left: 7,
      blur: 10,
      opacity: 0.2
    },
    toolbar: {
      show: false
    }
  },
  colors: ['#c9dcff', '#4788ff'],
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: 'straight',
    width: 3
  },
  title: {
    text: '',
    align: 'left'
  },
  grid: {
    borderColor: '#e7e7e7',
    padding: {
    left: -5,
    right: 0,
    bottom: -15
  }
  },
  markers: {
    size: 1
  },
  xaxis: {
    categories: ['02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15'],
    title: {
      text: ''
    },
    labels: {
        minHeight: 22,
        maxHeight: 35
      }
  },
  yaxis: {
    title: {
      text: ''
    },
    labels: {
        offsetX: -17,
        offsetY: 0,
        minWidth: 30,
        maxWidth: 30,
    },
    min: 5,
    max: 40
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  },
  
    responsive: [{
    breakpoint: 678,
    options: {
      xaxis: {
        labels: {
          minHeight: 48,
          maxHeight: 48
        }
      }
    }
  }]
      },
    }
  }
}
</script>
<style scoped>
.iq-progress-bar .progress-text-one{
    top: -30px !important
}
</style>