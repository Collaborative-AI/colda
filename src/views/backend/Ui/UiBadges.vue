<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Badge</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Badges scale to match the size of the immediate parent element by using relative font sizing and <code>em</code> units.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="badges">
                    <code>
&lt;h1 class="mb-3"&gt;Example heading &lt;b-badge variant="primary"&gt;New&lt;/b-badge&gt;&lt;/h1&gt;
&lt;h2 class="mb-3"&gt;Example heading &lt;b-badge variant="secondary"&gt;New&lt;/b-badge&gt;&lt;/h2&gt;
&lt;h3 class="mb-3"&gt;Example heading &lt;b-button variant="success"&gt;
  Notifications &lt;b-badge variant="light" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;&lt;/h3&gt;
&lt;h4 class="mb-3"&gt;Example heading &lt;b-badge variant="danger"&gt;New&lt;/b-badge&gt;&lt;/h4&gt;
&lt;h5 class="mb-3"&gt;Example heading &lt;b-badge variant="warning"&gt;New&lt;/b-badge&gt;&lt;/h5&gt;
&lt;h6 class="mb-0"&gt;Example heading &lt;b-badge variant="info"&gt;New&lt;/b-badge&gt;&lt;/h6&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <h1 class="mt-2">Example heading <b-badge variant="primary">New</b-badge></h1>
            <h2 class="mt-2">Example heading <b-badge variant="secondary">New</b-badge></h2>
            <h3 class="mt-2">Example heading <b-button variant="success">
              Notifications <b-badge variant="light" class="ml-2">4</b-badge>
            </b-button></h3>
            <h4 class="mt-2">Example heading <b-badge variant="danger">New</b-badge></h4>
            <h5 class="mt-2">Example heading <b-badge variant="warning">New</b-badge></h5>
            <h6 class="mb-0">Example heading <b-badge variant="info">New</b-badge></h6>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Button Badges</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Badges can be used as part of buttons to provide a counter.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="button-badges">
                    <code>
&lt;b-button variant="primary" class="mb-1"&gt;
  Notifications &lt;b-badge variant="light" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="success" class="mb-1"&gt;
  Notifications&lt;b-badge variant="light" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="danger" class="mb-1"&gt;
  Notifications&lt;b-badge variant="light" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button variant="primary" class="mb-1 mr-1">
              Notifications <b-badge variant="light" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="success" class="mb-1 mr-1">
              Notifications<b-badge variant="light" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="danger" class="mb-1 mr-1">
              Notifications<b-badge variant="light" class="ml-2">4</b-badge>
            </b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Button Light background Badges</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Badges can be used as part of buttons to provide a counter.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="button-light-background-badges">
                    <code>
&lt;b-button variant="outline-primary" class="mb-1"&gt;
  Notifications &lt;b-badge variant="primary" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="outline-success" class="mb-1"&gt;
  Notifications&lt;b-badge variant="success" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="outline-danger" class="mb-1"&gt;
  Notifications&lt;b-badge variant="danger" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button variant="outline-primary" class="mb-1 mr-1">
              Notifications <b-badge variant="primary" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="outline-success" class="mb-1 mr-1">
              Notifications<b-badge variant="success" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="outline-danger" class="mb-1 mr-1">
              Notifications<b-badge variant="danger" class="ml-2">4</b-badge>
            </b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Button Border Badges</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Badges can be used as part of buttons to provide a counter.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="button-border-badges">
                    <code>
&lt;b-button variant="none" class="iq-bg-primary mb-1"&gt;
  Notifications &lt;b-badge variant="primary" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="none" class="iq-bg-success mb-1"&gt;
  Notifications&lt;b-badge variant="success" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
&lt;b-button variant="none" class="iq-bg-danger mb-1"&gt;
  Notifications&lt;b-badge variant="danger" class="ml-2"&gt;4&lt;/b-badge&gt;
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button variant="none" class="bg-primary-light mb-1 mr-1">
              Notifications <b-badge variant="primary" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="none" class="bg-success-light mb-1 mr-1">
              Notifications<b-badge variant="success" class="ml-2">4</b-badge>
            </b-button>
            <b-button variant="none" class="bg-danger-light mb-1 mr-1">
              Notifications<b-badge variant="danger" class="ml-2">4</b-badge>
            </b-button>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Contextual variations</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add any of the below mentioned modifier classes to change the appearance of a badge.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="contextual-variations">
                    <code>
&lt;b-badge variant="primary"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge variant="secondary"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge variant="success"&gt;Success&lt;/b-badge&gt;
&lt;b-badge variant="danger"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge variant="warning"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge variant="info"&gt;Info&lt;/b-badge&gt;
&lt;b-badge variant="light"&gt;Light&lt;/b-badge&gt;
&lt;b-badge variant="dark"&gt;Dark&lt;/b-badge&gt;

