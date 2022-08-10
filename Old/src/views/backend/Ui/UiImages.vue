<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Responsive images</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Images in Bootstrap are made responsive with <code>.img-fluid</code>. <code>max-width: 100%;</code> and <code>height: auto;</code> are applied to the image so that it scales with the parent element.</p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-1">
                    <code>
&lt;b-img :src="require('../../../assets/images/small/img-1.jpg')" fluid alt="Responsive image"&gt;&lt;/b-img&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-img :src="require('../../../assets/images/small/img-1.jpg')" fluid alt="Responsive image"></b-img>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Equal-width multi-row</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Create equal-width columns that span multiple rows by inserting a <code>.w-100</code> where you want the columns to break to a new line. Make the breaks responsive by mixing the <code>.w-100</code> with some <a href="/docs/4.3/utilities/display/">responsive display utilities</a>.</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-2">
                    <code>
&lt;b-media&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/15.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0"&gt;Media heading&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
&lt;b-media&gt;
    &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/16.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0"&gt;Media heading&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
    &lt;b-media no-body class="mt-3"&gt;
      &lt;b-media-aside tag="a"&gt;
        &lt;b-img :src="require('../../../assets/images/page-img/17.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
      &lt;/b-media-aside&gt;
      &lt;b-media-body&gt;
        &lt;h5 class="mt-0"&gt;Media heading&lt;/h5&gt;
        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
      &lt;/b-media-body&gt;
    &lt;/b-media&gt;
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-media>
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/15.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0">Media heading</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
            <b-media>
               <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/16.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0">Media heading</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                <b-media no-body class="mt-3">
                  <b-media-aside tag="a">
                    <b-img :src="require('../../../assets/images/page-img/17.jpg')"  class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
                  </b-media-aside>
                  <b-media-body>
                    <h5 class="mt-0">Media heading</h5>
                    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                  </b-media-body>
                </b-media>
              </b-media-body>
            </b-media>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Order</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse- role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Change the order of content in media objects by modifying the HTML itself, or by adding some custom flexbox CSS to set the <code>order</code> property (to an integer of your choosing).</p>
            <b-collapse id="collapse-" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="images-3">
                    <code>
&lt;b-media right-align class="mb-5"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/18.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0 mb-1"&gt;Top-aligned media&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
&lt;b-media right-align vertical-align="center" class="mb-5"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/19.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0 mb-1"&gt;Center-aligned media&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
&lt;b-media right-align vertical-align="end"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/20.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0 mb-1"&gt;Bottom-aligned media&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-media right-align class="mb-5">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/18.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0 mb-1">Top-aligned media</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
            <b-media right-align vertical-align="center" class="mb-5">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/19.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0 mb-1">Center-aligned media</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
            <b-media right-align vertical-align="end">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/20.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0 mb-1">Bottom-aligned media</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Image thumbnails</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>In addition to our <a href="/docs/4.3/utilities/borders/">border-radius utilities</a>, you can use <code>.img-thumbnail</code> to give an image a rounded 1px border appearance.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-4">
                    <code>
&lt;b-img thumbnail class="ml-3" :src="require('../../../assets/images/page-img/10.jpg')" alt="Responsive image"&gt;&lt;/b-img&gt;
&lt;b-img rounded class="ml-3" :src="require('../../../assets/images/page-img/11.jpg')"  alt="Responsive image"&gt;&lt;/b-img&gt;
&lt;b-img rounded="circle" :src="require('../../../assets/images/page-img/12.jpg')" alt="Responsive image"&gt;&lt;/b-img&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <ul class="list-unstyled p-0 m-0 row">
                        <li class="col-lg-4 col-md-6 col-sm-6 mt-2"><img src="../../../assets/images/page-img/10.jpg" class="img-thumbnail w-100 img-fluid rounded" alt="Responsive image"></li>
                        <li class="col-lg-4 col-md-6 col-sm-6 mt-2"><img src="../../../assets/images/page-img/11.jpg" class="rounded w-100 img-fluid rounded" alt="Responsive image"></li>
                        <li class="col-lg-4 col-md-6 col-sm-6 mt-2"><img src="../../../assets/images/page-img/12.jpg" class="rounded w-100 img-fluid rounded" alt="Responsive image"></li>
            </ul>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Image thumbnails</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>In addition to our <a href="/docs/4.3/utilities/borders/">border-radius utilities</a>, you can use <code>.img-thumbnail</code> to give an image a rounded 1px border appearance.</p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-5">
                    <code>
