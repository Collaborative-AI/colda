<template>
    <div>
        <b-row class="setup-content" id="bank-detail">
                           <b-col sm="12">
                              <b-col md="12" class="p-0">
                                 <h3 class="mb-4">Bank Detail:</h3>
                                 <b-row>
                                    <b-col md="6" class="form-group">
                                       <label for="panno" class="control-label">Pan No: *</label>
                                       <input type="text" :class="`form-control ${$v.panno.$error ? 'is-invalid' : ''}`"  v-model="panno" @input="$v.panno.$touch()" @blur="$v.panno.$touch()" id="panno" placeholder="Pan No.">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="apanno" class="control-label">Account No: *</label>
                                       <input type="text" :class="`form-control ${$v.accno.$error ? 'is-invalid' : ''}`"  v-model="accno" @input="$v.accno.$touch()" @blur="$v.accno.$touch()" id="accno" placeholder="Account No.">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="accname" class="control-label">Account Holder Name: *</label>
                                       <input type="text" :class="`form-control ${$v.accname.$error ? 'is-invalid' : ''}`"  v-model="accname" @input="$v.accname.$touch()" @blur="$v.accname.$touch()" id="accname" placeholder="Account Holder Name.">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="ifsc" class="control-label">IFSC Code: *</label>
                                       <input type="text" :class="`form-control ${$v.ifsc.$error ? 'is-invalid' : ''}`"  v-model="ifsc" @input="$v.ifsc.$touch()" @blur="$v.ifsc.$touch()" id="ifsc" placeholder="IFSC Code.">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="bankname" class="control-label">Bank Name: *</label>
                                       <input type="text" :class="`form-control ${$v.bankname.$error ? 'is-invalid' : ''}`"  v-model="bankname" @input="$v.bankname.$touch()" @blur="$v.bankname.$touch()" id="bankname" name="bankname" placeholder="Bank Name.">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="branch" class="control-label">Bank Branch Name: *</label>
                                       <input type="text" :class="`form-control ${$v.branch.$error ? 'is-invalid' : ''}`"  v-model="branch" @input="$v.branch.$touch()" @blur="$v.branch.$touch()" id="branch" placeholder="Bank Branch Name.">
                                    </b-col>
                                 </b-row>
                                 <button @click="changeTab(4)" class="btn btn-primary nextBtn btn-lg pull-right" type="button" >Next</button>
                              </b-col>
                           </b-col>
                        </b-row>
    </div>
</template>
<script>
import { validationMixin } from 'vuelidate'
import { required, integer } from 'vuelidate/lib/validators'
export default {
   name:'Step3',
   mixins: [validationMixin],
   validations: {
      panno: { required },
      accno: { required, integer },
      accname: { required },
      ifsc: { required },
      bankname: { required },
      branch: { required }
   },
   data(){
      return{
         panno:'',
         accno:'',
         accname:'',
         ifsc:'',
         bankname:'',
         branch:''
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