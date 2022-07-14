<template>
  <ValidationObserver v-slot="{ passes }" tag="div">
    <form
      @submit.prevent="passes(formSubmit)"
      class="currency_validate"
      method="post"
    >
      <div class="mb-4 form-group">
        <label class="me-sm-2">Send</label>
        <div class="invalid-feedback">This field is required.</div>

        <div class="form-group d-flex">
          <ValidationProvider
            rules="required"
            v-slot="{ errors }"
            name="currency"
            tag="div"
            class="w-50"
          >
            <select name="currency" v-model="currency" class="form-control">
              <option value="1">Bitcoin</option>
              <option value="2">Litecoin</option>
            </select>
            <label class="error" for="currency">{{ errors[0] }}</label>
          </ValidationProvider>
          <ValidationProvider
            rules="required"
            v-slot="{ errors }"
            name="usd_amount"
            tag="div"
            class="w-50"
          >
            <input
              type="text"
              name="usd_amount"
              v-model="usd_amount"
              class="form-control"
              placeholder="125.00 USD"
            />
            <label class="error" for="currency">{{ errors[0] }}</label>
          </ValidationProvider>
        </div>
      </div>
      <div class="mb-4">
        <label class="me-sm-2">Get</label>
        <div class="invalid-feedback">This field is required.</div>
        <div class="input-group mb-3">
          <ValidationProvider
            rules="required"
            v-slot="{ errors }"
            name="currency_1"
            v-model="currency_1"
            tag="div"
            class="w-50"
          >
            <select
              name="currency_1"
              v-model="currency_1"
              class="form-control"
              aria-placeholder="Bitconin"
            >
              <option value="3" selected>Bitcoin</option>
              <option value="4">Litecoin</option>
            </select>
            <label class="error" for="currency_1">{{ errors[0] }}</label>
          </ValidationProvider>
          <ValidationProvider
            rules="required"
            v-slot="{ errors }"
            name="usd_amount_1"
            v-model="usd_amount_1"
            tag="div"
            class="w-50"
          >
            <input
              type="text"
              name="usd_amount_1"
              v-model="usd_amount_1"
              class="form-control"
              placeholder="125.00 USD"
            />
            <label class="error" for="usd_amount_1">{{ errors[0] }}</label>
          </ValidationProvider>
        </div>
        <div class="d-flex justify-content-between mt-0 align-items-center">
          <p class=" mb-0">Monthly Limit</p>
          <span class="mb-0 text-dark-400 fs-6 fw-semi-bold"
            >$49750 remaining</span
          >
        </div>
      </div>
      <button type="submit" name="submit" class="btn btn-success btn-block">
        Exchange Now
        <i class="la la-arrow-right"></i>
      </button>
    </form>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver, ValidationProvider } from "vee-validate";

export default {
  name: "CurrencyForm",
  components: {
    ValidationObserver,
    ValidationProvider,
  },
  data() {
    return {
      // erros: {},
      currency: 1,
      currency_1: 3,
      method: "",
      currency_amount: "",
      usd_amount: "",
      usd_amount_1: "",
      submitted: false,
    };
  },
  methods: {
    formSubmit() {
      this.$router.push("/signin");
    },
  },
};
</script>
