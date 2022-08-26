<template>
  <b-container fluid>
      <b-row>
         <b-col lg="12">
            <card className="card-transparent card-block card-stretch card-height rounded">
               <div class="newrealease-contens">
                  <Slick id="newrealease-slider" :option="option1">
                     <li v-for="(image,index) in images" :key="index" class="item">
                        <a href="#">
                           <img :src="image.src" class="img-fluid w-100 rounded" alt="">
                        </a>
                     </li>
                  </Slick>
               </div>
            </card>
         </b-col>
         <b-col lg="12">
            <card className=" card-block card-stretch card-height" headerClass=" align-items-center position-relative">
            <template v-slot:headerTitle>
                     <h4 class="card-title mb-0">Browse Books</h4>
            </template>
            <template v-slot:headerAction>
               <router-link to="/bookcategory" class="btn btn-sm btn-primary view-more text-white">View More</router-link>
            </template>
            <template v-slot:body>
                  <b-row>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/01.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Reading on the World</h6>
                                       <p class="font-size-13 line-height mb-1">Jhone Steben</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$100</span>
                                       <h6><b>$89</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/02.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">The Catcher in the Rye</h6>
                                       <p class="font-size-13 line-height mb-1">Fritz Wold</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <h6><b>$99</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/03.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Little Black Book</h6>
                                       <p class="font-size-13 line-height mb-1">John Klok</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$150</span>
                                       <h6><b>$129</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/04.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Take On The Risk</h6>
                                       <p class="font-size-13 line-height mb-1">George Strong</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$120</span>
                                       <h6><b>$100</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/05.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Absteact On Background</h6>
                                       <p class="font-size-13 line-height mb-1">Ichae Semos</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$105</span>
                                       <h6><b>$99</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/06.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Find The Wave Book</h6>
                                       <p class="font-size-13 line-height mb-1">Fidel Martin</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$110</span>
                                       <h6><b>$100</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/07.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">See the More Story</h6>
                                       <p class="font-size-13 line-height mb-1">Jules Boutin</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$89</span>
                                       <h6><b>$79</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/08.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">The Wikde Book</h6>
                                       <p class="font-size-13 line-height mb-1">Kusti Franti</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$99</span>
                                       <h6><b>$89</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent mb-lg-0">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/09.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">Conversion Erik Routley</h6>
                                       <p class="font-size-13 line-height mb-1">Argele Intili</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$100</span>
                                       <h6><b>$79</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent mb-md-0 mb-lg-0">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/10.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">The Leo Dominica</h6>
                                       <p class="font-size-13 line-height mb-1">Henry Jurk</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$120</span>
                                       <h6><b>$99</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent mb-sm-0 mb-md-0 mb-lg-0">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/11.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">By The Editbeth Jat</h6>
                                       <p class="font-size-13 line-height mb-1">David King</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <h6><b>$149</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-sm-6 col-md-4 col-lg-3">
                        <div class="card card-block card-stretch card-height browse-bookcontent mb-0 mb-sm-0 mb-md-0 mb-lg-0">
                           <div class="card-body p-0">
                              <div class="d-flex align-items-center">
                                 <div class="col-6 p-0 position-relative image-overlap-shadow">
                                    <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/browse-books/12.jpg" alt=""></a>
                                    <div class="view-book">
                                       <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                    </div>
                                 </div>
                                 <div class="col-6">
                                    <div class="mb-2">
                                       <h6 class="mb-1">The Crucial Decade</h6>
                                       <p class="font-size-13 line-height mb-1">Attilio Marzi</p>
                                       <div class="d-block line-height">
                                          <span class="font-size-11 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                       </div>
                                    </div>
                                    <div class="price d-flex align-items-center">
                                       <span class="pr-1 old-price">$99</span>
                                       <h6><b>$89</b></h6>
                                    </div>
                                    <div class="iq-product-action">
                                       <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                       <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </b-row>
            </template>
            </card>
         </b-col>
         <b-col lg="6">
            <card className=" card-block card-stretch card-height" headerClass=" mb-0">
               <template v-slot:headerTitle>
                     <h4 class="card-title">Featured Books</h4>
               </template>
                  <template v-slot:headerAction>
                  <b-dropdown id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                     <template v-slot:button-content>
                     This Week<i class="ri-arrow-down-s-fill"></i>
                     </template>
                     <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ 'dropdown.view'}}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ 'dropdown.delete'}}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ 'dropdown.edit'}}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ 'dropdown.print'}}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ 'dropdown.download'}}</b-dropdown-item>
                     </b-dropdown>
                  </template>
               <template v-slot:body>
                  <div class="row align-items-center">
                     <div class="col-sm-5 pr-0">
                        <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/page-img/featured-book.png" alt=""></a>
                     </div>
                     <div class="col-sm-7 mt-3 mt-sm-0">
                        <h4 class="mb-2">Casey Christie night book into find...</h4>
                        <p class="mb-2">Author: Gheg origin</p>
                        <div class="mb-2 d-block">
                           <span class="font-size-12 text-warning">
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                              <i class="fa fa-star"></i>
                           </span>
                        </div>
                        <span class="text-dark mb-3 d-block">Lorem Ipsum is simply dummy test in find a of the printing and typeset ing industry into end.</span>
                        <button type="submit" class="btn btn-primary learn-more">Learn More</button>
                     </div>
                  </div>
               </template>
            </card>
         </b-col>
         <b-col lg="6">
            <card className="card-block card-stretch card-height" headerClass=" mb-0">
               <template v-slot:headerTitle>
                     <h4 class="card-title">Featured Writer</h4>
               </template>
               <template v-slot:headerAction>
                     <b-dropdown id="dropdownMenuButton1" right variant="none" data-toggle="dropdown">
                     <template v-slot:button-content>
                     This Week<i class="ri-arrow-down-s-fill"></i>
                     </template>
                     <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ 'dropdown.view' }}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ 'dropdown.delete' }}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-pencil-fill mr-2"></i>{{ 'dropdown.edit' }}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-printer-fill mr-2"></i>{{ 'dropdown.print' }}</b-dropdown-item>
                     <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ 'dropdown.download' }}</b-dropdown-item>
                     </b-dropdown>
               </template>
               <template v-slot:body>
                  <ul class="list-inline row mb-0 align-items-center iq-scrollable-block">
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/01.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Brandon Guidelines</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/02.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Hugh Millie-Yate</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">432</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/03.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Nathaneal Down</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">5471</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/04.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Thomas R. Toe</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">8764</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/05.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Druid Wensleydale</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">8987</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/06.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Natalya Undgrowth</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/07.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Desmond Eagle</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">4324</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/08.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Lurch Schpellchek</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">012</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/09.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Natalya Undgrowth</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/10.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Natalya Undgrowth</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/11.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Natalya Undgrowth</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                     <li class="col-sm-6 d-flex mb-3 align-items-center">
                        <div class="icon iq-icon-box mr-3">
                           <a href="#"><img class="img-fluid avatar-60 rounded-circle" src="@/assets/images/user/01.jpg" alt=""></a>
                        </div>
                        <div class="mt-1">
                           <h6>Natalya Undgrowth</h6>
                           <p class="mb-0 text-primary">Publish Books: <span class="text-body">2831</span></p>
                        </div>
                     </li>
                  </ul>
               </template>
            </card>
         </b-col>
         <b-col lg="12">
                     <card className=" card-block card-stretch card-height" headerClass=" align-items-center position-relative" bodyClass="favorites-contens">
                        <template v-slot:headerTitle>
                              <h4 class="card-title mb-0">Favorite Reads</h4>
                        </template>
                        <template v-slot:headerAction>
                              <router-link to="category-page" class="btn text-white btn-sm btn-primary view-more">View More</router-link>
                        </template>
                        <template v-slot:body>
                            <Slick id="favorites-slider" :option="option">

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/01.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </div>
                                    <div class="col-7">
                                       <h5 class="mb-2">Every Book is a new Wonderful Travel..</h5>
                                       <p class="mb-2">Author : Pedro Araez</p>
                                       <div class="d-flex justify-content-between align-items-center text-dark font-size-13">
                                          <span>Reading</span>
                                          <span class="mr-4">78%</span>
                                       </div>
                                       <div class="iq-progress-bar-linear d-inline-block w-100">
                                          <b-progress :value="78" class="iq-progress-bar" variant="primary" />
                                       </div>
                                       <a href="#" class="text-dark">Read Now<i class="ri-arrow-right-s-line"></i></a>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/02.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </div>
                                    <div class="col-7">
                                       <h5 class="mb-2">Casey Christie night book into find...</h5>
                                       <p class="mb-2">Author : Michael klock</p>
                                       <div class="d-flex justify-content-between align-items-center text-dark font-size-13">
                                          <span>Reading</span>
                                          <span class="mr-4">78%</span>
                                       </div>
                                       <div class="iq-progress-bar-linear d-inline-block w-100">
                                         <b-progress :value="78" class="iq-progress-bar" variant="danger" />
                                       </div>
                                       <a href="#" class="text-dark">Read Now<i class="ri-arrow-right-s-line"></i></a>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/03.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </div>
                                    <div class="col-7">
                                       <h5 class="mb-2">The Secret to English Busy People..</h5>
                                       <p class="mb-2">Author : Daniel Ace</p>
                                       <div class="d-flex justify-content-between align-items-center text-dark font-size-13">
                                          <span>Reading</span>
                                          <span class="mr-4">78%</span>
                                       </div>
                                       <div class="iq-progress-bar-linear d-inline-block w-100">
                                          <b-progress :value="78" class="iq-progress-bar" variant="info" />
                                       </div>
                                       <a href="#" class="text-dark">Read Now<i class="ri-arrow-right-s-line"></i></a>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/04.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </div>
                                    <div class="col-7">
                                       <h5 class="mb-2">The adventures of Robins books...</h5>
                                       <p class="mb-2">Author : Luka Afton</p>
                                       <div class="d-flex justify-content-between align-items-center text-dark font-size-13">
                                          <span>Reading</span>
                                          <span class="mr-4">78%</span>
                                       </div>
                                       <div class="iq-progress-bar-linear d-inline-block w-100">
                                          <b-progress :value="78" class="iq-progress-bar" variant="success" />
                                       </div>
                                       <a href="#" class="text-dark">Read Now<i class="ri-arrow-right-s-line"></i></a>
                                    </div>
                                 </li>
                           </Slick>
                        </template>
                     </card>
                  </b-col>
      </b-row>
   </b-container>
