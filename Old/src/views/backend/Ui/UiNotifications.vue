<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Notifications</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Toasts are as flexible as you need and have very little required markup. At a minimum, we require a single element to contain your “toasted” content and strongly encourage a dismiss button.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-1">
                    <code>
&lt;b-toast visible static no-auto-hide no-close-button&gt;
  &lt;template v-slot:toast-title&gt;
    &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
      &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
    &lt;/svg&gt;
    &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
    &lt;small&gt;11 mins ago&lt;/small&gt;
    &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
      &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
    &lt;/button&gt;
  &lt;/template&gt;
  Hello, world! This is a toast message.
&lt;/b-toast&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-toast visible static no-auto-hide no-close-button>
              <template v-slot:toast-title>
                <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                  <rect width="100%" height="100%" fill="#007aff"></rect>
                </svg>
                <strong class="mr-auto">Bootstrap</strong>
                <small>11 mins ago</small>
                <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
              </template>
              Hello, world! This is a toast message.
            </b-toast>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Stacking</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>When you have multiple toasts, we default to vertically stacking them in a readable manner.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-2">
                    <code>
&lt;b-toast visible static no-auto-hide no-close-button&gt;
  &lt;template v-slot:toast-title&gt;
    &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
      &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
    &lt;/svg&gt;
    &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
    &lt;small class="text-muted"&gt;just now&lt;/small&gt;
    &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
      &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
    &lt;/button&gt;
  &lt;/template&gt;
  See? Just like this.
&lt;/b-toast&gt;
&lt;b-toast visible static no-auto-hide no-close-button&gt;
  &lt;template v-slot:toast-title&gt;
    &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
      &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
    &lt;/svg&gt;
    &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
    &lt;small class="text-muted"&gt;2 seconds ago&lt;/small&gt;
    &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
      &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
    &lt;/button&gt;
  &lt;/template&gt;
  Heads up, toasts will stack automatically
&lt;/b-toast&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-toast visible static no-auto-hide no-close-button>
              <template v-slot:toast-title>
                <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                  <rect width="100%" height="100%" fill="#007aff"></rect>
                </svg>
                <strong class="mr-auto">Bootstrap</strong>
                <small class="text-muted">just now</small>
                <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
              </template>
              See? Just like this.
            </b-toast>
            <b-toast visible static no-auto-hide no-close-button>
              <template v-slot:toast-title>
                <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                  <rect width="100%" height="100%" fill="#007aff"></rect>
                </svg>
                <strong class="mr-auto">Bootstrap</strong>
                <small class="text-muted">2 seconds ago</small>
                <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
              </template>
              Heads up, toasts will stack automatically
            </b-toast>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Notifications horizontally and/or vertically</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>You can also get fancy with flexbox utilities to align toasts horizontally and/or vertically.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-3">
                    <code>
&lt;div class="p-3 bg-dark"&gt;
  &lt;div aria-live="polite" aria-atomic="true" class="d-flex justify-content-center align-items-center" style="min-height: 200px;"&gt;
    &lt;b-toast visible static no-auto-hide no-close-button&gt;
      &lt;template v-slot:toast-title&gt;
        &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
          &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
        &lt;/svg&gt;
        &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
        &lt;small&gt;11 mins ago&lt;/small&gt;
        &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
          &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
        &lt;/button&gt;
      &lt;/template&gt;
      Hello, world! This is a toast message.
    &lt;/b-toast&gt;
  &lt;/div&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="p-3 bg-dark">
              <div aria-live="polite" aria-atomic="true" class="d-flex justify-content-center align-items-center" style="min-height: 200px;">
                <b-toast visible static no-auto-hide no-close-button>
                  <template v-slot:toast-title>
                    <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect width="100%" height="100%" fill="#007aff"></rect>
                    </svg>
                    <strong class="mr-auto">Bootstrap</strong>
                    <small>11 mins ago</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">×</span>
                    </button>
                  </template>
                  Hello, world! This is a toast message.
                </b-toast>
              </div>
            </div>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Notifications</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Toasts are as flexible as you need and have very little required markup. At a minimum, we require a single element to contain your “toasted” content and strongly encourage a dismiss button.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-4">
                    <code>
