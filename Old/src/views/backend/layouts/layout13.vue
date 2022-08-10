<template>
  <b-container fluid="" class="p-0">
        <b-row >
            <b-col xl="8" class=" row m-0">
                <b-col lg="4" md="6">
                    <card class=" card-block card-stretch card-height bg-warning">
                        <template v-slot:body>
                            <div class="top-title-text-block">
                                <div class="d-flex align-items-center">
                                    <div class="img-icon bg-white avatar-60 rounded-small">
                                        <a href="javascript:void(0);">
                                            <img src="../../../assets/images/layouts/layout-13/s-2.png" class="img-fluid" alt="image">
                                        </a>
                                    </div>
                                    <div class="image-text ml-3">
                                        <h4 class="text-white">Konex Shoes</h4>
                                        <p class="mb-0 text-capitlise">Men's Wear</p>
                                    </div>
                                </div>
                            </div>
                            <div class="text-center">
                                <h1 class="text-white"><b>100K</b></h1>
                                <p class="mb-0 mt-2">Total Sell</p>
                            </div>
                            <div class="d-flex align-items-center justify-content-between mt-5">
                                <p class="mb-0">Total USD</p>
                                <h3 class="text-white">$59.85k</h3>
                            </div>
                        </template>
                    </card>
                </b-col>
                <b-col lg="4" md="6">
                    <card class=" card-block card-stretch card-height bg-primary">
                        <template v-slot:body>
                            <div class="top-title-text-block">
                                <div class="d-flex align-items-center">
                                    <div class="img-icon bg-white avatar-60 rounded-small">
                                        <a href="javascript:void(0);" >
                                            <img src="../../../assets/images/layouts/layout-13/s-1.png" class="img-fluid" alt="image">
                                        </a>
                                    </div>
                                    <div class="image-text ml-3">
                                        <h4 class="text-white"><b>Sumace Shoes</b></h4>
                                        <p class="mb-0 text-capitlise">Men's Wear</p>
                                    </div>
                                </div>
                            </div>
                            <div class="text-center">
                                <h1 class="text-white">200K</h1>
                                <p class="mb-0 mt-2">Total Sell</p>
                            </div>
                            <div class="d-flex align-items-center justify-content-between mt-5">
                                <p class="mb-0">Total USD</p>
                                <h3 class="text-white">$59.85k</h3>
                            </div>
                        </template>
                    </card>
                </b-col>
                <b-col lg="4" md="12">
                    <card class=" card-block card-stretch card-height bg-success">
                        <template v-slot:body>
                            <div class="top-title-text-block mb-3">
                                <h3 class="text-white line-height">Analytics</h3>
                                <p class="mb-0">Status</p>
                            </div>
                            <div class="bg-white p-3 rounded">
                                <ApexChart element="ecommerce2-chart-06" :chartOption="chart6" />
                            </div>
                        </template>
                    </card>
                </b-col>
            </b-col>
            <b-col xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:body>
                        <h3>Popular Items</h3>
                        <ApexChart element="ecommerce2-chart-07" :chartOption="chart7" />
                    </template>
                </card>
            </b-col>
            
        </b-row>
        <b-row >
            <b-col lg="8" >
                <card class=" card-block card-stretch card-height" headerClass=" mr-md-0 mr-2">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">$ 1456 M</h4>
                            <p class="mb-0">Total Revenue</p>
                     </template>
                        <template v-slot:headerAction>
                         <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg btn btn-outline-primary" id="dropdownMenuButton4"
                                    data-toggle="dropdown" aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                        </template>
                    <template v-slot:body>
                        <ApexChart element="ecommerce2-chart-01" :chartOption="chart1" />
                    </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height"  headerClass="mr-md-0 mr-2" >
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Top Selling Products</h4>
                    </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                        </template>
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/t-p-1.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex justify-content-between">
                                        <h5>Gerish Watch</h5>
                                        <div class="text-body"><b>$ 12</b></div>
                                    </div>
                                    <p class="mb-0">Electronic</p>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/t-p-2.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Brand Shoes</h5>
                                        <div class="text-body"><b>$ 48.6</b></div>
                                    </div>
                                    <p class="mb-0">Footwear</p>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/t-p-3.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Caprese bag</h5>
                                        <div class="text-body"><b>$ 12.5</b></div>
                                    </div>
                                    <p class="mb-0">Bag</p>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/t-p-4.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Ethnic Dress</h5>
                                        <div class="text-body"><b>$ 20.5</b></div>
                                    </div>
                                    <p class="mb-0">Clothes</p>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
        </b-row>
        <b-row >
            <b-col lg="6" md="6" >
                <card class=" card-block card-stretch card-height" headerClass="mr-md-0 mr-2"  bodyClass="eco2-pro">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">New Products</h4>
                    </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View All</a>
                        </template>
                    <template v-slot:body>
                        <div class="table-responsive">
                            <table class="table mb-0 table-borderless">
                                <tbody>
                                    <tr class="iq-product-border">
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/07.png"
                                                        class="avatar-40 img-fluid" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <h6>Nike Shoes</h6>
                                                    <p class="mb-0">Shoes</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <h6>Item</h6>
                                            <p class="mb-0">90</p>
                                        </td>
                                        <td>
                                            <h6>Price</h6>
                                            <p class="mb-0">$25.00</p>
                                        </td>
                                        <td>
                                            <h6>Coupon Code</h6>
                                            <p class="mb-0">Ab56789</p>
                                        </td>
                                    </tr>
                                    <tr class="iq-product-border">
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/08.png"
                                                        class="avatar-40 img-fluid" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <h6>Caprese Bag</h6>
                                                    <p class="mb-0"> Bag</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <h6>Item</h6>
                                            <p class="mb-0">50</p>
                                        </td>
                                        <td>
                                            <h6>Price</h6>
                                            <p class="mb-0">$50.00</p>
                                        </td>
                                        <td>
                                            <h6>Coupon Code</h6>
                                            <p class="mb-0">AA56789</p>
                                        </td>
                                    </tr>
                                    <tr class="iq-product-border">
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/09.png"
                                                        class="avatar-40 img-fluid" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <h6>Smart Watch</h6>
                                                    <p class=mb-0>Watch</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <h6>Item</h6>
                                            <p class=mb-0>80</p>
                                        </td>
                                        <td>
                                            <h6>Price</h6>
                                            <p class=mb-0>$75.00</p>
                                        </td>
                                        <td>
                                            <h6>Coupon Code</h6>
                                            <p class=mb-0>Ac56789</p>
                                        </td>
                                    </tr>
                                    <tr class="iq-product-border">
                                        <td>
                                            <div class="media align-items-center">
                                                <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-13/07.png"
                                                        class="avatar-40 img-fluid" alt="image"></a>
                                                <div class="media-body ml-3">
                                                    <h6>Skechers Shoes</h6>
                                                    <p class="mb-0">Shoes</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>
                                            <h6>Item</h6>
                                            <p class=mb-0>70</p>
                                        </td>
                                        <td>
                                            <h6>Price</h6>
                                            <p class=mb-0>$55.00</p>
                                        </td>
                                        <td>
                                            <h6>Coupon Code</h6>
                                            <p class=mb-0>Ac55656</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </template>
                </card>
            </b-col>
            <b-col lg="6" md="6" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Viwed On Devices</h4>
                    </template>
                    <template v-slot:body>
                        <ApexChart element="ecommerce2-chart-02" :chartOption="chart2" />
                    </template>
                </card>
            </b-col>
        </b-row>
        <b-row>
            <b-col lg="6" >
                <card class=" card-block card-stretch card-height-half" bodyClass="mini-chart">
                   <template v-slot:body>
                        <b-row class=" align-items-center">
                            <b-col md="6"  class=" col-12 mb-md-0 mb-4">
                                <ApexChart element="ecommerce2-chart-04" :chartOption="chart4" />
                            </b-col>
                            <b-col md="6" class=" col-12 iq-cart-text">
                                <div class="d-flex justify-content-between">
                                    <div>
                                        <p class="mb-1 font-size-18"><b>Balance</b></p>
                                        <h4>$ 30,000 M</h4>
                                        <p class="mb-0 mt-1">Last update yesterday</p>
                                    </div>
                                    <div>
                                        <span class="icon-arrow bg-danger-light rounded d-block m-auto"><i
                                                class="las la-long-arrow-alt-up text-danger"></i></span>
                                        <p class="text-danger text-center pt-1">+33.5%</p>
                                    </div>
                                </div>
                            </b-col>
                        </b-row>
                   </template>
                </card>
                <card class=" card-block card-stretch card-height-half" bodyClass=" mini-chart">
                    <template v-slot:body>
                        <b-row class=" align-items-center">
                            <b-col md="6"  class=" col-12 mb-md-0 mb-4">
                                <ApexChart element="ecommerce2-chart-05" :chartOption="chart5" />
                            </b-col>
                            <b-col md="6" class=" col-12 iq-cart-text country-text">
                                <div class="d-flex justify-content-between res-align">
                                    <div>
                                        <h4>Top Selling Country</h4>
                                        <p class="my-1 font-size-18"><b>INDIA</b></p>
                                        <p class="mb-0">You are at the 1st postion in top Selling</p>
                                    </div>
                                    <div>
                                        <svg width="38" height="38" class="svg-primary" viewBox="0 0 42 42" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M21 0C9.39919 0 0 9.39919 0 21C0 32.6008 9.39919 42 21 42C32.6008 42 42 32.6008 42 21C42 9.39919 32.6008 0 21 0ZM32.9734 32.9734C29.7726 36.1742 25.5218 37.9355 21 37.9355C16.4782 37.9355 12.2274 36.1742 9.02661 32.9734C5.82581 29.7726 4.06452 25.5218 4.06452 21C4.06452 16.4782 5.82581 12.2274 9.02661 9.02661C12.2274 5.82581 16.4782 4.06452 21 4.06452C25.5218 4.06452 29.7726 5.82581 32.9734 9.02661C36.1742 12.2274 37.9355 16.4782 37.9355 21C37.9355 25.5218 36.1742 29.7726 32.9734 32.9734ZM27.7742 18.2903C29.273 18.2903 30.4839 17.0794 30.4839 15.5806C30.4839 14.0819 29.273 12.871 27.7742 12.871C26.2754 12.871 25.0645 14.0819 25.0645 15.5806C25.0645 17.0794 26.2754 18.2903 27.7742 18.2903ZM14.2258 18.2903C15.7246 18.2903 16.9355 17.0794 16.9355 15.5806C16.9355 14.0819 15.7246 12.871 14.2258 12.871C12.727 12.871 11.5161 14.0819 11.5161 15.5806C11.5161 17.0794 12.727 18.2903 14.2258 18.2903ZM30.6871 23.7097H11.3129C10.6185 23.7097 10.0851 24.3024 10.1698 24.9798C10.8048 29.9927 15.1573 33.871 20.4242 33.871H21.5758C26.8427 33.871 31.1952 29.9927 31.8302 24.9798C31.9149 24.3024 31.3815 23.7097 30.6871 23.7097Z" />
                                        </svg>
                                    </div>
                                </div>
                            </b-col>
                        </b-row>
                    </template>
                </card>
            </b-col>
             <b-col lg="6" >
                <card class=" card-block card-stretch card-height" headerClass=" mr-md-0 mr-2">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Used By Country</h4>
                     </template>
                       <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton11"
                                    data-toggle="dropdown" aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1 text-white"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                       </template>
                    <template v-slot:body>
                        <div class="table-responsive">
                            <table class="table mb-0 table-borderless">
                                <tbody>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>India</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px; ">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 50%; height: 10px;" aria-valuenow="15" aria-valuemin="50"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 30%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>75%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>U.S.A</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 30%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 20%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 15%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>55%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>Canada</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 35%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 20%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 30%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>85%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>London</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 10%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>30%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>Europe</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 30%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 20%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>60%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>Japan</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 15%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 40%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>65%</h6>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 10%;">
                                            <h6>Australia</h6>
                                        </td>
                                        <td style="width: 85%;">
                                            <div class="progress m-2" style="height: 10px;">
                                                <div class="progress-bar bg-danger rounded" role="progressbar"
                                                    style="width: 10%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                    aria-valuemax="100"></div>
                                                <div class="progress-bar bg-success rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="30"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                                <div class="progress-bar bg-primary rounded-right position-relative"
                                                    role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="20"
                                                    aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                        </td>
                                        <td style="width: 5%;">
                                            <h6>30%</h6>
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
    core.fullscreen()
   
  },
  data () {
    return{
     chart1:{
         series: [
      {
        name: "High Time",
        data: [316, 450, 612, 1200, 620, 300, 200, 202, 360, 464, 612, 160]
      }
    ],
    chart: {
      height: 260,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2
      },
      toolbar: {
        show: false
      }
    },
    colors: ['#4788ff'],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    markers: {
      size: 1
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      title: {
        text: ''
      }
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
      min: 20,
      max: 1400
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5
    }
     },
     chart2:{
         series: [{
      name: 'Desktop',
      data: [53, 55, 45, 40, 40, 28, 35, 25, 20, 12, 25, 24, 20, 13, 8]
    }, {
      name: 'Tablet',
      data: [63, 62, 52, 72, 55, 80, 70, 50, 60, 40, 50, 41, 38, 32, 18]
    }, {
      name: 'Mobile',
      data: [150, 135, 144, 115, 120, 114, 133, 124, 100, 94, 96, 90, 82, 76, 86]
    }],
    colors: ['#FF4B4B', '#4788FF', '#37E6B0'],
    chart: {
      type: 'bar',
      height: 290,
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
          offsetX: -10,
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
      show: false
    },
    yaxis: {
      show: false
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
     chart4:{
         series: [{
      name: 'Net Profit',
      data: [50, 75, 55, 46, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 70, 80, 90, 90]
    }],
    colors: ["#ffebdf", "#fe721c"],
    chart: {
      type: 'bar',
      height: 170,
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
      show: false
    },
    yaxis: {
      show: false
    },
    grid: {
      padding: {
        left: 0,
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
         series: [76],
    chart: {
      type: 'radialBar',
      offsetY: 0,
      width: 400,
      sparkline: {
        enabled: true
      }
    },
    plotOptions: {
      radialBar: {
        startAngle: -90,
        endAngle: 90,
        track: {
          background: "#e7e7e7",
          strokeWidth: '100%',
          margin: 0, // margin is in pixels

        },
        dataLabels: {
          name: {
            show: false
          },
          value: {
            offsetY: -2,
            fontSize: '22px'
          }
        }
      }
    },
    grid: {
      padding: {
        top: -10
      }
    },
    labels: ['Average Results'],
     },
     chart6:{
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
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      type: 'bar',
      height: 185
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
    legend: {
      show: false,
    },
    grid: {
      show: false,
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      show: false,
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
     chart7:{
         series: [{
      name: "Session Duration",
      data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
    },
    {
      name: "Page Views",
      data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
    },
    {
      name: 'Total Visits',
      data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
    }
    ],
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      height: 260,
      type: 'line',
      zoom: {
        enabled: false
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: [5, 7, 5],
      curve: 'straight',
      dashArray: [0, 8, 5]
    },
    title: {
      text: 'Chart Page Statistics',
      align: 'left'
    },
    legend: {
      offsetY: -12,
      tooltipHoverFormatter: function (val, opts) {
        return val + ' - ' + opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] + ''
      }
    },
    markers: {
      size: 0,
      hover: {
        sizeOffset: 6
      }
    },
    xaxis: {
      categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan',
        '10 Jan', '11 Jan', '12 Jan'
      ],
    },
    tooltip: {
      y: [
        {
          title: {
            formatter: function (val) {
              return val + " (mins)"
            }
          }
        },
        {
          title: {
            formatter: function (val) {
              return val + " per session"
            }
          }
        },
        {
          title: {
            formatter: function (val) {
              return val;
            }
          }
        }
      ]
    },
    grid: {
      borderColor: '#f1f1f1',
    }
     }
    }
  }
}
</script>
