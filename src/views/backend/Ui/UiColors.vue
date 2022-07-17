<template>
  <b-container fluid>
    <b-row>
      <b-col lg="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Similar to the contextual text color classes, easily set the background of an element to any contextual class. Anchor components will darken on hover, just like the text classes. Background utilities <strong>do not set <code>color</code></strong>, so in some cases you’ll want to use <code>.text-*</code> utilities.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-color1`">
                    <code>
  &lt;p class="bg-primary pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Primary&lt;/h6&gt;

  &lt;p class="bg-secondary pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Secondary&lt;/h6&gt;

  &lt;p class="bg-success pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Success&lt;/h6&gt;

  &lt;p class="bg-danger pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Danger&lt;/h6&gt;

  &lt;p class="bg-warning pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Warning&lt;/h6&gt;

  &lt;p class="bg-info pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Info&lt;/h6&gt;

  &lt;p class="bg-light pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Light&lt;/h6&gt;

  &lt;p class="bg-dark pt-5 pb-5 text-center rounded"&gt;&lt;/p&gt;
  &lt;h6&gt;Dark&lt;/h6&gt;
  </code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-row class="mt-4">
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-primary pt-5 pb-5 text-center rounded"></p>
                <h6>Primary</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-secondary pt-5 pb-5 text-center rounded"></p>
                <h6>Secondary</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-success pt-5 pb-5 text-center rounded"></p>
                <h6>Success</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-danger pt-5 pb-5 text-center rounded"></p>
                <h6>Danger</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-warning pt-5 pb-5 text-center rounded"></p>
                <h6>Warning</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-info pt-5 pb-5 text-center rounded"></p>
                <h6>Info</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center mt-4">
                <p class="bg-light pt-5 pb-5 text-center rounded"></p>
                <h6>Light</h6>
              </b-col>
              <b-col lg="2" md="6" class="text-center mt-4">
                <p class="bg-dark pt-5 pb-5 text-center rounded"></p>
                <h6>Dark</h6>
              </b-col>
            </b-row>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Similar to the contextual text color classes, easily set the background of an element to any contextual class. Anchor components will darken on hover, just like the text classes. Background utilities <strong>do not set <code>color</code></strong>, so in some cases you’ll want to use <code>.text-*</code> utilities.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-color2`">
                    <code>
&lt;p class="iq-bg-primary pt-5 pb-5 text-center rounded font-size-18"&gt;Primary&lt;/p&gt;

&lt;p class="iq-bg-secondary pt-5 pb-5 text-center rounded font-size-18"&gt;Secondary&lt;/p&gt;

&lt;p class="iq-bg-success pt-5 pb-5 text-center rounded font-size-18"&gt;Success&lt;/p&gt;

&lt;p class="iq-bg-danger pt-5 pb-5 text-center rounded font-size-18"&gt;Danger&lt;/p&gt;

&lt;p class="iq-bg-warning pt-5 pb-5 text-center rounded font-size-18"&gt;Warning&lt;/p&gt;

&lt;p class="iq-bg-info pt-5 pb-5 text-center rounded font-size-18"&gt;Info&lt;/p&gt;

&lt;p class="iq-bg-dark pt-5 pb-5 text-center rounded font-size-18"&gt;Dark&lt;/p&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-row class="mt-4">
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-primary-light pt-5 pb-5 text-center rounded font-size-18">Primary</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-secondary-light pt-5 pb-5 text-center rounded font-size-18">Secondary</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-success-light pt-5 pb-5 text-center rounded font-size-18">Success</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-danger-light pt-5 pb-5 text-center rounded font-size-18">Danger</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-warning-light pt-5 pb-5 text-center rounded font-size-18">Warning</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center">
                <p class="bg-info-light pt-5 pb-5 text-center rounded font-size-18">Info</p>
              </b-col>
              <b-col lg="2" md="6" class="text-center mt-4">
                <p class="bg-dark-light pt-5 pb-5 text-center rounded font-size-18">Dark</p>
              </b-col>
            </b-row>
          </template>
        </card>
      </b-col>
      <b-col lg="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Text Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Contextual text classes also work well on anchors with the provided hover and focus states. <strong>Note that the <code>.text-white</code> and <code>.text-muted</code> class has no additional link styling beyond underline.</strong></p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-text-color1`">
                    <code>
&lt;p class="text-primary"&gt;.text-primary&lt;/p&gt;
&lt;p class="text-secondary"&gt;.text-secondary&lt;/p&gt;
&lt;p class="text-success"&gt;.text-success&lt;/p&gt;
&lt;p class="text-danger"&gt;.text-danger&lt;/p&gt;
&lt;p class="text-warning"&gt;.text-warning&lt;/p&gt;
&lt;p class="text-info"&gt;.text-info&lt;/p&gt;
&lt;p class="text-light bg-dark"&gt;.text-light&lt;/p&gt;
&lt;p class="text-dark"&gt;.text-dark&lt;/p&gt;
&lt;p class="text-muted"&gt;.text-muted&lt;/p&gt;
&lt;p class="text-white bg-dark"&gt;.text-white&lt;/p&gt;
&lt;p class="text-black-50"&gt;.text-black-50&lt;/p&gt;
&lt;p class="text-white-50 bg-dark mb-0"&gt;.text-white-50&lt;/p&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <p class="text-primary">.text-primary</p>
            <p class="text-secondary">.text-secondary</p>
            <p class="text-success">.text-success</p>
            <p class="text-danger">.text-danger</p>
            <p class="text-warning">.text-warning</p>
            <p class="text-info">.text-info</p>
            <p class="text-light bg-dark">.text-light</p>
            <p class="text-dark">.text-dark</p>
            <p class="text-muted">.text-muted</p>
            <p class="text-white bg-dark">.text-white</p>
            <p class="text-black-50">.text-black-50</p>
            <p class="text-white-50 bg-dark mb-0">.text-white-50</p>
          </template>
        </card>
      </b-col>
      <b-col lg="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Text Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Contextual text classes also work well on anchors with the provided hover and focus states. <strong>Note that the <code>.text-white</code> and <code>.text-muted</code> class has no additional link styling beyond underline.</strong></p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-text-color2`">
                    <code>
