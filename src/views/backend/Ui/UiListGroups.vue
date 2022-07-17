<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">List group</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>The most basic list group is an unordered list with list items and the proper classes. Build upon it with the options that follow, or with your own CSS as needed.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="list-group">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Morbi leo risus&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Porta ac consectetur ac&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Vestibulum at eros&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item>Cras justo odio</b-list-group-item>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item>Morbi leo risus</b-list-group-item>
              <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
              <b-list-group-item>Vestibulum at eros</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Disabled items</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add <code>.disabled</code> to a <code>.list-group-item</code> to make it <em>appear</em> disabled. Note that some elements with <code>.disabled</code> will also require custom JavaScript to fully disable their click events (e.g., links).</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="disabled-items">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item disabled&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Morbi leo risus&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Porta ac consectetur ac&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Vestibulum at eros&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item disabled>Cras justo odio</b-list-group-item>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item>Morbi leo risus</b-list-group-item>
              <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
              <b-list-group-item>Vestibulum at eros</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Flush</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add <code class="highlighter-rouge">.list-group-flush</code> to remove some borders and rounded corners to render list group items edge-to-edge in a parent container (e.g., cards).</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="flush">
                    <code>
&lt;b-list-group flush&gt;
  &lt;b-list-group-item&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Morbi leo risus&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Porta ac consectetur ac&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Vestibulum at eros&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group flush>
              <b-list-group-item>Cras justo odio</b-list-group-item>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item>Morbi leo risus</b-list-group-item>
              <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
              <b-list-group-item>Vestibulum at eros</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Contextual classes</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use contextual classes to style list items with a stateful background and color.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="contextual-classes">
                    <code>
 &lt;b-list-group&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="primary"&gt;A simple primary list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="secondary"&gt;A simple secondary list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="success"&gt;A simple success list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="danger"&gt;A simple danger list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="warning"&gt;A simple warning list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="info"&gt;A simple info list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="light"&gt;A simple light list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item variant="dark"&gt;A simple dark list group item&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item variant="primary">A simple primary list group item</b-list-group-item>
              <b-list-group-item variant="secondary">A simple secondary list group item</b-list-group-item>
              <b-list-group-item variant="success">A simple success list group item</b-list-group-item>
              <b-list-group-item variant="danger">A simple danger list group item</b-list-group-item>
              <b-list-group-item variant="warning">A simple warning list group item</b-list-group-item>
              <b-list-group-item variant="info">A simple info list group item</b-list-group-item>
              <b-list-group-item variant="light">A simple light list group item</b-list-group-item>
              <b-list-group-item variant="dark">A simple dark list group item</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">With badges</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add badges to any list group item to show unread counts, activity, and more with the help of some <a href="/docs/4.3/utilities/flex/">utilities</a>.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="with-badges-1">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center"&gt;
    Cras justo odio
    &lt;b-badge variant="primary" pill&gt;14&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center"&gt;
    Dapibus ac facilisis in
    &lt;b-badge variant="success" pill&gt;2&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center"&gt;
    Morbi leo risus
    &lt;b-badge variant="danger" pill&gt;1&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item class="d-flex justify-content-between align-items-center">
                Cras justo odio
                <b-badge variant="primary" pill>14</b-badge>
              </b-list-group-item>
              <b-list-group-item class="d-flex justify-content-between align-items-center">
                Dapibus ac facilisis in
                <b-badge variant="success" pill>2</b-badge>
              </b-list-group-item>
              <b-list-group-item class="d-flex justify-content-between align-items-center">
                Morbi leo risus
                <b-badge variant="danger" pill>1</b-badge>
              </b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">With badges</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add badges to any list group item to show unread counts, activity, and more with the help of some <a href="/docs/4.3/utilities/flex/">utilities</a>.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="with-badges-2">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-primary"&gt;
    Cras justo odio
    &lt;b-badge variant="primary" pill&gt;14&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-success"&gt;
    Dapibus ac facilisis in
    &lt;b-badge variant="success" pill&gt;2&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-danger"&gt;
    Morbi leo risus
    &lt;b-badge variant="danger" pill&gt;1&lt;/b-badge&gt;
  &lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-primary">
                Cras justo odio
                <b-badge variant="primary" pill>14</b-badge>
              </b-list-group-item>
              <b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-success">
                Dapibus ac facilisis in
                <b-badge variant="success" pill>2</b-badge>
              </b-list-group-item>
              <b-list-group-item class="d-flex justify-content-between align-items-center iq-bg-danger">
                Morbi leo risus
                <b-badge variant="danger" pill>1</b-badge>
              </b-list-group-item>
            </b-list-group>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">List Active</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-7 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add <code>.active</code> to a <code>.list-group-item</code> to indicate the current active selection.</p>
            <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="list-active">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item active&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Morbi leo risus&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Porta ac consectetur ac&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Vestibulum at eros&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item active>Cras justo odio</b-list-group-item>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item>Morbi leo risus</b-list-group-item>
              <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
              <b-list-group-item>Vestibulum at eros</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Links and buttons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-8 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use <code>&lt;a&gt;</code>s or <code>&lt;button&gt;</code>s to create <em>actionable</em> list group items with hover, disabled, and active states by adding <code>.list-group-item-action</code>. We separate these pseudo-classes to ensure list groups made of non-interactive elements (like <code>&lt;li&gt;</code>s or <code>&lt;div&gt;</code>s) don’t provide a click or tap affordance.</p>
            <p>Be sure to <strong>not use the standard <code>.btn</code> classes here</strong>.</p>
            <b-collapse id="collapse-8" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="links-buttons">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item href="#" active&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#"&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#"&gt;Morbi leo risus&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#"&gt;Porta ac consectetur ac&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#"&gt;Vestibulum at eros&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item href="#" active>Cras justo odio</b-list-group-item>
              <b-list-group-item href="#">Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item href="#">Morbi leo risus</b-list-group-item>
              <b-list-group-item href="#">Porta ac consectetur ac</b-list-group-item>
              <b-list-group-item href="#">Vestibulum at eros</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Horizontal</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-9 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add <code>.list-group-horizontal</code> to change the layout of list group items from vertical to horizontal across all breakpoints. Alternatively, choose a responsive variant <code>.list-group-horizontal-{sm|md|lg|xl}</code> to make a list group horizontal starting at that breakpoint’s <code>min-width</code>. Currently <strong>horizontal list groups cannot be combined with flush list groups.</strong></p>
            <p><strong>ProTip:</strong> Want equal-width list group items when horizontal? Add <code>.flex-fill</code> to each list group item.</p>
            <b-collapse id="collapse-9" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="horizontal">
                    <code>
