<template>
  <b-container fluid="">
        <b-row class="row">            
            <b-col xl="8" lg="6" md="12" >
                <b-row class=" salon1-count">
                    <b-col xl="4" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height overflow-hidden">
                             <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-primary-light rounded">
                                        <i class="las la-user-friends primary"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Client’s</h5>
                                        <h3 class="mb-0 text-secondary">1334</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                    <Progressbar :value="85" color="primary"  colorName="primary"  class=" mt-2" midclass="iq-progress progress-1"  >
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-primary">85%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                             </template>
                            <span class="salon1-big-font">1</span>
                        </card>
                    </b-col>
                    <b-col xl="4" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height overflow-hidden">
                             <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-success-light rounded">
                                        <i class="las la-users success"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Total Staff</h5>
                                        <h3 class="mb-0  text-secondary">150</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                    <Progressbar :value="55" color="success" class=" mt-2" midclass="iq-progress progress-1" colorName="success">
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-success">55%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                             </template>
                            <span class="salon1-big-font">2</span>
                        </card>
                    </b-col>
                     <b-col xl="4" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height overflow-hidden">
                           <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-primary-light rounded">
                                        <i class="las la-calendar-day primary"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Appointments</h5>
                                        <h3 class="mb-0  text-secondary">1000</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                    <Progressbar :value="65" color="primary" class=" mt-2" midclass="iq-progress progress-1" colorName="primary">
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-primary">65%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                           </template>
                            <span class="salon1-big-font">3</span>
                        </card>
                     </b-col>
                    <b-col xl="4" lg="6" md="6" >
                        <card class="card-block card-stretch card-height overflow-hidden">
                           <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-success-light rounded">
                                        <i class="las la-headset success"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Inquiry</h5>
                                        <h3 class="mb-0  text-secondary">90</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                   <Progressbar :value="40" color="success" class=" mt-2" midclass="iq-progress progress-1" colorName="success">
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-success">40%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                           </template>
                            <span class="salon1-big-font">4</span>
                        </card>
                    </b-col>
                   <b-col xl="4" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height overflow-hidden">
                            <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-primary-light rounded">
                                        <i class="las la-signal primary"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Profit</h5>
                                        <h3 class="mb-0  text-secondary">1334</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                    <Progressbar :value="95" color="primary" class=" mt-2" midclass="iq-progress progress-1" colorName="primary">
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-primary">95%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                            </template>
                            <span class="salon1-big-font">5</span>
                        </card>
                    </b-col>
                   <b-col xl="4" lg="6" md="6" >
                        <card class="card card-block card-stretch card-height overflow-hidden">
                            <template v-slot:body>
                                <div class="media align-items-center">
                                    <div class="icon iq-icon-box bg-success-light rounded">
                                        <i class="lar la-building"></i>
                                    </div>
                                    <div class="media-body ml-3">
                                        <h5>Visitor’s</h5>
                                        <h3 class="mb-0  text-secondary">1968</h3>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center justify-content-between mt-3 position-relative">
                                   <Progressbar :value="70" color="success" class=" mt-2" midclass="iq-progress progress-1" colorName="success">
                                        <template v-slot:text>
                                            <span class="progress-text-one bg-success">70%</span>
                                        </template>
                                    </Progressbar>
                                </div>
                            </template>
                            <span class="salon1-big-font">6</span>
                        </card>
                    </b-col>
                </b-row>
            </b-col>
            <b-col xl="4" lg="6" md="12" >
                <card class=" card-block card-stretch card-height salon1-wecm" :style="`background: url(${require('../../../assets/images/layouts/layout-4/welcome-bg.png')});background-repeat:no-repeat;background-position: center right;background-size: contain;`">                    
                   <template v-slot:body>
                       <h4 class="text-secondary">Welcome</h4>
                       <h1 class="mt-4 mb-2">Mary Nara</h1>
                       <p class="mb-4">Sr. Manager</p>
                       <h4 class="text-body wid-90">Good hair reflects your style and attitude</h4>
                       <a href="#" class="btn btn-success mt-4">Learn More</a>
                   </template>
                </card>
            </b-col>
        </b-row>
        <b-row>
            <b-col lg="8" md="6" >
                <b-row>
                    <b-col sm="12" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:headerTitle>
                                    <h4 class="card-title">Stylist</h4>
                             </template>
                               <template v-slot:headerAction>
                                    <button class="btn btn-sm btn-primary">View All</button>
                               </template>
                            
                             <template v-slot:body>

                                
                                   <Slick  :option="option2">

                                    <li class="col-lg-12">
                                        <div class="card-transparent mb-0">
                                            <div class="card-body p-0">
                                                <img src="../../../assets/images/layouts/layout-4/01.jpg" class="style-img rounded w-100 img-fluid" alt="image">
                                                <div class="overly-style">
                                                    <span class="badge bg-primary "> <i class="las la-star text-white mr-1"></i> 4.5/5</span>
                                                </div>
                                                <div class="style-text text-center mt-2">
                                                    <h5>Melinda</h5>
                                                    <span>Hair Spa</span>
                                                    <ul class="list-unstyled ecommerce-social mt-2 mb-0">
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-facebook-f mr-2 text-info font-size-18"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-twitter mr-2 text-primary font-size-20"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-google-plus mr-2 text-danger font-size-20"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="col-lg-12">
                                        <div class="card-transparent mb-0">
                                            <div class="card-body p-0">
                                                <img src="../../../assets/images/layouts/layout-4/02.jpg" class="style-img rounded w-100 img-fluid" alt="image">
                                                <div class="overly-style">
                                                    <span class="badge bg-primary"> <i class="las la-star text-white mr-1"></i> 4.2/5</span>
                                                </div>
                                                <div class="style-text text-center mt-2">
                                                    <h5>Sal Monella</h5>
                                                    <span>Makeup</span>
                                                    <ul class="list-unstyled ecommerce-social mt-2 mb-0">
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-facebook-f mr-2 text-info font-size-18"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-twitter mr-2 text-primary font-size-20"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-google-plus mr-2 text-danger font-size-20"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="col-lg-12">
                                        <div class="card-transparent mb-0">
                                            <div class="card-body p-0">
                                                <img src="../../../assets/images/layouts/layout-4/03.jpg" class="style-img rounded w-100 img-fluid" alt="image">
                                                <div class="overly-style">
                                                    <span class="badge bg-primary"> <i class="las la-star text-white mr-1"></i> 4.0/5</span>
                                                </div>
                                                <div class="style-text text-center mt-2">
                                                    <h5>Maya Didas</h5>
                                                    <span>Hair Cut</span>
                                                    <ul class="list-unstyled ecommerce-social mt-2 mb-0">
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-facebook-f mr-2 text-info font-size-18"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-twitter mr-2 text-primary font-size-20"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-google-plus mr-2 text-danger font-size-20"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="col-lg-12">
                                        <div class="card-transparent mb-0">
                                            <div class="card-body p-0">
                                                <img src="../../../assets/images/layouts/layout-4/04.jpg" class="style-img rounded w-100 img-fluid" alt="image">
                                                <div class="overly-style">
                                                    <span class="badge bg-primary"> <i class="las la-star text-white mr-1"></i> 4.0/5</span>
                                                </div>
                                                <div class="style-text text-center mt-2">
                                                    <h5>Ira Membrit</h5>
                                                    <span>Hair Cut</span>
                                                    <ul class="list-unstyled ecommerce-social mt-2 mb-0">
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-facebook-f mr-2 text-info font-size-18"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-twitter mr-2 text-primary font-size-20"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-google-plus mr-2 text-danger font-size-20"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="col-lg-12">
                                        <div class="card-transparent mb-0">
                                            <div class="card-body p-0">
                                                <img src="../../../assets/images/layouts/layout-4/01.jpg" class="style-img rounded w-100 img-fluid" alt="image">
                                                <div class="overly-style">
                                                    <span class="badge bg-primary"> <i class="las la-star text-white mr-1"></i> 4.0/5</span>
                                                </div>
                                                <div class="style-text text-center mt-2">
                                                    <h5>Melinda</h5>
                                                    <span>Hair Spa</span>
                                                    <ul class="list-unstyled ecommerce-social mt-2 mb-0">
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-facebook-f mr-2 text-info font-size-18"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-twitter mr-2 text-primary font-size-20"></i></a>
                                                        </li>
                                                        <li><a href="javascript:void(0);"><i
                                                                    class="lab la-google-plus mr-2 text-danger font-size-20"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                
                                  </Slick>
                                  

                
                             </template>
                        </card>
                    </b-col>
                    <b-col lg="6">
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:headerTitle>
                                    <h4 class="card-title">Category Growth</h4>
                                </template>
                            <template v-slot:body>
                                <ApexChart element="salon-chart-02" :chartOption="chart1" />
                           </template>
                        </card>
                    </b-col>
                     <b-col lg="6">
                        <card class=" card-block card-stretch card-height"  bodyClass="text-center">
                            <template v-slot:headerTitle>
                                    <h4 class="card-title">Goal</h4>
                                </template>
                           <template v-slot:body>
                                <b-row>
                                    <b-col md="6" class=" mb-md-0 mb-3">
                                        <div class="progress-round goal-progress mx-auto" data-value="50">
                                            <span class="progress-left">
                                                <span class="progress-bar border-white" style="transform: rotate(0deg);"></span>
                                            </span>
                                            <span class="progress-right">
                                                <span class="progress-bar border-primary" style="transform: rotate(180deg);"></span>
                                            </span>
                                            <div
                                                class="progress-value w-100 h-100 rounded d-flex align-items-center justify-content-center text-center">
                                                <div class="h4 mb-0 text-primary">50%<br> Ahead</div>
                                            </div>
                                        </div>
                                        <div class="progress-value mt-4">
                                            <h4>Monthly</h4>
                                            <p class="mb-0">by Dec 2020</p>
                                        </div>
                                    </b-col>
                                    <b-col md="6" >
                                        <div class="progress-round goal-progress mx-auto" data-value="50">
                                            <span class="progress-left">
                                                <span class="progress-bar border-white" style="transform: rotate(0deg);"></span>
                                            </span>
                                            <span class="progress-right">
                                                <span class="progress-bar border-success" style="transform: rotate(180deg);"></span>
                                            </span>
                                            <div
                                                class="progress-value w-100 h-100 rounded d-flex align-items-center justify-content-center text-center">
                                                <div class="h4 mb-0 text-primary">50%<br> Ahead</div>
                                            </div>
                                        </div>
                                        <div class="progress-value mt-4">
                                            <h4>Yearly</h4>
                                            <p class="mb-0">by Dec 2020</p>
                                        </div>
                                    </b-col>
                                </b-row>
                    
                           </template>
                        </card>
                    </b-col>
                </b-row>               
            </b-col>
            <b-col lg="4" md="6">
                <card class=" card-block card-stretch card-height" bodyClass="up-com">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Upcoming Appointments</h4>
                    </template>
                        <template v-slot:headerAction>
                            <button class="btn btn-sm btn-primary">View All</button>
                        </template>
                     <template v-slot:body>
                        <ul class="list-unstyled mb-0">
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">23</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Julia Marten</h6>
                                    <p class="mb-0">Hair Styling</p>
                                    <span>8:30 To 9:30 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$25</h5>
                                </div>
                            </li>
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-success rounded-small font-size-18">
                                    <div class="date">24</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Venter Loren</h6>
                                    <p class="mb-0">Hair Spa</p>
                                    <span>9:50 To 10:45 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$50</h5>
                                </div>
                            </li>
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">25</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>John Loren</h6>
                                    <p class="mb-0">Hair Styling</p>
                                    <span>8:30 To 9:25 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$25</h5>
                                </div>
                            </li>
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-success rounded-small font-size-18">
                                    <div class="date">1</div>
                                    <div class="month">Nov</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Juliee Rosing</h6>
                                    <p class="mb-0">Makeup</p>
                                    <span>9:45 To 11:30 AM</span>
                                </div>
                                <div class="media-support-amount">
                                    <h5 class="mb-0">$70</h5>
                                </div>
                            </li>
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">2</div>
                                    <div class="month">Nov</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Darcey Nooert</h6>
                                    <p class="mb-0">Hair Spa</p>
                                    <span>10:15 To 11:30 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$50</h5>
                                </div>
                            </li>
                            <li class="d-flex mb-4 align-items-center">
                                <div class="icon iq-icon-box event-icon bg-success rounded-small font-size-18">
                                    <div class="date">3</div>
                                    <div class="month">Nov</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Petey Cruiser</h6>
                                    <p class="mb-0">Makeup</p>
                                    <span>8:30 To 11:30 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$84</h5>
                                </div>
                            </li>  
                            <li class="d-flex align-items-center">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">2</div>
                                    <div class="month">Nov</div>
                                </div>
                                <div class="media-support-info">
                                    <h6>Gail Forcewind</h6>
                                    <p class="mb-0">Hair Styling</p>
                                    <span>9:00 To 10:45 AM</span>
                                </div>
                                <div class="media-support-amount ml-3">
                                    <h5 class="mb-0">$74</h5>
                                </div>
                            </li>
                        </ul>                        
                     </template>
                </card>
            </b-col>
        </b-row>
        <b-row >
            <b-col lg="12">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Recent Customer</h4>
                    </template>
                       <template v-slot:headerAction>
                            <button class="btn btn-sm btn-primary">View All</button>
                       </template>
                      <template v-slot:body>
                        <div class="table-responsive">
                            <table class="table mb-0 table-borderless data-table">
                                <thead>
                                    <tr>
                                        <th style="width:15%">Name</th>
                                        <th style="width:10%">Date</th>
                                        <th style="width:10%">Gender</th>
                                        <th style="width:10%">Service</th>
                                        <th style="width:15%">Expert</th>
                                        <th style="width:10%">Code</th>
                                        <th style="width:10%">Number</th>
                                        <th style="width:10%">Price</th>
                                        <th style="width:10%">Status</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/01.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>William Smith</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>20/08/2020</span>
                                        </td>
                                        <td>
                                            <span>Male</span>
                                        </td>
                                        <td>
                                            <span>Hair Spa</span>
                                        </td>
                                        <td>
                                            <span>Melinda</span>
                                        </td>
                                        <td>
                                            <span>AB123</span>
                                        </td>
                                        <td>
                                            <span>1234567890</span>
                                        </td>
                                        <td>
                                            <span>25$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-danger">Confirm</span>
                                        </td>
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
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/02.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>Alena Mathew</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>2/09/2020</span>
                                        </td>
                                        <td>
                                            <span>Female</span>
                                        </td>
                                        <td>
                                            <span>Hair Cut</span>
                                        </td>
                                        <td>
                                            <span>John Martin</span>
                                        </td>
                                        <td>
                                            <span>AB124</span>
                                        </td>
                                        <td>
                                            <span>1234567890</span>
                                        </td>
                                        <td>
                                            <span>50$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-warning">Pending</span>
                                        </td>
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
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/03.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>Barry Deo</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>2/09/2020</span>
                                        </td>
                                        <td>
                                            <span>Female</span>
                                        </td>
                                        <td>
                                            <span>Hair Spa</span>
                                        </td>
                                        <td>
                                            <span>Sal Monella</span>
                                        </td>
                                        <td>
                                            <span>AB124</span>
                                        </td>
                                        <td>
                                            <span>1234567890</span>
                                        </td>
                                        <td>
                                            <span>50$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-warning">Pending</span>
                                        </td>
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
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/08.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>Kusti Franti</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>24/09/2020</span>
                                        </td>
                                        <td>
                                            <span>Female</span>
                                        </td>
                                        <td>
                                            <span>Makeup</span>
                                        </td>
                                        <td>
                                            <span>David King</span>
                                        </td>
                                        <td>
                                            <span>AB678</span>
                                        </td>
                                        <td>
                                            <span>6767687873</span>
                                        </td>
                                        <td>
                                            <span>15$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-warning">Pending</span>
                                        </td>
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
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/09.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>Jules Boutin</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>28/07/2020</span>
                                        </td>
                                        <td>
                                            <span>Female</span>
                                        </td>
                                        <td>
                                            <span>Hair Spa</span>
                                        </td>
                                        <td>
                                            <span>Anna Mull</span>
                                        </td>
                                        <td>
                                            <span>AB124</span>
                                        </td>
                                        <td>
                                            <span>789565677</span>
                                        </td>
                                        <td>
                                            <span>30$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-warning">Pending</span>
                                        </td>
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
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/user/10.jpg"
                                                        class="img-fluid avatar-40 rounded" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <span>Greta Life</span>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <span>8/10/2020</span>
                                        </td>
                                        <td>
                                            <span>Male</span>
                                        </td>
                                        <td>
                                            <span>Makeup</span>
                                        </td>
                                        <td>
                                            <span>Paul Molive</span>
                                        </td>
                                        <td>
                                            <span>AB890</span>
                                        </td>
                                        <td>
                                            <span>6768787933</span>
                                        </td>
                                        <td>
                                            <span>40$</span>
                                        </td>
                                        <td>
                                            <span class="badge bg-danger">Confirm</span>
                                        </td>
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
        name: 'Hair Style',
        data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
        }, {
            name: 'Makeup',
        data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
        }],
        chart: {
        type: 'bar',
        height: 230
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
        offsetY: -10,
        },
        stroke: {
        show: true,
        width: 2,
        colors: ['transparent']
        },
        xaxis: {
        labels: {
            maxHeight: 30,
            minHeight: 30,
        },
        categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        },
        yaxis: {
        labels:{
            maxWidth: 20,
            minWidth: 20,
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
      option2: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        slidesToShow: 4,
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
  }
}
</script>
<style scoped>
.iq-progress-bar .progress-text-one{
    top: -30px !important
}
</style>
