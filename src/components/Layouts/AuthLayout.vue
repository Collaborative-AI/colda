<template>
  <div id="main-wrapper" class="show">
    <div class="authincation section-padding">
      <div class="container h-100">
        <div class="row justify-content-center h-100 align-items-center">
          <div class="col-xl-5 col-md-6">
            <div class="mini-logo text-center my-5">
              <router-link to="/"
                ><img src="../../assets/images/logo.png" alt=""
              /></router-link>
            </div>
            <div class="auth-form card">
              <slot />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthLayout",
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
