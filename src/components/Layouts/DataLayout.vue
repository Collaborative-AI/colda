<template>
  <div id="main-wrapper" class="show">
    <Header :dark="dark" />
    <Sidebar :active="4" :dark="dark" />
    <Title :dark="dark" />
    <div class="content-body">
      <div class="container">
        <div class="row">
          <div class="col-xl-12">
            <div class="card sub-menu">
              <div class="card-body">
                <ul class="d-flex">
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('tbi')"
                      class="nav-link"
                      :class="active === 1 && 'active'"
                    >
                      <i class="mdi mdi-database-plus"></i>
                      <span>TBI</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('founding-rate')"
                      class="nav-link"
                      :class="active === 2 && 'active'"
                    >
                      <i class="mdi mdi-book"></i>
                      <span>Founding Rate</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('insurance-found')"
                      class="nav-link"
                      :class="active === 3 && 'active'"
                    >
                      <i class="mdi mdi-book-multiple"></i>
                      <span>Insurance Found</span>
                    </router-link>
                  </li>
                  <li class="nav-item dropdown">
                    <a
                      href="#"
                      class="nav-link  dropdown-toggle"
                      data-toggle="dropdown"
                      :class="[active === 4 && 'active', toggle && 'show']"
                      @click="toggle = !toggle"
                    >
                      <i class="mdi mdi-file-export"></i>
                      <span>Export CSV</span>
                    </a>
                    <div
                      class="dropdown-menu dropdown-menu-right"
                      :class="toggle && 'show'"
                    >
                      <router-link
                        class="dropdown-item"
                        :to="darkLink('last-price')"
                        >Last Price</router-link
                      >
                      <router-link
                        class="dropdown-item"
                        :to="darkLink('index-price')"
                        >Index Price</router-link
                      >
                      <router-link
                        class="dropdown-item"
                        :to="darkLink('mark-price')"
                        >Mark Price</router-link
                      >
                      <!-- <a class="dropdown-item" href="#">Founding Rate</a> -->
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <slot />
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "../Dashboard/Footer.vue";
import Header from "../Dashboard/Header.vue";
import Sidebar from "../Dashboard/Sidebar.vue";
import Title from "../Dashboard/Title.vue";
export default {
  components: { Header, Sidebar, Footer, Title },
  name: "DataLayout",
  props: {
    active: Number,
  },
  data() {
    return {
      toggle: false,
      dark: window.location.pathname.includes("dark"),
    };
  },
  mounted() {
    const body = document.querySelector("body");
    if (this.dark) {
      body.className = "dark";
    } else {
      body.className = "light";
    }
  },
  methods: {
    darkLink(name) {
      if (this.dark) {
        return `/data-${name}-dark`;
      } else {
        return `/data-${name}`;
      }
    },
  },
};
</script>
