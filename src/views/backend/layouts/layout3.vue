<template>
  <b-container fluid="">
      <b-row >
            <b-col lg="12" xl="8">
                <b-row>
                  <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-warning-light">
                                      <i class="fas fa-user-friends"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">1334</h3>
                                      <p class="mb-0">Users</p>
                                      <span class="text-danger"><i class="las la-long-arrow-alt-down"></i>10%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                  </b-col>
                   <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-info-light">
                                      <i class="fas fa-dumbbell"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">202</h3>
                                      <p class="mb-0">Trainers</p>
                                      <span class="text-success"><i class="las la-long-arrow-alt-up"></i>50%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                   </b-col>
                  <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-success-light">
                                      <i class="fas fa-search-location"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">50</h3>
                                      <p class="mb-0">Inquiry</p>
                                      <span class="text-danger"><i class="las la-long-arrow-alt-down"></i>20%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                  </b-col>
                    <b-col lg="12" >
                        <card class=" card-transparent" bodyClass="p-0">
                             <template v-slot:body>
                                <ApexChart element="fit-progress-chart-01" :chartOption="chart1" />
                             </template>
                        </card>
                    </b-col>

                </b-row>
            </b-col>
            <b-col lg="6" xl="4" >
                <card class=" card-block card-stretch card-height" bodyClass="iq-profile-top pt-0">
                    <template v-slot:cardImage>
                    <img src="../../../assets/images/layouts/layout-3/user-bg.jpg" class="img-fluid rounded" alt="image">
                    </template>
                    <template v-slot:body>
                        <div class=" text-center">
                            <div class="d-inline-block">
                                <img src="../../../assets/images/layouts/layout-3/user-1.jpg"
                                    class="img-fluid d-inline-block avatar-100 mx-auto rounded" alt="image">
                            </div>
                        </div>
                        <b-row class=" align-items-center justify-content-between pt-4">
                            <h3 class="col-7">Jimmy Gorge</h3>
                            <div class="col-5 text-right">
                                <p class="mb-0 badge badge-warning">New York, NY</p>
                            </div>
                            <h5 class="col-6 text-secondary">Sr.Trainer</h5>
                            <div class="col-6">
                                <div class="d-flex doc-social float-right">
                                    <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                    <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                    <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                </div>
                            </div>

                        </b-row>

                        <ul class="list-inline p-0 m-0 mt-4">
                            <li class="d-flex align-items-center justify-content-between mb-3 pb-2 border-bottom">
                                <h6><i class="fas fa-weight text-primary pr-3"></i>Weight</h6>
                                <p class="mb-0">50.2 Kg</p>
                            </li>
                            <li class="d-flex align-items-center justify-content-between mb-3 pb-2 border-bottom">
                                <h6><i class="fas fa-heartbeat text-danger pr-3"></i>Heart Rate</h6>
                                <p class="mb-0">98.2 Bpm</p>
                            </li>
                            <li class="d-flex align-items-center justify-content-between">
                                <h6><i class="fas fa-user text-success pr-3"></i>Age</h6>
                                <p class="mb-0">25 Yrs</p>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Trainers</h4>
                    </template>
                           <template v-slot:headerAction>
                            <span><i class="fas fa-circle text-primary mr-2 font-size-12"></i>Expert Level</span>
                        </template>
                     <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-2.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Julia<span class="text-body pl-2">(personal)</span></h5>
                                        <div class="text-primary"><b>5.8</b></div>
                                    </div>
                                    <p class="mb-0">Fitness</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-3.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Alina<span class="text-body pl-2">(General)</span></h5>
                                        <div class="text-primary"><b>5.6</b></div>
                                    </div>
                                    <p class="mb-0">Aerobics</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-4.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Julia<span class="text-body pl-2">(General)</span></h5>
                                        <div class="text-primary"><b>5.5</b></div>
                                    </div>
                                    <p class="mb-0">Zumba</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                        </ul>
                     </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center inln-date fitness-datepickr">
                     <template v-slot:body>
                         <flat-pickr :config="config" id="inline-date" value="" class="date-input basicFlatpickr d-none" readonly="readonly"/>
                        <div class="text-primary text-center mt-3"><span class="font-size-18 pr-2">1 / 9 / 2020</span>Lorem
                            ipsum dolor sit amet</div>
                     </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4">
                <b-row>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:body>
                                <i class="fas fa-fire-alt text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Calories</h5>
                                <h2>1259</h2>
                             </template>
                        </card>
                    </b-col>
                     <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:body>
                                <i class="fas fa-carrot text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Protiens</h5>
                                <h2>489</h2>
                             </template>
                        </card>
                     </b-col>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                            <template v-slot:body>
                                <i class="fas fa-cookie-bite text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Carbs</h5>
                                <h2>459</h2>
                            </template>
                        </card>
                    </b-col>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height bg-warning">
                             <template v-slot:body>
                                <i class="fas fa-pizza-slice text-white font-size-40"></i>
                                <h5 class="text-capitalize text-white mt-3">Fat</h5>
                                <h2 class="text-white">259</h2>
                             </template>
                        </card>
                    </b-col>

                </b-row>              
            </b-col>
              <b-col lg="6" >
                <card class=" card-block card-stretch card-height " bodyClass="row align-items-center">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">User's Progress</h4>
                     </template>
                        <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg border border-primary text-primary p-2 rounded-normal" id="dropdownMenuButton2"
                                    data-toggle="dropdown" aria-expanded="true">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                        </template>
                    
                    <template v-slot:body>
                        <b-col md="9">
                             <ApexChart element="fit-progress-chart-03" :chartOption="chart2"/>
                        </b-col>
                        <b-col md="3">
                            <ul class="m-0 p-0 list-inline text-center data-indicator">
                                <li class="position-relative">
                                    <h2 class="line-height"><b>84</b></h2>
                                    <span class="status"><i class="ri-checkbox-blank-circle-fill text-primary"></i></span>
                                    <p class="mb-0 mt-2">Your points</p>
                                </li>
                                <li class="mt-3 position-relative">
                                    <h2 class="line-height"><b>64</b></h2>
                                    <span class="status"><i class="ri-checkbox-blank-circle-fill text-danger"></i></span>
                                    <p class="mb-0 mt-2">Average</p>
                                </li>
                            </ul>
                        </b-col>

                    </template>
                </card>
            </b-col>
            <b-col lg="6">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Upcoming  Events</h4>
                     </template>
                    
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="d-flex align-items-center justify-content-between pb-3 border-bottom">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">23</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>Yoga Special Training</h5>
                                    <p class="mb-0">08 : 30 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                            <li class="d-flex align-items-center justify-content-between pb-3 pt-3 border-bottom">
                                <div class="icon iq-icon-box event-icon bg-warning rounded-small font-size-18">
                                    <div class="date">25</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>Zumba Training Sessions</h5>
                                    <p class="mb-0">08 : 45 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                            <li class="d-flex align-items-center justify-content-between pt-3">
                                <div class="icon iq-icon-box event-icon bg-success rounded-small font-size-18">
                                    <div class="date">28</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>personal Training Happy Week</h5>
                                    <p class="mb-0">09 : 00 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Top Performers</h4>
                     </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                        </template>
                    
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-5.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Julia Met</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-6.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Carolina Tensen</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-7.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Anna Mull</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Social Media</h4>
                   </template>
                         <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                         </template>
                    
                    <template v-slot:body>
                         <ApexChart element="fit-progress-chart-02" :chartOption="chart3"/>
                    </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Products</h4>
                     </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                        </template>
                   
                   <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-1.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>protein  Pills</h5>
                                    <p class="mb-0">100 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 12.8</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-2.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>Coffee beans</h5>
                                    <p class="mb-0">92 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 8.6</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-3.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>Protien Bar</h5>
                                    <p class="mb-0">50 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 15.5</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-4.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>CBD Oil</h5>
                                    <p class="mb-0">95 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 110</b></p>
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
import { english } from 'flatpickr/dist/l10n/default'