</template>
<script>
import { core } from '../../../../config/pluginInit'
const $ = require('jquery')
export default {
  name: 'BookShop',
  mounted () {
    core.index()
    $('#newrealease-slider .slick-active.slick-center').prev('.slick-active').addClass('temp')
    $('#newrealease-slider .slick-active.temp').prev().addClass('temp-1')
    $('#newrealease-slider .slick-active.temp-1').prev().addClass('temp-2')
    $('#newrealease-slider .slick-active.slick-center').next('.slick-active').addClass('temp-next')
    $('#newrealease-slider .slick-active.temp-next').next().addClass('temp-next-1')
    $('#newrealease-slider .slick-active.temp-next-1').next().addClass('temp-next-2')
    $('#newrealease-slider').on('afterChange', function () {
      let SLICKSLIDER = $('.slick-active.slick-center').data('slick-index')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 1) + '"]').addClass('temp')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 2) + '"]').addClass('temp-1')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 3) + '"]').addClass('temp-2')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 1)) + '"]').addClass('temp-next')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 2)) + '"]').addClass('temp-next-1')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 3)) + '"]').addClass('temp-next-2')
    })
    $('#newrealease-slider').on('beforeChange', function () {
      let SLICKSLIDER = $('.slick-active.slick-center').data('slick-index')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 1) + '"]').removeClass('temp')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 2) + '"]').removeClass('temp-1')
      $('#newrealease-slider .slick-active[data-slick-index="' + (SLICKSLIDER - 3) + '"]').removeClass('temp-2')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 1)) + '"]').removeClass('temp-next')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 2)) + '"]').removeClass('temp-next-1')
      $('#newrealease-slider .slick-active[data-slick-index="' + (parseInt(SLICKSLIDER + 3)) + '"]').removeClass('temp-next-2')
    })
  },
  methods: {
  },
  data () {
    return {
      option: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: false,
        autoplay: true,
        slidesToShow: 3,
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
      option1: {
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        centerMode: true,
        centerPadding: false,
        variableWidth: true,
        focusOnSelect: true,
        autoplay: false,
        slidesToShow: 7,
        slidesToScroll: 1
      },
      images: [
        {
          src: require('@/assets/images/book-image/new_realeases/01.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/02.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/03.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/04.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/05.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/06.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/07.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/08.jpg')
        },
        {
          src: require('@/assets/images/book-image/new_realeases/09.jpg')
        }
      ]
    }
  }
}
</script>
