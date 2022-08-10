<template>
<b-container fluid="">
    <b-row class="content-body">
      <b-col lg="12">
          <div class="navbar-breadcrumb mb-4">
            <h4 class="mb-0 text-black">Dashboard</h4>
            <p class="mb-0"><span class="text-danger">Hi there,</span> Great to see you again</p>
          </div>
      </b-col>
      <b-col sm= "6" md-="6" lg="3">
          <card class="card-block card-stretch card-height">
            <b-card-body class="box-relative">
                <div class="service d-flex align-items-center justify-content-between">
                  <div class="service-data">
                      <h2>24%</h2>
                      <p class="mb-0">Service used</p>
                  </div>
                  <ApexChart element="service-chart-01" :chartOption="serviceChat1"  />
                </div>
            </b-card-body>
          </card >
      </b-col>
      <b-col  sm= "6" md-="6" lg="3">
          <card class="card-block card-stretch card-height">
            <b-card-body  class="box-relative">
                <div class="service d-flex align-items-center justify-content-between">
                  <div class="service-data">
                      <h2>2.5</h2>
                      <p class="mb-0">GB Stored</p>
                  </div>
                  <ApexChart element="service-chart-02" :chartOption="serviceChat2" class="service-chart" />
                </div>
            </b-card-body >
          </card>
      </b-col>
      <b-col  sm= "6" md-="6" lg="3">
          <card class="card-block card-stretch card-height bg-danger">
            <b-card-body class="box-relative">
                <div class="service d-flex align-items-center justify-content-between">
                  <div class="service-data">
                      <h2 class="text-white">351</h2>
                      <p class="mb-0">User Collected</p>
                  </div>
                  <ApexChart element="service-chart-03" :chartOption="serviceChat3" class="service-chart" />
                </div>
            </b-card-body>
          </card>
      </b-col>
      <b-col  sm= "6" md-="6" lg="3">
          <card class="card-block card-stretch card-height">
            <b-card-body class=" box-relative">
                <div class="service d-flex align-items-center justify-content-between">
                  <div class="service-data">
                      <h2>485</h2>
                      <p class="mb-0">Visitors</p>
                  </div>
                  <ApexChart element="service-chart-04" :chartOption="serviceChat4"  />
                </div>
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="7">
          <card class="card-block card-stretch card-height">
            <template v-slot:headerTitle>
                  <h4 class="card-title">Response Graph</h4>
            </template>
            <template v-slot:headerAction>
                <div class="mt-1">
                  <div class="d-flex align-items-center justify-content-between">
                      <a href="#" class="d-flex align-items-center mr-4">
                        <span class="bg-danger p-1 rounded mr-2"></span>
                        <p class="text-danger mb-0">Response Time</p>
                      </a>
                      <div class="card-header-toolbar d-flex align-items-center">
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton1" data-toggle="dropdown">
                            7 Days<i class="ri-arrow-down-s-fill ml-1"></i>
                            </span></template>
                            <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                        </div>
                      </div>
                  </div>
            </template>
            <template v-slot:body>
              <ApexChart element="activity-chart" :chartOption="activiesChart1" style="min-height: 415px;"/>
            </template>
          </card >
      </b-col>
      <b-col lg="5">
          <card class=" card-block card-stretch card-height">
            <b-card-body class="card-body c-line">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="icon icon-width avatar-70 bg-danger border border-danger-light rounded-circle text-center">
                      <i class="ri-alert-line"></i>
                  </div>
                  <div class="right-detail text-right">
                      <p class="mb-0">Total Traffic</p>
                      <h3>136.486<span class="font-size-12">TPS</span></h3>
                  </div>
                </div>
                <ul class="list-inline p-0 mt-4">
                  <li class="mb-3">
                      <div class="d-flex justify-content-between align-items-center">
                        <h5>perfBenchmark_invalid_v1</h5>
                        <div class="btn bg-danger-light rounded-normal">48.428</div>
                      </div>
                      <p class="mb-0">us-west-2</p>
                  </li>
                  <li class="mb-3">
                      <div class="d-flex justify-content-between align-items-center">
                        <h5>perfBenchmark_invalid_v1</h5>
                        <div class="btn bg-success-light rounded-normal">48.428</div>
                      </div>
                      <p class="mb-0">us-west-2</p>
                  </li>
                </ul>
                <a href="#" class="d-block text-center mt-4 text-black font-weight-500">View all<i class="ri-arrow-down-s-line"></i></a>
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="5">
          <card class="card-block card-stretch card-height bg-danger">
            <b-card-body class="c-line">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="icon icon-width avatar-70 bg-white text-danger border border-danger-light rounded-circle text-center">
                      <i class="ri-alert-line"></i>
                  </div>
                  <div class="right-detail text-right">
                      <p class="mb-0">Error Rate</p>
                      <h3 class="text-white">54.754<span class="font-size-12">%</span></h3>
                  </div>
                </div>
                <ul class="list-inline p-0 mt-5">
                  <li class="mb-3">
                      <div class="d-flex justify-content-between align-items-center">
                        <h5 class="text-white">perfBenchmark_invalid_v1</h5>
                        <div class="btn bg-white">45.365</div>
                      </div>
                      <p class="mb-0">us-west-2</p>
                  </li>
                  <li class="mb-3">
                      <div class="d-flex justify-content-between align-items-center">
                        <h5 class="text-white">perfBenchmark_invalid_v1</h5>
                        <div class="btn bg-danger-light">20.458</div>
                      </div>
                      <p class="mb-0">us-west-2</p>
                  </li>
                </ul>
                <a href="#" class="d-block text-center mt-4 text-white font-weight-500">View all<i class="ri-arrow-down-s-line"></i></a>
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="7">
          <card class=" card-block card-stretch card-height">
            <template v-slot:headerTitle>
                  <h4 class="card-title">Project Tests</h4>
            </template>
            <template v-slot:headerAction>
                <div class="card-header-toolbar d-flex align-items-center">
                  <b-dropdown  id="dropdownMenuButton2" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                      <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton2" data-toggle="dropdown">
                      Order by Creation<i class="ri-arrow-down-s-line ml-1"></i>
                      </span>
                          </template>
                     <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                  </b-dropdown>
                  <b-dropdown  id="dropdownMenuButton3" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                      <span class="dropdown-toggle dropdown-bg bg-primary p-2 xs-none" id="dropdownMenuButton3" data-toggle="dropdown">
                      Sort by Name<i class="ri-arrow-down-s-line ml-1"></i>
                      </span>
                          </template>
                      <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                  </b-dropdown>
                  </div>
            </template>
            <b-card-body class="">
                <div class="table-responsive">
                  <table class="table mb-0 mt-2 table-borderless table-test">
                      <tbody>
                        <tr>
                            <td>
                              <h6>Retail Int</h6>
                              <p class="mb-0">Author: Jason...</p>
                            </td>
                            <td>
                              <p class="mb-0">2018/03/29 @07:25</p>
                              <span class="text-primary">Last Modified</span>
                            </td>
                            <td class="text-right">
                              <div class="text-danger"><i class="ri-alert-fill"></i></div>
                              <span class="text-danger">Test Inomplete</span>
                            </td>
                            <td class="float-right">
                              <div class="d-flex align-items-center text-right">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-primary-light font-size-18"><i class="ri-calendar-2-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-play-fill"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Retail Int</h6>
                              <p class="mb-0">Author: Jason...</p>
                            </td>
                            <td>
                              <p class="mb-0">2018/03/29 @07:25</p>
                              <span class="text-primary">Last Modified</span>
                            </td>
                            <td class="text-right">
                              <div class="text-success">0/3</div>
                              <p class="mb-0">Active Runs</p>
                            </td>
                            <td class="float-right">
                              <div class="d-flex align-items-center text-right">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-primary-light font-size-18"><i class="ri-calendar-2-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-play-fill"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Retail Int</h6>
                              <p class="mb-0">Author: Jason...</p>
                            </td>
                            <td>
                              <p class="mb-0">2018/03/29 @07:25</p>
                              <span class="text-primary">Last Modified</span>
                            </td>
                            <td class="text-right">
                              <div class="text-success">2/3</div>
                              <p class="mb-0">Active Runs</p>
                            </td>
                            <td class="float-right">
                              <div class="d-flex align-items-center text-right">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-primary-light font-size-18"><i class="ri-calendar-2-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-play-fill"></i></a>
                              </div>
                            </td>
                        </tr>
                      </tbody>
                  </table>
                  <a href="#" class="d-block text-center text-black font-weight-500">View all<i class="ri-arrow-down-s-line"></i></a>
                </div>
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="8">
          <card class="card card-block card-stretch card-height">
            <div class="card-header d-flex justify-content-between">
                <div class="header-title">
                  <h4 class="card-title">Activites</h4>
                </div>
                <div class="mt-1">
                  <div class="d-flex align-items-center justify-content-between">
                      <label class="mb-0 mr-2">Data Type: </label>
                      <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                        <input type="checkbox" class="custom-control-input bg-primary" id="customCheck-1" checked="">
                        <label class="custom-control-label" for="customCheck-1"> Operations</label>
                      </div>
                      <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                        <input type="checkbox" class="custom-control-input bg-success" id="customCheck-2" checked="">
                        <label class="custom-control-label" for="customCheck-2">API Calls</label>
                      </div>
                      <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                        <input type="checkbox" class="custom-control-input bg-danger" id="customCheck-3" checked="">
                        <label class="custom-control-label" for="customCheck-3">Errors</label>
                      </div>
                  </div>
                </div>
            </div>
            <b-card-body class="card-body postitive-relative">
              <ApexChart element="activity-chart1" :chartOption="activiesChart"  />
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="4">
          <card class="card-block card-stretch card-height">
            <div class="card-header d-flex justify-content-between">
                <div class="header-title">
                  <h4 class="card-title">Activities Percentage</h4>
                </div>
                <div class="card-header-toolbar d-flex align-items-center">
                  <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                      <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton4" data-toggle="dropdown">
                      Week<i class="ri-arrow-down-s-line ml-1 text-white"></i>
                      </span>
                       </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                  </div>
                </div>
            <b-card-body class="">
                <div class="activities-content position-relative mt-5">
                  <div class="avatar-235 activity activity-1 rounded-circle bg-danger text-center">
                      <h2 class="text-white line-height-4">51%</h2>
                      <p class="mb-0 line-height-3">Increase</p>
                  </div>
                  <div class="avatar-155 m-auto activity activity-2 rounded-circle bg-primary text-center">
                      <h3 class="text-white line-height-4">31%</h3>
                      <p class="mb-0 line-height-3">Increase</p>
                  </div>
                  <div class="avatar-110 m-auto activity activity-3 rounded-circle bg-success text-center">
                      <h3 class="text-white line-height-4">8%</h3>
                      <p class="mb-0 line-height-3">Decrease</p>
                  </div>
                </div>
                <div class="d-flex justify-content-between mb-1 mt-5">
                  <div class="text-center">
                      <h3>251</h3>
                      <p class="mb-0">Operations</p>
                  </div>
                  <div class="text-center">
                      <h3>198</h3>
                      <p class="mb-0">API Calls</p>
                  </div>
                  <div class="text-center">
                      <h3>21</h3>
                      <p class="mb-0">Errors</p>
                  </div>
                </div>
            </b-card-body>
          </card>
      </b-col>
      <b-col lg="12">
          <card class="card-block card-stretch card-height">
            <div class="card-header d-flex justify-content-between">
                <div class="header-title">
                  <h4 class="card-title">Acme API Monitors</h4>
                </div>
                <div class="card-header-toolbar d-flex align-items-center">
                  <div class="dropdown">
                      <span class="btn bg-primary">Add Monitor</span>
                      </div>
                </div>
            </div>
            <b-card-body class="">
                <div class="table-responsive">
                  <table class="table mb-0 mt-2 table-borderless table-test tbl-server-info">
                      <thead>
                        <tr class="text-center">
                            <th scope="col" class="text-left">Name</th>
                            <th scope="col">Status</th>
                            <th scope="col">Performance</th>
                            <th scope="col">Uptime 24 Hours</th>
                            <th scope="col">Last Run</th>
                            <th scope="col">Actions</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                            <td>
                              <h6>Facebook/whitehouse</h6>
                              <div class="btn bg-primary-light mt-2">Sample</div>
                            </td>
                            <td class="text-center">
                              <div class="text-success font-size-24"><i class="ri-arrow-up-fill"></i></div>
                            </td>
                            <td class="text-center">
                              <div class="api-chart-01 d-inline-block">
                                <ApexChart element="api-chart-01" :chartOption="apiChart1"  />
                              </div>
                              <span class="d-block mt-2 text-danger">81ms</span>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-01 d-inline-block">
                                <ApexChart element="apitime-chart-01" :chartOption="apitimeChart1"  />
                              </div>
                              <span class="d-block mt-2 text-primary">65%</span>
                            </td>
                            <td class="text-center">
                              <div class="text-black">2018/03/29 @07:25</div>
                            </td>
                            <td class="text-center m-auto">
                              <div class="d-flex align-items-center justify-content-center">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-bar-chart-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-dark-light font-size-18"><i class="ri-delete-bin-7-fill"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Facebook/whitehouse</h6>
                            </td>
                            <td class="text-center">
                              <div class="text-danger font-size-24"><i class="ri-arrow-down-fill"></i></div>
                            </td>
                            <td class="text-center">
                              <div class="api-chart-02 d-inline-block">
                              <ApexChart element="api-chart-02" :chartOption="apiChart2"  />
                              </div>
                              <span class="d-block mt-2 text-danger">81ms</span>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="apitime-chart-02" :chartOption="apitimeChart2"  />
                              </div>
                              <span class="d-block mt-2 text-primary">65%</span>
                            </td>
                            <td class="text-center">
                              <div class="text-black">2018/03/29 @07:25</div>
                            </td>
                            <td class="text-center m-auto">
                              <div class="d-flex align-items-center justify-content-center">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-primary-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-bar-chart-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-dark-light font-size-18"><i class="ri-repeat-2-line"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-pause-line"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Facebook/whitehouse</h6>
                            </td>
                            <td class="text-center">
                              <div class="text-success font-size-24"><i class="ri-arrow-up-fill"></i></div>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="api-chart-03" :chartOption="apiChart3"  />
                              </div>
                              <span class="d-block mt-2 text-danger">81ms</span>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="apitime-chart-03" :chartOption="apitimeChart3"  />
                              </div>
                              <span class="d-block mt-2 text-primary">65%</span>
                            </td>
                            <td class="text-center">
                              <div class="text-black">2018/03/29 @07:25</div>
                            </td>
                            <td class="text-center m-auto">
                              <div class="d-flex align-items-center justify-content-center">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-primary-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-bar-chart-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-dark-light font-size-18"><i class="ri-repeat-2-line"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-pause-line"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Facebook/whitehouse</h6>
                              <div class="btn bg-primary-light mt-2">Sample</div>
                            </td>
                            <td class="text-center">
                              <div class="text-danger font-size-24"><i class="ri-arrow-down-fill"></i></div>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="api-chart-04" :chartOption="apiChart4"  />
                              </div>
                              <span class="d-block mt-2 text-danger">81ms</span>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="apitime-chart-04" :chartOption="apitimeChart4"  />
                              <span class="d-block mt-2 text-primary">65%</span>
                              </div>
                            </td>
                            <td class="text-center">
                              <div class="text-black">2018/03/29 @07:25</div>
                            </td>
                            <td class="text-center m-auto">
                              <div class="d-flex align-items-center justify-content-center">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-bar-chart-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-dark-light font-size-18"><i class="ri-delete-bin-7-fill"></i></a>
                              </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                              <h6>Facebook/whitehouse</h6>
                            </td>
                            <td class="text-center">
                              <div class="text-success font-size-24"><i class="ri-arrow-up-fill"></i></div>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="api-chart-05" :chartOption="apiChart5"  />
                              <span class="d-block mt-2 text-danger">81ms</span>
                              </div>
                            </td>
                            <td class="text-center">
                              <div class="apitime-chart-02 d-inline-block">
                              <ApexChart element="apitime-chart-05" :chartOption="apitimeChart5"  />
                              </div>
                              <span class="d-block mt-2 text-primary">65%</span>
                            </td>
                            <td class="text-center">
                              <div class="text-black">2018/03/29 @07:25</div>
                            </td>
                            <td class="text-center m-auto">
                              <div class="d-flex align-items-center justify-content-center">
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-primary-light font-size-18"><i class="ri-pencil-fill"></i></a>
                                  <a href="#" class="avatar-45 text-center ml-3 rounded bg-danger-light font-size-18"><i class="ri-bar-chart-fill"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-dark-light font-size-18"><i class="ri-repeat-2-line"></i></a>
                                  <a href="#" class="avatar-45 rounded text-center ml-3 bg-success-light font-size-18"><i class="ri-pause-line"></i></a>
                              </div>
                            </td>
                        </tr>
                      </tbody>
                  </table>
                  <div class="d-block text-center text-black font-weight-500">View all<i class="ri-arrow-down-s-line"></i></div>
                </div>
            </b-card-body>
          </card>
      </b-col>
    </b-row>
