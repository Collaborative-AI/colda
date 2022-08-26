<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="12">
            <card>
               <template v-slot:headerTitle>
                           <h4 class="card-title">Basic Checkbox</h4>
               </template>
               <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                           <div class="checkbox d-inline-block mr-3">
                              <input type="checkbox" class="checkbox-input" id="checkbox1">
                              <label for="checkbox1">Primary-Inactive</label>
                           </div>
                           <div class="checkbox d-inline-block mr-3">
                              <input type="checkbox" class="checkbox-input" id="checkbox2" checked="">
                              <label for="checkbox2">Primary / Active</label>
                           </div>
                           <div class="checkbox d-inline-block mr-3">
                              <input type="checkbox" class="checkbox-input" id="checkbox3" disabled="">
                              <label for="checkbox3">Disable / Inactive</label>
                           </div>
                           <div class="checkbox d-inline-block mr-3">
                              <input type="checkbox" class="checkbox-input" id="checkbox4" checked="" disabled="">
                              <label for="checkbox4">Active / Disable</label>
                           </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                           <h4 class="card-title">Custom Checkbox</h4>
               </template>
                     <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck5">
                           <label class="custom-control-label" for="customCheck5">Primary / Inactive</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck6" Checked="">
                           <label class="custom-control-label" for="customCheck6">Primary - active</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck7"  disabled="">
                           <label class="custom-control-label" for="customCheck7">Primary - inactive - disabled</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck8"  checked="" disabled="">
                           <label class="custom-control-label" for="customCheck8">Primary - active - disabled</label>
                        </div>
                     </template>
            </card>
            <card>            
               <template v-slot:headerTitle>
                           <h4 class="card-title">Color</h4>
               </template>
               <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-primary" id="customCheck-1" checked="">
                           <label class="custom-control-label" for="customCheck-1"> Primary</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-success" id="customCheck-2" checked="">
                           <label class="custom-control-label" for="customCheck-2">Success</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-danger" id="customCheck-3" checked="">
                           <label class="custom-control-label" for="customCheck-3">Danger</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-warning" id="customCheck-4" checked="">
                           <label class="custom-control-label" for="customCheck-4">Warning</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-dark" id="customCheck-5" checked="">
                           <label class="custom-control-label" for="customCheck-5">Dark</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color-check custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-info" id="customCheck-6" checked="">
                           <label class="custom-control-label" for="customCheck-6">Info</label>
                        </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                           <h4 class="card-title">Custom Color</h4>
               </template>
               <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-primary" id="customCheck-11">
                           <label class="custom-control-label" for="customCheck-11">Primary </label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-success" id="customCheck-22">
                           <label class="custom-control-label" for="customCheck-22">Success</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-danger" id="customCheck-33">
                           <label class="custom-control-label" for="customCheck-33">Danger</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-warning" id="customCheck-44">
                           <label class="custom-control-label" for="customCheck-44">Warning</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-dark" id="customCheck-55">
                           <label class="custom-control-label" for="customCheck-55">Dark</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-checkbox-color custom-control-inline">
                           <input type="checkbox" class="custom-control-input bg-info" id="customCheck-66">
                           <label class="custom-control-label" for="customCheck-66"> Info</label>
                        </div>
               </template>
            </card>
            <card>
                  <template v-slot:headerTitle>
                           <h4 class="card-title">Change Icon</h4>
                  </template>
                     <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-10" checked="">
                           <label class="custom-control-label" for="customCheck-10"><i class="fa fa-music"></i>Music</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-20" checked="">
                           <label class="custom-control-label" for="customCheck-20"><i class="fa fa-commenting-o"></i>SMS</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-30" checked="">
                           <label class="custom-control-label" for="customCheck-30"><i class="fa fa-times"></i>Cancel</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-40" checked="">
                           <label class="custom-control-label" for="customCheck-40"><i class="fa fa-file"></i>File</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-50" checked="">
                           <label class="custom-control-label" for="customCheck-50"><i class="fa fa-bold"></i>Bold</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-60" checked="">
                           <label class="custom-control-label" for="customCheck-60"><i class="fa fa-map-marker"></i>Location</label>
                        </div>
                        <div class="custom-control custom-checkbox checkbox-icon custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-70" checked="">
                           <label class="custom-control-label" for="customCheck-70"><i class="fa fa-camera"></i>Camera</label>
                        </div>
                     </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                           <h4 class="card-title">Boolean Checkbox</h4>
               </template>
               <template v-slot:body>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam nibh finibus leo</p>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-t" checked="">
                           <label class="custom-control-label" for="customCheck-t">True</label>
                        </div>
                        <div class="custom-control custom-checkbox custom-control-inline">
                           <input type="checkbox" class="custom-control-input" id="customCheck-f">
                           <label class="custom-control-label" for="customCheck-f">False</label>
                        </div>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Checkbox'
}
</script>