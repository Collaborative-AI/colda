<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="12">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Validate Wizard</h4>
               </template>
               <template v-slot:body>
                     <div class="stepwizard mt-4">
                        <div class="stepwizard-row setup-panel">
                           <div :class="checkActive(0, 1)" id="user" class="wizard-step active">
                              <a href="#user-detail" class="active btn">
                              <i class="ri-lock-unlock-line text-primary"></i><span>User Detail</span>
                              </a>
                           </div>
                           <div :class="checkActive(1, 2)" id="document" class="wizard-step">
                              <a href="#document-detail" class="btn btn-default disabled" >
                              <i class="ri-user-fill text-danger"></i><span>Document Detail</span>
                              </a>
                           </div>
                           <div :class="checkActive(2, 3)" id="bank" class="wizard-step">
                              <a href="#bank-detail" class="btn btn-default disabled">
                              <i class="ri-camera-fill text-success"></i><span>Bank Detail</span>
                              </a>
                           </div>
                           <div :class="checkActive(3, 4)" id="confirm" class="wizard-step">
                              <a href="#cpnfirm-data" class="btn btn-default disabled">
                              <i class="ri-check-fill text-warning"></i><span>Confirm</span>
                              </a>
                           </div>
                        </div>
                     </div>
                     <fieldset :class="current == 1 ? 'd-block' : 'd-none'">
                        <Step1 @onNext="changeTab" />
                     </fieldset>
                     <fieldset :class="current == 2 ? 'd-block' : 'd-none'">
                        <Step2 @onNext="changeTab" />
                     </fieldset>
                     <fieldset :class="current == 3 ? 'd-block' : 'd-none'">
                        <Step3 @onNext="changeTab" />
                     </fieldset>
                     <fieldset :class="current == 4 ? 'd-block' : 'd-none'">
                        <Step4 @onNext="changeTab" />
                     </fieldset>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
import Step1 from './ValidateForms/Step1'
import Step2 from './ValidateForms/Step2'
import Step3 from './ValidateForms/Step3'
import Step4 from './ValidateForms/Step4'

export default {
    name:'Validate',
    components:{
       Step1,
       Step2,
       Step3,
       Step4,
    },
    data () {
       return {
          current: 1,
          name: ''
       }
    },
    methods: {
       changeTab(tab) {
          this.current = tab
          window.scrollTo({ top: 0, behavior: 'smooth' });
       },
       checkActive(item,active){
          let className = '';
          if (this.current > item) {
             className = 'active'
          }
          if(this.current > active) {
             className = className + ' done'
          }
          return className
       }
    },
    
}
</script>