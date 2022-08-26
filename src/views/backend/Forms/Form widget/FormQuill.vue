<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Quill Editor</h4>
               </template>
               <template v-slot:body>
                     <vue-editor></vue-editor>                     
               </template>
            </card>
         </b-col>
         <b-col lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custom Select</h4>
               </template>
               <template v-slot:body>
                  <vue-editor v-model="content"></vue-editor> 
         
                           
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
import { VueEditor } from 'vue2-editor'
export default {
    name:'FormQuill',
    components:{
       VueEditor,
    },
    data(){
       return{
          content:'<h1>This is a heading text...</h1><br/>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla dui arcu, pellentesque id mattis sed, mattis semper erat. Etiam commodo arcu a mollis consequat. Curabitur pretium auctor tortor, bibendum placerat elit feugiat et. Ut ac turpis nec dui ullamcorper ornare. Vestibulum finibus quis magna at accumsan. Praesent a purus vitae tortor fringilla tempus vel non purus. Suspendisse eleifend nibh porta dolor ullamcorper laoreet. Ut sit amet ipsum vitae lectus pharetra tincidunt. In ipsum quam, iaculis at erat ut, fermentum efficitur ipsum. Nunc odio diam, fringilla in auctor et, scelerisque at lorem. Sed convallis tempor dolor eu dictum. Cras ornare ornare imperdiet. Pellentesque sagittis lacus non libero fringilla faucibus. Aenean ullamcorper enim et metus vestibulum, eu aliquam nunc placerat. Praesent fringilla dolor sit amet leo pulvinar semper. '
       }
    }
}
</script>