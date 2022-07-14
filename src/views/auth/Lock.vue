<template>
  <auth-layout>
    <div class="card-header justify-content-center">
      <h4 class="card-title">Locked</h4>
    </div>
    <div class="card-body">
      <ValidationObserver v-slot="{ passes }">
        <form novalidate="" @submit.prevent="passes(formSubmit)">
          <ValidationProvider
            tag="div"
            rules="required"
            name="password"
            v-slot="{ errors }"
            class="form-group mb-4"
          >
            <label>Enter Password</label>
            <input
              type="password"
              class="form-control"
              placeholder="Password"
              name="password"
              v-model="password"
            />
            <div class="invalid-feedback d-block">
              {{ errors[0] }}
            </div>
          </ValidationProvider>
          <div>
            <button class="btn-success btn-block btn-lg border-0" type="submit">
              Unlock
            </button>
          </div>
        </form>
      </ValidationObserver>
      <div class="new-account text-center mt-3">
        <router-link class="text-primary" :to="dark ? 'reset-dark' : 'reset'">
          <h5>Not Sabuj Hasan Sarker ?</h5>
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
      password: "",
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    formSubmit() {
      this.$router.push(this.dark ? "/dark" : "/");
    },
  },
};
</script>
