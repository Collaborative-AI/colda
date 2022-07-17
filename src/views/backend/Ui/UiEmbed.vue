<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Embeds Video</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Wrap any embed like an <code class="highlighter-rouge">&lt;iframe&gt;</code> in a parent element with <code class="highlighter-rouge">.embed-responsive</code> and an aspect ratio. The <code class="highlighter-rouge">.embed-responsive-item</code> isn’t strictly required, but we encourage it.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="embeds-video">
                    <code>
&lt;b-embed
  type="iframe"
  aspect="16by9"
  src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
  allowfullscreen
&gt;&lt;/b-embed&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-embed
              type="iframe"
              aspect="16by9"
              src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
              allowfullscreen
            ></b-embed>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Responsive Aspect ratios 4:3</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Progress components are built with two HTML elements, some CSS to set the width, and a few attributes.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="ratios-1">
                    <code>
&lt;b-embed
  type="iframe"
  aspect="4by3"
  src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
  allowfullscreen
&gt;&lt;/b-embed&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-embed
              type="iframe"
              aspect="4by3"
              src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
              allowfullscreen
            ></b-embed>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Responsive Aspect ratios 21:9</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Progress components are built with two HTML elements, some CSS to set the width, and a few attributes.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="ratios-2">
                    <code>
&lt;b-embed
  type="iframe"
  aspect="21by9"
  src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
  allowfullscreen
&gt;&lt;/b-embed&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-embed
              type="iframe"
              aspect="21by9"
              src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
              allowfullscreen
            ></b-embed>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Responsive Aspect ratios 1:1</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Progress components are built with two HTML elements, some CSS to set the width, and a few attributes.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="ratios-3">
                    <code>
&lt;b-embed
  type="iframe"
  aspect="1by1"
  src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
  allowfullscreen
&gt;&lt;/b-embed&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-embed
              type="iframe"
              aspect="1by1"
              src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0"
              allowfullscreen
            ></b-embed>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiEmbedVideo',
}
</script>
