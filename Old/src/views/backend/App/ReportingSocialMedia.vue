<template>
     <div class="container-fluid">
         <b-row>
            <b-col lg="8" >
               <b-row >
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height">
                       <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-info icon iq-icon-box-2 mr-2 rounded">
                                 <i class="fab fa-facebook-f"></i>
                              </div>
                              <span class="text-success"><b> <i class="ri-arrow-up-line mr-1"></i> +50.12% </b></span>
                           </div>
                           <div class="mt-4">
                              <h3>96.64k</h3>
                              <p class="mb-0">Facebook</p>
                           </div>
                       </template>
                     </card>
                  </b-col>
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height bg-primary">
                       <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-white icon iq-icon-box-2 mr-2 rounded">
                                 <i class="fab fa-twitter text-primary"></i>
                              </div>
                              <span class="text-white"><b> <i class="ri-arrow-down-line mr-1"></i> -22.72% </b></span>
                           </div>      
                           <div class="mt-4">
                              <h3 class="text-white">35.56K</h3>
                              <p class="mb-0  text-white">Twitter</p>
                           </div>
                       </template>
                     </card>
                  </b-col>
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-success icon iq-icon-box-2 mr-2 rounded">
                                 <i class="lar la-hand-pointer"></i>
                              </div>
                              <span class="text-success"><b> <i class="ri-arrow-up-line mr-1"></i> +42.72% </b></span>
                           </div>      
                           <div class="mt-4">
                              <h3>78.65K</h3>
                              <p class="mb-0">Instagram</p>
                           </div>
                        </template>
                     </card>
                  </b-col>
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height">
                       <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-warning icon iq-icon-box-2 mr-2 rounded">
                                 <i class="fab fa-google-plus-g"></i>
                              </div>
                              <span class="text-danger"><b> <i class="ri-arrow-down-line mr-1"></i> -20.72% </b></span>
                           </div>
      
                           <div class="mt-4">
                              <h3>30.45K</h3>
                              <p class="mb-0">Google Plus</p>
                           </div>
                       </template>
                     </card>
                  </b-col>
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-danger icon iq-icon-box-2 mr-2 rounded">
                                 <i class="fab fa-linkedin-in"></i>
                              </div>
                              <span class="text-success"><b> <i class="ri-arrow-up-line mr-1"></i> +67.72% </b></span>
                           </div>
      
                           <div class="mt-4">
                              <h3>90.64k</h3>
                              <p class="mb-0">Linkedin</p>
                           </div>
                        </template>
                     </card>
                  </b-col>
                  <b-col lg="4" md="6" >
                     <card class=" card-block card-stretch card-height">
                        <template v-slot:body>
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-dark icon iq-icon-box-2 mr-2 rounded">
                                 <i class="fab fa-snapchat-ghost"></i>
                              </div>
                              <span class="text-danger"><b> <i class="ri-arrow-down-line mr-1"></i> -22.72% </b></span>
                           </div>
      
                           <div class="mt-4">
                              <h3>53.16k</h3>
                              <p class="mb-0">Snapchat</p>
                           </div>
                        </template>
                     </card>
                  </b-col>
               </b-row>
            </b-col>
            <b-col lg="4" >
               <card class=" card-block card-stretch card-height" headerClass="border-none" >
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Engagement Rate</h4>
                 </template>
                   <template v-slot:body>
                     <ApexChart element="reporting-chart-15" :chartOption="chart1" />
                   </template>
               </card>               
            </b-col>
            <b-col md="6">
               <card class=" card-block card-stretch card-height" bodyClass="social-report-chart"> 
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Viwed on Devices</h4>
                  </template>
                  <template v-slot:body>
                     <AmChart element="ecommerce-chart-03" type="social" :height="350" />
                  </template>
               </card>
            </b-col>
             <b-col md="6">
               <card class=" card-block card-stretch card-height" headerClass="border-none" >
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Top Keywords (Conversions)</h4>
                  </template>
                  <template v-slot:body>
                     <div class="iq-details">
                        <span class="title">Facebook</span>
                        
                         <Progressbar :value="90" color="primary" colorName="primary" class="   progress-1 mt-2">
                              <template v-slot:text>
                           <span class="progress-text-one  bg-primary">90%</span>
                              </template>
                           </Progressbar>
                     </div>
                     <div class="iq-details mt-4">
                        <span class="title">Twitter</span>
                         <Progressbar :value="60" color="warning" colorName="warning" class="   progress-1 mt-2">
                              <template v-slot:text>
                           <span class="progress-text-one  bg-warning">60%</span>
                              </template>
                           </Progressbar>
                     </div>
                     <div class="iq-details mt-4">
                        <span class="title">Instagram</span>
                         <Progressbar :value="76" color="info" colorName="info" class="   progress-1 mt-2">
                              <template v-slot:text>
                           <span class="progress-text-one  bg-info">76%</span>
                              </template>
                           </Progressbar>
                        
                     </div>
                     <div class="iq-details mt-4">
                        <span class="title">Google Plus</span>
                         <Progressbar :value="85" color="danger" colorName="danger" class="   progress-1 mt-2">
                              <template v-slot:text>
                           <span class="progress-text-one  bg-danger">85%</span>
                              </template>
                           </Progressbar>
                     </div>
                     <div class="iq-details mt-4">
                        <span class="title">Linkedin</span>
                        <Progressbar :value="70" color="success" colorName="success" class="   progress-1 mt-2">
                              <template v-slot:text>
                           <span class="progress-text-one  bg-success">70%</span>
                              </template>
                           </Progressbar>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="4" >               
               <card class=" card-block card-stretch card-height" headerClass=" border-none">
                  <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Browser Traffic</h4>
                  </template>
                  <template v-slot:body>
                     <ul class="perfomer-lists m-0 p-0">
                        <li class="d-flex mb-4 align-items-center">
                           <div class="user-img img-fluid"><img src="../../../assets/images/icon/14.png" alt="story-img"
                                 class="rounded"></div>
                           <div class="media-support-info ml-3">
                              <h6>Opera Mini</h6>
                           </div>
                           <div class="card-header-toolbar d-flex align-items-center">
                              <span><b>67.7%</b></span>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="user-img img-fluid"><img src="../../../assets/images/icon/15.png" alt="story-img"
                                 class="rounded"></div>
                           <div class="media-support-info ml-3">
                              <h6>Google Chrome</h6>
                           </div>
                           <div class="card-header-toolbar d-flex align-items-center">
                              <span><b>43.3%</b></span>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="user-img img-fluid"><img src="../../../assets/images/icon/16.png" alt="story-img"
                                 class="rounded"></div>
                           <div class="media-support-info ml-3">
                              <h6>Firefox</h6>
                           </div>
                           <div class="card-header-toolbar d-flex align-items-center">
                              <span><b>87.2%</b></span>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="user-img img-fluid"><img src="../../../assets/images/icon/17.png" alt="story-img"
                                 class="rounded"></div>
                           <div class="media-support-info ml-3">
                              <h6>Internet Explorer</h6>
                           </div>
                           <div class="card-header-toolbar d-flex align-items-center">
                              <span><b>91.3%</b></span>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="user-img img-fluid"><img src="../../../assets/images/icon/18.png" alt="story-img"
                                 class="rounded"></div>
                           <div class="media-support-info ml-3">
                              <h6>Safari</h6>
                           </div>
                           <div class="card-header-toolbar d-flex align-items-center">
                              <span><b>12.5%</b></span>
                           </div>
                        </li>                        
                     </ul>
                  </template>
               </card>
            </b-col>
            <b-col lg="4" >
               <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">IP Exclusions by Rule (Today)</h4>
                   </template>
                  <template v-slot:body>
                     <ul class="perfomer-lists m-0 p-0">
                        <li class="d-flex mb-4 align-items-center">
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-primary icon iq-icon-box-2 mr-2 rounded">
                                 <i class="las la-globe"></i>
                              </div>
                           </div>
                           <div class="media-support-info ml-3">
                              <h5>Anonymous</h5>
                              <p class="mb-0 font-size-12">Creative Performance</p>
                           </div>
                           <div class="iq-card-header-toolbar d-flex align-items-center">
                              <h3><b>268</b></h3>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-danger icon iq-icon-box-2 mr-2 rounded">
                                 <i class="lar la-hand-pointer"></i>
                              </div>
                           </div>
                           <div class="media-support-info ml-3">
                              <h5>Excessive Clicking</h5>
                              <p class="mb-0 font-size-12">Media Performance</p>
                           </div>
                           <div class="iq-card-header-toolbar d-flex align-items-center">
                              <h3><b>4342</b></h3>
                           </div>
                        </li>
                        <li class="d-flex mb-4 align-items-center">
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-warning icon iq-icon-box-2 mr-2 rounded">
                                 <i class="las la-signal"></i>
                              </div>
                           </div>
                           <div class="media-support-info ml-3">
                              <h5>Premium Impressions</h5>
                              <p class="mb-0 font-size-12">Reach Performance</p>
                           </div>
                           <div class="iq-card-header-toolbar d-flex align-items-center">
                              <h3><b>6565</b></h3>
                           </div>
                        </li>
                        <li class="d-flex align-items-center">
                           <div class="top-block-one d-flex align-items-center justify-content-between">
                              <div class="bg-info icon iq-icon-box-2 mr-2 rounded">
                                 <i class="las la-desktop"></i>
                              </div>
                           </div>
                           <div class="media-support-info ml-3">
                              <h5>Google Ads</h5>
                              <p class="mb-0 font-size-12">Premium Performance</p>
                           </div>
                           <div class="iq-card-header-toolbar d-flex align-items-center">
                              <h3><b>32423</b></h3>
                           </div>
                        </li>
                     </ul>
                  </template>
               </card>
            </b-col>
            <b-col lg="4" >
               <card class=" card-block card-stretch card-height" headerClass="border-none">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Statistic by gender</h4>
                        <p class="mb-0">Mar 17 - Apr 03</p>
                  </template>
                  <template v-slot:body>
                      <ApexChart element="reporting-chart-08" :chartOption="chart2" />
                    
                  </template>
               </card>
            </b-col>
            <b-col xl="8" lg="6" >
               <card class=" card-block card-stretch card-height" headerClass=" border-none">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Target Population for you brand</h4>
                  </template>
                 <template v-slot:body>
                     <div class="table-responsive">
                        <table class="table mb-0 table-borderless">
                           <thead>
                              <tr>
                                 <th scope="col">Target Population</th>
                                 <th scope="col">Visitor</th>
                                 <th scope="col">Reached</th>
                                 <th scope="col">Reached%</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td><span>Men aged between<b> 18-24</b></span></td>
                                 <td>45,332</td>
                                 <td>92,7937</td>
                                 <td>
                                    <div class="btn btn-primary">42.12% <i class="ri-arrow-up-fill"></i></div>
                                 </td>
                              </tr>
                              <tr>
                                 <td><span>Women aged between<b> 25-34</b></span> </td>
                                 <td>13,830</td>
                                 <td>88,799</td>
                                 <td>
                                    <div class="btn btn-danger">12.93% <i class="ri-arrow-down-line"></i></div>
                                 </td>
                              </tr>
                              <tr>
                                 <td><span>Men aged between<b> 35-44</b></span></td>
                                 <td>95,98</td>
                                 <td>32,9937</td>
                                 <td>
                                    <div class="btn btn-danger">02.76% <i class="ri-arrow-down-line"></i></div>
                                 </td>
                              </tr>
                              <tr>
                                 <td><span>Women aged between<b> 44-60</b></span></td>
                                 <td>58,732</td>
                                 <td>412,7935</td>
                                 <td>
                                    <div class="btn btn-primary">82.12% <i class="ri-arrow-up-fill"></i></div>
                                 </td>
                              </tr>
                              <tr>
                                 <td><span>Men aged between<b> 60+</b></span></td>
                                 <td>95,332</td>
                                 <td>452,7978</td>
                                 <td>
                                    <div class="btn btn-primary">92.41% <i class="ri-arrow-up-fill"></i></div>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                 </template>
               </card>
            </b-col>
            <b-col xl="4" lg="6" >
               <card class=" card-block card-stretch card-height" headerClass="border-none">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Overview</h4>
                 </template>            
                 <template v-slot:body>
                     <ApexChart element="reporting-chart-16" :chartOption="chart3" />
                     
                 </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>

