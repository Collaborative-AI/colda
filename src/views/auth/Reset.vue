<template>
  <auth-layout>
    <div class="card-header justify-content-center">
      <h4 class="card-title">Reset password</h4>
    </div>
    <div class="card-body">
      <ValidationObserver v-slot="{ passes }">
        <form
          class="needs-validation"
          novalidate=""
          @submit.prevent="passes(formSubmit)"
        >
          <ValidationProvider
            rules="required|email"
            v-slot="{ errors }"
            name="method"
            class="form-group"
            tag="div"
          >
            <label>Email</label>
            <input
              type="email"
              class="form-control"
              name="email"
              v-model="email"
              placeholder="hello@example.com"
            />
            <div class="invalid-feedback d-block">
              {{ errors[0] }}
            </div>
          </ValidationProvider>
          <div>
            <button type="submit" class="btn btn-success  w-100">
              Reset
            </button>
          </div>
        </form>
      </ValidationObserver>
      <div class="new-account mt-3">
        <p class="mb-1">Don't Received?</p>
        <router-link class="text-primary" :to="dark ? 'reset-dark' : 'reset'"
          >Resend
        </router-link>
      </div>
    </div>
  </auth-layout>
</template>

<script>
import AuthLayout from "../../components/Layouts/AuthLayout.vue";
import { ValidationObserver, ValidationProvider } from "vee-validate";
export default {
  components: { AuthLayout, ValidationObserver, ValidationProvider },
  data() {
    return {
      email: "",
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    formSubmit() {
      this.$router.push(this.dark ? "/signin-dark" : "/signin");
    },
  },
};
</script>
