<template>
  <b-container fluid="">
       <b-row>
            <b-col lg="8">
                <b-row>
                    <b-col lg="12" >
                        <card class=" border-none" bodyClass=" p-0 wrapper-map">
                             <template v-slot:body>
                                <Mapbox
                                  id="mapbox-chart"
                                  class="full-map"
                                  access-token="pk.eyJ1IjoiYW51cmFnLTAyMDgiLCJhIjoiY2tneGtrbjQxMGt2djJ6cjFveTd5czZwMSJ9.OczAfkRnEysA5zDlBy9eGA"
                                  :map-options="{
                                    container: 'mapbox-chart',
                                    style: 'mapbox://styles/mapbox/streets-v11',
                                    center: [-77.04, 38.907],
                                    zoom: 11.15
                                }"
                                  @map-load="loaded"
                                />

                             </template>
                        </card>
                    </b-col>
                   <b-col lg="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:headerTitle>
                                    <h4 class="card-title">Total Properties</h4>
                               </template>
                            <template v-slot:body>
                                 <highChart element="property-chart-06" :option="chart6" />
                             </template>
                        </card>
                    </b-col>
                    <b-col lg="6" >
                        <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="content-left">
                                        <h5 class="mb-1">Buying</h5>
                                        <p class="mb-0">(150 Sales)</p>
                                    </div>
                                    <h5 class="text-primary">$40,256</h5>
                                </div>
                                <ApexChart element="property-chart-07" :chartOption="chart7" />
                              </template>
                       </card>
                         <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="content-left">
                                        <h5 class="mb-1">Selling</h5>
                                        <p class="mb-0">(150 Sales)</p>
                                    </div>
                                    <h5 class="text-danger">$45,256</h5>
                                </div>
                                <ApexChart element="property-chart-08" :chartOption="chart8" />
                             </template>
                        </card>
                         <card>
                          <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="content-left">
                                        <h5 class="mb-1">Rent</h5>
                                        <p class="mb-0">(150 Sales)</p>
                                    </div>
                                    <h5 class="text-success">$32,256</h5>
                                </div>
                                 <ApexChart element="property-chart-09" :chartOption="chart9" />
                           </template>
                        </card>
                    </b-col>
                    <b-col lg="12">
                        <card  class="card-block card-stretch card-height" headerClass="font-size-18">
                            <template v-slot:headerTitle>
                                    <h4 class="card-title">Recent Property</h4>
                               </template>
                                <template v-slot:headerAction>
                                    <span class="mr-2"><a href="#" class="text-body"><i
                                                class="ri-edit-box-line"></i></a></span>
                                    <span><a href="#" class="text-body"><i class="ri-delete-bin-line"></i></a></span>
                               </template>
                           
                            <template v-slot:body>
                                <div class="table-responsive m-0">
                                    <table class="table mb-0 data-table table-borderless tbl-property-info text-body">
                                        <thead>
                                            <tr class="text-dark">
                                                <th scope="col">Date</th>
                                                <th scope="col">Order Id</th>
                                                <th scope="col">Customer</th>
                                                <th scope="col">Photo</th>
                                                <th scope="col">Property</th>
                                                <th scope="col">Type</th>
                                                <th scope="col">Status</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>20/08/2020</td>
                                                <td>#12345</td>
                                                <td>Fleece</td>
                                                <td>
                                                    <div class="avatar-70">
                                                        <a href="JavaScript:Void(0);">
                                                            <img src="../../../assets/images/layouts/layout-8/property-image/01.jpg"
                                                                class="img-fluid rounded-small" alt="image">
                                                        </a>
                                                    </div>
                                                </td>
                                                <td>Eaton Street</td>
                                                <td class="text-primary"><b>On Rent</b></td>
                                                <td>
                                                    <div class="badge badge-success">Paid</div>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>15/08/2020</td>
                                                <td>#56576</td>
                                                <td>Alexender</td>
                                                <td>
                                                    <div class="avatar-70">
                                                        <a href="JavaScript:Void(0);">
                                                            <img src="../../../assets/images/layouts/layout-8/property-image/02.jpg"
                                                                class="img-fluid rounded-small" alt="image">
                                                        </a>
                                                    </div>
                                                </td>
                                                <td>Lorem Place</td>
                                                <td class="text-warning"><b>Sold</b></td>
                                                <td>
                                                    <div class="badge badge-success">Paid</div>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>30/07/2020</td>
                                                <td>#23445</td>
                                                <td>Jhon</td>
                                                <td>
                                                    <div class="avatar-70">
                                                        <a href="JavaScript:Void(0);">
                                                            <img src="../../../assets/images/layouts/layout-8/property-image/03.jpg"
                                                                class="img-fluid rounded-small" alt="image">
                                                        </a>
                                                    </div>
                                                </td>
                                                <td>Prince Court</td>
                                                <td class="text-primary"><b>On Rent</b></td>
                                                <td>
                                                    <div class="badge badge-danger">Pending</div>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>11/06/2020</td>
                                                <td>#89895</td>
                                                <td>Melinda</td>
                                                <td>
                                                    <div class="avatar-70">
                                                        <a href="JavaScript:Void(0);">
                                                            <img src="../../../assets/images/layouts/layout-8/property-image/04.jpg"
                                                                class="img-fluid rounded-small" alt="image">
                                                        </a>
                                                    </div>
                                                </td>
                                                <td>Prine Place</td>
                                                <td class="text-primary"><b>On Rent</b></td>
                                                <td>
                                                    <div class="badge badge-success">Paid</div>
                                                </td>
                                            </tr>
                                            <tr class="border-0">
                                                <td>10/07/2020</td>
                                                <td>#45656</td>
                                                <td>Alice</td>
                                                <td>
                                                    <div class="avatar-70">
                                                        <a href="JavaScript:Void(0);">
                                                            <img src="../../../assets/images/layouts/layout-8/property-image/05.jpg"
                                                                class="img-fluid rounded-small" alt="image">
                                                        </a>
                                                    </div>
                                                </td>
                                                <td>Abrian Hall</td>
                                                <td class="text-primary"><b>On Rent</b></td>
                                                <td>
                                                    <div class="badge badge-danger">Pending</div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                             </template>
                        </card >
                     </b-col>
               </b-row>
            </b-col>
            <b-col lg="4">
                <card class=" border-none" bodyClass="p-0">
                      <template v-slot:body>
                          <Slick  :option="option2">
                        
                            <li>
                                <a href="#">
                                    <div class="blog-image-blog position-relative overflow-hiddne">
                                        <img src="../../../assets/images/layouts/layout-8/slider/b-1.jpg" class="img-fluid w-100 rounded" alt="image">
                                        <span class="badge badge-warning blog-lable text-uppercase">foe rent</span>
                                        <div class="blog-wishlist"><i class="fas fa-heart"></i></div>
                                    </div>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <div class="blog-image-blog position-relative overflow-hiddne">
                                        <img src="../../../assets/images/layouts/layout-8/slider/b-2.jpg" class="img-fluid w-100 rounded" alt="image">
                                        <span class="badge badge-warning blog-lable text-uppercase">foe rent</span>
                                        <div class="blog-wishlist"><i class="fas fa-heart"></i></div>
                                    </div>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <div class="blog-image-blog position-relative overflow-hiddne">
                                        <img src="../../../assets/images/layouts/layout-8/slider/b-3.jpg" class="img-fluid w-100 rounded" alt="image">
                                        <span class="badge badge-warning blog-lable text-uppercase">foe rent</span>
                                        <div class="blog-wishlist"><i class="fas fa-heart"></i></div>
                                    </div>
                                </a>
                            </li>
                        
                          </Slick>
                    </template>
                </card>
                <card>
                    <template v-slot:body>
                        <div class="d-flex flex-wrap align-items-center justify-content-between">
                            <div class="content-left">
                                <h5 class="text-body mb-2">Buyer's</h5>
                                <div class="d-flex align-items-center">
                                    <h3>500</h3>
                                    <div class="pl-3 line-height-3">
                                        <div class="text-primary">Active 100</div>
                                        <div class="text-success">Inactive 400</div>
                                    </div>
                                </div>
                            </div>
                            <ApexChart element="property-chart-03" :chartOption="chart1" />
                        </div>
                    </template>
                </card>
                 <card>
                   <template v-slot:body>
                        <div class="d-flex flex-wrap align-items-center justify-content-between">
                            <div class="content-left">
                                <h5 class="text-body mb-2">Profit</h5>
                                <div class="d-flex align-items-center">
                                    <h3>130 M</h3>
                                </div>
                            </div>
                            <ApexChart element="property-chart-04" :chartOption="chart2" />
                        </div>
                    </template>
                </card>
                <card>
                   <template v-slot:body>
                        <div class="d-flex flex-wrap align-items-center justify-content-between">
                            <div class="content-left">
                                <h5 class="text-body mb-2">Enquiry</h5>
                                <div class="d-flex align-items-center">
                                    <h3>200</h3>
                                    <div class="pl-3 line-height-3">
                                        <div class="text-primary">Solve 100</div>
                                        <div class="text-success">Pending 100</div>
                                    </div>
                                </div>
                            </div>
                            <ApexChart element="property-chart-05" :chartOption="chart3" />
                        </div>
                       </template>
                </card>
              <card headerClass="align-items-center position-relative">
                    <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Income Analysis</h4>
                         </template>
                        <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                               <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton4" data-toggle="dropdown"
                                    aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1 text-white"></i>
                                </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                       </template>
                    <div class="card-body" style="position: relative;">
                         <ApexChart element="property-chart-1" :chartOption="chart4" />
                    </div>
                 </card>
                <card headerClass="align-items-center mb-0" >
                     <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Request Enquiry</h4>
                        </template>
                      <template v-slot:body>
                        <form class="form-border">
                            <b-col class=" mb-3 p-0">
                                <input type="text" class="form-control" placeholder="Name *">
                            </b-col>
                            <b-col class=" mb-3 p-0">
                                <input type="text" class="form-control" placeholder="Email *">
                            </b-col>
                            <b-col class=" mb-3 p-0">
                                <input type="text" class="form-control" placeholder="Phone Number *">
                             </b-col>
                            <b-col class=" mb-3 p-0">
                                <textarea class="form-control" id="exampleFormControlTextarea1" rows="2"
                                    placeholder="Message *"></textarea>
                            </b-col>
                            <div class="float-right mt-2">
                                <button type="submit" class="btn btn-primary">Submit</button>
                            </div>
                        </form>
                    </template>
               </card>
            </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height" headerClass=" align-items-center mb-0">
                   <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Property Overview</h4>
                        </template>
                      <template v-slot:body>
                        <ul class="d-flex align-items-center list-inline mb-3 p-0">
                            <li class="d-flex align-items-center mr-4">
                                <span class="bg-warning p-1 rounded mr-2"></span>
                                <p class="text-warning mb-0">sale</p>
                            </li>
                            <li class="d-flex align-items-center mr-4">
                                <span class="bg-primary p-1 rounded mr-2"></span>
                                <p class="text-primary mb-0">Rent</p>
                            </li>
                        </ul>
                        <ul class="list-inline m-0 p-0">
                            <li class="mb-3">
                                <div class="d-flex align-items-center user-data-block">
                                    <div class="avatar-90">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-8/overview-image/01.jpg"
                                                class="img-fluid rounded-small" alt="image">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5 class="mb-1">Luxurious Villa sea facing</h5>
                                        <p class="mb-1">22 sep 2020, 12 Days Left</p>
                                        <div class="badge badge-warning">SALE</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex align-items-center user-data-block">
                                    <div class="avatar-90">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-8/overview-image/02.jpg"
                                                class="img-fluid rounded-small" alt="image">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5 class="mb-1">4BHK apartment top floor</h5>
                                        <p class="mb-1">15 sep 2020, 5 Days Left</p>
                                        <div class="badge badge-primary">RENT</div>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center user-data-block">
                                    <div class="avatar-90">
                                        <a href="JavaScript:Void(0);">
                                            <img src="../../../assets/images/layouts/layout-8/overview-image/03.jpg"
                                                class="img-fluid rounded-small" alt="image">
                                        </a>
                                    </div>
                                    <div class="overview-content pl-3">
                                        <h5 class="mb-1">Beach Cottage</h5>
                                        <p class="mb-1">25 sep 2020, 15 Days Left</p>
                                        <div class="badge badge-warning">SALE</div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
             <b-col lg="4">
                <card  class="card-block card-stretch card-height bg-primary" bodyClass="text-center">
                      <template v-slot:body>
                        <h1 class="badge badge-danger text-badge-large">IMPORTANT
