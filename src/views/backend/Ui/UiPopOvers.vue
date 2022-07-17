<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Popovers</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-1">
                    <code>
&lt;b-button size="lg" variant="danger" id="popover-button-variant"&gt;Click to toggle popover&lt;/b-button&gt;
&lt;b-popover target="popover-button-variant" variant="danger"&gt;
  &lt;template v-slot:title&gt;Popover title&lt;/template&gt;
  And here's some amazing content. It's very engaging. Right?
&lt;/b-popover&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button size="lg" variant="danger" id="popover-button-variant">Click to toggle popover</b-button>
            <b-popover target="popover-button-variant" variant="danger">
              <template v-slot:title>Popover title</template>
              And here's some amazing content. It's very engaging. Right?
            </b-popover>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Dismiss on next click</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use the <code>focus</code> trigger to dismiss popovers on the user’s next click of a different element than the toggle element.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-2">
                    <code>
&lt;b-button href="#" variant="danger" id="popover-button-dismiss"&gt;Dismissible popover&lt;/b-button&gt;
&lt;b-popover target="popover-button-dismiss" variant="danger" triggers="focus"&gt;
  &lt;template v-slot:title&gt;Dismissible popover&lt;/template&gt;
  And here's some amazing content. It's very engaging. Right?
&lt;/b-popover&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button href="#" variant="danger" id="popover-button-dismiss">Dismissible popover</b-button>
            <b-popover target="popover-button-dismiss" variant="danger" triggers="focus">
              <template v-slot:title>Dismissible popover</template>
              And here's some amazing content. It's very engaging. Right?
            </b-popover>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Disabled elements</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Elements with the <code>disabled</code> attribute aren’t interactive, meaning users cannot hover or click them to trigger a popover (or tooltip). As a workaround, you’ll want to trigger the popover from a wrapper <code>&lt;div&gt;</code> or <code>&lt;span&gt;</code> and override the <code>pointer-events</code> on the disabled element.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-3">
                    <code>
&lt;span class="d-inline-block" tabindex="0" v-b-popover title="Disabled popover"&gt;
  &lt;b-button variant="primary" style="pointer-events: none;" disabled&gt;Disabled button&lt;/b-button&gt;
&lt;/span&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <span class="d-inline-block" tabindex="0" v-b-popover title="Disabled popover">
              <b-button variant="primary" style="pointer-events: none;" disabled>Disabled button</b-button>
            </span>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Hover elements</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
             <p>For disabled popover triggers, you may also prefer <code>data-trigger="hover"</code> so that the popover appears as immediate visual feedback to your users as they may not expect to <em>click</em> on a disabled element.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-4">
                    <code>
&lt;span class="d-inline-block" tabindex="0" v-b-popover.hover title="Disabled popover"&gt;
  &lt;b-button variant="primary" style="pointer-events: none;" disabled&gt;Disabled button&lt;/b-button&gt;
&lt;/span&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <span class="d-inline-block" tabindex="0" v-b-popover.hover title="Disabled popover">
              <b-button variant="primary" style="pointer-events: none;" disabled>Disabled button</b-button>
            </span>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Four directions</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Four options are available: top, right, bottom, and left aligned.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-5">
                    <code>
&lt;b-button v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on top
&lt;/b-button&gt;
&lt;b-button v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on right
&lt;/b-button&gt;
&lt;b-button v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on bottom
&lt;/b-button&gt;
&lt;b-button v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on left
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="">
              Popover on top
            </b-button>
            <b-button v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="ml-1">
              Popover on right
            </b-button>
            <b-button v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="ml-1">
              Popover on bottom
            </b-button>
            <b-button v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="mt-2">
              Popover on left
            </b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Popovers With Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Four options are available: top, right, bottom, and left aligned.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-6">
                    <code>
&lt;b-button variant="primary" v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on top
&lt;/b-button&gt;
&lt;b-button variant="success" v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on right
&lt;/b-button&gt;
&lt;b-button variant="danger" v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on bottom
&lt;/b-button&gt;
&lt;b-button variant="info" v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on left
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button variant="primary" v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'">
              Popover on top
            </b-button>
            <b-button variant="success" v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="ml-1">
              Popover on right
            </b-button>
            <b-button variant="danger" v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="ml-1">
              Popover on bottom
            </b-button>
            <b-button variant="info" v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" class="mt-2">
              Popover on left
            </b-button>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Popovers With Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-7 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Four options are available: top, right, bottom, and left aligned.</p>
            <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="popover-7">
                    <code>
&lt;b-button  variant="none" class="iq-bg-primary" v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on top
&lt;/b-button&gt;
&lt;b-button  variant="none" class="iq-bg-success" v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on right
&lt;/b-button&gt;
&lt;b-button  variant="none" class="iq-bg-danger" v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on bottom
&lt;/b-button&gt;
&lt;b-button  variant="none" class="iq-bg-info" v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"&gt;
  Popover on left
&lt;/b-button&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button  variant="none" class="iq-bg-primary" v-b-popover.click.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'" >
              Popover on top
            </b-button>
            <b-button  variant="none" class="iq-bg-success" v-b-popover.click.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'">
              Popover on right
            </b-button>
            <b-button  variant="none" class="iq-bg-danger" v-b-popover.click.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'">
              Popover on bottom
            </b-button>
            <b-button  variant="none" class="iq-bg-info" v-b-popover.click.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'">
              Popover on left
            </b-button>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiPopovers',
}
</script>