</b-container>
</template>
<script>
import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
export default {
  name: 'ServerMonitoring',
  mounted () {
    core.index()
    // core.bodyClassCheck('page-menu-horizontal')
  },
  components: { ApexChart },
  data () {
    return {
      serviceChat2: {
        series: [{
          name: 'series1',
          data: [25, 23, 28, 26]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 65,
          width: 140,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      serviceChat3: {
        series: [{
          name: 'series1',
          data: [25, 23, 28, 23]
        }],
        colors: ['#ffffff'],
        chart: {
          height: 65,
          width: 140,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      serviceChat4: {
        series: [{
          name: 'series1',
          data: [25, 27, 24, 26]
        }],
        colors: ['#1ee2ac'],
        chart: {
          height: 65,
          width: 140,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      serviceChat1: {
        series: [{
          name: 'series1',
          data: [25, 30, 22, 29]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 65,
          width: 140,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      activiesChart: {
        series: [{
          name: 'Net Profit',
          data: [44, 55, 57, 56, 61, 58]
        }, {
          name: 'Revenue',
          data: [76, 85, 101, 98, 87, 105]
        }, {
          name: 'Free Cash Flow',
          data: [35, 41, 36, 26, 45, 48]
        }],
        colors: ['#4788ff', '#ff4b4b', '#37e6b0'],
        chart: {
          type: 'bar',
          height: 400
        },
        legend: {
          show: false
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
          }
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
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
        },
        yaxis: {
          title: {
            text: ''
          },
          labels: {
            offsetX: -20,
            offsetY: 0
          }
        },
        grid: {
          padding: {
            left: -5,
            right: 0,
            bottom: -15
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return '$ ' + val + ' thousands'
            }
          }
        }
      },
      activiesChart1: {
        series: [{
          name: 'Net Profit',
          data: [90, 70, 120, 72, 120, 80, 60, 52, 85, 65, 90, 75, 110]
        }],
        colors: ['rgb(71, 136, 255)'],
        chart: {
          type: 'bar',
          height: 230
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '20%',
            endingShape: 'rounded'
          }
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
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'nov', 'dec', 'jan']
        },
        yaxis: {
          title: {
            text: ''
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return '$ ' + val + ' thousands'
            }
          }
        }
      },
      apiChart1: {
        series: [{
          name: 'series1',
          data: [4, 3, 4, 3.5, 4.1]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apiChart2: {
        series: [{
          name: 'series1',
          data: [4, 3, 4, 3.5, 4.1]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apiChart3: {
        series: [{
          name: 'series1',
          data: [4, 3, 4, 3.5, 4.1]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apiChart4: {
        series: [{
          name: 'series1',
          data: [4, 3, 4, 3.5, 4.1]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apiChart5: {
        series: [{
          name: 'series1',
          data: [4, 3, 4, 3.5, 4.1]
        }],
        colors: ['#ff4b4b'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apitimeChart1: {
        series: [{
          name: 'series1',
          data: [1, 3, 2.2, 3, 2]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apitimeChart2: {
        series: [{
          name: 'series1',
          data: [1, 3, 2.2, 3, 2]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apitimeChart3: {
        series: [{
          name: 'series1',
          data: [1, 3, 2.2, 3, 2]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apitimeChart4: {
        series: [{
          name: 'series1',
          data: [1, 3, 2.2, 3, 2]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      },
      apitimeChart5: {
        series: [{
          name: 'series1',
          data: [1, 3, 2.2, 3, 2]
        }],
        colors: ['#4788ff'],
        chart: {
          height: 30,
          width: 83,
          type: 'area',
          sparkline: {
            enabled: true
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
          categories: ['2018-09-19T00:00:00.000Z', '2018-09-19T01:30:00.000Z', '2018-09-19T02:30:00.000Z', '2018-09-19T03:30:00.000Z', '2018-09-19T04:30:00.000Z', '2018-09-19T05:30:00.000Z']
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          }
        }
      }
    }
  }
}
</script>
