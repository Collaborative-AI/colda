<template>
  <b-container fluid="">
        <b-row>
        <b-col lg="3" md="6">
            <card class=" card-block card-stretch card-height">
              <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <div class="iq-cart-image">
                            <div class="fit-icon rounded text-cente svg-danger">
                                <svg width="50" height="52" class="svg-danger" viewBox="0 0 511 511.99978" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="m235.792969 347.265625c3.902343-3.910156 3.902343-10.238281 0-14.148437-3.90625-3.898438-10.234375-3.898438-14.144531 0-3.898438 3.910156-3.898438 10.238281 0 14.148437 3.910156 3.898437 10.238281 3.898437 14.144531 0zm0 0">
                                    </path>
                                    <path
                                        d="m188.449219 109.96875c0 60.636719 49.332031 109.972656 109.96875 109.972656s109.96875-49.335937 109.96875-109.972656-49.332031-109.96875-109.96875-109.96875-109.96875 49.332031-109.96875 109.96875zm199.945312 0c0 49.613281-40.363281 89.976562-89.976562 89.976562s-89.976563-40.363281-89.976563-89.976562c0-49.609375 40.363282-89.972656 89.976563-89.972656s89.976562 40.363281 89.976562 89.972656zm0 0">
                                    </path>
                                    <path
                                        d="m115.652344 509.042969c3.875 3.90625 10.183594 3.949219 14.109375.082031l48.46875-47.75c8.234375-8.234375 10.738281-20.425781 7.117187-31.023438l10.425782-10.054687c5.613281-5.421875 13.003906-8.410156 20.816406-8.410156h132.902344c23.578124 0 45.863281-9.054688 62.757812-25.496094.695312-.675781-5.277344 6.359375 90.667969-108.3125 14.230469-16.835937 12.101562-42.117187-4.75-56.363281-16.746094-14.113282-41.832031-12.085938-56.101563 4.460937l-58.992187 60.632813c-7.449219-9.167969-18.808594-14.882813-31.082031-14.882813h-111.480469c-15.863281-6.636719-32.695313-9.996093-50.0625-9.996093-48.140625 0-90.175781 22.234374-112.734375 63.921874-9.503906-1.800781-19.527344 1.074219-26.738282 8.285157l-47.558593 47.699219c-3.882813 3.894531-3.890625 10.195312-.015625 14.101562zm74.792968-227.121094c15.3125 0 30.117188 3.082031 44.011719 9.160156 1.265625.554688 2.628907.839844 4.007813.839844h113.527344c10.839843 0 19.996093 8.839844 19.996093 19.992187 0 11.027344-8.96875 19.996094-19.996093 19.996094h-81.566407c-5.519531 0-9.996093 4.476563-9.996093 9.996094 0 5.523438 4.476562 9.996094 9.996093 9.996094h81.566407c22.050781 0 39.988281-17.9375 39.988281-39.988282 0-1.757812-.125-3.5-.351563-5.226562 57.066406-58.660156 65.113282-66.902344 65.457032-67.3125 7.125-8.410156 19.773437-9.476562 28.1875-2.382812 8.421874 7.121093 9.488281 19.761718 2.34375 28.21875l-89.667969 107.195312c-13.09375 12.570312-30.285157 19.488281-48.457031 19.488281h-132.902344c-13.023438 0-25.351563 4.980469-34.703125 14.015625l-8.496094 8.199219-78.320313-78.316406c18.304688-34.339844 52.652344-53.871094 95.375-53.871094zm-125.320312 66.34375c3.296875-3.296875 8.359375-3.890625 12.378906-1.40625 1.730469 1.054687-3.238281-3.46875 86.589844 86.234375 3.996094 3.996094 3.78125 10.363281.054688 14.089844l-41.320313 40.707031-98.230469-98.980469zm0 0">
                                    </path>
                                    <path
                                        d="m286.421875 49.988281v11.714844c-11.636719 4.125-19.996094 15.238281-19.996094 28.273437 0 16.535157 13.453125 29.992188 29.992188 29.992188 5.511719 0 9.996093 4.484375 9.996093 9.996094 0 5.511718-4.484374 9.996094-9.996093 9.996094-4.269531 0-8.882813-2.683594-12.980469-7.5625-3.554688-4.226563-9.859375-4.769532-14.085938-1.21875-4.226562 3.554687-4.773437 9.859374-1.21875 14.085937 5.34375 6.355469 11.628907 10.785156 18.289063 13.019531v11.667969c0 5.523437 4.476563 9.996094 9.996094 9.996094s9.996093-4.472657 9.996093-9.996094v-11.714844c11.636719-4.128906 19.996094-15.242187 19.996094-28.273437 0-16.539063-13.453125-29.992188-29.992187-29.992188-5.511719 0-9.996094-4.484375-9.996094-9.996094 0-5.511718 4.484375-10 9.996094-10 3.542969 0 7.28125 1.808594 10.8125 5.226563 3.96875 3.839844 10.296875 3.734375 14.136719-.230469 3.839843-3.96875 3.734374-10.296875-.230469-14.136718-5.074219-4.910157-10.152344-7.6875-14.722657-9.203126v-11.644531c0-5.523437-4.476562-10-9.996093-10s-9.996094 4.476563-9.996094 10zm0 0">
                                    </path>
                                </svg>
                            </div>
                        </div>
                        <div class="iq-cart-text">
                            <h2>12k</h2>
                            <p class="mb-0">Total Sale</p>
                        </div>
                        <span class="light-font-overlay">1</span>
                    </div>
              </template>
            </card>
        </b-col >
         <b-col lg="3" md="6">
            <card class=" card-block card-stretch card-height">
               <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <div class="iq-cart-image">
                            <div class="fit-icon rounded text-center svg-success">
                                <svg width="52" height="50" class="svg-success" viewBox="0 0 52 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <g>
                                        <path
                                            d="M46.5904 41.1663L44.2682 13.0749C44.1234 11.2652 42.5291 9.8474 40.6384 9.8474H36.0516V9.64948C36.0516 4.32871 31.5425 0 26 0C20.4575 0 15.9485 4.32871 15.9485 9.64948V9.8474H11.3617C9.47092 9.8474 7.87649 11.2651 7.73227 13.0711L5.40934 41.1701C5.22957 43.4199 6.04258 45.6597 7.63975 47.3151C9.23692 48.9704 11.5011 49.92 13.8515 49.92H38.1484C40.4988 49.92 42.763 48.9705 44.3603 47.3151C45.9575 45.6596 46.7704 43.4199 46.5904 41.1663ZM18.9943 9.64948C18.9943 5.94106 22.1372 2.92402 26 2.92402C29.8628 2.92402 33.0057 5.94116 33.0057 9.64948V9.8474H18.9943V9.64948ZM42.1256 45.3282C41.0878 46.4037 39.6755 46.996 38.1484 46.996H13.8516C12.3245 46.996 10.9122 46.4037 9.87443 45.3282C8.83677 44.2527 8.32956 42.8553 8.44616 41.3975L10.7689 13.2985C10.7925 13.0029 11.0529 12.7714 11.3617 12.7714H15.9485V16.3726C15.9485 17.18 16.6304 17.8346 17.4714 17.8346C18.3124 17.8346 18.9943 17.18 18.9943 16.3726V12.7714H33.0057V16.3726C33.0057 17.18 33.6876 17.8346 34.5286 17.8346C35.3697 17.8346 36.0516 17.18 36.0516 16.3726V12.7714H40.6384C40.9472 12.7714 41.2076 13.003 41.2315 13.3024L43.5538 41.3936C43.6706 42.8553 43.1633 44.2526 42.1256 45.3282Z">
                                        </path>
                                        <path
                                            d="M32.861 24.7928C32.2665 24.2218 31.3021 24.2218 30.7075 24.7928L23.9073 31.321L21.2924 28.8108C20.6978 28.2398 19.7334 28.2398 19.1387 28.8108C18.5439 29.3817 18.5439 30.3074 19.1387 30.8783L22.8304 34.4224C23.1278 34.7078 23.5176 34.8507 23.9072 34.8507C24.2967 34.8507 24.6866 34.7079 24.9839 34.4224L32.8609 26.8605C33.4558 26.2894 33.4558 25.3637 32.861 24.7928Z">
                                        </path>
                                    </g>
                                </svg>
                            </div>
                        </div>
                        <div class="iq-cart-text">
                            <h2>250</h2>
                            <p class="mb-0">New Order's</p>
                        </div>
                        <span class="light-font-overlay">2</span>
                    </div>
                  </template>
             </card>
      </b-col >
        <b-col lg="3" md="6">
            <card  class="card-block card-stretch card-height">
                <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <div class="iq-cart-image">
                            <div class="fit-icon rounded text-center svg-primary">
                                <svg width="52" height="44" class="svg-primary" viewBox="0 0 52 44" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M26 17.1825C30.8722 17.1825 34.8359 13.3773 34.8359 8.7C34.8359 4.02273 30.8722 0.217499 26 0.217499C21.1278 0.217499 17.1641 4.02273 17.1641 8.7C17.1641 13.3773 21.1278 17.1825 26 17.1825ZM26 3.1425C29.1921 3.1425 31.7891 5.63557 31.7891 8.7C31.7891 11.7644 29.1921 14.2575 26 14.2575C22.8079 14.2575 20.2109 11.7644 20.2109 8.7C20.2109 5.63557 22.8079 3.1425 26 3.1425Z">
                                    </path>
                                    <path
                                        d="M43.875 17.1825C46.9551 17.1825 49.4609 14.7769 49.4609 11.82C49.4609 8.86311 46.9551 6.45749 43.875 6.45749C40.7949 6.45749 38.2891 8.86311 38.2891 11.82C38.2891 14.7769 40.7949 17.1825 43.875 17.1825ZM43.875 9.38249C45.275 9.38249 46.4141 10.476 46.4141 11.82C46.4141 13.164 45.275 14.2575 43.875 14.2575C42.475 14.2575 41.3359 13.164 41.3359 11.82C41.3359 10.476 42.475 9.38249 43.875 9.38249Z">
                                    </path>
                                    <path
                                        d="M45.1039 20.4975H42.7477C39.971 20.4975 37.5742 22.0723 36.482 24.3343C34.2333 21.9777 31.0033 20.4975 27.4197 20.4975H24.5804C20.9968 20.4975 17.7668 21.9777 15.5181 24.3343C14.4258 22.0723 12.029 20.4975 9.25234 20.4975H6.89609C3.09359 20.4975 0 23.4494 0 27.0778V37.7257C0 39.301 1.34002 40.5825 2.98716 40.5825H12.3032C12.4594 42.3277 13.9881 43.7025 15.846 43.7025H36.1541C38.0119 43.7025 39.5406 42.3277 39.6969 40.5825H48.9065C50.6124 40.5825 52.0001 39.2555 52.0001 37.6243V27.0778C52 23.4494 48.9064 20.4975 45.1039 20.4975ZM3.04688 27.0778C3.04688 25.0623 4.77364 23.4225 6.89609 23.4225H9.25234C11.3748 23.4225 13.1016 25.0623 13.1016 27.0778V28.0792C12.0771 30.6399 12.2891 32.1746 12.2891 37.6575H3.04688V27.0778ZM36.6641 40.288C36.6641 40.5579 36.4353 40.7775 36.1541 40.7775H15.8459C15.5647 40.7775 15.3359 40.5578 15.3359 40.288V32.2971C15.3359 27.4036 19.4829 23.4225 24.5803 23.4225H27.4196C32.5171 23.4225 36.6641 27.4036 36.6641 32.297V40.288ZM48.9531 37.6243C48.9531 37.6748 49.5211 37.6575 39.7109 37.6575C39.7109 32.134 39.9213 30.6357 38.8984 28.0792V27.0778C38.8984 25.0623 40.6252 23.4225 42.7477 23.4225H45.1039C47.2264 23.4225 48.9531 25.0623 48.9531 27.0778V37.6243Z">
                                    </path>
                                    <path
                                        d="M8.125 17.1825C11.2051 17.1825 13.7109 14.7769 13.7109 11.82C13.7109 8.86311 11.2051 6.45749 8.125 6.45749C5.04491 6.45749 2.53906 8.86311 2.53906 11.82C2.53906 14.7769 5.04491 17.1825 8.125 17.1825ZM8.125 9.38249C9.52504 9.38249 10.6641 10.476 10.6641 11.82C10.6641 13.164 9.52504 14.2575 8.125 14.2575C6.72496 14.2575 5.58594 13.164 5.58594 11.82C5.58594 10.476 6.72496 9.38249 8.125 9.38249Z">
                                    </path>
                                </svg>
                            
                            </div>
                        </div>
                        <div class="iq-cart-text">
                            <h2>25k</h2>
                            <p class="mb-0">Customer's</p>
                        </div>
                        <span class="light-font-overlay">3</span>
                    </div>
                </template>
            </card >
         </b-col >
        <b-col lg="3" md="6">
            <card class=" card-block card-stretch card-height">
               <template v-slot:body>
                    <div class="d-flex align-items-center justify-content-between">
                        <div class="iq-cart-image">
                            <div class="fit-icon rounded text-center svg-warning">
                                <svg width="38" height="46" class="svg-warning" viewBox="0 0 42 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M39.7657 0H2.23486C1.39352 0 0.711426 0.65481 0.711426 1.4625V39.0585V48.4575C0.711426 49.2652 1.39352 49.92 2.23486 49.92H39.7656C40.6069 49.92 41.289 49.2652 41.289 48.4575V39.0585V1.4625C41.2891 0.65481 40.607 0 39.7657 0ZM3.7583 46.995V40.521H11.2096H30.791H38.2421V46.995H3.7583ZM12.8738 37.596C13.5908 33.916 16.962 31.122 21.0004 31.122C25.0387 31.122 28.41 33.9159 29.1269 37.596H12.8738ZM38.2422 37.596H32.2115C31.4652 32.2961 26.7224 28.197 21.0004 28.197C15.2783 28.197 10.5356 32.2961 9.78918 37.596H3.7583V2.925H38.2422V37.596Z">
                                    </path>
                                    <path
                                        d="M21.0004 9.39899C17.4609 9.39899 14.5815 12.1633 14.5815 15.561C14.5815 18.9587 17.4609 21.723 21.0004 21.723C24.5397 21.723 27.419 18.9587 27.419 15.561C27.419 12.1633 24.5396 9.39899 21.0004 9.39899ZM21.0004 18.7979C19.141 18.7979 17.6284 17.3457 17.6284 15.5609C17.6284 13.7761 19.141 12.3239 21.0004 12.3239C22.8596 12.3239 24.3722 13.7761 24.3722 15.5609C24.3722 17.3458 22.8595 18.7979 21.0004 18.7979Z">
                                    </path>
                                </svg>
                            
                            </div>
                        </div>
                        <div class="iq-cart-text">
                            <h2>200</h2>
                            <p class="mb-0">New Visitor's</p>
                        </div>
                        <span class="light-font-overlay">4</span>
                    </div>
               </template>
            </card>
        </b-col >
    </b-row>
    <b-row>
        <b-col lg="8" xl="9">
            <card class=" card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">$ 1456 M</h4>
                        <p class="mb-0">Total Revenue</p>
                   </template>
                    <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton5"
                                data-toggle="dropdown" aria-expanded="false" role="button">
                                Monthly<i class="ri-arrow-down-s-line ml-1 text-white"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                    </template>
                 <template v-slot:body>
                     <ApexChart element="ecommerce-chart-01" :chartOption="chart1" />
                 </template>
           </card>
       </b-col >
       <b-col lg="4" xl="3">
            <card class=" card-block card-stretch card-height">
               <template v-slot:headerTitle>
                        <h4 class="card-title">Products</h4>
                    </template>
                     <template v-slot:headerAction>
                        <a href="#" class="btn btn-sm btn-primary view-more">View More</a>
                     </template>
                <template v-slot:body>
                    <ul class="list-inline p-0 m-0">
                        <li class="media align-items-center">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/product/prod-1.png"
                                    class="img-fluid avatar-60 rounded-small" alt="image"></a>
                            <div class="media-body ml-3">
                                <h5>Vault T-shirt</h5>
                                <p class="mb-0">100 Items</p>
                            </div>
                            <p class="mb-0"><b>$ 12.8</b></p>
                        </li>
                        <li class="media align-items-center mt-3">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/product/prod-2.png"
                                    class="img-fluid avatar-60 rounded-small" alt="image"></a>
                            <div class="media-body ml-3">
                                <h5>Shrine Watches</h5>
                                <p class="mb-0">92 Items</p>
                            </div>
                            <p class="mb-0"><b>$ 8.6</b></p>
                        </li>
                        <li class="media align-items-center mt-3">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/product/prod-3.png"
                                    class="img-fluid avatar-60 rounded-small" alt="image"></a>
                            <div class="media-body ml-3">
                                <h5>Checks Shirt</h5>
                                <p class="mb-0">50 Items</p>
                            </div>
                            <p class="mb-0"><b>$ 15.5</b></p>
                        </li>
                        <li class="media align-items-center mt-3">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/product/prod-4.png"
                                    class="img-fluid avatar-60 rounded-small" alt="image"></a>
                            <div class="media-body ml-3">
                                <h5>Ally Jacket</h5>
                                <p class="mb-0">50 Items</p>
                            </div>
                            <p class="mb-0"><b>$ 15.5</b></p>
                        </li>
                        <li class="media align-items-center mt-3">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/product/prod-5.png"
                                    class="img-fluid avatar-60 rounded-small" alt="image"></a>
                            <div class="media-body ml-3">
                                <h5>shelter shoes</h5>
                                <p class="mb-0">95 Items</p>
                            </div>
                            <p class="mb-0"><b>$ 110</b></p>
                        </li>
                    </ul>
                </template>
            </card>
         </b-col >
    </b-row>
    <b-row>
        <b-col lg="6">
            <card  class="card-block card-stretch card-height">
                <template v-slot:headerTitle>
                        <h4 class="card-title">Viwed on Devices</h4>
                    </template>
                <template v-slot:body>
                     <AmChart element="ecommerce-chart-03" type="social" :height="220" />
                  </template>
            </card >
       </b-col >
        <b-col lg="6">
            <card  class="card-block card-stretch card-height">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Sales By Category</h4>
                    </template>
                      <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton6"
                                data-toggle="dropdown" aria-expanded="false" role="button">
                                Monthly<i class="ri-arrow-down-s-line ml-1 text-white"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                     </template>
               <template v-slot:body>
                    <ul class="list-inline p-0 mb-0">
                        <li>
                            <div class="d-flex align-items-center justify-content-between mb-3 row">
                                <b-col lg="3" xl="2" >
                                    <h6>Shoes</h6>
                                </b-col>
                                <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="70" color="primary" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-primary font-weight-bold">70<span>%</span></h6> 
                                    </div>
                                </b-col>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center justify-content-between mb-3 row">
                                <b-col lg="3" xl="2" >
                                    <h6>Watch</h6>
                                 </b-col>
                                <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="50" color="success" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-success font-weight-bold">50<span>%</span></h6>
                                    </div>
                                 </b-col>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center justify-content-between mb-3 row">
                                 <b-col lg="3" xl="2" >
                                    <h6>Bag</h6>
                               </b-col>
                                 <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block iq-progress-height mt-1 w-80">
                                        <Progressbar :value="85" color="warning" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-warning font-weight-bold">85<span>%</span></h6>
                                    </div>
                                 </b-col>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center justify-content-between mb-3 row">
                                <b-col lg="3" xl="2" >
                                    <h6>Clothes</h6>
                               </b-col>
                                 <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block mt-1 iq-progress-height w-80">
                                        <Progressbar :value="68" color="info" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-info font-weight-bold">68<span>%</span></h6>
                                    </div>
                               </b-col>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center justify-content-between mb-3 row">
                               <b-col lg="3" xl="2" >
                                    <h6>Mobile</h6>
                               </b-col>
                               <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block mt-1 iq-progress-height w-80">
                                        <Progressbar :value="90" color="danger" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-danger font-weight-bold">90<span>%</span></h6>
                                    </div>
                             </b-col>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center justify-content-between row">
                                  <b-col lg="3" xl="2" >
                                    <h6>Laptop</h6>
                                </b-col>
                                <b-col lg="9" xl="10">
                                    <div class="iq-progress-bar-linear d-inline-block mt-1 iq-progress-height w-80">
                                        <Progressbar :value="55" color="secondary" midclass="iq-progress"/>
                                    </div>
                                    <div class="percentage float-right">
                                        <h6 class="text-secondary font-weight-bold">55<span>%</span></h6>
                                    </div>
                                </b-col>
                            </div>
                        </li>
                    </ul>
                 </template>
             </card >
          </b-col >
    </b-row>
    <b-row>
        <b-col lg="6" >
            <card class=" card-block card-stretch card-height">
                <template v-slot:headerTitle>
                        <h4 class="card-title">Used By Country</h4>
                     </template>
                     <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none p-0" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg bg-primary p-2" id="dropdownMenuButton7"
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
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 50%; height: 10px;" aria-valuenow="15" aria-valuemin="50"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 30%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
                                                role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="20"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </td>
                                    <td style="width: 5%;">
                                        <h6>90%</h6>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="width: 10%;">
                                        <h6>U.S.A</h6>
                                    </td>
                                    <td style="width: 85%;">
                                        <div class="progress m-2" style="height: 10px;">
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 30%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 20%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
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
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 35%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 20%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
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
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 10%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
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
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 30%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 10%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
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
                                            <div class="progress-bar bg-primary rounded" role="progressbar"
                                                style="width: 10%; height: 10px;" aria-valuenow="15" aria-valuemin="0"
                                                aria-valuemax="100"></div>
                                            <div class="progress-bar bg-danger rounded-right position-relative"
                                                role="progressbar" style="width: 30%; height: 10px;" aria-valuenow="30"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                            <div class="progress-bar bg-success rounded-right position-relative"
                                                role="progressbar" style="width: 40%; height: 10px;" aria-valuenow="20"
                                                aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                    </td>
                                    <td style="width: 5%;">
                                        <h6>75%</h6>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                 </template>
            </card>
        </b-col >
        <b-col lg="3" md="6">
            <card class=" card-block card-stretch card-height bg-dark">
                <template v-slot:body>
                    <img src="../../../assets/images/layouts/layout-9/13.png" class="img-fluid mx-auto d-block" alt="image">
                    <p class="text-white text-center mb-0 mt-3">Lorem ipsum dolor sit amet</p>
                </template>
            </card>
          </b-col >
        <b-col lg="3" md="6">
            <card class=" card-block card-stretch card-height">
                <template v-slot:headerTitle>
                        <h4 class="card-title">Top Selling</h4>
                   </template>
                  <template v-slot:headerAction>
                        <button class="btn btn-sm btn-primary">View All</button>
                    </template>
                <template v-slot:body>
                    <div class="media align-items-center">
                        <div class="iq-sell-image">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/05.png"
                                    class="img-fluid" alt="image"></a>
                        </div>
                        <div class="media-body ml-3">
                            <h4>Gerish Watch</h4>
                            <p class="mb-0">Electronic</p>
                            <span class="mb-0">$12</span>
                        </div>
                    </div>
                    <hr>
                    <div class="media align-items-center">
                        <div class="iq-sell-image">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/06.png"
                                    class="img-fluid" alt="image"></a>
                        </div>
                        <div class="media-body ml-3">
                            <h4>Shoes</h4>
                            <p class="mb-0">Footwear</p>
                            <span class="mb-0">$20</span>
                        </div>
                    </div>
                    <hr>
                    <div class="media align-items-center">
                        <div class="iq-sell-image">
                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/04.png" class="img-fluid" alt="image"></a>
                        </div>
                        <div class="media-body ml-3">
                            <h4>T-Shirt</h4>
                            <p class="mb-0">Cloth</p>
                            <span class="mb-0">$18</span>
                        </div>
                    </div>
                    
                  </template>
            </card>
        </b-col >
    </b-row>
    <b-row>
        <b-col lg="6" >
            <card class=" card-block card-stretch card-height">
              <template v-slot:headerTitle>
                        <h4 class="card-title">New Product</h4>
                   </template>
                     <template v-slot:headerAction>
                        <button class="btn btn-sm btn-primary">View All</button>
                    </template>
                <template v-slot:body>
                    <div class="table-responsive">
                        <table class="table mb-0 table-borderless">
                            <tbody>
                                <tr class="iq-product-border">
                                    <td>
                                        <div class="media align-items-center">
                                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/07.png"
                                                    class="img-fluid avatar-50" alt="image"></a>
                                            <div class="media-body ml-3">
                                                <h6>Nike Shoes</h6>
                                                <p class="mb-0">Shoes</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <h6>Item</h6>
                                        <p class="mb-0">100</p>
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
                                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/08.png"
                                                    class="img-fluid avatar-50" alt="image"></a>
                                            <div class="media-body ml-3">
                                                <h6>Caprese Bag</h6>
                                                <p class="mb-0"> Bag</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <h6>Item</h6>
                                        <p class="mb-0">100</p>
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
                                            <a href="javascript:void(0);"><img src="../../../assets/images/layouts/layout-9/09.png"
                                                    class="img-fluid avatar-50" alt="image"></a>
                                            <div class="media-body ml-3">
                                                <h6>Smart Watch</h6>
                                                <p class="mb-0">Watch</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <h6>Item</h6>
                                        <p class="mb-0">100</p>
                                    </td>
                                    <td>
                                        <h6>Price</h6>
                                        <p class="mb-0">$75.00</p>
                                    </td>
                                    <td>
                                        <h6>Coupon Code</h6>
                                        <p class="mb-0">Ac56789</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </template>
            </card>
         </b-col >
         <b-col lg="6" >
            <card class=" card-block card-stretch card-height">
                <div class="card-body">
                    <div class="header-title text-center">
                        <h3 class="card-title mb-0">Mathew Harrison California, LA</h3>
                        <div class="d-flex justify-content-center doc-social mt-2">
                            <a class="text-info mr-2" href="#"><i class="lab la-facebook-f m-0"></i></a>
                            <a class="text-warning mr-2" href="#"><i class="lab la-twitter m-0"></i></a>
                            <a class="text-success" href="#"><i class="lab la-google-plus m-0"></i></a>
                        </div>
                    </div>
                </div>
                <div class="card-body rounded bg-dark mt-3">
                    <div class="ecommerce-avtar">
                        <img src="../../../assets/images/user/10.jpg" class="img-fluid avatar-100" alt="image">
                    </div>
                    <b-row class=" iq-profile-ecommerce">
                        <b-col lg="4" md="4" >
                            <div class="card-body mathew-icon">
                                <div class="media align-items-center">
                                    <a href="javascript:void(0);"><i class="fas fa-shopping-bag text-white font-icon"></i></a>
                                    <div class="media-body  ml-3">
                                        <h3 class="text-white">20K</h3>
                                        <p class="mb-0">Item Buy</p>
                                    </div>
                                </div>
                            </div>
                       </b-col>
                        <b-col lg="4" md="4" class=" mt-3 mt-md-0">
                            <div class="card-body mathew-icon">
                                <div class="media align-items-center">
                                    <a href="javascript:void(0);"><i class="fas fa-comment-dollar text-white font-icon"></i></a>
                                    <div class="media-body ml-3">
                                        <h3 class="text-white">$1,345</h3>
                                        <p class="mb-0">Amount</p>
                                    </div>
                                </div>
                            </div>
                          </b-col>
                        <b-col lg="4" md="4" class="mt-3 mt-md-0">
                            <div class="card-body mathew-icon">
                                <div class="media align-items-center">
                                    <a href="javascript:void(0);"><i class="fas fa-shield-alt text-white font-icon f-small"></i></a>
                                    <div class="media-body ml-3">
                                        <h3 class="text-white">2 year</h3>
                                        <p class="mb-0">Member</p>
                                    </div>
                                </div>
                            </div>
                        </b-col>
                    </b-row>
                </div>
            </card>
        </b-col >
    </b-row>
  </b-container>
</template>
<script>
import AmChart from '../../../components/charts/AmChart'
import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
export default {
  name:"DefaultDashboard",
  components:{
      ApexChart,
      AmChart
  },
  mounted () {
   
   core.fullscreen()
  },
  data () {
    return{
     chart1:{
         series: [{
      name: 'Net Profit',
      data: [5, 15, 25, 35, 45, 55, 45, 35, 25, 15, 5]
     
    }, {
      name: 'Revenue',
      data: [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]
    }],
    chart: {
      type: 'bar',
      height: 350
    },
    colors: ['#fe721c', '#4788ff'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '35%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
      labels: {
        minHeight: 20,
        maxHeight: 20
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
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
      breakpoint: 578,
      options: {
        xaxis: {
          labels: {
            minHeight: 48,
            maxHeight: 48
          }
        }
      }
    }]
     }
    }
  }
}
</script>
