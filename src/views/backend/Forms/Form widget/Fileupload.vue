<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Default</h4>
               </template>
               <template v-slot:body>
                     <form action="/action_page.php">
                        <p>Custom file:</p>
                        <div class="custom-file mb-3">
                           <input type="file" class="custom-file-input" id="customFile" name="filename">
                           <label class="custom-file-label" for="customFile">Choose file</label>
                        </div>
                        <p>Default file:</p>
                        <input type="file" id="myFile" name="filename2">
                        <div class="mt-3">
                           <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                     </form>
               </template>
            </card>
         </b-col>
         <b-col lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title"> file input</h4>
               </template>
               <template v-slot:body>
                     <form id="file-upload-form" class="uploader-file" action="/action_page.php">
                        <input id="file-upload" type="file" name="fileUpload" accept="image/*" />
                        <label id="file-drag">
                           <img id="file-image" src="#" alt="Preview" class="hidden">
                           <span id="start-one">
                              <i class="fa fa-download" aria-hidden="true"></i>
                              <span class="d-block">Select a file or drag here</span>
                              <span id="notimage" class="hidden d-block">Please select image</span>
                              <span id="file-upload-btn" class="btn btn-primary">Select a file</span>
                           </span>
                           <span id="response" class="hidden">
                           <span id="messages"></span>
                           <progress class="progress" id="file-progress" value="0">
                              <span>0</span>%
                           </progress>
                           </span>
                        </label>
                     </form>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Fileupload'
}
</script>