<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="6" md="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Default</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <div class="form-group">
                        <label for="exampleFormControlTextarea1">textarea</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Horizontal Input</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <div class="form-group row align-items-center">
                        <div class="col-sm-3 col-4">
                           <label class="col-form-label">Description</label>
                        </div>
                        <div class="col-sm-9 col-8">
                           <textarea class="form-control" id="horizontalTextarea" rows="3" placeholder="Textarea"></textarea>
                        </div>
                     </div>
               </template>
            </card>
         </b-col>
         <b-col sm="12" lg="6" md="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Floating Label</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <div class="form-label-group">
                        <textarea class="form-control" id="exampleFormControlTextarea2" rows="4"
                           placeholder="Label in Textarea"></textarea>
                        <label>Textarea</label>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Counter</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <div class="form-label-group mb-0">
                        <textarea data-length="20" class="form-control" id="exampleFormControlTextarea3" rows="3"
                           placeholder="Counter"></textarea>
                        <label>Counter</label>
                     </div>
                     <small class="counter-value-text float-right"><span class="char-count">0</span> / 20 </small>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'TextArea'
}
</script>