&lt;b-list-group horizontal&gt;
  &lt;b-list-group-item&gt;Cras justo odio&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item&gt;Morbi leo risus&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group horizontal>
              <b-list-group-item>Cras justo odio</b-list-group-item>
              <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item>Morbi leo risus</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Contextual classes Action</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-10 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use contextual classes to style list items with a stateful background and color.</p>
            <b-collapse id="collapse-10" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="contextual-action">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item href="#"&gt;Dapibus ac facilisis in&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="primary"&gt;A simple primary list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="secondary"&gt;A simple secondary list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="success"&gt;A simple success list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="danger"&gt;A simple danger list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="warning"&gt;A simple warning list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="info"&gt;A simple info list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="light"&gt;A simple light list group item&lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" variant="dark"&gt;A simple dark list group item&lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item href="#">Dapibus ac facilisis in</b-list-group-item>
              <b-list-group-item href="#" variant="primary">A simple primary list group item</b-list-group-item>
              <b-list-group-item href="#" variant="secondary">A simple secondary list group item</b-list-group-item>
              <b-list-group-item href="#" variant="success">A simple success list group item</b-list-group-item>
              <b-list-group-item href="#" variant="danger">A simple danger list group item</b-list-group-item>
              <b-list-group-item href="#" variant="warning">A simple warning list group item</b-list-group-item>
              <b-list-group-item href="#" variant="info">A simple info list group item</b-list-group-item>
              <b-list-group-item href="#" variant="light">A simple light list group item</b-list-group-item>
              <b-list-group-item href="#" variant="dark">A simple dark list group item</b-list-group-item>
            </b-list-group>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Links and buttons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-12 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add nearly any HTML within, even for linked list groups like the one below, with the help of <a href="/docs/4.3/utilities/flex/">flexbox utilities</a>.</p>
            <b-collapse id="collapse-12" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="links-buttons">
                    <code>
&lt;b-list-group&gt;
  &lt;b-list-group-item href="#" active class="flex-column align-items-start"&gt;
    &lt;div class="d-flex w-100 justify-content-between"&gt;
      &lt;h5 class="mb-1 text-white"&gt;List group item heading&lt;/h5&gt;
      &lt;small&gt;3 days ago&lt;/small&gt;
    &lt;/div&gt;
    &lt;p class="mb-1"&gt;Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.&lt;/p&gt;
    &lt;small&gt;Donec id elit non mi porta.&lt;/small&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" class="flex-column align-items-start"&gt;
    &lt;div class="d-flex w-100 justify-content-between"&gt;
      &lt;h5 class="mb-1"&gt;List group item heading&lt;/h5&gt;
      &lt;small class="text-muted"&gt;3 days ago&lt;/small&gt;
    &lt;/div&gt;
    &lt;p class="mb-1"&gt;Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.&lt;/p&gt;
    &lt;small class="text-muted"&gt;Donec id elit non mi porta.&lt;/small&gt;
  &lt;/b-list-group-item&gt;
  &lt;b-list-group-item href="#" class="flex-column align-items-start"&gt;
    &lt;div class="d-flex w-100 justify-content-between"&gt;
      &lt;h5 class="mb-1"&gt;List group item heading&lt;/h5&gt;
      &lt;small class="text-muted"&gt;3 days ago&lt;/small&gt;
    &lt;/div&gt;
    &lt;p class="mb-1"&gt;Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.&lt;/p&gt;
    &lt;small class="text-muted"&gt;Donec id elit non mi porta.&lt;/small&gt;
  &lt;/b-list-group-item&gt;
&lt;/b-list-group&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-list-group>
              <b-list-group-item href="#" active class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1 text-white">List group item heading</h5>
                  <small>3 days ago</small>
                </div>
                <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                <small>Donec id elit non mi porta.</small>
              </b-list-group-item>
              <b-list-group-item href="#" class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small class="text-muted">3 days ago</small>
                </div>
                <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                <small class="text-muted">Donec id elit non mi porta.</small>
              </b-list-group-item>
              <b-list-group-item href="#" class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small class="text-muted">3 days ago</small>
                </div>
                <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                <small class="text-muted">Donec id elit non mi porta.</small>
              </b-list-group-item>
            </b-list-group>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>

export default {
  name: 'UiListGroup',
}
</script>
