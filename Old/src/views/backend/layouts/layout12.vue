<template>
  <div>
    <div class="bg-nav-horizontal mt-0">
        <div class="main-scroll">
            <tab-nav :pills="true "  id="myTab-1" extraclass="nav-tabs h-tabs" role="tablist">
                 <tab-nav-items :active="true" id="layout1-tab" ariaControls="layout1" dataToggle="tab" role="tab" :ariaSelected="true" title="Layout 1" />
                 <tab-nav-items :active="false" id="layout2-tab"  ariaControls="layout2" role="tab" dataToggle="tab" :ariaSelected="false" title="Layout 2" />
                 <tab-nav-items :active="false" id="layout3-tab"  ariaControls="layout3" role="tab" dataToggle="tab" :ariaSelected="false" title="Layout 3" />
                 <tab-nav-items :active="false" id="layout4-tab"  ariaControls="layout4" role="tab" dataToggle="tab" :ariaSelected="false" title="Layout 4" />
                 <tab-nav-items :active="false" id="layout5-tab"  ariaControls="layout5" role="tab" dataToggle="tab" :ariaSelected="false" title="Layout 5" />
            </tab-nav>
        </div>
    </div>
   
        <tab-content id="myTabContent-2">
            <tab-content-item :active="true" id="layout1" aria-labelled-by="layout1-tab" role="tabpanel" >
            <div class="container-fluid">
                <b-row >
                    <b-col xl="3" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height-half" bodyClass="res-block">
                             <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <div class="bg-warning-light icon iq-icon-box mr-2 rounded">
                                        <svg width="32" height="26" viewBox="0 0 32 26" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M9.6 12.8C12.695 12.8 15.2 10.295 15.2 7.20001C15.2 4.10501 12.695 1.60001 9.6 1.60001C6.505 1.60001 4 4.10501 4 7.20001C4 10.295 6.505 12.8 9.6 12.8ZM13.44 14.4H13.025C11.985 14.9 10.83 15.2 9.6 15.2C8.37 15.2 7.22 14.9 6.175 14.4H5.76C2.58 14.4 0 16.98 0 20.16V21.6C0 22.925 1.075 24 2.4 24H16.8C18.125 24 19.2 22.925 19.2 21.6V20.16C19.2 16.98 16.62 14.4 13.44 14.4ZM24 12.8C26.65 12.8 28.8 10.65 28.8 8.00001C28.8 5.35001 26.65 3.20001 24 3.20001C21.35 3.20001 19.2 5.35001 19.2 8.00001C19.2 10.65 21.35 12.8 24 12.8ZM26.4 14.4H26.21C25.515 14.64 24.78 14.8 24 14.8C23.22 14.8 22.485 14.64 21.79 14.4H21.6C20.58 14.4 19.64 14.695 18.815 15.17C20.035 16.485 20.8 18.23 20.8 20.16V22.08C20.8 22.19 20.775 22.295 20.77 22.4H29.6C30.925 22.4 32 21.325 32 20C32 16.905 29.495 14.4 26.4 14.4Z"
                                                fill="#FE721C" />
                                        </svg>
                                    </div>
                                    <div class="media-support-info ml-3">
                                        <h5 class="text-warning">1334</h5>
                                        <p class="mb-0">Client’s</p>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                        <div class="progress-round income-progress salon2-progress-warning mx-auto"
                                            data-value="46">
                                            <span class="progress-left">
                                                <span class="progress-bar border-white"
                                                    style="transform: rotate(0deg);"></span>
                                            </span>
                                            <span class="progress-right">
                                                <span class="progress-bar border-warning"
                                                    style="transform: rotate(150deg);"></span>
                                            </span>
                                            <div
                                                class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center text-center">
                                                <div class="h4 mb-0">46</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                             </template>
                        </card>
                        <card class=" card-block card-stretch card-height-half" bodyClass="res-block">
                            <template v-slot:body>
                                <div class="d-flex align-items-center">
                                    <div class="bg-info-light icon iq-icon-box mr-2 rounded">
                                        <svg width="40" height="32" viewBox="0 0 40 32" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M38.1562 21.3313C38.3187 20.45 38.3187 19.55 38.1562 18.6688L39.7687 17.7375C39.9562 17.6313 40.0375 17.4125 39.975 17.2063C39.5562 15.8563 38.8375 14.6313 37.9 13.6188C37.7563 13.4625 37.525 13.425 37.3375 13.5313L35.725 14.4625C35.0437 13.8813 34.2625 13.4313 33.4188 13.1313V11.2688C33.4188 11.0563 33.2687 10.8688 33.0625 10.825C31.6688 10.5125 30.25 10.525 28.925 10.825C28.7188 10.8688 28.5688 11.0563 28.5688 11.2688V13.1313C27.725 13.4313 26.9438 13.8813 26.2625 14.4625L24.65 13.5313C24.4688 13.425 24.2312 13.4625 24.0875 13.6188C23.15 14.6313 22.4313 15.8563 22.0125 17.2063C21.95 17.4125 22.0375 17.6313 22.2188 17.7375L23.8312 18.6688C23.6687 19.55 23.6687 20.45 23.8312 21.3313L22.2188 22.2625C22.0312 22.3688 21.95 22.5875 22.0125 22.7938C22.4313 24.1438 23.15 25.3625 24.0875 26.3813C24.2312 26.5375 24.4625 26.575 24.65 26.4688L26.2625 25.5375C26.9438 26.1188 27.725 26.5688 28.5688 26.8688V28.7313C28.5688 28.9438 28.7188 29.1313 28.925 29.175C30.3187 29.4875 31.7375 29.475 33.0625 29.175C33.2687 29.1313 33.4188 28.9438 33.4188 28.7313V26.8688C34.2625 26.5688 35.0437 26.1188 35.725 25.5375L37.3375 26.4688C37.5188 26.575 37.7563 26.5375 37.9 26.3813C38.8375 25.3688 39.5562 24.1438 39.975 22.7938C40.0375 22.5875 39.95 22.3688 39.7687 22.2625L38.1562 21.3313ZM31 23.0313C29.325 23.0313 27.9688 21.6688 27.9688 20C27.9688 18.3313 29.3312 16.9688 31 16.9688C32.6688 16.9688 34.0312 18.3313 34.0312 20C34.0312 21.6688 32.675 23.0313 31 23.0313ZM6 14C8.20625 14 10 12.2063 10 10C10 7.79376 8.20625 6.00001 6 6.00001C3.79375 6.00001 2 7.79376 2 10C2 12.2063 3.79375 14 6 14ZM20 16C20.1187 16 20.2313 15.9688 20.35 15.9625C20.8687 14.6063 21.6313 13.3313 22.6187 12.2625C23.0812 11.7625 23.7375 11.475 24.425 11.475C24.8562 11.475 25.2812 11.5875 25.65 11.8063L26.1437 12.0938C26.1937 12.0625 26.2438 12.0375 26.2938 12.0063C26.7313 11.0938 26.9937 10.0813 26.9937 9.00626C26.9937 5.13751 23.8625 2.00626 19.9937 2.00626C16.125 2.00626 13 5.13126 13 9.00001C13 12.8688 16.1313 16 20 16ZM26.575 28.1563C26.4313 28.0813 26.2875 27.9938 26.15 27.9125C25.6375 28.2125 25.1938 28.525 24.4312 28.525C23.75 28.525 23.0938 28.2375 22.625 27.7375C21.4813 26.5 20.6062 24.9938 20.1125 23.3875C19.4437 21.2313 21.6688 20.2813 21.725 20.2438C21.7188 20.0813 21.7188 19.9188 21.725 19.7563L21.2313 19.4688C20.9938 19.3313 20.7937 19.1563 20.6187 18.9625C20.4125 18.975 20.2125 19 20.0063 19C18.4688 19 17.0312 18.625 15.725 18H15.2063C11.225 18 8 21.225 8 25.2V27C8 28.6563 9.34375 30 11 30H26.9625C26.7312 29.625 26.575 29.2 26.575 28.7313V28.1563ZM10.8188 17.1625C10.0938 16.4438 9.1 16 8 16H4C1.79375 16 0 17.7938 0 20V22C0 23.1063 0.89375 24 2 24H6.11875C6.5125 21.0375 8.3 18.5438 10.8188 17.1625Z"
                                                fill="#876CFE" />
                                        </svg>
                                    </div>
                                    <div class="media-support-info ml-3">
                                        <h5 class="text-info">200</h5>
                                        <p class="mb-0">Total Staff</p>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                         <ApexChart element="salon2-chart-01" :chartOption="chart17" />
                                       
                                    </div>
                                </div>
                            </template>
                        </card>
                    </b-col>
                    <b-col xl="9" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height salon-2-back" :style="`background: url(${require('@/assets/images/layouts/layout-12/11.png')}) no-repeat; background-size: cover;`">
                             <template v-slot:body>
                                <div class="row">
                                    <div class="col-lg-7">
                                        <div class="mt-4 mb-4">
                                            <h4>Good Morning</h4>
                                            <h1 class="mt-5">Mr. John Doe</h1>
                                            <h5 class="mt-3">27 October 2020 - 10:00 AM</h5>
                                        </div>
                                    </div>
                                    <div class="col-lg-5">
                                        
                                    </div>
                                </div>
                             </template>
                        </card>
                    </b-col>
                     <b-col xl="3" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height" bodyClass="res-block">
                             <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="d-flex align-items-center">
                                        <div class="bg-primary-light icon iq-icon-box mr-2 rounded">
                                            <svg width="28" height="32" viewBox="0 0 28 32" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <g clip-path="url(#clip0)">
                                                    <path
                                                        d="M27.25 10H0.75C0.335812 10 0 9.66419 0 9.25V7C0 5.34312 1.34312 4 3 4H6V0.75C6 0.335813 6.33581 0 6.75 0H9.25C9.66419 0 10 0.335813 10 0.75V4H18V0.75C18 0.335813 18.3358 0 18.75 0H21.25C21.6642 0 22 0.335813 22 0.75V4H25C26.6569 4 28 5.34312 28 7V9.25C28 9.66419 27.6642 10 27.25 10ZM0.75 12H27.25C27.6642 12 28 12.3358 28 12.75V29C28 30.6569 26.6569 32 25 32H3C1.34312 32 0 30.6569 0 29V12.75C0 12.3358 0.335812 12 0.75 12ZM21.581 17.9967L19.8204 16.2218C19.5287 15.9278 19.0539 15.9258 18.7598 16.2176L12.1325 22.7916L9.25875 19.8946C8.96706 19.6005 8.49212 19.5986 8.19806 19.8903L6.42325 21.6509C6.12919 21.9426 6.12725 22.4175 6.419 22.7116L11.5816 27.9159C11.8732 28.2099 12.3481 28.2119 12.6422 27.9201L21.5767 19.0573C21.8708 18.7656 21.8727 18.2907 21.581 17.9967Z"
                                                        fill="#4788ff" />
                                                </g>
                                                <defs>
                                                    <clipPath id="clip0">
                                                        <rect width="28" height="32" fill="white" />
                                                    </clipPath>
                                                </defs>
                                            </svg>
                                        </div>
                                        <div class="media-support-primary salon-2 ml-3">
                                            <h5 class="text-primary">1000</h5>
                                            <p class="mb-0">Event</p>
                                        </div>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                         <ApexChart element="salon2-chart-02" :chartOption="chart18" />
                                        
                                    </div>
                                </div>
                             </template>
                        </card>
                     </b-col>
                    <b-col xl="3" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height" bodyClass="res-block">
                             <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="d-flex align-items-center">
                                        <div class="bg-danger-light icon iq-icon-box mr-2 rounded">
                                            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <g clip-path="url(#clip0)">
                                                    <path
                                                        d="M22 6C22 2.68625 19.3137 0 16 0C12.6862 0 10 2.68625 10 6C10 9.31375 12.6862 12 16 12C19.3137 12 22 9.31375 22 6ZM14.5994 15.0688C10.8912 12.7987 4.885 12.175 1.8625 12.0031C0.846875 11.9456 0 12.7194 0 13.6962V27.6213C0 28.5169 0.724375 29.2638 1.65562 29.3119C4.38438 29.455 9.905 29.9794 13.7206 31.9013C14.3062 32.1963 15.0006 31.7944 15.0006 31.1594V15.785C15 15.4931 14.8556 15.2256 14.5994 15.0688ZM30.1375 12.0031C27.1156 12.1744 21.1088 12.7987 17.4013 15.0688C17.145 15.2256 17.0006 15.5037 17.0006 15.7956V31.1575C17.0006 31.7944 17.6969 32.1969 18.2844 31.9013C22.0994 29.9813 27.6169 29.4569 30.345 29.3137C31.2762 29.265 32.0006 28.5181 32.0006 27.6225V13.6962C32 12.7194 31.1531 11.9456 30.1375 12.0031Z"
                                                        fill="#FF4B4B" />
                                                </g>
                                                <defs>
                                                    <clipPath id="clip1">
                                                        <rect width="32" height="32" fill="white" />
                                                    </clipPath>
                                                </defs>
                                            </svg>
                                        </div>
                                        <div class="media-support-danger salon-2 ml-3 flex-1">
                                            <h5 class="text-danger">1000</h5>
                                            <p class="mb-0">Enquries</p>
                                        </div>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                        <div class="progress-round income-progress salon2-progress-danger mx-auto"
                                            data-value="46">
                                            <span class="progress-left">
                                                <span class="progress-bar border-white"
                                                    style="transform: rotate(0deg);"></span>
                                            </span>
                                            <span class="progress-right">
                                                <span class="progress-bar border-danger"
                                                    style="transform: rotate(150deg);"></span>
                                            </span>
                                            <div
                                                class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center text-center">
                                                <div class="h4 mb-0">46</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                             </template>
                        </card>
                    </b-col>
                    <b-col xl="3" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height" bodyClass="res-block">
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="d-flex align-items-center">
                                        <div class="bg-success-light icon iq-icon-box mr-2 rounded">
                                            <svg width="24" height="32" viewBox="0 0 24 32" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <path
                                                    d="M23.5625 6.5625L17.4438 0.4375C17.1625 0.15625 16.7812 0 16.3813 0H16V8H24V7.61875C24 7.225 23.8438 6.84375 23.5625 6.5625ZM14 8.5V0H1.5C0.66875 0 0 0.66875 0 1.5V30.5C0 31.3312 0.66875 32 1.5 32H22.5C23.3312 32 24 31.3312 24 30.5V10H15.5C14.675 10 14 9.325 14 8.5ZM4 4.5C4 4.22375 4.22375 4 4.5 4H9.5C9.77625 4 10 4.22375 10 4.5V5.5C10 5.77625 9.77625 6 9.5 6H4.5C4.22375 6 4 5.77625 4 5.5V4.5ZM4 9.5V8.5C4 8.22375 4.22375 8 4.5 8H9.5C9.77625 8 10 8.22375 10 8.5V9.5C10 9.77625 9.77625 10 9.5 10H4.5C4.22375 10 4 9.77625 4 9.5ZM13 25.9925V27.5C13 27.7763 12.7762 28 12.5 28H11.5C11.2238 28 11 27.7763 11 27.5V25.9819C10.2944 25.9456 9.60813 25.6994 9.03938 25.2725C8.79563 25.0894 8.78312 24.7244 9.00375 24.5138L9.73812 23.8131C9.91125 23.6481 10.1687 23.6406 10.3713 23.7675C10.6131 23.9188 10.8875 24 11.1725 24H12.9294C13.3356 24 13.6669 23.63 13.6669 23.1756C13.6669 22.8037 13.4412 22.4762 13.1187 22.38L10.3062 21.5362C9.14437 21.1875 8.3325 20.0725 8.3325 18.8244C8.3325 17.2919 9.52313 16.0469 10.9994 16.0075V14.5C10.9994 14.2238 11.2231 14 11.4994 14H12.4994C12.7756 14 12.9994 14.2238 12.9994 14.5V16.0181C13.705 16.0544 14.3912 16.3 14.96 16.7275C15.2037 16.9106 15.2162 17.2756 14.9956 17.4862L14.2612 18.1869C14.0881 18.3519 13.8306 18.3594 13.6281 18.2325C13.3863 18.0806 13.1119 18 12.8269 18H11.07C10.6637 18 10.3325 18.37 10.3325 18.8244C10.3325 19.1963 10.5581 19.5238 10.8806 19.62L13.6931 20.4638C14.855 20.8125 15.6669 21.9275 15.6669 23.1756C15.6669 24.7087 14.4762 25.9531 13 25.9925Z"
                                                    fill="#37E6B0" />
                                            </svg>
                                        </div>
                                        <div class="media-support-success salon-2 ml-3">
                                            <h5 class="text-success">150</h5>
                                            <p class="mb-0">Profit</p>
                                        </div>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                        <ApexChart element="salon2-chart-03" classname="chart-salon" :chartOption="chart19" />
                                      
                                    </div>
                                </div>
                            </template>
                        </card>
                    </b-col>
                     <b-col xl="3" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height" bodyClass="res-block">
                             <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                    <div class="d-flex align-items-center">
                                        <div class="bg-info-light icon iq-icon-box mr-2 rounded">
                                            <svg width="32" height="26" viewBox="0 0 32 26" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <path
                                                    d="M4.8 11.2C6.565 11.2 8 9.76501 8 8.00001C8 6.23501 6.565 4.80001 4.8 4.80001C3.035 4.80001 1.6 6.23501 1.6 8.00001C1.6 9.76501 3.035 11.2 4.8 11.2ZM27.2 11.2C28.965 11.2 30.4 9.76501 30.4 8.00001C30.4 6.23501 28.965 4.80001 27.2 4.80001C25.435 4.80001 24 6.23501 24 8.00001C24 9.76501 25.435 11.2 27.2 11.2ZM28.8 12.8H25.6C24.72 12.8 23.925 13.155 23.345 13.73C25.36 14.835 26.79 16.83 27.1 19.2H30.4C31.285 19.2 32 18.485 32 17.6V16C32 14.235 30.565 12.8 28.8 12.8ZM16 12.8C19.095 12.8 21.6 10.295 21.6 7.20001C21.6 4.10501 19.095 1.60001 16 1.60001C12.905 1.60001 10.4 4.10501 10.4 7.20001C10.4 10.295 12.905 12.8 16 12.8ZM19.84 14.4H19.425C18.385 14.9 17.23 15.2 16 15.2C14.77 15.2 13.62 14.9 12.575 14.4H12.16C8.98 14.4 6.4 16.98 6.4 20.16V21.6C6.4 22.925 7.475 24 8.8 24H23.2C24.525 24 25.6 22.925 25.6 21.6V20.16C25.6 16.98 23.02 14.4 19.84 14.4ZM8.655 13.73C8.075 13.155 7.28 12.8 6.4 12.8H3.2C1.435 12.8 0 14.235 0 16V17.6C0 18.485 0.715 19.2 1.6 19.2H4.895C5.21 16.83 6.64 14.835 8.655 13.73Z"
                                                    fill="#876cfe" />
                                            </svg>
                                        </div>
                                        <div class="media-support-info salon-2 ml-3">
                                            <h5 class="text-info">1000</h5>
                                            <p class="mb-0">Visitor’s</p>
                                        </div>
                                    </div>
                                    <div class="media-support-amount ml-3">
                                         <ApexChart element="salon2-chart-04"  classname="chart-salon" :chartOption="chart20" />
                                     
                                    </div>
                                </div>
                             </template>
                        </card>
                     </b-col>
                    <b-col xl="6" lg="6" md="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:headerTitle>
                                    <h4 class="card-title">Experts</h4>
                             </template>
                                <div id="trending-order-slick-arrow" class="slick-aerrow-block">                                
                                </div>
                            
                          <template v-slot:body>
                                <Slick  :option="option2" classname="salone-styles">
                              
                                    <div class="item">
                                        <div class="rounded-circle avatar-120 bg-white odr-img">
                                            <img src="../../../assets/images/layouts/layout-12/02.png" class="img-fluid m-auto" alt="image">
                                        </div>
                                        
                                        <div class="odr-content bg-danger-light">                                            
                                            <h5>Ira Membrit</h5>
                                            <p class="mt-2">Hair Cut</p>
                                            <ul class="list-unstyled  mt-2 mb-0">
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-facebook-f text-primary"></i></a>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-twitter text-info"></i></a></li>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"> <i
                                                            class="lab la-instagram  text-danger"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="rounded-circle avatar-120 bg-white odr-img">
                                            <img src="../../../assets/images/layouts/layout-12/03.png" class="img-fluid m-auto" alt="image">
                                        </div>
                                        <div class="odr-content bg-info-light">                                            
                                            <h5>Malinda</h5>
                                            <p class="mt-2">Hair Spa</p>
                                            <ul class="list-unstyled  mt-2 mb-0">
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-facebook-f text-primary"></i></a>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-twitter text-info"></i></a></li>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"> <i
                                                            class="lab la-instagram  text-danger"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="item">
                                        <div class="rounded-circle avatar-120 bg-white odr-img">
                                            <img src="../../../assets/images/layouts/layout-12/04.png" class="img-fluid m-auto" alt="image">
                                        </div>
                                        <div class="odr-content bg-primary-light">                                            
                                            <h5>Maya Didas</h5>
                                            <p class="mt-2">Makeup</p>
                                            <ul class="list-unstyled mt-2 mb-0">
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-facebook-f text-primary"></i></a>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"><i
                                                            class="lab la-twitter text-info"></i></a></li>
                                                <li class="bg-white rounded-small iq-card-icon-small mr-3"><a href="javascript:void(0);"> <i
                                                            class="lab la-instagram  text-danger"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                               
                                </Slick>
                          </template>
                        </card>
                    </b-col>
                    <b-col xl="3" lg="6" md="6">
                        <card class=" card-block card-stretch card-height-half bg-success rounded">
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                     <ApexChart element="salon2-chart-09"   :chartOption="chart21" />
                                    
                                    <div class="pl-3">
                                        <h2 class="text-white">500</h2>
                                        <p class="mb-0">Cancellation</p>
                                    </div>
                                </div>
                            </template>
                        </card>
                        <card class=" card-block card-stretch card-height-half">
                            <template v-slot:body>
                                <div class="d-flex align-items-center justify-content-between">
                                     <ApexChart element="salon2-chart-10"   :chartOption="chart22" />
                                   
                                    <div class="pl-3">
                                        <h2>2,456</h2>
                                        <p class="mb-0">Enquiry</p>
                                    </div>
                                </div>
                            </template>
                        </card>
                    </b-col>
                     <b-col xl="3" lg="6" md="6">
                        <card class=" card-block card-stretch card-height">
                          <template v-slot:headerTitle>
                                    <h4 class="card-title">By Gender</h4>
                          </template>
                            <template v-slot:body>
                                 <MorrisChart :element="item1.id" :type="item1.type" :data="item1.bodyData" :colors="item1.colors" style="min-height: 250px"/>
                                  
                            </template>
                        </card>
                   </b-col>
                   <b-col xl="3" lg="6" md="6">
                        <card class=" card-block card-stretch card-height">
                           <template v-slot:headerTitle>
                                    <h4 class="card-title">Growth</h4>
                           </template>
                           <template v-slot:body>
                                <ApexChart element="salon2-chart-05"   :chartOption="chart24" /> 
                                
                           </template>
                        </card>
                   </b-col>
                   <b-col xl="3" lg="6" md="6">
                        <card class=" card-block card-stretch card-height">
                            <template v-slot:headerTitle>
                                    <h4 class="card-title">Upcoming Events</h4>
                            </template>
                            <template v-slot:body>
                                <ul class="perfomer-lists m-0 p-0">
                                    <li class="d-flex mb-3 ">
                                        <div class="top-block-one d-flex align-items-center justify-content-between">
                                            <div
                                                class="icon iq-icon-box event-icon bg-primary-light rounded-small font-size-18">
                                                <div class="date">23</div>
                                                <div class="month">Oct</div>
                                            </div>
                                        </div>
                                        <div class="media-support-info ml-3">
                                            <h5>Hugh Briss</h5>
                                            <p class="mb-0">Makeup</p>
                                            <span>08:30AM to 09:00AM</span>
                                        </div>
                                        <div class="iq-card-header-toolbar d-flex">
                                            <h5 class="mb-0"><b>$25</b></h5>
                                        </div>
                                    </li>
                                    <li class="d-flex mb-3 align-items-center border-top pt-3">
                                        <div class="top-block-one d-flex align-items-center justify-content-between">
                                            <div
                                                class="icon iq-icon-box event-icon bg-danger-light rounded-small font-size-18">
                                                <div class="date">24</div>
                                                <div class="month">Oct</div>
                                            </div>
                                        </div>
                                        <div class="media-support-info ml-3">
                                            <h5>Claire Voyant</h5>
                                            <p class="mb-0">Hair Spa</p>
                                            <span>09:00AM to 09:30AM</span>
                                        </div>
                                        <div class="iq-card-header-toolbar d-flex ">
                                            <h4><b>$50</b></h4>
                                        </div>
                                    </li>
                                    <li class="d-flex align-items-center border-top pt-3">
                                        <div class="top-block-one d-flex align-items-center justify-content-between">
                                            <div
                                                class="icon iq-icon-box event-icon bg-warning-light rounded-small font-size-18">
                                                <div class="date">25</div>
                                                <div class="month">Oct</div>
                                            </div>
                                        </div>
                                        <div class="media-support-info ml-3">
                                            <h5>Marcus Down</h5>
                                            <p class="mb-0"> Body Spa</p>
                                            <span>09:30AM to 10:00AM</span>
                                        </div>
                                        <div class="iq-card-header-toolbar">
                                            <h4><b>$78</b></h4>
                                        </div>
                                    </li>
                                </ul>
                            </template>
                        </card>
                    </b-col>
                    
                    <div class="col-xl-6 col-lg-6 col-md-6">
                        <div class="card card-block card-stretch card-height">
                            <div class="card-header d-flex justify-content-between">
                                <div class="header-title">
                                    <h4 class="card-title">Category Growth</h4>
                                </div>
                                <div class="card-header-toolbar d-flex align-items-center">
                                    <div class="dropdown">
                                        <span class="dropdown-toggle dropdown-bg bg-success rounded p-2"
                                            id="dropdownMenuButton1" data-toggle="dropdown">
                                            Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                                        </span>
                                        <div class="dropdown-menu dropdown-menu-right shadow-none"
                                            aria-labelledby="dropdownMenuButton1">
                                            <a class="dropdown-item" href="#"><i
                                                    class="ri-delete-bin-6-fill mr-2"></i>Delete</a>
                                            <a class="dropdown-item" href="#"><i class="ri-pencil-fill mr-2"></i>Edit</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                 <ApexChart element="salon2-chart-06"   :chartOption="chart23" />
                                
                            </div>
                        </div>
                    </div>
                    
                   
                    <div class="col-xl-9 col-lg-6 col-md-6">
                        <div class="card card-block card-stretch card-height">
                            <div class="card-header d-flex justify-content-between">
                                <div class="header-title">
                                    <h4 class="card-title">Recent Customer</h4>
                                </div>
                                <div class="card-header-toolbar d-flex align-items-center">
                                    <button class="btn btn-sm btn-success">View All</button>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table data-table mb-0 table-borderless">
                                        <thead>
                                            <tr>
                                                <th scope="col">Name</th>
                                                <th scope="col">Date</th>
                                                <th scope="col">Gender</th>
                                                <th scope="col">Service</th>
                                                <th scope="col">Expert</th>
                                                <th scope="col">Code</th>
                                                <th scope="col">Number</th>
                                                <th scope="col">Price</th>
                                                <th scope="col">Status</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>
                                                    <div class="media align-items-center">
                                                        <a href="javascript:void(0);"><img
                                                                src="../../../assets/images/user/01.jpg"
                                                                class="img-fluid avatar-40 rounded-normal" alt="image"></a>
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
                                                    <span>Smith Jackson</span>
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
                                                    <span class="badge bg-danger">Confirmed</span>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <div class="media align-items-center">
                                                        <a href="javascript:void(0);"><img
                                                                src="../../../assets/images/user/02.jpg"
                                                                class="img-fluid avatar-40 rounded-normal" alt="image"></a>
                                                        <div class="media-body ml-3">
                                                            <span>Alena Mathew</span>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <span>02/09/2020</span>
                                                </td>
                                                <td>
                                                    <span>Female</span>
                                                </td>
                                                <td>
                                                    <span>Hair Cut</span>
                                                </td>
                                                <td>
                                                    <span>Smith Jackson</span>
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
                                            </tr>
                                            <tr>
                                                <td>
                                                    <div class="media align-items-center">
                                                        <a href="javascript:void(0);"><img
                                                                src="../../../assets/images/user/03.jpg"
                                                                class="img-fluid avatar-40 rounded-normal" alt="image"></a>
                                                        <div class="media-body ml-3">
                                                            <span>Barry Deo</span>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <span>02/09/2020</span>
                                                </td>
                                                <td>
                                                    <span>Female</span>
                                                </td>
                                                <td>
                                                    <span>Hair Cut</span>
                                                </td>
                                                <td>
                                                    <span>Smith Jackson</span>
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
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-3 col-lg-6 col-md-6">
                        <div class="card card-block card-stretch card-height">
                            <div class="card-body">
                                <div class="d-flex align-items-center mb-4">
                                    <img src="../../../assets/images/user/08.jpg" class="img-fluid avatar-90 rounded-normal"
                                        alt="image">
                                    <div class="d-flex doc-social ml-4">
                                        <a href="#"><i class="lab la-facebook-f text-primary font-size-20"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark font-size-20"></i></a>
                                        <a href="#"><i class="lab la-instagram mr-2 text-danger font-size-20"></i></a>
                                    </div>
                                </div>
                                <h4 class="text-uppercase">Chris P. Bacon</h4>
                                <p class="font-size-16">Top Expert</p>
                                <div class="d-flex align-items-center pt-3">
                                    <span class="bg-warning-light rounded-small iq-card-icon-small mr-3">
                                        <i class="las la-phone-volume"></i>
                                    </span>
                                    <h5>+91 01234 56789</h5>
                                </div>
                                <div class="d-flex align-items-center pt-3">
                                    <span class="bg-success-light rounded-small iq-card-icon-small mr-3">
                                        <i class="las la-envelope"></i>
                                    </span>
                                    <h5>charis@salon.com</h5>
                                </div>
                                <div class="d-flex align-items-center pt-3">
                                    <span class="bg-primary-light rounded-small iq-card-icon-small mr-3">
                                        <i class="lab la-twitter"></i>
                                    </span>
                                    <h5>social@salon.com</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </b-row>
            </div>
            </tab-content-item>
        <tab-content-item :active="false" id="layout2" aria-labelled-by="layout2-tab" role="tabpanel">
          <b-container fluid="">
      <b-row >
            <b-col lg="12" xl="8">
                <b-row>
                  <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-warning-light">
                                      <i class="fas fa-user-friends"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">1334</h3>
                                      <p class="mb-0">Users</p>
                                      <span class="text-danger"><i class="las la-long-arrow-alt-down"></i>10%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                  </b-col>
                   <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-info-light">
                                      <i class="fas fa-dumbbell"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">202</h3>
                                      <p class="mb-0">Trainers</p>
                                      <span class="text-success"><i class="las la-long-arrow-alt-up"></i>50%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                   </b-col>
                  <b-col md="4">
                      <card>
                          <template v-slot:body>
                              <div class="d-flex align-items-center">
                                  <div class="fit-icon rounded text-center bg-success-light">
                                      <i class="fas fa-search-location"></i>
                                  </div>
                                  <div class="iq-card-text pl-4">
                                      <h3 class="line-height">50</h3>
                                      <p class="mb-0">Inquiry</p>
                                      <span class="text-danger"><i class="las la-long-arrow-alt-down"></i>20%</span>
                                  </div>
                              </div>
                          </template>
                      </card>
                  </b-col>
                    <b-col lg="12" >
                        <card class=" card-transparent" bodyClass="p-0">
                             <template v-slot:body>
                                <ApexChart element="fit-progress-chart-01" :chartOption="chart1" />
                             </template>
                        </card>
                    </b-col>

                </b-row>
            </b-col>
            <b-col lg="6" xl="4" >
                <card class=" card-block card-stretch card-height" bodyClass="iq-profile-top pt-0">
                    <template v-slot:cardImage>
                    <img src="../../../assets/images/layouts/layout-3/user-bg.jpg" class="img-fluid rounded" alt="image">
                    </template>
                    <template v-slot:body>
                        <div class=" text-center">
                            <div class="d-inline-block">
                                <img src="../../../assets/images/layouts/layout-3/user-1.jpg"
                                    class="img-fluid d-inline-block avatar-100 mx-auto rounded" alt="image">
                            </div>
                        </div>
                        <b-row class=" align-items-center justify-content-between pt-4">
                            <h3 class="col-7">Jimmy Gorge</h3>
                            <div class="col-5 text-right">
                                <p class="mb-0 badge badge-warning">New York, NY</p>
                            </div>
                            <h5 class="col-6 text-secondary">Sr.Trainer</h5>
                            <div class="col-6">
                                <div class="d-flex doc-social float-right">
                                    <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                    <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                    <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                </div>
                            </div>

                        </b-row>

                        <ul class="list-inline p-0 m-0 mt-4">
                            <li class="d-flex align-items-center justify-content-between mb-3 pb-2 border-bottom">
                                <h6><i class="fas fa-weight text-primary pr-3"></i>Weight</h6>
                                <p class="mb-0">50.2 Kg</p>
                            </li>
                            <li class="d-flex align-items-center justify-content-between mb-3 pb-2 border-bottom">
                                <h6><i class="fas fa-heartbeat text-danger pr-3"></i>Heart Rate</h6>
                                <p class="mb-0">98.2 Bpm</p>
                            </li>
                            <li class="d-flex align-items-center justify-content-between">
                                <h6><i class="fas fa-user text-success pr-3"></i>Age</h6>
                                <p class="mb-0">25 Yrs</p>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4">
                <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                            <h4 class="card-title">Trainers</h4>
                    </template>
                           <template v-slot:headerAction>
                            <span><i class="fas fa-circle text-primary mr-2 font-size-12"></i>Expert Level</span>
                        </template>
                     <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-2.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Julia<span class="text-body pl-2">(personal)</span></h5>
                                        <div class="text-primary"><b>5.8</b></div>
                                    </div>
                                    <p class="mb-0">Fitness</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-3.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Alina<span class="text-body pl-2">(General)</span></h5>
                                        <div class="text-primary"><b>5.6</b></div>
                                    </div>
                                    <p class="mb-0">Aerobics</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-4.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <div class="d-flex align-items-center justify-content-between">
                                        <h5>Julia<span class="text-body pl-2">(General)</span></h5>
                                        <div class="text-primary"><b>5.5</b></div>
                                    </div>
                                    <p class="mb-0">Zumba</p>
                                    <div class="d-flex doc-social mt-2">
                                        <a href="#"><i class="lab la-facebook-f text-primary"></i></a>
                                        <a href="#"><i class="lab la-twitter text-primary-dark"></i></a>
                                        <a href="#"><i class="lab la-google-plus text-danger"></i></a>
                                    </div>
                                </div>
                            </li>
                        </ul>
                     </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4" >
                <card class=" card-block card-stretch card-height" bodyClass="text-center inln-date fitness-datepickr">
                     <template v-slot:body>
                         <flat-pickr :config="config" id="inline-date" value="" class="date-input basicFlatpickr d-none" readonly="readonly"/>
                        <div class="text-primary text-center mt-3"><span class="font-size-18 pr-2">1 / 9 / 2020</span>Lorem
                            ipsum dolor sit amet</div>
                     </template>
                </card>
            </b-col>
            <b-col lg="6" xl="4">
                <b-row>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:body>
                                <i class="fas fa-fire-alt text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Calories</h5>
                                <h2>1259</h2>
                             </template>
                        </card>
                    </b-col>
                     <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                             <template v-slot:body>
                                <i class="fas fa-carrot text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Protiens</h5>
                                <h2>489</h2>
                             </template>
                        </card>
                     </b-col>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height">
                            <template v-slot:body>
                                <i class="fas fa-cookie-bite text-warning font-size-40"></i>
                                <h5 class="text-capitalize mt-3">Carbs</h5>
                                <h2>459</h2>
                            </template>
                        </card>
                    </b-col>
                    <b-col sm="6" >
                        <card class=" card-block card-stretch card-height bg-warning">
                             <template v-slot:body>
                                <i class="fas fa-pizza-slice text-white font-size-40"></i>
                                <h5 class="text-capitalize text-white mt-3">Fat</h5>
                                <h2 class="text-white">259</h2>
                             </template>
                        </card>
                    </b-col>

                </b-row>              
            </b-col>
              <b-col lg="6" >
                <card class=" card-block card-stretch card-height " bodyClass="row align-items-center">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">User's Progress</h4>
                     </template>
                        <template v-slot:headerAction>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg border border-primary text-primary p-2 rounded-normal" id="dropdownMenuButton2"
                                    data-toggle="dropdown">
                                    Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                        </b-dropdown>
                        </template>
                    
                    <template v-slot:body>
                        <b-col md="9">
                             <ApexChart element="fit-progress-chart-03" :chartOption="chart2"/>
                        </b-col>
                        <b-col md="3">
                            <ul class="m-0 p-0 list-inline text-center data-indicator">
                                <li class="position-relative">
                                    <h2 class="line-height"><b>84</b></h2>
                                    <span class="status"><i class="ri-checkbox-blank-circle-fill text-primary"></i></span>
                                    <p class="mb-0 mt-2">Your points</p>
                                </li>
                                <li class="mt-3 position-relative">
                                    <h2 class="line-height"><b>64</b></h2>
                                    <span class="status"><i class="ri-checkbox-blank-circle-fill text-danger"></i></span>
                                    <p class="mb-0 mt-2">Average</p>
                                </li>
                            </ul>
                        </b-col>

                    </template>
                </card>
            </b-col>
            <b-col lg="6">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Upcoming  Events</h4>
                     </template>
                    
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="d-flex align-items-center justify-content-between pb-3 border-bottom">
                                <div class="icon iq-icon-box event-icon bg-primary rounded-small font-size-18">
                                    <div class="date">23</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>Yoga Special Training</h5>
                                    <p class="mb-0">08 : 30 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                            <li class="d-flex align-items-center justify-content-between pb-3 pt-3 border-bottom">
                                <div class="icon iq-icon-box event-icon bg-warning rounded-small font-size-18">
                                    <div class="date">25</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>Zumba Training Sessions</h5>
                                    <p class="mb-0">08 : 45 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                            <li class="d-flex align-items-center justify-content-between pt-3">
                                <div class="icon iq-icon-box event-icon bg-success rounded-small font-size-18">
                                    <div class="date">28</div>
                                    <div class="month">Oct</div>
                                </div>
                                <div class="event-info ml-3">
                                    <h5>personal Training Happy Week</h5>
                                    <p class="mb-0">09 : 00 Am</p>
                                </div>
                                <div class="d-flex align-items-center font-size-18">
                                    <span class="mr-2"><i class="ri-edit-box-line"></i></span>
                                    <span><i class="ri-delete-bin-line text-danger"></i></span>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="4">
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Top Performers</h4>
                     </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                        </template>
                    
                    <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-5.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Julia Met</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-6.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Carolina Tensen</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/user-7.jpg"
                                        class="img-fluid avatar-80 rounded-small" alt="image"></a>
                                <div class="media-body ml-4">
                                    <h5>Anna Mull</h5>
                                    <p class="mb-0">Fitness</p>
                                    <div class="text-body">23/8/2020</div>
                                </div>
                            </li>
                        </ul>
                    </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                            <h4 class="card-title">Social Media</h4>
                   </template>
                         <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                         </template>
                    
                    <template v-slot:body>
                         <ApexChart element="fit-progress-chart-02" :chartOption="chart3"/>
                    </template>
                </card>
            </b-col>
            <b-col lg="4" >
                <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                            <h4 class="card-title">Products</h4>
                     </template>
                        <template v-slot:headerAction>
                            <a href="#" class="btn btn-sm btn-outline-primary view-more">View More</a>
                        </template>
                   
                   <template v-slot:body>
                        <ul class="list-inline p-0 m-0">
                            <li class="media align-items-center">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-1.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>protein  Pills</h5>
                                    <p class="mb-0">100 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 12.8</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-2.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>Coffee beans</h5>
                                    <p class="mb-0">92 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 8.6</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-3.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>Protien Bar</h5>
                                    <p class="mb-0">50 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 15.5</b></p>
                            </li>
                            <li class="media align-items-center mt-3">
                                <a href="JavaScript:Void(0);"><img src="../../../assets/images/layouts/layout-3/prod-4.jpg"
                                        class="img-fluid avatar-60 rounded-small" alt="image"></a>
                                <div class="media-body ml-3">
                                    <h5>CBD Oil</h5>
                                    <p class="mb-0">95 Items</p>
                                </div>
                                <p class="mb-0 font-size-18"><b>$ 110</b></p>
                            </li>
                        </ul>
                   </template>
                </card>
            </b-col>
      </b-row>  
  </b-container>
    </tab-content-item>
     <tab-content-item :active="false" id="layout3" aria-labelled-by="layout3-tab" role="tabpanel">
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
                                    <Progressbar :value="85" color="primary" class=" mt-2" midclass="iq-progress progress-1" colorName="primary">
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
                <card class=" card-block card-stretch card-height salon1-wecm" style="background: url(../../../assets/images/layouts/layout-4/welcome-bg.png);background-repeat:no-repeat;background-position: center right;background-size: contain;">                    
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
                               
                                  <Slick  :option="option">

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
                                <ApexChart element="salon-chart-02" :chartOption="chart4" />
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
     </tab-content-item>
      <tab-content-item :active="false" id="layout4" aria-labelled-by="layout4-tab" role="tabpanel">
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
                        <ApexChart element="ecommerce2-chart-07" :chartOption="chart10" />
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
                         <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
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
                        <ApexChart element="ecommerce2-chart-01" :chartOption="chart5" />
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
                        <ApexChart element="ecommerce2-chart-02" :chartOption="chart9" />
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
                                <ApexChart element="ecommerce2-chart-04" :chartOption="chart7" />
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
                                <ApexChart element="ecommerce2-chart-05" :chartOption="chart8" />
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
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
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
      </tab-content-item>
      <tab-content-item :active="false" id="layout5" aria-labelled-by="layout5-tab" role="tabpanel">
             <b-container fluid="">
        <b-row >
               <b-col lg="3" md="6" >
                  <card class=" card-block card-stretch card-height bg-primary" bodyClass=" tdy-appoin">
                    <template v-slot:body>                       
                           <div class="d-flex align-items-center">
                              <div class="img-icon bg-white avatar-60 rounded-small">
                                 <i class="las la-briefcase-medical"></i>
                              </div>
                              <div class="image-text ml-3">
                                 <h4 class="text-white mb-1"><b>john Hospital</b></h4>
                                 <p class="mb-0 text-capitlise">Appoinments</p>
                              </div>
                           </div>
                           <div class="top-title-text-block">
                              <div class="d-flex align-items-center">
                                 <h1 class="text-white mr-3">15</h1>
                                 <div>
                                    <span class="app-percentage">25%</span>
                                 </div>
                              </div>                             
                              <p class="mb-0 mt-2 text-white">Today Appoinment</p>
                           </div>                      
                           <div class="pt-50">
                              <div class="d-flex align-items-center">
                                 <h1 class="text-white mr-3">30</h1>
                                 <div>
                                    <span class="app-percentage">40%</span>
                                 </div>
                              </div>
                              <p class="mb-0 mt-2 text-white">Upcoming Appoinment</p>
                           </div>
                    </template>
                  </card>
               </b-col>
               <b-col lg="3" md="6" >
                  <card class=" card-block card-stretch card-height-half">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between fit-box">
                           <div>
                              <div class="fit-icon rounded text-center bg-danger-light svg-danger">
                                 <svg width="32" height="39" viewBox="0 0 52 65" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                       d="M39.9512 38.0488H36.7527C35.3671 38.0488 34.2439 36.9255 34.2439 35.5399C34.2439 34.7139 34.6602 33.9521 35.2961 33.4249C38.525 30.7475 40.5854 26.7077 40.5854 22.1951V9.51219C40.5854 4.26717 36.3182 0 31.0732 0H14.5854C10.0397 0 6.34146 3.69821 6.34146 8.2439C6.34146 9.40055 6.58094 10.5022 7.0129 11.5021C8.53651 15.0286 11.4146 18.3535 11.4146 22.1951C11.4146 26.7077 13.475 30.7475 16.7039 33.4249C17.3398 33.9521 17.7561 34.7139 17.7561 35.5399C17.7561 36.9255 16.6329 38.0488 15.2473 38.0488H12.0488C5.40508 38.0488 0 43.4539 0 50.0976V63.0341C0 64.0848 0.851785 64.9366 1.90244 64.9366H50.0976C51.1482 64.9366 52 64.0848 52 63.0341V50.0976C52 43.4539 46.5949 38.0488 39.9512 38.0488ZM14.5854 3.80488H31.0732C34.2202 3.80488 36.7805 6.36518 36.7805 9.51219C36.7805 11.1978 35.3111 12.5534 33.7378 11.9486C32.3083 11.3991 30.9971 10.5506 29.8817 9.43521C29.5251 9.07844 29.0412 8.87805 28.5366 8.87805C28.0319 8.87805 27.5481 9.07844 27.1914 9.43534C25.0971 11.5295 22.3127 12.6829 19.3508 12.6829H14.5854C14.284 12.6829 13.9898 12.6525 13.7052 12.5949C13.7002 12.5939 13.6952 12.5931 13.6902 12.5921C11.6701 12.1769 10.1463 10.385 10.1463 8.2439C10.1463 5.79622 12.1377 3.80488 14.5854 3.80488ZM15.2195 22.1951V20.6191C15.2195 18.3375 17.0692 16.4878 19.3508 16.4878C21.3293 16.4878 23.2489 16.1046 25.0249 15.3733C27.239 14.4617 29.8298 14.4588 32.0441 15.37C34.5782 16.4129 36.7805 18.5909 36.7805 21.3312V22.1951C36.7805 28.1395 31.9444 32.9756 26 32.9756C20.0556 32.9756 15.2195 28.1395 15.2195 22.1951ZM26 36.7805C26.2172 36.7805 26.4333 36.7757 26.6482 36.7662C28.5563 36.6821 30.439 38.0413 30.439 39.9512C30.439 41.0019 31.2908 41.8537 32.3415 41.8537H39.9512C44.4969 41.8537 48.1951 45.5519 48.1951 50.0976V50.3869C48.1951 52.8354 45.5379 54.36 43.4241 53.1242C42.4515 52.5556 41.8537 51.5136 41.8537 50.3869V50.0976C41.8537 49.0469 41.0019 48.1951 39.9512 48.1951C38.6356 48.1951 36.7091 49.1985 35.5733 48.5345L21.846 40.5093C21.6535 40.3967 21.5611 40.1742 21.5611 39.9512C21.5611 38.0414 23.4439 36.6821 25.3519 36.7662C25.5668 36.7757 25.7828 36.7805 26 36.7805ZM3.80488 50.0976C3.80488 46.7357 5.82778 43.8377 8.72028 42.5562C10.2127 41.8949 11.8638 42.6222 12.9416 43.8482L19.4683 51.2723C19.804 51.6542 19.5329 52.2537 19.0244 52.2537C15.5277 52.2537 12.6829 55.0984 12.6829 58.5951C12.6829 59.8258 11.8345 61.1317 10.6038 61.1317H7.5238C5.46989 61.1317 3.80488 59.4667 3.80488 57.4128V50.0976ZM16.4878 58.5951C16.4878 57.1964 17.6257 56.0585 19.0244 56.0585H22.5285C23.2579 56.0585 23.952 56.3725 24.4336 56.9203C25.8744 58.5592 24.7106 61.1317 22.5285 61.1317H19.0244C17.6257 61.1317 16.4878 59.9938 16.4878 58.5951ZM37.5625 61.1317C34.7908 61.1317 32.1532 59.9386 30.3232 57.8569L16.4615 42.0894C16.3809 41.9977 16.446 41.8537 16.5682 41.8537C16.5934 41.8537 16.6181 41.8604 16.6398 41.8731L47.9399 60.1715C48.098 60.264 48.1951 60.4333 48.1951 60.6164C48.1951 60.901 47.9644 61.1317 47.6798 61.1317H37.5625Z" />
                                 </svg>
                              </div>
                              <div class="iq-cart-text mt-3">
                                 <h2 class="text-danger">212</h2>
                                 <p class="mb-0">New Patient</p>
                              </div>
                           </div>
                           <div class="iq-progress-bar-linear d-inline-block">
                              <Progressbar :value="60" color="danger" :verticle="true" class="progress-bar-vertical"/>
                           </div>
                        </div>
                    </template>
                  </card>
                  <card class=" card-block card-stretch card-height-half">
                    <template v-slot:body>
                        <div class="d-flex align-items-center justify-content-between fit-box">
                           <div>
                              <div class="fit-icon rounded text-center bg-success-light svg-success">
                                 <svg width="43" height="39" viewBox="0 0 52 47" fill="none" xmlns="http://www.w3.org/2000/svg">
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
                              <div class="iq-cart-text mt-3">
                                 <h2 class="text-success">250 M</h2>
                                 <p class="mb-0">Total Earning</p>
                              </div>
                           </div>
                           <div class="iq-progress-bar-linear d-inline-block">
                              <Progressbar :value="75" color="success" :verticle="true" class="progress-bar-vertical"/>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col lg="6" >
                  <card class=" card-block card-stretch card-height">
                     <div class="c-medical-bg" :style="`background:url(${require('../../../assets/images/layouts/layout-14/medicine.jpg')})center bottom no-repeat;background-size: cover;`">
                        <div class="card-body p-4">
                           <h1 class="medi-text">Exceptional care close to You</h1>                        
                        </div>   
                     </div>
                  </card>
               </b-col>             
              <b-col lg="6" xl="5" >
                  <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                           <h4 class="card-title">Annual Report</h4>
                    </template>
                       <template v-slot:headerAction>
                         <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                               <span class="dropdown-toggle dropdown-bg btn btn-outline-primary" role="button" id="dropdownMenuButton5"
                                 data-toggle="dropdown" aria-expanded="false">
                              Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                         </b-dropdown>
                       </template>
                     <template v-slot:body>
                        <div class="row mb-1">
                           <div class="col-md-4 mb-3 mb-md-0">
                              <h4>$ 50K</h4>
                              <p class="text-info font-weight-700 mb-0">Profit</p>
                              <div class="iq-progress-bar-linear d-inline-block w-100">
                                  <Progressbar :value="35" color="info"/>
                              </div>
                           </div>
                           <div class="col-md-4 mb-3 mb-md-0">
                              <h4>$ 75K</h4>
                              <p class="text-warning font-weight-700 mb-0">Maintenance</p>
                              <div class="iq-progress-bar-linear d-inline-block w-100">
                                  <Progressbar :value="65" color="warning"/>
                              </div>
                           </div>
                           <div class="col-md-4 mb-3 mb-md-0">
                              <h4>$ 20K</h4>
                              <p class="text-success font-weight-700 mb-0">Pharmacy</p>
                              <div class="iq-progress-bar-linear d-inline-block w-100">
                                  <Progressbar :value="25" color="success"/>
                              </div>
                           </div>
                        </div>
                         <ApexChart element="hospital2-chart-01" :chartOption="chart11"/>
                     </template>
                  </card>
               </b-col>
               <b-col lg="6" xl="3" md="6">
                  <card class=" card-block card-stretch card-height" bodyClass="recent-appo">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">Recent Appoinment</h4>
                        </template>
                    <template v-slot:body>                     
                        <div class="media border rounded-normal">
                           <div class="img-icon bg-primary position-relative rounded-small avatar-60">
                              <img src="../../../assets/images/layouts/layout-14/r-1.png"
                                 class="img-fluid" alt="image">                             
                           </div>
                           <div class="media-body ml-3">
                              <h5 class="mb-1 text-primary">Mathew Versteng</h5>
                              <p class="mb-1">HiLead Fenix LLC</p> 
                              <p class="mb-3"><span class="title-text">10 October 2020</span> at 4:07 PM</p>
                              <a href="#" class="text-primary"><span>Book Now</span> <i class="ri-arrow-right-s-line read-ic"></i></a>                                    
                           </div>
                        </div>
                        <div class="media border rounded-normal spc-20">
                           <div class="img-icon bg-primary position-relative rounded-small avatar-60">
                              <img src="../../../assets/images/layouts/layout-14/r-2.png" class="img-fluid" alt="image">
                           </div>
                           <div class="media-body ml-3">
                              <h5 class="mb-1 text-primary">David King</h5>
                              <p class="mb-1">Acme Corporation</p>
                              <p class="mb-3"><span class="title-text">25 September 2020</span> at 10:00 AM</p>
                              <a href="#" class="text-primary"><span>Book Now</span> <i class="ri-arrow-right-s-line read-ic"></i></a>
                           </div>
                        </div>
                      </template>
                  </card>
               </b-col>
              <b-col lg="6" xl="4" md="6">
                  <card class=" card-block card-stretch card-height">
                   <template v-slot:headerTitle>
                           <h4 class="card-title">Appoinment Survey</h4>
                       </template>
                    <template v-slot:body>
                       <ApexChart element="hospital2-chart-02" :chartOption="chart12"/>
                      </template>
                  </card>
               </b-col>           
               <b-col lg="6" xl="3" md="6">
                  <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">By Country</h4>
                      </template>
                      <template v-slot:body>
                       <ApexChart element="hospital2-chart-03" :chartOption="chart13"/>
                     </template>
                  </card>
              </b-col> 
              <b-col lg="6" xl="3" md="6">
                  <card class=" card-block card-stretch card-height" bodyClass="text-center">
                    <template v-slot:headerTitle>
                           <h4 class="card-title">Hospital Rating</h4>
                       </template>
                    <template v-slot:body>
                        <p class="mb-1">Your Progress is pretty good</p>
                        <ApexChart element="hospital2-chart-04" :chartOption="chart14"/>
                        <h3 class="rat-no">4.2/5</h3>
                    </template>
                  </card>
                </b-col> 
               <b-col lg="6" >
                  <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">Operation Survey</h4>
                     </template>
                         <template v-slot:headerAction>
                           <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                               <span class="dropdown-toggle btn btn-outline-primary p-2" id="dropdownMenuButton6" role="button"
                                 data-toggle="dropdown" aria-expanded="false">
                              Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                         </b-dropdown>
                         </template>
                     <template v-slot:body>
                       <ApexChart element="hospital2-chart-05" :chartOption="chart15"/>
                     </template>
                  </card>
               </b-col>             
               <b-col lg="4" md="6" >
                  <card class=" card-block card-stretch card-height" bodyClass=" text-center inln-date">
                     <template v-slot:body>
                        <flat-pickr :config="config" id="inline-date" value="" class="date-input basicFlatpickr d-none" readonly="readonly"/>
                     </template>
                  </card>
               </b-col>
              <b-col lg="4" md="6" >
                  <card class=" card-block card-stretch card-height">
                     <template v-slot:body>                      
                        <div class="media">
                           <img src="../../../assets/images/user/03.jpg" class="avatar-110 rounded" alt="image">
                           <div class="media-body ml-4">
                              <h4>Dr. Bob Frapples</h4>
                              <h6 class="text-primary mt-1">Surgeon Expert</h6>
                              <p class="mb-0">Ontario, Canada</p>
                              <div class="d-flex justify-content-left doc-social h-doc-s">
                                 <a href="#"><i class="las la-star text-warning"></i></a>
                                 <a href="#"><i class="las la-star text-warning"></i></a>
                                 <a href="#"><i class="las la-star text-warning"></i></a>
                                 <a href="#"><i class="las la-star text-warning"></i></a>
                              </div>
                           </div>
                        </div>                     
                        
                        <ul class="list-inline p-0 m-0 mt-4">
                           <li class="d-flex align-items-center justify-content-between mb-3">
                              <div class="d-flex align-items-center">
                                 <div class="ex-box iq-icon-box rounded-small bg-warning-light svg-warning text-center">
                                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <path
                                          d="M11.1326 7.40612C10.7945 6.96059 10.582 6.42168 10.582 5.83594V0H9.52734V5.83594C9.52734 6.84693 9.94665 7.78187 10.6387 8.45986C10.7208 8.06769 10.8971 7.71346 11.1326 7.40612Z"
                                          fill="#FE721C" />
                                       <path
                                          d="M10.582 12.1641C10.582 11.5783 10.7945 11.0394 11.1326 10.5939C10.8971 10.2866 10.7208 9.9323 10.6387 9.54013C9.94669 10.2181 9.52734 11.1531 9.52734 12.1641V18H10.582V12.1641Z"
                                          fill="#FE721C" />
                                       <path
                                          d="M11.6287 11.0894C11.475 11.4234 11.3838 11.7847 11.3838 12.1641C11.3838 12.8686 11.6583 13.5308 12.1557 14.0283C13.1862 15.0588 14.8901 15.0592 15.9199 14.0283C17.3407 12.6075 18.0335 10.7302 17.9982 8.86417C17.9647 7.08871 17.2721 5.32351 15.9204 3.97168C14.9244 2.97571 13.1512 2.97571 12.1563 3.97168C11.6583 4.46914 11.3838 5.13142 11.3838 5.83591C11.3838 6.21525 11.475 6.57645 11.6287 6.91057C12.0721 6.57226 12.6192 6.36329 13.2187 6.36329V7.41798C12.3463 7.41798 11.6366 8.12764 11.6366 9.00001C11.6366 9.87238 12.3463 10.582 13.2187 10.582V11.6367C12.6192 11.6367 12.0722 11.4278 11.6287 11.0894Z"
                                          fill="#FE721C" />
                                       <path
                                          d="M5.84369 14.0283C6.34168 13.5308 6.61618 12.8685 6.61618 12.164C6.61618 11.6575 6.4694 11.1753 6.20457 10.758C5.72163 11.2934 5.02997 11.6367 4.25393 11.6367V10.582C5.1263 10.582 5.83596 9.87234 5.83596 8.99998C5.83596 8.12761 5.1263 7.41794 4.25393 7.41794V6.36326C5.02993 6.36326 5.72163 6.70656 6.20457 7.24195C6.4694 6.82468 6.61618 6.34241 6.61618 5.83591C6.61618 5.13142 6.34168 4.46914 5.84422 3.97168C4.84824 2.97571 3.075 2.97571 2.08008 3.97168C0.728143 5.32358 0.0354239 7.08874 0.00177939 8.8642C-0.0336229 10.7301 0.659026 12.6075 2.07955 14.0283C3.11001 15.0588 4.81386 15.0592 5.84369 14.0283Z"
                                          fill="#FE721C" />
                                       <path
                                          d="M8.47273 18V12.1641C8.47273 10.9123 7.84748 9.80486 6.87699 9.13583C6.85632 9.53296 6.74695 9.90336 6.56909 10.2353C7.09225 10.718 7.41804 11.4026 7.41804 12.1641V18H8.47273Z"
                                          fill="#FE721C" />
                                       <path
                                          d="M6.87699 8.86416C7.84748 8.19513 8.47273 7.08768 8.47273 5.83594V0H7.41804V5.83594C7.41804 6.59735 7.09225 7.28202 6.56909 7.76475C6.74695 8.09666 6.85632 8.46707 6.87699 8.86416Z"
                                          fill="#FE721C" />
                                    </svg>
                                 </div>
                                 <div class="iq-result-info">
                                    <h5>Kidney</h5>
                                 </div>
                              </div>
                              <p class="mb-0 font-size-18"><b>85</b></p>
                           </li>
                           <li class="d-flex align-items-center justify-content-between mb-3">
                              <div class="d-flex align-items-center">
                                 <div class="ex-box iq-icon-box rounded-small bg-success-light svg-success text-center">
                                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <g>
                                          <path
                                             d="M10.8676 1.97743C9.60581 1.64306 8.15948 1.89454 7.15236 2.6171H6.75752C6.21668 2.6171 5.77667 2.17677 5.77667 1.6355V0.693422C5.77667 0.311063 5.46557 0 5.08325 0H4.54413C4.1618 0 3.8507 0.311063 3.8507 0.693422V1.91468C3.8507 3.15415 4.71126 4.20493 5.88495 4.47623C5.86139 4.57235 5.84192 4.67005 5.82669 4.76866C5.59565 6.26273 6.39647 7.23741 7.03993 8.02062C7.94317 9.11995 8.43398 9.77361 6.70461 11.2562C6.26611 11.6321 5.98806 12.1538 5.9181 12.7178H5.24757C4.13709 12.7178 3.23364 13.6217 3.23364 14.7327V17.3066C3.23364 17.6889 3.5447 18 3.92706 18H4.37847C4.76079 18 5.07189 17.6889 5.07189 17.3066V15.126C5.07189 14.9806 5.19019 14.8623 5.3356 14.8623H6.86672C7.29534 15.1597 8.03088 15.4026 8.68296 15.4026C9.64698 15.4026 10.695 14.9606 11.6932 14.1219C12.8828 13.1226 13.844 11.6886 14.3996 10.084C15.6562 6.45529 13.4896 2.67212 10.8676 1.97743ZM12.5101 10.2302C11.9875 11.7215 9.76788 14.2178 8.26439 13.7851C7.55353 13.5806 7.35852 12.7109 8.10545 12.0365C8.93014 11.2918 9.41175 10.4907 9.46156 9.78082C9.46831 9.68474 9.59143 9.69096 9.68751 9.69096C9.93181 9.69096 10.2897 9.75625 10.764 10.0061C11.2496 10.262 11.8126 10.2982 12.3922 10.1107C12.4651 10.0871 12.5353 10.1584 12.5101 10.2302ZM9.36105 3.51352C9.18088 3.47467 9.0906 3.29115 9.15644 3.12996C9.2746 2.84664 9.69715 2.93171 9.69715 3.23754C9.69711 3.41346 9.53697 3.54741 9.36105 3.51352ZM12.9209 6.82179C12.55 5.31436 11.8494 4.0069 10.3318 3.65752C10.1804 3.62268 10.086 3.47171 10.1208 3.32033C10.1556 3.16898 10.3066 3.07455 10.458 3.10936C11.9764 3.45892 12.9607 4.6293 13.4672 6.68739C13.5108 6.86464 13.3764 7.03593 13.1939 7.03593C13.0674 7.03589 12.9525 6.95004 12.9209 6.82179Z"
                                             fill="#37E6B0" />
                                       </g>
                                    </svg>
                                 </div>
                                 <div class="iq-result-info">
                                    <h5>Stomach</h5>
                                 </div>
                              </div>
                              <p class="mb-0 font-size-18"><b>40</b></p>
                           </li>
                           <li class="d-flex align-items-center justify-content-between mb-3">
                              <div class="d-flex align-items-center">
                                 <div class="ex-box iq-icon-box rounded-small bg-info-light svg-info text-center">
                                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <g>
                                          <path
                                             d="M16.2674 2.14775H14.337C13.9225 2.14775 13.5035 2.12771 13.0767 2.09361C13.4374 2.93982 13.4465 3.97657 13.4289 4.43466C13.4317 5.05868 13.5678 5.5906 13.823 5.9738C14.4569 6.92548 14.8194 8.12853 14.8039 9.18849C16.3932 8.49137 18.0085 6.27952 17.9999 4.25501C17.9947 2.95318 17.3306 2.14775 16.2674 2.14775Z"
                                             fill="#4788FF" />
                                          <path
                                             d="M12.3743 4.41462C12.3743 4.4111 12.4826 2.11646 11.5028 1.89743C11.5017 1.89743 11.5007 1.89708 11.5 1.89673C11.2285 1.85461 10.6225 1.73758 10.016 1.59228C8.61187 1.25513 7.15676 1.08708 5.69004 1.08989C2.55832 1.09798 0 3.69005 0 6.82564V12.8996C0 13.9479 0.852891 14.8008 1.9016 14.8008C2.57098 14.8008 3.19816 14.4426 3.53883 13.866C4.18289 12.7751 5.16691 11.918 6.36293 11.6944V10.4917C6.36293 9.67048 6.04371 8.8988 5.46328 8.31837C5.25727 8.11235 5.25727 7.77837 5.46328 7.57235C5.66895 7.36634 6.00293 7.36669 6.20895 7.57235C6.98871 8.35212 7.41797 9.38888 7.41797 10.4917V12.1778C7.425 12.4622 7.65879 12.6915 7.94496 12.6915C8.2357 12.6915 8.47195 12.4549 8.47195 12.1641C8.47195 12.1595 8.47195 12.155 8.47231 12.1508C8.47231 11.6189 8.47231 11.0221 8.47231 10.4917C8.47231 9.38888 8.90227 8.35212 9.68203 7.57235C9.8877 7.36634 10.2217 7.36634 10.4277 7.57235C10.6337 7.77837 10.6337 8.11235 10.4277 8.31837C9.84727 8.8988 9.52734 9.67048 9.52734 10.4917V11.6371C10.472 11.6371 11.3098 11.6368 11.3122 11.6368C12.5914 11.6368 13.6342 10.6422 13.7355 9.42579C13.7359 9.42333 13.7362 9.42087 13.7366 9.41841C13.8108 8.62493 13.5671 7.4922 12.9452 6.55845C12.5719 5.99771 12.3743 5.25661 12.3743 4.41462Z"
                                             fill="#4788FF" />
                                          <path
                                             d="M7.41797 13.6558V16.3828C7.41797 16.6854 7.67197 16.9309 7.98609 16.9088C8.25891 16.8887 8.47231 16.6486 8.47231 16.3621V13.6554C8.30707 13.7141 8.12988 13.7461 7.94496 13.7461C7.76039 13.7461 7.58285 13.7141 7.41797 13.6558Z"
                                             fill="#4788FF" />
                                       </g>
                                    </svg>
                                 </div>
                                 <div class="iq-result-info">
                                    <h5>Liver</h5>
                                 </div>
                              </div>
                              <p class="mb-0 font-size-18"><b>35</b></p>
                           </li>
                           <li class="d-flex align-items-center justify-content-between">
                              <div class="d-flex align-items-center">
                                 <div class="ex-box iq-icon-box rounded-small bg-primary-light svg-primary text-center">
                                    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                       <path
                                          d="M3.32728 11.5619C3.37552 11.5947 3.41239 11.6416 3.43279 11.6962C3.45319 11.7508 3.45612 11.8104 3.44115 11.8668C3.31611 12.3372 3.36952 12.8373 3.5911 13.2708C3.81268 13.7042 4.18677 14.0404 4.64135 14.2146H4.64163H4.64188C4.91021 14.3167 5.19763 14.359 5.48403 14.3385C5.77042 14.3179 6.04886 14.235 6.29983 14.0955C6.55081 13.9561 6.76827 13.7634 6.93697 13.5311C7.10567 13.2987 7.22154 13.0323 7.27645 12.7505C7.28316 12.7139 7.29703 12.6791 7.31728 12.6479C7.33752 12.6168 7.36374 12.59 7.39441 12.569C7.42508 12.548 7.4596 12.5334 7.49597 12.5258C7.53235 12.5183 7.56986 12.518 7.60633 12.525C7.64281 12.5321 7.67753 12.5463 7.7085 12.5668C7.73946 12.5873 7.76605 12.6138 7.78673 12.6446C7.80741 12.6755 7.82177 12.7102 7.82899 12.7466C7.8362 12.783 7.83612 12.8205 7.82876 12.857C7.76397 13.1899 7.63299 13.5064 7.44357 13.7877C7.25416 14.069 7.01017 14.3094 6.72609 14.4947C6.442 14.68 6.12361 14.8063 5.78978 14.8661C5.45596 14.926 5.11351 14.9183 4.78275 14.8433C4.78208 14.8642 4.78124 14.885 4.78124 14.9059C4.78124 15.4281 4.98866 15.9288 5.35787 16.298C5.72708 16.6673 6.22784 16.8747 6.74999 16.8747C7.27213 16.8747 7.77289 16.6673 8.14211 16.298C8.51132 15.9288 8.71874 15.4281 8.71874 14.9059V11.8125C8.27134 11.812 7.84242 11.634 7.52606 11.3177C7.2097 11.0013 7.03175 10.5724 7.03124 10.125V9.84375C7.03124 9.76916 7.06087 9.69762 7.11361 9.64488C7.16636 9.59213 7.2379 9.5625 7.31249 9.5625C7.38708 9.5625 7.45862 9.59213 7.51136 9.64488C7.56411 9.69762 7.59374 9.76916 7.59374 9.84375V10.125C7.59407 10.4233 7.71271 10.7092 7.92361 10.9201C8.13452 11.131 8.42047 11.2497 8.71874 11.25V3.65625H7.87499C7.8004 3.65625 7.72886 3.62662 7.67611 3.57387C7.62337 3.52113 7.59374 3.44959 7.59374 3.375C7.59374 3.30041 7.62337 3.22887 7.67611 3.17613C7.72886 3.12338 7.8004 3.09375 7.87499 3.09375H8.71874C8.71874 2.57161 8.51132 2.07085 8.14211 1.70163C7.77289 1.33242 7.27213 1.125 6.74999 1.125C6.22784 1.125 5.72708 1.33242 5.35787 1.70163C4.98866 2.07085 4.78124 2.57161 4.78124 3.09375C4.78124 3.11467 4.78208 3.13552 4.78275 3.1564C5.11351 3.08143 5.45596 3.07366 5.78978 3.13354C6.12361 3.19342 6.442 3.31973 6.72609 3.50498C7.01017 3.69024 7.25416 3.93066 7.44357 4.21199C7.63299 4.49332 7.76397 4.80982 7.82876 5.14273C7.83612 5.17914 7.8362 5.21665 7.82899 5.25309C7.82177 5.28953 7.80741 5.32418 7.78673 5.35504C7.76605 5.3859 7.73946 5.41236 7.7085 5.43289C7.67753 5.45342 7.64281 5.46761 7.60633 5.47464C7.56986 5.48167 7.53235 5.48141 7.49597 5.47387C7.4596 5.46632 7.42508 5.45165 7.39441 5.43069C7.36374 5.40973 7.33752 5.3829 7.31728 5.35175C7.29703 5.3206 7.28316 5.28575 7.27645 5.24922C7.22154 4.96739 7.10567 4.70097 6.93697 4.46863C6.76827 4.23628 6.55081 4.04363 6.29983 3.90415C6.04886 3.76468 5.77042 3.68176 5.48403 3.6612C5.19763 3.64064 4.91021 3.68294 4.64188 3.78513H4.64163H4.64135C4.18677 3.95929 3.81268 4.29545 3.5911 4.72889C3.36952 5.16234 3.31611 5.66244 3.44115 6.1329C3.45612 6.18925 3.45319 6.24886 3.43279 6.30348C3.41239 6.3581 3.37552 6.40503 3.32728 6.43778C2.90883 6.72138 2.56622 7.10317 2.3294 7.54977C2.09257 7.99637 1.96875 8.49418 1.96875 8.99968C1.96875 9.50519 2.09257 10.003 2.3294 10.4496C2.56622 10.8962 2.90883 11.278 3.32728 11.5616V11.5619ZM4.49999 9.84375H4.78124C5.0795 9.84342 5.36546 9.72478 5.57636 9.51388C5.78727 9.30297 5.9059 9.01702 5.90624 8.71875V8.69488C5.51328 8.62796 5.15663 8.42429 4.89931 8.11987C4.64198 7.81545 4.50054 7.42986 4.49999 7.03125V6.75C4.49999 6.67541 4.52962 6.60387 4.58236 6.55113C4.63511 6.49838 4.70665 6.46875 4.78124 6.46875C4.85583 6.46875 4.92737 6.49838 4.98011 6.55113C5.03286 6.60387 5.06249 6.67541 5.06249 6.75V7.03125C5.06249 7.32962 5.18102 7.61577 5.39199 7.82675C5.60297 8.03772 5.88912 8.15625 6.18749 8.15625C6.48586 8.15625 6.77201 8.03772 6.98298 7.82675C7.19396 7.61577 7.31249 7.32962 7.31249 7.03125V6.75C7.31249 6.67541 7.34212 6.60387 7.39486 6.55113C7.44761 6.49838 7.51915 6.46875 7.59374 6.46875C7.66833 6.46875 7.73987 6.49838 7.79261 6.55113C7.84536 6.60387 7.87499 6.67541 7.87499 6.75V7.03125C7.87443 7.42986 7.733 7.81545 7.47567 8.11987C7.21834 8.42429 6.86169 8.62796 6.46874 8.69488V8.71875C6.46823 9.16615 6.29027 9.59507 5.97392 9.91143C5.65756 10.2278 5.22863 10.4057 4.78124 10.4062H4.49999C4.4254 10.4062 4.35386 10.3766 4.30112 10.3239C4.24837 10.2711 4.21874 10.1996 4.21874 10.125C4.21874 10.0504 4.24837 9.97887 4.30112 9.92613C4.35386 9.87338 4.4254 9.84375 4.49999 9.84375Z"
                                          fill="#4788FF" />
                                       <path
                                          d="M14.6727 6.43814C14.6245 6.40539 14.5876 6.35847 14.5672 6.30385C14.5468 6.24923 14.5439 6.18962 14.5588 6.13327C14.6839 5.66279 14.6305 5.16269 14.4089 4.72924C14.1873 4.29579 13.8132 3.95962 13.3586 3.78546H13.3584H13.3581C13.0898 3.68327 12.8024 3.64097 12.516 3.66153C12.2296 3.68209 11.9511 3.76501 11.7002 3.90448C11.4492 4.04395 11.2317 4.23661 11.063 4.46895C10.8943 4.7013 10.7785 4.96771 10.7235 5.24954C10.7168 5.28608 10.703 5.32093 10.6827 5.35208C10.6625 5.38323 10.6363 5.41006 10.6056 5.43101C10.5749 5.45197 10.5404 5.46665 10.504 5.47419C10.4676 5.48174 10.4301 5.482 10.3937 5.47497C10.3572 5.46793 10.3225 5.45374 10.2915 5.43322C10.2605 5.41269 10.2339 5.38623 10.2133 5.35537C10.1926 5.32451 10.1782 5.28986 10.171 5.25342C10.1638 5.21698 10.1639 5.17947 10.1712 5.14305C10.236 4.81015 10.367 4.49364 10.5564 4.21231C10.7458 3.93099 10.9898 3.69056 11.2739 3.50531C11.558 3.32006 11.8764 3.19374 12.2102 3.13387C12.5441 3.07399 12.8865 3.08176 13.2173 3.15673C13.2179 3.13584 13.2188 3.115 13.2188 3.09408C13.2188 2.57193 13.0113 2.07117 12.6421 1.70196C12.2729 1.33275 11.7721 1.12533 11.25 1.12533C10.7279 1.12533 10.2271 1.33275 9.85788 1.70196C9.48867 2.07117 9.28125 2.57193 9.28125 3.09408H10.125C10.1996 3.09408 10.2711 3.12371 10.3239 3.17645C10.3766 3.2292 10.4062 3.30074 10.4062 3.37533C10.4062 3.44992 10.3766 3.52146 10.3239 3.5742C10.2711 3.62695 10.1996 3.65658 10.125 3.65658H9.28125V11.25C9.57952 11.2497 9.86547 11.131 10.0764 10.9201C10.2873 10.7092 10.4059 10.4233 10.4062 10.125V9.84376C10.4062 9.76917 10.4359 9.69763 10.4886 9.64489C10.5414 9.59214 10.6129 9.56251 10.6875 9.56251C10.7621 9.56251 10.8336 9.59214 10.8864 9.64489C10.9391 9.69763 10.9688 9.76917 10.9688 9.84376V10.125C10.9682 10.5724 10.7903 11.0013 10.4739 11.3177C10.1576 11.634 9.72865 11.812 9.28125 11.8125V14.9063C9.28125 15.4284 9.48867 15.9292 9.85788 16.2984C10.2271 16.6676 10.7279 16.875 11.25 16.875C11.7721 16.875 12.2729 16.6676 12.6421 16.2984C13.0113 15.9292 13.2188 15.4284 13.2188 14.9063C13.2188 14.8852 13.2179 14.8645 13.2173 14.8436C12.8865 14.9186 12.5441 14.9264 12.2102 14.8665C11.8764 14.8066 11.558 14.6803 11.2739 14.495C10.9898 14.3098 10.7458 14.0694 10.5564 13.788C10.367 13.5067 10.236 13.1902 10.1712 12.8573C10.1639 12.8209 10.1638 12.7834 10.171 12.7469C10.1782 12.7105 10.1926 12.6758 10.2133 12.645C10.2339 12.6141 10.2605 12.5876 10.2915 12.5671C10.3225 12.5466 10.3572 12.5324 10.3937 12.5254C10.4301 12.5183 10.4676 12.5186 10.504 12.5261C10.5404 12.5337 10.5749 12.5484 10.6056 12.5693C10.6363 12.5903 10.6625 12.6171 10.6827 12.6483C10.703 12.6794 10.7168 12.7143 10.7235 12.7508C10.7785 13.0326 10.8943 13.299 11.063 13.5314C11.2317 13.7637 11.4492 13.9564 11.7002 14.0959C11.9511 14.2353 12.2296 14.3183 12.516 14.3388C12.8024 14.3594 13.0898 14.3171 13.3581 14.2149H13.3584H13.3586C13.8132 14.0407 14.1873 13.7046 14.4089 13.2711C14.6305 12.8377 14.6839 12.3376 14.5588 11.8671C14.5439 11.8108 14.5468 11.7511 14.5672 11.6965C14.5876 11.6419 14.6245 11.5949 14.6727 11.5622C15.0912 11.2786 15.4338 10.8968 15.6706 10.4502C15.9074 10.0036 16.0312 9.50583 16.0312 9.00033C16.0312 8.49483 15.9074 7.99702 15.6706 7.55043C15.4338 7.10384 15.0912 6.72206 14.6727 6.43846V6.43814ZM13.5 10.4063H13.2188C12.7714 10.4058 12.3424 10.2278 12.0261 9.91144C11.7097 9.59508 11.5318 9.16616 11.5312 8.71876V8.69489C11.1383 8.62797 10.7816 8.42431 10.5243 8.11988C10.267 7.81546 10.1256 7.42987 10.125 7.03126V6.75001C10.125 6.67542 10.1546 6.60388 10.2074 6.55114C10.2601 6.49839 10.3317 6.46876 10.4062 6.46876C10.4808 6.46876 10.5524 6.49839 10.6051 6.55114C10.6579 6.60388 10.6875 6.67542 10.6875 6.75001V7.03126C10.6875 7.32963 10.806 7.61578 11.017 7.82676C11.228 8.03773 11.5141 8.15626 11.8125 8.15626C12.1109 8.15626 12.397 8.03773 12.608 7.82676C12.819 7.61578 12.9375 7.32963 12.9375 7.03126V6.75001C12.9375 6.67542 12.9671 6.60388 13.0199 6.55114C13.0726 6.49839 13.1442 6.46876 13.2188 6.46876C13.2933 6.46876 13.3649 6.49839 13.4176 6.55114C13.4704 6.60388 13.5 6.67542 13.5 6.75001V7.03126C13.4994 7.42987 13.358 7.81546 13.1007 8.11988C12.8434 8.42431 12.4867 8.62797 12.0938 8.69489V8.71876C12.0941 9.01703 12.2127 9.30298 12.4236 9.51389C12.6345 9.72479 12.9205 9.84343 13.2188 9.84376H13.5C13.5746 9.84376 13.6461 9.87339 13.6989 9.92614C13.7516 9.97888 13.7812 10.0504 13.7812 10.125C13.7812 10.1996 13.7516 10.2711 13.6989 10.3239C13.6461 10.3766 13.5746 10.4063 13.5 10.4063Z"
                                          fill="#4788FF" />
                                    </svg>
                                 </div>
                                 <div class="iq-result-info">
                                    <h5>Brain</h5>
                                 </div>
                              </div>
                              <p class="mb-0 font-size-18"><b>50</b></p>
                           </li>
                        </ul>
                     </template>
                  </card>
              </b-col>
               <b-col lg="4" >
                  <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">Patient Survey</h4>
                     </template>
                        <template v-slot:headerAction>
                           <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown" class="dropdown shadow-none">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle dropdown-bg btn btn-outline-primary" role="button" id="dropdownMenuButton7" data-toggle="dropdown"
                                 aria-expanded="false">
                              Monthly<i class="ri-arrow-down-s-line ml-1"></i>
                              </span>
                          </template>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                         </b-dropdown>
                        </template>
                      <template v-slot:body>
                        <ApexChart element="hospital2-chart-06" :chartOption="chart16"/>
                      </template>
                  </card>
               </b-col>            
               <b-col lg="12" >
                  <card class=" card-block card-stretch card-height" bodyClass="rec-pat">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">Recent Patient</h4>
                     </template>
                        <template v-slot:headerAction>
                           <button class="btn btn-outline-primary">View All</button>
                        </template>
                      <template v-slot:body>
                        <div class="table-responsive">
                           <table class="table table-striped mb-0 table-borderless">
                              <thead>
                                 <tr>
                                    <th>Name</th>
                                    <th>Date</th>
                                    <th>Age</th>
                                    <th>Diseases</th>
                                    <th>Doctor</th>
                                    <th>Progress</th>
                                    <th>Report</th>
                                    <th>Status</th>
                                 </tr>
                              </thead>
                              <tbody>
                                 <tr>
                                    <td>
                                       <div class="media align-items-center">
                                          <img src="../../../assets/images/user/08.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                          <div class="media-body ml-3">
                                             <p class="mb-0">William Smith</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>20/08/2020
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
                                          <Progressbar :value="75" color="primary"/>
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
                                          <img src="../../../assets/images/user/03.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                          <div class="media-body ml-3">
                                             <p class="mb-0">Melina Martin</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>12/09/2020
                                    </td>
                                    <td>
                                       32 yrs
                                    </td>
                                    <td>
                                       Typhoid
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
                                       <img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image">
                                    </td>
                                    <td>
                                       <span class="badge badge-danger">Discharge</span>
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
                                    <td>18/08/2020
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
                                       <img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image">
                                    </td>
                                    <td>
                                       <span class="badge badge-success">Admit</span>
                                    </td>
                                 </tr>
                                 <tr>
                                    <td>
                                       <div class="media align-items-center">
                                          <img src="../../../assets/images/user/08.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                          <div class="media-body ml-3">
                                             <p class="mb-0">Kusti Franti</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>24/09/2020
                                    </td>
                                    <td>
                                       30 yrs
                                    </td>
                                    <td>
                                       Migraine
                                    </td>
                                    <td>
                                       Dr. Bob
                                    </td>
                                    <td>
                                       <div class="iq-progress-bar-linear d-inline-block w-80">
                                          <Progressbar :value="65" color="primary"/>
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
                                          <img src="../../../assets/images/user/03.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                          <div class="media-body ml-3">
                                             <p class="mb-0">Jules Boutin</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>28/07/2020
                                    </td>
                                    <td>
                                      42 yrs
                                    </td>
                                    <td>
                                       Covid-19
                                    </td>
                                    <td>
                                       Dr. peter
                                    </td>
                                    <td>
                                       <div class="iq-progress-bar-linear d-inline-block w-80">
                                         <Progressbar :value="40" color="primary"/>
                                       </div>
                                    </td>
                                    <td>
                                       <img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image">
                                    </td>
                                    <td>
                                       <span class="badge badge-danger">Discharge</span>
                                    </td>
                                 </tr>
                                 <tr>
                                    <td>
                                       <div class="media align-items-center">
                                          <img src="../../../assets/images/user/07.jpg" class="img-fluid avatar-35 rounded" alt="image">
                                          <div class="media-body ml-3">
                                             <p class="mb-0">Greta Life</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>8/10/2020
                                    </td>
                                    <td>
                                       28 yrs
                                    </td>
                                    <td>
                                       Dengue
                                    </td>
                                    <td>
                                       Dr. Anna
                                    </td>
                                    <td>
                                       <div class="iq-progress-bar-linear d-inline-block w-80">
                                          <Progressbar :value="95" color="primary"/>
                                       </div>
                                    </td>
                                    <td>
                                       <img src="../../../assets/images/icon/pdf.png" class="img-fliud" alt="image">
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
      </tab-content-item>
        </tab-content>
   
    
  </div>
