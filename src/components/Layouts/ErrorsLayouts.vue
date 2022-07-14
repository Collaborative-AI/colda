<template>
  <div class="authincation h-100">
    <div class="container h-100">
      <div class="row justify-content-center h-100 align-items-center">
        <div class="col-md-5">
          <div class="form-input-content text-center">
            <slot />
            <div class="mb-5">
              <router-link class="btn btn-primary" to="/"
                >Back to Home</router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ErrorsLayout",
  data() {
    return {
      toggle: false,
      dark: window.location.pathname.includes("dark"),
    };
  },
  mounted() {
    document.querySelector("body").className = "h-100";
    document.querySelector("html").className = "h-100";
    document.querySelector("#app").className = "h-100";
    const body = document.querySelector("body");
    if (this.dark) {
      body.className = "dark";
    } else {
      body.className = "light";
    }
  },
};
</script>
