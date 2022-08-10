<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Slides only</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Here’s a carousel with slides only. Note the presence of the <code>.d-block</code> and <code>.img-fluid</code> on carousel images to prevent browser default image alignment.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="slides-only">
                    <code>
&lt;b-carousel
  id="carouselExampleSlidesOnly"
&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
&lt;/b-carousel&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-carousel
              id="carouselExampleSlidesOnly"
            >
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Slides With Controls</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Here’s a carousel with slides only. Note the presence of the <code>.d-block</code> and <code>.img-fluid</code> on carousel images to prevent browser default image alignment.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="slides-controls">
                    <code>
&lt;b-carousel
  id="carouselExampleControls"
  controls
&gt;
  &lt;b-carousel-slide :img-src="require('../../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
&lt;/b-carousel&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-carousel
              id="carouselExampleControls"
              controls
            >
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Slides With Indicators</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Here’s a carousel with slides only. Note the presence of the <code>.d-block</code> and <code>.img-fluid</code> on carousel images to prevent browser default image alignment.</p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="slides-indicators">
                    <code>
&lt;b-carousel
  id="carouselExampleIndicators"
  controls
  indicators
&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
&lt;/b-carousel&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-carousel
              id="carouselExampleIndicators"
              controls
              indicators
            >
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Slides With Captions</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Here’s a carousel with slides only. Note the presence of the <code>.d-block</code> and <code>.img-fluid</code> on carousel images to prevent browser default image alignment.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="slides-captions">
                    <code>
&lt;b-carousel
  id="carouselExampleCaptions"
  controls
  indicators
&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
&lt;/b-carousel&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-carousel
              id="carouselExampleCaptions"
              controls
              indicators
            >
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')">
                <h4 class="text-white">First slide label</h4>
                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
              </b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')">
                <h4 class="text-white">Second slide label</h4>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')">
                <h4 class="text-white">Third slide label</h4>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
              </b-carousel-slide>
            </b-carousel>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Slides With Crossfade</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Here’s a carousel with slides only. Note the presence of the <code>.d-block</code> and <code>.img-fluid</code> on carousel images to prevent browser default image alignment.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="slides-fade">
                    <code>
&lt;b-carousel
  id="carouselExampleFade"
  fade
  controls
&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
  &lt;b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"&gt;&lt;/b-carousel-slide&gt;
&lt;/b-carousel&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-carousel
              id="carouselExampleFade"
              fade
              controls
            >
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('../../../assets/images/small/img-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiCarousel',
}
</script>