</template>
<script>
import { core } from '../../../config/pluginInit'
import ApexChart from '../../../components/charts/ApexChart'
import { english } from 'flatpickr/dist/l10n/default'
import MorrisChart from '../../../components/charts/MorrisChart'

export default {
  name:"DefaultDashboard",
  components:{
    ApexChart,
    MorrisChart
  },
  mounted () {
      core.fullscreen()
  
  },
  data () {
    return{
       chart1:{
          series: [{
      name: 'Successful deals',
      data: [60, 40, 50, 80, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 55, 28, 60, 30, 80, 30]
    }],
    colors: ["#fe721c", "#876cfe"],
    chart: {
      height: 320,
      type: 'area',
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
      chart2:{
          series: [{
      name: 'Revenue',
      data: [76, 85, 101, 98, 87, 105, 91]
    }, {
        name: 'Net Profit',
        data: [44, 55, 57, 56, 61, 58, 63]
      }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#fe721c'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      labels:{
        minHeight: 30,
        maxHeight: 30,
      }
    },
    yaxis: {
      title: {
        
      },
      labels: {
        offsetY: 0,
        minWidth: 15,
        maxWidth: 15,
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
      chart3:{
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
      height: 280,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    options: {
      legend: {
        markers: {
          radius: 12,
        }
      }
    },
    
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0,
         
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
      labels: {
          minHeight: 22,
          maxHeight: 40,
       }
    },
    yaxis: {
      labels: {
          
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
        }
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
      config: {
        dateFormat: 'Y-m-d',
        inline: true,
        locale: english
      },
       chart4:{
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
      chart5:{
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
      chart6:{
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
      chart7:{
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
     chart8:{
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
      chart9:{
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
      chart10:{
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
     },
     chart11:{
        series: [{
      name: "series1",
      data: [80, 5, 4, 35, 57, 55, 80]
    }, {
      name: 'series2',
      data: [160, 115, 124, 40, 20, 48, 28]
    },
    {
      name: 'series3',
      data: [45, 25, 80, 110, 70, 25, 30]
    }],
    colors: ['#876CFE', '#FE721C', '#37E6B0'],
    chart: {
      height: 250,
      type: 'line',
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'],
        opacity: 0
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      labels: {
        minHeight: 22,
        maxHeight: 19
      }
    },
    yaxis: {
      labels: {

        minWidth: 15,
        maxWidth: 15
      }
    },
    legend: {
      show: false
    }
     },
       chart12:{
        series: [{
      data: [75, 60, 20, 45]
    }],
    chart: {
      height: 350,
      type: 'bar',
      events: {
      },
      sparkline: {
        enabled: false,
      }
    },
    colors: ["#876CFE", "#FF4B4B", "#4788FF", "#FE721C"],
    plotOptions: {
      bar: {
        columnWidth: '45%',
        distributed: true
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    xaxis: {
      categories: [
        ['Cancelled'],
        ['Pending'],
        ['Completed'],
        ['Upcoming'],
      ],
      labels: {
        minHeight: 23,
        maxHeight: 23
      }
    },
    yaxis: {
      labels: {
        
        minWidth: 15,
        maxWidth: 15
      }
    }
     },
       chart13:{
        series: [{
      name: 'Operation',
      data: [60, 55, 41, 37, 22, 43, 21]
    }, {
      name: 'Visit',
      data: [40, 32, 33, 52, 13, 43, 32]
    }],
    chart: {
      type: 'bar',
      height: 290,
      stacked: true
    },
    plotOptions: {
      bar: {
        horizontal: true,
      },
    },
    stroke: {
      width: 1,
      colors: ['#fff']
    },
    colors: ["#FE721C", "#FFEDE6"],
    xaxis: {
      categories: ['United States', 'Russia', 'Ukraine', 'India', 'China', 'Canada'],
      labels: {
        formatter: function (val) {
          return val + "K"
        },
        show: false,
        minHeight: 0,
        maxHeight: 0
      },
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      }
    },
    dataLabels: {
      enabled: false
    },
    yaxis: {
     
      show: false,
      labels: {
        minWidth: 0,
        maxWidth: 0
      }
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return val + "K"
        }
      }
    },
    fill: {
      opacity: 1
    },
    legend: {
      show: true,
      position: 'top',
      horizontalAlign: 'left'
    }
     },
      chart14:{
        series: [75],
    chart: {
      height: 280,
      type: 'radialBar',
    },
    stroke: {
      lineCap: "round",
    },
    colors: ["#4788FF"],
    labels: [''],
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 15,
          size: "60%"
        },
        dataLabels: {
          showOn: "always",
          name: {
            show: false,

          },
          value: {
            color: "#4788FF",
            fontSize: "35px",
            show: true,
           
          }
        }
      }
    },
    responsive: [{      
      breakpoint: 992,
      options: {
        chart: {
          height: 280
        }
      }
    }]
     },
     chart15:{
        series: [{
      name: 'Success',
      data: [28, 55, 60, 100, 55, 57, 98]
    }, {
      name: 'Failed',
      data: [25, 22, 17, 40, 16, 18, 36]
    }],
    chart: {
      height: 280,
      type: 'area'
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    colors: ['#FF5151', '#37E6B0'],
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      labels: {
        minHeight: 20,
        maxHeight: 15
      }
    },
    yaxis: {
      labels: {

        minWidth: 15,
        maxWidth: 15
      }

    },
    legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -35
    }
     },
      chart16:{
        series: [{
      name: 'New Patient',
      data: [75, 50, 60, 70, 40, 87, 40]
    }, {
      name: 'Exit Patient',
      data: [35, 23, 25, 35, 23, 37, 23]
    }, {
      name: 'ICU Patient',
      data: [20, 15, 18, 20, 15, 23, 15]
    }, {
      name: 'OPD Patient',
      data: [30, 30, 35, 35, 35, 26, 30]
    }, {
      name: 'Discharge Patient',
      data: [25, 25, 25, 25, 25, 28, 25]
    }],
    colors: ['#876CFE', '#FE721C', '#37E6B0', '#FF5151', '#4788FF'],
    chart: {
      type: 'bar',
      height: 265,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    stroke: {
      lineCap: "round",
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
        columnWidth: '20%'
      },
    },
    xaxis: {
      type: 'category',
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
       labels: {
         minHeight: 22,
         maxHeight:19
      }
    },
    yaxis: {
      labels: {

        minWidth: 18,
        maxWidth: 18
      }
    },
    legend: {
      show: false
      

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
     },
     chart17:{
          series: [{
          name: "Desktops",
          data: [5, 8, 6, 15, 10, 15, 10,6,5]
      }],
      colors: ['#876cfe'],
        chart: {
        height: 60,
        width: 100,
        type: 'line',
        zoom: {
          enabled: false
        },
        sparkline: {
        enabled: true,
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
    
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      }
     },
     chart18:{
           series: [{
       name: 'Net Profit',
       data: [50, 35, 45, 80, 65]
     }, {
       name: 'Revenue',
       data: [76, 85, 101, 98, 70]
     }],
     colors: ["#c9dcff", "#4788ff"],
       chart: {
       type: 'bar',
       height: 60,
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
         columnWidth: '45%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 1,
       colors: ['transparent']
     },
     xaxis: {
       categories: ['02:30', '02:45', '03:00', '03:15'],
     },
     yaxis: {
       title: {
         text: ''
       },
       labels: {
       offsetX: 0,
       offsetY: 0
     },
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
     chart19:{
         series: [{
          name: "Desktops",
          data: [5, 8, 6, 15, 10, 15, 10,6,5]
      }],
      colors: ['#37e6b0'],
        chart: {
        height: 60,
        width: 100,
        type: 'line',
        zoom: {
          enabled: false
        },
        sparkline: {
        enabled: true,
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
    
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      }
     },
     chart20:{
           series: [{
       name: 'Net Profit',
       data: [50, 35, 45, 80, 65]
     }, {
       name: 'Revenue',
       data: [76, 85, 101, 98, 70]
     }],
     colors: ["#dcd4ff", "#876cfe"],
       chart: {
       type: 'bar',
       height: 60,
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
         columnWidth: '45%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 1,
       colors: ['transparent']
     },
     xaxis: {
       categories: ['02:30', '02:45', '03:00', '03:15'],
     },
     yaxis: {
       title: {
         text: ''
       },
       labels: {
       offsetX: 0,
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
     }
     },
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
      chart21:{
        series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#ffffff", "#ffecec"],
    chart: {
      type: 'bar',
      height: 90,
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
      categories: ['02:30', '02:45', '03:00', '03:15'],
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
    }   
      },
      chart22:{
           series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#e2fcf4", "#49f0d3"],
    chart: {
      type: 'bar',
      height: 90,
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
      categories: ['02:30', '02:45', '03:00', '03:15'],
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
    }
      },
      chart23:{
  series: [{
           name: "Hair Style",
           data: [
           [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 25], [10.9, 23]]
         },{
           name: "Makeup",
           data: [
           [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 24]]
         },{
           name: "Spa",
           data: [
           [21.7, 4], [23.6, 3.6], [24.6, 8], [29.9, 6], [21.7, 25], [23, 9], [10.9, 28]]
         }],
         colors: ["#ff4b4b","#fe721c","#37e6b0"],
           chart: {
           height: 275,
           type: 'scatter',
           zoom: {
             enabled: true,
             type: 'xy'
           }
         },
         legend: {
           offsetY: -10,
         },
         xaxis: {
           tickAmount: 10,
           labels: {
             formatter: function(val) {
               return parseFloat(val).toFixed(1)
             }          
           }
         },
         yaxis: {
           tickAmount: 7,
           labels: {
          offsetY: 0,
          minWidth: 25,
          maxWidth: 25,
          }
         }
      },
      chart24:{
          series: [{
          name: 'Weekly',
          data: [53, 55, 45, 40, 40, 28, 35, 25, 20, 12, 25, 24,20,13,8]
       }, {
          name: 'Monthly',
          data: [63, 62, 52, 72, 55, 80, 70, 50, 60, 40, 50, 41,38, 32, 18]
       }, {
          name: 'Yearly',
          data: [150, 135, 144, 115, 120, 114, 133, 124, 100, 94, 96, 90, 82, 76, 86]
       }],
       colors: ['#FF4B4B', '#4788FF', '#37E6B0' ],
       chart: {
          type: 'bar',
          height: 280,
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
          show:false
       },
       yaxis: {
          show:false
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
      item1:{
         type:"donut",
         id:"salon2-chart-08",
         colors: ["#876cfe", "#fe721c"],
         resize: true,
         hideHover: "auto",
         bodyData: [
             {label: "Female", value: 30},
             {label: "Male", value: 20}
         ],
          
      },
      option: {
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