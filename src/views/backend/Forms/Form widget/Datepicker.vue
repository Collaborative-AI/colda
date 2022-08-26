<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Basic</h4>
                     </template>
               <template v-slot:body>
                     <div class="form-group">
                        <label for="exampleInputdate">Date Input</label>
                        <input type="date" class="form-control" id="exampleInputdate" value="2019-12-18">
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Month Date</h4>
               </template>
               <template v-slot:body>
                     <div class="form-group">
                        <label for="exampleInputmonth">Month Input</label>
                        <input type="month" class="form-control" id="exampleInputmonth" value="2019-12">
                     </div>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Time</h4>
               </template>
               <template v-slot:body>
                     <div class="form-group">
                        <label for="exampleInputtime">Time Input</label>
                        <input type="time" class="form-control" id="exampleInputtime" value="13:45">
                     </div>
               </template>
            </card>
         </b-col>
         <b-col lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Week</h4>
               </template>
               <template v-slot:body>
                     <div class="form-group">
                     <label for="exampleInputweek">Week Input</label>
                     <input type="week" class="form-control" id="exampleInputweek" value="2019-W46">
                  </div> 
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Date and Time</h4>
               </template>
               <template v-slot:body>
                     <div class="form-group">
                        <label for="exampleInputdatetime">Date and Time Input</label>
                        <input type="datetime-local" class="form-control" id="exampleInputdatetime" value="2019-12-19T13:45:00">
                     </div>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Datepicker'
}
</script>