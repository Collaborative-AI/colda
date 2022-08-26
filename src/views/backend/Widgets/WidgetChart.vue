<template>
   <b-container fluid="">
            <b-row>
               <b-col md="6" lg="3">
                  <card class="card-block card-stretch card-height overflow-hidden" style="position: relative;" bodyClass="pb-0">
                   <template v-slot:body>
                   <div class="rounded iq-card-icon bg-primary-light"><i class="ri-exchange-dollar-fill"></i>
                        </div> <span class="float-right line-height-6">Net Worth</span>
                        <div class="clearfix"></div>
                        <div class="text-center">
                           <h2 class="mb-0"><span class="counter">65</span><span>M</span></h2>
                           <p class="mb-0 text-secondary line-height"><i class="ri-arrow-up-line text-success mr-1"></i><span class="text-success">10%</span> Increased</p>
                        </div>
                   </template>
                    <ApexChart element="chart-1" :chartOption="chart1" />
                  </card>
               </b-col>
               <b-col md="6" lg="3">
                  <card class="card-block card-stretch card-height overflow-hidden" style="position: relative;" bodyClass="pb-0">
                        <template v-slot:body>
                        <div class="rounded iq-card-icon bg-warning-light"><i class="ri-bar-chart-grouped-line"></i>
                        </div> <span class="float-right line-height-6">Todays Gains</span>
                        <div class="clearfix"></div>
                        <div class="text-center">
                           <h2 class="mb-0"><span>$</span><span class="counter">4500</span></h2>
                           <p class="mb-0 text-secondary line-height"><i class="ri-arrow-up-line text-success mr-1"></i><span class="text-success">20%</span> Increased</p>
                        </div>
                        </template>
                        <ApexChart element="chart-2" :chartOption="chart2" />
                  </card>
               </b-col>
               <b-col md="6" lg="3">
                  <card class="card-block card-stretch card-height overflow-hidden" style="position: relative;" bodyClass="pb-0">
                        <template v-slot:body>
                        <div class="rounded iq-card-icon bg-success-light"><i class="ri-group-line"></i>
                        </div> <span class="float-right line-height-6">Total Users</span>
                        <div class="clearfix"></div>
                        <div class="text-center">
                           <h2 class="mb-0"><span class="counter">96.6</span><span>K</span></h2>
                           <p class="mb-0 text-secondary line-height"><i class="ri-arrow-up-line text-success mr-1"></i><span class="text-success">30%</span> Increased</p>
                        </div>
                        </template>
                        <ApexChart element="chart-3" :chartOption="chart3" />
                  </card>
               </b-col>
               <b-col md="6" lg="3">
                  <card class="card-block card-stretch card-height overflow-hidden" style="position: relative;" bodyClass="pb-0">
                        <template v-slot:body>
                        <div class="rounded iq-card-icon bg-danger-light"><i class="ri-shopping-cart-line"></i>
                        </div> <span class="float-right line-height-6">Orders Received</span>
                        <div class="clearfix"></div>
                        <div class="text-center">
                           <h2 class="mb-0"><span class="counter">15.5</span><span>K</span></h2>
                           <p class="mb-0 text-secondary line-height"><i class="ri-arrow-down-line text-danger mr-1"></i><span class="text-danger">10%</span> Increased</p>
                        </div>
                        </template>
                        <ApexChart element="chart-4" :chartOption="chart4" />
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="iq-box-absolute icon iq-icon-box rounded bg-primary-light"> <i class="ri-focus-2-line"></i>
                           </div>
                           <p class="text-secondary">Total Sales</p>
                        </div>
                        <div class="d-flex align-items-center justify-content-between" style="position: relative;">
                           <h5><b>$18 378</b></h5>
                           <ApexChart element="iq-chart-box1" :chartOption="box1" /> <span class="text-primary"><b> +14% <i class="ri-arrow-up-fill"></i></b></span>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="iq-box-absolute icon iq-icon-box rounded bg-danger-light"> <i class="ri-pantone-line"></i>
                           </div>
                           <p class="text-secondary">Sales Today</p>
                        </div>
                        <div class="d-flex align-items-center justify-content-between" style="position: relative;">
                           <h5><b>$190</b></h5>
                           <ApexChart element="iq-chart-box2" :chartOption="box2" /> <span class="text-danger"><b> -6% <i class="ri-arrow-down-fill"></i></b></span>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="iq-box-absolute icon iq-icon-box rounded bg-success-light"> <i class="ri-database-2-line"></i>
                           </div>
                           <p class="text-secondary">Total Classon</p>
                        </div>
                        <div class="d-flex align-items-center justify-content-between" style="position: relative;">
                           <h5><b>45</b></h5>
                          <ApexChart element="iq-chart-box3" :chartOption="box3" /> <span class="text-success"><b> +0.36% <i class="ri-arrow-up-fill"></i></b></span>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="iq-box-absolute icon iq-icon-box rounded bg-warning-light"> <i class="ri-pie-chart-2-line"></i>
                           </div>
                           <p class="text-secondary">Total Profit</p>
                        </div>
                        <div class="d-flex align-items-center justify-content-between" style="position: relative;">
                           <h5><b>60</b></h5>
                           <ApexChart element="iq-chart-box4" :chartOption="box4" />  <span class="text-warning"><b> +0.45% <i class="ri-arrow-up-fill"></i></b></span>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Invoice Sent</h6>
                           <span class="iq-icon"><i class="ri-information-fill"></i></span>
                        </div>
                        <div class="iq-customer-box d-flex align-items-center justify-content-between mt-3">
                           <div class="d-flex align-items-center">
                              <div class="rounded iq-card-icon bg-primary-light mr-2"> <i class="ri-inbox-fill"></i>
                              </div>
                              <h2>352</h2>
                           </div>
                           <div class="iq-map text-primary font-size-32"><i class="ri-bar-chart-grouped-line"></i>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Credited From Accounts</h6>
                           <span class="iq-icon"><i class="ri-information-fill"></i></span>
                        </div>
                        <div class="iq-customer-box d-flex align-items-center justify-content-between mt-3">
                           <div class="d-flex align-items-center">
                              <div class="rounded iq-card-icon bg-danger-light mr-2"><i class="ri-radar-line"></i>
                              </div>
                              <h2>$37k</h2>
                           </div>
                           <div class="iq-map text-danger font-size-32"><i class="ri-bar-chart-grouped-line"></i>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>AVG Employee Costs</h6>
                           <span class="iq-icon"><i class="ri-information-fill"></i></span>
                        </div>
                        <div class="iq-customer-box d-flex align-items-center justify-content-between mt-3">
                           <div class="d-flex align-items-center">
                              <div class="rounded iq-card-icon bg-warning-light mr-2"><i class="ri-price-tag-3-line"></i>
                              </div>
                              <h2>32%</h2>
                           </div>
                           <div class="iq-map text-warning font-size-32"><i class="ri-bar-chart-grouped-line"></i>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Average payment delay</h6>
                           <span class="iq-icon"><i class="ri-information-fill"></i></span>
                        </div>
                        <div class="iq-customer-box d-flex align-items-center justify-content-between mt-3">
                           <div class="d-flex align-items-center">
                              <div class="rounded iq-card-icon bg-info-light mr-2"><i class="ri-refund-line"></i>
                              </div>
                              <h2>27h</h2>
                           </div>
                           <div class="iq-map text-info font-size-32"><i class="ri-bar-chart-grouped-line"></i>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                      <template v-slot:body>
                        <div class="iq-service d-flex align-items-center justify-content-between" style="position: relative;">
                           <div class="service-data">
                              <h3>24%</h3>
                              <p class="mb-0">Service used</p>
                           </div>
                           <ApexChart element="service-chart-01" :chartOption="service1" />
                        </div>
                      </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                      <template v-slot:body>
                        <div class="iq-service d-flex align-items-center justify-content-between" style="position: relative;">
                           <div class="service-data">
                              <h3>2.5</h3>
                              <p class="mb-0">GB Stored</p>
                           </div>
                           <ApexChart element="service-chart-02" :chartOption="service2" />
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                      <template v-slot:body>
                        <div class="iq-service d-flex align-items-center justify-content-between" style="position: relative;">
                           <div class="service-data">
                              <h3>351</h3>
                              <p class="mb-0">user collect</p>
                           </div>
                           <ApexChart element="service-chart-03" :chartOption="service3" />
                        </div>
                     </template>
                  </card>
               </b-col>
              <b-col sm="6" md="6" lg="3">
                  <card class="card-block card-stretch card-height" bodyClass="iq-box-relative">
                      <template v-slot:body>
                        <div class="iq-service d-flex align-items-center justify-content-between" style="position: relative;">
                           <div class="service-data">
                              <h3>4,852</h3>
                              <p class="mb-0">Visitors</p>
                           </div>
                           <ApexChart element="service-chart-04" :chartOption="service4" />
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col lg="12" class="row m-0 p-0 iq-duration-block">
                  <b-col sm="6" md="2" lg="2">
                     <card class="card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="icon iq-icon-box bg-primary-light rounded"> <i class="ri-drag-move-2-fill"></i>
                           </div>
                           <div class="mt-4">
                              <h2>2.14s</h2>
                              <p>Frontend time</p>
                           </div>
                           <div id=""></div>
                           <ApexChart element="ethernet-chart-01" :chartOption="ethernet1" />
                        </template>
                     </card>
                  </b-col>
                  <b-col sm="6" md="2" lg="2">
                     <card class="card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="icon iq-icon-box bg-success-light rounded" data-wow-delay="0.2s"> <i class="ri-artboard-2-line"></i>
                           </div>
                           <div class="mt-4">
                              <h2>1.05s</h2>
                              <p>Backend time</p>
                           </div>
                           <ApexChart element="ethernet-chart-02" :chartOption="ethernet2" />
                        </template>
                     </card>
                  </b-col>
                  <b-col sm="6" md="2" lg="2">
                     <card class="card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="icon iq-icon-box bg-danger-light rounded" data-wow-delay="0.2s"> <i class="ri-map-pin-time-line"></i>
                           </div>
                           <div class="mt-4">
                              <h2>0.25s</h2>
                              <p>Local time</p>
                           </div>
                           <ApexChart element="ethernet-chart-03" :chartOption="ethernet3" />
                        </template>
                     </card>
                  </b-col>
                  <b-col sm="6" md="2" lg="2">
                     <card class="card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="icon iq-icon-box bg-primary rounded" data-wow-delay="0.2s"> <i class="ri-timer-line"></i>
                           </div>
                           <div class="mt-4">
                              <h2>3.07s</h2>
                              <p>Processing time</p>
                           </div>
                          <ApexChart element="ethernet-chart-04" :chartOption="ethernet4" />
                        </template>
                     </card>
                  </b-col>
                  <b-col md="4" lg="4">
                     <card class="card-block card-stretch card-height">
                        <template v-slot:body>
                           <h4 class="text-uppercase text-black mb-0">Session(Now)</h4>
                           <div class="d-flex justify-content-between align-items-center">
                              <div class="font-size-80 text-black">12</div>
                              <div class="text-left">
                                 <p class="m-0 text-uppercase font-size-12">1 Hours Ago</p>
                                 <div class="mb-1 text-black">1500<span class="text-danger"><i class="ri-arrow-down-s-fill"></i>3.25%</span>
                                 </div>
                                 <p class="m-0 text-uppercase font-size-12">1 Day Ago</p>
                                 <div class="mb-1 text-black">1890<span class="text-success"><i class="ri-arrow-down-s-fill"></i>1.00%</span>
                                 </div>
                                 <p class="m-0 text-uppercase font-size-12">1 Week Ago</p>
                                 <div class="text-black">1260<span class="text-danger"><i class="ri-arrow-down-s-fill"></i>9.87%</span>
                                 </div>
                              </div>
                           </div>
                           
                            <ApexChart element="chart-9" :chartOption="service5" />
                        </template>
                     </card>
                  </b-col>
               </b-col>
            </b-row>
   </b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
