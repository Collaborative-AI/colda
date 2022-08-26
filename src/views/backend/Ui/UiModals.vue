<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Modal components</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Below is a <em>static</em> modal example (meaning its <code>position</code> and <code>display</code> have been overridden). Included are the modal header, modal body (required for <code>padding</code>), and modal footer (optional). We ask that you include modal headers with dismiss actions whenever possible, or provide another explicit dismiss action.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="modal-components-1">
                    <code>
&lt;b-button v-b-modal.modal-1 variant="primary"&gt;Launch demo modal&lt;/b-button&gt;
&lt;b-modal id="modal-1" title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  ...
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-1 variant="primary">Launch demo modal</b-button>
            <b-modal id="modal-1" title="Modal title" ok-title="Save Changes" cancel-title="Close">
              ...
            </b-modal>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Modal Scrolling</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>When modals become too long for the user’s viewport or device, they scroll independent of the page itself. Try the demo below to see what we mean.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="modal-scrolling">
                    <code>
&lt;b-button v-b-modal.modal-2 variant="primary"&gt;Launch demo modal&lt;/b-button&gt;
&lt;b-modal id="modal-2" scrollable title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-2 variant="primary">Launch demo modal</b-button>
            <b-modal id="modal-2" scrollable title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
            </b-modal>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Optional sizes</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Modals have three optional sizes, available via modifier classes to be placed on a .modal-dialog. These sizes kick in at certain breakpoints to avoid horizontal scrollbars on narrower viewports.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="modal-components-2">
                    <code>
&lt;b-button v-b-modal.modal-3 variant="primary"&gt;Extra large modal&lt;/b-button&gt;
&lt;b-button v-b-modal.modal-4 variant="primary"&gt;Large modal&lt;/b-button&gt;
&lt;b-button v-b-modal.modal-5 variant="primary"&gt;Small modal&lt;/b-button&gt;

&lt;b-modal id="modal-3" size="xl" title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Modal body text goes here.&lt;/p&gt;
&lt;/b-modal&gt;

&lt;b-modal id="modal-4" size="lg" title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Modal body text goes here.&lt;/p&gt;
&lt;/b-modal&gt;

&lt;b-modal id="modal-5" size="sm" title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Modal body text goes here.&lt;/p&gt;
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-3 variant="primary" class="mr-1">Extra large modal</b-button>
            <b-button v-b-modal.modal-4 variant="primary" class="mr-1">Large modal</b-button>
            <b-button v-b-modal.modal-5 variant="primary" class="mr-1">Small modal</b-button>
            <b-modal id="modal-3" size="xl" title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Modal body text goes here.</p>
            </b-modal>
            <b-modal id="modal-4" size="lg" title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Modal body text goes here.</p>
            </b-modal>
            <b-modal id="modal-5" size="sm" title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Modal body text goes here.</p>
            </b-modal>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Scrolling long content</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>When modals become too long for the user’s viewport or device, they scroll independent of the page itself. Try the demo below to see what we mean.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="scroll-long-components">
                    <code>
&lt;b-button v-b-modal.modal-6 variant="primary"&gt;Launch demo modal&lt;/b-button&gt;
&lt;b-modal id="modal-6" title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-6 variant="primary">Launch demo modal</b-button>
            <b-modal id="modal-6" title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
            </b-modal>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Vertically centered</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Add <code class="highlighter-rouge">.modal-dialog-centered</code> to <code class="highlighter-rouge">.modal-dialog</code> to vertically center the modal.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="vertical-center">
                    <code>
