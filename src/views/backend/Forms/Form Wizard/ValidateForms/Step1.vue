<template>
    <div>
        <div class="form-card text-left">
                        <form>
                        <b-row class="setup-content" id="user-detail">
                           <b-col sm="12">
                              <b-col md="12" class="p-0">
                                 <h3 class="mb-4">User Information:</h3>
                                 <b-row>
                                    <b-col md="6" class="form-group">

                                       <label for="input-live" class="control-label">First Name</label>
                                       <b-form-input id="input-live" maxlength="100" :class="`form-control ${$v.fname.$error ? 'is-invalid' : ''}`" v-model="fname" @input="$v.fname.$touch()" @blur="$v.fname.$touch()" placeholder="Enter First Name" >
                                       </b-form-input>
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label class="control-label">Last Name</label>
                                       <input maxlength="100" type="text" :class="`form-control ${$v.lname.$error ? 'is-invalid' : ''}`"  v-model="lname" @input="$v.lname.$touch()" @blur="$v.lname.$touch()" placeholder="Enter Last Name" />
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="uname" class="control-label">User Name: *</label>
                                       <input type="text" :class="`form-control ${$v.username.$error ? 'is-invalid' : ''}`" id="uname" required="required" v-model="username" @input="$v.username.$touch()" @blur="$v.username.$touch()" placeholder="Enter User Name">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="emailid" class="control-label">Email Id: *</label>
                                       <input type="email" id="emailid" :class="`form-control ${$v.email.$error ? 'is-invalid' : ''}`" v-model="email" @input="$v.email.$touch()" @blur="$v.email.$touch()" placeholder="Email ID">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="pwd" class="control-label">Password: *</label>
                                       <input type="password" :class="`form-control ${$v.pwd.$error ? 'is-invalid' : ''}`" v-model="pwd" @input="$v.pwd.$touch()" @blur="$v.pwd.$touch()" id="pwd" placeholder="Password">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="cpwd" class="control-label">Confirm Password: *</label>
                                       <input type="password" :class="`form-control ${$v.cpwd.$error ? 'is-invalid' : ''}`" v-model="cpwd" @input="$v.cpwd.$touch()" @blur="$v.cpwd.$touch()" id="cpwd" placeholder="Confirm Password">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="cno" class="control-label">Contact Number: *</label>
                                       <input type="text" :class="`form-control ${$v.cno.$error ? 'is-invalid' : ''}`" v-model.number="cno" @input="$v.cno.$touch()" @blur="$v.cno.$touch()" id="cno" placeholder="Contact Number">
                                    </b-col>
                                    <b-col md="6" class="form-group">
                                       <label for="acno" class="control-label">Alternate Contact Number: *</label>
                                       <input type="text" :class="`form-control ${$v.acno.$error ? 'is-invalid' : ''}`" v-model="acno" @input="$v.acno.$touch()" @blur="$v.acno.$touch()" id="acno" placeholder="Alternate Contact Number">
                                    </b-col>
                                    <b-col md="12" class="mb-3 form-group">
                                       <label for="address" class="control-label">Address: *</label>
                                       <textarea name="address" :class="`form-control ${$v.address.$error ? 'is-invalid' : ''}`" v-model="address" @input="$v.address.$touch()" @blur="$v.address.$touch()" id="address" rows="5" required="required"></textarea>
                                    </b-col>
                                 </b-row>
                                 <button @click="changeTab(2)" class="btn btn-primary nextBtn btn-lg pull-right" type="button" >Next</button>
                              </b-col>
                           </b-col>
                        </b-row>
                        </form>
                     </div>
    </div>
</template>
<script>
import { validationMixin } from 'vuelidate'
import { required, email ,sameAs , integer } from 'vuelidate/lib/validators'
export default {
    name:'Step1',
    mixins: [validationMixin],
    validations: {
      fname: { required },
      lname: { required },
      username: { required },
      email:{ required , email },
      pwd:{required},
      cpwd:{required , sameAsPassword : sameAs('pwd')},
      cno:{required, integer},
      acno:{required, integer},
      address:{required}
    },
    data(){
        return{
            fname: '',
            lname: '',
            username: '',
            email:'',
            pwd:'',
            cpwd:'',
            cno:'',
            acno:'',
            address:''
        }
    },
    computed: {
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