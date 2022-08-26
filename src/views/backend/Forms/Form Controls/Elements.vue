<template>
   <b-container fluid="">
      <b-row>
         <b-col sm="12" lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Form</h4>
               </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="email">Email address:</label>
                           <input type="email" class="form-control" id="email1">
                        </div>
                        <div class="form-group">
                           <label for="pwd">Password:</label>
                           <input type="password" class="form-control" id="pwd">
                        </div>
                        <div class="checkbox mb-3">
                           <label><input type="checkbox"> Remember me</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Form Grid</h4>
               </template>
                  <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="row">
                           <div class="col">
                              <input type="text" class="form-control" placeholder="First name">
                           </div>
                           <div class="col">
                              <input type="text" class="form-control" placeholder="Last name">
                           </div>
                        </div>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Textarea</h4>
               </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="exampleFormControlTextarea1"> textarea</label>
                           <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Telephone</h4>
               </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="exampleInputphone">Teliphone Input</label>
                           <input type="tel" class="form-control" id="exampleInputphone" value="1-(555)-555-5555">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Search</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="search-text">Search</label>
                           <input id="search-text" type="search" class="form-control" required="">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input</h4>
                </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="exampleInputText1">Input Text </label>
                           <input type="text" class="form-control" id="exampleInputText1" value="Mark Tech"
                              placeholder="Enter Name">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputEmail2">Email Input</label>
                           <input type="email" class="form-control" id="exampleInputEmail2" value="markTech@gmail.com"
                              placeholder="Enter Email">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputNumber3">Number Input</label>
                           <input type="number" class="form-control" id="exampleInputNumber3" value="123456">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputPassword4">Password Input</label>
                           <input type="password" class="form-control" id="exampleInputPassword4" value="example123"
                              placeholder="Enter Password">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Size</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="colFormLabelSm">Small</label>
                           <input type="email" class="form-control form-control-sm" id="colFormLabelSm"
                              placeholder="form-control-sm">
                        </div>
                        <div class="form-group">
                           <label for="colFormLabel">Default</label>
                           <input type="email" class="form-control" id="colFormLabel" placeholder="form-control">
                        </div>
                        <div class="form-group mb-0">
                           <label for="colFormLabelLg" class="pb-0">Large</label>
                           <input type="email" class="form-control form-control-lg" id="colFormLabelLg"
                              placeholder="form-control-lg">
                        </div>
                     </form>
               </template>
            </card>
         </b-col>
         <b-col sm="12" lg="6">
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Horizontal Form</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form class="form-horizontal" action="/action_page.php">
                        <div class="form-group row">
                           <label class="control-label col-sm-3 align-self-center" for="email">Email:</label>
                           <div class="col-sm-9">
                              <input type="email" class="form-control" id="email" placeholder="Enter Your  email">
                           </div>
                        </div>
                        <div class="form-group row">
                           <label class="control-label col-sm-3 align-self-center" for="pwd1">Password:</label>
                           <div class="col-sm-9">
                              <input type="password" class="form-control" id="pwd1" placeholder="Enter Your password">
                           </div>
                        </div>
                        <div class="form-group">
                           <div class="checkbox">
                              <label><input type="checkbox"> Remember me</label>
                           </div>
                        </div>
                        <div class="form-group">
                           <button type="submit" class="btn btn-primary">Submit</button>
                           <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                        </div>
                     </form>
               </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Form row</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-row">
                           <div class="col">
                              <input type="text" class="form-control" placeholder="First name">
                           </div>
                           <div class="col">
                              <input type="text" class="form-control" placeholder="Last name">
                           </div>
                        </div>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Url</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="exampleInputurl">Url Input</label>
                           <input type="url" class="form-control" id="exampleInputurl" value="https://getbootstrap.com"
                              placeholder="Enter Url">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Range</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="formControlRange">Range input</label>
                           <input type="range" class="form-control-range" id="formControlRange">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Custom Range</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="customRange1">Range Input</label>
                           <input type="range" class="custom-range" id="customRange1">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input Choose file</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <div class="custom-file">
                              <input type="file" class="custom-file-input" id="customFile">
                              <label class="custom-file-label" for="customFile">Choose file</label>
                           </div>
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Input</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <form>
                        <div class="form-group">
                           <label for="exampleInputDisabled5">Disabled Input</label>
                           <input type="text" class="form-control" id="exampleInputDisabled5" disabled="" value="Mark Tech">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputPlaceholder">Placeholder</label>
                           <input type="text" class="form-control" id="exampleInputPlaceholder"
                              placeholder="This is Placeholder">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputReadonly">Readonly</label>
                           <input type="text" class="form-control" id="exampleInputReadonly" readonly="" value="Mark Tech">
                        </div>
                        <div class="form-group">
                           <label for="exampleInputcolor">Input Color </label>
                           <input type="color" class="form-control" id="exampleInputcolor" value="#4788ff">
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                        <button type="submit" class="btn bg-danger ml-1">Cancel</button>
                     </form>
                  </template>
            </card>
            <card>
               <template v-slot:headerTitle>
                        <h4 class="card-title">Select Size</h4>
                     </template>
               <template v-slot:body>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vulputate, ex ac venenatis mollis, diam
                        nibh finibus leo</p>
                     <div class="form-group">
                        <label>Small</label>
                        <select class="form-control form-control-sm mb-3">
                           <option selected="">Open this select menu</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div>
                     <div class="form-group">
                        <label>Default</label>
                        <select class="form-control mb-3">
                           <option selected="">Open this select menu</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div>
                     <div class="form-group">
                        <label>Large</label>
                        <select class="form-control form-control-lg">
                           <option selected="">Open this select menu</option>
                           <option value="1">One</option>
                           <option value="2">Two</option>
                           <option value="3">Three</option>
                        </select>
                     </div>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'Elements'
}
</script>