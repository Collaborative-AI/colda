<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Default Radio Buttons</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                     <div class="radio d-inline-block mr-2">
                        <input type="radio" name="bsradio" id="radio1" checked="">
                        <label for="radio1">Active</label>
                     </div>
                     <div class="radio d-inline-block mr-2">
                        <input type="radio" name="bsradio" id="radio2">
                        <label for="radio2">Inactive</label>
                     </div>
                     <div class="radio d-inline-block mr-2">
                        <input type="radio" name="bsradio1" id="radio3" disabled="" checked="">
                        <label for="radio3">Active - Disabled</label>
                     </div>
                     <div class="radio d-inline-block mr-2">
                        <input type="radio" name="bsradio1" id="radio4" disabled="">
                        <label for="radio3">Inactive - Disabled</label>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custom Colored Radio Buttons</h4>
               </template>
               <template v-slot:body>
                  <div class="card-body">
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio01" name="customRadio-11" class="custom-control-input bg-primary">
                        <label class="custom-control-label" for="customRadio01"> Primary </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio02" name="customRadio-11" class="custom-control-input bg-success">
                        <label class="custom-control-label" for="customRadio02"> Success </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio03" name="customRadio-11" class="custom-control-input bg-danger">
                        <label class="custom-control-label" for="customRadio03"> Danger </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio04" name="customRadio-11" class="custom-control-input bg-warning">
                        <label class="custom-control-label" for="customRadio04"> Warning </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio05" name="customRadio-11" class="custom-control-input bg-dark">
                        <label class="custom-control-label" for="customRadio05"> Dark </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color custom-control-inline">
                        <input type="radio" id="customRadio06" name="customRadio-11" class="custom-control-input bg-info">
                        <label class="custom-control-label" for="customRadio06"> Info </label>
                     </div>
                  </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custom Radio Buttons</h4>
               </template>
               <template v-slot:body>
                  <div class="card-body">
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio6" name="customRadio-1" class="custom-control-input">
                        <label class="custom-control-label" for="customRadio6"> One </label>
                     </div>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio7" name="customRadio-1" class="custom-control-input">
                        <label class="custom-control-label" for="customRadio7"> Two </label>
                     </div>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio8" name="customRadio-1" class="custom-control-input" checked="">
                        <label class="custom-control-label" for="customRadio8"> Three </label>
                     </div>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio-8" name="customRadio-2" class="custom-control-input" checked="">
                        <label class="custom-control-label" for="customRadio-8"> Four Checked </label>
                     </div>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio9" name="customRadio-3" class="custom-control-input" disabled="">
                        <label class="custom-control-label" for="customRadio9"> Five disabled</label>
                     </div>
                     <div class="custom-control custom-radio custom-control-inline">
                        <input type="radio" id="customRadio10" name="customRadio-4" class="custom-control-input" disabled="" checked="">
                        <label class="custom-control-label" for="customRadio10"> Six Selected and  disabled</label>
                     </div>
                  </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Colored Radio Buttons</h4>
               </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-1" name="customRadio-10" class="custom-control-input bg-primary">
                        <label class="custom-control-label" for="customRadio-1"> Primary </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-2" name="customRadio-10" class="custom-control-input bg-success">
                        <label class="custom-control-label" for="customRadio-2"> Success </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-3" name="customRadio-10" class="custom-control-input bg-danger">
                        <label class="custom-control-label" for="customRadio-3"> Danger </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-4" name="customRadio-10" class="custom-control-input bg-warning">
                        <label class="custom-control-label" for="customRadio-4"> Warning </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-5" name="customRadio-10" class="custom-control-input bg-dark">
                        <label class="custom-control-label" for="customRadio-5"> Dark </label>
                     </div>
                     <div class="custom-control custom-radio custom-radio-color-checked custom-control-inline">
                        <input type="radio" id="customRadio-6" name="customRadio-10" class="custom-control-input bg-info">
                        <label class="custom-control-label" for="customRadio-6"> Info </label>
                     </div>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Radio'
}
</script>