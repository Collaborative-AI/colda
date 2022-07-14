<template>
  <auth-layout>
    <div class="card-header justify-content-center">
      <h4 class="card-title">Sign in</h4>
    </div>
    <div class="card-body">
      <ValidationObserver v-slot="{ passes }" tag="div">
        <form
          @submit.prevent="passes(formSubmit)"
          class="signin_validate"
          action="otp-1"
          novalidate=""
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
              class="form-control error"
              placeholder="hello@example.com"
              name="email"
              v-model="email"
              aria-invalid="true"
            />
            <!-- <label class="error" for="email">{{ errors[0] }}</label> -->
            <div class="invalid-feedback d-block">
              {{ errors[0] }}
            </div>
          </ValidationProvider>
          <ValidationProvider
            rules="passwordFieldName|verify_password"
            v-slot="{ errors }"
            name="password"
            class="form-group"
            tag="div"
          >
            <label>Password</label>
            <input
              type="password"
              class="form-control error"
              placeholder="Password"
              name="password"
              v-model="password"
              aria-invalid="true"
            />
            <div class="invalid-feedback d-block">
              {{ errors[0] }}
            </div>
          </ValidationProvider>
          <div class="d-flex justify-content-between">
            <div class="input-group-form mb-0">
              <label class="toggle">
                <input class="toggle-checkbox" type="checkbox" />
                <span class="toggle-switch"></span>
                <span class="toggle-label">Remember me</span>
              </label>
            </div>
            <div class="form-group">
              <router-link
                class="text-primary"
                :to="dark ? 'reset-dark' : 'reset'"
                >Forgot Password?</router-link
              >
            </div>
          </div>
          <div>
            <button type="submit" class="btn btn-success btn-block">
              Sign in
            </button>
          </div>
        </form>
      </ValidationObserver>
      <div class="new-account mt-3">
        <p>
          Don't have an account?
          <router-link
            class="text-primary"
            :to="dark ? 'signup-dark' : 'signup'"
            >Sign up</router-link
          >
        </p>
      </div>
    </div>
  </auth-layout>
</template>

<script>
import { ValidationObserver, ValidationProvider } from "vee-validate";
import AuthLayout from "../../components/Layouts/AuthLayout";
export default {
  components: {
    ValidationObserver,
    ValidationProvider,
    AuthLayout,
  },
  data() {
    return {
      email: "",
      password: "",
      checkbox: "",
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    formSubmit() {
      this.$router.push(this.dark ? "/otp-1-dark" : "/otp-1");
    },
  },
};
</script>
