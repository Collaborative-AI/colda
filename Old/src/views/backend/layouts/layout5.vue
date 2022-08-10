<template>
  <b-container>
        <b-row >
        <b-col lg="4">
            <div class="card-transparent card-block card-stretch card-height">
                <div class="card-body p-0">
                    <a href="#"><img src="../../../assets/images/layouts/layout-5/card.png" class="img-fluid w-100 rounded" alt="image"></a>
                </div>
            </div>
        </b-col>
        <b-col lg="8">
            <card class=" card-block card-stretch card-height bg-primary">
                <div class="card-body p-0 payment-detail" :style="`background:  url(${require('@/assets/images/layouts/layout-5/01.png')}) scroll no-repeat top left; background-size: cover;`">
                    <div class="d-flex flex-wrap align-items-center payment-text pt-3 pt-md-0">
                        <div class="col-lg-6 pl-sm-5 mt-3 mt-lg-0">
                            <h3 class="text-white mb-3">Dreams Come True With</h3>
                            <p class="text-white font-size-16">Lorem Ipsum Dolor sit, Consectetur adipiscing Elit.
                                Aliquam Id Diam Viverra At Viverra.</p>
                        </div>
                        <div class="col-lg-6 ml-auto">
                            <div class="bottom-img float-right">
                                <img src="../../../assets/images/layouts/layout-5/02.png" class="img-fluid" alt="image">
                            </div>
                        </div>
                    </div>
                </div>
            </card>
        </b-col>
        <b-col lg=6 >
            <b-row>
                <b-col lg="4">
                    <card class=" card-block card-stretch card-height">
                          <template v-slot:body>
                            <p class="mb-0">Income</p>
                            <h3>$ 90,789</h3>
                            <ApexChart element="payment-layout-chart-1" :chartOption="chart1" />
                          </template>
                    </card>
                </b-col>
                 <b-col lg="4">
                    <card class=" card-block card-stretch card-height">
                         <template v-slot:body>
                            <p class="mb-0">Outgoing</p>
                            <h3>$ 40,748</h3>
                            <ApexChart element="payment-layout-chart-2" :chartOption="chart2" />
                        </template>
                    </card>
               </b-col>
               <b-col lg="4">
                    <card  class="card-block card-stretch card-height">
                        <template v-slot:body>
                            <p class="mb-0">Saving</p>
                            <h3>$ 50,458</h3>
                            <ApexChart element="payment-layout-chart-3" :chartOption="chart3" />
                        </template>
                    </card >
                </b-col>
                 <b-col lg="12">
                    <card class=" card-block card-stretch card-height">
                         <template v-slot:body>
                           <div class="d-flex align-items-center justify-content-between">
                               <div class="d-flex align-items-center">
                                    <div class="icon iq-icon-box rounded bg-warning text-center">
                                        <i class="fas fa-sync-alt"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Conversion</h5>
                                    </div>
                               </div>
                               <a href="#" class="btn btn-primary btn-sm">Archive</a>
                           </div>
                           <div class="row mt-3 mb-4">
                               <div class="col-md-6">
                                   <div class="d-flex align-items-center justify-content-between border rounded p-3">
                                       <input type="text" class="form-control conversion-text" value="1,000.00">
                                        <select class="form-control value-select">
                                            <option>GBP</option>
                                            <option>USD</option>
                                        </select>
                                   </div>
                               </div>
                               <div class="col-md-6 mt-3 mt-md-0">
                                    <div class="d-flex align-items-center justify-content-between border rounded p-3">
                                        <input type="text" class="form-control conversion-text" value="1,240.61">
                                        <select class="form-control value-select">
                                            <option>USD</option>
                                            <option>GBP</option>
                                        </select>
                                    </div>
                               </div>
                           </div>
                           <div class="block-rate">
                               <h4>Rate= 1.24 <span class="text-secondary">(Apr 27, 14:44 UTC)</span></h4>
                           </div>
                         </template>
                    </card>
                </b-col>
            </b-row>
        </b-col>
        <b-col lg="6">
            <card class=" card-block card-stretch card-height">
                <template v-slot:headerTitle>
                        <h4 class="card-title">Card Balance</h4>
                  </template>
                <template v-slot:body>
                    <div class="card-header-toolbar d-flex align-items-center card-balance">
                        <ul class="nav nav-pills">
                            <li class="nav-item">
                                <a href="#" class="nav-link active rounded-small">Weekly</a>
                            </li>
                            <li class="nav-item">
                                <a href="#" class="nav-link">Monthly</a>
                            </li>
                            <li class="nav-item">
                                <a href="#" class="nav-link">Yearly</a>
                            </li>
                        </ul>
                    </div>
                   
                         <ApexChart element="payment-layout-chart-4" :chartOption="chart4" />
                </template>
            </card>
        </b-col>
        <b-col lg="4">
            <card class=" card-block card-stretch card-height">
               <template v-slot:headerTitle>
                        <h4 class="card-title">Card Info</h4>
               </template>
                    <template v-slot:headerAction>
                        <a href="#" class="btn btn-sm btn-primary view-more">More Details</a>
                    </template>
               <template v-slot:body>
                    <ul class="list-inline p-0 m-0">
                        <li class="d-flex align-items-center justify-content-between pb-3 border-bottom">
                            <h5 class="d-flex align-items-center"><i class="ri-profile-line text-primary mr-3"></i>Status</h5>
                            <p class="mb-0">Active</p>
                        </li>
                        <li class="d-flex align-items-center justify-content-between mt-3 pb-3 border-bottom">
                            <h5 class="d-flex align-items-center"><i class="ri-terminal-window-line text-primary mr-3"></i>Type Of Card</h5>
                            <p class="mb-0">Master Card</p>
                        </li>
                        <li class="d-flex align-items-center justify-content-between mt-3">
                            <h5 class="d-flex align-items-center"><i class="ri-profile-line text-primary mr-3"></i>Currency</h5>
                            <p class="mb-0">USD</p>
                        </li>
                    </ul>
               </template>
            </card>
        </b-col>
         <b-col lg="4">
            <card class=" card-block card-stretch card-height">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Expanses</h4>
                 </template>
                     <template v-slot:headerAction>
                        <a href="#" class="btn btn-sm btn-primary view-more">Weekly</a>
                     </template>
                <template v-slot:body>
                    <ApexChart element="payment-layout-chart-5" :chartOption="chart5" />
                </template>
            </card>
        </b-col>
        <b-col lg="4">
            <card class="card-block card-stretch card-height">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Card Member's</h4>
                 </template>
                   <template v-slot:headerAction>
                        <a href="#" class="btn btn-sm btn-primary view-more">View All</a>
                    </template>
                <template v-slot:body>
                    <ul class="list-inline p-0 m-0">
                        <li class="d-flex align-items-center mb-3">
                            <img src="../../../assets/images/user/04.jpg" class="img-fluid rounded-small avatar-60" alt="image">
                            <div class="ml-3">
                                <h5>Mr. Breody Anderson</h5>
                                <p class="mb-0">breody@gmail.com</p>
                            </div>
                        </li>
                        <li class="d-flex align-items-center">
                            <img src="../../../assets/images/user/05.jpg" class="img-fluid rounded-small avatar-60" alt="image">
                            <div class="ml-3">
                                <h5>Leta Halvorson</h5>
                                <p class="mb-0">leta@gmail.com</p>
                            </div>
                        </li>
                    </ul>
                 </template>
            </card >
        </b-col>
        <b-col lg="12">
            <card>
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Recent Transaction</h4>
                     </template>
                      <template v-slot:headerAction>
                        <a href="#" class="btn btn-sm btn-primary view-more">View More</a>
                     </template>
                 <template v-slot:body>
                    <div class="table-responsive">
                        <table class="table data-table mb-0 table-borderless tbl-recent-info text-body">
                            <thead>
                                <tr class="text-dark">
                                    <th scope="col">No</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Date & Time</th>
                                    <th scope="col">Paid By</th>
                                    <th scope="col">Price</th>
                                    <th scope="col">Details</th>
                                    <th scope="col">Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <div class="avatar-40 mr-2">
                                                <img src="../../../assets/images/user/01.jpg" class="img-fluid rounded"
                                                    alt="image">
                                            </div>
                                            <div>Maggie Potts</div>
                                        </div>
                                    </td>
                                    <td>01/09/2020, 9:30</td>
                                    <td><img src="../../../assets/images/icon/20.png" class="img-fliud" alt="image"></td>
                                    <td>2500 $</td>
                                    <td><img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image"></td>
                                    <td>
                                        <div class="badge badge-danger">Paid</div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <div class="avatar-40 mr-2">
                                                <img src="../../../assets/images/user/02.jpg" class="img-fluid rounded"
                                                    alt="image">
                                            </div>
                                            <div>John Watson</div>
                                        </div>
                                    </td>
                                    <td>08/09/2020, 7:45</td>
                                    <td><img src="../../../assets/images/icon/20.png" class="img-fliud" alt="image"></td>
                                    <td>4805 $</td>
                                    <td><img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image"></td>
                                    <td>
                                        <div class="badge badge-danger">Paid</div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>3</td>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <div class="avatar-40 mr-2">
                                                <img src="../../../assets/images/user/03.jpg" class="img-fluid rounded"
                                                    alt="image">
                                            </div>
                                            <div>Kusti Franti</div>
                                        </div>
                                    </td>
                                    <td>25/08/2020, 8:05</td>
                                    <td><img src="../../../assets/images/icon/21.png" class="img-fliud" alt="image"></td>
                                    <td>3804 $</td>
                                    <td><img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image"></td>
                                    <td>
                                        <div class="badge badge-danger">Paid</div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>4</td>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <div class="avatar-40 mr-2">
                                                <img src="../../../assets/images/user/04.jpg" class="img-fluid rounded"
                                                    alt="image">
                                            </div>
                                            <div>Abigail Franti</div>
                                        </div>
                                    </td>
                                    <td>15/08/2020, 7:20</td>
                                    <td><img src="../../../assets/images/icon/22.png" class="img-fliud" alt="image"></td>
                                    <td>5600 $</td>
                                    <td><img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image"></td>
                                    <td>
                                        <div class="badge badge-danger">Paid</div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
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
   
   core.initDataTable(),
   core.fullscreen()
  },
  data () {
    return{
     chart1:{
         series: [{
      name: "Desktops",
      data: [5, 12, 30, 20, 25, 13, 15, 3, 0]
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
     chart2:{
         series: [{
      name: "Desktops",
      data: [15, 8, 25, 30, 23, 13, 22, 5, 0]
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
     chart3:{
         series: [{
      name: "Desktops",
      data: [0, 10, 20, 30, 40, 30, 20, 10, 0]
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
     chart4:{
         series: [{
      name: 'Successful deals',
      data: [30, 50, 35, 60, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 50, 55, 50, 30, 80, 30]
    }],
    chart: {
      type: 'bar',
      height: 300,
      stacked: true
    },
    colors: ["#4788ff", "#e8f0ff"],

    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '15%',
        endingShape: 'rounded'
      },
    },
    legend: {
      show: false
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
   
    yaxis: {
      title: {
        text: ''
      },
      labels: {
          minWidth: 19,
          maxWidth: 19,
      }
    },
    xaxis: {
      labels: {
        maxHight: 50,
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
    }
     },
     chart5:{
    series: [44, 55, 33],
    chart: {
      height: 150,
      type: "donut"
    },
    dataLabels: {
      enabled: !1
    },
    colors: ["#37e6b0", "#fe721c", "#4788ff"],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          show: !1
        }
      }
    }],
    legend: {
      position: "right",
      offsetY: 0,
      height: 150
    }}
    }
  }
}
</script>