&lt;div class="p-3 bg-dark"&gt;
  &lt;b-toast visible static no-auto-hide no-close-button&gt;
    &lt;template v-slot:toast-title&gt;
      &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
        &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
      &lt;/svg&gt;
      &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
      &lt;small&gt;11 mins ago&lt;/small&gt;
      &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
        &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
      &lt;/button&gt;
    &lt;/template&gt;
    Hello, world! This is a toast message.
  &lt;/b-toast&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
              <div class="p-3 bg-dark">
                <b-toast visible static no-auto-hide no-close-button>
                  <template v-slot:toast-title>
                    <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect width="100%" height="100%" fill="#007aff"></rect>
                    </svg>
                    <strong class="mr-auto">Bootstrap</strong>
                    <small>11 mins ago</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">×</span>
                    </button>
                  </template>
                  Hello, world! This is a toast message.
                </b-toast>
              </div>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Stacking Placement</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Place toasts with custom CSS as you need them. The top right is often used for notifications, as is the top middle. If you’re only ever going to show one toast at a time, put the positioning styles right on the <code>.toast</code>.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-5">
                    <code>
&lt;div class="p-3 bg-dark"&gt;
  &lt;div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;"&gt;
    &lt;b-toast visible static no-auto-hide no-close-button toast-class="position-absolute"&gt;
      &lt;template v-slot:toast-title&gt;
        &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
          &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
        &lt;/svg&gt;
        &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
        &lt;small&gt;11 mins ago&lt;/small&gt;
        &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
          &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
        &lt;/button&gt;
      &lt;/template&gt;
      Hello, world! This is a toast message.
    &lt;/b-toast&gt;
  &lt;/div&gt;
&lt;/div&gt;
&lt;p class="mt-3"&gt;For systems that generate more notifications, consider using a wrapping element so they can easily stack.&lt;/p&gt;
&lt;div class="bg-dark p-3 mt-3"&gt;
  &lt;div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;"&gt;
    &lt;div style="position: absolute; top: 0; right: 0;"&gt;
    &lt;b-toast visible static no-auto-hide no-close-button&gt;
      &lt;template v-slot:toast-title&gt;
        &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
          &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
        &lt;/svg&gt;
        &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
        &lt;small class="text-muted"&gt;just now&lt;/small&gt;
        &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
          &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
        &lt;/button&gt;
      &lt;/template&gt;
      See? Just like this.
    &lt;/b-toast&gt;
    &lt;b-toast visible static no-auto-hide no-close-button&gt;
      &lt;template v-slot:toast-title&gt;
        &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
          &lt;rect width="100%" height="100%" fill="#007aff"&gt;&lt;/rect&gt;
        &lt;/svg&gt;
        &lt;strong class="mr-auto"&gt;Bootstrap&lt;/strong&gt;
        &lt;small class="text-muted"&gt;2 seconds ago&lt;/small&gt;
        &lt;button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"&gt;
          &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
        &lt;/button&gt;
      &lt;/template&gt;
      Heads up, toasts will stack automatically
    &lt;/b-toast&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="p-3 bg-dark">
              <div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;">
                <b-toast visible static no-auto-hide no-close-button toast-class="position-absolute">
                  <template v-slot:toast-title>
                    <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect width="100%" height="100%" fill="#007aff"></rect>
                    </svg>
                    <strong class="mr-auto">Bootstrap</strong>
                    <small>11 mins ago</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">×</span>
                    </button>
                  </template>
                  Hello, world! This is a toast message.
                </b-toast>
              </div>
            </div>
            <p class="mt-3">For systems that generate more notifications, consider using a wrapping element so they can easily stack.</p>
            <div class="bg-dark p-3 mt-3">
              <div aria-live="polite" aria-atomic="true" style="position: relative; min-height: 200px;">
                <div style="position: absolute; top: 0; right: 0;">
                <b-toast visible static no-auto-hide no-close-button>
                  <template v-slot:toast-title>
                    <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect width="100%" height="100%" fill="#007aff"></rect>
                    </svg>
                    <strong class="mr-auto">Bootstrap</strong>
                    <small class="text-muted">just now</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">×</span>
                    </button>
                  </template>
                  See? Just like this.
                </b-toast>
                <b-toast visible static no-auto-hide no-close-button>
                  <template v-slot:toast-title>
                    <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                      <rect width="100%" height="100%" fill="#007aff"></rect>
                    </svg>
                    <strong class="mr-auto">Bootstrap</strong>
                    <small class="text-muted">2 seconds ago</small>
                    <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                      <span aria-hidden="true">×</span>
                    </button>
                  </template>
                  Heads up, toasts will stack automatically
                </b-toast>
                </div>
              </div>
            </div>
          </template>
        </card>
      </b-col>
      <b-col sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Notifications</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Toasts are as flexible as you need and have very little required markup. At a minimum, we require a single element to contain your “toasted” content and strongly encourage a dismiss button.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="notification-6">
                    <code>
