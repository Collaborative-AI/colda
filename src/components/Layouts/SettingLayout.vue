<template>
  <div id="main-wrapper" class="show">
    <Header :dark="dark" />
    <Sidebar :active="5" :dark="dark" />
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
                      :to="dark ? '/settings-dark' : '/settings'"
                      class="nav-link"
                      :class="active === 1 && 'active'"
                    >
                      <i class="mdi mdi-account-settings-variant"></i>
                      <span>Edit Profile</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('preferences')"
                      class="nav-link"
                      :class="active === 2 && 'active'"
                    >
                      <i class="mdi mdi-settings"></i>
                      <span>Preferences</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('security')"
                      class="nav-link"
                      :class="active === 3 && 'active'"
                    >
                      <i class="mdi mdi-lock"></i>
                      <span>Security</span>
                    </router-link>
                  </li>
                  <li class="nav-item">
                    <router-link
                      :to="darkLink('account')"
                      class="nav-link"
                      :class="active === 4 && 'active'"
                    >
                      <i class="mdi mdi-bank"></i>
                      <span>Linked Account</span>
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
  name: "SettingLayout",
  props: {
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
      if (this.dark) {
        return `/settings-${name}-dark`;
      } else {
        return `/settings-${name}`;
      }
    },
  },
};
</script>
