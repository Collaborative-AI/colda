<template>
  <b-container fluid>
    <b-row>
      <b-col sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Grid options</h4>
          </template>
          <template v-slot:body>
            <p>See how aspects of the Bootstrap grid system work across multiple devices with a handy table..</p>
            <table class="table table-bordered table-striped">
              <thead>
                <tr>
                  <th></th>
                  <th class="text-center">
                    Extra small<br>
                    <small>&lt;576px</small>
                  </th>
                  <th class="text-center">
                    Small<br>
                    <small>≥576px</small>
                  </th>
                  <th class="text-center">
                    Medium<br>
                    <small>≥768px</small>
                  </th>
                  <th class="text-center">
                    Large<br>
                    <small>≥992px</small>
                  </th>
                  <th class="text-center">
                    Extra large<br>
                    <small>≥1200px</small>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Max container width</th>
                  <td>None (auto)</td>
                  <td>540px</td>
                  <td>720px</td>
                  <td>960px</td>
                  <td>1140px</td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Prop</th>
                  <td><code>cols="*"</code></td>
                  <td><code>sm="*"</code></td>
                  <td><code>md="*"</code></td>
                  <td><code>lg="*"</code></td>
                  <td><code>xl="*"</code></td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row"># of columns</th>
                  <td colspan="5">12</td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Gutter width</th>
                  <td colspan="5">30px (15px on each side of a column)</td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Nestable</th>
                  <td colspan="5">Yes</td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Offset</th>
                  <td><code>offset="*"</code></td>
                  <td><code>offset-sm="*"</code></td>
                  <td><code>offset-md="*"</code></td>
                  <td><code>offset-lg="*"</code></td>
                  <td><code>offset-xl="*"</code></td>
                </tr>
                <tr>
                  <th class="text-nowrap text-left" scope="row">Column ordering</th>
                  <td><code>order="*"</code></td>
                  <td><code>order-sm="*"</code></td>
                  <td><code>order-md="*"</code></td>
                  <td><code>order-lg="*"</code></td>
                  <td><code>order-xl="*"</code></td>
                </tr>
              </tbody>
            </table>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Equal-width</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>For example, here are two grid layouts that apply to every device and viewport, from <code>xs</code> to <code>xl</code>. Add any number of unit-less classes for each breakpoint you need and every column will be the same width.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-2">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;!-- Stack the columns on mobile by making one full-width and the other half-width --&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col cols="12" md="8"&gt; cols="12" md="8"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt; cols="6" md="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop --&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col cols="6" md="4"&gt; cols="6" md="4"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt; cols="6" md="4"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt; cols="6" md="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;!-- Columns are always 50% wide, on mobile and desktop --&gt;
    &lt;b-row&gt;
      &lt;b-col cols="6"&gt; cols="6"&lt;/b-col&gt;
      &lt;b-col cols="6"&gt; cols="6"&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <!-- Stack the columns on mobile by making one full-width and the other half-width -->
                <b-row class="mb-3">
                  <b-col cols="12" md="8"> cols="12" md="8"</b-col>
                  <b-col cols="6" md="4"> cols="6" md="4"</b-col>
                </b-row>
                <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
                <b-row class="mb-3">
                  <b-col cols="6" md="4"> cols="6" md="4"</b-col>
                  <b-col cols="6" md="4"> cols="6" md="4"</b-col>
                  <b-col cols="6" md="4"> cols="6" md="4"</b-col>
                </b-row>
                <!-- Columns are always 50% wide, on mobile and desktop -->
                <b-row>
                  <b-col cols="6"> cols="6"</b-col>
                  <b-col cols="6"> cols="6"</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Setting one column width</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Auto-layout for flexbox grid columns also means you can set the width of one column and have the sibling columns automatically resize around it. You may use predefined grid classes (as shown below), grid mixins, or inline widths. Note that the other columns will resize no matter the width of the center column.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-3">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col&gt;1 of 3&lt;/b-col&gt;
      &lt;b-col cols="6"&gt;2 of 3 (wider)&lt;/b-col&gt;
      &lt;b-col&gt;3 of 3&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row&gt;
      &lt;b-col&gt;1 of 3&lt;/b-col&gt;
      &lt;b-col cols="5"&gt;2 of 3 (wider)&lt;/b-col&gt;
      &lt;b-col&gt;3 of 3&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row class="mb-3">
                  <b-col>1 of 3</b-col>
                  <b-col cols="6">2 of 3 (wider)</b-col>
                  <b-col>3 of 3</b-col>
                </b-row>
                <b-row>
                  <b-col>1 of 3</b-col>
                  <b-col cols="5">2 of 3 (wider)</b-col>
                  <b-col>3 of 3</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Variable width content</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use <code>col-{breakpoint}-auto</code> classes to size columns based on the natural width of their content.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-4">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row class="justify-content-md-center mb-3"&gt;
      &lt;b-col col lg="2"&gt;1 of 3&lt;/b-col&gt;
      &lt;b-col md="auto"&gt;Variable width content&lt;/b-col&gt;
      &lt;b-col col lg="2"&gt;3 of 3&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row&gt;
      &lt;b-col&gt;1 of 3&lt;/b-col&gt;
      &lt;b-col md="auto"&gt;Variable width content&lt;/b-col&gt;
      &lt;b-col col lg="2"&gt;3 of 3&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row class="justify-content-md-center mb-3">
                  <b-col col lg="2">1 of 3</b-col>
                  <b-col md="auto">Variable width content</b-col>
                  <b-col col lg="2">3 of 3</b-col>
                </b-row>
                <b-row>
                  <b-col>1 of 3</b-col>
                  <b-col md="auto">Variable width content</b-col>
                  <b-col col lg="2">3 of 3</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Equal-width multi-row</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Create equal-width columns that span multiple rows by inserting a <code>.w-100</code> where you want the columns to break to a new line. Make the breaks responsive by mixing the <code>.w-100</code> with some <a href="/docs/4.3/utilities/display/">responsive display utilities</a>.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-5">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;div class="w-100"&gt;&lt;/div&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row>
                  <b-col>col</b-col>
                  <b-col>col</b-col>
                  <div class="w-100"></div>
                  <b-col>col</b-col>
                  <b-col>col</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Responsive classes</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Bootstrap’s grid includes five tiers of predefined classes for building complex responsive layouts. Customize the size of your columns on extra small, small, medium, large, or extra large devices however you see fit.</p>
            <h4 class="card-title">All breakpoints</h4>
            <p>For grids that are the same from the smallest of devices to the largest, use the <code>.col</code> and <code>.col-*</code> classes. Specify a numbered class when you need a particularly sized column; otherwise, feel free to stick to <code>.col</code>.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-6">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
      &lt;b-col&gt;col&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row&gt;
      &lt;b-col cols="8"&gt;cols="8"&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;cols="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row class="mb-3">
                  <b-col>col</b-col>
                  <b-col>col</b-col>
                  <b-col>col</b-col>
                  <b-col>col</b-col>
                </b-row>
                <b-row>
                  <b-col cols="8">cols="8"</b-col>
                  <b-col cols="4">cols="4"</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Stacked to horizontal</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-7 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Using a single set of <code>.col-sm-*</code> classes, you can create a basic grid system that starts out stacked and becomes horizontal at the small breakpoint (<code>sm</code>).</p>
            <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-7">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col sm="8"&gt;sm="8"&lt;/b-col&gt;
      &lt;b-col sm="4"&gt;sm="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row&gt;
      &lt;b-col sm&gt;sm&lt;/b-col&gt;
      &lt;b-col sm&gt;sm&lt;/b-col&gt;
      &lt;b-col sm&gt;sm&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row class="mb-3">
                  <b-col sm="8">sm="8"</b-col>
                  <b-col sm="4">sm="4"</b-col>
                </b-row>
                <b-row>
                  <b-col sm>sm</b-col>
                  <b-col sm>sm</b-col>
                  <b-col sm>sm</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Mix and match</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-8 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Don’t want your columns to simply stack in some grid tiers? Use a combination of different classes for each tier as needed. See the example below for a better idea of how it all works.</p>
            <b-collapse id="collapse-8" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-8">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;!-- Stack the columns on mobile by making one full-width and the other half-width --&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col cols="12" md="8"&gt;cols="12" md="8"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt;cols="6" md="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop --&gt;
    &lt;b-row class="mb-3"&gt;
      &lt;b-col cols="6" md="4"&gt;cols="6" md="4"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt;cols="6" md="4"&lt;/b-col&gt;
      &lt;b-col cols="6" md="4"&gt;cols="6" md="4"&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;!-- Columns are always 50% wide, on mobile and desktop --&gt;
    &lt;b-row&gt;
      &lt;b-col cols="6"&gt;cols="6"&lt;/b-col&gt;
      &lt;b-col cols="6"&gt;cols="6"&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <!-- Stack the columns on mobile by making one full-width and the other half-width -->
                <b-row class="mb-3">
                  <b-col cols="12" md="8">cols="12" md="8"</b-col>
                  <b-col cols="6" md="4">cols="6" md="4"</b-col>
                </b-row>
                <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
                <b-row class="mb-3">
                  <b-col cols="6" md="4">cols="6" md="4"</b-col>
                  <b-col cols="6" md="4">cols="6" md="4"</b-col>
                  <b-col cols="6" md="4">cols="6" md="4"</b-col>
                </b-row>
                <!-- Columns are always 50% wide, on mobile and desktop -->
                <b-row>
                  <b-col cols="6">cols="6"</b-col>
                  <b-col cols="6">cols="6"</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Gutters</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-9 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Gutters can be responsively adjusted by breakpoint-specific padding and negative margin utility classes. To change the gutters in a given row, pair a negative margin utility on the <code>.row</code> and matching padding utilities on the <code>.col</code>s. The <code>.container</code> or <code>.container-fluid</code> parent may need to be adjusted too to avoid unwanted overflow, using again matching padding utility.</p>
            <p>Here’s an example of customizing the Bootstrap grid at the large (<code>lg</code>) breakpoint and above. We’ve increased the <code>.col</code> padding with <code>.px-lg-5</code>, counteracted that with <code>.mx-lg-n5</code> on the parent <code>.row</code> and then adjusted the <code>.container</code> wrapper with <code>.px-lg-5</code>.</p>
            <b-collapse id="collapse-9" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-9">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid class="px-lg-5"&gt;
    &lt;b-row class="mx-lg-n5"&gt;
      &lt;b-col class="py-3 px-lg-5 border bg-light"&gt;Custom column padding&lt;/b-col&gt;
      &lt;b-col class="py-3 px-lg-5 border bg-light"&gt;Custom column padding&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid class="px-lg-5">
                <b-row class="mx-lg-n5">
                  <b-col class="py-3 px-lg-5 border bg-light">Custom column padding</b-col>
                  <b-col class="py-3 px-lg-5 border bg-light">Custom column padding</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alignment</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-10 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use flexbox alignment utilities to vertically and horizontally align columns. <strong>Internet Explorer 10-11 do not support vertical alignment of flex items when the flex container has a <code>min-height</code> as shown below.</strong> <a href="https://github.com/philipwalton/flexbugs#flexbug-3">See Flexbugs #3 for more details.</a></p>
            <h4 class="mb-3">Vertical alignment</h4>
            <b-collapse id="collapse-10" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-10">
                    <code>
