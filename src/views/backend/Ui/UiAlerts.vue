<template>
  <b-container fluid>
    <b-row>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
              <h4 class="card-title">Basic Alerts</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1  role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="basic-alert"><code>
&lt;b-alert :show="true" variant="primary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary">
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="secondary">
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="success">
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="danger">
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="warning">
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="info">
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="light">
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Basic Alerts With Icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                   <pre class="text-white" id="basic-alert-icon"><code>
&lt;b-alert :show="true" variant="primary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="secondary">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="success">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="danger">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="warning">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="info">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="light">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Basic Line Alerts</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="basic-line-alert"><code>
&lt;b-alert :show="true" variant="primary" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light" class="bg-white"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary" class="bg-white">
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="secondary" class="bg-white">
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="success" class="bg-white">
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="danger" class="bg-white">
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="warning" class="bg-white">
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="info" class="bg-white">
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="light" class="bg-white">
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Basic Line Alerts With Icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="basic-line-alert-icon"><code>
&lt;b-alert :show="true" variant="primary" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light" class="bg-white"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="secondary" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="success" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="danger" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="warning" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="info" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant="light" class="bg-white">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alerts With Background</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                   <pre class="text-white" id="alert-with-background"><code>
&lt;b-alert :show="true" variant=" " class="text-white bg-primary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-secondary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-success"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-danger"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-warning"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" "  class="text-white bg-info"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="bg-light"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant=" " class="text-white bg-primary">
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-secondary">
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-success">
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-danger">
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-warning">
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" "  class="text-white bg-info">
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="bg-light">
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Background Alerts With Icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="alert-with-background-icon"><code>
&lt;b-alert :show="true" variant=" " class="text-white bg-primary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-secondary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-success"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-danger"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-warning"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="text-white bg-info"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " class="bg-light"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant=" " class="text-white bg-primary">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-secondary">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-success">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-danger">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-warning">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="text-white bg-info">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " class="bg-light">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alerts Dismissing</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-7  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="alert-with-dismiss"><code>
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-primary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-secondary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-success"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-danger"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-warning"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade  class="text-white bg-info"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="bg-light"&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-primary">
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-secondary">
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-success">
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-danger">
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-warning">
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade  class="text-white bg-info">
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="bg-light">
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alerts Dismissing With Icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-8  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-8" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="alert-with-dismiss-icon"><code>
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-primary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;primary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-secondary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;secondary&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-success"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;success&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-danger"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;danger&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-warning"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;warning&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="text-white bg-info"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;info&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant=" " dismissible fade class="bg-light"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple &lt;b&gt;light&lt;/b&gt; alert—check it out!&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-primary">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>primary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-secondary">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>secondary</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-success">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>success</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-danger">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>danger</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-warning">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>warning</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="text-white bg-info">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>info</b> alert—check it out!</div>
            </b-alert>
            <b-alert :show="true" variant=" " dismissible fade class="bg-light">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple <b>light</b> alert—check it out!</div>
            </b-alert>
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alerts With Background</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-9  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-9" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="alert-with-link"><code>
&lt;b-alert :show="true" variant="primary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light"&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="secondary">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="success">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="danger">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="warning">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="info">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="light">
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="6">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Background Alerts With Icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-10  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-10" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="alert-with-link-icon"><code>
&lt;b-alert :show="true" variant="primary" class="text-white bg-primary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white "&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="secondary" class="text-white bg-secondary"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="success" class="text-white bg-success"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="danger" class="text-white bg-danger"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="warning" class="text-white bg-warning"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="info" class="text-white bg-info"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-information-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
&lt;b-alert :show="true" variant="light" class="bg-light"&gt;
  &lt;div class="iq-alert-icon"&gt;
    &lt;i class="ri-alert-line"&gt;&lt;/i&gt;
  &lt;/div&gt;
  &lt;div class="iq-alert-text"&gt;A simple light alert with &lt;a href="#" class="alert-link text-white"&gt;an example link&lt;/a&gt;. Give it a click if you like.&lt;/div&gt;
&lt;/b-alert&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-alert :show="true" variant="primary" class="text-white bg-primary">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white ">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="secondary" class="text-white bg-secondary">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="success" class="text-white bg-success">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="danger" class="text-white bg-danger">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="warning" class="text-white bg-warning">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="info" class="text-white bg-info">
              <div class="iq-alert-icon">
                <i class="ri-information-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
            <b-alert :show="true" variant="light" class="bg-light">
              <div class="iq-alert-icon">
                <i class="ri-alert-line"></i>
              </div>
              <div class="iq-alert-text">A simple light alert with <a href="#" class="alert-link text-white">an example link</a>. Give it a click if you like.</div>
            </b-alert>
          </template>
        </card>
      </b-col>
      <b-col md="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Additional content</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-11  role="button">
              <i class="ri-code-s-slash-line"></i>
            </a>
          </template>
          <template v-slot:body>
            <p class="mb-4">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever</p>
            <b-collapse id="collapse-11" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                 <pre class="text-white" id="alert-with-link-additional"><code>
&lt;div class="col-sm-6"&gt;
  &lt;b-alert :show="true" variant="primary"&gt;
    &lt;div class="iq-alert-text"&gt;
      &lt;h5 class="alert-heading"&gt;Well done!&lt;/h5&gt;
      &lt;p&gt;Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.&lt;/p&gt;
      &lt;hr&gt;
      &lt;p class="mb-0"&gt;Whenever you need to, be sure to use margin utilities to keep things nice and tidy.&lt;/p&gt;
    &lt;/div&gt;
  &lt;/b-alert&gt;
&lt;/div&gt;
&lt;div class="col-sm-6"&gt;
  &lt;b-alert :show="true" variant="success"&gt;
    &lt;div class="iq-alert-text"&gt;
      &lt;h5 class="alert-heading"&gt;Well done!&lt;/h5&gt;
      &lt;p&gt;Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.&lt;/p&gt;
      &lt;hr&gt;
      &lt;p class="mb-0"&gt;Whenever you need to, be sure to use margin utilities to keep things nice and tidy.&lt;/p&gt;
    &lt;/div&gt;
  &lt;/b-alert&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div class="row">
              <div class="col-sm-6">
                <b-alert :show="true" variant="primary">
                  <div class="iq-alert-text">
                    <h5 class="alert-heading">Well done!</h5>
                    <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                    <hr>
                    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
                  </div>
                </b-alert>
              </div>
              <div class="col-sm-6">
                <b-alert :show="true" variant="success">
                  <div class="iq-alert-text">
                    <h5 class="alert-heading">Well done!</h5>
                    <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                    <hr>
                    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
                  </div>
                </b-alert>
              </div>
            </div>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiAlerts',
}
</script>
