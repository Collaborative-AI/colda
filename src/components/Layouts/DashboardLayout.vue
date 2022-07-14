<template>
  <div id="main-wrapper" class="show">
    <Header :dark="dark" />
    <Sidebar :active="active" :dark="dark" />
    <Title v-if="title" :dark="dark" />
    <div class="content-body">
      <div :class="container ? 'container-fluid' : 'container'">
        <slot />
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
  name: "DashboardLayout",
  props: {
    title: Boolean,
    active: Number,
    container: Boolean,
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
};
</script>
