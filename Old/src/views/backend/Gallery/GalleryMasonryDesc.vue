<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card class="card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Masonry Gallery with Description</h4>
                     </template>
                  <template v-slot:body>
                     <div id="gallery" class="gallery masonry">
                        <div class="grid-sizer"></div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/01.jpg')">
                              <img src="../../../assets/images/gallery/masonry/01.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/02.jpg')">
                              <img src="../../../assets/images/gallery/masonry/02.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/03.jpg')">
                              <img src="../../../assets/images/gallery/masonry/03.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/04.jpg')">
                              <img src="../../../assets/images/gallery/masonry/04.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/05.jpg')">
                              <img src="../../../assets/images/gallery/masonry/05.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/06.jpg')">
                              <img src="../../../assets/images/gallery/masonry/06.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/07.jpg')">
                              <img src="../../../assets/images/gallery/masonry/07.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/08.jpg')">
                              <img src="../../../assets/images/gallery/masonry/08.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/09.jpg')">
                              <img src="../../../assets/images/gallery/masonry/09.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/10.jpg')">
                              <img src="../../../assets/images/gallery/masonry/10.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/11.jpg')">
                              <img src="../../../assets/images/gallery/masonry/11.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been
                                 the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/12.jpg')">
                              <img src="../../../assets/images/gallery/masonry/12.jpg" class="b-radius-top" alt="">
                           </a>
                           <div class="g-desc b-radius-bottom p-3">
                              <h4>Portfolio Title</h4>
                              <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                                 Ipsum has been
                                 the
                                 industry's standard
                                 dummy text.
                              </p>
                           </div>
                        </div>
                     </div>
                  </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
import {core} from '@/config/pluginInit'
export default {
    name:'GalleryMasonryDesc',
    mounted(){
       core.verticalImagePopup()
       setTimeout(() => {
          core.masonry()
       }, 1000)
    }
}
</script>