import AmChart from '../../../components/charts/AmChart'
import ApexChart from '../../../components/charts/ApexChart'
export default {
    name:'ReportingSocialMedia',
    components:{
      ApexChart,
      AmChart,


    },
   
    data(){
       return{
       chart1:{
           series: [{
      name: 'Likes',
      data: [44, 55, 57, 56, 61, 58, 63]
    }, {
      name: 'Comments',
      data: [76, 85, 101, 98, 87, 105, 91]
    }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#fe721c'],
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
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
    },
    yaxis: {
      labels:{
        minWidth:20,
        maxWidth:20
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
          series: [44, 55],
    chart: {
      width: 310,
      type: 'pie',
    },
    labels: ['Men', 'Women'],
    colors: ["#4788ff", "#fe721c"],
    legend: {
      position: 'bottom'
    }
       },
       chart3:{
           series: [76, 67, 61, 90, 100],
      chart: {
        height: 330,
        type: 'radialBar',
      },
      plotOptions: {
        radialBar: {
          offsetY: 0,
          startAngle: 0,
          endAngle: 270,
          hollow: {
            margin: 5,
            size: '10%',
            background: 'transparent',
            image: undefined,
          },
          dataLabels: {
            name: {
              show: false,
            },
            value: {
              show: false,
            }
          }
        }
      },
      colors: ["#4788ff", "#fe721c", "#37e6b0", "#ff4b4b", "#876cfe"],
      labels: ['Facebook', 'Twitter', 'Instagram', 'Google Plus', 'Linkedin'],
      legend: {
        show: true,
        floating: true,
        fontSize: '10px',
        position: 'left',
        offsetX: 2,
        offsetY: 0,
        labels: {
          useSeriesColors: true,
        },
        markers: {
          size: 0
        },
        formatter: function (seriesName, opts) {
          return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
        },
        itemMargin: {
          vertical: 3
        }
      },
      responsive: [{
        breakpoint: 380,        
        options: {
          chart: {
            height: 280
          },
          legend: {
            show: false            
          }
        }
      }]
       },
       }
    }
}
</script>