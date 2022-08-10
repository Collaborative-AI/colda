<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="12">
               <div class="iq-card">
                  <div class="iq-card-header d-flex justify-content-between">
                     <div class="iq-header-title">
                        <h4 class="card-title">Simple Wizard</h4>
                     </div>
                  </div>
                  <div class="iq-card-body">
                     <form id="form-wizard1" class="text-center mt-4">
                        <ul id="top-tab-list" class="p-0">
                           <li :class="checkActive(0, 1)" @click="changeTab(1)" id="account">
                              <a href="javascript:void(0);">
                              <i class="ri-lock-unlock-line"></i><span>Account</span>
                              </a>
                           </li>
                           <li :class="checkActive(1, 2)" @click="changeTab(2)" id="personal">
                              <a href="javascript:void(0);">
                              <i class="ri-user-fill"></i><span>Personal</span>
                              </a>
                           </li>
                           <li :class="checkActive(2, 3)" @click="changeTab(3)" id="payment">
                              <a href="javascript:void(0);">
                              <i class="ri-camera-fill"></i><span>Image</span>
                              </a>
                           </li>
                           <li :class="checkActive(3, 4)" @click="changeTab(4)" id="confirm">
                              <a href="javascript:void(0);">
                              <i class="ri-check-fill"></i><span>Finish</span>
                              </a>
                           </li>
                        </ul>
                        <!-- fieldsets -->
                        <fieldset :class="current == 1 ? 'd-block' : 'd-none'">
                           <div class="form-card text-left">
                              <b-row>
                                 <div class="col-7">
                                    <h3 class="mb-4">Account Information:</h3>
                                 </div>
                                 <div class="col-5">
                                    <h2 class="steps">Step 1 - 4</h2>
                                 </div>
                              </b-row>
                              <b-row>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Email: *</label>
                                       <input type="email" class="form-control" name="email" placeholder="Email Id" />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Username: *</label>
                                       <input type="text" class="form-control" name="uname" placeholder="UserName" />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Password: *</label>
                                       <input type="password" class="form-control" name="pwd" placeholder="Password" />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Confirm Password: *</label>
                                       <input type="password" class="form-control" name="cpwd" placeholder="Confirm Password" />
                                    </div>
                                 </b-col>
                              </b-row>
                           </div>
                           <button type="button" name="next" @click="changeTab(2)" class="btn btn-primary next action-button float-right" value="Next" >Next</button>
                        </fieldset>
                        <fieldset :class="current == 2 ? 'd-block' : 'd-none'">
                           <div class="form-card text-left">
                              <b-row>
                                 <div class="col-7">
                                    <h3 class="mb-4">Personal Information:</h3>
                                 </div>
                                 <div class="col-5">
                                    <h2 class="steps">Step 2 - 4</h2>
                                 </div>
                              </b-row>
                              <b-row>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>First Name: *</label>
                                       <input type="text" class="form-control" name="fname" placeholder="First Name" />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Last Name: *</label>
                                       <input type="text" class="form-control" name="lname" placeholder="Last Name" />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Contact No.: *</label>
                                       <input type="text" class="form-control" name="phno" placeholder="Contact No." />
                                    </div>
                                 </b-col>
                                 <b-col md="6">
                                    <div class="form-group">
                                       <label>Alternate Contact No.: *</label>
                                       <input type="text" class="form-control" name="phno_2" placeholder="Alternate Contact No." />
                                    </div>
                                 </b-col>
                              </b-row>
                           </div>
                           <button type="button" name="next" @click="changeTab(3)" class="btn btn-primary next action-button float-right" value="Next" >Next</button>
                           <button type="button" name="previous" @click="changeTab(1)" class="btn btn-dark previous action-button-previous float-right mr-3" value="Previous" >Previous</button>
                        </fieldset>
                        <fieldset :class="current == 3 ? 'd-block' : 'd-none'">
                           <div class="form-card text-left">
                              <b-row>
                                 <div class="col-7">
                                    <h3 class="mb-4">Image Upload:</h3>
                                 </div>
                                 <div class="col-5">
                                    <h2 class="steps">Step 3 - 4</h2>
                                 </div>
                              </b-row>
                              <div class="form-group">
                                 <label>Upload Your Photo:</label>
                                 <input type="file" class="form-control" name="pic" accept="image/*">
                              </div>
                              <div class="form-group">
                                 <label>Upload Signature Photo:</label>
                                 <input type="file" class="form-control" name="pic-2" accept="image/*">
                              </div>
                           </div>
                           <button type="button" name="next" @click="changeTab(4)" class="btn btn-primary next action-button float-right" value="Submit" >Submit</button>
                           <button type="button" name="previous" @click="changeTab(2)" class="btn btn-dark previous action-button-previous float-right mr-3" value="Previous" >Previous</button>
                        </fieldset>
                        <fieldset :class="current == 4 ? 'd-block' : 'd-none'">
                           <div class="form-card">
                              <b-row>
                                 <div class="col-7">
                                    <h3 class="mb-4 text-left">Finish:</h3>
                                 </div>
                                 <div class="col-5">
                                    <h2 class="steps">Step 4 - 4</h2>
                                 </div>
                              </b-row>
                              <br><br>
                              <h2 class="text-success text-center"><strong>SUCCESS !</strong></h2>
                              <br>
                              <div class="row justify-content-center">
                                 <div class="col-3"> <img src="../../../../assets/images/page-img/img-success.png" class="fit-image" alt="fit-image"> </div>
                              </div>
                              <br><br>
                              <div class="row justify-content-center">
                                 <div class="col-7 text-center">
                                    <h5 class="purple-text text-center">You Have Successfully Signed Up</h5>
                                 </div>
                              </div>
                           </div>
                        </fieldset>
                     </form>
                  </div>
               </div>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Simple',
    data () {
       return {
          current: 1
       }
    },
    methods: {
       changeTab(tab) {
          this.current = tab
          window.scrollTo({ top: 0, behavior: 'smooth' });
       },
       checkActive(item,active){
          let className = '';
          if (this.current > item) {
             className = 'active'
          }
          if(this.current > active) {
             className = className + ' done'
          }
          return className
       }
    }
}
</script>