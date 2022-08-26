<template>
  <b-container fluid="">
         <b-row>
            <b-col lg="12">
                <card class=" card-block card-stretch card-height bg-orange-light orange-background-image" :style="`background: url(${require('../../../assets/images/layouts/layout-2/background.jpg')}) no-repeat scroll right center; background-size: contain;`"  bodyClass="property2-content">
                    <template v-slot:body>
                        <div class="d-flex flex-wrap align-items-center">
                            <b-col lg="6" class="p-0">
                                <h3 class="text-uppercase mb-2">Find The Best Properties.</h3>
                                <p>We find the best suited properties for you in any city around the world.<br>
                                    Use our mobile app to get all notifications.</p>
                                <div class="iq-search-bar search-book d-flex align-items-center">
                                    <form action="#" class="searchbox">
                                        <input type="text" class="text search-input" placeholder="search here...">
                                    </form>
                                    <button type="submit" class="btn btn-warning search-data ml-2"><i
                                            class="fas fa-angle-right mr-0 font-size-18"></i></button>
                                </div>
                            </b-col>
                            <b-col lg="6" class=" ml-auto p-0">

                            </b-col>
                        </div>
                    </template>
                </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-info-light">
                    <template v-slot:body>
                        <div class="media align-items-center">
                            <div class="icon iq-icon-box bg-info rounded">
                                <i class="fas fa-laptop-house"></i>
                            </div>
                            <div class="media-body">
                                <h3 class="mb-0 text-info">130</h3>
                                <h5>Properties</h5>
                            </div>
                        </div>
                        <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="90" color="info" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-info">90%</span>
                              </template>
                           </Progressbar>
                        </div>
                    </template>
                </card>
            </b-col>
             <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-warning-light">
                      <template v-slot:body>
                        <div class="media align-items-center">
                            <div class="icon iq-icon-box bg-warning rounded">
                                <i class="fas fa-hand-holding-usd"></i>
                            </div>
                            <div class="media-body">
                                <h3 class="mb-0 text-warning">300 M</h3>
                                <h5>Profit</h5>
                            </div>
                        </div>
                        <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="70" color="warning" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-warning">70%</span>
                              </template>
                           </Progressbar>
                        </div>
                      </template>
                </card>
             </b-col>
             <b-col sm="6" md="6" lg="3">
                <card class="card card-block card-stretch card-height bg-info-light">
                     <template v-slot:body>
                        <div class="media align-items-center">
                            <div class="icon iq-icon-box bg-info rounded">
                                <i class="fab fa-sellsy"></i>
                            </div>
                            <div class="media-body">
                                <h3 class="mb-0 text-info">150</h3>
                                <h5>Seller</h5>
                            </div>
                        </div>
                        <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="85" color="info" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-info">85%</span>
                              </template>
                           </Progressbar>
                        </div>
                     </template>
                </card>
             </b-col>
            <b-col sm="6" md="6" lg="3">
                <card class=" card-block card-stretch card-height bg-warning-light">
                    <template v-slot:body>
                        <div class="media align-items-center">
                            <div class="icon iq-icon-box bg-warning rounded">
                                <i class="fas fa-money-check"></i>
                            </div>
                            <div class="media-body">
                                <h3 class="mb-0 text-warning">600</h3>
                                <h5>Buyers</h5>
                            </div>
                        </div>
                        <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="95" color="warning" class=" bg-white mt-2" midclass="iq-progress progress-1" colorName="white">
                              <template v-slot:text>
                                <span class="progress-text-one bg-warning">95%</span>
                              </template>
                           </Progressbar>
                        </div>
                    </template>
                </card>
            </b-col>
            <b-col xl="6">
                <card class="card card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Income</h4>
                   </template>
                      <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-info p-1 rounded-small" id="dropdownMenuButton1"
                                    data-toggle="dropdown">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                             </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                      </template>
                    
                    <template v-slot:body>
                        <ApexChart element="property2-chart-01" :chartOption="chart1"/>
                   </template>
                </card>
            </b-col>
            <b-col lg="6" xl="3" >
                <card class="card-block card-stretch card-height">
                   <template v-slot:body>
                        <div class="d-flex align-items-center mb-3 social-icon-with-image">
                            <img src="../../../assets/images/layouts/layout-2/user.jpg" class="img-fluid avatar-70 rounded" alt="image">
                            <div class="d-flex doc-social ml-4">
                                <a class="text-info mr-2" href="#"><i class="lab la-facebook-f m-0"></i></a>
                                <a class="text-warning mr-2" href="#"><i class="lab la-twitter m-0"></i></a>
                                <a class="text-success" href="#"><i class="lab la-google-plus m-0"></i></a>
                            </div>
                        </div>
                        <h3 class="">Paul Molive</h3>
                        <p class="font-size-16 mb-3">Agent Of Property</p>
                        <div class="d-flex align-items-center pt-4 border-top">
                            <span class="bg-warning-light rounded-small iq-card-icon-small mr-3">
                                <i class="las la-phone-volume"></i>
                            </span>
                            <h5 class="text-break">+91 01234 56789</h5>
                        </div>
                        <div class="d-flex align-items-center pt-4">
                            <span class="bg-success-light rounded-small iq-card-icon-small mr-3">
                                <i class="las la-envelope"></i>
                            </span>
                            <h5 class="text-break">john@property.com</h5>
                        </div>
                        <div class="d-flex align-items-center pt-4">
                            <span class="bg-primary-light rounded-small iq-card-icon-small mr-3">
                                <i class="lab la-twitter"></i>
                            </span>
                            <h5 class="text-break">social@property.com</h5>
                        </div>
                   </template>
                </card>
            </b-col>
            <b-col lg="6" xl="3" >
                <card>
                   <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between data-block-center">
                           
                            <ApexChart element="property2-chart-02" classname="mr-sm-3" :chartOption="chart2"/>
                            <div class="text-data">
                                <h2>$4,020</h2>
                                <p class="mb-0">Avg Buyers</p>
                            </div>
                        </div>
                   </template>
                </card>
                <card class=" iq-progress-block">
                   <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between data-block-center">
                            <div class="text-left iq-property-circle mr-sm-3">
                                <div class="progress progress-round mx-auto warning selling">
                                    <span class="progress-left">
                                        <span class="progress-bar"></span>
                                    </span>
                                    <span class="progress-right">
                                        <span class="progress-bar"></span>
                                    </span>
                                    <div class="progress-value">46%</div>
                                </div>                                                                                                                                                                                 
                            </div>
                            <div class="text-data">
                                <h2>$8,586</h2>
                                <p class="mb-0">Avg Selling</p>
                            </div>
                        </div>
                   </template>
                </card>
                <card>
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between data-block-center">
                           
                            <ApexChart element="property2-chart-03"  classname="mr-sm-3" :chartOption="chart3"/>
                            <div class="text-data">
                                <h2>$4,256</h2>
                                <p class="mb-0">Avg Per Day</p>
                            </div>
                        </div>
                    </template>
                </card>
            </b-col>
            <b-col lg="12" xl="9">
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Recent Property</h4>
                   </template>
                         <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class="text-primary"><i class="ri-more-2-fill"></i></span>
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
                                                    <img src="../../../assets/images/layouts/layout-2/property-image/06.jpg"
                                                        class="img-fluid rounded-small avatar-50" alt="">
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
                                                    <img src="../../../assets/images/layouts/layout-2/property-image/07.jpg"
                                                        class="img-fluid rounded-small avatar-50" alt="">
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
                                                    <img src="../../../assets/images/layouts/layout-2/property-image/08.jpg"
                                                        class="img-fluid rounded-small avatar-50" alt="">
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
                                                    <img src="../../../assets/images/layouts/layout-2/property-image/10.jpg"
                                                        class="img-fluid rounded-small avatar-50" alt="">
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
            <b-col lg="6" xl="3">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Request Enquiry</h4>
                    </template>
                    
                     <template v-slot:body>
                        <form class="form-box">
                            <div class="col mb-4 p-0">
                                <input type="text" class="form-control" placeholder="Name *">
                            </div>
                            <div class="col mb-4 p-0">
                                <input type="text" class="form-control" placeholder="Email *">
                            </div>
                            <div class="col mb-4 p-0">
                                <input type="text" class="form-control" placeholder="Phone Number *">
                            </div>
                            <div class="col mb-4 p-0">
                                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
                                    placeholder="Message *"></textarea>
                            </div>
                            <div class="float-right">
                                <button type="submit" class="btn btn-outline-primary">Submit</button>
                            </div>
                        </form>
                     </template>
                </card>
            </b-col>
             <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Property Overview</h4>
                    </template>
                    <template v-slot:body>
                        <ul class="d-flex align-items-center list-inline mb-3 p-0">
                            <li class="d-flex align-items-center mr-4">
                                <span class="bg-warning p-1 rounded mr-2"></span>
                                <p class="text-warning mb-0">Sale</p>
                            </li>
                            <li class="d-flex align-items-center mr-4">
                                <span class="bg-primary p-1 rounded mr-2"></span>
                                <p class="text-primary mb-0">Rent</p>
                            </li>
                        </ul>
                        <ul class="list-inline m-0 p-0">
                            <li class="mb-3">
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="avatar-70">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-2/overview-image/01.jpg"
                                                class="img-fluid rounded-small avatar-70" alt="">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5>Luxurious Villa sea facing</h5>
                                        <p class="mb-0">22 sep 2020, 12 Days Left</p>
                                        <div class="badge badge-warning">SALE</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="avatar-70">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-2/overview-image/02.jpg"
                                                class="img-fluid rounded-small avatar-70" alt="">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5>4BHK appartment top floor</h5>
                                        <p class="mb-0">15 sep 2020, 5 Days Left</p>
                                        <div class="badge badge-primary">RENT</div>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="avatar-70">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-2/overview-image/03.jpg"
                                                class="img-fluid rounded-small avatar-70" alt="">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5>Beach Cottage</h5>
                                        <p class="mb-0">25 sep 2020, 15 Days Left</p>
                                        <div class="badge badge-warning">SALE</div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
             </b-col>
             <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height"  bodyClass="text-center">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Property Type</h4>
                    </template>
                    <template v-slot:body>
                        <MorrisChart :element="item.id" :type="item.type" :data="item.bodyData" :colors="item.colors" style="min-height: 300px"/>
                    </template>
                </card>
             </b-col>
            <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Agent</h4>
                    </template>
                    
                   <template v-slot:body>
                        <ul class="list-inline m-0 p-0">
                            <li class="mb-4">
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="user-img">
                                        <img src="../../../assets/images/layouts/layout-2/user2.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex align-items-center">
                                            <h5>Gayri Williams</h5>
                                            <span class="text-body pl-2">(Sales)</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>3.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="user-img">
                                        <img src="../../../assets/images/layouts/layout-2/user3.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex align-items-center">
                                            <h5>Alice Mathew</h5>
                                            <span class="text-body pl-2">(Retail)</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.0 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="user-img">
                                        <img src="../../../assets/images/layouts/layout-2/user4.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex align-items-center">
                                            <h5>Milie Watson</h5>
                                            <span class="text-body pl-2">(Sales)</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center data-center-xs">
                                    <div class="user-img">
                                        <img src="../../../assets/images/layouts/layout-2/user5.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex align-items-center">
                                            <h5>Cliff Hanger</h5>
                                            <span class="text-body pl-2">(Retail)</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>3.5 / 5</div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                   </template>
                </card>
            </b-col>
         </b-row>
  </b-container>
