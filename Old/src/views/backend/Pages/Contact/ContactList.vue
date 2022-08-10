<template>
    <div class="container-fluid">
         <b-row >
            <b-col lg="12">
               <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Contact List</h4>
                      </template>
                     <template v-slot:headerAction>
                        <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#addContact">Add New</a>
                   </template>
                 <template v-slot:body>
                     <div class="table-responsive data-table">
                        <table class="data-tables table" style="width:100%">
                           <thead>
                              <tr>
                                 <th>Profile</th>
                                 <th>Name</th>
                                 <th>Email</th>
                                 <th>Phone No.</th>
                                 <th>Action</th>
                              </tr>
                           </thead>
                           <tbody>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/01.jpg"  class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Anna Sthesia</td>
                                 <td>annasthesia@gmail.com</td>
                                 <td>(760) 756 7568</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="Rating"
                                          href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/02.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Brock Lee</td>
                                 <td>brocklee@gmail.com</td>
                                 <td>+62 5689 458 658</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                      <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/03.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Dan Druff</td>
                                 <td>dandruff@gmail.com</td>
                                 <td>+55 6523 456 856</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/04.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Hans Olo</td>
                                 <td>hansolo@gmail.com</td>
                                 <td>+91 2586 253 125</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                        <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/05.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Lynn Guini</td>
                                 <td>lynnguini@gmail.com</td>
                                 <td>+27 2563 456 589</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                      <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/06.jpg"  class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Eric Shun</td>
                                 <td>ericshun@gmail.com</td>
                                 <td>+55 2568 256 589</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/07.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>aaronottix</td>
                                 <td>budwiser@ymail.com</td>
                                 <td>(760) 765 2658</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/08.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Marge Arita</td>
                                 <td>margearita@gmail.com</td>
                                 <td>+27 5625 456 589</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                     <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/09.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>Bill Dabear</td>
                                 <td>billdabear@gmail.com</td>
                                 <td>+55 2563 456 589</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
                                       </span>
                                    </div>
                                 </td>
                              </tr>
                              <tr>
                                 <td>
                                    <img src="../../../../assets/images/user/10.jpg" class="rounded avatar-40 img-fluid" alt="">
                                 </td>
                                 <td>John Doe</td>
                                 <td>Johndoe@gmail.com</td>
                                 <td>+55 2598 256 890</td>
                                 <td>
                                    <div class="d-flex align-items-center list-action">
                                       <a class="badge bg-warning-light mr-2" data-toggle="tooltip" data-placement="top" title=""
                                          data-original-title="Rating" href="#"><i class="far fa-star"></i></a>
                                       <a class="badge bg-success-light mr-2" data-toggle="tooltip" data-placement="top" title="" data-original-title="View"
                                          href="#"><i class="lar la-eye"></i></a>
                                       <span class="badge a bg-primary-light" data-toggle="tooltip" data-placement="top" title="" data-original-title="Action"
                                             href="#">
                                             <b-dropdown  id="dropdownMenuButton1"  variant="none" data-toggle="dropdown" >
                                                <template v-slot:button-content >
                                                <i class="fas fa-caret-down b"></i>
                                                </template>
                                                <b-dropdown-item>{{ ('Edit') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('delete') }}</b-dropdown-item>
                                                <b-dropdown-item>{{ ('Hide from Contacts') }}</b-dropdown-item>
                                                </b-dropdown>
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
      </div>
</template>
<script>
import { core } from '../../../../config/pluginInit'
export default {
    name:'ContactList',
     mounted () {
   core.index()
   core.initDataTable()
   },
   methods: {
   },
   data () {
   return {
   }
   }
}
</script>
<style scoped>
.a{
   padding-top: 0px;
   padding-bottom: 0px;
   padding-left: 0px;
   padding-right: 0px;
   margin: 0px;
   height: 25px;
   width: 31px;
  
}
.b{
   position: relative;
   bottom: 5px;
   right: 1px;
}
</style>