<template>
  <b-container >
       <b-row class=" mb-3">
            <b-col lg="12" >
                <div class="d-flex align-items-center justify-content-between welcome-content">
                    <div class="navbar-breadcrumb">
                        <h5 class="mb-0">Dashboard</h5>
                        <nav aria-label="breadcrumb">
                            <ul class="breadcrumb">
                                <li class="breadcrumb-item"><router-link to="/"><i class="las la-home mr-2"></i>Home</router-link>
                                </li>
                                <li class="breadcrumb-item active" aria-current="page"><i
                                        class="las la-hospital-alt mt-1 mr-2"></i>Hospital Dashboard</li>
                            </ul>
                        </nav>
                    </div>
                    <div class="iq-search-bar device-search">
                        <form action="#" class="searchbox">
                            <input type="text" class="text search-input" placeholder="Type here to search...">
                            <a class="search-link" href="#"><i class="ri-search-line"></i></a>
                        </form>
                    </div>
                </div>
            </b-col>
       </b-row>
        <b-row class=" hospi-row-top">
            <b-col lg="8" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Annual Report</h4>
                        </template>
                        <template v-slot:headerAction>
                        <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle dropdown-bg btn btn-outline-primary p-2" id="dropdownMenuButton4"
                                    data-toggle="dropdown" aria-expanded="false">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                            </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                         </template>
                   <template v-slot:body>
                        <b-row  class=" mb-4">
                            <b-col md="4">
                                <h4>$ 50K</h4>
                                <p class="text-primary font-weight-700">Profit</p>
                                <div class="iq-progress-bar-linear d-inline-block w-100">
                                   <Progressbar :value="35" color="primary"/>
                                </div>
                            </b-col>
                            <b-col md="4" class="mt-3 mt-md-0">
                                <h4>$ 75K</h4>
                                <p class="text-warning font-weight-700">Maintenance</p>
                                <div class="iq-progress-bar-linear d-inline-block w-100">
                                     <Progressbar :value="65" color="warning"/>
                                </div>
                            </b-col>
                             <b-col md="4" class="mt-3 mt-md-0">
                                <h4>$ 20K</h4>
                                <p class="text-success font-weight-700">Pharmacy</p>
                                <div class="iq-progress-bar-linear d-inline-block w-100">
                                     <Progressbar :value="25" color="success"/>
                                </div>
                            </b-col>
                        </b-row>
                        <AmChart element="hospital-chart-01" type="hospitalchart" :height="350" />
                     </template>
                </card>
          </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Doctor's List</h4>
                          </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-outline-primary rounded-small">View All</a>
                         </template>
                    <template v-slot:body>
                        <div class="media align-items-center border rounded p-3 mb-3">
                            <div>
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/user/05.jpg"
                                        class="img-fluid avatar-60 rounded" alt="image"></a>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="mb-2">Ms. Sommer Ray</h5>
                                <div class="d-flex align-items-center">
                                    <p class="mb-0">Age: <b>26</b>  Today 5:40 PM</p>
                                </div>
                            </div>
                        </div>
                        <div class="media align-items-center border rounded p-3 mb-3">
                            <div>
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/user/08.jpg"
                                        class="img-fluid avatar-60 rounded" alt="image"></a>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="mb-2">Mr. Samuel Jackson</h5>
                                <div class="d-flex align-items-center">
                                    <p class="mb-0">Age: <b>34</b>  Today 5:10 PM</p>
                                </div>
                            </div>
                        </div>
                        <div class="media align-items-center border rounded p-3 mb-3">
                            <div>
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/user/09.jpg" class="img-fluid avatar-60 rounded"
                                        alt="image"></a>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="mb-2">Ms. Dina Krudev</h5>
                                <div class="d-flex align-items-center">
                                    <p class="mb-0">Age: <b>55</b> Today 4:30 PM</p>
                                </div>
                            </div>
                        </div>
                        <div class="media align-items-center border rounded p-3">
                            <div>
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/user/10.jpg"
                                        class="img-fluid avatar-60 rounded" alt="image"></a>
                            </div>
                            <div class="media-body ml-3">
                                <h5 class="mb-2">Mr. Julia Marigold</h5>
                                <div class="d-flex align-items-center">
                                    <p class="mb-0">Age: <b>28</b>  Today 6:00 PM</p>
                                </div>
                            </div>
                        </div>
                    </template>
                </card>
            </b-col>
        </b-row>
        <b-row >
            <b-col lg="3" md="6" >
                <card  class="card-block card-stretch card-height position-relative overflow-hidden card-overlay-image">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="iq-cart-image">
                                <svg width="52" height="65" viewBox="0 0 52 65" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M39.9512 38.0488H36.7527C35.3671 38.0488 34.2439 36.9255 34.2439 35.5399C34.2439 34.7139 34.6602 33.9521 35.2961 33.4249C38.525 30.7475 40.5854 26.7077 40.5854 22.1951V9.51219C40.5854 4.26717 36.3182 0 31.0732 0H14.5854C10.0397 0 6.34146 3.69821 6.34146 8.2439C6.34146 9.40055 6.58094 10.5022 7.0129 11.5021C8.53651 15.0286 11.4146 18.3535 11.4146 22.1951C11.4146 26.7077 13.475 30.7475 16.7039 33.4249C17.3398 33.9521 17.7561 34.7139 17.7561 35.5399C17.7561 36.9255 16.6329 38.0488 15.2473 38.0488H12.0488C5.40508 38.0488 0 43.4539 0 50.0976V63.0341C0 64.0848 0.851785 64.9366 1.90244 64.9366H50.0976C51.1482 64.9366 52 64.0848 52 63.0341V50.0976C52 43.4539 46.5949 38.0488 39.9512 38.0488ZM14.5854 3.80488H31.0732C34.2202 3.80488 36.7805 6.36518 36.7805 9.51219C36.7805 11.1978 35.3111 12.5534 33.7378 11.9486C32.3083 11.3991 30.9971 10.5506 29.8817 9.43521C29.5251 9.07844 29.0412 8.87805 28.5366 8.87805C28.0319 8.87805 27.5481 9.07844 27.1914 9.43534C25.0971 11.5295 22.3127 12.6829 19.3508 12.6829H14.5854C14.284 12.6829 13.9898 12.6525 13.7052 12.5949C13.7002 12.5939 13.6952 12.5931 13.6902 12.5921C11.6701 12.1769 10.1463 10.385 10.1463 8.2439C10.1463 5.79622 12.1377 3.80488 14.5854 3.80488ZM15.2195 22.1951V20.6191C15.2195 18.3375 17.0692 16.4878 19.3508 16.4878C21.3293 16.4878 23.2489 16.1046 25.0249 15.3733C27.239 14.4617 29.8298 14.4588 32.0441 15.37C34.5782 16.4129 36.7805 18.5909 36.7805 21.3312V22.1951C36.7805 28.1395 31.9444 32.9756 26 32.9756C20.0556 32.9756 15.2195 28.1395 15.2195 22.1951ZM26 36.7805C26.2172 36.7805 26.4333 36.7757 26.6482 36.7662C28.5563 36.6821 30.439 38.0413 30.439 39.9512C30.439 41.0019 31.2908 41.8537 32.3415 41.8537H39.9512C44.4969 41.8537 48.1951 45.5519 48.1951 50.0976V50.3869C48.1951 52.8354 45.5379 54.36 43.4241 53.1242C42.4515 52.5556 41.8537 51.5136 41.8537 50.3869V50.0976C41.8537 49.0469 41.0019 48.1951 39.9512 48.1951C38.6356 48.1951 36.7091 49.1985 35.5733 48.5345L21.846 40.5093C21.6535 40.3967 21.5611 40.1742 21.5611 39.9512C21.5611 38.0414 23.4439 36.6821 25.3519 36.7662C25.5668 36.7757 25.7828 36.7805 26 36.7805ZM3.80488 50.0976C3.80488 46.7357 5.82778 43.8377 8.72028 42.5562C10.2127 41.8949 11.8638 42.6222 12.9416 43.8482L19.4683 51.2723C19.804 51.6542 19.5329 52.2537 19.0244 52.2537C15.5277 52.2537 12.6829 55.0984 12.6829 58.5951C12.6829 59.8258 11.8345 61.1317 10.6038 61.1317H7.5238C5.46989 61.1317 3.80488 59.4667 3.80488 57.4128V50.0976ZM16.4878 58.5951C16.4878 57.1964 17.6257 56.0585 19.0244 56.0585H22.5285C23.2579 56.0585 23.952 56.3725 24.4336 56.9203C25.8744 58.5592 24.7106 61.1317 22.5285 61.1317H19.0244C17.6257 61.1317 16.4878 59.9938 16.4878 58.5951ZM37.5625 61.1317C34.7908 61.1317 32.1532 59.9386 30.3232 57.8569L16.4615 42.0894C16.3809 41.9977 16.446 41.8537 16.5682 41.8537C16.5934 41.8537 16.6181 41.8604 16.6398 41.8731L47.9399 60.1715C48.098 60.264 48.1951 60.4333 48.1951 60.6164C48.1951 60.901 47.9644 61.1317 47.6798 61.1317H37.5625Z"
                                        fill="#FF4B4B" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-danger">500K</h2>
                                <p class="mb-0 text-danger">New Patient</p>
                            </div>
                        </div>
                    </template>
                    <div class="overlay-image svg-danger">
                        <svg height="100%" viewBox="0 0 264 113" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M108.5 68C82.4829 96.2795 31.0226 108.712 4.54413 112H259C262.2 112 263.333 108.667 263.5 107V6C263.5 1.6 259.167 0.166667 257 0H192.5C172.1 3.2 128 46.6667 108.5 68Z"
                                 />
                        </svg>
                    </div>
                </card >
             </b-col>
            <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height position-relative overflow-hidden card-overlay-image">
                   <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="iq-cart-image">
                                <svg width="62" height="57" viewBox="0 0 52 47" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M39.7522 19.5738C39.7511 19.5641 39.7504 19.5544 39.7489 19.5448C39.7421 19.4973 39.7331 19.4499 39.7202 19.4031C39.7201 19.4026 39.7199 19.4021 39.7198 19.4015C39.7078 19.3578 39.6925 19.3146 39.6752 19.2719C39.6702 19.2597 39.6648 19.2479 39.6595 19.2359C39.6459 19.2051 39.6307 19.1747 39.6142 19.1448C39.6071 19.1318 39.6001 19.1187 39.5924 19.1059C39.5882 19.099 39.5849 19.0918 39.5806 19.0848C39.5632 19.0572 39.5441 19.0312 39.5248 19.0054C39.5212 19.0006 39.5182 18.9956 39.5146 18.9908C39.4852 18.9527 39.4534 18.9173 39.4201 18.8838C39.4139 18.8774 39.4071 18.8716 39.4006 18.8654C39.3717 18.8376 39.3417 18.8114 39.3104 18.7868C39.3024 18.7806 39.2946 18.7744 39.2864 18.7684C39.2445 18.7373 39.2013 18.7084 39.1562 18.6833L21.824 8.83128L31.8034 2.54732L48.5335 12.0569L41.4875 16.4937C40.9376 16.8398 40.7726 17.5663 41.1188 18.116C41.4649 18.6659 42.1913 18.831 42.7412 18.4847L51.45 13.0009C51.8002 12.7805 52.0087 12.3924 51.9993 11.9788C51.99 11.5651 51.7643 11.187 51.4045 10.9826L32.3537 0.153696C31.9769 -0.0606553 31.5125 -0.050067 31.1455 0.180872L18.9155 7.88211C18.913 7.88364 18.9104 7.88528 18.9079 7.88681L12.7966 11.7351C12.7937 11.7369 12.7909 11.7387 12.7882 11.7404L0.549839 19.447C0.199725 19.6673 -0.00886203 20.0554 0.000549664 20.4691C0.00984371 20.8827 0.235607 21.2608 0.595369 21.4653L19.6463 32.2942C19.8268 32.3969 20.0272 32.4479 20.2276 32.4479C20.4456 32.4479 20.6632 32.3873 20.8544 32.267L29.5633 26.783C30.1131 26.4369 30.2782 25.7104 29.932 25.1607C29.586 24.6108 28.8594 24.4456 28.3096 24.792L20.1966 29.9006L3.46652 20.3908L13.446 14.1068L31.2894 24.2493V37.6823C31.2894 38.1108 31.5222 38.5053 31.8972 38.7123C32.0745 38.8102 32.2703 38.8588 32.4658 38.8588C32.6839 38.8588 32.9016 38.7982 33.0926 38.6779L39.2119 34.8246C39.554 34.6092 39.7615 34.2333 39.7615 33.8291V19.7115C39.7615 19.7046 39.7604 19.698 39.7601 19.6911C39.7594 19.652 39.7568 19.613 39.7522 19.5738ZM33.6423 35.5514V23.5649C33.6423 23.1418 33.415 22.7513 33.0471 22.5422L15.7048 12.6845L19.5651 10.2536L36.2951 19.7633L34.8303 20.6857C34.2804 21.0318 34.1153 21.7582 34.4616 22.308C34.6851 22.6633 35.0673 22.8578 35.4583 22.8578C35.6724 22.8578 35.8893 22.7993 36.0839 22.6767L37.4085 21.8427V33.1798L33.6423 35.5514Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M50.1967 15.7156L41.4878 21.1994C40.9379 21.5455 40.7728 22.272 41.1191 22.8218C41.3426 23.177 41.7248 23.3715 42.1158 23.3715C42.3299 23.3715 42.5468 23.313 42.7414 23.1905L51.4503 17.7066C52.0002 17.3605 52.1652 16.634 51.819 16.0843C51.4729 15.5344 50.7464 15.3692 50.1967 15.7156Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M28.3096 29.4977L20.1966 34.6064L1.758 24.1256C1.19353 23.8047 0.47495 24.0019 0.153893 24.567C-0.167163 25.1319 0.0303646 25.8501 0.595302 26.1711L19.6462 37C19.8267 37.1027 20.0272 37.1538 20.2275 37.1538C20.4455 37.1538 20.6631 37.0932 20.8543 36.9728L29.5632 31.4889C30.1131 31.1428 30.2781 30.4163 29.9319 29.8665C29.5859 29.3165 28.8593 29.1514 28.3096 29.4977Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M50.1967 20.4214L41.4878 25.9053C40.9379 26.2514 40.7728 26.9778 41.1191 27.5276C41.3426 27.8829 41.7248 28.0774 42.1158 28.0774C42.3299 28.0774 42.5468 28.0189 42.7414 27.8963L51.4503 22.4125C52.0002 22.0663 52.1652 21.3399 51.819 20.7901C51.4729 20.2401 50.7464 20.0751 50.1967 20.4214Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M28.3096 34.2035L20.1966 39.3122L1.758 28.8315C1.19353 28.5105 0.47495 28.7077 0.153893 29.2729C-0.167163 29.8377 0.0303646 30.5559 0.595302 30.877L19.6462 41.7058C19.8267 41.8086 20.0272 41.8596 20.2275 41.8596C20.4455 41.8596 20.6631 41.799 20.8543 41.6787L29.5632 36.1947C30.1131 35.8486 30.2781 35.1221 29.9319 34.5724C29.5859 34.0223 28.8593 33.8572 28.3096 34.2035Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M50.1967 25.1273L41.4878 30.6111C40.9379 30.9572 40.7728 31.6837 41.1191 32.2334C41.3426 32.5887 41.7248 32.7832 42.1158 32.7832C42.3299 32.7832 42.5468 32.7247 42.7414 32.6021L51.4503 27.1183C52.0002 26.7722 52.1652 26.0457 51.819 25.496C51.4729 24.9461 50.7464 24.781 50.1967 25.1273Z"
                                        fill="#37E6B0" />
                                    <path
                                        d="M28.3096 38.9094L20.1966 44.0181L1.758 33.5373C1.19353 33.2164 0.47495 33.4136 0.153893 33.9787C-0.167163 34.5436 0.0303646 35.2618 0.595302 35.5828L19.6462 46.4117C19.8267 46.5144 20.0272 46.5655 20.2275 46.5655C20.4455 46.5655 20.6631 46.5049 20.8543 46.3845L29.5632 40.9006C30.1131 40.5545 30.2781 39.828 29.9319 39.2782C29.5859 38.7282 28.8593 38.5631 28.3096 38.9094Z"
                                        fill="#37E6B0" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-success">250M</h2>
                                <p class="mb-0 text-success">Total Earning</p>
                            </div>
                        </div>
                   </template>
                    <div class="overlay-image svg-success">
                        <svg height="100%" viewBox="0 0 264 113" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M108.5 68C82.4829 96.2795 31.0226 108.712 4.54413 112H259C262.2 112 263.333 108.667 263.5 107V6C263.5 1.6 259.167 0.166667 257 0H192.5C172.1 3.2 128 46.6667 108.5 68Z" />
                        </svg>
                    </div>
                </card>
            </b-col>
             <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height  position-relative overflow-hidden card-overlay-image">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="iq-cart-image">
                                <svg width="52" height="52" viewBox="0 0 52 52" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M39.5586 27.1172C33.0403 27.1172 27.6774 32.156 27.1588 38.543H24.8412C24.6245 35.8745 23.5621 33.4418 21.9232 31.5132L31.5089 21.9274C32.4719 22.7465 33.5465 23.4102 34.716 23.9047C36.2497 24.5538 37.8787 24.8828 39.5586 24.8828C41.2384 24.8828 42.8675 24.5537 44.4011 23.9048C45.8829 23.2781 47.2134 22.3813 48.3559 21.2388C49.4985 20.0962 50.3953 18.7657 51.022 17.2839C51.6709 15.7503 52 14.1213 52 12.4414C52 10.9474 51.738 9.48492 51.2199 8.09758C51.0727 7.70148 50.6897 7.43641 50.2684 7.43641C50.1475 7.43641 50.0287 7.45773 49.9139 7.50039C49.66 7.59484 49.4579 7.78273 49.3451 8.02953C49.2324 8.27633 49.2222 8.55258 49.3167 8.80648C49.7494 9.96734 49.9688 11.1902 49.9688 12.4414C49.9688 14.6385 49.2911 16.7319 48.0369 18.4845C46.8998 16.4948 45.1826 14.9874 43.1649 14.1633C44.3746 13.1379 45.1445 11.6087 45.1445 9.90234C45.1445 6.82226 42.6387 4.31641 39.5586 4.31641C36.4785 4.31641 33.9727 6.82226 33.9727 9.90234C33.9727 11.6083 34.7422 13.1372 35.9515 14.1627C33.9335 14.9863 32.2159 16.4931 31.0786 18.4823C29.8255 16.7301 29.1484 14.6376 29.1484 12.4414C29.1484 9.66164 30.2321 7.04742 32.1973 5.08016C34.1646 3.11492 36.7788 2.03125 39.5586 2.03125C41.0169 2.03125 42.4277 2.3268 43.7511 2.90977C43.881 2.96664 44.0192 2.99609 44.1603 2.99609C44.5625 2.99609 44.9282 2.75844 45.0906 2.38977C45.3161 1.87688 45.0825 1.27664 44.5706 1.05117C42.9873 0.353438 41.3024 0 39.5606 0H39.5586C37.8787 0 36.2497 0.329063 34.716 0.978047C33.2342 1.60469 31.9038 2.50148 30.7612 3.64406C29.6187 4.78664 28.7219 6.11711 28.0952 7.59891C27.4463 9.1325 27.1172 10.7616 27.1172 12.4414C27.1172 14.1213 27.4463 15.7503 28.0952 17.2839C28.5898 18.4534 29.2534 19.5281 30.0726 20.4911L20.4869 30.0769C18.5582 28.438 16.1256 27.3756 13.4571 27.1589V24.8412C19.844 24.3226 24.8828 18.9597 24.8828 12.4414C24.8828 5.58116 19.3016 0 12.4414 0C5.58116 0 0 5.58116 0 12.4414C0 18.9597 5.03882 24.3226 11.4258 24.8412V27.1589C5.03882 27.6774 0 33.0403 0 39.5586C0 46.4188 5.58116 52 12.4414 52C18.9597 52 24.3226 46.9612 24.8412 40.5742H27.1589C27.6774 46.9612 33.0403 52 39.5586 52C46.4188 52 52 46.4188 52 39.5586C52 32.6984 46.4188 27.1172 39.5586 27.1172ZM36.0039 9.90234C36.0039 7.94229 37.5985 6.34766 39.5586 6.34766C41.5187 6.34766 43.1133 7.94229 43.1133 9.90234C43.1133 11.8552 41.5302 13.4447 39.5801 13.4565C39.5726 13.4565 39.5651 13.4561 39.5576 13.4561C39.5504 13.4561 39.5433 13.4565 39.5361 13.4565C37.5865 13.4442 36.0039 11.8549 36.0039 9.90234ZM39.5363 15.4877C39.5438 15.4877 39.5511 15.4883 39.5586 15.4883C39.5658 15.4883 39.5729 15.4878 39.58 15.4878C42.5814 15.4967 45.2705 17.2893 46.5958 20.1121C44.6691 21.881 42.1887 22.8516 39.5586 22.8516C36.9277 22.8516 34.4454 21.8803 32.5193 20.1103C33.845 17.2882 36.5345 15.4962 39.5363 15.4877ZM8.88672 9.90234C8.88672 7.94229 10.4814 6.34766 12.4414 6.34766C14.4015 6.34766 15.9961 7.94229 15.9961 9.90234C15.9961 11.8552 14.413 13.4447 12.4629 13.4565C12.4554 13.4565 12.4479 13.4561 12.4404 13.4561C12.4332 13.4561 12.4261 13.4565 12.419 13.4565C10.4693 13.4442 8.88672 11.8549 8.88672 9.90234ZM12.4414 15.4883C12.4486 15.4883 12.4557 15.4878 12.4628 15.4878C15.4627 15.4967 18.1504 17.2874 19.4763 20.1076C17.6222 21.8104 15.1513 22.8516 12.4414 22.8516C9.7305 22.8516 7.25867 21.8096 5.40434 20.1056C6.73085 17.2861 9.41891 15.4962 12.4191 15.4877C12.4266 15.4878 12.4339 15.4883 12.4414 15.4883ZM12.4414 2.03125C18.1816 2.03125 22.8516 6.7012 22.8516 12.4414C22.8516 14.6907 22.1343 16.7755 20.9168 18.4795C19.7797 16.4922 18.0637 14.9867 16.0477 14.1633C17.2574 13.1378 18.0273 11.6087 18.0273 9.90234C18.0273 6.82226 15.5215 4.31641 12.4414 4.31641C9.36132 4.31641 6.85547 6.82226 6.85547 9.90234C6.85547 11.6083 7.62501 13.1372 8.83431 14.1627C6.81799 14.9855 5.10179 16.4906 3.96429 18.4773C2.74777 16.7737 2.03125 14.6897 2.03125 12.4414C2.03125 6.7012 6.7012 2.03125 12.4414 2.03125ZM12.4414 49.9688C6.7012 49.9688 2.03125 45.2988 2.03125 39.5586C2.03125 33.8184 6.7012 29.1484 12.4414 29.1484C18.1816 29.1484 22.8516 33.8184 22.8516 39.5586C22.8516 45.2988 18.1816 49.9688 12.4414 49.9688ZM32.5215 47.2228C33.8511 44.3972 36.5486 42.6055 39.5576 42.6055C42.5667 42.6055 45.2644 44.398 46.5935 47.2247C44.7395 48.9276 42.2685 49.9688 39.5586 49.9688C36.8477 49.9688 34.3759 48.9268 32.5215 47.2228ZM39.5586 40.5742C37.5985 40.5742 36.0039 38.9796 36.0039 37.0195C36.0039 35.0595 37.5985 33.4648 39.5586 33.4648C41.5187 33.4648 43.1133 35.0595 43.1133 37.0195C43.1133 38.9796 41.5187 40.5742 39.5586 40.5742ZM48.034 45.5968C46.8969 43.6096 45.1806 42.1043 43.1643 41.2811C44.3744 40.2556 45.1445 38.7262 45.1445 37.0195C45.1445 33.9394 42.6387 31.4336 39.5586 31.4336C36.4785 31.4336 33.9727 33.9394 33.9727 37.0195C33.9727 38.7259 34.7425 40.2549 35.9521 41.2804C33.9355 42.103 32.219 43.6079 31.0815 45.5945C29.865 43.8908 29.1484 41.8069 29.1484 39.5586C29.1484 33.8184 33.8184 29.1484 39.5586 29.1484C45.2988 29.1484 49.9688 33.8184 49.9688 39.5586C49.9688 41.8079 49.2515 43.8928 48.034 45.5968Z"
                                        fill="#4788FF" />
                                    <path
                                        d="M17.829 34.1433C17.3623 33.8322 16.7318 33.9582 16.4206 34.4249L11.1085 42.3931L8.41895 38.9351C8.07445 38.4923 7.43643 38.4126 6.99372 38.757C6.55091 39.1014 6.47118 39.7394 6.81558 40.1822L10.3703 44.7525C10.563 45.0004 10.8592 45.1446 11.1719 45.1446C11.1843 45.1446 11.1967 45.1444 11.2091 45.1439C11.5353 45.132 11.8359 44.9641 12.017 44.6924L18.1107 35.5517C18.4218 35.085 18.2957 34.4544 17.829 34.1433Z"
                                        fill="#4788FF" />
                                    <path
                                        d="M47.8684 5.61539C48.4293 5.61539 48.884 5.16068 48.884 4.59976C48.884 4.03885 48.4293 3.58414 47.8684 3.58414C47.3075 3.58414 46.8528 4.03885 46.8528 4.59976C46.8528 5.16068 47.3075 5.61539 47.8684 5.61539Z"
                                        fill="#4788FF" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-primary">350</h2>
                                <p class="mb-0 text-primary">Total Staff</p>
                            </div>
                        </div>
                    </template>
                    <div class="overlay-image svg-primary">
                        <svg height="100%" viewBox="0 0 264 113" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M108.5 68C82.4829 96.2795 31.0226 108.712 4.54413 112H259C262.2 112 263.333 108.667 263.5 107V6C263.5 1.6 259.167 0.166667 257 0H192.5C172.1 3.2 128 46.6667 108.5 68Z" />
                        </svg>
                    </div>
                </card>
             </b-col>
             <b-col lg="3" md="6" >
                <card class=" card-block card-stretch card-height  position-relative overflow-hidden card-overlay-image">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between">
                            <div class="iq-cart-image">
                                <svg width="52" height="52" viewBox="0 0 52 52" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M39.2031 23.3594C40.325 23.3594 41.2344 22.45 41.2344 21.3281C41.2344 20.2063 40.325 19.2969 39.2031 19.2969C38.0813 19.2969 37.1719 20.2063 37.1719 21.3281C37.1719 22.45 38.0813 23.3594 39.2031 23.3594Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M43.875 4.0625H41.2344V2.03125C41.2344 0.909391 40.325 0 39.2031 0C38.0813 0 37.1719 0.909391 37.1719 2.03125V4.0625H27.9297V2.03125C27.9297 0.909391 27.0203 0 25.8984 0C24.7766 0 23.8672 0.909391 23.8672 2.03125V4.0625H14.7266V2.03125C14.7266 0.909391 13.8172 0 12.6953 0C11.5735 0 10.6641 0.909391 10.6641 2.03125V4.0625H8.125C3.64488 4.0625 0 7.70738 0 12.1875V43.875C0 48.3551 3.64488 52 8.125 52H23.6641C24.7859 52 25.6953 51.0906 25.6953 49.9688C25.6953 48.8469 24.7859 47.9375 23.6641 47.9375H8.125C5.88494 47.9375 4.0625 46.1151 4.0625 43.875V12.1875C4.0625 9.94744 5.88494 8.125 8.125 8.125H10.6641V10.1562C10.6641 11.2781 11.5735 12.1875 12.6953 12.1875C13.8172 12.1875 14.7266 11.2781 14.7266 10.1562V8.125H23.8672V10.1562C23.8672 11.2781 24.7766 12.1875 25.8984 12.1875C27.0203 12.1875 27.9297 11.2781 27.9297 10.1562V8.125H37.1719V10.1562C37.1719 11.2781 38.0813 12.1875 39.2031 12.1875C40.325 12.1875 41.2344 11.2781 41.2344 10.1562V8.125H43.875C46.1151 8.125 47.9375 9.94744 47.9375 12.1875V23.7656C47.9375 24.8875 48.8469 25.7969 49.9688 25.7969C51.0906 25.7969 52 24.8875 52 23.7656V12.1875C52 7.70738 48.3551 4.0625 43.875 4.0625Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M39.7109 27.4219C32.9347 27.4219 27.4219 32.9347 27.4219 39.7109C27.4219 46.4872 32.9347 52 39.7109 52C46.4872 52 52 46.4872 52 39.7109C52 32.9347 46.4872 27.4219 39.7109 27.4219ZM39.7109 47.9375C35.1749 47.9375 31.4844 44.2471 31.4844 39.7109C31.4844 35.1747 35.1749 31.4844 39.7109 31.4844C44.247 31.4844 47.9375 35.1747 47.9375 39.7109C47.9375 44.2471 44.247 47.9375 39.7109 47.9375Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M42.6562 37.6797H41.7422V35.5469C41.7422 34.425 40.8328 33.5156 39.7109 33.5156C38.5891 33.5156 37.6797 34.425 37.6797 35.5469V39.7109C37.6797 40.8328 38.5891 41.7422 39.7109 41.7422H42.6562C43.7781 41.7422 44.6875 40.8328 44.6875 39.7109C44.6875 38.5891 43.7781 37.6797 42.6562 37.6797Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M30.3672 23.3594C31.489 23.3594 32.3984 22.45 32.3984 21.3281C32.3984 20.2063 31.489 19.2969 30.3672 19.2969C29.2454 19.2969 28.3359 20.2063 28.3359 21.3281C28.3359 22.45 29.2454 23.3594 30.3672 23.3594Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M21.5312 32.1953C22.6531 32.1953 23.5625 31.2859 23.5625 30.1641C23.5625 29.0422 22.6531 28.1328 21.5312 28.1328C20.4094 28.1328 19.5 29.0422 19.5 30.1641C19.5 31.2859 20.4094 32.1953 21.5312 32.1953Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M12.6953 23.3594C13.8171 23.3594 14.7266 22.45 14.7266 21.3281C14.7266 20.2063 13.8171 19.2969 12.6953 19.2969C11.5735 19.2969 10.6641 20.2063 10.6641 21.3281C10.6641 22.45 11.5735 23.3594 12.6953 23.3594Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M12.6953 32.1953C13.8171 32.1953 14.7266 31.2859 14.7266 30.1641C14.7266 29.0422 13.8171 28.1328 12.6953 28.1328C11.5735 28.1328 10.6641 29.0422 10.6641 30.1641C10.6641 31.2859 11.5735 32.1953 12.6953 32.1953Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M12.6953 41.0312C13.8171 41.0312 14.7266 40.1218 14.7266 39C14.7266 37.8782 13.8171 36.9688 12.6953 36.9688C11.5735 36.9688 10.6641 37.8782 10.6641 39C10.6641 40.1218 11.5735 41.0312 12.6953 41.0312Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M21.5312 41.0312C22.6531 41.0312 23.5625 40.1218 23.5625 39C23.5625 37.8782 22.6531 36.9688 21.5312 36.9688C20.4094 36.9688 19.5 37.8782 19.5 39C19.5 40.1218 20.4094 41.0312 21.5312 41.0312Z"
                                        fill="#FE721C" />
                                    <path
                                        d="M21.5312 23.3594C22.6531 23.3594 23.5625 22.45 23.5625 21.3281C23.5625 20.2063 22.6531 19.2969 21.5312 19.2969C20.4094 19.2969 19.5 20.2063 19.5 21.3281C19.5 22.45 20.4094 23.3594 21.5312 23.3594Z"
                                        fill="#FE721C" />
                                </svg>
                            </div>
                            <div class="iq-cart-text">
                                <h2 class="text-warning">500</h2>
                                <p class="mb-0 text-warning">Appointment</p>
                            </div>
                        </div>
                    </template>
                    <div class="overlay-image svg-warning">
                        <svg height="100%" viewBox="0 0 264 113" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M108.5 68C82.4829 96.2795 31.0226 108.712 4.54413 112H259C262.2 112 263.333 108.667 263.5 107V6C263.5 1.6 259.167 0.166667 257 0H192.5C172.1 3.2 128 46.6667 108.5 68Z" />
                        </svg>
                    </div>
                </card>
           </b-col>
        </b-row>
        <b-row >
            <b-col lg="6" >
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Patient Survey</h4>
                        </template>
                       <template v-slot:headerAction>
                             <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                            <template v-slot:button-content>
                                <span class="dropdown-toggle dropdown-bg btn btn-outline-primary p-2" id="dropdownMenuButton4"
                                        data-toggle="dropdown" aria-expanded="false">
                                        Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                </span>
                            </template>
                            <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                            <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                            </b-dropdown>
                        </template>
                    <template v-slot:body>
                        <MorrisChart :element="item.id" :type="item.type" :data="item.bodyData" :colors="item.colors"/>
                     </template>
                </card>
             </b-col>
             <b-col lg="6" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">By Country</h4>
                        </template>
                        <template v-slot:headerAction>
                             <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                            <template v-slot:button-content>
                                <span class="dropdown-toggle dropdown-bg btn btn-outline-primary p-2" id="dropdownMenuButton4"
                                        data-toggle="dropdown" aria-expanded="false">
                                        Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                </span>
                            </template>
                            <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                            <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                            </b-dropdown>
                         </template>
                    <template v-slot:body>
                         <ApexChart element="hospital-chart-03" :chartOption="chart2"/>
                    </template>
                </card>
             </b-col>
        </b-row>
        <b-row >
            <b-col lg="8" >
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Operation Survey</h4>
                        </template>
                        <template v-slot:headerAction>
                             <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                            <template v-slot:button-content>
                                <span class="dropdown-toggle dropdown-bg btn btn-outline-primary p-2" id="dropdownMenuButton4"
                                        data-toggle="dropdown" aria-expanded="false">
                                        Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                </span>
                            </template>
                            <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                            <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                            </b-dropdown>
                      </template>
                     <template v-slot:body>
                         <ApexChart element="hospital-chart-04" :chartOption="chart3"/>
                     </template>
                </card>
            </b-col>
           <b-col lg="4" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center">
                     <template v-slot:body>
    
                        <img src="../../../assets/images/user/user-1.jpg"
                            class="img-fluid d-inline-block avatar-100 mx-auto rounded mb-4" alt="image">
    
                        <h4>John Xtrem</h4>
                        <p class="mb-0">johnxtrem@example.com</p>
                        <div class="d-flex justify-content-center doc-social mt-2">
                            <a href="#"><i class="las la-star text-warning"></i></a>
                            <a href="#"><i class="las la-star text-warning"></i></a>
                            <a href="#"><i class="las la-star text-warning"></i></a>
                            <a href="#"><i class="las la-star text-warning"></i></a>
                        </div>
                        <b-row class=" mt-4">
                            <b-col sm="4">
                                <div class="op-count text-center bg-danger-light">
                                <div class="h-100">
                                    <h3 class="text-danger">530</h3>
                                    <p class="mb-0">Liver</p>
                                </div>
                            </div>
                            </b-col>
                            
                            <b-col sm="4" class=" mt-3 mt-sm-0">
                                <div class="op-count text-center bg-success-light">
                                    <div class="h-100">
                                        <h3 class="text-success">450</h3>
                                        <p class="mb-0">Brain</p>
                                    </div>
                                </div>
                             </b-col>
                            
                            <b-col sm="4" class=" mt-3 mt-sm-0">
                                <div class="op-count text-center bg-primary-light">
                                    <div class="h-100">
                                        <h3 class="text-primary">210</h3>
                                        <p class="mb-0">Kidney</p>
                                    </div>
                                </div>
                            </b-col>
                            
                        </b-row>
                   </template>
                </card>
            </b-col>
            <!-- Page end  -->
        </b-row>
        <b-row>
            <b-col lg="4">
                <card class=" bg-success-light" bodyClass="p-0">
                     <template v-slot:body>
                       <b-row>
                            <div class="col-4">
                                <div class="bg-success h-100 rounded">
                                    <div class="ratting-icons">
                                        <i class="far fa-smile"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="col-8 pt-3 pb-3">
                                <h6>Positive Reviews</h6>
                                <div class="d-flex align-items-center">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                </div>
                                <p class="mb-0">4.5 / 5</p>
                            </div>
                        </b-row>
                     </template>
                </card>
                <card class="  bg-danger-light" bodyClass="p-0">
                     <template v-slot:body>
                        <b-row>
                            <div class="col-4">
                                <div class="bg-danger h-100 rounded">
                                    <div class="ratting-icons">
                                        <i class="far fa-frown"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="col-8 pt-3 pb-3">
                                <h6>Negative Reviews</h6>
                                <div class="d-flex align-items-center">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="lar la-star text-warning"></i></a>
                                    <a href="#"><i class="lar la-star text-warning"></i></a>
                                </div>
                                <p class="mb-0">4.5 / 5</p>
                            </div>
                        </b-row>
                    </template>
                </card>
                <card class="  bg-primary-light" bodyClass=" p-0">
                    <template v-slot:body>
                        <b-row>
                            <div class="col-4">
                                <div class="bg-primary h-100 rounded">
                                    <div class="ratting-icons">
                                        <i class="far fa-meh"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="col-8 pt-3 pb-3">
                                <h6>Average Reviews</h6>
                                <div class="d-flex align-items-center">
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star text-warning"></i></a>
                                    <a href="#"><i class="las la-star-half-alt text-warning"></i></a>
                                    <a href="#"><i class="lar la-star text-warning"></i></a>
                                </div>
                                <p class="mb-0">4.5 / 5</p>
                            </div>
                        </b-row>
                     </template>
                </card>
             </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height" bodyClass="text-center">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Appointment Survey</h4>
                       </template>
                   <template v-slot:body>
                        <ApexChart element="hospital-chart-05" :chartOption="chart4"/>
                     </template>
                </card>
             </b-col>
             <b-col lg="4">
                <card class=" card-block card-stretch card-height" bodyClass="text-center inln-date">
                     <template v-slot:body>
                        <flat-pickr :config="config" id="inline-date" value="" class="date-input basicFlatpickr d-none" readonly="readonly"/>
                    </template>
                </card>
             </b-col>
          
        </b-row>
        <b-row>
            <b-col lg="12">
                <card class="  card-block card-stretch card-height" bodyClass="rec-pat">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Recent Patient</h4>
                       </template>
                        <template v-slot:headerAction>
                            <button class="btn btn-outline-primary">View All</button>
                       </template>
                    <template v-slot:body>
                        <div class="table-responsive">
                            <table class="table data-table table-striped table-bordered mb-0">
                                <thead>
                                    <th>Name</th>
                                    <th>Date</th>
                                    <th>Age</th>
                                    <th>Diseases</th>
                                    <th>Doctor</th>
                                    <th>Progress</th>
                                    <th>Report</th>
                                    <th>Status</th>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <img src="../../../assets/images/user/08.jpg"
                                                    class="img-fluid avatar-35 rounded" alt="image">
                                                <div class="media-body ml-3">
                                                    <p class="mb-0">William Smith</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>20/8/2020
                                        </td>
                                        <td>
                                            25 yrs
                                        </td>
                                        <td>
                                            Nimonia
                                        </td>
                                        <td>
                                            Dr. Smith
                                        </td>
                                        <td>
                                            <div class="iq-progress-bar-linear d-inline-block w-80">
                                                 <Progressbar :value="55" color="primary"/>
                                            </div>
                                        </td>
                                        <td>
                                            <img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image">
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Admit</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <img src="../../../assets/images/user/03.jpg"
                                                    class="img-fluid avatar-35 rounded" alt="image">
                                                <div class="media-body ml-3">
                                                    <p class="mb-0">Melina Martin</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>12/9/2020
                                        </td>
                                        <td>
                                            32 yrs
                                        </td>
                                        <td>
                                            Thyphod
                                        </td>
                                        <td>
                                            Dr. John
                                        </td>
                                        <td>
                                            <div class="iq-progress-bar-linear d-inline-block w-80">
                                                 <Progressbar :value="55" color="primary"/>
                                            </div>
                                        </td>
                                        <td>
                                            <img src="../../../assets/images/icon/pdf.png" class="img-fliud">
                                        </td>
                                        <td>
                                            <span class="badge badge-danger">Discharge</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <img src="../../../assets/images/user/02.jpg"
                                                    class="img-fluid avatar-35 rounded" alt="image">
                                                <div class="media-body ml-3">
                                                    <p class="mb-0">Pete Sariya</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>15/08/2020
                                        </td>
                                        <td>
                                            35 yrs
                                        </td>
                                        <td>
                                            Paige
                                        </td>
                                        <td>
                                            Dr. Greta
                                        </td>
                                        <td>
                                            <div class="iq-progress-bar-linear d-inline-block w-80">
                                                 <Progressbar :value="90" color="primary"/>
                                            </div>
                                        </td>
                                        <td>
                                            <img src="../../../assets/images/icon/pdf.png" class="img-fliud">
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Admit</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <img src="../../../assets/images/user/07.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                                <div class="media-body ml-3">
                                                    <p class="mb-0">Alindro Smith</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>18/8/2020
                                        </td>
                                        <td>
                                            48 yrs
                                        </td>
                                        <td>
                                            Malaria
                                        </td>
                                        <td>
                                            Dr. Julia
                                        </td>
                                        <td>
                                            <div class="iq-progress-bar-linear d-inline-block w-80">
                                                 <Progressbar :value="90" color="primary"/>
                                            </div>
                                        </td>
                                        <td>
                                            <img src="../../../assets/images/icon/pdf.png" class="img-fliud">
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Admit</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            <div class="media align-items-center">
                                                <img src="../../../assets/images/user/01.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                                <div class="media-body ml-3">
                                                    <p class="mb-0">Kusti Franti</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td>25/09/2020
                                        </td>
                                        <td>
                                            56 yrs
                                        </td>
                                        <td>
                                            Malaria
                                        </td>
                                        <td>
                                            Dr. Molive
                                        </td>
                                        <td>
                                            <div class="iq-progress-bar-linear d-inline-block w-80">
                                                <Progressbar :value="70" color="primary"/>
                                            </div>
                                        </td>
                                        <td>
                                            <img src="../../../assets/images/icon/pdf.png" class="img-fliud">
                                        </td>
                                        <td>
                                            <span class="badge badge-success">Admit</span>
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
import { english } from 'flatpickr/dist/l10n/default'
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
    core.fullscreen()
    core.index()
    
  },
  data () {
    return{
      config: {
        dateFormat: 'Y-m-d',
        inline: true,
        locale: english
      },
      item:{
         type:"donut",
         id:"hospital-chart-02",
         colors: ["#FF4B4B", "#37E6B0", "#4788FF", "#FE721C", "#1B223F"],
         resize: !0,
         hideHover: "auto",
         bodyData: [{
                    label: "New Patient",
                    value: 40
                }, {
                    label: "Exit Patient",
                    value: 12
                }, {
                    label: "ICU Patient",
                    value: 20
                }, {
                    label: "Discharge Patient",
                    value: 33
                }, {
                    label: "OPD Patient",
                    value: 5
                }
         ],
          
      },
      chart2:{
          series: [{
      name: 'Operation',
      data: [44, 25, 10, 60, 50, 25, 40, 20]
    }, {
      name: 'Visitors',
      data: [25, 38, 70, 0, 30, 15, 30, 30]
    }],
    colors: ['#4788ff', '#e8f0ff'],
    chart: {
      type: 'bar',
      height: 340,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    responsive: [{
      breakpoint: 580,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -30,
          offsetY: 0,
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
      },
    },
    xaxis: {
      type: 'category',
      categories: ['India', 'Canada', 'U.S.A', 'Africa', 'London ', 'Europe ','Dubai','Kuvet'],
    },
     yaxis: {
      labels: {
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
        }
     },
    legend: {
      position: 'top',
      offsetX: -35
    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
      },
      chart3:{
          series: [{
      name: 'Success',
      data: [110, 85, 87, 40, 45, 20, 91, 45, 94, 88]
    }, {
      name: 'Failed',
      data: [20, 55, 35, 30, 25, 80, 63, 45, 66, 115]
    }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#37E6B0'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '85%',
      },
    },
    legend: {
      position: 'top',
      offsetX: -35
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
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
      },
      labels: {
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
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
      chart4:{
          series: [22, 83, 10, 30],
    colors: ['#876CFE', '#4788FF', '#C33030', '#FE721C'],
    chart: {
      height: 250,
      type: 'pie',
    },
    legend: {
      position: 'bottom',
      offsetX: 0
    },
    labels: ['Cancelled', 'Completed', 'Pending', 'Upcoming'],
      },
    }
  }
}
</script>
