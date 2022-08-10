<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Pagination Examples</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>In addition, as pages likely have more than one such navigation section, it’s advisable to provide a descriptive <code>aria-label</code> for the <code>&lt;nav&gt;</code> to reflect its purpose. For example, if the pagination component is used to navigate between a set of search results, an appropriate label could be <code>aria-label="Search results pages"</code>.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="pagination-examples">
                    <code>
&lt;b-pagination value="1"
              prev-text="Previous"
              next-text="Next"
              first-text="First"
              last-text="Last"
              :total-rows="50"
&gt;&lt;/b-pagination&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-pagination value="1" prev-text="Previous" next-text="Next" first-text="First" last-text="Last" :total-rows="50" />
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Disabled and active states</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Pagination links are customizable for different circumstances. Use <code>disabled</code> for links that appear un-clickable and <code>.active</code> to indicate the current page.</p>
            <p>While the <code>disabled</code> prop uses <code>pointer-events: none</code> to <em>try</em> to disable the link functionality of <code>&lt;a&gt;</code>s, that CSS property is not yet standardized and doesn’t account for keyboard navigation. As such, you should always add <code>tabindex="-1"</code> on disabled links and use custom JavaScript to fully disable their functionality.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="disabled-active-1">
                    <code>
&lt;b-pagination value="1" disabled :total-rows="50" /&gt;
&lt;b-pagination value="2" :total-rows="50" /&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-pagination value="1" disabled :total-rows="50" />
            <p>You can optionally swap out active or disabled anchors for <code>&lt;span&gt;</code>, or omit the anchor in the case of the prev/next arrows, to remove click functionality and prevent keyboard focus while retaining intended styles.</p>
            <b-pagination value="2" :total-rows="50" />
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Pagination With Color</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>In addition, as pages likely have more than one such navigation section, it’s advisable to provide a descriptive <code>aria-label</code> for the <code>&lt;nav&gt;</code> to reflect its purpose. For example, if the pagination component is used to navigate between a set of search results, an appropriate label could be <code>aria-label="Search results pages"</code>.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="disabled-active-3">
                    <code>
&lt;b-pagination class="iq-page-primary" :value="2" :total-rows="50" /&gt;
&lt;b-pagination class="iq-page-success" :value="2" :total-rows="50" /&gt;
&lt;b-pagination class="iq-page-info" :value="2" :total-rows="50" /&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-pagination class="iq-page-primary" :value="2" :total-rows="50" />
            <b-pagination class="iq-page-success" :value="2" :total-rows="50" />
            <b-pagination class="iq-page-info" :value="2" :total-rows="50" />
          </template>
        </card>
      </b-col>
      <b-col>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Working with icons</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Looking to use an icon or symbol in place of text for some pagination links? Be sure to provide proper screen reader support with <code>aria</code> attributes.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="pagination-with-icon">
                    <code>
&lt;b-pagination value="1"
              :total-rows="50"
&gt;&lt;/b-pagination&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-pagination value="1" :total-rows="50" />
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Pagination Sizing</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Fancy larger or smaller pagination? Add prop <code>size="lg"</code> or <code>size="sm"</code> for additional sizes.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="pagination-with-icon-size">
                    <code>
&lt;b-pagination value="1" :total-rows="50" size="lg" /&gt;
&lt;b-pagination value="1" :total-rows="50" /&gt;
&lt;b-pagination value="1" :total-rows="50" size="sm" /&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-pagination value="1" :total-rows="50" size="lg" />
            <b-pagination value="1" :total-rows="50" />
            <b-pagination value="1" :total-rows="50" size="sm" />
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Alignment</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>By default the pagination component is left aligned. Change the alignment to <code>center</code>, <code>right</code> (<code>right</code> is an alias for <code>end</code>), or <code>fill</code> by setting the prop align to the appropriate value.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="pagination-align">
                    <code>
&lt;div&gt;
  &lt;h6&gt;Left alignment (default)&lt;/h6&gt;
  &lt;b-pagination :value="1" :total-rows="50" /&gt;
&lt;/div&gt;

&lt;div class="mt-3"&gt;
  &lt;h6 class="text-center"&gt;Center alignment&lt;/h6&gt;
  &lt;b-pagination :value="1" :total-rows="50" align="center" /&gt;
&lt;/div&gt;

&lt;div class="mt-3"&gt;
  &lt;h6 class="text-right"&gt;Right (end) alignment&lt;/h6&gt;
  &lt;b-pagination :value="1" :total-rows="50" align="right" /&gt;
&lt;/div&gt;

&lt;div class="mt-3"&gt;
  &lt;h6 class="text-center"&gt;Fill alignment&lt;/h6&gt;
  &lt;b-pagination :value="1" :total-rows="50" align="fill" /&gt;
&lt;/div&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <div>
              <h6>Left alignment (default)</h6>
              <b-pagination :value="1" :total-rows="50" />
            </div>

            <div class="mt-3">
              <h6 class="text-center">Center alignment</h6>
              <b-pagination :value="1" :total-rows="50" align="center" />
            </div>

            <div class="mt-3">
              <h6 class="text-right">Right (end) alignment</h6>
              <b-pagination :value="1" :total-rows="50" align="right" />
            </div>

            <div class="mt-3">
              <h6 class="text-center">Fill alignment</h6>
              <b-pagination :value="1" :total-rows="50" align="fill" />
            </div>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiPagination',
  mounted () {
    const pageination = document.getElementsByClassName('iq-page-primary')[0]
    Array.from(pageination.children).forEach((el) => {
      if (el.querySelector('button')) {
        el.querySelector('button').classList.add('bg-primary', 'text-white', 'border-primary')
      }
    })
    const pageinationSuccess = document.getElementsByClassName('iq-page-success')[0]
    Array.from(pageinationSuccess.children).forEach((el) => {
      if (el.querySelector('button')) {
        el.querySelector('button').classList.add('bg-success', 'text-white', 'border-success')
      }
    })
    const pageinationInfo = document.getElementsByClassName('iq-page-info')[0]
    Array.from(pageinationInfo.children).forEach((el) => {
      if (el.querySelector('button')) {
        el.querySelector('button').classList.add('bg-info', 'text-white', 'border-info')
      }
    })
  }
}
</script>
