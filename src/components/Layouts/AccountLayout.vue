<template>
  <div id="main-wrapper" class="show">
    <Header :dark="dark" />
    <Sidebar :active="3" :dark="dark" />
    <Title :dark="dark" />
    <div class="content-body">
      <div class="container">
        <div class="row">
          <div class="col-xl-12">
            <div class="card sub-menu">
              <div class="card-body active">
                <ul class="d-flex show">
                  <li class="nav-item active">
                    <router-link
                      :to="darkLink('overview')"
                      class="nav-link"
                      :class="active === 1 && 'active'"
                    >
                      <i class="mdi mdi-bullseye"></i>
                      <span>Overview</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('deposit')"
                      class="nav-link"
                      :class="active === 2 && 'active'"
                    >
                      <i class="mdi mdi-heart"></i>
                      <span>Deposit</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('withdraw')"
                      class="nav-link"
                      :class="active === 3 && 'active'"
                    >
                      <i class="mdi mdi-pentagon"></i>
                      <span>Withdraw</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('api')"
                      class="nav-link"
                      :class="active === 4 && 'active'"
                    >
                      <i class="mdi mdi-database"></i>
                      <span>API</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('affiliate')"
                      class="nav-link"
                      :class="active === 5 && 'active'"
                    >
                      <i class="mdi mdi-diamond"></i>
                      <span>Affiliate</span>
                    </router-link>
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
  name: "AccountLayout",
  props: {
    title: Boolean,
    active: Number,
  },
  data() {
    return {
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
      console.log(this.dark);
      if (this.dark) {
        return `/account-${name}-dark`;
      } else {
        return `/account-${name}`;
      }
    },
  },
};
</script>
