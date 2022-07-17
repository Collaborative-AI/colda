<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-1 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use the items in order to programatically generate the breadcrumb links.use class <code>.breadcrumb to ol</code></p>
            <b-collapse id="collapse-1" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-1">
                    <code>
&lt;b-breadcrumb :items="items1" /&gt;
&lt;b-breadcrumb :items="items2" /&gt;
&lt;b-breadcrumb :items="items3" /&gt;

&lt;script&gt;
export default {
  data() {
    return {
      items1: [
        {
          text: 'Home',
          active: true
        }
      ],
      items2: [
        {
          text: 'Home',
          href: '#'
        },
        {
          text: 'Library',
          active: true
        }
      ],
      items3: [
        {
          text: 'Home',
          href: '#'
        },
        {
          text: 'Library',
          href: '#'
        },
        {
          text: 'Data',
          active: true
        }
      ]
    }
  }
}
</code></pre>
                </kbd>
              </div>
            </b-collapse>
             <b-breadcrumb :items="items1" />
             <b-breadcrumb :items="items2" />
             <b-breadcrumb :items="items3" />
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb With Icon</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-2 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>Use the items in order to programatically generate the breadcrumb links.use class <code>.breadcrumb to ol</code> with Icon</p>
            <b-collapse id="collapse-2" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-icon-1">
                    <code>
&lt;b-breadcrumb :items="itemsIcon1" /&gt;
&lt;b-breadcrumb :items="itemsIcon2" /&gt;
&lt;b-breadcrumb :items="itemsIcon3" /&gt;

&lt;script&gt;
export default {
  data() {
    return {
      itemsIcon1: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          active: true
        }
      ],
      itemsIcon2: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          href: '#'
        },
        {
          text: 'Library',
          active: true
        }
      ],
      itemsIcon3: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          href: '#'
        },
        {
          text: 'Library',
          href: '#'
        },
        {
          text: 'Data',
          active: true
        }
      ]
    }
  }
}
</code></pre>
                </kbd>
              </div>
            </b-collapse>
             <b-breadcrumb :items="itemsIcon1" />
             <b-breadcrumb :items="itemsIcon2" />
             <b-breadcrumb :items="itemsIcon3" />
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-3 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>use class <code>.breadcrumb .bg-primary</code></p>
            <b-collapse id="collapse-3" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-2">
                    <code>
&#x3C;nav aria-label=&#x22;breadcrumb &#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;Home&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;Library&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary mb-0&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;Library&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;Data&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <nav aria-label="breadcrumb ">
              <ol class="breadcrumb bg-primary">
                <li class="breadcrumb-item active text-white" aria-current="page">Home</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb bg-primary">
                <li class="breadcrumb-item"><a href="#" class="text-white">Home</a></li>
                <li class="breadcrumb-item active text-white" aria-current="page">Library</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb bg-primary mb-0">
                <li class="breadcrumb-item"><a href="#" class="text-white">Home</a></li>
                <li class="breadcrumb-item"><a href="#" class="text-white">Library</a></li>
                <li class="breadcrumb-item active text-white" aria-current="page">Data</li>
              </ol>
            </nav>
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb With Icon</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-4 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>use class <code>.breadcrumb .bg-primary </code> With Icon.</p>
            <b-collapse id="collapse-4" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-icon-2">
                    <code>
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;Library&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
  &#x3C;ol class=&#x22;breadcrumb bg-primary mb-0&#x22;&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-white&#x22;&#x3E;Library&#x3C;/a&#x3E;&#x3C;/li&#x3E;
    &#x3C;li class=&#x22;breadcrumb-item active text-white&#x22; aria-current=&#x22;page&#x22;&#x3E;Data&#x3C;/li&#x3E;
  &#x3C;/ol&#x3E;
&#x3C;/nav&#x3E;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb bg-primary">
                <li class="breadcrumb-item active text-white" aria-current="page"><i class="ri-home-4-line mr-1 float-left"></i>Home</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb bg-primary">
                <li class="breadcrumb-item"><a href="#" class="text-white"><i class="ri-home-4-line mr-1 float-left"></i>Home</a></li>
                <li class="breadcrumb-item active text-white" aria-current="page">Library</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb bg-primary mb-0">
                <li class="breadcrumb-item"><a href="#" class="text-white"><i class="ri-home-4-line mr-1 float-left"></i>Home</a></li>
                <li class="breadcrumb-item"><a href="#" class="text-white">Library</a></li>
                <li class="breadcrumb-item active text-white" aria-current="page">Data</li>
              </ol>
            </nav>
          </template>
        </card>
      </b-col>
    </b-row>
    <b-row>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb With Icon</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-5 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>use class <code>.breadcrumb .iq-bg-primary</code></p>
            <b-collapse id="collapse-5" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-icon-3">
                    <code>
&lt;b-breadcrumb class="iq-bg-primary" :items="itemsIcon1" /&gt;
&lt;b-breadcrumb class="iq-bg-primary" :items="itemsIcon2" /&gt;
&lt;b-breadcrumb class="iq-bg-primary" :items="itemsIcon3" /&gt;

