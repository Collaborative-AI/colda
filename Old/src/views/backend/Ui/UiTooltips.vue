<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Tooltips</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Hover over the buttons below to see the four tooltips directions: top, right, bottom, and left. The data-placement attribute specifies the tooltip position.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="tooltips-1">
                    <code>
&lt;b-button v-b-tooltip.top="'Tooltip on top'" variant="secondary" class="mt-3 mr-1"&gt;Tooltip on top&lt;/b-button&gt;
&lt;b-button v-b-tooltip.right="'Tooltip on right'" variant="secondary" class="mt-3 mr-1"&gt;Tooltip on right&lt;/b-button&gt;
&lt;b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="secondary" class="mt-3 mr-1"&gt;Tooltip on bottom&lt;/b-button&gt;
&lt;b-button v-b-tooltip.left="'Tooltip on left'" variant="secondary" class="mt-3 mr-1"&gt;Tooltip on left&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-tooltip.top="'Tooltip on top'" variant="secondary" class="mt-3 mr-1">Tooltip on top</b-button>
            <b-button v-b-tooltip.right="'Tooltip on right'" variant="secondary" class="mt-3 mr-1">Tooltip on right</b-button>
            <b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="secondary" class="mt-3 mr-1">Tooltip on bottom</b-button>
            <b-button v-b-tooltip.left="'Tooltip on left'" variant="secondary" class="mt-3 mr-1">Tooltip on left</b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Disabled elements</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Elements with the <code>disabled</code> attribute aren’t interactive, meaning users cannot focus, hover, or click them to trigger a tooltip (or popover). As a workaround, you’ll want to trigger the tooltip from a wrapper <code>&lt;div&gt;</code> or <code>&lt;span&gt;</code>, ideally made keyboard-focusable using <code>tabindex="0"</code>, and override the <code>pointer-events</code> on the disabled element.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="disabled-1">
                    <code>
&lt;span class="d-inline-block" tabindex="0" v-b-tooltip.top title="Disabled tooltip"&gt;
  &lt;b-button variant="primary" style="pointer-events: none;" disabled&gt;Disabled button&lt;/b-button&gt;
&lt;/span&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <span class="d-inline-block" tabindex="0" v-b-tooltip.top title="Disabled tooltip">
              <b-button variant="primary" style="pointer-events: none;" disabled>Disabled button</b-button>
            </span>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Tooltips</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Hover over the buttons below to see the four tooltips directions: top, right, bottom, and left Using background colors</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="tooltips-2">
                    <code>
 &lt;b-button v-b-tooltip.top="'Tooltip on top'" variant="primary" class="mt-3 mr-1"&gt;Tooltip on top&lt;/b-button&gt;
&lt;b-button v-b-tooltip.right="'Tooltip on right'" variant="success" class="mt-3 mr-1"&gt;Tooltip on right&lt;/b-button&gt;
&lt;b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="danger" class="mt-3 mr-1"&gt;Tooltip on bottom&lt;/b-button&gt;
&lt;b-button v-b-tooltip.left="'Tooltip on left'" variant="info" class="mt-3 mr-1"&gt;Tooltip on left&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-tooltip.top="'Tooltip on top'" variant="primary" class="mt-3 mr-1">Tooltip on top</b-button>
            <b-button v-b-tooltip.right="'Tooltip on right'" variant="success" class="mt-3 mr-1">Tooltip on right</b-button>
            <b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="danger" class="mt-3 mr-1">Tooltip on bottom</b-button>
            <b-button v-b-tooltip.left="'Tooltip on left'" variant="info" class="mt-3 mr-1">Tooltip on left</b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Tooltips</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Hover over the buttons below to see the four tooltips directions: top, right, bottom, and left Using Light background colors</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="tooltips-2">
                    <code>
&lt;b-button v-b-tooltip.top="'Tooltip on top'" variant="none" class="iq-bg-primary mt-3"&gt;Tooltip on top&lt;/b-button&gt;
&lt;b-button v-b-tooltip.right="'Tooltip on right'" variant="none" class="iq-bg-success mt-3"&gt;Tooltip on right&lt;/b-button&gt;
&lt;b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="none" class="iq-bg-danger mt-3"&gt;Tooltip on bottom&lt;/b-button&gt;
&lt;b-button v-b-tooltip.left="'Tooltip on left'" variant="none" class="iq-bg-info mt-3"&gt;Tooltip on left&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-tooltip.top="'Tooltip on top'" variant="none" class="iq-bg-primary mt-3 mr-1">Tooltip on top</b-button>
            <b-button v-b-tooltip.right="'Tooltip on right'" variant="none" class="iq-bg-success mt-3  mr-1">Tooltip on right</b-button>
            <b-button v-b-tooltip.bottom="'Tooltip on bottom'" variant="none" class="iq-bg-danger mt-3  mr-1">Tooltip on bottom</b-button>
            <b-button v-b-tooltip.left="'Tooltip on left'" variant="none" class="iq-bg-info mt-3  mr-1">Tooltip on left</b-button>
          </template>
        </card>
      </b-col>
      <b-col lg="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Hover elements</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Hover over the buttons below to see the tooltip.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="tooltips-5">
                    <code>
&lt;b-button href="#" v-b-tooltip.hover="'Some tooltip text!'" variant="link" &gt;Hover over me&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button href="#" v-b-tooltip.hover="'Some tooltip text!'" variant="link" >Hover over me</b-button>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiTooltips',
}
</script>
