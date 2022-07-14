<template>
  <auth-layout>
    <div class="card-body">
      <router-link class="page-back text-muted" to="otp-1"
        ><span><i class="fa fa-angle-left"></i></span> Back</router-link
      >
      <h3 class="text-center">OTP Verification</h3>
      <p class="text-center mb-5">We will send one time code on this number</p>
      <form @submit.prevent="formSubmit">
        <div class="form-group">
          <label>Your OTP Code</label>
          <input
            type="text"
            class="form-control text-center font-weight-bold"
            value="11 22 33"
          />
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-success btn-block">
            Verify
          </button>
        </div>
      </form>
      <div class="info mt-3">
        <p class="text-muted">
          You dont recommended to save password to browsers!
        </p>
      </div>
    </div>
  </auth-layout>
</template>

<script>
import AuthLayout from "../../components/Layouts/AuthLayout.vue";
export default {
  components: { AuthLayout },
  data() {
    return {
      password: "",
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    formSubmit() {
      this.$router.push(this.dark ? "/dashboard-dark" : "/dashboard");
    },
  },
};
</script>
