<template>
  <ValidationObserver v-slot="{ passes }" tag="div">
    <form
      method="post"
      @submit.prevent="passes(formSubmit)"
      name="myform"
      class="currency_validate"
    >
      <div class="form-group">
        <label class="me-sm-2">Currency</label>
        <div class="input-group mb-3">
          <select name="currency" class="form-control mw-150">
            <option data-display="Bitcoin" value="bitcoin">Bitcoin </option>
            <option value="litecoin">Litecoin</option>
          </select>
          <input
            type="text"
            name="usd_amount"
            class="form-control text-right"
            value="125.00 USD"
          />
        </div>
      </div>

      <div class="form-group">
        <label class="me-sm-2">Payment Method</label>
        <div class="input-group mb-3">
          <select name="currency" class="form-control">
            <option data-display="Bitcoin" value="bitcoin">Bitcoin </option>
            <option value="litecoin">Litecoin</option>
          </select>
          <!-- <input type="text" name="usd_amount" class="form-control"
                                                    value="125.00 USD"> -->
        </div>
      </div>

      <div class="form-group">
        <label class="me-sm-2">Enter your amount</label>
        <ValidationProvider rules="required" v-slot="{ errors }">
          <div class="input-group">
            <input
              type="text"
              name="currency_amount"
              v-model="currency_amount"
              class="form-control"
              placeholder="0.0214 BTC"
            />
            <!-- <input type="text" name="usd_amount" class="form-control"
             
                                                    placeholder="125.00 USD"> -->
            <label class="error" for="currency">{{ errors[0] }}</label>
          </div>
        </ValidationProvider>
        <div class="d-flex justify-content-between mt-3">
          <p class="mb-0">Monthly Limit</p>
          <h6 class="mb-0">$49750 remaining</h6>
        </div>
      </div>
      <button
        type="submit"
        name="submit"
        class="btn  btn-block"
        :class="`btn-${className}`"
      >
        Buy Now
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
  props: {
    className: String,
  },
  data() {
    return {
      currency_amount: "",
    };
  },
  methods: {
    formSubmit(e) {
      e.preventDefault();
    },
  },
};
</script>
