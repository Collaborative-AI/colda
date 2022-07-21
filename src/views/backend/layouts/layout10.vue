<template>
  <b-container>
         <b-row>
            <b-col lg="8" >
                <b-row>
                    <b-col lg="6" md="12" >
                        <card  class="card-block card-stretch card-height bg-warning rounded">
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <ApexChart element="hotel-chart-4" :chartOption="chart4" />
                                    <div class="pl-3">
                                        <h2 class="text-white">500</h2>
                                        <p class="mb-0">Cancellation</p>
                                    </div>
                                </div>
                            </template>
                        </card >
                    </b-col>
                    <b-col md="6" lg="3">
                        <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <span class="icon-small bg-success rounded mr-2">
                                        <i class="las la-ticket-alt"></i></span>Booking
                                </div>
                                <h2><span class="counter">12</span>K</h2>
                                <Progressbar :value="55" color="success" class="mt-2" />
                           </template>
                        </card >
                   </b-col>
                   <b-col md="6" lg="3">
                         <card>
                             <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <span class="icon-small bg-warning rounded mr-2">
                                        <i class="las la-dollar-sign"></i></span>Earning
                                </div>
                                <h2>$<span class="counter">8500</span></h2>
                                 <Progressbar :value="55" color="warning" class="mt-2" />
                           </template>
                        </card >
                   </b-col>
                    <b-col lg="6" >
                        <card class=" card-block card-stretch card-height bg-primary" bodyClass="pb-0">
                            <template v-slot:body>
                                <h1 class="text-white">600+</h1>
                                <p class="mb-0">Enquires via call and online forms </p>
                            </template>
                            <ApexChart element="hotel-column-1" :chartOption="chart1" />
                        </card>
                    </b-col>
                    <b-col lg="6" >
                        <card class=" card-block card-stretch card-height">
                            <template v-slot:headerTitle>
                                    <h4 class="card-title">Guest By Country's</h4>
                                </template>
                            <template v-slot:body>
                                <AmChart element="hotel-chart-2" type="dashboard-map" :height="150" />
                            </template>
                        </card>
                     </b-col>
               </b-row>
            </b-col>
             <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                      <template v-slot:headerTitle>
                            <h4 class="card-title">Earning Statistics</h4>
                     </template>
                   <template v-slot:body>
                        <div class="text-center">
                            <ApexChart element="hotel-payment-01" :chartOption="chart2" classname="mb-3" />
                            <h5>Your earning this month</h5>
                            <h1 class="text-primary mt-3 mb-2"><b>$ 2.5K</b></h1>
                            <p>Change your payment <br>account from setting </p>
                            <div class="payment-button">
                                <button type="button" class="btn btn-secondary">Withdraw All Earning</button>
                            </div>
                        </div>
                   </template>
                </card>
            </b-col>
            <b-col lg="8" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Income</h4>
                        </template>
                          <template v-slot:headerAction>
                            <div class="dropdown">
                                <span class="dropdown-toggle dropdown-bg border p-1 border-primary text-primary rounded-normal" id="dropdownMenuButton1"
                                    data-toggle="dropdown">
                                    Weekly123<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                                </span>
                                <div class="dropdown-menu dropdown-menu-right shadow-none"
                                    aria-labelledby="dropdownMenuButton1">
                                    <a class="dropdown-item" href="#"><i class="ri-delete-bin-6-fill mr-2"></i>Delete</a>
                                    <a class="dropdown-item" href="#"><i class="ri-pencil-fill mr-2"></i>Edit</a>
                                </div>
                            </div>
                       </template>
                     <template v-slot:body>
                        <ApexChart element="hotel-chart-3" :chartOption="chart3" />
                     </template>
                </card>
            </b-col>
            <b-col lg="4">
                <b-row>
                    <b-col md="6">
                        <card>
                             <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <span class="icon-small bg-primary rounded mr-2">
                                    <i class="las la-user-secret"></i></span>Guest
                                </div>
                                <h2 class="counter">5266</h2>
                                <Progressbar :value="55" color="primary" class="mt-2" />
                            </template>
                        </card>
                    </b-col>
                    <b-col md="6">
                         <card>
                             <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <span class="icon-small bg-danger rounded mr-2">
                                        <i class="las la-user-astronaut"></i></span>Staff
                                </div>
                                <h2 class="counter">450</h2>
                                <Progressbar :value="55" color="danger" class="mt-2" />
                            </template>
                       </card>
                    </b-col>
                </b-row>
                <card class=" card-block card-stretch card-height-half">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <ApexChart element="hotel-chart-5" :chartOption="chart5" />
                            <div class="pl-3">
                                <h2>2,456</h2>
                                <p class="mb-0">Enquiry</p>
                            </div>
                        </div>
                    </template>
                </card>
            </b-col>
            <b-col lg="12" >
                <card>
                       <template v-slot:headerTitle>
                            <h4 class="card-title">Recent Guest</h4>
                        </template>
                         <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                        </template>
                     <template v-slot:body>
                        <div class="table-responsive m-0">
                            <table class="table data-table mb-0 table-borderless tbl-recent-info text-body">
                                <thead>
                                    <tr class="text-dark">
                                        <th scope="col">No</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Member's</th>
                                        <th scope="col">Check In</th>
                                        <th scope="col">Check Out</th>
                                        <th scope="col">Ph No.</th>
                                        <th scope="col">Status</th>
                                        <th scope="col">Room Type</th>
                                        <th scope="col">City</th>
                                        <th scope="col">Action</th>
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
                                        <td>05</td>
                                        <td>01/09/2020</td>
                                        <td>10/09/2020</td>
                                        <td>12345 6789</td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>Double</td>
                                        <td>Canada</td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit" href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Delete" href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
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
                                        <td>02</td>
                                        <td>20/08/2020</td>
                                        <td>25/08/2020</td>
                                        <td>12345 6789</td>
                                        <td>
                                            <div class="badge badge-danger">Pending</div>
                                        </td>
                                        <td>Single</td>
                                        <td>Canada</td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Delete" href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
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
                                        <td>05</td>
                                        <td>05/09/2020</td>
                                        <td>22/09/2020</td>
                                        <td>12345 6789</td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>Single</td>
                                        <td>Canada</td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Edit"
                                                    href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Delete" href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                        
                                    </tr>
                                    <tr>
                                        <td>4</td>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <div class="avatar-40 mr-2">
                                                    <img src="../../../assets/images/user/04.jpg" class="img-fluid rounded" alt="image">
                                                </div>
                                                <div>Madelyn Franci</div>
                                            </div>
                                        </td>
                                        <td>03</td>
                                        <td>01/08/2020</td>
                                        <td>15/08/2020</td>
                                        <td>12345 6789</td>
                                        <td>
                                            <div class="badge badge-danger">Pending</div>
                                        </td>
                                        <td>Duplex</td>
                                        <td>Canada</td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Edit" href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Delete" href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    
                                    </tr>
                                    <tr>
                                        <td>5</td>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <div class="avatar-40 mr-2">
                                                    <img src="../../../assets/images/user/05.jpg" class="img-fluid rounded" alt="image">
                                                </div>
                                                <div>Kadin Franci</div>
                                            </div>
                                        </td>
                                        <td>02</td>
                                        <td>27/07/2020</td>
                                        <td>01/08/2020</td>
                                        <td>12345 6789</td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>Deluxe</td>
                                        <td>Canada</td>
                                        <td>
                                            <div class="d-flex align-items-center list-action">
                                                <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Edit" href="#"><i class="ri-pencil-line"></i></a>
                                                <a class="badge bg-danger-light" data-toggle="tooltip" data-placement="top" title=""
                                                    data-original-title="Delete" href="#"><i class="ri-delete-bin-line"></i></a>
                                            </div>
                                        </td>
                                    
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                   </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Room Categories</h4>
                       </template>
                     <template v-slot:body>
                        <div id="hotel-chart-6"></div>
                        <MorrisChart :element="item.id" :type="item.type" :data="item.bodyData" :colors="item.colors"/>
                    </template>
                </card>
            </b-col>
             <b-col lg="4" >
                <card  class="card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Hotel Amenities</h4>
                       </template>
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-warning-light text-center">
                                        <i class="fas fa-utensils"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Oceans 11 Restaurant</h5>
                                        <p class="mb-0">09:00 to 18:00</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-info-light text-center">
                                        <i class="fas fa-glass-cheers"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Open Bar Overlooking Sea</h5>
                                        <p class="mb-0">05/09/2020</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-danger-light text-center">
                                        <i class="fas fa-tshirt"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Laundry & Valet Service</h5>
                                        <p class="mb-0">25/08/2020</p>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-success-light text-center">
                                        <i class="fas fa-wifi"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Lounge with Free Wi-Fi</h5>
                                        <p class="mb-0">10/08/2020</p>
                                    </div>
                                </div>
                            </li>
                        </ul>
                   </template>
                </card >
            </b-col>
             <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Task To Do</h4>
                        </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                         </template>
                   <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="mb-3">
                                <div class="d-flex align-items-center">
                                    <div class="badge badge-primary iq-number">1</div>
                                    <div class="ml-4">
                                        <h5>Clean The Room</h5>
                                        <p class="mb-0">Room No: 103</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex align-items-center">
                                    <div class="badge badge-danger iq-number">2</div>
                                    <div class="ml-4">
                                        <h5>Clean The Table</h5>
                                        <p class="mb-0">Room No: 207</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex align-items-center">
                                    <div class="badge badge-success iq-number">3</div>
                                    <div class="ml-4">
                                        <h5>Clean The Window</h5>
                                        <p class="mb-0">Room No: 302</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-3">
                                <div class="d-flex align-items-center">
                                    <div class="badge badge-warning iq-number">4</div>
                                    <div class="ml-4">
                                        <h5>Clean The Floor</h5>
                                        <p class="mb-0">Room No: 406</p>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center">
                                    <div class="badge badge-info iq-number">5</div>
                                    <div class="ml-4">
                                        <h5>Change Bed</h5>
                                        <p class="mb-0">Room No: 205</p>
                                    </div>
                                </div>
                            </li>
                        </ul>
                      </template>
                </card >
            </b-col>
        </b-row>
  </b-container>