</h1>
                        <div class="imp-image-block">
                            <img src="../../../assets/images/layouts/layout-8/text-report.png" class="img-fluid mx-auto d-block" alt="image">
                        </div>
                            
                        <h3 class="mt-4 text-white">Tax Report</h3>
                        <p class="mt-3">Prepae Your Yearly Tax <br> Report By Sep 2020</p>
                    </template>
                </card>
             </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height" headerClass="align-items-center mb-0">
                     <template v-slot:headerTitle>
                            <h4 class="card-title mb-0">Agent</h4>
                       </template>
                   <template v-slot:body>
                        <ul class="list-inline m-0 p-0">
                            <li class="mb-4">
                                <div class="d-flex align-items-center">
                                    <div class="user-img">
                                        <img src="../../../assets/images/user/01.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex flex-wrap align-items-center">
                                            <h5>Gayri Williams</h5>
                                            <span class="text-body pl-2">( Sales )</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center">
                                    <div class="user-img">
                                        <img src="../../../assets/images/user/02.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex flex-wrap align-items-center">
                                            <h5>Alice Mathew</h5>
                                            <span class="text-body pl-2">( Retail )</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center">
                                    <div class="user-img">
                                        <img src="../../../assets/images/user/03.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex flex-wrap align-items-center">
                                            <h5>Milie Watson</h5>
                                            <span class="text-body pl-2">( Sales )</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center">
                                    <div class="user-img">
                                        <img src="../../../assets/images/user/04.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex flex-wrap align-items-center">
                                            <h5>John Williams</h5>
                                            <span class="text-body pl-2">( Sales )</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center">
                                    <div class="user-img">
                                        <img src="../../../assets/images/user/05.jpg" alt="user-img"
                                            class="rounded img-fluid avatar-60">
                                    </div>
                                    <div class="pl-3">
                                        <div class="d-flex flex-wrap align-items-center">
                                            <h5>Cliff Hanger</h5>
                                            <span class="text-body pl-2">( Retail )</span>
                                        </div>
                                        <div><i class="fa fa-star text-warning mr-2"></i>4.2 / 5</div>
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
import HighChart from '../../../components/charts/HighChart'
import Mapbox from 'mapbox-gl-vue'
import mapboxgl from 'mapbox-gl'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,
      HighChart,
      Mapbox
  },
  mounted () {
  
    core.initDataTable(),
    core.fullscreen()
  },
  data () {
    return{
      chart1:{
          series: [{
      name: "Active",
      data: [45, 30, 35, 25]
    },
    {
      name: "Inactive",
      data: [25, 10, 15, 5]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
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
      chart2:{
          series: [{
      name: "Active",
      data: [5, 15, 5, 15]
    },
    {
      name: "Inactive",
      data: [15, 5, 15, 5]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
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
          series: [{
      name: "Active",
      data: [25, 35, 30, 45]
    },
    {
      name: "Inactive",
      data: [5, 15, 10, 25]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
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
      chart4:{
          series: [{
      name: 'Net Profit',
      data: [5, 15, 25, 35, 45, 35, 25, 15, 5]
    }, {
      name: 'Revenue',
        data: [10, 20, 30, 40, 50, 40, 30, 20, 10]
    }],
    chart: {
      type: 'bar',
      height: 240
    },
    colors: ['#4788ff', '#37e6b0'],
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
    legend: {
      show: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
      labels:{
        minHeight:20,
        maxHeight:20
      },
    },
    yaxis: {
      labels:{
        minWidth:15,
        maxWidth:15
      },
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
    },
    
    responsive: [{
      breakpoint: 578,
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
      chart6:{
     chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      height: 380,
      type: 'pie'
    },
    title: {
      text: ''
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
      point: {
        valueSuffix: '%'
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: false
        },
        showInLegend: true
      }
    },
    colors: ["#fe721c", "#4788ff", "#37e6b0", "#ff4b4b"],
    series: [{
      name: 'Brands',
      colorByPoint: true,
      data: [{
        name: 'Commerical',
        y: 30,
        sliced: true,
        selected: true
      }, {
        name: 'Residential',
        y: 55
      }, {
        name: 'Purchased',
        y: 20
      }, {
        name: 'Rent',
        y: 15.85
      }]
    }]
      },
      chart7:{
          series: [{
      name: 'series1',
      data: [0, 5, 20, 30, 25, 13, 20, 5, 2]
    }],
    colors: ["#4788ff"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
      },
      chart8:{
          series: [{
      name: 'series1',
      data: [15, 25, 35, 45, 55, 45, 35, 25, 15]
    }],
    colors: ["#fe721c"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
      },
      chart9:{
          series: [{
      name: 'series1',
      data: [25, 20, 25, 15, 8, 10, 25, 10, 22]
    }],
    colors: ["#37e6b0"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
      },
       option2: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              infinite: true
            }
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 767,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      },
      
    }
  },
  methods: {
 loaded (map) {
      map.resize();
      map.loadImage(
          'https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png',
          // Add an image to use as a custom marker
          function (error, image) {
              if (error) throw error;
              map.addImage('custom-marker', image);

              map.addSource('places', {
                  'type': 'geojson',
                  'data': {
                      'type': 'FeatureCollection',
                      'features': [
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Make it Mount Pleasant</strong><p>Make it Mount Pleasant is a handmade and vintage market and afternoon of live entertainment and kids activities. 12:00-6:00 p.m.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.038659, 38.931567]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Mad Men Season Five Finale Watch Party</strong><p>Head to Lounge 201 (201 Massachusetts Avenue NE) Sunday for a Mad Men Season Five Finale Watch Party, complete with 60s costume contest, Mad Men trivia, and retro food and drink. 8:00-11:00 p.m. $10 general admission, $20 admission and two hour open bar.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.003168, 38.894651]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Big Backyard Beach Bash and Wine Fest</strong><p>EatBar (2761 Washington Boulevard Arlington VA) is throwing a Big Backyard Beach Bash and Wine Fest on Saturday, serving up conch fritters, fish tacos and crab sliders, and Red Apron hot dogs. 12:00-3:00 p.m. $25.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.090372, 38.881189]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Ballston Arts & Crafts Market</strong><p>The Ballston Arts & Crafts Market sets up shop next to the Ballston metro this Saturday for the first of five dates this summer. Nearly 35 artists and crafters will be on hand selling their wares. 10:00-4:00 p.m.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.111561, 38.882342]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      "<strong>Seersucker Bike Ride and Social</strong><p>Feeling dandy? Get fancy, grab your bike, and take part in this year's Seersucker Social bike ride from Dandies and Quaintrelles. After the ride enjoy a lawn party at Hillwood with jazz, cocktails, paper hat-making, and more. 11:00-7:00 p.m.</p>"
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.052477, 38.943951]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Capital Pride Parade</strong><p>The annual Capital Pride Parade makes its way through Dupont this Saturday. 4:30 p.m. Free.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.043444, 38.909664]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Muhsinah</strong><p>Jazz-influenced hip hop artist Muhsinah plays the Black Cat (1811 14th Street NW) tonight with Exit Clov and Gods’illa. 9:00 p.m. $12.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.031706, 38.914581]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      "<strong>A Little Night Music</strong><p>The Arlington Players' production of Stephen Sondheim's <em>A Little Night Music</em> comes to the Kogod Cradle at The Mead Center for American Theater (1101 6th Street SW) this weekend and next. 8:00 p.m.</p>"
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.020945, 38.878241]
                              }
                          },
                          {
                              'type': 'Feature',
                              'properties': {
                                  'description':
                                      '<strong>Truckeroo</strong><p>Truckeroo brings dozens of food trucks, live music, and games to half and M Street SE (across from Navy Yard Metro Station) today from 11:00 a.m. to 11:00 p.m.</p>'
                              },
                              'geometry': {
                                  'type': 'Point',
                                  'coordinates': [-77.007481, 38.876516]
                              }
                          }
                      ]
                  }
              });

              // Add a layer showing the places.
              map.addLayer({
                  'id': 'places',
                  'type': 'symbol',
                  'source': 'places',
                  'layout': {
                      'icon-image': 'custom-marker',
                      'icon-allow-overlap': true
                  }
              });
          }
      );

      // Create a popup, but don't add it to the map yet.
      var popup = new mapboxgl.Popup({
          closeButton: false,
          closeOnClick: false
      });

      map.on('mouseenter', 'places', function (e) {
          // Change the cursor style as a UI indicator.
          map.getCanvas().style.cursor = 'pointer';

          var coordinates = e.features[0].geometry.coordinates.slice();
          var description = e.features[0].properties.description;

          // Ensure that if the map is zoomed out such that multiple
          // copies of the feature are visible, the popup appears
          // over the copy being pointed to.
          while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
              coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
          }

          // Populate the popup and set its coordinates
          // based on the feature found.
          popup.setLngLat(coordinates).setHTML(description).addTo(map);
      });

      map.on('mouseleave', 'places', function () {
          map.getCanvas().style.cursor = '';
          popup.remove();
      });
    }
  }
}
</script>