export default {
  name:"DefaultDashboard",
  components:{
      ApexChart
   
    
  
  },
  mounted () {
   
   core.fullscreen()
  },
  data () {
    return{
      chart1:{
          series: [{
      name: 'Successful deals',
      data: [60, 40, 50, 80, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 55, 28, 60, 30, 80, 30]
    }],
    colors: ["#fe721c", "#876cfe"],
    chart: {
      height: 320,
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
      
      row: {
        colors: ['#f3f3f3', 'transparent'], 
        opacity: 0
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
          minWidth: 15,
          maxWidth: 15,
        }
     },
     legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -33
    }
      },
      chart2:{
          series: [{
      name: 'Revenue',
      data: [76, 85, 101, 98, 87, 105, 91]
    }, {
        name: 'Net Profit',
        data: [44, 55, 57, 56, 61, 58, 63]
      }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#fe721c'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      labels:{
        minHeight: 30,
        maxHeight: 30,
      }
    },
    yaxis: {
      title: {
        
      },
      labels: {
        offsetY: 0,
        minWidth: 15,
        maxWidth: 15,
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
      name: 'Likes',
      data: [8, 44, 55, 10, 40, 34, 5]
    }, {
      name: 'Comments',
      data: [0, 25, 10, 70, 25, 30, 25]
    }, {
      name: 'Share',
      data: [0, 44, 20, 35, 22, 22, 10]
    }, {
      name: 'Save',
      data: [0, 25, 10, 15, 40, 10, 8]
    }],
    colors: ['#4788FF', '#FE721C', '#876CFE', '#37E6B0'],
    chart: {
      type: 'bar',
      height: 280,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    options: {
      legend: {
        markers: {
          radius: 12,
        }
      }
    },
    
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0,
         
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%'
      },
    },
    xaxis: {
      type: 'category',
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      labels: {
          minHeight: 22,
          maxHeight: 40,
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
      position: 'bottom',
      offsetX: 0,
      offsetY: -10

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
      },
      config: {
        dateFormat: 'Y-m-d',
        inline: true,
        locale: english
      },
    }
  }
}
</script>
