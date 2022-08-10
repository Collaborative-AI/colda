<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Basic select boxes</h4>
               </template>
               <template v-slot:body>
                     <select class="form-control" id="sel1" name="sellist1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                     </select>
               </template>
            </card>
           <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Mutiple select</h4>
               </template>
               <template v-slot:body>
                     <select multiple class="form-control" id="sel2" name="sellist2">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                     </select>
               </template>
           </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Select with Input Group</h4>
               </template>
               <template v-slot:body>
                     <div class="input-group mb-3">
                        <div class="input-group-prepend">
                           <label class="input-group-text" for="inputGroupSelect01">Options</label>
                        </div>
                        <select class="form-control" id="inputGroupSelect01">
                           <option selected="">Choose...</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div>
                     <div class="input-group">
                        <select class="form-control" id="inputGroupSelect02">
                           <option selected="">Choose...</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                        <div class="input-group-append">
                           <label class="input-group-text" for="inputGroupSelect02">Options</label>
                        </div>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Single Select2</h4>
               </template>
               <template v-slot:body>
                     <div class="form-group">
                        <Select2 :options="singleOption" v-model="singleSelect">
                           <option>Select</option>
                        </Select2>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Multiple Select2</h4>
               </template>
               <template v-slot:body>
                     <Select2 :options="singleOption1" v-model="singleSelect1" multiple>
                           <option>Select</option>
                     </Select2>
               </template>
            </card>
         </b-col>
         <b-col lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custom Select</h4>
               </template>
               <template v-slot:body>
                     <select class="custom-select form-control">
                        <option selected="">Open this menu</option>
                        <option value="IT">IT</option>
                        <option value="Blade Runner">Blade Runner</option>
                        <option value="Thor Ragnarok">Thor Ragnarok</option>
                     </select>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Disabled Select</h4>
               </template>
               <template v-slot:body>
                     <select disabled="disabled" id="disabledSelect" class="form-control">
                        <option>Disabled select</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                     </select>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custome Select with Input Group</h4>
               </template>
               <template v-slot:body>
                     <div class="input-group mb-3">
                        <div class="input-group-prepend">
                           <label class="input-group-text" for="inputGroupSelect03">Options</label>
                        </div>
                        <select class="custom-select" id="inputGroupSelect03">
                           <option selected>Choose...</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div>
                     <div class="input-group">
                        <select class="custom-select" id="inputGroupSelect04">
                           <option selected>Choose...</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                        <div class="input-group-append">
                           <label class="input-group-text" for="inputGroupSelect04">Options</label>
                        </div>
                     </div>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Custom Select Menu Sizing</h4>
               </template>
               <template v-slot:body>
                     <form>
                        <select class="custom-select custom-select-sm mb-3">
                           <option selected>Small Custom Select Menu</option>
                           <option value="volvo">Volvo</option>
                           <option value="fiat">Fiat</option>
                           <option value="audi">Audi</option>
                        </select>
                        <select name="cars" class="custom-select mb-3">
                           <option selected>Default Custom Select Menu</option>
                           <option value="volvo">Volvo</option>
                           <option value="fiat">Fiat</option>
                           <option value="audi">Audi</option>
                        </select>
                        <select name="cars" class="custom-select custom-select-lg mb-3">
                           <option selected>Large Custom Select Menu</option>
                           <option value="volvo">Volvo</option>
                           <option value="fiat">Fiat</option>
                           <option value="audi">Audi</option>
                        </select>
                     </form>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'SelectComponents',
    data() {
      return {
         singleSelect: '',
         singleSelect1: '',
         singleOption: [
            { id: 1, text: "Java" },
            { id: 2, text: "PHP" },
            { id: 3, text: "JavaScript" },
            { id: 4, text: "Visual Basics" }
         ],
         singleOption1: [
            { id: 1, text: "Red" },
            { id: 2, text: "Green" },
            { id: 3, text: "Blue" },
            { id: 4, text: "Yellow" }
         ],
      }
    }
}
</script>