&lt;h5 class="card-title mt-4"&gt;Pill badges&lt;/h5&gt;
&lt;p&gt;Use the &lt;code&gt;.badge-pill&lt;/code&gt; modifier class to make badges more rounded (with a larger &lt;code&gt;border-radius&lt;/code&gt; and additional horizontal &lt;code&gt;padding&lt;/code&gt;). Useful if you miss the badges from v3.&lt;/p&gt;

&lt;b-badge pill variant="primary"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge pill variant="secondary"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge pill variant="success"&gt;Success&lt;/b-badge&gt;
&lt;b-badge pill variant="danger"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge pill variant="warning"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge pill variant="info"&gt;Info&lt;/b-badge&gt;
&lt;b-badge pill variant="light"&gt;Light&lt;/b-badge&gt;
&lt;b-badge pill variant="dark"&gt;Dark&lt;/b-badge&gt;

&lt;h5 class="card-title mt-4"&gt;Links&lt;/h5&gt;
&lt;p&gt;Using the contextual &lt;code&gt;.badge-*&lt;/code&gt; classes on an &lt;code&gt;&amp;lt;a&amp;gt;&lt;/code&gt; element quickly provide &lt;em&gt;actionable&lt;/em&gt; badges with hover and focus states.&lt;/p&gt;

&lt;b-badge href="#" variant="primary"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge href="#" variant="secondary"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge href="#" variant="success"&gt;Success&lt;/b-badge&gt;
&lt;b-badge href="#" variant="danger"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge href="#" variant="warning"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge href="#" variant="info"&gt;Info&lt;/b-badge&gt;
&lt;b-badge href="#" variant="light"&gt;Light&lt;/b-badge&gt;
&lt;b-badge href="#" variant="dark"&gt;Dark&lt;/b-badge&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-badge variant="primary" class="mr-1">Primary</b-badge>
            <b-badge variant="secondary" class="mr-1">Secondary</b-badge>
            <b-badge variant="success" class="mr-1">Success</b-badge>
            <b-badge variant="danger" class="mr-1">Danger</b-badge>
            <b-badge variant="warning" class="mr-1">Warning</b-badge>
            <b-badge variant="info" class="mr-1">Info</b-badge>
            <b-badge variant="light" class="mr-1">Light</b-badge>
            <b-badge variant="dark" class="mr-1">Dark</b-badge>
            <h5 class="card-title mt-4">Pill badges</h5>
            <p>Use the <code>.badge-pill</code> modifier class to make badges more rounded (with a larger <code>border-radius</code> and additional horizontal <code>padding</code>). Useful if you miss the badges from v3.</p>
            <b-badge pill variant="primary" class="mr-1">Primary</b-badge>
            <b-badge pill variant="secondary" class="mr-1">Secondary</b-badge>
            <b-badge pill variant="success" class="mr-1">Success</b-badge>
            <b-badge pill variant="danger" class="mr-1">Danger</b-badge>
            <b-badge pill variant="warning" class="mr-1">Warning</b-badge>
            <b-badge pill variant="info" class="mr-1">Info</b-badge>
            <b-badge pill variant="light" class="mr-1">Light</b-badge>
            <b-badge pill variant="dark" class="mr-1">Dark</b-badge>
            <h5 class="card-title mt-4">Links</h5>
            <p>Using the contextual <code>.badge-*</code> classes on an <code>&lt;a&gt;</code> element quickly provide <em>actionable</em> badges with hover and focus states.</p>
            <b-badge href="#" variant="primary" class="mr-1">Primary</b-badge>
            <b-badge href="#" variant="secondary" class="mr-1">Secondary</b-badge>
            <b-badge href="#" variant="success" class="mr-1">Success</b-badge>
            <b-badge href="#" variant="danger" class="mr-1">Danger</b-badge>
            <b-badge href="#" variant="warning" class="mr-1">Warning</b-badge>
            <b-badge href="#" variant="info" class="mr-1">Info</b-badge>
            <b-badge href="#" variant="light" class="mr-1">Light</b-badge>
            <b-badge href="#" variant="dark" class="mr-1">Dark</b-badge>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Contextual variations Border</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add any of the below mentioned modifier classes to change the appearance of a badge.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="contextual-variations-border">
                    <code>
&lt;b-badge class="border border-primary text-primary" variant="none"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge class="border border-secondary text-secondary" variant="none"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge class="border border-success text-success" variant="none"&gt;Success&lt;/b-badge&gt;
&lt;b-badge class="border border-danger text-danger" variant="none"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge class="border border-warning text-warning" variant="none"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge class="border border-info text-info" variant="none"&gt;Info&lt;/b-badge&gt;
&lt;b-badge class="border border-light text-light" variant="none"&gt;Light&lt;/b-badge&gt;
&lt;b-badge class="border border-dark text-dark" variant="none"&gt;Dark&lt;/b-badge&gt;