</template>
<script>
 import { core } from '../../../config/pluginInit'
 import ApexChart from '../../../components/charts/ApexChart'
 import AmChart from '../../../components/charts/AmChart'
 import MorrisChart from '../../../components/charts/MorrisChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,
      AmChart,
      MorrisChart
  },
  mounted () {
    core.index()
    core.initDataTable()
  },
  data () {
    return{
     chart1:{
      series: [{
      name: 'Net Profit',
      data: [30, 35, 40, 56, 61, 65, 70, 50, 40, 30, 25]
    }],
    chart: {
      type: 'bar',
      height: 140,
      sparkline: {
        enabled: true,
      },
    },
    colors: ["#c9dcff"],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '25%',
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
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      style:{
        color: '#000000'
      },
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
     },
     chart2:{
         series: [{
      name: 'Net Profit',
      data: [15, 25, 20, 30, 40]
    }],
    chart: {
      type: 'bar',
      height: 100,
      width:100,
      sparkline: {
        enabled: true,
      }
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
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
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
      name: 'Successful deals',
      data: [90, 70, 80, 60, 70, 90, 90]
    }, {
      name: 'Failed deals',
      data: [70, 85, 58, 90, 60, 100, 60]
    }],
    colors: ["#fe721c", "#4788ff"],
    chart: {
      height: 200,
      type: 'area',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: false,
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
      show: true,
      row: {
        colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      labels: {
        minHeight: 22,
        maxHeight: 35,
      }
    },
    yaxis: {
      labels: {
        offsetY: 0,
        minWidth: 20,
        maxWidth: 20,
      }
    },
    legend: {
      show: false,
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -33
    }
     },
     chart4:{
         series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#ffffff", "#ffecec"],
    chart: {
      type: 'bar',
      height: 90,
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
     chart5:{
         series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#e2fcf4", "#49f0d3"],
    chart: {
      type: 'bar',
      height: 90,
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
      item:{
         type:"donut",
         id:"hotel-chart-6",
         colors: ["#4788ff", "#ff4b4b", "#d592ff", "#fe721c"],
         resize: true,
         hideHover: "auto",
         bodyData: [
            { label: "Single", value: 45 },
            { label: "Double", value: 55 },
            { label: "Deluxe", value: 25 },
            { label: "Duplex", value: 30 }
         ],
          
      }
    }
  }
}
</script>
