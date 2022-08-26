<template>
  <b-container fluid="">
       <b-row>
            <b-col lg="12" xl="6" >
                <h3 class="card-title pb-3">Welcome Ariana</h3>
                        <ul class="welcome-block list-inline p-0 mb-0 row align-items-center">
                            <li class="col-md-4 mb-4 mb-md-0">
                                <card class=" bg-primary-light p-3 rounded position-relative overflow-hidden">
                                    <span class="iq-overlay-image-block">
                                        <i class="far fa-id-badge"></i>
                                    </span>
                                    <div class="icon iq-icon-box rounded text-center bg-primary mb-3">
                                        <i class="fas fa-cloud-upload-alt"></i>
                                    </div>
                                    <h4 class="mb-1">Upload <br>Assignment</h4>
                                    <p class="mt-2">30/11/2020<br>4:20 PM</p>
                                    <div class="block-btn mt-3">
                                        <button type="submit" class="btn btn-primary learn-more">Upload</button>
                                    </div>                                    
                                </card>
                            </li>
                            <li class="col-md-4 mb-4 mb-md-0">
                                <card class=" bg-info-light p-3 rounded position-relative overflow-hidden">
                                    <span class="iq-overlay-image-block">
                                        <i class="fas fa-globe"></i>
                                    </span>
                                    <div class="icon iq-icon-box rounded text-center bg-info mb-3">1</div>
                                    <h4 class="mb-1">Physics <br>Assignment</h4>
                                    <p class="mt-2">10/11/2020<br>1:15 PM</p>
                                    <div class="block-btn mt-3">
                                        <button type="submit" class="btn btn-info learn-more">Pending</button>
                                    </div>                                    
                                </card>
                            </li>
                            <li class="col-md-4">
                                <card class=" bg-success-light p-3 rounded position-relative overflow-hidden">
                                    <span class="iq-overlay-image-block">
                                        <i class="far fa-calendar-alt"></i>
                                    </span>
                                    <div class="icon iq-icon-box rounded text-center bg-success mb-3">2</div>
                                    <h4 class="mb-1">Biology <br>Assignment</h4>
                                    <p class="mt-2">15/11/2020<br>5:15 PM</p>
                                    <div class="block-btn mt-3">
                                        <button type="submit" class="btn btn-success learn-more">Finished</button>
                                    </div>                                    
                                </card>
                            </li>
                        </ul>
                   
            </b-col>
             <b-col lg="12" xl="6" >
                <card class="card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Branch</h4>
                    </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                        </template>
                    
                    <template v-slot:body>
                        <b-row>
                            <b-col md="8" >
                                <AmChart element="school-chart-05" type="dashboard-map2" :height="260" />
                            </b-col>
                            <b-col md="4"> 
                                <ul class="list-inline p-0 m-0">
                                    <li class="mb-2">
                                        <h6>Europe</h6>
                                        <div class="iq-progress-bar-linear d-inline-block w-100">
                                           <Progressbar :value="85" color="primary" midclass="iq-progress"/>
                                        </div>
                                    </li>
                                    <li class="mb-2">
                                        <h6>North America</h6>
                                        <div class="iq-progress-bar-linear d-inline-block w-100">
                                            <Progressbar :value="65" color="warning" midclass="iq-progress"/>
                                        </div>
                                    </li>
                                    <li>
                                        <h6>Australia</h6>
                                        <div class="iq-progress-bar-linear d-inline-block w-100">
                                            <Progressbar :value="40" color="success" midclass="iq-progress"/>
                                        </div>
                                    </li>
                                </ul>
                             </b-col>
                        </b-row>
                   </template>
                </card>
            </b-col>
            <b-col lg="6" xl="3">
                <card>
                      <template v-slot:body>
                        <div class="d-flex align-items-center">
                            <div class="fit-icon-2 text-center text-danger">
                                <i class="fas fa-users"></i>
                            </div>
                            <div class="iq-card-text pl-3">
                                <p class="mb-1">Staff</p>
                                <h4 class="text-danger"><b>1859</b></h4>
                                <div>Increaded By 50%</div>
                            </div>
                        </div>
                     </template>
                </card>
                <card>
                      <template v-slot:body>
                        <div class="d-flex align-items-center">
                            <div class="fit-icon-2 text-center text-success">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <div class="iq-card-text pl-3">
                                <p class="mb-1">Progress</p>
                                <h4 class="text-success"><b>50%</b></h4>
                                <div>Increaded By 50%</div>
                            </div>
                        </div>
                    </template>
                </card>
                <card>
                   <template v-slot:body>
                        <div class="d-flex align-items-center">
                            <div class="fit-icon-2 text-center text-warning">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <div class="iq-card-text pl-3">
                                <p class="mb-1">Years</p>
                                <h4 class="text-warning"><b>15 Years</b></h4>
                                <div>Increaded By 80%</div>
                            </div>
                        </div>
                   </template>
                </card>
            </b-col>           
            <b-col lg="6" xl="3">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Top Teacher</h4>
                       </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                         </template>
                    <template v-slot:body>
                        <div class="d-flex align-items-center mb-3">
                            <img src="../../../assets/images/user/user-1.jpg" class="img-fluid avatar-80 rounded" alt="image">
                            <div class="teacher-detail ml-3">
                                <h5>Petey Cruiser</h5>
                                <p class="mb-0">Chemistry Expert</p>
                                <div class="d-flex justify-content-left">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star-half text-warning"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center mb-3">
                            <img src="../../../assets/images/user/user-2.jpg" class="img-fluid avatar-80 rounded" alt="image">
                            <div class="teacher-detail ml-3">
                                <h5>Barb Ackue</h5>
                                <p class="mb-0">Maths Expert</p>
                                <div class="d-flex justify-content-left">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex align-items-center">
                            <img src="../../../assets/images/user/user-3.jpg" class="img-fluid avatar-80 rounded" alt="image">
                            <div class="teacher-detail ml-3">
                                <h5>Maya Didas</h5>
                                <p class="mb-0">Physics Expert</p>
                                <div class="d-flex justify-content-left">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                </div>
                            </div>
                        </div>
                  </template>
                </card>
             </b-col>  
              <b-col lg="6" xl="6">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Courses Overview</h4>
                         </template>
                         <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                         </template>
                      <template v-slot:body>
                        <ApexChart element="school-chart-04" :chartOption="chart1" />
                      </template>
                </card>
             </b-col> 
          <b-col lg="6" xl="9">
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Courses Overview</h4>
                        </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                        </template>
                    <template v-slot:body>
                        <div class="table-responsive m-0">
                            <table class="table data-table mb-0 table-borderless tbl-recent-info text-body">
                                <thead>
                                    <tr class="text-dark">
                                        <th scope="col">No</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Sr</th>
                                        <th scope="col">DOB</th>
                                        <th scope="col">Roll No.</th>
                                        <th scope="col">Fees</th>
                                        <th scope="col">Standard</th>
                                        <th scope="col">Address</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1</td>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <div class="avatar-40 mr-2">
                                                    <img src="../../../assets/images/user/01.jpg" class="img-fluid rounded" alt="image">
                                                </div>
                                                <div>Maggie Potts</div>
                                            </div>
                                        </td>
                                        <td>05</td>
                                        <td>01/09/2012</td>
                                        <td>18</td>
                                        <td><div class="badge badge-success">Paid</div></td>
                                        <td> First</td>
                                        <td>U.S.A</td>
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
                                        <td>2</td>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <div class="avatar-40 mr-2">
                                                    <img src="../../../assets/images/user/02.jpg" class="img-fluid rounded" alt="image">
                                                </div>
                                                <div>John Watson</div>
                                            </div>
                                        </td>
                                        <td>05</td>
                                        <td>01/09/2004</td>
                                        <td>48</td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>Fifth</td>
                                        <td>U.S.A</td>
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
                                        <td>3</td>
                                        <td>
                                            <div class="d-flex align-items-center">
                                                <div class="avatar-40 mr-2">
                                                    <img src="../../../assets/images/user/03.jpg" class="img-fluid rounded" alt="image">
                                                </div>
                                                <div>Kadin Franci</div>
                                            </div>
                                        </td>
                                        <td>07</td>
                                        <td>01/09/2020</td>
                                        <td>47</td>
                                        <td>
                                            <div class="badge badge-success">Paid</div>
                                        </td>
                                        <td>Second</td>
                                        <td>U.S.A</td>
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
             <b-col lg="6" xl="3">
                <card class=" card-block card-stretch card-height" bodyClass="pt-5">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Students</h4>
                       </template>
                      <template v-slot:body>
                        <MorrisChart :element="item.id" :type="item.type" :data="item.bodyData" :colors="item.colors"  :height="item.height" style="height: 170px"/>
                      </template>
                 </card>
           </b-col> 
            <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Result</h4>
                       </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">Recent</a>
                      </template>
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="fit-icon-2 text-danger text-center">
                                        <i class="fas fa-flask"></i>
                                    </div>
                                    <div class="iq-result-info pl-3">
                                        <h5>Biology</h5>
                                        <p class="mb-0">7 / 14 Chapters</p>
                                    </div>
                                    <div class="progress progress-round mx-auto danger">
                                        <span class="progress-left">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <span class="progress-right">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <div class="progress-value text-danger">46%</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="fit-icon-2 text-success text-center">
                                        <i class="fas fa-square-root-alt"></i>
                                    </div>
                                    <div class="iq-result-info pl-3">
                                        <h5>Maths</h5>
                                        <p class="mb-0">5 / 10 Chapters</p>
                                    </div>
                                    <div class="progress progress-round mx-auto success">
                                        <span class="progress-left">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <span class="progress-right">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <div class="progress-value text-success">46%</div>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="fit-icon-2 text-info text-center">
                                        <i class="fas fa-history"></i>
                                    </div>
                                    <div class="iq-result-info pl-3">
                                        <h5>Physics</h5>
                                        <p class="mb-0">8 / 15 Chapters</p>
                                    </div>
                                    <div class="progress progress-round mx-auto info">
                                        <span class="progress-left">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <span class="progress-right">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <div class="progress-value text-info">90%</div>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="fit-icon-2 text-warning text-center">
                                        <i class="fas fa-atom"></i>
                                    </div>
                                    <div class="iq-result-info pl-3">
                                        <h5>Chemistry</h5>
                                        <p class="mb-0">5 / 8 Chapters</p>
                                    </div>
                                    <div class="progress progress-round mx-auto warning">
                                        <span class="progress-left">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <span class="progress-right">
                                            <span class="progress-bar"></span>
                                        </span>
                                        <div class="progress-value text-warning">90%</div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                   </template>
                </card>
           </b-col> 
            <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Activity</h4>
                       </template>
                       <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">Recent</a>
                       </template>
                     <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-warning-light text-center">
                                        <i class="fas fa-laptop-code"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Competition of making website</h5>
                                        <p class="mb-0">12/ 09/ 2020</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-info-light text-center">
                                        <i class="fas fa-table-tennis"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Physical Activity</h5>
                                        <p class="mb-0">5/ 09/ 2020</p>
                                    </div>
                                </div>
                            </li>
                            <li class="mb-4">
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-danger-light text-center">
                                        <i class="fas fa-ruler-combined"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Craft Competition</h5>
                                        <p class="mb-0">25/ 08/ 2020</p>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="icon iq-icon-box rounded bg-success-light text-center">
                                        <i class="fas fa-running"></i>
                                    </div>
                                    <div class="iq-result-info">
                                        <h5>Sport Event</h5>
                                        <p class="mb-0">10/ 08/ 2020</p>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </template>
               </card>
           </b-col>
            <b-col lg="6" xl="4" >
                <card>
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="holiday-info mr-md-5">
                                <h2>59</h2>
                                <h4>Holidays</h4>
                            </div>
                            <div class="icon iq-icon-box bg-warning-light m-0 text-center rounded">
                                <i class="fas fa-laugh"></i>
                            </div>
                        </div>
                        <div class=" mt-3">
                            <p class="mb-2">It is as impossible to withhold education from the receptive mind as it is impossible to force it upon the unreasoning.</p>
                            <p class="mb-0">- Agnes Repplierg</p>
                        </div>
                   </template>
                  </card>
                <b-row>
                    <b-col lg="6" >
                        <card>
                             <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <a href="#"><img class="img-fluid rounded-small" src="../../../assets/images/icon/08.png"
                                            alt="image"></a>
                                    <div class="ml-3">
                                        <h4>25 K</h4>
                                        <p class="mb-0">Followers</p>
                                    </div>
                                </div>
                              </template>
                       </card>
                        <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <a href="#"><img class="img-fluid rounded-small" src="../../../assets/images/icon/10.png"
                                            alt="image"></a>
                                    <div class="ml-3">
                                        <h4>689</h4>
                                        <p class="mb-0">Followers</p>
                                    </div>
                                </div>
                            </template>
                       </card>
                    </b-col>
                    <b-col lg="6">
                        <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <a href="#"><img class="img-fluid rounded-small" src="../../../assets/images/icon/09.png"
                                            alt="image"></a>
                                    <div class="ml-3">
                                        <h4>289</h4>
                                        <p class="mb-0">Followers</p>
                                    </div>
                                </div>
                            </template>
                         </card>
                        <card>
                            <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <a href="#"><img class="img-fluid rounded-small" src="../../../assets/images/icon/13.png"
                                            alt="image"></a>
                                    <div class="ml-3">
                                        <h4>15 K</h4>
                                        <p class="mb-0">Followers</p>
                                    </div>
                                </div>
                           </template>
                         </card>
                    </b-col>
                </b-row>
           </b-col>
       </b-row> 
  </b-container>
</template>
<script>
 import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
import MorrisChart from '../../../components/charts/MorrisChart'
import AmChart from '../../../components/charts/AmChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,
      MorrisChart,
      AmChart
  },
  mounted () {
   
    core.initDataTable(),
    core.fullscreen()
  },
  data () {
    return{
     chart1:{
         series: [{
      name: 'Successful deals',
      data: [60, 40, 50, 30, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 55, 28, 60, 30, 80, 30]
    }],
    colors: ["#4788ff", "#37e6b0"],
    chart: {
      height: 270,
      type: 'line',
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
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
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
      item:{
         type:"donut",
         id:"school-chart-02",
         colors: ["#4788ff", "#876cfe", "#37e6b0"],
         height:170,
         resize: true,
         hideHover: "auto",
         bodyData: [{ label: "82.3%", value: 35 },
          { label: "30.4%", value: 25 },
          { label: "60.3%", value: 40 },
         ],
          
      }
    }
  }
}
</script>