&lt;b-toast visible static no-auto-hide no-close-button toast-class="bg-primary" body-class="text-white"  header-class="bg-primary text-white"&gt;
  &lt;template v-slot:toast-title&gt;
    &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
      &lt;rect width="100%" height="100%" fill="#fff"&gt;&lt;/rect&gt;
    &lt;/svg&gt;
    &lt;strong class="mr-auto text-white"&gt;Bootstrap&lt;/strong&gt;
    &lt;small class="text-white"&gt;11 mins ago&lt;/small&gt;
    &lt;button type="button" class="ml-2 mb-1 close text-white" data-dismiss="toast" aria-label="Close"&gt;
      &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
    &lt;/button&gt;
  &lt;/template&gt;
  See? Just like this.
&lt;/b-toast&gt;
&lt;b-toast variant="success" visible static no-auto-hide no-close-button toast-class="bg-success mt-3" body-class="text-white"  header-class="bg-success text-white"&gt;
  &lt;template v-slot:toast-title&gt;
    &lt;svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img"&gt;
      &lt;rect width="100%" height="100%" fill="#fff"&gt;&lt;/rect&gt;
    &lt;/svg&gt;
    &lt;strong class="mr-auto text-white"&gt;Bootstrap&lt;/strong&gt;
    &lt;small class="text-white"&gt;11 mins ago&lt;/small&gt;
    &lt;button type="button" class="ml-2 mb-1 close text-white" data-dismiss="toast" aria-label="Close"&gt;
      &lt;span aria-hidden="true"&gt;×&lt;/span&gt;
    &lt;/button&gt;
  &lt;/template&gt;
  Heads up, toasts will stack automatically
&lt;/b-toast&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="toast fade show bg-primary text-white border-0 rounded p-2 mt-3 d-flex">
            <b-toast visible static no-auto-hide no-close-button toast-class="toast fade show" body-class="text-white"  header-class="bg-primary text-white" >
              <template v-slot:toast-title>
                <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                  <rect width="100%" height="100%" fill="#fff"></rect>
                </svg>
                <strong class="mr-auto text-white">Bootstrap</strong>
                <small class="text-white">11 mins ago</small>
                <button type="button" class="ml-10 mb-1 close text-white" data-dismiss="toast" aria-label="Close">
                  
                </button>
              </template>
              Hello, world! This is a toast message.
            </b-toast>
            <span class="close text-white" style="margin-left:70%;" aria-hidden="true">×</span>
            </div>
            <div class="bg-success text-white border-0 rounded p-2 mt-3 d-flex ">
            <b-toast variant="success" visible static no-auto-hide no-close-button toast-class="toast fade show " body-class="text-white"  header-class="bg-success text-white">
              <template v-slot:toast-title>
                <svg class="bd-placeholder-img rounded mr-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img">
                  <rect width="100%" height="100%" fill="#fff"></rect>
                </svg>
                <strong class="mr-auto text-white">Bootstrap</strong>
                <small class="text-white">11 mins ago</small>
                <button type="button" class="ml-2 mb-1 close text-white" data-dismiss="toast" aria-label="Close">
                 
                </button>
              </template>
              Hello, world! This is a toast message.
            </b-toast>
             <span class="close text-white" style="margin-left:70%;" aria-hidden="true">×</span>
            </div>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiNotifications',
  methods: {
    makeToast (append = false) {
      this.$bvToast.toast('This is toast numbe', {
        title: 'BootstrapVue Toast',
        autoHideDelay: 5000,
        appendToast: append
      })
    }
  }
}
</script>
<style>
.b-toast .toast {
  opacity: 1 !important;
  background-color: unset;
}
</style>
