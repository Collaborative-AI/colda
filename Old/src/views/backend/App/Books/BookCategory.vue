<template>
  <b-container fluid>
               <b-row>
                  <b-col lg="12">
                     <card className="card-transparent">
                        <div class="d-block text-center">
                           <h2 class="mb-3">Search by Book Name</h2>
                           <div class="w-100 iq-search-filter">
                              <ul class="list-inline p-0 m-0 row justify-content-center search-menu-options">
                                 <li class="search-menu-opt">
                                    <div class="iq-dropdown">
                                       <div class="form-group mb-0">
                                          <select class="form-control form-search-control bg-white border-0" id="exampleFormControlSelect1">
                                             <option selected="">All</option>
                                             <option>A Books</option>
                                             <option>the Sun</option>
                                             <option>Harsh book</option>
                                             <option>People book</option>
                                             <option>the Fog</option>
                                          </select>
                                       </div>
                                    </div>
                                 </li>
                                 <li class="search-menu-opt">
                                    <div class="iq-dropdown">
                                       <div class="form-group mb-0">
                                          <select class="form-control form-search-control bg-white border-0" id="exampleFormControlSelect2">
                                             <option selected="">Genres</option>
                                             <option>General</option>
                                             <option>History</option>
                                             <option>Horror</option>
                                             <option>Fantasy</option>
                                             <option>Literary</option>
                                             <option>Manga</option>
                                          </select>
                                       </div>
                                    </div>
                                 </li>
                                 <li class="search-menu-opt">
                                    <div class="iq-dropdown">
                                       <div class="form-group mb-0">
                                          <select class="form-control form-search-control bg-white border-0" id="exampleFormControlSelect3">
                                             <option selected="">Year</option>
                                             <option>2015</option>
                                             <option>2016</option>
                                             <option>2017</option>
                                             <option>2018</option>
                                             <option>2019</option>
                                             <option>2020</option>
                                          </select>
                                       </div>
                                    </div>
                                 </li>
                                 <li class="search-menu-opt">
                                    <div class="iq-dropdown">
                                       <div class="form-group mb-0">
                                          <select class="form-control form-search-control bg-white border-0" id="exampleFormControlSelect4">
                                             <option selected="">Author</option>
                                             <option>Milesiy Yor</option>
                                             <option>Ira Membrit</option>
                                             <option>Anna Mull</option>
                                             <option>John Smith</option>
                                             <option>David King</option>
                                             <option>Kusti Franti</option>
                                          </select>
                                       </div>
                                    </div>
                                 </li>
                                 <li class="search-menu-opt">
                                    <div class="iq-search-bar search-book d-flex align-items-center">
                                       <form action="#" class="searchbox">
                                          <input type="text" class="text search-input" placeholder="search here...">
                                          <a class="search-link" href="#"><i class="ri-search-line"></i></a>
                                       </form>
                                       <button type="submit" class="btn btn-primary search-data ml-2">Search</button>
                                    </div>
                                 </li>
                              </ul>
                           </div>
                        </div>
                     </card>
                     <card>
                        <template v-slot:body>
                           <div class="row">
                              <div class="col-sm-6 col-md-4 col-lg-3">
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/01.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">A Hunger knut book</h6>
                                                <p class="font-size-13 line-height mb-1">Gurt Mistrioty</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/02.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">In Cold Blood Book..</h6>
                                                <p class="font-size-13 line-height mb-1">Anna Mull</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
                                                <span class="pr-1 old-price">$129</span>
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/03.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">The Truman Capite</h6>
                                                <p class="font-size-13 line-height mb-1">Ira Membrit</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
                                                <span class="pr-1 old-price">$79</span>
                                                <h6><b>$70</b></h6>
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/04.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">A Book Of Thinner</h6>
                                                <p class="font-size-13 line-height mb-1">Pete Sariya</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/05.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">Book of Texi Driver</h6>
                                                <p class="font-size-13 line-height mb-1">Paige Turner</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
                                                <span class="pr-1 old-price">$129</span>
                                                <h6><b>$120</b></h6>
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/06.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">A man with those Faces</h6>
                                                <p class="font-size-13 line-height mb-1">Bob Frapples</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/07.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">The Great Gatsb</h6>
                                                <p class="font-size-13 line-height mb-1">Barb Ackue</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/08.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">The Cover Design Book</h6>
                                                <p class="font-size-13 line-height mb-1">Monty Carlo</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
                                                <span class="pr-1 old-price">$102</span>
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
                                 <div class="card card-block card-stretch card-height search-bookcontent mb-lg-0">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/09.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">Starving Start up book</h6>
                                                <p class="font-size-13 line-height mb-1">Monty Carlo</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent mb-md-0 mb-lg-0">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/10.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">I can do it anything</h6>
                                                <p class="font-size-13 line-height mb-1">Terry Aki</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                      <i class="fa fa-star"></i>
                                                   </span>
                                                </div>
                                             </div>
                                             <div class="price d-flex align-items-center">
                                                <span class="pr-1 old-price">$103</span>
                                                <h6><b>$98</b></h6>
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
                                 <div class="card card-block card-stretch card-height search-bookcontent mb-sm-0 mb-md-0 mb-lg-0">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/11.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">A horror Novel Book</h6>
                                                <p class="font-size-13 line-height mb-1">Hal Appeno</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                                 <div class="card card-block card-stretch card-height search-bookcontent m-0 mb-sm-0 mb-md-0 mb-lg-0">
                                    <div class="card-body p-0">
                                       <div class="d-flex align-items-center">
                                          <div class="col-6 p-0 position-relative image-overlap-shadow">
                                             <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/search-book/12.jpg" alt=""></a>
                                             <div class="view-book">
                                                <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                             </div>
                                          </div>
                                          <div class="col-6">
                                             <div class="mb-2">
                                                <h6 class="mb-1">Think Outside Box</h6>
                                                <p class="font-size-13 line-height mb-1">Bill Emia</p>
                                                <div class="d-block">
                                                   <span class="font-size-13 text-warning">
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
                           </div>
                        </template>
                     </card>
                  </b-col>
                  <b-col lg="12">
                     <card className="card card-block card-stretch card-height" headerClass="align-items-center position-relative mb-0 similar-detail" bodyClass="similar-contens">
                        <template v-slot:headerTitle>
                              <h4 class="card-title mb-0">Similar Books</h4>
                           </template>
                           <template v-slot:headerAction>
                              <router-link to="/bookcategory" class="btn btn-sm btn-primary view-more text-white">View More</router-link>
                           </template>
                        <template v-slot:body>
                            <Slick id="similar-slider" :option="option1">

                           <li class="d-flex align-items-center">
                             <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/01.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">The Raze Night Book</h6>
                                          <p class="font-size-13 line-height mb-1">Tara Zona</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                             </span>
                                          </div>
                                       </div>
                                       <div class="price d-flex align-items-center">
                                          <span class="pr-1 old-price">$102</span>
                                          <h6><b>$95</b></h6>
                                       </div>
                                       <div class="iq-product-action">
                                          <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                           </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/02.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Set For Life Book..</h6>
                                          <p class="font-size-13 line-height mb-1">Anna Rexia</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <h6><b>$110</b></h6>
                                       </div>
                                       <div class="iq-product-action">
                                          <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/03.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Through the Breaking</h6>
                                          <p class="font-size-13 line-height mb-1">Bill Emia</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/04.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Wild Beautiful Places</h6>
                                          <p class="font-size-13 line-height mb-1">Hal Appeno</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <h6><b>$95</b></h6>
                                       </div>
                                       <div class="iq-product-action">
                                          <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/05.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">The Mockup Magazine</h6>
                                          <p class="font-size-13 line-height mb-1">Zack Lee</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="#"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/06.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Every Book Of travel</h6>
                                          <p class="font-size-13 line-height mb-1">Moe Fugga</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                                <i class="fa fa-star"></i>
                                             </span>
                                          </div>
                                       </div>
                                       <div class="price d-flex align-items-center">
                                          <h6><b>$120</b></h6>
                                       </div>
                                       <div class="iq-product-action">
                                          <a href="#"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="#" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>
                            </Slick>
                        </template>
                     </card>
                  </b-col>
                  <b-col sm="12">
                     <card className="card card-block card-stretch card-height" headerClass="align-items-center position-relative mb-0 trendy-detail" bodyClass="trendy-contens">
                        <template v-slot:headerTitle>
                              <h4 class="card-title mb-0">Trendy Books</h4>
                           </template>
                           <template v-slot:headerAction>
                              <router-link to="/bookcategory" class="btn btn-sm btn-primary view-more text-white">View More</router-link>
                           </template>
                        <template v-slot:body>
                           <Slick id="trendy-slider" :option="option2">

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/01.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">The Word Books Day..</h6>
                                          <p class="font-size-13 line-height mb-1">Paul Molive</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/02.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">The catcher in the Rye</h6>
                                          <p class="font-size-13 line-height mb-1">Anna Sthesia</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/03.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Little Black Book</h6>
                                          <p class="font-size-13 line-height mb-1">Monty Carlo</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/04.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Take The Risk Book</h6>
                                          <p class="font-size-13 line-height mb-1">Smith goal</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/05.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">The Raze Night Book </h6>
                                          <p class="font-size-13 line-height mb-1">Paige Turner</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>

                                 <li class="d-flex align-items-center">
                                    <div class="col-5 p-0 position-relative image-overlap-shadow">
                                       <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/trendy-books/06.jpg" alt=""></a>
                                       <div class="view-book">
                                          <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                                       </div>
                                    </div>
                                    <div class="col-7">
                                       <div class="mb-2">
                                          <h6 class="mb-1">Find the Wave Book..</h6>
                                          <p class="font-size-13 line-height mb-1">Barb Ackue</p>
                                          <div class="d-block">
                                             <span class="font-size-13 text-warning">
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
                                          <a href="javascript:void();"><i class="ri-shopping-cart-2-fill text-primary"></i></a>
                                          <a href="javascript:void();" class="ml-2"><i class="ri-heart-fill text-danger"></i></a>
                                       </div>
                                    </div>
                                 </li>
                           </Slick>
                        </template>
                     </card>
                  </b-col>
                  <b-col lg="12">
                    <card className="card card-block card-stretch card-height" headerClass="align-items-center position-relative" bodyClass="favorites-contens">
                        <template v-slot:headerTitle>
                              <h4 class="card-title mb-0">Favorite Reads</h4>
                           </template>
                           <template v-slot:headerAction>
                              <router-link to="/bookcategory" class="btn btn-sm btn-primary view-more text-white">View More</router-link>
                           </template>
                        <template v-slot:body>
                        <Slick id="favorites-slider" :option="option3">

                                 <li class="d-flex justify-content-between align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/05.jpg" class="img-fluid rounded w-100" alt="">
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

                                 <li class="d-flex justify-content-between align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/06.jpg" class="img-fluid rounded w-100" alt="">
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

                                 <li class="d-flex justify-content-between align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/07.jpg" class="img-fluid rounded w-100" alt="">
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

                                 <li class="d-flex justify-content-between align-items-center">
                                    <div class="col-5 p-0 position-relative">
                                       <a href="#">
                                          <img src="@/assets/images/book-image/favorite/08.jpg" class="img-fluid rounded w-100" alt="">
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
export default {
  name: 'BookCategory',
  mounted () {
    core.index()
  },
  methods: {
  },
  data () {
    return {
      option1: {
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
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 576,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      },
      option2: {
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
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 576,
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
      }
    }
  }
}
</script>
