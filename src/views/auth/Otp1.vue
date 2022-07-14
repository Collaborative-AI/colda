<template>
  <auth-layout>
    <div class="card-body">
      <router-link class="page-back text-muted" to="signin">
        <span><i class="fa fa-angle-left"></i></span> Back</router-link
      >
      <h3 class="text-center">OTP Verification</h3>
      <p class="text-center mb-5">We will send one time code on this number</p>
      <form @submit.prevent="formSubmit">
        <div class="form-group">
          <label>Your phone number</label>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text pl-4 pr-4"
                ><i class="fa fa-phone"></i
              ></span>
            </div>
            <input type="text" class="form-control" value="+1 12365480" />
          </div>
        </div>
        <div class="text-center mt-4">
          <button type="submit" class="btn btn-success btn-block">Send</button>
        </div>
      </form>
      <div class="new-account mt-3 d-flex justify-content-between">
        <p>
          Don't get code?
          <router-link class="text-primary" :to="dark ? 'otp-1-dark' : 'otp-1'"
            >Resend</router-link
          >
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
      this.$router.push(this.dark ? "/otp-2-dark" : "/otp-2");
    },
  },
};
</script>