&lt;div class="iq-example-row iq-example-row-flex-cols"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row align-v="start"&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-v="center"&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-v="end"&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col&gt;One of three columns&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
  &lt;b-container fluid&gt;
    &lt;b-row&gt;
      &lt;b-col align-self="start"&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col align-self="center"&gt;One of three columns&lt;/b-col&gt;
      &lt;b-col align-self="end"&gt;One of three columns&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row iq-example-row-flex-cols">
              <b-container fluid>
                <b-row align-v="start">
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                </b-row>
                <b-row align-v="center">
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                </b-row>
                <b-row align-v="end">
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                  <b-col>One of three columns</b-col>
                </b-row>
              </b-container>
              <b-container fluid>
                <b-row>
                  <b-col align-self="start">One of three columns</b-col>
                  <b-col align-self="center">One of three columns</b-col>
                  <b-col align-self="end">One of three columns</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Horizontal alignment</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-11 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
          <p>Create equal-width columns that span multiple rows by inserting a <code>.w-100</code> where you want the columns to break to a new line. Make the breaks responsive by mixing the <code>.w-100</code> with some <a href="/docs/4.3/utilities/display/">responsive display utilities</a>.</p>
            <b-collapse id="collapse-11" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="grid-11">
                    <code>
&lt;div class="iq-example-row"&gt;
  &lt;b-container fluid&gt;
    &lt;b-row align-h="start" class="mb-3"&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-h="center" class="mb-3"&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-h="end" class="mb-3"&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-h="around" class="mb-3"&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
    &lt;/b-row&gt;
    &lt;b-row align-h="between" class="mb-3"&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
      &lt;b-col cols="4"&gt;One of two columns&lt;/b-col&gt;
    &lt;/b-row&gt;
  &lt;/b-container&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="iq-example-row">
              <b-container fluid>
                <b-row align-h="start" class="mb-3">
                  <b-col cols="4">One of two columns</b-col>
                  <b-col cols="4">One of two columns</b-col>
                </b-row>
                <b-row align-h="center" class="mb-3">
                  <b-col cols="4">One of two columns</b-col>
                  <b-col cols="4">One of two columns</b-col>
                </b-row>
                <b-row align-h="end" class="mb-3">
                  <b-col cols="4">One of two columns</b-col>
                  <b-col cols="4">One of two columns</b-col>
                </b-row>
                <b-row align-h="around" class="mb-3">
                  <b-col cols="4">One of two columns</b-col>
                  <b-col cols="4">One of two columns</b-col>
                </b-row>
                <b-row align-h="between" class="mb-3">
                  <b-col cols="4">One of two columns</b-col>
                  <b-col cols="4">One of two columns</b-col>
                </b-row>
              </b-container>
            </div>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiGrid',
}
</script>
