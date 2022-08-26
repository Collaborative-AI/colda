<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card class="card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Hover Effects</h4>
                     </template>
                  <template v-slot:body>
                     <b-row>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/01.jpg" class="img-fluid rounded effect-1" alt="" />
                              </a>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/02.jpg" class="img-fluid rounded effect-2" alt="" />
                              </a>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/03.jpg" class="img-fluid rounded effect-3" alt="" />
                              </a>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/04.jpg" class="img-fluid rounded effect-4" alt="" />
                              </a>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/05.jpg" class="img-fluid rounded" alt="" />
                              </a>
                              <div class="ovrlay-1-a"></div>
                              <div class="ovrlay-1-b"></div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/06.jpg" class="img-fluid rounded" alt="" />
                              </a>
                              <div class="ovrlay-2-a"></div>
                              <div class="ovrlay-2-b"></div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/07.jpg" class="img-fluid rounded" alt="" />
                              </a>
                              <div class="ovrlay-3-a"></div>
                              <div class="ovrlay-3-b"></div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <a href="#">
                                 <img src="../../../assets/images/gallery/hover-effects/08.jpg" class="img-fluid rounded" alt="" />
                              </a>
                              <div class="ovrlay-4-a"></div>
                              <div class="ovrlay-4-b"></div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <img src="../../../assets/images/gallery/hover-effects/09.jpg" class="img-fluid rounded" alt="" />
                              <div class="ovrlay-5">
                                 <h4 class="mt-4 mb-2">Lorem Ipsum</h4>
                                 <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has
                                    been the industry's standard
                                    dummy text.
                                 </p>
                                 <a href="#" class="btn btn-primary mb-3">Read More</a>
                              </div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <img src="../../../assets/images/gallery/hover-effects/10.jpg" class="img-fluid rounded" alt="" />
                              <div class="ovrlay-6">
                                 <h4 class="mt-4 mb-2 text-center">Lorem Ipsum</h4>
                                 <p class="text-center">Lorem Ipsum is simply dummy text of the printing and typesetting
                                    industry. Lorem Ipsum has been the
                                    industry's standard dummy text.
                                 </p>
                                 <div class="d-flex justify-content-center mb-3">
                                    <a href="#" class="btn btn-primary">Read More</a>
                                 </div>
                              </div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <img src="../../../assets/images/gallery/hover-effects/11.jpg" class="img-fluid rounded" alt="" />
                              <div class="ovrlay-7">
                                 <a href="#" class="button"><i class="fa fa-search"></i></a>
                              </div>
                           </div>
                        </b-col>
                        <b-col xl="3" lg="4" md="6" class="grid-m">
                           <div class="hover-effects">
                              <img src="../../../assets/images/gallery/hover-effects/12.jpg" class="img-fluid rounded effect-8" alt="" />
                              <div class="ovrlay-8">
                                 <h4 class="mt-3 pl-2">Lorem ipsum</h4>
                                 <a href="#" class="i-btn"><i class="fas fa-long-arrow-alt-right"></i></a>
                              </div>
                           </div>
                        </b-col>
                     </b-row>
                  </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'GalleryHover'
}
</script>