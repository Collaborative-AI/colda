<template>
  <account-layout :active="1">
    <div class="col-xl-6 col-lg-6 col-md-6">
      <div class="card profile_card">
        <div class="card-body">
          <div class="media">
            <img
              class="me-3 rounded-circle me-0 me-sm-3"
              src="../../../assets/images/profile/2.png"
              width="60"
              height="60"
              alt=""
            />
            <div class="media-body">
              <span>Hello</span>
              <h4 class="mb-2">Sabuj Hasan Sarker</h4>
              <p class="mb-1">
                <span><i class="fa fa-phone me-2 text-primary"></i></span> +1
                235 5547
              </p>
              <p class="mb-1">
                <span><i class="fa fa-envelope me-2 text-primary"></i></span>
                hello@example.com
              </p>
            </div>
          </div>

          <ul class="card-profile__info">
            <li>
              <h5 class="me-4">Address</h5>
              <span class="text-muted">House 14, Road 9, Gulshan, Dhaka</span>
            </li>
            <li class="mb-1">
              <h5 class="me-4">Total Log</h5>
              <span>103 Time (Today 5 Times)</span>
            </li>
            <li>
              <h5 class="text-danger me-4">Last Log</h5>
              <span class="text-danger">3 February, 2020, 10:00 PM</span>
            </li>
          </ul>
          <div class="social-icons">
            <a class="facebook text-center" href="javascript:void(0)"
              ><span><i class="fa fa-facebook"></i></span
            ></a>
            <a class="twitter text-center" href="javascript:void(0)"
              ><span><i class="fa fa-twitter"></i></span
            ></a>
            <a class="youtube text-center" href="javascript:void(0)"
              ><span><i class="fa fa-youtube"></i></span
            ></a>
            <a class="googlePlus text-center" href="javascript:void(0)"
              ><span><i class="fa fa-google"></i></span
            ></a>
          </div>
        </div>
      </div>
    </div>

    <div class="col-xl-6 col-lg-6 col-md-6">
      <div class="card acc_balance">
        <div class="card-header">
          <h4 class="card-title">Wallet</h4>
        </div>
        <div class="card-body">
          <span>Available BTC</span>
          <h3>0.0230145 BTC</h3>

          <div class="d-flex justify-content-between my-3">
            <div>
              <p class="mb-1">Total Equity</p>
              <h4>78950.35 USD</h4>
            </div>
            <div>
              <p class="mb-1">Available Margin</p>
              <h4>56845.25 USD</h4>
            </div>
          </div>

          <div class="d-flex justify-content-between my-3">
            <div>
              <p class="mb-1">Buy this month</p>
              <h4>3.0215485 BTC</h4>
            </div>
            <div>
              <p class="mb-1">Sell this month</p>
              <h4>3.0215485 BTC</h4>
            </div>
          </div>

          <div class="btn-group mb-3">
            <button class="btn btn-success">Buy</button>
            <button class="btn btn-danger">Sell</button>
          </div>
        </div>
      </div>
    </div>

    <div class="col-xl-12">
      <div class="row">
        <div class="col-xl-3 col-lg-3 col-md-3 col-sm-6">
          <div class="card text-center pt-2">
            <div class="card-body">
              <p class="mb-1">Maintainance</p>
              <h4>0.03654 BTC</h4>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-3 col-md-3 col-sm-6">
          <div class="card text-center pt-2">
            <div class="card-body">
              <p class="mb-1">Unrealized P&L</p>
              <h4>0.03654 BTC</h4>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-3 col-md-3 col-sm-6">
          <div class="card text-center pt-2">
            <div class="card-body">
              <p class="mb-1">Open Positions</p>
              <h4>0.03654 BTC</h4>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-3 col-md-3 col-sm-6">
          <div class="card text-center pt-2">
            <div class="card-body">
              <p class="mb-1">Active Orders</p>
              <h4>0.03654 BTC</h4>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Transactions History</h4>
        </div>
        <div class="card-body">
          <div class="transaction-table">
            <div class="table-responsive">
              <table class="table table-striped mb-0 table-responsive-sm">
                <thead>
                  <tr>
                    <th>Transaction ID</th>
                    <th>Time</th>
                    <th>Type</th>
                    <th>Amount</th>
                    <th>Status</th>
                    <th>Balance</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>#565845522</td>
                    <td>January 10, 2020</td>
                    <td>Realized P&L</td>
                    <td>0.254782 BTC</td>
                    <td>Completed</td>
                    <td>0.125476 BTC</td>
                  </tr>
                  <tr>
                    <td>#565845522</td>
                    <td>January 10, 2020</td>
                    <td>Realized P&L</td>
                    <td>0.254782 BTC</td>
                    <td>Completed</td>
                    <td>0.125476 BTC</td>
                  </tr>
                  <tr>
                    <td>#565845522</td>
                    <td>January 10, 2020</td>
                    <td>Realized P&L</td>
                    <td>0.254782 BTC</td>
                    <td>Completed</td>
                    <td>0.125476 BTC</td>
                  </tr>
                  <tr>
                    <td>#565845522</td>
                    <td>January 10, 2020</td>
                    <td>Realized P&L</td>
                    <td>0.254782 BTC</td>
                    <td>Completed</td>
                    <td>0.125476 BTC</td>
                  </tr>
                  <tr>
                    <td>#565845522</td>
                    <td>January 10, 2020</td>
                    <td>Realized P&L</td>
                    <td>0.254782 BTC</td>
                    <td>Completed</td>
                    <td>0.125476 BTC</td>
                  </tr>
                </tbody>
              </table>
            </div>
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
};
</script>