</template>
<script>

import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
import MorrisChart from '../../../components/charts/MorrisChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,
      MorrisChart
   
    
 
  
},
  mounted () {
   
       core.initDataTable(),
       core.fullscreen()
  },
  data () {
    return{
      chart1:{
        series: [
    {
      name: "High Time",
      data: [20, 15, 21, 18, 30, 18, 15, 20, 10, 28, 15, 12]
    },
    {
      name: "Low Time",
      data: [7, 10, 23, 10, 19, 25, 18, 25, 30, 15, 31, 28]
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
  colors: ['#fe721c', '#876cfe'],
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
      text: '',
     
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
       item:{
         type:"donut",
         id:"property2-chart-04",
         colors: ["#876cfe", "#fe721c", "#876cfe", "#fe721c"],
         resize: true,
         hideHover: "auto",
         bodyData: [{
          label: "Commercial",
          value: "38"
          }, {
          label: "Residential",
          value: "29"
          }, {
          label: "Purchased",
          value: "26"
          }, {
          label: "Rent",
          value: "24"
    }
         ],
          
      },
      chart2:{
series: [{
 name: 'Net Profit',
 data: [50, 35, 45, 80, 65, 50]
}, {
 name: 'Revenue',
 data: [76, 85, 101, 98, 50, 80]
}],
  colors: ["#876cfe", "#dcd4ff"],
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
      chart3:{
           series: [{
   name: "Desktops",
   data: [5, 30, 6, 20, 5, 18, 10]
}],
  colors: ['#876cfe'],
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
      }
    }
  }
}
</script>
<style scoped>
.iq-progress-bar .progress-text-one{
    top: -30px !important
}
</style>