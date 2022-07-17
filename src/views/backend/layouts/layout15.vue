<template>
  <b-container>
        <b-row >
            <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <i class="las la-long-arrow-alt-up text-danger a-rotate a-rotate-down"></i>
                            <span>12 Dec - 25 Feb</span>
                        </div>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="fit-icon rounded text-center bg-primary-light svg-primary">
                                <svg width="42" height="48" viewBox="0 0 42 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M40.5 0C39.6715 0 39 0.671625 39 1.5V2.25C37.5388 2.25 5.09981 2.25 3 2.25V1.5C3 0.671625 2.32847 0 1.5 0C0.671531 0 0 0.671625 0 1.5V6C0 6.82838 0.671531 7.5 1.5 7.5C2.32847 7.5 3 6.82838 3 6V5.25H4.5V42.75H3V42C3 41.1716 2.32847 40.5 1.5 40.5C0.671531 40.5 0 41.1716 0 42V46.5C0 47.3284 0.671531 48 1.5 48C2.32847 48 3 47.3284 3 46.5V45.75H39V46.5C39 47.3284 39.6715 48 40.5 48C41.3285 48 42 47.3284 42 46.5V42C42 41.1716 41.3285 40.5 40.5 40.5C39.6715 40.5 39 41.1716 39 42V42.75H37.5V5.25H39V6C39 6.82838 39.6715 7.5 40.5 7.5C41.3285 7.5 42 6.82838 42 6V1.5C42 0.671625 41.3285 0 40.5 0ZM34.5 42.75H7.5V5.25H34.5V42.75Z"
                                        fill="#4788FF" />
                                    <path
                                        d="M20.434 26.1391C20.7968 26.2869 21.2031 26.287 21.566 26.1391C21.9611 25.9781 31.2443 22.1184 31.2443 15.358C31.2443 10.1399 25.2132 7.19018 21 10.2163C16.7772 7.18343 10.7557 10.1491 10.7557 15.358C10.7557 22.1184 20.0389 25.9781 20.434 26.1391ZM17.2053 12C18.2334 12 19.2008 12.4422 19.8593 13.2134C20.4578 13.9141 21.5421 13.9142 22.1407 13.2134C22.7992 12.4422 23.7666 12 24.7947 12C26.6968 12 28.2443 13.5064 28.2443 15.358C28.2443 18.9842 23.4635 21.9628 21.011 23.1071C19.2263 22.2509 13.7557 19.3027 13.7557 15.358C13.7557 13.5064 15.3032 12 17.2053 12Z"
                                        fill="#4788FF" />
                                    <path
                                        d="M29.25 30H12.75C11.9215 30 11.25 30.6716 11.25 31.5C11.25 32.3284 11.9215 33 12.75 33H29.25C30.0785 33 30.75 32.3284 30.75 31.5C30.75 30.6716 30.0785 30 29.25 30Z"
                                        fill="#4788FF" />
                                    <path
                                        d="M29.25 36H12.75C11.9215 36 11.25 36.6716 11.25 37.5C11.25 38.3284 11.9215 39 12.75 39H29.25C30.0785 39 30.75 38.3284 30.75 37.5C30.75 36.6716 30.0785 36 29.25 36Z"
                                        fill="#4788FF" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-primary">40 K</h2>
                                <p class="mb-0">Total Story</p>
                            </div>
                        </div>
            
                     </template>
                     <ApexChart element="chart-1" :chartOption="chart1" />
                </card>
            </b-col>
              <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <i class="las la-long-arrow-alt-up text-success a-rotate"></i>
                            <span>25 Aug - 25 Sep</span>
                        </div>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="fit-icon rounded text-center bg-warning-light svg-warning">
                                <svg width="46" height="46" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M0 2.8125V45.1875H48V2.8125H0ZM45.1875 42.375H2.8125V11.25H45.1875V42.375ZM45.1875 8.4375H2.8125V5.625H45.1875V8.4375Z"
                                        fill="#876CFE" />
                                    <path d="M25.4062 15V38.625H42.375V15H25.4062ZM39.5625 35.8125H28.2188V17.8125H39.5625V35.8125Z"
                                        fill="#876CFE" />
                                    <path d="M22.5938 15H5.625V17.8125H22.5938V15Z" fill="#876CFE" />
                                    <path d="M16.9688 20.625H5.625V23.4375H16.9688V20.625Z" fill="#876CFE" />
                                    <path d="M22.5938 28.125H5.625V30.9375H22.5938V28.125Z" fill="#876CFE" />
                                    <path d="M16.9688 33.75H5.625V36.5625H16.9688V33.75Z" fill="#876CFE" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-warning">42,458</h2>
                                <p class="mb-0">Total Post</p>
                            </div>
                        </div>
                        
                    </template>
                    <ApexChart element="chart-2" :chartOption="chart2" />
                </card>
            </b-col>
              <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <i class="las la-long-arrow-alt-up text-danger a-rotate a-rotate-down"></i>
                            <span>15 oct - 30 nov</span>
                        </div>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="fit-icon rounded text-center bg-success-light svg-success">
                                <svg width="48" height="42" viewBox="0 0 48 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M43.8461 0.230774H4.15387C1.86337 0.230774 0 2.09415 0 4.38455V30.2307C0 32.5211 1.86337 34.3846 4.15387 34.3846H17.7693L22.8923 41.2154C23.1538 41.564 23.5642 41.7692 24 41.7692C24.4358 41.7692 24.8462 41.564 25.1077 41.2154L30.2307 34.3846H43.8461C46.1365 34.3846 48 32.5212 48 30.2307V4.38455C48 2.09415 46.1366 0.230774 43.8461 0.230774ZM45.2308 30.2308C45.2308 30.9943 44.6097 31.6154 43.8462 31.6154H29.5385C29.1026 31.6154 28.6923 31.8206 28.4308 32.1692L24 38.0769L19.5692 32.1692C19.3077 31.8206 18.8974 31.6154 18.4615 31.6154H4.15387C3.39037 31.6154 2.76928 30.9943 2.76928 30.2308V4.38455C2.76919 3.62105 3.39037 2.99996 4.15387 2.99996H43.8462C44.6097 2.99996 45.2308 3.62105 45.2308 4.38455V30.2308Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M28.5737 16.9599C30.0127 15.6904 30.9231 13.8345 30.9231 11.7691C30.9231 7.95173 27.8174 4.84607 24 4.84607C20.1826 4.84607 17.0769 7.95173 17.0769 11.7691C17.0769 13.8345 17.9872 15.6903 19.4263 16.9599C15.856 18.6717 13.3846 22.3216 13.3846 26.5384C13.3846 27.3031 14.0046 27.923 14.7692 27.923H33.2307C33.9954 27.923 34.6153 27.3031 34.6153 26.5384C34.6154 22.3217 32.144 18.6717 28.5737 16.9599ZM24 7.61535C26.2904 7.61535 28.1539 9.47873 28.1539 11.7692C28.1539 14.0597 26.2904 15.923 24 15.923C21.7096 15.923 19.8461 14.0596 19.8461 11.7691C19.8461 9.47863 21.7096 7.61535 24 7.61535ZM16.2761 25.1538C16.932 21.4856 20.146 18.6923 24 18.6923C27.854 18.6923 31.0679 21.4856 31.7239 25.1538H16.2761Z"
                                        fill="#FE721C" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-success">38 K</h2>
                                <p class="mb-0">Follower's</p>
                            </div>
                        </div>
                        
                     </template>
                    <ApexChart element="chart-3" :chartOption="chart3" />
                </card>
            </b-col>
            
             <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <i class="las la-long-arrow-alt-up text-success a-rotate"></i>
                            <span>01 Mar - 25 Apr</span>
                        </div>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="fit-icon rounded text-center bg-danger-light svg-danger">
                                <svg width="42" height="42" viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M6.5709 33.2719C6.85801 33.4687 7.96543 34.0183 8.90059 32.8371L15.2334 23.584L21.9354 30.048C22.2881 30.3844 22.7721 30.5648 23.2643 30.5074C23.7482 30.4582 24.1912 30.2039 24.4783 29.8019L35.5936 13.8633L35.9955 19.1953C36.0939 20.5488 37.3654 20.7703 37.792 20.7375C38.7107 20.6637 39.408 19.8679 39.3342 18.941L38.6287 9.56482C38.5631 8.64607 37.7592 7.94881 36.8322 8.02264L27.4561 8.7281C26.5373 8.79373 25.84 9.59764 25.9139 10.5246C25.9795 11.4433 26.7752 12.1324 27.7104 12.0668L33.0424 11.6648L22.8541 26.2664L16.1357 19.7859C15.783 19.4414 15.2908 19.2691 14.8068 19.3265C14.3146 19.3758 13.8717 19.6383 13.5928 20.0484L6.13613 30.9422C5.61113 31.7051 5.80801 32.7469 6.5709 33.2719V33.2719Z"
                                        fill="#FF4B4B" />
                                    <path
                                        d="M39.4242 37.7508H4.24922V2.57578C4.24922 1.64883 3.50273 0.902344 2.57578 0.902344C1.64883 0.902344 0.902344 1.64883 0.902344 2.57578V39.4242C0.902344 40.3512 1.64883 41.0977 2.57578 41.0977H39.4242C40.3512 41.0977 41.0977 40.3512 41.0977 39.4242C41.0977 38.4973 40.3512 37.7508 39.4242 37.7508Z"
                                        fill="#FF4B4B" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-danger">78%</h2>
                                <p class="mb-0">Growth</p>
                            </div>
                        </div>
                        
                    </template>
                   <ApexChart element="chart-4" :chartOption="chart4" />
                </card>
             </b-col>
        </b-row>
        <b-row>
            <b-col lg="6" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Overview</h4>
                     </template>
                        <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton5"
                                    data-toggle="dropdown" aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                        </template>
                   <template v-slot:body>
                        <ApexChart element="social-chart-01" :chartOption="chart5" />
                   </template>
                </card>
            </b-col>
            <b-col lg="6" >
                <card class=" card-block card-stretch card-height-half bg-primary-light" bodyClass="mini-chart">
                    <template v-slot:body>
                        <b-row class=" align-items-center justify-content-between">
                            <b-col sm="6" >
                                <a href="#">
                                    <img src="../../../assets/images/layouts/layout-15/01.png" class="img-fluid">
                                </a>
                            </b-col>
                            <b-col sm="6" class=" iq-cart-text mt-3 mt-sm-0">
                                <h3 class="text-primary line-height">Business Thinking for Designer</h3>
                                <p class="mb-0">Lorem ipsum dolor sit amet, consectetur.</p>
                                <button type="button" class="btn btn-primary mt-3">View More</button>
                            </b-col>
                        </b-row>
                    </template>
                </card>
                <card class=" card-block card-stretch card-height-half bg-warning-light" bodyClass="mini-chart">
                   <template v-slot:body>
                        <b-row class=" align-items-center justify-content-between">
                            <b-col sm="6" >
                                <a href="#">
                                    <img src="../../../assets/images/layouts/layout-15/02.png" class="img-fluid">
                                </a>
                            </b-col>
                            <b-col sm="6" class=" iq-cart-text mt-3 mt-sm-0">
                                <h3 class="text-warning line-height">Business Thinking for Designer</h3>
                                <p class="mb-0">Lorem ipsum dolor sit amet, consectetur.</p>
                                <button type="button" class="btn btn-warning mt-3">View More</button>
                            </b-col>
                        </b-row>
                   </template>
                </card>
            </b-col>
        </b-row>
        <b-row >
            <b-col lg="3" md="6">
                <card class=" card-block card-stretch card-height">
                    <div class="card-header d-flex justify-content-between">
                        <div class="header-title">
                            <h4 class="card-title">Post Type</h4>
                        </div>
                    </div>
                    <div class="card-body">
                         <ApexChart element="social-chart-04" :chartOption="chart6" />
                        <hr>
                        <div class="data-block">
                            <ul class="list-inline p-0 m-0">
                                <li class="d-flex align-items-center mb-3">
                                        <div class="ex-box iq-icon-box rounded-small bg-warning-light svg-warning text-center ml-3">
                                            <i class="far fa-images"></i>
                                        </div>
                                        <div class="iq-result-info">
                                            <h5>Images</h5>
                                            <p class="mb-0">25 Aug - 25 Sep</p>
                                        </div>
                                </li>
                                <li class="d-flex align-items-center">
                                        <div class="ex-box iq-icon-box rounded-small bg-success-light svg-success text-center ml-3">
                                            <i class="far fa-play-circle"></i>
                                        </div>
                                        <div class="iq-result-info">
                                            <h5>Videos</h5>
                                            <p class="mb-0">25 Aug - 25 Sep</p>
                                        </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </card>
            </b-col>
            <b-col lg="3" md="6">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Most Popular Post</h4>
                    </template>
                     <template v-slot:body>
                          <Slick  :option="option2" classname="post-social"> 
                       
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-15/post/01.png" class="img-fluid w-100 mb-3" alt="image">
                                <h5>It is a long established fact that a reader</h5>
                                <ul class="like-box p-0 my-2">
                                    <li><a href="#"><i class="las la-heart mr-2"></i>2856</a></li>
                                    <li><a href="#"><i class="fas fa-comment mr-2"></i>500</a></li>
                                    <li><a href="#"><i class="fas fa-bookmark mr-2"></i>100</a></li>
                                </ul>
                                <span class="text-primary">Engagement Rate: 75%</span>
                            </div>
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-15/post/01.png" class="img-fluid w-100 mb-3" alt="image">
                                <h5>It is a long established fact that a reader</h5>
                                <ul class="like-box p-0 my-2">
                                    <li><a href="#"><i class="las la-heart mr-2"></i>2856</a></li>
                                    <li><a href="#"><i class="fas fa-comment mr-2"></i>500</a></li>
                                    <li><a href="#"><i class="fas fa-bookmark mr-2"></i>100</a></li>
                                </ul>
                                <span class="text-primary">Engagement Rate: 75%</span>
                            </div>
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-15/post/01.png" class="img-fluid w-100 mb-3" alt="image">
                                <h5>It is a long established fact that a reader</h5>
                                <ul class="like-box p-0 my-2">
                                    <li><a href="#"><i class="las la-heart mr-2"></i>2856</a></li>
                                    <li><a href="#"><i class="fas fa-comment mr-2"></i>500</a></li>
                                    <li><a href="#"><i class="fas fa-bookmark mr-2"></i>100</a></li>
                                </ul>
                                <span class="text-primary">Engagement Rate: 75%</span>
                            </div>
                        
                          </Slick>
                     </template>
                </card>
            </b-col>
            <b-col lg="6" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Total Engagement</h4>
                    </template>
                         <template v-slot:headerAction>
                         <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton5"
                                    data-toggle="dropdown" aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                        </template>
                   <template v-slot:body>
                         <ApexChart element="social-chart-05" :chartOption="chart7" />
                   </template>
                </card>
            </b-col>
        </b-row>
    
        <b-row >
            <b-col lg="12" >
                <card class=" card-block card-stretch card-height">
                   <template v-slot:body>
                         <VueFullCalendar defaultView="dayGridMonth"
                   :header="header"
                   :plugins="calendarPlugins"
                   :events="calendarEvents"
                   time-zone="UTC"
  />
                   </template>
                </card>
            </b-col>
        </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
import VueFullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import listPlugin from '@fullcalendar/list'
import ApexChart from '../../../components/charts/ApexChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,VueFullCalendar
  },
  mounted () {
      core.fullscreen()
   
  },
    props: {
    // eslint-disable-next-line vue/require-valid-default-prop
    calendarEvents: { type: Array },
    header: { type: Object,
      // eslint-disable-next-line vue/require-valid-default-prop
      default () {
        return {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        }
      }
    }
  },
  data () {
    return{
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
     chart5:{
         series: [{
      name: 'Views',
      data: [85, 60, 95, 60]
    }, {
      name: 'Likes',
      data: [75, 90, 35, 95]
    }],
    chart: {
      type: 'bar'
    },
    colors: ['#4788FF', '#FE721C'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    legend: {
      position: 'bottom',
      offsetX: 0,
      offsetY: -10,
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
      categories: ['Facebook', 'Instagram', 'Twitter', 'Linkedin'],
    },
    yaxis: {
      
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
      breakpoint: 480,
      options: {
        chart: {
          height: 270
        }
      }
    }]
     },
     chart6:{
         series: [40],
    chart: {
      height: 250,
      type: 'radialBar',
    },
    stroke: {
      lineCap: "round",
    },
    colors: ["#FF4B4B"],
    labels: ['Images'],
    responsive: [{
      breakpoint: 1199,
      options: {
        chart: {
          height: 300
        }
      }
    }]
     },
     chart7:{
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
      height: 310,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -30,
          offsetY: 0
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
      calendarPlugins: [
        dayGridPlugin,
        timeGridPlugin,
        interactionPlugin,
        listPlugin
      ],
    }
  }
}
</script>
<style lang='scss'>
  .fc-event, .fc-event:hover{
    color: #ffffff !important;
  }
  @import '~@fullcalendar/core/main.css';
  @import '~@fullcalendar/daygrid/main.css';
  @import '~@fullcalendar/timegrid/main.css';
  @import '~@fullcalendar/list/main.min.css';
</style>