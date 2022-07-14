<template>
  <auth-layout>
    <div class="card-header justify-content-center">
      <h4 class="card-title">Sign up your account</h4>
    </div>
    <div class="card-body">
      <ValidationObserver v-slot="{ passes }" tag="div">
        <form
          @submit.prevent="passes(formSubmit)"
          class="needs-validation"
          novalidate=""
        >
          <ValidationProvider
            rules="required"
            v-slot="{ errors }"
            name="username"
            class="form-group"
            tag="div"
          >
            <label>Username</label>
            <input
              type="text"
              class="form-control error"
              placeholder="Username"
              name="username"
              v-model="username"
              aria-invalid="true"
            />
            <!-- <label class="error" for="email">{{ errors[0] }}</label> -->
            <div class="invalid-feedback d-block">
              {{ errors[0] }}
            </div>
          </ValidationProvider>

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
          <div>
            <button type="submit" class="btn btn-success btn-block">
              Sign in
            </button>
          </div>
        </form>
      </ValidationObserver>
      <div class="new-account mt-3">
        <p>
          Already have an account?
          <router-link
            class="text-primary"
            :to="dark ? 'signin-dark' : 'signin'"
            >Sign in</router-link
          >
        </p>
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
      username: "",
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
