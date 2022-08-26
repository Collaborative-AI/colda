<template>
     <div class="container-fluid crm2">
      <b-row>
         <b-col lg="8" md="6" >
            <card class=" card-block card-stretch card-height">
               <template v-slot:body>
                  <div class="d-flex justify-content-between flex-wrap">
                     <div class="d-flex align-items-center">
                        <div class="media mr-4 mb-4">
                           <div class="crm-profile-img-edit">
                              <img class="crm-profile-pic rounded-circle avatar-100" src="../../../../assets/images/user/11.png"
                                 alt="profile-pic">
                              <div class="crm-p-image bg-primary">
                                 <i class="las la-link upload-button"></i>
                                 <input class="file-upload" type="file" accept="image/*">
                              </div>
                           </div>
                        </div>
                        <div class="media-support-info">
                           <h4 class="mb-2">Jonathan Doe</h4>
                           <div class="d-flex align-items-center crm-social">
                              <span class="mb-0 text-primary mr-2">Sales Manager <i
                                    class="fa fa-circle pro-font line-height ml-1" aria-hidden="true"></i> </span> <span
                                 class="mb-0 text-danger"> Globex Corporation </span>
                           </div>
                           <p class="mb-0 mt-2"><i class="las la-map-marker"></i> Haritsow, New York, USA</p>
                        </div>
                     </div>
                     <div class=" d-flex mb-3">
                        <a href="#" class="c-icon bg-primary">
                           <i class="ri-facebook-fill"></i>
                        </a>
                        <a href="#" class="c-icon bg-danger">
                           <i class="lab la-pinterest-p"></i>
                        </a>
                        <a href="#" class="c-icon bg-primary">
                           <i class="lab la-twitter"></i>
                        </a>
                     </div>
                  </div>
                  <div class="d-flex align-items-center mb-3">
                     <h4 class="mr-3">Tags:</h4>
                     <a href="javascript:void(0)" class="btn  bg-primary-light mr-2">
                        Lead
                     </a>
                     <a href="javascript:void(0)" class="btn  bg-danger-light mr-2">
                        Tasks
                     </a>
                  </div>
                  <hr>
                  <div class="row mt-4">
                     <div class="col-lg-6">
                        <ul class="list-unstyled mb-0">
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Email:</b></span>
                              <span class="col-md-7">jonathan485@gmail.com</span>
                           </li>
                           <li class=" row mb-2">
                              <span class="col-md-5"><b>Work:</b></span>
                              <span class="col-md-7">(368) 493-2360</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Unqualified reason:</b></span>
                              <span class="col-md-7">Not Available</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Territory:</b></span>
                              <span class="col-md-7">Not Available</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Other phone no.</b></span>
                              <span class="col-md-7">+880 185 645 1554</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Zipcode:</b></span>
                              <span class="col-md-7">100652</span>
                           </li>
                        </ul>
                     </div>
                     <div class="col-lg-6">
                        <ul class="list-unstyled mb-0">
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Mobile:</b></span>
                              <span class="col-md-7">+880 178 712 3195</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Sales Owner:</b></span>
                              <span class="col-md-7">Denliver Tarison</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Subscription status:</b></span>
                              <span class="col-md-7">Subscribed</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Time zone:</b></span>
                              <span class="col-md-7">(GMT-07:00) New York</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Address:</b></span>
                              <span class="col-md-7">604-5854 Beckford St.</span>
                           </li>
                           <li class="row mb-2">
                              <span class="col-md-5"><b>Company address:</b></span>
                              <span class="col-md-7">160-6802 Aliquet Rd.</span>
                           </li>
                        </ul>
                     </div>
                  </div>
               </template>
            </card>
         </b-col>
         <b-col lg="4" md="6" >
            <b-row >
               <b-col lg="12" >
                  <card class=" card-block card-stretch card-height">
                     <template v-slot:headerTitle>
                           <h4 class="card-title">Convert this link into a contact?</h4>
                     </template>
                     <template v-slot:body>
                        <div class="d-flex">
                           <a href="" class="btn btn-primary mr-3">Convert</a>
                           <div class="input-group card-header-toolbar">
                              <div class="input-group-append">
                                 <button type="button" class="btn btn-outline-primary">Add task</button>
                                 <button type="button" class="btn btn-outline-primary m-0 p-0">
                                    <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                      <i class="las la-angle-down"></i>
                               </template>
                             <b-dropdown-item>{{ ('Action') }}</b-dropdown-item>
                             <b-dropdown-item>{{ ('Another action') }}</b-dropdown-item>
                             <b-dropdown-item>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item>{{ ('Something else here') }}</b-dropdown-item>
                             <div role="separator" class="dropdown-divider"></div>
                              <b-dropdown-item>{{ ('Separated link') }}</b-dropdown-item>
                         </b-dropdown>
                                 </button>
                               
                              </div>
                           </div>
                        </div>
                     </template>
                  </card>
               </b-col>
               <b-col lg="12" >
                  <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                           <h4 class="card-title">Notes</h4>
                    </template>
                    <template v-slot:body>
                        <fieldset class="form-group">
                           <textarea class="form-control" id="basicTextarea" rows="3"
                              placeholder="Type here..."></textarea>
                        </fieldset>
                        <h6 class="mb-2"><i class="las la-file-alt mr-1 text-primary"></i> Expressed interest in purchasing
                           the product and require...</h6>
                        <span class="ic-25 bg-info-light rounded-circle d-inline-block mr-1 mb-0">F</span><span
                           class="mb-0">Faysal Rabby</span>
                    </template>
                  </card>
               </b-col>
            </b-row>
         </b-col>
      </b-row>
      <b-row >
         <b-col lg="8" md="6" >
            <b-row >
               <b-col lg="12" >
                  <card class=" card-block card-stretch card-height" headerClass="align-items-center"> 
                      <template v-slot:headerTitle>
                           <h4 class="card-title mb-1">Last Stage Changed</h4>
                           <p class="mb-0">10 Days ago</p>
                      </template>
                        <template v-slot:headerAction>
                           <h4 class="mb-1">Last Contacted</h4>
                           <span>10 Days ago</span>
                        </template>
                     <template v-slot:body>
                        <ul class="list-unstyled list-content">
                           <li><span class="badge bg-primary-light text-primary">New<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-warning-light text-warning">Contacted<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-success-light text-success">Interested<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-info-light text-info">Under Review<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-danger-light text-danger">Demo<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-primary-light text-dark">Converted<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-success-light text-success">Qualified<i class="las la-angle-right mr-1"></i></span></li>
                           <li><span class="badge bg-info-light text-info">Selected<i class="las la-angle-right mr-1"></i></span></li>
                        </ul>
                     </template>
                  </card>
               </b-col>
                <b-col lg="12" >
                  <card class=" card-block card-stretch card-height" headerClass="align-items-center">
                     <template v-slot:headerTitle>
                           <h4 class="card-title mb-1">Recent Conversations</h4>
                           <p class="mb-0">10 Days ago</p>
                         </template>
                    <template v-slot:body>
                        <div class="table-responsive">
                           <table class="table mb-0 table-borderless">
                              <tbody>
                                 <tr>
                                    <td>
                                       <div class="d-flex align-items-center">
                                          <div class="iq-avatar position-relative rec-dots">
                                             <img class="avatar-40 rounded-circle" src="../../../../assets/images/user/1.jpg"
                                                alt="#" data-original-title="" title=""> <span
                                                class="bg-success dots"></span>
                                          </div>
                                          <div class="media-support-info ml-3">
                                             <h5>Jonathan Swifte</h5>
                                             <p class="mb-0 text-success">Active now</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td><span class="text-danger">[Draft]</span> Re: (Sample) Re: Require a demo? <span
                                          class="text-primary">(3)</span></td>
                                    <td>
                                       <div class="dropdown">
                                          <span>
                                             <i class="ri-more-2-fill"></i>
                                          </span>                                         
                                       </div>
                                    </td>
                                 </tr>
                                 <tr>
                                    <td>
                                       <div class="d-flex align-items-center">
                                          <div class="iq-avatar position-relative rec-dots">
                                             <img class="avatar-40 rounded-circle" src="../../../../assets/images/user/02.jpg"
                                                alt="#" data-original-title="" title=""> <span
                                                class="bg-secondary dots"></span>
                                          </div>
                                          <div class="media-support-info ml-3">
                                             <h5>Taylor Jane</h5>
                                             <p class="mb-0">15 mins ago</p>
                                          </div>
                                       </div>
                                    </td>
                                    <td>Hey, Is that project going well? Can have a overview? Let me...</td>
                                    <td>
                                       <div class="dropdown">
                                          <span>
                                             <i class="ri-more-2-fill"></i>
                                          </span>                                          
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
         </b-col>
         <b-col lg="4" md="6" >
            <card class=" card-block card-stretch card-height">
              <template v-slot:headerTitle>
                     <h4 class="card-title">Reminders</h4>
              </template>
               <template v-slot:body>
                  <img src="../../../../assets/images/crm/01.png" class="img-fluid mx-auto d-block mt-3" alt="">
                  <p class="mb-0 mt-5 text-center">No reminders found</p>
               </template>
            </card>
         </b-col>
      </b-row>
      <b-row >
         <b-col lg="8" md="6">
            <card class=" card-block card-stretch card-height" headerClass="align-items-center"> 
              <template v-slot:headerTitle>
                     <h4 class="card-title">Recent Activities</h4>
              </template>
                 <template v-slot:headerAction>
                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                       <span class="dropdown-toggle dropdown-bg bg-primary-light p-2" id="dropdownMenuButton1"
                           data-toggle="dropdown" aria-expanded="false" role="button">
                           Today<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                        </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                 </template>
                <template v-slot:body>
                  <div class="row">
                     <div class="col-lg-7">
                        <div class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-primary-light"><span><i class="las la-globe"></i></span></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Viewed Webpage - <span class="text-primary">yourcompany.com/pricing</span>
                              </h6>
                              <div class="d-flex align-items-center">
                                 <span class="mb-0 text-danger mr-2">Jane Sampton</span><i
                                    class="fa fa-circle pro-font line-height mr-2" aria-hidden="true"></i><span>17 Days
                                    ago</span>
                              </div>
                           </div>
                        </div>
                        <div class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-primary-light"><span><i class="las la-percentage"></i></span></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Viewed Webpage </h6>
                              <div class="d-flex align-items-center">
                                 <span class="mb-0 text-danger mr-2">Jane Sampton</span>
                                 <i class="fa fa-circle pro-font line-height mr-2" aria-hidden="true"></i>
                                 <span>17 Days ago</span>
                              </div>
                           </div>
                        </div>
                        <div class="d-flex mb-4 align-items-center">
                           <div class="profile-icon bg-primary-light"><span><i class="las la-user-check"></i></span></div>
                           <div class="media-support-info ml-3">
                              <h6 class="mb-1">Viewed Webpage</h6>
                              <div class="d-flex align-items-center">
                                 <span class="mb-0 text-danger mr-2">Jane Sampton</span>
                                 <i class="fa fa-circle pro-font line-height mr-2" aria-hidden="true"></i>
                                 <span>17 Days ago</span>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-lg-5">
                        <div class="card  card-score">
                           <div class="card-body text-center">
                              <h4>Score</h4>
                              <div class="profile-icon ic-score d-block mx-auto mt-2 mb-2">9</div>
                              <p class="mb-1"><span class="title-text"><b>Last seen</b></span>:17 Days ago</p>
                              <p class="mb-1"><span class="title-text"><b>Last contacted</b></span>:17 Days ago</p>
                              <p class="mb-0"><span class="title-text"><b>Last modified</b></span>:17 Days ago</p>
                           </div>
                        </div>
                     </div>
   
                  </div>
                  <div class="text-center view-crm">
                     <a href="javascript:void(0);">View all</a>
                  </div>
                </template>
            </card>
         </b-col>
         <b-col lg="4" md="6" >
            <card class=" card-block card-stretch card-height" headerClass="align-items-center">
              <template v-slot:headerTitle>
                     <h4 class="card-title">Lead Score</h4>
              </template>
                   <template v-slot:headerAction>
                      <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                      <span class="dropdown-toggle dropdown-bg bg-primary-light p-2" id="dropdownMenuButton8"
                           data-toggle="dropdown" aria-expanded="false" role="button">
                           This Week<i class="ri-arrow-down-s-line ml-1 text-primary"></i>
                        </span>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                   </template>
              
              <template v-slot:body>
                  <div class="d-flex mb-2 align-items-center">
                     <div class="profile-icon bg-primary"><span>9</span></div>
                     <div class="media-support-info ml-3">
                        <h6 class="mb-1">Doesn't meet any condition set for lead scoring</h6>
                     </div>
                  </div>
                  <div class="d-flex justify-content-between align-items-center">
                     <h6 class="text-primary">Cold</h6>
                     <p class="mb-0 mt-1 text-success"><i class="ri-arrow-right-up-line"></i> 20% Increased</p>
                  </div>
                  <h6 class="mb-2 mt-2">Top Scoring Factors</h6>
                  <p class="mb-0"><span class="text-success"><i class="las la-angle-double-up mr-2"></i></span>Created a
                     ticket</p>
                  <p class="mb-0"><span class="text-success"><i class="las la-angle-double-up mr-2"></i></span>Viewed web
                     page - yourcompany.com/pricing</p>
                  <p class="mb-0"><span class="text-success"><i class="las la-angle-double-up mr-2"></i></span>Downloaded
                     white paper</p>
                  <p class="mb-0"><span class="text-success"><i class="las la-angle-double-up mr-2"></i></span>Lead details
                     updated</p>
                  <p class="mb-0"><span class="text-success"><i class="las la-angle-double-up mr-2"></i></span>Added a use
                  </p>
              </template>
            </card>
         </b-col>
      </b-row>
      <b-row >
         <b-col lg="8" >
            <card class=" card-block card-stretch card-height">
               <template v-slot:headerTitle>
                     <h4 class="card-title">Integrations</h4>
               </template>
                <template v-slot:body>
                  <b-row >
                     <b-col lg="4" md="6"  class=" mb-lg-0 mb-3">
                        <div class="feature-list text-center">
                           <div class="profile-icon-1 bg-danger-light d-block mx-auto mb-3">
                              <img src="../../../../assets/images/crm/02.png" class="img-fluid" alt="">
                           </div>
                           <h5>Gmail</h5>
                           <p class="mb-0 mt-2 line-height">Integrate with Gmail for a two-way sync of your inbox
                              between your Freshsales and Gmail account</p>
                           <a href="javascript:void(0);" class="btn btn-danger  mt-3">Integrate</a>
                        </div>
                     </b-col>
                     <b-col lg="4" md="6" class=" mb-lg-0 mb-3">
                        <div class="feature-list text-center">
                           <div class="profile-icon-1 bg-primary-light d-block mx-auto mb-3">
                              <img src="../../../../assets/images/crm/03.png" class="img-fluid " alt="">
                           </div>
                           <h5>Google Calendar</h5>
                           <p class="mb-0 mt-2 line-height">Integrate with Gmail for a two-way sync of your inbox
                              between your Freshsales and Gmail account</p>
                           <a href="javascripe:void();" class="btn btn-primary mt-3">Integrate</a>
                        </div>
                     </b-col>
                     <b-col lg="4" md="6" class=" mb-lg-0 mb-3">
                        <div class="feature-list text-center">
                           <div class="profile-icon-1 bg-warning-light d-block mx-auto mb-3">
                              <img src="../../../../assets/images/crm/04.png" class="img-fluid " alt="">
                           </div>
                           <h5>Office365 Calendar</h5>
                           <p class="mb-0 mt-2 line-height">Integrate with Gmail for a two-way sync of your inbox
                              between your Freshsales and Gmail account</p>
                           <a href="javascript:void();" class="btn btn-warning mt-3">Integrate</a>
                        </div>
                     </b-col>
                  </b-row>
                </template>
            </card>
         </b-col>
         <b-col lg="4" >
            <card class=" card-block card-stretch card-height" headerClass="align-items-center">
              <template v-slot:headerTitle>
                     <h4 class="card-title">Contacts</h4>
              </template>
               <template v-slot:headerAction>
                  
                   <b-dropdown  id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                                 <template v-slot:button-content>
                                      <div class="bg-primary-light icon iq-icon-box-3 rounded-circle">
                       <a href="#" id="dropdownMenuReport1" data-toggle="dropdown" aria-expanded="true">
                        <i class="ri-more-2-fill font-size-20"></i>
                     </a> </div>
                               </template>
                             <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ ('view') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ ('delete') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ ('edit') }}</b-dropdown-item>
                             <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ ('print') }}</b-dropdown-item>
                              <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ ('download') }}</b-dropdown-item>
                         </b-dropdown>
                   
                         
               </template>
               <template v-slot:body>
                  <div class="d-flex justify-content-between ">
                     <div class="iq-avatar">
                        <img class="avatar-40 rounded-circle" src="../../../../assets/images/user/06.jpg" alt="#"
                           data-original-title="" title=""> <span class="bg-success iq-dots dots-80"></span>
                     </div>
                     <div class="media-support-info ml-3">
                        <h5>James Sampleton</h5>
                        <span class="mb-0">jamessampleton@gmail.com<br>
                           (473)-160-8261<br>
                           Widgetz.io (sample) <br>
                           CEO
                        </span>
                     </div>                     
                  </div>
                  <div class="mt-5">
                     <button type="button" class="btn btn-primary mb-4 col-sm-12">Send Email</button>
                  </div>
                  <div class="text-center view-crm">
                     <a href="javascript:void(0);">View all <i class="ri-arrow-down-s-line"></i></a>
                  </div>
               </template>
            </card>
         </b-col>
      </b-row>
   </div>
</template>
<script>
export default {
    name:'CrmLead'
}
</script>