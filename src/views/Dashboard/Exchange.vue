<template>
  <dashboard-layout :title="true" :active="2">
    <div class="row">
      <div class="col-xl-6 col-lg-6 col-md-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Buy</h4>
          </div>
          <div class="card-body">
            <div class="buy-sell-widget">
              <currency-form-2 :className="'success'" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-6 col-lg-6 col-md-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Sell</h4>
          </div>
          <div class="card-body">
            <div class="buy-sell-widget">
              <currency-form-2 :className="'danger'" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-9 col-lg-9 col-md-12">
        <div class="card">
          <div class="card-body">
            <div class="buyer-seller">
              <div class="d-flex justify-content-between mb-3">
                <div class="buyer-info">
                  <div class="media">
                    <img
                      class="me-3 rounded"
                      src="../../assets/images/avatar/2.jpg"
                      alt=""
                    />
                    <div class="media-body">
                      <h4>Buyer</h4>
                      <h5 class="text-body">Michael John</h5>
                      <a href="#" class="text-body">hello@example.com</a>
                    </div>
                  </div>
                </div>
                <div class="seller-info text-right">
                  <div class="media">
                    <div class="media-body">
                      <h4>Seller</h4>
                      <h5 class="text-body">John Doe</h5>
                      <a href="#" class="text-body">hello@example.com</a>
                    </div>
                    <img
                      class="ms-3 rounded"
                      src="../../assets/images/avatar/5.jpg"
                      alt=""
                    />
                  </div>
                </div>
              </div>
              <div class="table-responsive">
                <table class="table table-striped">
                  <tbody>
                    <tr>
                      <td><span class="text-primary">You are selling</span></td>
                      <td><span class="text-primary">0.00254 BTC</span></td>
                    </tr>
                    <tr>
                      <td>Payment Method</td>
                      <td>Bank of America Bank ***********5245</td>
                    </tr>
                    <tr>
                      <td>Exchange Rate</td>
                      <td>0.00212455 BTC</td>
                    </tr>
                    <tr>
                      <td>Fee</td>
                      <td>$28.00 USD</td>
                    </tr>
                    <tr>
                      <td>Total</td>
                      <td>$854.00 USD</td>
                    </tr>
                    <tr>
                      <td>Vat</td>
                      <td>
                        <div class="text-danger">$25.00 USD</div>
                      </td>
                    </tr>
                    <tr>
                      <td>Sub Total</td>
                      <td>$1232.00 USD</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-3 col-lg-3">
        <div class="apps-download">
          <div class="apps-download-content">
            <h4>
              Get the best mobile app to exchange or buy crypto on the go:
            </h4>
            <div class="mt-4 text-center">
              <a href="#" class="btn btn-primary m-2"
                ><img src="../../assets/images/android.svg" alt=""
              /></a>
              <a href="#" class="btn btn-success m-2"
                ><img src="../../assets/images/apple.svg" alt=""
              /></a>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-12">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">All Activities</h4>
          </div>
          <div class="card-body">
            <div class="transaction-table">
              <div class="table-responsive">
                <table class="table table-striped mb-0 table-responsive-sm">
                  <tbody>
                    <tr>
                      <td>
                        <span class="sold-thumb"
                          ><i class="mdi mdi-arrow-down"></i
                        ></span>
                      </td>

                      <td>
                        <span class="badge bg-danger p-2">Sold</span>
                      </td>
                      <td><i class="cc BTC"></i> BTC</td>
                      <td>
                        Using - Bank *******5264
                      </td>
                      <td class="text-danger">-0.000242 BTC</td>
                      <td>-0.125 USD</td>
                    </tr>
                    <tr>
                      <td>
                        <span class="buy-thumb"
                          ><i class="mdi mdi-arrow-up"></i
                        ></span>
                      </td>
                      <td>
                        <span class="badge bg-success p-2">Buy</span>
                      </td>
                      <td><i class="cc LTC"></i> LTC</td>
                      <td>
                        Using - Card *******8475
                      </td>
                      <td class="text-success">-0.000242 BTC</td>
                      <td>-0.125 USD</td>
                    </tr>
                    <tr>
                      <td>
                        <span class="sold-thumb"
                          ><i class="mdi mdi-arrow-down"></i
                        ></span>
                      </td>
                      <td>
                        <span class="badge bg-danger p-2">Sold</span>
                      </td>
                      <td><i class="cc XRP"></i> XRP</td>
                      <td>
                        Using - Card *******8475
                      </td>
                      <td class="text-danger">-0.000242 BTC</td>
                      <td>-0.125 USD</td>
                    </tr>
                    <tr>
                      <td>
                        <span class="buy-thumb"
                          ><i class="mdi mdi-arrow-up"></i
                        ></span>
                      </td>
                      <td>
                        <span class="badge bg-success p-2">Buy</span>
                      </td>
                      <td><i class="cc DASH"></i> DASH</td>
                      <td>
                        Using - Card *******2321
                      </td>
                      <td class="text-success">-0.000242 BTC</td>
                      <td>-0.125 USD</td>
                    </tr>
                    <tr>
                      <td>
                        <span class="sold-thumb"
                          ><i class="mdi mdi-arrow-down"></i
                        ></span>
                      </td>
                      <td>
                        <span class="badge bg-danger p-2">Sold</span>
                      </td>
                      <td><i class="cc BTC"></i> BTC</td>
                      <td>
                        Using - Card *******2321
                      </td>
                      <td class="text-danger">-0.000242 BTC</td>
                      <td>-0.125 USD</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-6 col-lg-6 col-md-12">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">FAQ</h4>
          </div>
          <div class="card-body">
            <div id="accordion-faq" class="accordion">
              <div class="card">
                <b-card-header header-bg-variant="" v-b-toggle="'collapseOne1'">
                  <h5 class="mb-0 collapsed c-pointer">
                    <i class="fa" aria-hidden="true"></i>What Shipping Methods
                    are Available?
                  </h5>
                </b-card-header>
                <b-collapse id="collapseOne1">
                  <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life
                    accusamus terry richardson ad squid. 3 wolf moon officia
                    aute, non cupidatat skateboard dolor brunch. Food truck
                    quinoa nesciunt laborum eiusmod.
                  </div>
                </b-collapse>
              </div>
              <div class="card">
                <b-card-header header-bg-variant="" v-b-toggle="'collapse2'">
                  <h5 class="mb-0 collapsed c-pointer">
                    <i class="fa" aria-hidden="true"></i>How Long Will it Take
                    To Get My Package?
                  </h5>
                </b-card-header>
                <b-collapse id="collapse2">
                  <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life
                    accusamus terry richardson ad squid. 3 wolf moon officia
                    aute, non cupidatat skateboard dolor brunch. Food truck
                    quinoa nesciunt laborum eiusmod.
                  </div>
                </b-collapse>
              </div>
              <div class="card">
                <b-card-header header-bg-variant="" v-b-toggle="'collapse3'">
                  <h5 class="mb-0 collapsed c-pointer">
                    <i class="fa" aria-hidden="true"></i>How Do I Track My
                    Order?
                  </h5>
                </b-card-header>
                <b-collapse id="collapse3">
                  <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life
                    accusamus terry richardson ad squid. 3 wolf moon officia
                    aute, non cupidatat skateboard dolor brunch. Food truck
                    quinoa nesciunt laborum eiusmod.
                  </div>
                </b-collapse>
              </div>
              <div class="card">
                <b-card-header header-bg-variant="" v-b-toggle="'collapse4'">
                  <h5 class="mb-0 collapsed c-pointer">
                    <i class="fa" aria-hidden="true"></i>Do I Need A Account To
                    Place Order?
                  </h5>
                </b-card-header>
                <b-collapse id="collapse4">
                  <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life
                    accusamus terry richardson ad squid. 3 wolf moon officia
                    aute, non cupidatat skateboard dolor brunch. Food truck
                    quinoa nesciunt laborum eiusmod.
                  </div>
                </b-collapse>
              </div>
              <div class="card">
                <b-card-header header-bg-variant="" v-b-toggle="'collapse5'">
                  <h5 class="mb-0 collapsed c-pointer">
                    <i class="fa" aria-hidden="true"></i>How do I Place an
                    Order?
                  </h5>
                </b-card-header>
                <b-collapse id="collapse5">
                  <div class="card-body">
                    Anim pariatur cliche reprehenderit, enim eiusmod high life
                    accusamus terry richardson ad squid. 3 wolf moon officia
                    aute, non cupidatat skateboard dolor brunch. Food truck
                    quinoa nesciunt laborum eiusmod.
                  </div>
                </b-collapse>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-6 col-lg-6 col-md-12">
        <div class="intro-video-play">
          <div class="play-btn">
            <a class="popup-youtube c-pointer" @click="showVideo = true">
              <span><i class="fa fa-play"></i></span
            ></a>
          </div>
        </div>
      </div>
    </div>
    <videos v-show="showVideo" :closeFuntion="closeFuntion" />
  </dashboard-layout>
</template>

<script>
import DashboardLayout from "../../components/Layouts/DashboardLayout.vue";
import CurrencyForm2 from "../../components/Tradio/From/CurrencyForm2.vue";
import Videos from "../../components/Tradio/Videos.vue";
export default {
  components: { DashboardLayout, CurrencyForm2, Videos },
  data() {
    return {
      showVideo: false,
    };
  },
  methods: {
    closeFuntion() {
      this.showVideo = false;
    },
  },
};
</script>
