<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card class="card-block card-stretch card-height">
               <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Masonary Gallery</h4>
                    </template>
                  <template v-slot:body>
                     <div id="gallery" class="gallery masonry">
                        <div class="grid-sizer"></div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/01.jpg')">
                              <img src="../../../assets/images/gallery/masonry/01.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/02.jpg')">
                              <img src="../../../assets/images/gallery/masonry/02.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/03.jpg')">
                              <img src="../../../assets/images/gallery/masonry/03.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/04.jpg')">
                              <img src="../../../assets/images/gallery/masonry/04.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/05.jpg')">
                              <img src="../../../assets/images/gallery/masonry/05.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/06.jpg')">
                              <img src="../../../assets/images/gallery/masonry/06.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/07.jpg')">
                              <img src="../../../assets/images/gallery/masonry/07.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/08.jpg')">
                              <img src="../../../assets/images/gallery/masonry/08.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/09.jpg')">
                              <img src="../../../assets/images/gallery/masonry/09.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/10.jpg')">
                              <img src="../../../assets/images/gallery/masonry/10.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/11.jpg')">
                              <img src="../../../assets/images/gallery/masonry/11.jpg" class="rounded" alt="">
                           </a>
                        </div>
                        <div class="item">
                           <a :href="require('../../../assets/images/gallery/masonry/12.jpg')">
                              <img src="../../../assets/images/gallery/masonry/12.jpg" class="rounded" alt="">
                           </a>
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
    name:'GalleryMasonry',
    mounted(){
      core.verticalImagePopup();
      core.masonry();
    }
}
</script>