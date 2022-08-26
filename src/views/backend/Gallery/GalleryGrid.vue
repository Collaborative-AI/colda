<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card class="card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title mb-0">Image Gallery</h4>
                     </template>
                  <template v-slot:body>
                     <b-row>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/01.jpg')">
                           <img src="../../../assets/images/gallery/grid/01.jpg" class="img-fluid rounded" alt="" />  
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/02.jpg')">
                           <img src="../../../assets/images/gallery/grid/02.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/03.jpg')">
                           <img src="../../../assets/images/gallery/grid/03.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/04.jpg')">
                           <img src="../../../assets/images/gallery/grid/04.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/05.jpg')">
                           <img src="../../../assets/images/gallery/grid/05.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/06.jpg')">
                           <img src="../../../assets/images/gallery/grid/06.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/07.jpg')">
                           <img src="../../../assets/images/gallery/grid/07.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/08.jpg')">
                           <img src="../../../assets/images/gallery/grid/08.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/09.jpg')">
                           <img src="../../../assets/images/gallery/grid/09.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/10.jpg')">
                           <img src="../../../assets/images/gallery/grid/10.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/11.jpg')">
                           <img src="../../../assets/images/gallery/grid/11.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                        <b-col xl="3" lg="4" md="3" class="grid-m">
                           <a class="image-popup-vertical-fit" :href="require('../../../assets/images/gallery/grid/12.jpg')">
                           <img src="../../../assets/images/gallery/grid/12.jpg" class="img-fluid rounded" alt="" />
                           </a>
                        </b-col>
                     </b-row>
                  </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
import {core} from '@/config/pluginInit'
export default {
    name:'GalleryGrid',
    mounted () {
      core.verticalImagePopup()
    }
}
</script>