&lt;h5 class="card-title mt-4"&gt;Pill badges&lt;/h5&gt;
&lt;p&gt;Use the &lt;code&gt;.badge-pill&lt;/code&gt; modifier class to make badges more rounded (with a larger &lt;code&gt;border-radius&lt;/code&gt; and additional horizontal &lt;code&gt;padding&lt;/code&gt;). Useful if you miss the badges from v3.&lt;/p&gt;
&lt;b-badge class="border border-primary text-primary" pill variant="none"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge class="border border-secondary text-secondary" pill variant="none"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge class="border border-success text-success" pill variant="none"&gt;Success&lt;/b-badge&gt;
&lt;b-badge class="border border-danger text-danger" pill variant="none"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge class="border border-warning text-warning" pill variant="none"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge class="border border-info text-info" pill variant="none"&gt;Info&lt;/b-badge&gt;
&lt;b-badge class="border border-light text-light" pill variant="none"&gt;Light&lt;/b-badge&gt;
&lt;b-badge class="border border-dark text-dark" pill variant="none"&gt;Dark&lt;/b-badge&gt;

&lt;h5 class="card-title mt-4"&gt;Links&lt;/h5&gt;
&lt;p&gt;Using the contextual &lt;code&gt;.badge-*&lt;/code&gt; classes on an &lt;code&gt;&amp;lt;a&amp;gt;&lt;/code&gt; element quickly provide &lt;em&gt;actionable&lt;/em&gt; badges with hover and focus states.&lt;/p&gt;
&lt;b-badge href="#" class="border border-primary text-primary" variant="none"&gt;Primary&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-secondary text-secondary" variant="none"&gt;Secondary&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-success text-success" variant="none"&gt;Success&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-danger text-danger" variant="none"&gt;Danger&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-warning text-warning" variant="none"&gt;Warning&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-info text-info" variant="none"&gt;Info&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-light text-light" variant="none"&gt;Light&lt;/b-badge&gt;
&lt;b-badge href="#" class="border border-dark text-dark" variant="none"&gt;Dark&lt;/b-badge&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-badge class="border border-primary text-primary mr-1 " variant="none">Primary</b-badge>
            <b-badge class="border border-secondary text-secondary mr-1" variant="none">Secondary</b-badge>
            <b-badge class="border border-success text-success mr-1" variant="none">Success</b-badge>
            <b-badge class="border border-danger text-danger mr-1" variant="none">Danger</b-badge>
            <b-badge class="border border-warning text-warning mr-1" variant="none">Warning</b-badge>
            <b-badge class="border border-info text-info mr-1" variant="none">Info</b-badge>
            <b-badge class="border border-light text-light mr-1" variant="none">Light</b-badge>
            <b-badge class="border border-dark text-dark mr-1 mt-2" variant="none">Dark</b-badge>
            <h5 class="card-title mt-4">Pill badges</h5>
            <p>Use the <code>.badge-pill</code> modifier class to make badges more rounded (with a larger <code>border-radius</code> and additional horizontal <code>padding</code>). Useful if you miss the badges from v3.</p>
            <b-badge class="border border-primary text-primary mr-1" pill variant="none">Primary</b-badge>
            <b-badge class="border border-secondary text-secondary mr-1" pill variant="none">Secondary</b-badge>
            <b-badge class="border border-success text-success mr-1" pill variant="none">Success</b-badge>
            <b-badge class="border border-danger text-danger mr-1" pill variant="none">Danger</b-badge>
            <b-badge class="border border-warning text-warning mr-1" pill variant="none">Warning</b-badge>
            <b-badge class="border border-info text-info mr-1" pill variant="none">Info</b-badge>
            <b-badge class="border border-light text-light mr-1" pill variant="none">Light</b-badge>
            <b-badge class="border border-dark text-dark mr-1 mt-2" pill variant="none">Dark</b-badge>
            <h5 class="card-title mt-4">Links</h5>
            <p>Using the contextual <code>.badge-*</code> classes on an <code>&lt;a&gt;</code> element quickly provide <em>actionable</em> badges with hover and focus states.</p>
            <b-badge href="#" class="border border-primary text-primary mr-1" variant="none">Primary</b-badge>
            <b-badge href="#" class="border border-secondary text-secondary mr-1" variant="none">Secondary</b-badge>
            <b-badge href="#" class="border border-success text-success mr-1" variant="none">Success</b-badge>
            <b-badge href="#" class="border border-danger text-danger mr-1" variant="none">Danger</b-badge>
            <b-badge href="#" class="border border-warning text-warning mr-1" variant="none">Warning</b-badge>
            <b-badge href="#" class="border border-info text-info mr-1" variant="none">Info</b-badge>
            <b-badge href="#" class="border border-light text-light mr-1" variant="none">Light</b-badge>
            <b-badge href="#" class="border border-dark text-dark mr-1 mt-2" variant="none">Dark</b-badge>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiBadges',
}
</script>
