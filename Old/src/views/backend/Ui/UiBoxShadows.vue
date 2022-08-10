<template>
    <div class="container-fluid">
         <b-row>
            <b-col lg="12">
               <card class=" card-block card-stretch card-height">
                   <template v-slot:body>
                     <h4>Box Shadow</h4>
                     <p class="mb-0">A box shadow is an enclosed glass-front display case containing an object or objects presented in a thematic grouping with artistic or personal significance. The grouping of the objects and the depth effect created by their relative heights from the backing creates a dramatic visual result.</p>
                  </template>
               </card>
            </b-col>
            <b-col lg="12">
               <card class=" card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Shadows</h4>
                    </template>
                    <template v-slot:headerAction>
                       <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
                         <i class="ri-code-s-slash-line" />
                       </a>
                     </template>
                   <template v-slot:body>
                      <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;div class=&quot;row&quot;&gt;
   &lt;div class=&quot;col-sm-6 col-md-6 col-lg-3&quot;&gt;
      &lt;div class=&quot;shadow-lg p-4 shadow-showcase text-center&quot;&gt;
         &lt;h6&gt;Larger shadow&lt;/h6&gt;
      &lt;/div&gt;
   &lt;/div&gt;
   &lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0&quot;&gt;
      &lt;div class=&quot;shadow p-4 shadow-showcase text-center&quot;&gt;
         &lt;h6&gt;Regular shadow&lt;/h6&gt;
      &lt;/div&gt;
   &lt;/div&gt;
   &lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
      &lt;div class=&quot;shadow-sm p-4 shadow-showcase text-center&quot;&gt;
         &lt;h6&gt;Small shadow&lt;/h6&gt;
      &lt;/div&gt;
   &lt;/div&gt;
   &lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
      &lt;div class=&quot;shadow-none p-4 shadow-showcase text-center&quot;&gt;
         &lt;h6&gt;No shadow&lt;/h6&gt;
      &lt;/div&gt;
   &lt;/div&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <div class="row">
                        <div class="col-sm-6 col-md-6 col-lg-3">
                           <div class="shadow-lg p-4 shadow-showcase text-center">
                              <h6>Larger shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0">
                           <div class="shadow p-4 shadow-showcase text-center">
                              <h6>Regular shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="shadow-sm p-4 shadow-showcase text-center">
                              <h6>Small shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="shadow-none p-4 shadow-showcase text-center">
                              <h6>No shadow</h6>
                           </div>
                        </div>
                     </div>
                   </template>
               </card>
            </b-col>
              <b-col lg="12">
               <card class=" card-block card-stretch card-height">
                    <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Shadow</h4>
                    </template>
                    <template v-slot:headerAction>
                       <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
                         <i class="ri-code-s-slash-line" />
                       </a>
                     </template>
                   <template v-slot:body>
                                            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;div class=&quot;row&quot;&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3&quot;&gt;
   &lt;div class=&quot;bottom-left p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Bottom left&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0&quot;&gt;
   &lt;div class=&quot;top-left p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Top Left&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
   &lt;div class=&quot;bottom-right p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Bottom right&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
   &lt;div class=&quot;top-right p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Top right&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <div class="row">
                        <div class="col-sm-6 col-md-6 col-lg-3">
                           <div class="bottom-left p-4 shadow-showcase text-center">
                              <h6>Bottom left</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0">
                           <div class="top-left p-4 shadow-showcase text-center">
                              <h6>Top Left</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="bottom-right p-4 shadow-showcase text-center">
                              <h6>Bottom right</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="top-right p-4 shadow-showcase text-center">
                              <h6>Top right</h6>
                           </div>
                        </div>
                     </div>
                   </template>
               </card>
              </b-col>
            <b-col lg="12">
               <card class=" card-block card-stretch card-height">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Drop Shadow</h4>
                      </template>
                      <template v-slot:headerAction>
                       <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
                         <i class="ri-code-s-slash-line" />
                       </a>
                     </template>
                  <template v-slot:body>
                     <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;div class=&quot;row&quot;&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3&quot;&gt;
   &lt;div class=&quot;shadow-bottom p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Bottom shadow&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0&quot;&gt;
   &lt;div class=&quot;basic-drop-shadow p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Basic Shadow&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
   &lt;div class=&quot;inner-shadow p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;inner Shadow&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;div class=&quot;col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0&quot;&gt;
   &lt;div class=&quot;blur-shadow p-4 shadow-showcase text-center&quot;&gt;
      &lt;h6&gt;Blur Shadow&lt;/h6&gt;
   &lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <div class="row">
                        <div class="col-sm-6 col-md-6 col-lg-3">
                           <div class="shadow-bottom p-4 shadow-showcase text-center">
                              <h6>Bottom shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-md-0">
                           <div class="basic-drop-shadow p-4 shadow-showcase text-center">
                              <h6>Basic Shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="inner-shadow p-4 shadow-showcase text-center">
                              <h6>inner Shadow</h6>
                           </div>
                        </div>
                        <div class="col-sm-6 col-md-6 col-lg-3 mt-3 mt-lg-0">
                           <div class="blur-shadow p-4 shadow-showcase text-center">
                              <h6>Blur Shadow</h6>
                           </div>
                        </div>
                     </div>
                 </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
export default {
    name:'UiBoxShadows'
}
</script>