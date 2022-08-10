<template>
  <b-container fluid>
   <b-row>
      <b-col sm="12">
         <card className="card card-block card-stretch card-height" headerClass="align-items-center" bodyClass="pb-0">
            <template v-slot:headerTitle>
               <h4 class="card-title mb-0">Books Description</h4>
            </template>
            <template v-slot:body>
               <div class="description-contens align-items-top row">
                  <div class="col-md-6">
                     <div class="card-transparent card-block card-stretch card-height">
                        <div class="card-body p-0">
                           <div class="row align-items-center">
                              <div class="col-3">
                                 <Slick id="description-slider-nav" :option="option4">
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/01.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/02.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/03.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/04.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/05.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/06.jpg" class="img-fluid rounded w-100" alt="">
                                       </a>
                                    </li>
                                 </slick>
                              </div>
                              <div class="col-9">
                                 <Slick id="description-slider" :option="option3">
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/01.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/02.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/03.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/04.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/05.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                    <li>
                                       <a href="#">
                                       <img src="@/assets/images/book-image/book-dec/06.jpg" class="img-fluid w-100 rounded" alt="">
                                       </a>
                                    </li>
                                 </Slick>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="col-md-6">
                     <div class="card-transparent card-block card-stretch card-height">
                        <div class="card-body p-0">
                           <h3 class="mb-3">A Casey Christi night books in the raza Dakota Krout</h3>
                           <div class="price d-flex align-items-center font-weight-500 mb-2">
                              <span class="font-size-20 pr-2 old-price">$99</span>
                              <span class="font-size-24 text-dark">$48</span>
                           </div>
                           <div class="mb-3 d-block">
                              <span class="font-size-20 text-warning">
                              <i class="fa fa-star mr-1"></i>
                              <i class="fa fa-star mr-1"></i>
                              <i class="fa fa-star mr-1"></i>
                              <i class="fa fa-star mr-1"></i>
                              <i class="fa fa-star"></i>
                              </span>
                           </div>
                           <span class="text-dark mb-4 pb-4 iq-border-bottom d-block">Monterhing in the best book testem ipsum is simply dtest in find in a of the printing and typeseting industry into to end.in find in a of the printing and typeseting industry in find to make it all done into end.</span>
                           <div class="text-primary mb-4">Author: <span class="text-body">Jhone Steben</span></div>
                           <div class="mb-4 d-flex align-items-center">
                              <a href="#" class="btn btn-primary view-more mr-2 text-white">Add To Cart</a>
                              <router-link to="/book-pdf" class="btn btn-primary view-more mr-2 text-white">Read Sample</router-link>
                           </div>
                           <div class="mb-3">
                              <a href="#" class="text-body text-center"><span class="avatar-30 rounded-circle bg-primary d-inline-block mr-2"><i class="ri-heart-fill"></i></span><span>Add to Wishlist</span></a>
                           </div>
                           <div class="iq-social d-flex align-items-center">
                              <h5 class="mr-2">Share:</h5>
                              <ul class="list-inline d-flex p-0 mb-0 align-items-center">
                                 <li>
                                    <a href="#" class="avatar-40 rounded-circle bg-primary mr-2 facebook"><i class="fab fa-facebook-f" aria-hidden="true"></i></a>
                                 </li>
                                 <li>
                                    <a href="#" class="avatar-40 rounded-circle bg-primary mr-2 twitter"><i class="fab fa-twitter" aria-hidden="true"></i></a>
                                 </li>
                                 <li>
                                    <a href="#" class="avatar-40 rounded-circle bg-primary mr-2 youtube"><i class="fab fa-youtube" aria-hidden="true"></i></a>
                                 </li>
                                 <li >
                                    <a href="#" class="avatar-40 rounded-circle bg-primary pinterest"><i class="fab fa-pinterest" aria-hidden="true"></i></a>
                                 </li>
                              </ul>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </template>
         </card>
      </b-col>
      <b-col sm="12">
         <card className="card card-block card-stretch card-height" headerClass="align-items-center position-relative" bodyClass="single-similar-contens">
            <template v-slot:headerTitle>
                  <h4 class="card-title mb-0">Similar Books</h4>
               </template>
               <template v-slot:headerAction>
                  <router-link to="/bookcategory" class="btn btn-sm btn-primary view-more text-white">View More</router-link>
               </template>
            <template v-slot:body>
               <Slick id="single-similar-slider" :option="option1">

                     <li class="d-flex align-items-center">
                        <div class="col-5">
                           <div class="position-relative image-overlap-shadow">
                              <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/01.jpg" alt=""></a>
                              <div class="view-book">
                                 <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                              </div>
                           </div>
                        </div>
                        <div class="col-7 pl-0">
                           <h6 class="mb-2">The Book of treasure Island find...</h6>
                           <p class="text-body">Author : Tara Zona</p>
                           <a href="#" class="text-dark" tabindex="-1">Read Now<i class="ri-arrow-right-s-line"></i></a>
                        </div>
                     </li>

                     <li class="d-flex align-items-center">
                        <div class="col-5">
                           <div class="position-relative image-overlap-shadow">
                              <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/02.jpg" alt=""></a>
                              <div class="view-book">
                                 <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                              </div>
                           </div>
                        </div>
                        <div class="col-7 pl-0">
                           <h6 class="mb-2">Set For Lifr Being Scott Trench..</h6>
                           <p class="text-body">Author : Anna Rexia</p>
                           <a href="#" class="text-dark" tabindex="-1">Read Now<i class="ri-arrow-right-s-line"></i></a>
                        </div>
                     </li>

                     <li class="d-flex align-items-center">
                        <div class="col-5">
                           <div class="position-relative image-overlap-shadow">
                              <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/03.jpg" alt=""></a>
                              <div class="view-book">
                                 <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                              </div>
                           </div>
                        </div>
                        <div class="col-7 pl-0">
                           <h6 class="mb-2">A Birth and Evolutions of the Soul...</h6>
                           <p class="text-body">Author : Bill Emia</p>
                           <a href="#" class="text-dark" tabindex="-1">Read Now<i class="ri-arrow-right-s-line"></i></a>
                        </div>
                     </li>

                     <li class="d-flex align-items-center">
                        <div class="col-5">
                           <div class="position-relative image-overlap-shadow">
                              <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/04.jpg" alt=""></a>
                              <div class="view-book">
                                 <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                              </div>
                           </div>
                        </div>
                        <div class="col-7 pl-0">
                           <h6 class="mb-2">The Nature of world Beautiful Places.</h6>
                           <p class="text-body">Author : Hal Appeno</p>
                           <a href="#" class="text-dark" tabindex="-1">Read Now<i class="ri-arrow-right-s-line"></i></a>
                        </div>
                     </li>

                     <li class="d-flex align-items-center">
                        <div class="col-5">
                           <div class="position-relative image-overlap-shadow">
                              <a href="javascript:void();"><img class="img-fluid rounded w-100" src="@/assets/images/book-image/similar-books/05.jpg" alt=""></a>
                              <div class="view-book">
                                 <router-link to="/bookpage" class="btn btn-sm btn-white">View Book</router-link>
                              </div>
                           </div>
                        </div>
                        <div class="col-7 pl-0">
                           <h6 class="mb-2">The mackup magazine find books..</h6>
                           <p class="text-body">Author : Zack Lee</p>
                           <a href="#" class="text-dark" tabindex="-1">Read Now<i class="ri-arrow-right-s-line"></i></a>
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
// import { core } from '../../config/pluginInit'
export default {
  name: 'Bookpage',
  mounted () {
   //  core.index()
  },
  watch: {
    // 'rtl': function (value) {
    //   this.option.rtl = this.rtl
    //   this.option1.rtl = this.rtl
    //   this.option2.rtl = this.rtl
    //   this.option3.rtl = this.rtl
    //   this.option4.rtl = this.rtl
    // }
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
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '#description-slider-nav'
      },
      option4: {
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '#description-slider',
        dots: false,
        arrows: false,
        infinite: true,
        vertical: true,
        centerMode: false,
        focusOnSelect: true
      }
    }
  }
}
</script>
