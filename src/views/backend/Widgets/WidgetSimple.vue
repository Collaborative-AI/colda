<template>
      <b-container fluid="">
         <b-row>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <template v-slot:body>
                        <div class="text-center"><span>AVG Impressions</span>
                        </div>
                        <div class="d-flex justify-content-between align-items-center">
                           <div class="value-box">
                              <h2 class="mb-0"><span class="counter">2.648</span></h2>
                              <p class="mb-0 text-secondary line-height">26.84%</p>
                           </div>
                           <div class="iq-iconbox bg-danger-light"> <i class="ri-arrow-down-line"></i>
                           </div>
                        </div>
                        <Progressbar :value="80" color="danger" class="mt-5" />
                  </template>
               </card>
            </b-col>
             <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <template v-slot:body>
                        <div class="text-center"><span>AVG Engagements Rate</span>
                        </div>
                        <div class="d-flex justify-content-between align-items-center">
                           <div class="value-box">
                              <h2 class="mb-0"><span class="counter">89.6</span></h2>
                              <p class="mb-0 pl-2 text-secondary line-height">8.64%</p>
                           </div>
                           <div class="iq-iconbox bg-info-light"> <i class="ri-arrow-up-line"></i>
                           </div>
                        </div>
                        <Progressbar :value="50" color="info" class="mt-5" />
                     </template>
               </card>
            </b-col>
             <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <template v-slot:body>
                        <div class="text-center"><span>AVG Reach</span>
                        </div>
                        <div class="d-flex justify-content-between align-items-center">
                           <div class="value-box">
                              <h2 class="mb-0"><span class="counter">826</span></h2>
                              <p class="mb-0 pl-2 text-secondary line-height">0.86%</p>
                           </div>
                           <div class="iq-iconbox bg-success-light"> <i class="ri-arrow-up-line"></i>
                           </div>
                        </div>
                        <Progressbar :value="66" color="success" class="mt-5" />
                    </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height">
                  <template v-slot:body>
                        <div class="text-center"><span>AVG Transport</span>
                        </div>
                        <div class="d-flex justify-content-between align-items-center">
                           <div class="value-box">
                              <h2 class="mb-0"><span class="counter">7.55</span></h2>
                              <p class="mb-0 pl-2 text-secondary line-height">25.5%</p>
                           </div>
                           <div class="iq-iconbox bg-primary-light"> <i class="ri-arrow-up-line"></i>
                           </div>
                        </div>
                       
                        <Progressbar :value="70" color="primary" class="mt-5" />
                       
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height" bodyClass="bg-primary-light rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="rounded iq-card-icon bg-primary"><i class="ri-user-fill"></i>
                           </div>
                           <div class="text-right">
                              <h2 class="mb-0"><span class="counter">5600</span></h2>
                              <h5 class="">Doctors</h5>
                           </div>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height" bodyClass="bg-warning-light rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="rounded iq-card-icon bg-warning"><i class="ri-women-fill"></i>
                           </div>
                           <div class="text-right">
                              <h2 class="mb-0"><span class="counter">3450</span></h2>
                              <h5 class="">Nurses</h5>
                           </div>
                        </div>
                      </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height" bodyClass="bg-danger-light rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="rounded iq-card-icon bg-danger"><i class="ri-group-fill"></i>
                           </div>
                           <div class="text-right">
                              <h2 class="mb-0"><span class="counter">3500</span></h2>
                              <h5 class="">Patients</h5>
                           </div>
                        </div>
                      </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height" bodyClass="bg-info-light rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="rounded iq-card-icon bg-info"><i class="ri-hospital-line"></i>
                           </div>
                           <div class="text-right">
                              <h2 class="mb-0"><span class="counter">4500</span></h2>
                              <h5 class="">Pharmacists</h5>
                           </div>
                        </div>
                      </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height bg-primary rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="icon iq-icon-box rounded iq-bg-primary rounded shadow" data-wow-delay="0.2s"> <i class="las la-users"></i>
                           </div>
                           <div class="iq-text">
                              <h6 class="text-white">Customers</h6>
                              <h3 class="text-white">75</h3>
                           </div>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height bg-warning rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="icon iq-icon-box rounded iq-bg-warning rounded shadow" data-wow-delay="0.2s"> <i class="lab la-product-hunt"></i>
                           </div>
                           <div class="iq-text">
                              <h6 class="text-white">Products</h6>
                              <h3 class="text-white">60</h3>
                           </div>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height bg-success rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="icon iq-icon-box rounded iq-bg-success rounded shadow" data-wow-delay="0.2s"> <i class="las la-user-tie"></i>
                           </div>
                           <div class="iq-text">
                              <h6 class="text-white">User</h6>
                              <h3 class="text-white">80</h3>
                           </div>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height bg-danger rounded">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <div class="icon iq-icon-box rounded iq-bg-danger rounded shadow" data-wow-delay="0.2s"> <i class="lab la-buffer"></i>
                           </div>
                           <div class="iq-text">
                              <h6 class="text-white">Category</h6>
                              <h3 class="text-white">45</h3>
                           </div>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height iq-border-box iq-border-box-1 text-primary">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Worked Today</h6>
                           <h5>08:00 Hr</h5>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height iq-border-box iq-border-box-1 text-warning">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Worked This Week</h6>
                           <h5>40:00 Hr</h5>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height iq-border-box iq-border-box-1 text-danger">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Worked Issue</h6>
                           <h5>1200</h5>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col md="6" lg="3">
               <card class="card-block card-stretch card-height iq-border-box iq-border-box-1 text-info">
                     <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                           <h6>Worked Income</h6>
                           <h5>$54000</h5>
                        </div>
                     </template>
               </card>
            </b-col>
            <b-col lg="4">
               <card class="card-block card-stretch card-height">
                  <template v-slot:body>
                        <h2 class="mb-0"><span>$</span><span class="counter">3450</span></h2>
                        <p class="mb-0">Your Current Balance</p>
                        <h6 class="mb-4"><span class="text-success">20%</span> ($520)</h6>
                        <a href="javascript:void();" class="btn btn-danger d-block mt-5 mb-5"> Add Credit</a>
                        <div class="mt-2">
                           <div class="d-flex align-items-center justify-content-between">
                              <p class="mt-1 mb-2">Insurance</p>
                              <h4 class="counter">81</h4> 
                           </div>
                           <div class="iq-progress-bar-linear d-inline-block mt-0 w-100">
                             
                               <Progressbar :value="60" color="primary"  />
                             
                           </div>
                        </div>
                        <div class="mt-2">
                           <div class="d-flex align-items-center justify-content-between">
                              <p class="mt-1 mb-2">Savings</p>
                              <h4 class="counter">124</h4> 
                           </div>
                           <div class="iq-progress-bar-linear d-inline-block mt-0 w-100">
                               <Progressbar :value="70" color="success"  />
                           </div>
                        </div>
                        <div class="mt-2">
                           <div class="d-flex align-items-center justify-content-between">
                              <p class="mt-1 mb-2">Investment</p>
                              <h4 class="counter">74</h4> 
                           </div>
                           <div class="iq-progress-bar-linear d-inline-block mt-0 w-100">
                               <Progressbar :value="50" color="info"  />
                           </div>
                        </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="4" class="d-flex flex-wrap p-0">
               <b-col md="6">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                        <b-row>
                           <b-col lg="12" class="mb-2 d-flex justify-content-between">
                                 <div class="icon iq-icon-box rounded bg-primary rounded shadow" data-wow-delay="0.2s"> <i class="las la-users"></i>
                                 </div>
                           </b-col>
                           <b-col lg="12" class="mt-3">
                                 <h6 class="card-title text-uppercase text-secondary mb-0">Customer</h6>
                                 <span class="h2 mb-0 counter d-inline-block w-100">60,586</span>
                           </b-col>
                        </b-row>
                           <p class="mb-0 mt-3"> <span class="badge badge-primary mr-2"><i class="ri-arrow-up-fill"></i> 3.48%</span>
                           </p>
                     </template>
                  </card>
               </b-col>
               <b-col md="6">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                        <b-row>
                           <b-col lg="12" class="mb-2 d-flex justify-content-between">
                                 <div class="icon iq-icon-box rounded bg-warning rounded shadow" data-wow-delay="0.2s"> <i class="las la-balance-scale"></i>
                                 </div>
                             </b-col>
                           <b-col lg="12" class="mt-3">
                                 <h6 class="card-title text-uppercase text-secondary mb-0">Sales</h6>
                                 <span class="h2 mb-0 counter d-inline-block w-100">80,586</span>
                             </b-col>
                        </b-row>
                           <p class="mb-0 mt-3"> <span class="badge badge-warning mr-2"><i class="ri-arrow-up-fill"></i> 3.48%</span>
                           </p>
                        </template>
                  </card>
               </b-col>
               <b-col md="6">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                        <b-row>
                           <b-col lg="12" class="mb-2 d-flex justify-content-between">
                                 <div class="icon iq-icon-box rounded bg-info rounded shadow" data-wow-delay="0.2s"> <i class="las la-plus-circle"></i>
                                 </div>
                           </b-col>
                           <b-col lg="12" class="mt-3">
                                 <h6 class="card-title text-uppercase text-secondary mb-0">Profit</h6>
                                 <span class="h2 mb-0 d-inline-block w-100"><span class="counter">80</span>%</span>
                           </b-col>
                        </b-row>
                           <p class="mb-0 mt-3"> <span class="badge badge-info mr-2"><i class="ri-arrow-up-fill"></i> 3.48%</span>
                           </p>
                        </template>
                  </card>
               </b-col>
               <b-col md="6">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                        <b-row>
                           <b-col lg="12" class="mb-2 d-flex justify-content-between">
                                 <div class="icon iq-icon-box rounded bg-danger rounded shadow" data-wow-delay="0.2s"> <i class="las la-minus-circle"></i>
                                 </div>
                           </b-col>
                           <b-col lg="12" class="mt-3">
                                 <h6 class="card-title text-uppercase text-secondary mb-0">Loss</h6>
                                 <span class="h2 mb-0 d-inline-block w-100"><span class="counter">15</span>%</span>
                            </b-col>
                        </b-row>
                           <p class="mb-0 mt-3"> <span class="badge badge-danger mr-2"><i class="ri-arrow-up-fill"></i> 3.48%</span>
                           </p>
                        </template>
                  </card>
               </b-col>
            </b-col>
            <b-col lg="4" class="row m-0 p-0">
               <b-col md="12" lg="12">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                           <h6>Assets</h6>
                           <div class="text-center">
                              <h2>-108.56K</h2>
                              <p class="mb-0">Lorem ipsum dolor sit amet</p>
                           </div>
                     </template>
                  </card>
               </b-col>
               <b-col md="12" lg="12">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                           <h6>Liabilities</h6>
                           <div class="text-center">
                              <h2>-425.20K</h2>
                              <p class="mb-0">Lorem ipsum dolor sit amet</p>
                           </div>
                        </template>
                  </card>
               </b-col>
               <b-col md="12" lg="12">
                  <card class="card-block card-stretch card-height rounded">
                     <template v-slot:body>
                           <h6>Working Capital</h6>
                           <div class="text-center">
                              <h2>-380.40K</h2>
                              <p class="mb-0">Lorem ipsum dolor sit amet</p>
                           </div>
                        </template>
                  </card>
               </b-col>
               </b-col>
               <b-col lg="6">
                  <b-row>
                     <b-col md="6">
                        <card class="card-block card-stretch card-height">
                           <template v-slot:body>
                              <div class="top-block d-flex align-items-center justify-content-between">
                                 <h5>Revenue</h5>
                                 <span class="badge badge-primary">Monthly</span>
                              </div>
                              <h3>$<span class="counter">35000</span></h3>
                              <div class="d-flex align-items-center justify-content-between mt-1">
                                 <p class="mb-0">Total Revenue</p> <span class="text-primary">35%</span>
                              </div>
                               <Progressbar :value="55" color="primary" class="mt-3" />
                           </template>
                        </card>
                     </b-col>
                     <b-col md="6">
                        <card class="card-block card-stretch card-height">
                           <template v-slot:body>
                              <div class="top-block d-flex align-items-center justify-content-between mt-1">
                                 <h5>Orders</h5>
                                 <span class="badge badge-warning">Anual</span>
                              </div>
                              <h3><span class="counter">2500</span></h3>
                              <div class="d-flex align-items-center justify-content-between mt-1">
                                 <p class="mb-0">New Orders</p> <span class="text-warning">24%</span>
                              </div>
                               <Progressbar :value="45" color="warning" class="mt-3" />
                           </template>
                        </card>
                     </b-col>
                  </b-row>
                  <b-row>
                     <b-col md="6">
                        <card class="card-block card-stretch card-height">
                           <template v-slot:body>
                              <div class="top-block d-flex align-items-center justify-content-between mt-1">
                                 <h5>Leads</h5>
                                 <span class="badge badge-danger">Today</span>
                              </div>
                              <h3>$<span class="counter">55000</span></h3>
                              <div class="d-flex align-items-center justify-content-between">
                                 <p class="mb-0">New Leads</p> <span class="text-danger">50%</span>
                              </div>
                               <Progressbar :value="50" color="danger" class="mt-3" />
                           </template>
                        </card>
                     </b-col>
                     <b-col md="6">
                        <card class="card-block card-stretch card-height">
                           <template v-slot:body>
                              <div class="top-block d-flex align-items-center justify-content-between">
                                 <h5>Conversion Rate</h5>
                                 <span class="badge badge-info">This Month</span>
                              </div>
                              <h3><span class="counter">35</span>%</h3>
                              <div class="d-flex align-items-center justify-content-between">
                                 <p class="mb-0">This Month</p> <span class="text-info">5%</span>
                              </div>
                               <Progressbar :value="25" color="info" class="mt-3" />
                           </template>
                        </card>
                     </b-col>
                  </b-row>
               </b-col>
               <b-col lg="6">
                  <card class="card-block card-stretch card-height iq-user-profile-block">
                     <template v-slot:body>
                        <div class="user-details-block">
                           <div class="user-profile text-center">
                              <img src="../../../assets/images/user/11.png" alt="profile-img" class="avatar-60 rounded img-fluid">
                           </div>
                           <div class="text-center mt-3">
                              <h4><b>Bini Jets</b></h4>
                              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in arcu turpis. Nunc</p> <a href="#" class="btn btn-primary">Assign</a>
                           </div>
                           <hr>
                           <ul class="d-flex align-items-center justify-content-between p-0 mb-0 list-inline">
                              <li class="text-center">
                                 <h3 class="counter">4500</h3>
                                 <span>Operations</span>
                              </li>
                              <li class="text-center">
                                 <h3 class="counter">3.9</h3>
                                 <span>Medical Rating</span>
                              </li>
                           </ul>
                        </div>
                     </template>
                  </card>
               </b-col>
         </b-row>
      </b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
export default {
    name:'widgetSimple',
     mounted () {
    core.index()
  },
}
</script>