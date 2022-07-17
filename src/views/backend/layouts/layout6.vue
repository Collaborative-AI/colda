<template>
  <b-container fluid="" class="r-banner-cap">
        <b-row >
            <b-col xl="3" lg="6" md="6">
                <card class=" card-block card-stretch card-height r-odr-block"> 
                    <div class="d-flex align-items-center justify-content-between p-20">
                        <div class="text-warning">
                            <i class="fas fa-utensils resto-img"></i>
                        </div>                                    
                        <div class="iq-card-text">
                            <h2 class="mb-0 line-height">25 K</h2>                                
                            <p class="mb-0">Order Served</p>
                        </div>                     
                        <div>
                             
                            <span class="badge badge-success cust-badge">75% <i class="fas fa-angle-up ml-1"></i></span>
                        </div>
                    </div>                                       
                </card>
            </b-col>
           <b-col xl="3" lg="6" md="6">
                <card  class="card-block card-stretch card-height r-odr-block success">
                    <div class="d-flex align-items-center justify-content-between p-20">
                        <div class="text-success">
                            <i class="fas fa-users resto-img"></i>
                        </div>
                        <div class="iq-card-text">
                            <h2 class="mb-0 line-height">15 K</h2>
                            <p class="mb-0">Daily User's</p>
                        </div>
                        <div>
                            <span class="badge badge-success cust-badge">53% <i class="fas fa-angle-up ml-1"></i></span>
                        </div>
                    </div>
                </card>
           </b-col>
            <b-col xl="3" lg="6" md="6">
                <card  class="card-block card-stretch card-height r-odr-block info">
                    <div class="d-flex align-items-center justify-content-between p-20">
                        <div class="text-info">
                            <i class="fas fa-coins resto-img"></i>
                        </div>
                        <div class="iq-card-text">
                            <h2 class="mb-0 line-height">40 K</h2>
                            <p class="mb-0">Total Earning</p>
                        </div>
                        <div>
                            <span class="badge badge-danger cust-badge">25% <i class="fas fa-angle-down ml-1"></i></span>
                        </div>
                    </div>
                </card>
             </b-col>
            <b-col xl="3" lg="6" md="6">
                <card class=" card-block card-stretch card-height r-odr-block danger">
                    <div class="d-flex align-items-center justify-content-between p-20">
                        <div class="text-danger">
                            <i class="fas fa-comment-alt resto-img"></i>
                        </div>
                        <div class="iq-card-text">
                            <h2 class="mb-0 line-height">258</h2>
                            <p class="mb-0">New Feedback</p>
                        </div>
                        <div>
                            <span class="badge badge-danger cust-badge">20% <i class="fas fa-angle-down ml-1"></i></span>
                        </div>
                    </div>
                </card>
           </b-col>
        </b-row>
        <b-row >
            <b-col lg="6">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Trending Order's</h4>
                     </template>
                        <div id="trending-order-slick-arrow" class="slick-aerrow-block"><!--arrow not put in  -->

                        </div>
                     <template v-slot:body>
                     <Slick  :option="option2" classname="trending-order">
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-6/or-1.png"
                                    class="img-fluid rounded-circle avatar-120 odr-img" alt="image">
                                <div class="odr-content bg-danger-light">
                                    <span class="badge badge-white text-center"><i
                                            class="fas fa-heart text-danger"></i></span>
                                    <h5 class="mb-1">Mix Sushi Rice</h5>
                                    <h5><strong>$25.25</strong></h5>
                                    <p class="mb-0">order: 85</p>
                                </div>
                            </div>
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-6/or-2.png"
                                    class="img-fluid rounded-circle avatar-120 odr-img" alt="image">
                                <div class="odr-content bg-success-light">
                                    <span class="badge badge-white text-center"><i
                                            class="fas fa-heart text-danger"></i></span>
                                    <h5 class="mb-1">Tropical Fruits</h5>
                                    <h5><strong>$36.25</strong></h5>
                                    <p class="mb-0">order: 70</p>
                                </div>
                            </div>
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-6/or-3.png"
                                    class="img-fluid rounded-circle avatar-120 odr-img" alt="image">
                                <div class="odr-content bg-danger-light">
                                    <span class="badge badge-white text-center"><i
                                            class="fas fa-heart text-danger"></i></span>
                                    <h5 class="mb-1">Veg Fried Rice</h5>
                                    <h5><strong>$15.25</strong></h5>
                                    <p class="mb-0">order: 55</p>
                                </div>
                            </div>
                            <div class="item">
                                <img src="../../../assets/images/layouts/layout-6/or-1.png" class="img-fluid rounded-circle avatar-120 odr-img" alt="image">
                                <div class="odr-content bg-danger-light">
                                    <span class="badge badge-white text-center"><i class="fas fa-heart text-danger"></i></span>
                                    <h5 class="mb-1">Mix Sushi Rice</h5>
                                    <h5 class="mb-1"><strong>$25.25</strong></h5>
                                    <p class="mb-0">order: 85</p>
                                </div>
                            </div>
                    
                     </Slick>
                     </template>
                </card>
             </b-col>
            <b-col  lg="6" >
                <card class=" card-transparent">
                       <Slick  :option="option3" classname="resto-blog">
                   
                        <div class="item">
                            <img src="../../../assets/images/layouts/layout-6/blog-1.jpg" class="rounded img-fluid w-100" alt="image">
                            <div class="r-blog-content">                           
                                <h4 class="mb-1">Green Curry</h4>
                                <div class="d-flex justify-content-left mb-1">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-light"></i></a>
                                </div>
                                <p class="body-text font-weight-bold mb-1"><i class="las la-map-marker-alt mr-1"></i> 8517 West Norcross, GA 30092</p>
                                <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                        <div class="item">
                            <img src="../../../assets/images/layouts/layout-6/blog-2.jpg" class="rounded img-fluid w-100" alt="image">
                            <div class="r-blog-content">
                                <h4 class="mb-1">Pancake World</h4>
                                <div class="d-flex justify-content-left mb-1">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-light"></i></a>
                                </div>
                                <p class="body-text font-weight-bold mb-1"><i class="las la-map-marker-alt mr-1"></i> 8517 West Norcross, GA
                                    30092</p>
                                <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                        <div class="item">
                            <img src="../../../assets/images/layouts/layout-6/blog-3.jpg" class="rounded img-fluid w-100" alt="image">
                            <div class="r-blog-content">
                                <h4 class="mb-1">Green Curry</h4>
                                <div class="d-flex justify-content-left mb-1">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-light"></i></a>
                                </div>
                                <p class="body-text font-weight-bold mb-1"><i class="las la-map-marker-alt mr-1"></i> 8517 West Norcross, GA
                                    30092</p>
                                <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                   
                       </Slick>
                </card>
            </b-col>          
        </b-row>
        <b-row>
            <b-col lg="6">
                <card class=" card-block card-stretch card-height" bodyClass='pb-0'>
                      <template v-slot:headerTitle>
                            <h4 class="card-title">Overview</h4>
                          </template>
                         <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg bg-warning p-2" id="dropdownMenuButton7"
                                    data-toggle="dropdown" aria-expanded="false" role="button">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                       </template>
                    <template v-slot:body>
                         <AmChart element="resto-chart-03" type="line-zoom-v" :height="350" /> 
                     </template>
                </card>
            </b-col>
             <b-col lg="6">
                <card class="card-block card-stretch card-height" headerClass="position-relative" bodyClass="r-lke-tab">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Rating</h4>
                    </template>
                      <template v-slot:headerAction>
                        <div class="rate-like">
                            <i class="fas fa-star mb-1"></i>
                            <p class="mb-0">4.5/5</p>
                        </div>
                      </template>
                   <template v-slot:body>
                         <tab-nav   id="myTab-1" extraclass="nav-tabs " role="tablist">
                             <tab-nav-items :active="true" id="home-tab" ariaControls="like" dataToggle="tab" role="tab" :ariaSelected="true" title=" Customer Like" />
                             <tab-nav-items :active="false" id="profile-tab"  ariaControls="dislike" role="tab" dataToggle="tab" :ariaSelected="false" title=" Customer Dislike" />     
                         </tab-nav>
                        <div class="tab-content" id="myTabContent-2">
                            <div class="tab-pane fade show active" id="like" role="tabpanel">
                                <div class="mb-3 mt-4">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-primary mr-1"></i> Service</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="80" color="primary" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">80 <span>%</span></div>
                                </div>
                                <div class="mb-3">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-warning mr-1"></i> Food</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="60" color="warning" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">60 <span>%</span></div>
                                </div>
                                <div class="mb-3">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-success mr-1"></i> Cleanliness
                                    </p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                       <Progressbar :value="75" color="success" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">75 <span>%</span></div>
                                </div>
                                <div>
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-info mr-1"></i> Behaviour</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="70" color="info" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">70 <span>%</span></div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="dislike" role="tabpanel">
                                <div class="mb-3 mt-4">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-primary mr-1"></i> Service</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                         <Progressbar :value="50" color="primary" midclass="iq-progress"/>
                                       
                                    </div>
                                    
                                    <div class="percentage float-right font-weight-bold">50 <span>%</span></div>
                                </div>
                                <div class="mb-3">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-warning mr-1"></i> Food</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                          <Progressbar :value="35" color="warning" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">35 <span>%</span></div>
                                </div>
                                <div class="mb-3">
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-success mr-1"></i> Cleanliness
                                    </p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                          <Progressbar :value="28" color="success" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">28 <span>%</span></div>
                                </div>
                                <div>
                                    <p class="d-avail-text mb-1"><i class="fas fa-circle text-info mr-1"></i> Behaviour</p>
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                         <Progressbar :value="70" color="info" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right font-weight-bold">45 <span>%</span></div>
                                </div>
                            </div>
                        </div>
                   </template>
                </card >
            </b-col>
        </b-row>
        <b-row>
            <b-col lg="12">
                <card class=" card-block card-stretch card-height">
                      <template v-slot:headerTitle>
                            <h4 class="card-title">Order List</h4>
                      </template>
                         <template v-slot:headerAction>
                            <button class="btn btn-warning">View All</button>
                         </template>
                    <template v-slot:body>
                        <div class="table-responsive">
                            <table class="table mb-0 table-borderless data-table">
                                <thead class="order-resto">
                                    <tr>
                                        <th>Order ID</th>
                                        <th>Order Name</th>
                                        <th>Customer Name</th>
                                        <th>Date & Time</th>
                                        <th>Amount</th>
                                        <th>Ph No.</th>
                                        <th>Quantity</th>
                                        <th>Location</th>
                                        <th>Status</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                </thead>
                                <tbody class="odr-tble">
                                    <tr>
                                        <td>
                                            #12345
                                        </td>
                                        <td>Lorem Ipsum Idor
                                        </td>
                                        <td>
                                            Mario Speedwagon
                                        </td>
                                        <td>
                                            09/09/2020 , 09:30
                                        </td>
                                        <td>
                                            $85
                                        </td>
                                        <td>
                                            + 114 12345 67891
                                        </td>
                                        <td>
                                            05
                                        </td>
                                        <td>
                                            Canada
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Paid</span>
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
                                            #56565
                                        </td>
                                        <td>Lorem Ipsum Idor
                                        </td>
                                        <td>
                                            Petey Cruiser
                                        </td>
                                        <td>
                                            08/09/2020 , 11:30
                                        </td>
                                        <td>
                                            $21
                                        </td>
                                        <td>
                                            + 114 12345 67891
                                        </td>
                                        <td>
                                            15
                                        </td>
                                        <td>
                                            England
                                        </td>
                                        <td>
                                            <span class="badge badge-danger">Pending</span>
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
                                            #766768
                                        </td>
                                        <td>Lorem Ipsum Idor
                                        </td>
                                        <td>
                                            Anna Sthesia
                                        </td>
                                        <td>
                                            05/09/2020 , 07:30
                                        </td>
                                        <td>
                                            $65
                                        </td>
                                        <td>
                                            + 114 12345 67891
                                        </td>
                                        <td>
                                            08
                                        </td>
                                        <td>
                                            London
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Paid</span>
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
                                </tbody>
                            </table>
                        </div>
                     </template>
                </card >
           </b-col>
        </b-row>
  </b-container>
</template>
<script>
 import { core } from '../../../config/pluginInit'
 import AmChart from '../../../components/charts/AmChart'
export default {
  name:"DefaultDashboard",
  components:{
    AmChart
  },
  mounted () {
   
    core.initDataTable(),
    core.fullscreen()
  },
  data () {
    return{
      option2: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        slidesToShow: 2,
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
       option3: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        slidesToShow: 2,
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