&lt;script&gt;
export default {
  data() {
    return {
      itemsIcon1: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          active: true
        }
      ],
      itemsIcon2: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          href: '#'
        },
        {
          text: 'Library',
          active: true
        }
      ],
      itemsIcon3: [
        {
          html: '&lt;i class="ri-home-4-line mr-1 float-left"&gt;&lt;/i&gt;Home',
          href: '#'
        },
        {
          text: 'Library',
          href: '#'
        },
        {
          text: 'Data',
          active: true
        }
      ]
    }
  }
}
</code></pre>
                </kbd>
              </div>
            </b-collapse>
             <b-breadcrumb class="iq-bg-primary" :items="itemsIcon1" />
             <b-breadcrumb class="iq-bg-primary" :items="itemsIcon2" />
             <b-breadcrumb class="iq-bg-primary mb-0" :items="itemsIcon3" />
          </template>
        </card>
      </b-col>
      <b-col lg="6" sm="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Breadcrumb With Icon</h4>
          </template>
          <template v-slot:headerAction>
            <a class="text-primary float-right" v-b-toggle.collapse-6 role="button">
              <i class="ri-code-s-slash-line" />
            </a>
          </template>
          <template v-slot:body>
            <p>use class <code>.breadcrumb .iq-bg-danger</code></p>
            <b-collapse id="collapse-6" class="mb-2">
              <div class="card">
                <kbd class="bg-dark">
                  <pre class="text-white" id="breadcrumb-icon-4">
                    <code>
&#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
    &#x3C;ol class=&#x22;breadcrumb iq-bg-danger&#x22;&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item active&#x22; aria-current=&#x22;page&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/li&#x3E;
    &#x3C;/ol&#x3E;
  &#x3C;/nav&#x3E;
  &#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
    &#x3C;ol class=&#x22;breadcrumb iq-bg-danger&#x22;&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-danger&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item active&#x22; aria-current=&#x22;page&#x22;&#x3E;Library&#x3C;/li&#x3E;
    &#x3C;/ol&#x3E;
  &#x3C;/nav&#x3E;
  &#x3C;nav aria-label=&#x22;breadcrumb&#x22;&#x3E;
    &#x3C;ol class=&#x22;breadcrumb iq-bg-danger mb-0&#x22;&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-danger&#x22;&#x3E;&#x3C;i class=&#x22;ri-home-4-line mr-1 float-left&#x22;&#x3E;&#x3C;/i&#x3E;Home&#x3C;/a&#x3E;&#x3C;/li&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item&#x22;&#x3E;&#x3C;a href=&#x22;#&#x22; class=&#x22;text-danger&#x22;&#x3E;Library&#x3C;/a&#x3E;&#x3C;/li&#x3E;
      &#x3C;li class=&#x22;breadcrumb-item active&#x22; aria-current=&#x22;page&#x22;&#x3E;Data&#x3C;/li&#x3E;
    &#x3C;/ol&#x3E;
  &#x3C;/nav&#x3E;
</code></pre>
                </kbd>
              </div>
            </b-collapse>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb iq-bg-danger">
                <li class="breadcrumb-item active" aria-current="page"><i class="ri-home-4-line mr-1 float-left"></i>Home</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb iq-bg-danger">
                <li class="breadcrumb-item"><a href="#" class="text-danger"><i class="ri-home-4-line mr-1 float-left"></i>Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb iq-bg-danger mb-0">
                <li class="breadcrumb-item"><a href="#" class="text-danger"><i class="ri-home-4-line mr-1 float-left"></i>Home</a></li>
                <li class="breadcrumb-item"><a href="#" class="text-danger">Library</a></li>
                <li class="breadcrumb-item active" aria-current="page">Data</li>
              </ol>
            </nav>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiBreadcrumb',
  data () {
    return {
      items1: [
        {
          text: 'Home',
          active: true
        }
      ],
      items2: [
        {
          text: 'Home',
          href: '#'
        },
        {
          text: 'Library',
          active: true
        }
      ],
      items3: [
        {
          text: 'Home',
          href: '#'
        },
        {
          text: 'Library',
          href: '#'
        },
        {
          text: 'Data',
          active: true
        }
      ],
      itemsIcon1: [
        {
          html: '<i class="ri-home-4-line mr-1 float-left"></i>Home',
          active: true
        }
      ],
      itemsIcon2: [
        {
          html: '<i class="ri-home-4-line mr-1 float-left"></i>Home',
          href: '#'
        },
        {
          text: 'Library',
          active: true
        }
      ],
      itemsIcon3: [
        {
          html: '<i class="ri-home-4-line mr-1 float-left"></i>Home',
          href: '#'
        },
        {
          text: 'Library',
          href: '#'
        },
        {
          text: 'Data',
          active: true
        }
      ]
    }
  }
}
</script>