import card from '../../../components/cards/card.vue'
import ApexChart from '../../../components/charts/ApexChart'
export default {
  components: { card,ApexChart  },
    name:'widgetChart',
     mounted () {
    core.index()
  },
  
  
  data(){
     return{
        chart1:{
            chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },

    series: [{
        name: 'series1',
        data: [60, 15, 50, 30, 70]
    }, ],
    colors: ['#50b5ff'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
        },
        chart2:{
            chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [70, 40, 60, 30, 60]
    }, ],
    colors: ['#fd7e14'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
        },
        chart3:{
           chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [60, 40, 60, 40, 70]
    }, ],
    colors: ['#49f0d3'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
        },
        chart4:{
            chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [75, 30, 60, 35, 60]
    }, ],
    colors: ['#ff9b8a'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
        },
        box1:{
             series: [{
        name: "Total sales",
        data: [10, 10, 35, 10]
    }],
      colors: ["#50b5ff"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
        },
        box2:{
           series: [{
        name: "Sale Today",
        data: [10, 10, 35, 10]
    }],
      colors: ["#ff9b8a"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
        },
        box3:{
             series: [{
        name: "Total Classon",
        data: [10, 10, 35, 10]
    }],
      colors: ["#49f0d3"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
        },
        box4:{
             series: [{
        name: "Total Profit",
        data: [10, 10, 35, 10]
    }],
      colors: ["#fd7e14"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
        },
        service1:{
            series: [{
      name: 'series1',
      data: [25, 30, 22, 29]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 65,
      width: 140,
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
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
        },
        service2:{
             series: [{
      name: 'series1',
      data: [25, 23, 28, 26]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 65,
      width: 140,
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
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
        },
        service3:{
             series: [{
      name: 'series1',
      data: [25, 23, 28, 23]
    }],
    colors: ["#d592ff"],
      chart: {
      height: 65,
      width: 140,
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
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
        },
        service4:{
           series: [{
      name: 'series1',
      data: [25, 27, 24, 26]
    }],
    colors: ["#1ee2ac"],
      chart: {
      height: 65,
      width: 140,
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
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
        },
        ethernet1:{
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
        ethernet2:{
  series: [{
        name: "Desktops",
        data: [5, 20, 4, 18, 3, 15, 10]
    }],
    colors: ['#1ee2ac'],
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
        ethernet3:{
            series: [{
        name: "Desktops",
        data: [5, 20, 6, 18, 5, 15, 4]
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
        ethernet4:{
           series: [{
        name: "Desktops",
        data: [5, 15, 3, 20, 5, 18, 13]
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
        service5:{
           series: [{
      name: 'series1',
      data: [25, 27, 24, 26]
    }],
    colors: ["#1ee2ac"],
      chart: {
      height: 65,
      width: 140,
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
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
        },
     }
  }
 
}
</script>