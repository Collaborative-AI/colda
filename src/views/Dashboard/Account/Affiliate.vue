<template>
  <account-layout :active="5">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Affiliate Program</h4>
        </div>
        <div class="card-body">
          <div class="row justify-content-between">
            <div class="col-xl-6 col-lg-6">
              <h5>Affiliate Link</h5>
              <p>
                Copy and paste this link to send to friends or use in your
                articles. When users sign up using this link, your account will
                be credited with referral bonuses.
              </p>
            </div>
            <div class="col-xl-5 col-lg-6">
              <h5>Share your link</h5>
              <form action="">
                <div class="input-group">
                  <input type="text" class="form-control" :value="message" />
                  <div class="input-group-append">
                    <span
                      class="input-group-text bg-primary text-white c-pointer"
                      @click="doCopy"
                      >Copy</span
                    >
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Affiliate Status</h4>
          <small class="mb-0">Pay on a daily basis</small>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Index</th>
                  <th>Total</th>
                  <th>Previous Day</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Invites</td>
                  <td>5 User</td>
                  <td>3 User</td>
                </tr>
                <tr>
                  <td>Total Turnover</td>
                  <td>0.248 BTC</td>
                  <td>0.354 BTC</td>
                </tr>
                <tr>
                  <td>Free Paid</td>
                  <td>0.255 BTC</td>
                  <td>0.253 BTC</td>
                </tr>
                <tr>
                  <td>Affiliate Level (% of Commissions)</td>
                  <td>50%</td>
                  <td></td>
                </tr>
              </tbody>
              <tfoot>
                <tr>
                  <th>
                    Affiliate Payouts
                    <br />
                    <small>Not listed on affiliate leaderboard</small>
                  </th>
                  <th>0.925 BTC</th>
                  <th>0.235 BTC</th>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Affiliate Payout Status</h4>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Time</th>
                  <th>Free Paid (BTC)</th>
                  <th>Affiliate Level</th>
                  <th>Payouts (BTC)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>March 8th, 2020</td>
                  <td>0.2954 BTC</td>
                  <td>Level 3</td>
                  <td>0.2547 BTC</td>
                </tr>
                <tr>
                  <td>March 8th, 2020</td>
                  <td>0.2954 BTC</td>
                  <td>Level 3</td>
                  <td>0.2547 BTC</td>
                </tr>
                <tr>
                  <td>March 8th, 2020</td>
                  <td>0.2954 BTC</td>
                  <td>Level 3</td>
                  <td>0.2547 BTC</td>
                </tr>
                <tr>
                  <td>March 8th, 2020</td>
                  <td>0.2954 BTC</td>
                  <td>Level 3</td>
                  <td>0.2547 BTC</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </account-layout>
</template>

<script>
import AccountLayout from "../../../components/Layouts/AccountLayout.vue";
export default {
  components: { AccountLayout },
  data() {
    return {
      message: "https://exchange.tradio.com/register?ref=0595b6ff8865ee37",
    };
  },
  methods: {
    doCopy: function() {
      this.$copyText(this.message).then(
        function(e) {
          alert("Copied");
          console.log(e);
        },
        function(e) {
          alert("Can not copy");
          console.log(e);
        }
      );
    },
  },
};
</script>
