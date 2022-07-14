<template>
  <account-layout :active="2">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Cold Wallet Deposit Address</h4>
        </div>
        <div class="card-body" id="deposits">
          <b-tabs>
            <b-tab title="TUSD">
              <bar-code />
            </b-tab>
            <b-tab title="USDC">
              <bar-code />
            </b-tab>
            <b-tab title="FIAT">
              <bar-code />
            </b-tab>
          </b-tabs>
        </div>
      </div>
    </div>
  </account-layout>
</template>

<script>
import BarCode from "../../../components/Dashboard/BarCode.vue";
import AccountLayout from "../../../components/Layouts/AccountLayout.vue";
export default {
  components: { AccountLayout, BarCode },
};
</script>
