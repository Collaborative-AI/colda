<template>
  <b-container fluid>
    <b-row>
      <b-col sm="3">
        <b-card
        title="Card Title"
        :img-src="require('../../../assets/images/page-img/07.jpg')"
        img-alt="#"
        img-top
        class="iq-mb-3"
        >
        <b-card-text>
          It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
        </b-card-text>
        <b-button href="#" variant="primary">Button</b-button>
        </b-card>
      </b-col>
      <b-col sm="3">
        <b-card
          title="Card Title"
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-top
          class="iq-mb-3"
        >
          <b-card-text>
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
          </b-card-text>
          <p>It is a long established fact that a the readable content of a page when looking at its layout.</p>
          <a href="#" class="card-link">Card link</a>
          <b-link href="#" class="card-link">Another link</b-link>
        </b-card>
      </b-col>
      <b-col sm="3">
        <b-card
          title="Card Title"
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-top
          class="iq-mb-3"
        >
          <b-card-text>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</b-card-text>
          <b-list-group flush>
            <b-list-group-item>Cras justo odio</b-list-group-item>
            <b-list-group-item>Vestibulum at eros</b-list-group-item>
          </b-list-group>
        </b-card>
      </b-col>
      <b-col sm="3">
        <b-card
          no-body
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-top
        >
          <b-card-body>
            <b-card-title>Card Title</b-card-title>
            <b-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</b-card-text>
          </b-card-body>
          <b-list-group flush>
            <b-list-group-item>Cras justo odio</b-list-group-item>
          </b-list-group>
          <b-card-body>
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="6">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
        >
          <b-card-text>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</b-card-text>
          <b-button href="#" block variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
      <b-col sm="6">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
        >
          <b-card-text>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</b-card-text>
          <b-button href="#" block variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col lg="4">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
          header="Featured"
        >
          <b-card-text>With supporting text below as a natural lead-in to additional content.</b-card-text>
          <b-button href="#" variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card header="Quote">
          <blockquote class="blockquote mb-0">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer">
              Someone famous in <cite title="Source Title">Source Title</cite>
            </footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          header="Featured"
          footer="2 days ago"
          footer-tag="footer"
          footer-class="text-muted"
        >
          <b-button href="#" variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col lg="4">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
        >
          <b-card-text>
            With supporting text below as a natural lead-in to additional content.
          </b-card-text>
          <b-button href="#" block variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
      <b-col lg="4" class="text-center">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
        >
          <b-card-text>
            With supporting text below as a natural lead-in to additional content.
          </b-card-text>
          <b-button href="#" block variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
      <b-col lg="4" class="text-right">
        <b-card
          title="Special title treatment"
          class="iq-mb-3"
        >
          <b-card-text>
            With supporting text below as a natural lead-in to additional content.
          </b-card-text>
          <b-button href="#" block variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="4">
        <b-card
          title="Card title"
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-top
          class="iq-mb-3"
        >
          <b-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</b-card-text>
          <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
        </b-card>
      </b-col>
      <b-col sm="4">
        <b-card
          title="Card title"
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-bottom
          class="iq-mb-3"
        >
          <b-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</b-card-text>
          <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
        </b-card>
      </b-col>
      <b-col sm="4">
        <b-card
          bg-variant="dark"
          text-variant="white"
          title="Card title"
          overlay
          :img-src="require('../../../assets/images/page-img/07.jpg')"
          img-alt="#"
          img-bottom
          class="iq-mb-3"
        >
          <b-card-text>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</b-card-text>
          <b-card-text>Last updated 3 mins ago</b-card-text>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="12">
        <h3 class="mt-4 mb-3">Horizontal Card</h3>
      </b-col>
      <b-col lg="6">
        <b-card no-body class="iq-mb-3">
          <b-row no-gutters>
            <b-col md="4">
              <b-card-img :src="require('../../../assets/images/page-img/08.jpg')"></b-card-img>
            </b-col>
            <b-col md="8">
              <b-card-body title="Card Title">
                <b-card-text>
                  This is a wider card with supporting text below as a natural lead-in. a little bit longer.
                </b-card-text>
                <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </b-col>
      <b-col lg="6">
        <b-card no-body class="iq-mb-3">
          <b-row no-gutters class="flex-row-reverse">
            <b-col md="4">
              <b-card-img :src="require('../../../assets/images/page-img/09.jpg')"></b-card-img>
            </b-col>
            <b-col md="8">
              <b-card-body title="Card Title" align="right">
                <b-card-text>
                  This is a wider card with supporting text below as a natural lead-in. a little bit longer.
                </b-card-text>
                <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
              </b-card-body>
            </b-col>
          </b-row>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="12">
        <h3 class="mt-4 mb-3">Card Colored Styles</h3>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="primary"
          class="iq-mb-3"
        >
        <b-card-title class="text-white">Primary card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="secondary"
          class="iq-mb-3"
        >
          <b-card-title class="text-white">Secondary card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="success"
          class="iq-mb-3"
        >
        <b-card-title class="text-white">Success card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="danger"
          class="iq-mb-3"
        >
          <b-card-title class="text-white">Danger card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="warning"
          class="iq-mb-3"
        >
          <b-card-title class="text-white">Warning card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="white"
          bg-variant="info"
          class="iq-mb-3"
        >
        <b-card-title class="text-white">Info card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-white font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="12">
        <h3 class="mt-4 mb-3">Border Card</h3>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="primary"
          border-variant="primary"
          class="iq-mb-3"
        >
          <b-card-title class="text-primary">Primary card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-primary font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="secondary"
          border-variant="secondary"
          class="iq-mb-3"
        >
          <b-card-title class="text-secondary">Secondary card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-secondary font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="success"
          border-variant="success"
          class="iq-mb-3"
        >
          <b-card-title class="text-success">Success card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-success font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="danger"
          border-variant="danger"
          class="iq-mb-3"
        >
          <b-card-title class="text-danger">Danger card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-danger font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="warning"
          border-variant="warning"
          class="iq-mb-3"
        >
          <b-card-title class="text-warning">Warning card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-warning font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
      <b-col lg="4">
        <b-card
          text-variant="info"
          border-variant="info"
          class="iq-mb-3"
        >
          <b-card-title class="text-info">Info card title</b-card-title>
          <blockquote class="blockquote mb-0">
            <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
            <footer class="blockquote-footer text-info font-size-12">Someone famous in <cite title="Source Title">Source Title</cite></footer>
          </blockquote>
        </b-card>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="12">
        <h3 class="mt-4 mb-3">Card groups</h3>
      </b-col>
      <b-col sm="12">
        <b-card-group class="iq-mb-3">
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This is a wider card with supporting text below as a natural lead-in to additional content.
              This content is a little bit longer.
            </b-card-text>
            <b-card-text>
              <small class="text-muted">Last updated 3 mins ago</small>
            </b-card-text>
          </b-card>
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This card has supporting text below as a natural lead-in to additional content.
            </b-card-text>
            <b-card-text>
              <small class="text-muted">Last updated 3 mins ago</small>
            </b-card-text>
          </b-card>
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This is a wider card with supporting text below as a natural lead-in to additional content.
              This card has even longer content than the first to show that equal height action.
            </b-card-text>
            <b-card-text>
              <small class="text-muted">Last updated 3 mins ago</small>
            </b-card-text>
          </b-card>
        </b-card-group>
      </b-col>
      <b-col sm="12">
        <b-card-group class="iq-mb-3">
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This is a wider card with supporting text below as a natural lead-in to additional content.
              This content is a little bit longer.
            </b-card-text>
            <template v-slot:footer>
              <small class="text-muted">Last updated 3 mins ago</small>
            </template>
          </b-card>
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This card has supporting text below as a natural lead-in to additional content.
            </b-card-text>
            <template v-slot:footer>
              <small class="text-muted">Last updated 3 mins ago</small>
            </template>
          </b-card>
          <b-card title="Card title" :img-src="require('../../../assets/images/page-img/07.jpg')" img-alt="#" img-top>
            <b-card-text>
              This is a wider card with supporting text below as a natural lead-in to additional content.
              This card has even longer content than the first to show that equal height action.
            </b-card-text>
            <template v-slot:footer>
              <small class="text-muted">Last updated 3 mins ago</small>
            </template>
          </b-card>
        </b-card-group>
      </b-col>
      <b-col sm="12">
        <h3 class="mb-3">Card Masonry Columns</h3>
        <b-card-group columns>
          <b-card
            title="Card title that wraps to a new line"
            :img-src="require('../../../assets/images/page-img/07.jpg')"
            img-alt="#"
            img-top
            class="iq-mb-3"
          >
            <b-card-text>
              This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.
            </b-card-text>
          </b-card>
          <b-card no-body class="iq-mb-3">
            <blockquote class="blockquote mb-0 card-body">
              <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer class="blockquote-footer">
                <small class="text-muted">Someone famous in <cite title="Source Title">Source Title</cite></small>
              </footer>
            </blockquote>
          </b-card>
          <b-card
            title="Card title"
            :img-src="require('../../../assets/images/page-img/07.jpg')"
            img-alt="#"
            img-top
            class="iq-mb-3"
          >
            <b-card-text>This is a longer card with supporting text below as a natural lead-in to additional content.</b-card-text>
            <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
          </b-card>
          <b-card no-body class="iq-mb-3 text-center" bg-variant="primary" text-variant="white">
            <blockquote class="blockquote mb-0 card-body">
              <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer class="blockquote-footer">
                <small class="text-white">Someone famous in <cite title="Source Title">Source Title</cite></small>
              </footer>
            </blockquote>
          </b-card>
          <b-card title="Card title" class="iq-mb-3 text-center">
            <b-card-text>This card has a regular title and short paragraphy of text below it.</b-card-text>
            <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
          </b-card>
          <b-card
            :img-src="require('../../../assets/images/page-img/07.jpg')"
            img-alt="#"
            img-top
            class="iq-mb-3"
            no-body
          >
          </b-card>
          <b-card no-body class="iq-mb-3 text-right">
            <blockquote class="blockquote mb-0 card-body">
              <p class="font-size-14">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
              <footer class="blockquote-footer">
                <small class="text-muted">Someone famous in <cite title="Source Title">Source Title</cite></small>
              </footer>
            </blockquote>
          </b-card>
          <b-card title="Card title" class="iq-mb-3">
            <b-card-text>This is another card with title and supporting text below. This card has some additional content to make it slightly taller overall.</b-card-text>
            <b-card-text><small class="text-muted">Last updated 3 mins ago</small></b-card-text>
          </b-card>
        </b-card-group>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: 'UiCards',
}
</script>