&lt;b-img :src="require('../../../assets/images/page-img/10.jpg')" alt="Responsive image"&gt;&lt;/b-img&gt;
&lt;b-img right :src="require('../../../assets/images/page-img/11.jpg')" alt="Responsive image"&gt;&lt;/b-img&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-img :src="require('../../../assets/images/page-img/13.jpg')" alt="Responsive image"></b-img>
            <b-img right :src="require('../../../assets/images/page-img/14.jpg')" alt="Responsive image"></b-img>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Media object</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>The images or other media can be aligned top, middle, or bottom. The default is top aligned.</p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-6">
                    <code>
&lt;b-media class="mb-4"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/21.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0"&gt;Top-aligned media&lt;/h5&gt;
    &lt;p&gt;Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.&lt;/p&gt;
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
&lt;b-media vertical-align="center" class="mb-4"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/22.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0 mb-1"&gt;Center-aligned media&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
&lt;b-media vertical-align="end"&gt;
  &lt;template v-slot:aside&gt;
    &lt;b-img :src="require('../../../assets/images/page-img/23.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
  &lt;/template&gt;
  &lt;b-media-body&gt;
    &lt;h5 class="mt-0 mb-1"&gt;Bottom-aligned media&lt;/h5&gt;
    Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
  &lt;/b-media-body&gt;
&lt;/b-media&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <b-media class="mb-4">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/21.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0">Top-aligned media</h5>
                <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
              </b-media-body>
            </b-media>
            <b-media vertical-align="center" class="mb-4">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/22.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0 mb-1">Center-aligned media</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
            <b-media vertical-align="end">
              <template v-slot:aside>
                <b-img :src="require('../../../assets/images/page-img/23.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
              </template>
              <b-media-body>
                <h5 class="mt-0 mb-1">Bottom-aligned media</h5>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media-body>
            </b-media>
          </template>
        </card>
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Media list</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-7 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Because the media object has so few structural requirements, you can also use these classes on list HTML elements. On your <code>&lt;ul&gt;</code> or <code>&lt;ol&gt;</code>, add the <code>.list-unstyled</code> to remove any browser default list styles, and then apply <code>.media</code> to your <code>&lt;li&gt;</code>s. As always, use spacing utilities wherever needed to fine tune.</p>
            <b-collapse id="collapse-7" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="image-7">
                    <code>
&lt;ul class="list-unstyled"&gt;
  &lt;b-media tag="li"&gt;
    &lt;template v-slot:aside&gt;
      &lt;b-img :src="require('../../../assets/images/page-img/24.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
    &lt;/template&gt;
    &lt;b-media-body&gt;
      &lt;h5 class="mt-0"&gt;List-based media object&lt;/h5&gt;
      &lt;p&gt;Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.&lt;/p&gt;
    &lt;/b-media-body&gt;
  &lt;/b-media&gt;
  &lt;b-media tag="li" class="my-4"&gt;
    &lt;template v-slot:aside&gt;
      &lt;b-img :src="require('../../../assets/images/page-img/15.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
    &lt;/template&gt;
    &lt;b-media-body&gt;
      &lt;h5 class="mt-0 mb-1"&gt;List-based media object&lt;/h5&gt;
      Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
    &lt;/b-media-body&gt;
  &lt;/b-media&gt;
  &lt;b-media tag="li"&gt;
    &lt;template v-slot:aside&gt;
      &lt;b-img :src="require('../../../assets/images/page-img/16.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"&gt;&lt;/b-img&gt;
    &lt;/template&gt;
    &lt;b-media-body&gt;
      &lt;h5 class="mt-0 mb-1"&gt;List-based media object&lt;/h5&gt;
      Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
    &lt;/b-media-body&gt;
  &lt;/b-media&gt;
&lt;/ul&gt;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <ul class="list-unstyled">
              <b-media tag="li">
                <template v-slot:aside>
                  <b-img :src="require('../../../assets/images/page-img/24.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
                </template>
                <b-media-body>
                  <h5 class="mt-0">List-based media object</h5>
                  <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                </b-media-body>
              </b-media>
              <b-media tag="li" class="my-4">
                <template v-slot:aside>
                  <b-img :src="require('../../../assets/images/page-img/15.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
                </template>
                <b-media-body>
                  <h5 class="mt-0 mb-1">List-based media object</h5>
                  Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                </b-media-body>
              </b-media>
              <b-media tag="li">
                <template v-slot:aside>
                  <b-img :src="require('../../../assets/images/page-img/16.jpg')" class="mr-3 avatar-70 img-fluid rounded" alt="#"></b-img>
                </template>
                <b-media-body>
                  <h5 class="mt-0 mb-1">List-based media object</h5>
                  Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                </b-media-body>
              </b-media>
            </ul>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiImages',
}
</script>
