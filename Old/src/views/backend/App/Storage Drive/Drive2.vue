<template>
 <div class="container-fluid">
         <b-row >
            <b-col lg="9" md="8" >
               <card class=" card-transparent" headerClass=" pl-0 pr-0  border-none iq-view" >
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Quick Access</h4>
                 </template>
                      <template v-slot:headerAction>
                        <p class="mb-0 text-primary"><a href="javascript:void(0);">See more <i class="las la-angle-right"></i></a></p>
                      </template>
                  <b-row>
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="iq-thumb">
                                 <a href="javascript:void(0);">
                                    <img src="../../../../assets/images/idrive-app/quick-access/01.jpg"
                                       class="img-border-radius img-fluid w-100" alt="">
                                 </a>
                              </div>
                              <div class="d-flex justify-content-between align-items-center mt-3 mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-primary-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                    <h6 class="font-weight-600 mb-0">color.jpg</h6>
                                 </div>
                                 <div class="iq-media-group d-flex">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="iq-thumb">
                                 <a href="javascript:void(0);">
                                    <img src="../../../../assets/images/idrive-app/quick-access/02.jpg"
                                       class="img-border-radius img-fluid w-100" alt="">
                                 </a>
                              </div>
                              <div class="d-flex justify-content-between align-items-center mt-3 mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-warning-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                    <h6 class="font-weight-600 mb-0">color.jpg</h6>
                                 </div>
                                 <div class="iq-media-group d-flex align-items-center">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class="mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="iq-thumb">
                                 <a href="javascript:void(0);">
                                    <img src="../../../../assets/images/idrive-app/quick-access/03.jpg"
                                       class="img-border-radius img-fluid w-100" alt="">
                                 </a>
                              </div>
                              <div class="d-flex justify-content-between align-items-center mt-3 mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-danger-light  bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                    <h6 class="font-weight-600 mb-0">color.jpg</h6>
                                 </div>
                                 <div class="iq-media-group d-flex align-items-center">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                     <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class="mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="iq-thumb">
                                 <a href="javascript:void(0);">
                                    <img src="../../../../assets/images/idrive-app/quick-access/04.jpg"
                                       class="img-border-radius img-fluid w-100" alt="">
                                 </a>
                              </div>
                              <div class="d-flex justify-content-between align-items-center mt-3 mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-success-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                    <h6 class="font-weight-600 mb-0">color.jpg</h6>
                                 </div>
                                 <div class="iq-media-group d-flex align-items-center">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                   <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                  </b-row>
               </card>
               <card class=" card-transparent" headerClass="pl-0 pr-0 border-none iq-view">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Folders</h4>
                  </template>
                    <template v-slot:headerAction>
                        <span class="mb-0 text-primary"><a href="latest.html">See more <i class="las la-angle-right"></i></a></span>
                     </template>
                  <b-row class=" mb-0">
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                          <template v-slot:body>
                              <div class="d-flex justify-content-between align-items-center mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-primary-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                 </div>
                                 <div class="iq-media-group d-flex">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <h5>Online Classes</h5>
                              <p>24 Files</p>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                 <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                          </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="d-flex justify-content-between align-items-center mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-success-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                 </div>
                                 <div class="iq-media-group d-flex">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <h5>Online Classes</h5>
                              <p>24 Files</p>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                 <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                          <template v-slot:body>
                              <div class="d-flex justify-content-between align-items-center mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-warning-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                 </div>
                                 <div class="iq-media-group d-flex">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <h5>Online Classes</h5>
                              <p>24 Files</p>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                 <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                          </template>
                        </card>
                     </b-col>
                     <b-col xl="3" lg="6" md="6" class=" mb-lg-0 mb-4">
                        <card class=" mb-0">
                           <template v-slot:body>
                              <div class="d-flex justify-content-between align-items-center mb-3">
                                 <div class="d-flex align-items-center">
                                    <div class="bg-danger-light bg-box-color mr-2">
                                       <i class="ri-gallery-fill"></i>
                                    </div>
                                 </div>
                                 <div class="iq-media-group d-flex">
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="">
                                    </a>
                                    <a href="#" class="iq-media">
                                       <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg" alt="">
                                    </a>
                                 </div>
                              </div>
                              <h5>Online Classes</h5>
                              <p>24 Files</p>
                              <hr>
                              <div class="d-flex align-items-center justify-content-between iq-social-icon">
                                 <ul class="list-unstyled d-flex mb-0">
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-share-fill iq-icone mr-3"></i>
                                       </a>
                                    </li>
                                    <li><a href="javascript:void(0);">
                                          <i class="ri-star-fill mr-3"></i>
                                       </a>
                                    </li>
                                    <li>
                                       <a href="javascript:void(0);">
                                          <i class="ri-download-fill mr-3"></i>
                                       </a>
                                    </li>
                                 </ul>
                                  <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class=""><i class="ri-more-2-fill"></i></span>
                          </template>
                          <b-dropdown-item>{{ ('Copy Link') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Make a Copy') }}</b-dropdown-item>
                          <b-dropdown-item>{{ ('Rename') }}</b-dropdown-item>
                        </b-dropdown>      
                              </div>
                           </template>
                        </card>
                     </b-col>
                  </b-row>
               </card>
               <card  headerClass="border-none iq-view" >
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Files</h4>
                   </template>
                     <template v-slot:headerAction>
                        <p class="mb-0 text-primary"><a href="music-latest.html">See more <i class="las la-angle-right"></i></a></p>
                     </template>
      
                  <template v-slot:body>
                     <div class="">
                        <table class="data-tables table table-borderless" style="width:100%">
                           <thead>
                              <tr>
                                 <th style="width:30%;">Name</th>
                                 <th style="width:30%;">Owner</th>
                                 <th style="width:20%;">Last Modified</th>
                                 <th style="width:15%;">File Size</th>
                                 <th style="width:5%;"></th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-primary-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-primary"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                             <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton5"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-warning-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-warning"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                              <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton6"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-info-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-info"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                 
                                       <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton7"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                    
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-danger-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-danger"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                            <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                           <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton8"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-success-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-success"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                     <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                           <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton9"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-primary-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-primary"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                     <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                          <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton10"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <div class="media align-items-center">
                                       <div class="iq-movie">
                                          <a href="javascript:void(0);">
                                             <div class="bg-warning-light bg-box-color mr-2">
                                                <i class="ri-gallery-fill text-warning"></i>
                                             </div>
                                          </a>
                                       </div>
                                       <div class="media-body text-white text-left ml-3">
                                          <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                       </div>
                                    </div>
                                 </td>
                                 <td>
                                    <div class="iq-media-group d-flex align-items-center justify-content-center">
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/05.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/06.jpg"
                                             alt="">
                                       </a>
                                       <a href="#" class="iq-media">
                                          <img class="img-fluid avatar-24 rounded-circle" src="../../../../assets/images/user/07.jpg"
                                             alt="">
                                       </a>
                                    </div>
                                 </td>
                                 <td>
                                    <p class="mb-0">July 22, 2020</p>
                                 </td>
                                 <td>
                                    <p class="mb-0">20.05 mb</p>
                                 </td>
                                 <td>
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                          <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton11"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                 </td>
                                 </tr>
                                 <tr>
                                    <td>
                                       <div class="media align-items-center">
                                          <div class="iq-movie">
                                             <a href="javascript:void(0);">
                                                <div class="bg-info-light bg-box-color mr-2">
                                                   <i class="ri-gallery-fill text-info"></i>
                                                </div>
                                             </a>
                                          </div>
                                          <div class="media-body text-white text-left ml-3">
                                             <h6 class="font-weight-600 mb-0">lorem.jpg</h6>
                                          </div>
                                       </div>
                                    </td>
                                    <td>
                                       <div class="iq-media-group d-flex align-items-center justify-content-center">
                                          <a href="#" class="iq-media">
                                             <img class="img-fluid avatar-24 rounded-circle"
                                                src="../../../../assets/images/user/05.jpg" alt="">
                                          </a>
                                          <a href="#" class="iq-media">
                                             <img class="img-fluid avatar-24 rounded-circle"
                                                src="../../../../assets/images/user/06.jpg" alt="">
                                          </a>
                                          <a href="#" class="iq-media">
                                             <img class="img-fluid avatar-24 rounded-circle"
                                                src="../../../../assets/images/user/07.jpg" alt="">
                                          </a>
                                       </div>
                                    </td>
                                    <td>
                                       <p class="mb-0">July 22, 2020</p>
                                    </td>
                                    <td>
                                       <p class="mb-0">20.05 mb</p>
                                    </td>
                                    <td>
                                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                          <span class="dropdown-toggle text-primary drop-idrive" id="dropdownMenuButton12"
                                          data-toggle="dropdown" aria-expanded="false" role="button">
                                          <i class="ri-more-2-fill text-primary"></i>
                                       </span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                        </b-dropdown>
                                    </td>
                                 </tr>
                           </tbody>
                        </table>
                     </div>
                  </template>
               </card>
            </b-col>
            <b-col lg="3" md="4" >
               <card  headerClass="border-none pb-0">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Activity</h4>
                  </template>>
                  <template v-slot:body>
                     <div class="list-unstyled mb-0">
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media  mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/01.png"
                                 class="img-fluid mr-3 avatar-40 iq-activity-image iq-primary" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/02.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                        </div>
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/03.png"
                                 class=" img-fluid mr-3 avatar-40 iq-danger  iq-activity-image" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/04.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                           <div class="d-flex justify-content-between align-items-center mt-2">
                              <div class="d-flex align-items-center">
                                 <img src="../../../../assets/images/idrive-app/activity/1.png" class=" img-fluid mr-3 avatar-24"
                                    alt="">
                                 <h6>john deo</h6>
                              </div>
                              <span>Can edit</span>
                           </div>
                        </div>
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/05.png"
                                 class=" img-fluid mr-3 avatar-40 iq-activity-image iq-warning" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/06.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                        </div>
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/07.png"
                                 class=" img-fluid mr-3 avatar-40 iq-activity-image iq-success" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/08.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                        </div>
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/09.png"
                                 class=" iq-activity-image img-fluid mr-3 avatar-40" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/10.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                           <div class="d-flex justify-content-between align-items-center mt-2">
                              <div class="d-flex align-items-center">
                                 <img src="../../../../assets/images/idrive-app/activity/2.png" class=" img-fluid mr-3 avatar-24"
                                    alt="">
                                 <h6>Carolina Tensen</h6>
                              </div>
                              <span>Can edit</span>
                           </div>
                        </div>
                        <div class="mb-4">
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/11.png"
                                 class=" img-fluid mr-3 avatar-40 iq-activity-image iq-success" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/12.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                        </div>
                        <div>
                           <div class="iq-acivity">
                              <span>Sat 08:26 pm</span>
                           </div>
                           <div class="media mt-2">
                              <img src="../../../../assets/images/idrive-app/activity/13.png"
                                 class=" iq-activity-image img-fluid mr-3 avatar-40" alt="">
                              <div class="media-body">
                                 <p class=" mb-2 mt-0"><strong class="text-black">You</strong> Permanently Deleted an item</p>
                                 <img src="../../../../assets/images/idrive-app/activity/14.png" class=" img-fluid mr-3  avatar-24"
                                    alt="">
                                 <p class="mt-2 mb-0">Rp Assignment</p>
                              </div>
                           </div>
                           <div class="d-flex justify-content-between align-items-center mt-2">
                              <div class="d-flex align-items-center">
                                 <img src="../../../../assets/images/idrive-app/activity/3.png" class=" img-fluid mr-3 avatar-24"
                                    alt="">
                                 <h6>Anna Mull</h6>
                              </div>
                              <span>Can edit</span>
                           </div>
                        </div>
                     </div>
                  </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
import { core } from '../../../../config/pluginInit'
export default {
  name:'Drive2',
   mounted () {
   core.index()
   core.initDataTable()
   },
  
}
</script>