&lt;b-button v-b-modal.modal-7 variant="primary"&gt;Launch demo modal&lt;/b-button&gt;
&lt;b-button v-b-modal.modal-8 variant="primary"&gt;Vertically centered scrollable modal&lt;/b-button&gt;
&lt;b-modal id="modal-7" centered title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  ...
&lt;/b-modal&gt;
&lt;b-modal id="modal-8" centered title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
  &lt;p&gt;Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.&lt;/p&gt;
  &lt;p&gt;Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.&lt;/p&gt;
  &lt;p&gt;Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.&lt;/p&gt;
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-7 variant="primary" class="mr-1">Launch demo modal</b-button>
            <b-button v-b-modal.modal-8 variant="primary" class="mr-1">Vertically centered scrollable modal</b-button>
            <b-modal id="modal-7" centered title="Modal title" ok-title="Save Changes" cancel-title="Close">
              ...
            </b-modal>
            <b-modal id="modal-8" centered title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
              <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
              <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
            </b-modal>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Using the grid</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
             <p>Utilize the Bootstrap grid system within a modal by nesting <code>.container-fluid</code> within the <code>.modal-body</code>. Then, use the normal grid system classes as you would anywhere else.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="using-grid">
                    <code>
&lt;b-button v-b-modal.modal-9 variant="primary"&gt;Launch demo modal&lt;/b-button&gt;
&lt;b-modal id="modal-9" centered title="Modal title" ok-title="Save Changes" cancel-title="Close"&gt;
  &lt;div class="iq-example-row"&gt;
    &lt;b-container fluid&gt;
      &lt;b-row class="mb-3"&gt;
        &lt;b-col md="4"&gt;
          md="4"
        &lt;/b-col&gt;
        &lt;b-col md="4" class="ml-auto"&gt;
          md="4" .ml-auto
        &lt;/b-col&gt;
      &lt;/b-row&gt;
      &lt;b-row class="mb-3"&gt;
        &lt;b-col md="3" class="ml-auto"&gt;md="3" .ml-auto&lt;/b-col&gt;
        &lt;b-col md="2" class="ml-auto"&gt;md="2" .ml-auto&lt;/b-col&gt;
      &lt;/b-row&gt;
      &lt;b-row class="mb-3"&gt;
        &lt;b-col md="6" class="ml-auto"&gt;md="6" .ml-auto&lt;/b-col&gt;
      &lt;/b-row&gt;
      &lt;b-row&gt;
        &lt;b-col sm="9"&gt;
          Level 1: sm="9"
          &lt;b-row&gt;
            &lt;b-col cols="8" sm="6"&gt;Level 2: cols="8" sm="6"&lt;/b-col&gt;
            &lt;b-col cols="4" sm="6"&gt;Level 2: cols="4" sm="6"&lt;/b-col&gt;
          &lt;/b-row&gt;
        &lt;/b-col&gt;
      &lt;/b-row&gt;
    &lt;/b-container&gt;
  &lt;/div&gt;
&lt;/b-modal&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-button v-b-modal.modal-9 variant="primary">Launch demo modal</b-button>
            <b-modal id="modal-9" centered title="Modal title" ok-title="Save Changes" cancel-title="Close">
              <div class="iq-example-row">
                <b-container fluid>
                  <b-row class="mb-3">
                    <b-col md="4">
                      md="4"
                    </b-col>
                    <b-col md="4 ml-auto">
                      md="4" .ml-auto
                    </b-col>
                  </b-row>
                  <b-row class="mb-3">
                    <b-col md="3 ml-auto">md="3" .ml-auto</b-col>
                    <b-col md="2 ml-auto">md="2" .ml-auto</b-col>
                  </b-row>
                  <b-row class="mb-3">
                    <b-col md="6 ml-auto">md="6" .ml-auto</b-col>
                  </b-row>
                  <b-row>
                    <b-col sm="9">
                      Level 1: sm="9"
                      <b-row>
                        <b-col cols="8" sm="6">Level 2: cols="8" sm="6"</b-col>
                        <b-col cols="4" sm="6">Level 2: cols="4" sm="6"</b-col>
                      </b-row>
                    </b-col>
                  </b-row>
                </b-container>
              </div>
            </b-modal>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>

export default {
  name: 'UiModal',
}
</script>
