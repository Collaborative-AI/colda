<template>
     <div class="container-fluid">
         <b-row>
            <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Flat Button</h4>
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
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-flat&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-flat&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-flat&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle btn-group-flat"> <a class="button btn button-icon bg-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle btn-group-flat"> <a class="button btn button-icon bg-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle btn-group-flat"> <a class="button btn button-icon bg-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                 </template>
               </card>
            </b-col>
            <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Edges Button</h4>
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
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle btn-group-edges"> <a class="button btn button-icon bg-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle btn-group-edges"> <a class="button btn button-icon bg-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle btn-group-edges"> <a class="button btn button-icon bg-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                   </template>
               </card>
            </b-col>
             <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Buttons</h4>
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
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                 </template>
               </card>
            </b-col>
            <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Outline Middle Buttons</h4>
                     </template>
                     <template v-slot:headerAction>
                     <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
                       <i class="ri-code-s-slash-line" />
                     </a>
                  </template>
                  <template v-slot:body>
                     <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                  </template>
               </card>
           </b-col>
             <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                 <template v-slot:headerTitle>
                        <h4 class="card-title">Outline Side Buttons</h4>
                    </template>
                    <template v-slot:headerAction>
                     <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
                       <i class="ri-code-s-slash-line" />
                     </a>
                  </template>
                 <template v-slot:body>
                    <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon bg-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                   </template>
               </card>
            </b-col>
            <b-col lg="4" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                  <template v-slot:headerTitle>
                        <h4 class="card-title">Outline Buttons</h4>
                   </template>
                   <template v-slot:headerAction>
                     <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
                       <i class="ri-code-s-slash-line" />
                     </a>
                  </template>
                  <template v-slot:body>
                     <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle&quot;&gt; &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon btn-outline-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
               </div>
            </b-collapse>
            <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle"> <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon btn-outline-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                     
                  </template>
               </card>
            </b-col>
           <b-col lg="6" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                    <template v-slot:headerTitle>
                        <h4 class="card-title">Toolbar Buttons</h4>
                     </template>
                     <template v-slot:headerAction>
                     <a class="text-primary float-right" v-b-toggle.collapse-7 role="button">
                       <i class="ri-code-s-slash-line" />
                     </a>
                  </template>
                 <template v-slot:body>
                    <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;d-flex align-items-center justify-content-center mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group1&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;1&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;2&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;3&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group2&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;4&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;5&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group3&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary rounded&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;6&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;d-flex align-items-center justify-content-center mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group1&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;1&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;2&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;3&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group2&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;4&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;5&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group3&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success rounded&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;6&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;d-flex align-items-center justify-content-center&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group1&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;1&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;2&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;3&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-edges mr-2 btn-group2&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;4&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;5&lt;/a&gt;
   &lt;/div&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group3&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning rounded&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;6&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="d-flex align-items-center justify-content-center mb-2">
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group1"> <a class="button btn button-icon bg-primary" target="_blank" href="#">1</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">2</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">3</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group2"> <a class="button btn button-icon bg-primary" target="_blank" href="#">4</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">5</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group3"> <a class="button btn button-icon bg-primary rounded" target="_blank" href="#">6</a>
                           </div>
                        </li>
                        <li class="d-flex align-items-center justify-content-center mb-2">
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group1"> <a class="button btn button-icon bg-success" target="_blank" href="#">1</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">2</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">3</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group2"> <a class="button btn button-icon bg-success" target="_blank" href="#">4</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">5</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group3"> <a class="button btn button-icon bg-success rounded" target="_blank" href="#">6</a>
                           </div>
                        </li>
                        <li class="d-flex align-items-center justify-content-center">
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group1"> <a class="button btn button-icon bg-warning" target="_blank" href="#">1</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">2</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">3</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group-edges mr-2 btn-group2"> <a class="button btn button-icon bg-warning" target="_blank" href="#">4</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">5</a>
                           </div>
                           <div class="btn-group btn-group-toggle btn-group3"> <a class="button btn button-icon bg-warning rounded" target="_blank" href="#">6</a>
                           </div>
                        </li>
                     </ul>
                  </template>
               </card>
            </b-col>
            <b-col lg="6" md="6" sm="6">
               <card class=" card-block card-stretch card-height blog">
                   <template v-slot:headerTitle>
                        <h4 class="card-title">Basic Buttons</h4>
                    </template>
                    <template v-slot:headerAction>
                     <a class="text-primary float-right" v-b-toggle.collapse-8 role="button">
                       <i class="ri-code-s-slash-line" />
                     </a>
                  </template>
                   <template v-slot:body>
                      <b-collapse id="collapse-8" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="default-buttons">
                    <code>
&lt;ul class=&quot;list-inline p-0 m-0 text-center&quot;&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-sm  btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-primary&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mb-2&quot;&gt;
   &lt;div class=&quot;btn-group btn-group-toggle  btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-success&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;li&gt;
   &lt;div class=&quot;btn-group btn-group-toggle btn-group-lg  btn-group-edges&quot;&gt; &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Left&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Middle&lt;/a&gt;
      &lt;a class=&quot;button btn button-icon bg-warning&quot; target=&quot;_blank&quot; href=&quot;#&quot;&gt;Right&lt;/a&gt;
   &lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
                     <ul class="list-inline p-0 m-0 text-center">
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle btn-group-sm  btn-group-edges"> <a class="button btn button-icon bg-primary" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-primary" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li class="mb-2">
                           <div class="btn-group btn-group-toggle  btn-group-edges"> <a class="button btn button-icon bg-success" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-success" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                        <li>
                           <div class="btn-group btn-group-toggle btn-group-lg  btn-group-edges"> <a class="button btn button-icon bg-warning" target="_blank" href="#">Left</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Middle</a>
                              <a class="button btn button-icon bg-warning" target="_blank" href="#">Right</a>
                           </div>
                        </li>
                     </ul>
                  </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
export default {
    name:'UiButtonGroups'
}
</script>