&lt;p&gt;&lt;a href="#" class="text-primary"&gt;Primary link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-secondary"&gt;Secondary link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-success"&gt;Success link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-danger"&gt;Danger link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-warning"&gt;Warning link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-info"&gt;Info link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-light bg-dark"&gt;Light link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-dark"&gt;Dark link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="text-muted"&gt;Muted link&lt;/a&gt;&lt;/p&gt;
&lt;p class="mb-0"&gt;&lt;a href="#" class="text-white bg-dark"&gt;White link&lt;/a&gt;&lt;/p&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <p><a href="#" class="text-primary">Primary link</a></p>
            <p><a href="#" class="text-secondary">Secondary link</a></p>
            <p><a href="#" class="text-success">Success link</a></p>
            <p><a href="#" class="text-danger">Danger link</a></p>
            <p><a href="#" class="text-warning">Warning link</a></p>
            <p><a href="#" class="text-info">Info link</a></p>
            <p><a href="#" class="text-light bg-dark">Light link</a></p>
            <p><a href="#" class="text-dark">Dark link</a></p>
            <p><a href="#" class="text-muted">Muted link</a></p>
            <p class="mb-0"><a href="#" class="text-white bg-dark">White link</a></p>
          </template>
        </card>
      </b-col>
      <b-col lg="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Text Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Contextual text classes also work well on anchors with the provided hover and focus states. <strong>Note that the <code>.text-white</code> and <code>.text-muted</code> class has no additional link styling beyond underline.</strong></p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-text-color3`">
                    <code>
&lt;p class="iq-bg-primary pl-3 pr-3 pt-2 pb-2 rounded"&gt;Primary link&lt;/p&gt;
&lt;p class="iq-bg-secondary pl-3 pr-3 pt-2 pb-2 rounded"&gt;Secondary link&lt;/p&gt;
&lt;p class="iq-bg-success pl-3 pr-3 pt-2 pb-2 rounded"&gt;Success link&lt;/p&gt;
&lt;p class="iq-bg-danger pl-3 pr-3 pt-2 pb-2 rounded"&gt;Danger link&lt;/p&gt;
&lt;p class="iq-bg-warning pl-3 pr-3 pt-2 pb-2 rounded"&gt;Warning link&lt;/p&gt;
&lt;p class="iq-bg-info pl-3 pr-3 pt-2 pb-2 rounded"&gt;Info link&lt;/p&gt;
&lt;p class="iq-bg-dark pl-3 pr-3 pt-2 pb-2 rounded mb-0"&gt;Dark link&lt;/p&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <p class="bg-primary-light pl-3 pr-3 pt-2 pb-2 rounded">Primary link</p>
            <p class="bg-secondary-light pl-3 pr-3 pt-2 pb-2 rounded">Secondary link</p>
            <p class="bg-success-light pl-3 pr-3 pt-2 pb-2 rounded">Success link</p>
            <p class="bg-danger-light pl-3 pr-3 pt-2 pb-2 rounded">Danger link</p>
            <p class="bg-warning-light pl-3 pr-3 pt-2 pb-2 rounded">Warning link</p>
            <p class="bg-info-light pl-3 pr-3 pt-2 pb-2 rounded">bg-Info link</p>
            <p class="bg-dark-light pl-3 pr-3 pt-2 pb-2 rounded mb-0">Dark link</p>
          </template>
        </card>
      </b-col>
      <b-col lg="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ appName }} Text Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Contextual text classes also work well on anchors with the provided hover and focus states. <strong>Note that the <code>.text-white</code> and <code>.text-muted</code> class has no additional link styling beyond underline.</strong></p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" :id="`${appName}-text-color4`">
                    <code>
&lt;p&gt;&lt;a href="#" class="iq-bg-primary pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Primary link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="iq-bg-secondary pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Secondary link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="iq-bg-success pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Success link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="iq-bg-danger pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Danger link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="iq-bg-warning pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Warning link&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;&lt;a href="#" class="iq-bg-info pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Info link&lt;/a&gt;&lt;/p&gt;
&lt;p class="mb-0"&gt;&lt;a href="#" class="iq-bg-dark pl-3 pr-3 pt-2 pb-2 rounded d-inline-block"&gt;Dark link&lt;/a&gt;&lt;/p&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <p><a href="#" class="bg-primary-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Primary link</a></p>
            <p><a href="#" class="bg-secondary-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Secondary link</a></p>
            <p><a href="#" class="bg-success-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Success link</a></p>
            <p><a href="#" class="bg-danger-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Danger link</a></p>
            <p><a href="#" class="bg-warning-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Warning link</a></p>
            <p><a href="#" class="bg-info-light pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">bg-Info link</a></p>
            <p class="mb-0"><a href="#" class="bg-dark pl-3 pr-3 pt-2 pb-2 rounded d-inline-block">Dark link</a></p>
          </template>
        </card>
      </b-col>

    </b-row>
  </b-container>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'UiColor',
  data () {
    return {
    }
  },
  computed : {
        ...mapGetters({
            appName: 'appName'
        })
    }
}
</script>
