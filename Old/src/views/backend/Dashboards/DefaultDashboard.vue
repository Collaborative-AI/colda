<template>
  <b-container fluid="">
         <b-row>
            <b-col lg="12" class="mb-3">
               <div class="d-flex align-items-center justify-content-between welcome-content">
                  <div class="navbar-breadcrumb">
                     <h5 class="mb-0">Welcome To Dashboard</h5>
                     <nav aria-label="breadcrumb">
                        <ul class="breadcrumb m-0">
                           <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                           <li class="breadcrumb-item active" aria-current="page">Dashboard</li>
                        </ul>
                     </nav>
                  </div>
                  <div class="btn-group btn-group-toggle">
                     <router-link to="/" class="button btn btn-success mr-2 button-icon" target="_blank" ><i class="ri-shopping-cart-2-line m-auto m-0"></i></router-link>
                     <router-link to="/" class="button btn btn-warning mr-2 button-icon rounded-small" target="_blank" ><i class="ri-download-2-line m-0"></i></router-link>
                     <router-link to="/" class="button btn btn-info mr-2 button-icon rounded-small" target="_blank" ><i class="ri-add-line m-0"></i></router-link>
                     <router-link to="/" class="button btn btn-primary button-icon" target="_blank" ><i class="ri-drag-move-2-line"></i>Export<i class="ri-arrow-down-s-fill"></i></router-link>
                  </div>
               </div>
            </b-col>
            <b-col sm="6" md="6" lg="3">
               <card  class="card-block card-stretch card-height">
                  <div class="card-body iq-total-content">
                     <div class="top-block d-flex align-items-center justify-content-between">
                        <p class="mb-1">Total Visitor</p>
                        <span class="badge badge-danger rounded-normal">3.563%<i class="ri-arrow-down-s-fill"></i></span>
                     </div>
                     <h4>$<span class="counter">837,8370</span><i class="ri-add-line text-danger"></i></h4>
                     <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                           <Progressbar :value="67" color="danger" colorName="danger" class="iq-progress-bar-icon mt-3">
                              <template v-slot:text>
                           <span class="progress-text text-danger">67%</span>
                              </template>
                           </Progressbar>
                        <div id="total-chart-01" class="ml-4"></div>
                     </div>
                  </div>
               </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <div class="card-body iq-total-content">
                     <div class="top-block d-flex align-items-center justify-content-between">
                        <p class="mb-1">Total Order</p>
                        <span class="badge badge-success rounded-normal">9.563%<i class="ri-arrow-down-s-fill"></i></span>
                     </div>
                     <h4>$<span class="counter">537,8370</span><i class="ri-add-line text-success"></i></h4>
                     <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                        <Progressbar :value="79" color="success" colorName="success" class=" iq-progress-bar-icon mt-3">
                              <template v-slot:text>
                           <span class="progress-text text-success">79%</span>
                              </template>
                           </Progressbar>
                        <div id="total-chart-02" class="ml-4"></div>
                     </div>
                  </div>
               </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <div class="card-body iq-total-content">
                     <div class="top-block d-flex align-items-center justify-content-between">
                        <p class="mb-1">Total Revenue</p>
                        <span class="badge badge-primary rounded-normal">4.523%<i class="ri-arrow-down-s-fill"></i></span>
                     </div>
                     <h4>$<span class="counter">1437,837</span><i class="ri-add-line text-primary"></i></h4>
                     <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="81" color="primary" colorName="primary"  class="iq-progress-bar-icon mt-3">
                              <template v-slot:text>
                           <span class="progress-text text-primary">81%</span>
                              </template>
                           </Progressbar>
                        <div id="total-chart-03" class="ml-4"></div>
                     </div>
                  </div>
               </card>
            </b-col>
            <b-col sm="6" md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <div class="card-body iq-total-content">
                     <div class="top-block d-flex align-items-center justify-content-between">
                        <p class="mb-1">Total Clients</p>
                        <span class="badge badge-warning rounded-normal">2.893%<i class="ri-arrow-down-s-fill"></i></span>
                     </div>
                     <h4>$<span class="counter">829,8470</span><i class="ri-add-line text-warning"></i></h4>
                     <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                            <Progressbar :value="34" color="warning" colorName="warning" class="iq-progress-bar-icon mt-3">
                              <template v-slot:text>
                           <span class="progress-text text-warning">34%</span>
                              </template>
                           </Progressbar>
                        <div id="total-chart-04" class="ml-4"></div>
                     </div>
                  </div>
               </card>
            </b-col>
            <b-col lg="7">
               <card class="card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Site Traffic</h4>
                   </template>     
                     <template v-slot:headerAction>
                        <div class="pl-0">
                       <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton1" data-toggle="dropdown">
                           7.563%<i class="ri-arrow-down-s-fill ml-1"></i>
                           </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                        </div>
                        <div class="pr-0">
                        <b-dropdown  id="dropdownMenuButton2" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle dropdown-bg bg-warning p-2 ml-3 d-none d-sm-inline-block" id="dropdownMenuButton6" data-toggle="dropdown">
                           3.563%<i class="ri-arrow-down-s-fill ml-1"></i>
                           </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                        </div>
                    </template>
                   <template v-slot:body>
                     <div id="site-trafic-chart"></div>
                     <ApexChart element="site-trafic-chart" :chartOption="chart1" />
                   </template>
               </card>
            </b-col>
            <b-col lg="5">
               <card class="card-block card-stretch card-height">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Popular Products</h4>
                  </template>
                  <template v-slot:headerAction>
                     <p class="mb-0">Goal 1500 Unit</p>
                  </template>
                  <template v-slot:body>
                     <div class="iq-details">
                        <span class="title"><b>iPhone XS</b></span>
                        <div class="percentage float-right text-warning">113283 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                          <Progressbar :value="50" color="warning" colorName="warning" class="iq-progress-bar-icon"/>
                        </div>
                     </div>
                     <div class="iq-details mt-3">
                        <span class="title"><b>iPhone 3 XL</b></span>
                        <div class="percentage float-right text-primary">56446 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                          <Progressbar :value="70" color="primary" colorName="primary" class="iq-progress-bar-icon" />
                        </div>
                     </div>
                     <div class="iq-details mt-3">
                        <span class="title"><b>Sony 7iii Mirrorless</b></span>
                        <div class="percentage float-right text-success">553546 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                          <Progressbar :value="40" color="success" colorName="success" class="iq-progress-bar-icon" />
                        </div>
                     </div>
                     <div class="iq-details mt-3">
                        <span class="title"><b>Audio technical A 750</b></span>
                        <div class="percentage float-right text-info">45566 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                           <Progressbar :value="85" color="info" colorName="info" class="iq-progress-bar-icon" />
                        </div>
                     </div>
                     <div class="iq-details mt-3">
                        <span class="title"><b>Xiamomi Pocophone f1</b></span>
                        <div class="percentage float-right text-danger">878663 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                           <Progressbar :value="60" color="danger" colorName="danger" class="iq-progress-bar-icon" />
                        </div>
                     </div>
                     <div class="iq-details mt-3">
                        <span class="title"><b>Redmi note pro</b></span>
                        <div class="percentage float-right text-primary">66746 Sold</div>
                        <div class="iq-progress-bar-linear d-inline-block w-100">
                           <Progressbar :value="45" color="primary" colorName="primary" class="iq-progress-bar-icon" />
                        </div>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="5">
               <card class="card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Sales by category</h4>
                  </template>
                  <template v-slot:body>
                     <MorrisChart :element="item.id" :type="item.type" :data="item.bodyData" :colors="item.colors"/>
                  </template>
               </card>
            </b-col>
            <b-col lg="7">
               <card class="card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Recent Hits (Sales)</h4>
                  </template>
                  <template v-slot:body>
                     <AmChart element="recent-hits-map" type="dashboard-map" :height="350" />
                  </template>
               </card>
            </b-col>
            <b-col lg="12" xl="8">
               <card class="card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Recent Orders</h4>
                   </template>
                     <template v-slot:headerAction>
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
                     </template>
                  <template v-slot:body>
                     <div class="table-responsive">
                        <table class="table mb-0 table-borderless tbl-server-info">
                           <thead>
                              <tr class="text-primary">
                                 <th scope="col">#</th>
                                 <th scope="col">Customer</th>
                                 <th scope="col">Customer ID</th>
                                 <th scope="col">Date</th>
                                 <th scope="col">Price</th>
                                 <th scope="col">Status</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>1</td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <img src="../../../assets/images/user/01.jpg" alt="profile" class="img-fluid rounded avatar-40 text-center">
                                       <div class="pl-3">
                                          <h6>Rodney Artichoke</h6>
                                          <p class="text-body mb-0">United States</p>
                                       </div>
                                    </div>
                                 </td>
                                 <td>#836729267</td>
                                 <td>05-02-2020</td>
                                 <td>$908</td>
                                 <td>
                                    <div class="badge badge-success">Delivered</div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>2</td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <img src="../../../assets/images/user/02.jpg" alt="profile" class="img-fluid rounded avatar-40 text-center">
                                       <div class="pl-3">
                                          <h6>Dominic L. Ement</h6>
                                          <p class="text-body mb-0">India</p>
                                       </div>
                                    </div>
                                 </td>
                                 <td>#948947392</td>
                                 <td>09-02-2020</td>
                                 <td>$564</td>
                                 <td>
                                    <div class="badge badge-warning">Pending</div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>3</td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <img src="../../../assets/images/user/03.jpg" alt="profile" class="img-fluid rounded avatar-40 text-center">
                                       <div class="pl-3">
                                          <h6>Caspian Bellevedere</h6>
                                          <p class="text-body mb-0">Germany</p>
                                       </div>
                                    </div>
                                 </td>
                                 <td>#927351323</td>
                                 <td>16-02-2020</td>
                                 <td>$235</td>
                                 <td>
                                    <div class="badge badge-danger">Declined</div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>4</td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <img src="../../../assets/images/user/04.jpg" alt="profile" class="img-fluid rounded avatar-40 text-center">
                                       <div class="pl-3">
                                          <h6>Max Conversion</h6>
                                          <p class="text-body mb-0">United States</p>
                                       </div>
                                    </div>
                                 </td>
                                 <td>#253427834</td>
                                 <td>27-02-2020</td>
                                 <td>$235</td>
                                 <td>
                                    <div class="badge badge-success">Delivered</div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>5</td>
                                 <td>
                                    <div class="d-flex align-items-center">
                                       <img src="../../../assets/images/user/05.jpg" alt="profile" class="img-fluid rounded avatar-40 text-center">
                                       <div class="pl-3">
                                          <h6>Chaplain Mondover</h6>
                                          <p class="text-body mb-0">Bangladesh</p>
                                       </div>
                                    </div>
                                 </td>
                                 <td>#736292697</td>
                                 <td>19-02-2020</td>
                                 <td>$757</td>
                                 <td>
                                    <div class="badge badge-success">Delivered</div>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="12" xl="4">
               <card class="card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Payment History</h4>
                     </template>
                     <template v-slot:headerAction>
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
                     </template>
                  <template v-slot:body>
                     <ul class="suggestions-lists m-0 p-0">
                        <li class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-primary-light"><i class="ri-currency-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From ATL</h6>
                              <p class="mb-0">5 march, 18:34</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $908.00</h6>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-warning-light"><i class="ri-paypal-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From Paypal</h6>
                              <p class="mb-0">5 march, 18:33</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $736.00</h6>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-success-light"><i class="ri-bank-card-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From Card</h6>
                              <p class="mb-0">5 march, 18:20</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $125.00</h6>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-info-light"><i class="ri-home-6-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From Bank</h6>
                              <p class="mb-0">5 march, 18:23</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $676.00</h6>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-danger-light"><i class="ri-refund-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From Payza</h6>
                              <p class="mb-0">5 march, 18:33</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $232.00</h6>
                           </div>
                        </li>
                        <li class="d-flex align-items-center">
                           <div class="profile-icon bg-primary-light"><i class="ri-money-pound-box-line"></i></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Payment From Skrill</h6>
                              <p class="mb-0">5 march, 18:13</p>
                           </div>
                           <div class="media-support-amount ml-3">
                              <h6>+ $984.00</h6>
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
import AmChart from '../../../components/charts/AmChart'
import ApexChart from '../../../components/charts/ApexChart'
import MorrisChart from '../../../components/charts/MorrisChart'
export default {
  name:"DefaultDashboard",
  components:{
     AmChart,
    ApexChart,
    MorrisChart
  },
  mounted () {
    core.index()
  },
  data () {
    return{
      chart1:{
        series: [{
            name: "series1",
            data: [0, 70, 30, 90, 80, 150]
        }, {
          name: 'series2',
          data: [0, 20, 90, 70, 130, 110]
        }],
        colors: ['#fe721c','#4788ff'],
          chart: {
          height: 310,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Product Trends by Month',
          align: 'left'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0
          },
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
        },
        yaxis: {
          title: {
            text: ''
          },
          labels: {
            offsetX: -20,
            offsetY: 0
          },
        }
      },
      item:{
         type:"donut",
         id:"category-sales-chart",
         colors: ["#0dd6b8", "#ff4b4b", "#1ee2ac"],
         resize: !0,
         hideHover: "auto",
         bodyData: [{
            label: "Sales",
            value: 30
         }, {
            label: "Profit",
            value: 12
         }, {
            label: "Loss",
            value: 20
         }, {
            label: "Stock",
            value: 20
         },
         ],
          
      }
    }
  }
}
</script>
