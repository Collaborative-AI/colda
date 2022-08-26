<template>
    <div>
         <b-row class="setup-content" id="document-detail">
                           <b-col sm="12">
                              <b-col md="12" class="p-0">
                                 <h3 class="mb-4">Document Details:</h3>
                                 <b-row>
                                    <b-col md="6" class="form-group">
                                       <label for="fname" class="control-label">Company Name: *</label>
                                       <input type="text" :class="`form-control ${$v.cname.$error ? 'is-invalid' : ''}`"  v-model="cname" @input="$v.cname.$touch()" @blur="$v.cname.$touch()" id="cname" placeholder="Company Name">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <div class="form-group">
                                          <label for="ccno" class="control-label">Contact Number: *</label>
                                          <input type="text" :class="`form-control ${$v.ccno.$error ? 'is-invalid' : ''}`"  v-model="ccno" @input="$v.ccno.$touch()" @blur="$v.ccno.$touch()" id="ccno" placeholder="Contact Number">
                                       </div>
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <div class="form-group">
                                          <label for="url" class="control-label">Company Url: *</label>
                                          <input type="text" :class="`form-control ${$v.url.$error ? 'is-invalid' : ''}`"  v-model="url" @input="$v.url.$touch()" @blur="$v.cname.$touch()" id="url" placeholder="Company Url.">
                                       </div>
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <div class="form-group">
                                          <label for="cemail" class="control-label">Company Mail Id: *</label>
                                          <input type="email" :class="`form-control ${$v.cemail.$error ? 'is-invalid' : ''}`"  v-model="cemail" @input="$v.cemail.$touch()" @blur="$v.cemail.$touch()" id="cemail" placeholder="Company Mail Id.">
                                       </div>
                                    </b-col>
                                    <b-col md="12">
                                       <div class="form-group">
                                          <label for="cadd" class="control-label">Company Address: *</label>
                                          <textarea name="cadd" id="cadd" :class="`form-control ${$v.cadd.$error ? 'is-invalid' : ''}`"  v-model="cadd" @input="$v.cadd.$touch()" @blur="$v.cadd.$touch()" rows="5"></textarea>
                                       </div>
                                   </b-col>
                                 </b-row>
                                 <button @click="changeTab(3)" class="btn btn-primary nextBtn btn-lg pull-right" type="button" >Next</button>
                              </b-col>
                           </b-col>
                        </b-row>
    </div>
</template>
<script>
import { validationMixin } from 'vuelidate'
import { required, email, integer, url	  } from 'vuelidate/lib/validators'
export default {
    name : 'Step2',
    mixins: [validationMixin],
    validations: {
      cname: { required },
      ccno: { required, integer },
      url: { required ,url	 },
      cemail: { required , email},
      cadd : { required }
    },
    data(){
       return{
          cname:'',
          ccno:'',
          url:'',
          cemail:'',
          cadd:''
       }
    },
    methods: {
        submit () {
            this.$v.$touch()
        },
        changeTab(value){
            this.$v.$touch()
            if (!this.$v.$invalid) {
                this.$emit('onNext', value) 
            }
        }
    }
}
</script>