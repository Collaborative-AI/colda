<template>
  <dashboard-layout :active="1" :container="true">
    <toster />
    <div class="row">
      <div class="col-xl-6 col-xxl-12 col-lg-12 col-xxl-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">BTC - USD Perpetual Swap</h4>
            <span
              >24h Change <strong class="text-success"> +5.30%</strong></span
            >
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">24h Volume</p>
                <h6>814,107.51 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Index Price</p>
                <h6>10,326.19 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Mark Price</p>
                <h6>10,343.94 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Last Price</p>
                <h6>10,383.51 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Funding Rate</p>
                <h6>0.1392%</h6>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-6 col-xxl-12 col-lg-12 col-xxl-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Your Wallet</h4>
            <span>Update <span>10</span> minutes ago</span>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Equity</p>
                <h6>34.00 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Available Margin</p>
                <h6>47.00 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Unrealized P&L</p>
                <h6>92.00 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Position Margin</p>
                <h6>58.00 USD</h6>
              </div>
              <div class="col-xl col-lg col-md col-sm-auto col-6">
                <p class="mb-0">Active Orders</p>
                <h6>15.00 USD</h6>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-xl-3 col-lg-6 col-md-12 col-xxl-6">
        <div class="card">
          <b-tabs
            class="tab-content tab-content-default"
            nav-wrapper-class="card-header"
            pills
          >
            <b-tab title="Limit">
              <perfect-scrollbar class="card-body">
                <form
                  @submit.prevent=""
                  method="post"
                  name="myform"
                  class="currency_limit"
                >
                  <div class="form-group">
                    <!-- <label class="me-sm-2">Currency</label> -->
                    <div class="input-group mb-3">
                      <select name="currency" class="form-control mw-150">
                        <option data-display="Bitcoin" value="bitcoin"
                          >Bitcoin
                        </option>
                        <option value="litecoin">Litecoin</option>
                      </select>
                      <input
                        type="text"
                        name="usd_amount"
                        class="form-control text-right"
                        placeholder="Enter Size"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">USD</span>
                      </div>
                      <input
                        type="text"
                        name="currency_amount"
                        class="form-control text-right"
                        placeholder="501458"
                      />
                    </div>
                  </div>

                  <perfect-scrollbar tag="ul" class="list-group limit-nested">
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Time In Force
                      <select name="currency" class="border-0 h-0">
                        <option data-display="Good 'Til Cancelled" value=""
                          >Good 'Til Cancelled</option
                        >
                        <option value="">Fill Or Kill</option>
                        <option value="">Immediate Or Cancel</option>
                      </select>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Post Only
                      <label class="toggle mb-0">
                        <input
                          class="toggle-checkbox"
                          type="checkbox"
                          checked
                        />
                        <span class="toggle-switch"></span>
                      </label>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Size in BTC
                      <strong class="strong"> 0.00254 BTC</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Order Value
                      <strong class="strong">65850 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Available Margin
                      <strong class="strong">15458 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Buy Cost @ 1.0x
                      <strong class="strong">0.00 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Sell Cost @ 1.0x
                      <strong class="strong">0.00 USD</strong>
                    </li>
                  </perfect-scrollbar>

                  <div class="btn-group btn-block mt-3">
                    <button type="submit" name="submit" class="btn btn-success">
                      Buy Now
                    </button>
                    <button type="submit" name="submit" class="btn btn-danger">
                      Sell Now
                    </button>
                  </div>
                </form>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Market">
              <perfect-scrollbar class="card-body">
                <form
                  @submit.prevent=""
                  method="post"
                  name="myform"
                  class="currency_limit"
                >
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">USD</span>
                      </div>
                      <input
                        type="text"
                        name="currency_amount"
                        class="form-control text-right"
                        placeholder="501458"
                      />
                    </div>
                  </div>

                  <perfect-scrollbar tag="ul" class="list-group market-nested">
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Size in BTC
                      <span class="strong"> 0.00254 BTC</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Order Value
                      <span class="strong">65850 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Available Margin
                      <span class="strong">15458 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Buy Cost @ 1.0x
                      <span class="strong">0.00 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Sell Cost @ 1.0x
                      <span class="strong">0.00 USD</span>
                    </li>
                  </perfect-scrollbar>

                  <div class="btn-group btn-block mt-3">
                    <button type="submit" name="submit" class="btn btn-success">
                      Buy Now
                    </button>
                    <button type="submit" name="submit" class="btn btn-danger">
                      Sell Now
                    </button>
                  </div>
                </form>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Stop Limit">
              <perfect-scrollbar class="card-body">
                <form
                  @submit.prevent=""
                  method="post"
                  name="myform"
                  class="currency_limit"
                >
                  <div class="form-group">
                    <!-- <label class="me-sm-2">Currency</label> -->
                    <div class="input-group mb-3">
                      <select name="currency" class="form-control mw-150">
                        <option data-display="Bitcoin" value="bitcoin"
                          >Bitcoin
                        </option>
                        <option value="litecoin">Litecoin</option>
                      </select>
                      <input
                        type="text"
                        name="usd_amount"
                        class="form-control text-right"
                        placeholder="Enter Size"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">USD</span>
                      </div>
                      <input
                        type="text"
                        name="currency_amount"
                        class="form-control text-right"
                        placeholder="501458"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">USD</span>
                      </div>
                      <input
                        type="text"
                        name="currency_amount"
                        class="form-control text-right"
                        placeholder="501458"
                      />
                    </div>
                  </div>

                  <perfect-scrollbar
                    tag="ul"
                    class="list-group stop-limit-nested"
                  >
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Stop Trigger
                      <select name="currency" class="border-0 h-0">
                        <option data-display="Mark Price" value=""
                          >Mark Price</option
                        >
                        <option value="">Last Price</option>
                      </select>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Time In Force
                      <select name="currency" class="border-0 h-0">
                        <option data-display="Good 'Til Cancelled" value=""
                          >Good 'Til Cancelled</option
                        >
                        <option value="">Fill Or Kill</option>
                        <option value="">Immediate Or Cancel</option>
                      </select>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Post Only
                      <label class="toggle mb-0">
                        <input
                          class="toggle-checkbox"
                          type="checkbox"
                          checked
                        />
                        <span class="toggle-switch"></span>
                      </label>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Size in BTC
                      <span class="strong"> 0.00254 BTC</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Order Value
                      <span class="strong">65850 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Available Margin
                      <span class="strong">15458 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Buy Cost @ 1.0x
                      <span class="strong">0.00 USD</span>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Sell Cost @ 1.0x
                      <span class="strong">0.00 USD</span>
                    </li>
                  </perfect-scrollbar>

                  <div class="btn-group btn-block mt-3">
                    <button type="submit" name="submit" class="btn btn-success">
                      Buy Now
                    </button>
                    <button type="submit" name="submit" class="btn btn-danger">
                      Sell Now
                    </button>
                  </div>
                </form>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Stop Market">
              <perfect-scrollbar class="card-body">
                <form
                  method="post"
                  @submit.prevent=""
                  name="myform"
                  class="currency_limit"
                >
                  <div class="form-group">
                    <!-- <label class="me-sm-2">Currency</label> -->
                    <div class="input-group mb-3">
                      <select name="currency" class="form-control mw-150">
                        <option data-display="Bitcoin" value="bitcoin"
                          >Bitcoin
                        </option>
                        <option value="litecoin">Litecoin</option>
                      </select>
                      <input
                        type="text"
                        name="usd_amount"
                        class="form-control text-right"
                        placeholder="Enter Size"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">USD</span>
                      </div>
                      <input
                        type="text"
                        name="currency_amount"
                        class="form-control text-right"
                        placeholder="501458"
                      />
                    </div>
                  </div>

                  <perfect-scrollbar tag="ul" class="list-group limit-nested">
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Time In Force
                      <select name="currency" class="border-0 h-0">
                        <option data-display="Good 'Til Cancelled" value=""
                          >Good 'Til Cancelled</option
                        >
                        <option value="">Fill Or Kill</option>
                        <option value="">Immediate Or Cancel</option>
                      </select>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Post Only
                      <label class="toggle mb-0">
                        <input
                          class="toggle-checkbox"
                          type="checkbox"
                          checked
                        />
                        <span class="toggle-switch"></span>
                      </label>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Size in BTC
                      <strong class="strong"> 0.00254 BTC</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Order Value
                      <strong class="strong">65850 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Available Margin
                      <strong class="strong">15458 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Buy Cost @ 1.0x
                      <strong class="strong">0.00 USD</strong>
                    </li>
                    <li
                      class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
                    >
                      Sell Cost @ 1.0x
                      <strong class="strong">0.00 USD</strong>
                    </li>
                  </perfect-scrollbar>

                  <div class="btn-group btn-block mt-3">
                    <button type="submit" name="submit" class="btn btn-success">
                      Buy Now
                    </button>
                    <button type="submit" name="submit" class="btn btn-danger">
                      Sell Now
                    </button>
                  </div>
                </form>
              </perfect-scrollbar>
            </b-tab>
          </b-tabs>
        </div>
      </div>

      <div class="col-xl-5 col-lg-6 col-md-12 col-xxl-6">
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container card">
          <!-- <div id="tradingview_e8053"></div> -->
          <tranding-vue />
        </div>
        <!-- TradingView Widget END -->
      </div>

      <div class="col-xl-2 col-lg-4 col-md-6 col-xxl-4">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Order Book</h4>
          </div>
          <perfect-scrollbar class="card-body order-book">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Price (USD)</th>
                  <th scope="col">Price (BTC)</th>
                  <th scope="col">Total</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-danger">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-danger">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-danger">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-danger">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-danger">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
              </tbody>
            </table>

            <div class="order-book-divider">
              <h6 class="text-danger">
                <i class="la la-arrow-down"></i> 6587.35
              </h6>
              <span>6520.220 / 4835.00</span>
            </div>

            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Price (USD)</th>
                  <th scope="col">Price (BTC)</th>
                  <th scope="col">Total</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-success">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-success">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-success">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-success">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
                <tr>
                  <td class="text-success">10393.50</td>
                  <td>0.010</td>
                  <td>14.109</td>
                </tr>
              </tbody>
            </table>
          </perfect-scrollbar>
        </div>
      </div>

      <div class="col-xl-2 col-lg-4 col-md-6 col-xxl-4">
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-header">
                <h4 class="card-title">Trade History</h4>
              </div>
              <perfect-scrollbar class="card-body trade-history">
                <div class="table-responsive">
                  <table class="table table-borderless">
                    <thead>
                      <tr>
                        <th scope="col">Price</th>
                        <th scope="col">Size</th>
                        <th scope="col">Time</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                      <tr>
                        <td class="text-danger">10393.50</td>
                        <td>0.010</td>
                        <td>14.109</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </perfect-scrollbar>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-3 col-lg-4 col-md-12 col-xxl-4">
        <div class="card">
          <b-tabs
            class="tab-content tab-content-default"
            nav-wrapper-class="card-header"
            pills
          >
            <b-tab>
              <template slot="title">
                <i class="mdi mdi-star"></i>
              </template>
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/BTC</td>
                      <td>0.00020255</td>
                      <td class="red">-2.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/BTC</td>
                      <td>0.00013192</td>
                      <td class="green">+5.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/BTC</td>
                      <td>0.00002996</td>
                      <td class="red">-1.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/BTC</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/BTC</td>
                      <td>0.00020255</td>
                      <td class="red">-2.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/BTC</td>
                      <td>0.00013192</td>
                      <td class="green">+5.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/BTC</td>
                      <td>0.00002996</td>
                      <td class="red">-1.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/BTC</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/BTC</td>
                      <td>0.00002996</td>
                      <td class="red">-1.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/BTC</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="BTC">
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/BTC</td>
                      <td>0.00020255</td>
                      <td class="red">-2.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/BTC</td>
                      <td>0.00013192</td>
                      <td class="green">+5.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/BTC</td>
                      <td>0.00002996</td>
                      <td class="red">-1.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/BTC</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> EOS/BTC</td>
                      <td>0.00000103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTT/BTC</td>
                      <td>0.00002303</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> LTC/BTC</td>
                      <td>0.03520103</td>
                      <td class="green">+1.5%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRX/BTC</td>
                      <td>0.00330103</td>
                      <td class="red">-3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BSV/BTC</td>
                      <td>0.00300103</td>
                      <td class="green">+2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> COTI/BTC</td>
                      <td>0.003500103</td>
                      <td class="green">+2.85%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XYT/BTC</td>
                      <td>0.00003103</td>
                      <td class="green">+3.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BNB/BTC</td>
                      <td>0.003500103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XMR/BTC</td>
                      <td>0.003500103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRY/BTC</td>
                      <td>0.00000123</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ADA/BTC</td>
                      <td>0.00050103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> NEO/BTC</td>
                      <td>0.00340103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XLM/BTC</td>
                      <td>0.00035103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ENQ/BTC</td>
                      <td>0.00354103</td>
                      <td class="green">+2.02%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AVA/BTC</td>
                      <td>0.02535103</td>
                      <td class="green">+3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AMB/BTC</td>
                      <td>0.05335103</td>
                      <td class="green">+1.0%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> MAP/BTC</td>
                      <td>0.00234103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GO/BTC</td>
                      <td>0.00354103</td>
                      <td class="red">-6.50%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KICK/BTC</td>
                      <td>0.02053103</td>
                      <td class="red">-6.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> DBC/BTC</td>
                      <td>0.02535103</td>
                      <td class="green">+7.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GGC/BTC</td>
                      <td>0.00353103</td>
                      <td class="red">-4.05%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="ETH">
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTC/ETH</td>
                      <td>0.00020255</td>
                      <td class="green">+1.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/ETH</td>
                      <td>0.00013192</td>
                      <td class="red">-0.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/ETH</td>
                      <td>0.00002996</td>
                      <td class="red">-0.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/ETH</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> EOS/ETH</td>
                      <td>0.00000103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTT/ETH</td>
                      <td>0.00002303</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> LTC/ETH</td>
                      <td>0.03520103</td>
                      <td class="green">+1.5%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRX/ETH</td>
                      <td>0.00330103</td>
                      <td class="red">-3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BSV/ETH</td>
                      <td>0.00300103</td>
                      <td class="green">+2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> COTI/ETH</td>
                      <td>0.003500103</td>
                      <td class="green">+2.85%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XYT/ETH</td>
                      <td>0.00003103</td>
                      <td class="green">+3.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BNB/ETH</td>
                      <td>0.003500103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XMR/ETH</td>
                      <td>0.003500103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRY/ETH</td>
                      <td>0.00000123</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ADA/ETH</td>
                      <td>0.00050103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> NEO/ETH</td>
                      <td>0.00340103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XLM/ETH</td>
                      <td>0.00035103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ENQ/ETH</td>
                      <td>0.00354103</td>
                      <td class="green">+2.02%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AVA/ETH</td>
                      <td>0.02535103</td>
                      <td class="green">+3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AMB/ETH</td>
                      <td>0.05335103</td>
                      <td class="green">+1.0%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> MAP/ETH</td>
                      <td>0.00234103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GO/ETH</td>
                      <td>0.00354103</td>
                      <td class="red">-6.50%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KICK/ETH</td>
                      <td>0.02053103</td>
                      <td class="red">-6.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> DBC/ETH</td>
                      <td>0.02535103</td>
                      <td class="green">+7.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GGC/ETH</td>
                      <td>0.00353103</td>
                      <td class="red">-4.05%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="NEO">
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/NEO</td>
                      <td>0.00350255</td>
                      <td class="red">-6.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/NEO</td>
                      <td>0.00013192</td>
                      <td class="green">+0.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/NEO</td>
                      <td>0.00002996</td>
                      <td class="red">-0.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/NEO</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> EOS/NEO</td>
                      <td>0.00000103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTT/NEO</td>
                      <td>0.00002303</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> LTC/NEO</td>
                      <td>0.03520103</td>
                      <td class="green">+1.5%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRX/NEO</td>
                      <td>0.00330103</td>
                      <td class="red">-3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BSV/NEO</td>
                      <td>0.00300103</td>
                      <td class="green">+2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> COTI/NEO</td>
                      <td>0.003500103</td>
                      <td class="green">+2.85%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XYT/NEO</td>
                      <td>0.00003103</td>
                      <td class="green">+3.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BNB/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XMR/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRY/NEO</td>
                      <td>0.00000123</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ADA/NEO</td>
                      <td>0.00050103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> NEO/NEO</td>
                      <td>0.00340103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XLM/NEO</td>
                      <td>0.00035103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ENQ/NEO</td>
                      <td>0.00354103</td>
                      <td class="green">+2.02%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AVA/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AMB/NEO</td>
                      <td>0.05335103</td>
                      <td class="green">+1.0%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> MAP/NEO</td>
                      <td>0.00234103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GO/NEO</td>
                      <td>0.00354103</td>
                      <td class="red">-6.50%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KICK/NEO</td>
                      <td>0.02053103</td>
                      <td class="red">-6.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> DBC/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+7.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GGC/NEO</td>
                      <td>0.00353103</td>
                      <td class="red">-4.05%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="USDT">
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/NEO</td>
                      <td>0.00350255</td>
                      <td class="red">-6.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/NEO</td>
                      <td>0.00013192</td>
                      <td class="green">+0.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/NEO</td>
                      <td>0.00002996</td>
                      <td class="red">-0.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/NEO</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> EOS/NEO</td>
                      <td>0.00000103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTT/NEO</td>
                      <td>0.00002303</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> LTC/NEO</td>
                      <td>0.03520103</td>
                      <td class="green">+1.5%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRX/NEO</td>
                      <td>0.00330103</td>
                      <td class="red">-3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BSV/NEO</td>
                      <td>0.00300103</td>
                      <td class="green">+2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> COTI/NEO</td>
                      <td>0.003500103</td>
                      <td class="green">+2.85%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XYT/NEO</td>
                      <td>0.00003103</td>
                      <td class="green">+3.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BNB/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XMR/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRY/NEO</td>
                      <td>0.00000123</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ADA/NEO</td>
                      <td>0.00050103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> NEO/NEO</td>
                      <td>0.00340103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XLM/NEO</td>
                      <td>0.00035103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ENQ/NEO</td>
                      <td>0.00354103</td>
                      <td class="green">+2.02%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AVA/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AMB/NEO</td>
                      <td>0.05335103</td>
                      <td class="green">+1.0%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> MAP/NEO</td>
                      <td>0.00234103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GO/NEO</td>
                      <td>0.00354103</td>
                      <td class="red">-6.50%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KICK/NEO</td>
                      <td>0.02053103</td>
                      <td class="red">-6.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> DBC/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+7.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GGC/NEO</td>
                      <td>0.00353103</td>
                      <td class="red">-4.05%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="DAI">
              <perfect-scrollbar class="card-body price-pair">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Pairs</th>
                      <th>Last Price</th>
                      <th>Change</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ETH/NEO</td>
                      <td>0.00350255</td>
                      <td class="red">-6.58%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KCS/NEO</td>
                      <td>0.00013192</td>
                      <td class="green">+0.6%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XRP/NEO</td>
                      <td>0.00002996</td>
                      <td class="red">-0.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> VET/NEO</td>
                      <td>0.00000103</td>
                      <td class="green">+1.8%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> EOS/NEO</td>
                      <td>0.00000103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BTT/NEO</td>
                      <td>0.00002303</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> LTC/NEO</td>
                      <td>0.03520103</td>
                      <td class="green">+1.5%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRX/NEO</td>
                      <td>0.00330103</td>
                      <td class="red">-3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BSV/NEO</td>
                      <td>0.00300103</td>
                      <td class="green">+2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> COTI/NEO</td>
                      <td>0.003500103</td>
                      <td class="green">+2.85%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XYT/NEO</td>
                      <td>0.00003103</td>
                      <td class="green">+3.55%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> BNB/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XMR/NEO</td>
                      <td>0.003500103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> TRY/NEO</td>
                      <td>0.00000123</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ADA/NEO</td>
                      <td>0.00050103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> NEO/NEO</td>
                      <td>0.00340103</td>
                      <td class="red">-1.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> XLM/NEO</td>
                      <td>0.00035103</td>
                      <td class="green">+5.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> ENQ/NEO</td>
                      <td>0.00354103</td>
                      <td class="green">+2.02%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AVA/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+3.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> AMB/NEO</td>
                      <td>0.05335103</td>
                      <td class="green">+1.0%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> MAP/NEO</td>
                      <td>0.00234103</td>
                      <td class="red">-2.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GO/NEO</td>
                      <td>0.00354103</td>
                      <td class="red">-6.50%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> KICK/NEO</td>
                      <td>0.02053103</td>
                      <td class="red">-6.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> DBC/NEO</td>
                      <td>0.02535103</td>
                      <td class="green">+7.05%</td>
                    </tr>
                    <tr>
                      <td><i class="mdi mdi-star"></i> GGC/NEO</td>
                      <td>0.00353103</td>
                      <td class="red">-4.05%</td>
                    </tr>
                  </tbody>
                </table>
              </perfect-scrollbar>
            </b-tab>
          </b-tabs>
        </div>
      </div>

      <div class="col-xl-5 col-lg-8 col-md-12 col-xxl-8">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Depth Chart</h4>
          </div>
          <div class="card-body">
            <!-- <div id="chartdiv"></div> -->

            <!-- <div id="chartdiv" ref="chartdiv"></div> -->
            <!-- <AmChartDark v-else /> -->
            <am-chart :dark="dark" />
          </div>
        </div>
      </div>

      <div class="col-xl-2 col-lg-4 col-xxl-4">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Your Portfolio</h4>
          </div>
          <perfect-scrollbar class="card-body balance-widget">
            <div class="total-balance">
              <h3>$ 63411.00</h3>
              <h6>Total Balance</h6>
            </div>

            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th>Type</th>
                    <th>Size</th>
                    <th>USD</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>BTC</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>LTC</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>XRP</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>ETH</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>XTZ</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>EOS</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>Dash</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                  <tr>
                    <td>USDT</td>
                    <td>0.000242</td>
                    <td>0.125 USD</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </perfect-scrollbar>
        </div>
      </div>

      <div class="col-xl-2 col-lg-6 col-md-6 col-xxl-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Market News</h4>
          </div>
          <perfect-scrollbar class="card-body market-news">
            <div class="row">
              <div class="col-xl-12">
                <img
                  class="img-fluid"
                  src="../../assets/images/blog/1.jpg"
                  alt="..."
                  height="100"
                />
                <a href="#" class="news-content">
                  <h6 class="mt-2 mb-3">
                    The Cryptocurrency Act of 2020 Is ‘Dead on Arrival,’
                    Washington Tells Sponsors
                  </h6>
                </a>
              </div>
              <div class="col-xl-12">
                <img
                  class="img-fluid"
                  src="../../assets/images/blog/2.jpg"
                  alt="..."
                />
                <a href="#" class="news-content">
                  <h6 class="mt-2 mb-3">
                    UK Trade Negotiators Eye Blockchain Provisions in Coming US
                    Trade Talks
                  </h6>
                </a>
              </div>
              <div class="col-xl-12">
                <img
                  class="img-fluid"
                  src="../../assets/images/blog/3.jpg"
                  alt="..."
                />
                <a href="#" class="news-content">
                  <h6 class="mt-2 mb-3">
                    Bitcoin Options Saw Record Volume of $198M Amid Recent Price
                    Drop
                  </h6>
                </a>
              </div>
              <div class="col-xl-12">
                <img
                  class="img-fluid"
                  src="../../assets/images/blog/4.jpg"
                  alt="..."
                />
                <a href="#" class="news-content">
                  <h6 class="mt-2 mb-3">
                    Blockforce Capital’s Crypto Fund Captures 86% of Bitcoin’s
                    Upside in 2020
                  </h6>
                </a>
              </div>
            </div>
          </perfect-scrollbar>
        </div>
      </div>

      <div class="col-xl-2 col-lg-6 col-md-6 col-xxl-6">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">Your Position</h4>
          </div>
          <div class="card-body your-position">
            <div class="slider-container">
              <input
                id="slider"
                type="range"
                min="0"
                max="100"
                value="0"
                v-model="sliderValue"
                @change="onChange"
              />
              <div
                class="count"
                :style="
                  `left: ${sliderValue}%; transform: translateX(-${sliderValue}%);`
                "
              >
                {{ sliderValue }}
              </div>
              <div class="fill" :style="`width:${sliderValue}%`"></div>
            </div>

            <button class="btn btn-primary btn-block mb-2 text-white">
              Edit Leverage
            </button>
            <ul class="list-group">
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Position Leverage
                <span class="strong"> 1.0x</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Size in BTC
                <span class="strong"> 0.00254 BTC</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Contracts
                <span class="strong"> 283</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Liquidation Price
                <span class="strong">65850 USD</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Unrealized P&L
                <span class="strong">15458 USD</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Unrealized ROE
                <span class="strong">0.00 USD</span>
              </li>
              <li
                class="list-group-item border-0 px-0 py-1 d-flex justify-content-between align-items-center"
              >
                Sell Cost @ 1.0x
                <span class="strong">0.00 USD</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="col-xl-10 col-lg-12 col-xxl-12">
        <div class="card">
          <b-tabs
            class="tab-content tab-content-default"
            nav-wrapper-class="card-header"
            pills
          >
            <b-tab title="Open Position">
              <perfect-scrollbar class="card-body">
                <div class="table-responsive home-table">
                  <table class="table table-striped" id="tbUser">
                    <thead>
                      <tr>
                        <th scope="col">Symbol</th>
                        <th scope="col">Size</th>
                        <th scope="col">Entry Value</th>
                        <th scope="col">Entry Price</th>
                        <th scope="col">Liq. Price</th>
                        <th scope="col">Margin</th>
                        <th scope="col">Eff. Lvg.</th>
                        <th scope="col">Unrealized P&L (ROE %)</th>
                        <th scope="col">Realized P&L</th>
                        <th scope="col">Close</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5698.25</td>
                        <td>0.3658745698 BTC</td>
                        <td>0.32658745566</td>
                        <td>0.95874585254 BTC</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td>0.24566</td>
                        <td><i class="la la-close btnDelete"></i></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Active Orders">
              <perfect-scrollbar class="card-body">
                <div class="table-responsive home-table">
                  <table class="table table-striped">
                    <thead>
                      <tr>
                        <th scope="col">Symbol</th>
                        <th scope="col">Type</th>
                        <th scope="col">Size</th>
                        <th scope="col">Filled</th>
                        <th scope="col">Remaining</th>
                        <th scope="col">Limit Price</th>
                        <th scope="col">Fill Price</th>
                        <th scope="col">Rem. Value</th>
                        <th scope="col">Stop Price</th>
                        <th scope="col">Status</th>
                        <th scope="col">Time</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Fills">
              <perfect-scrollbar class="card-body">
                <div class="table-responsive home-table">
                  <table class="table table-striped">
                    <thead>
                      <tr>
                        <th scope="col">Symbol</th>
                        <th scope="col">Size</th>
                        <th scope="col">Entry Price</th>
                        <th scope="col">Entry Value</th>
                        <th scope="col">Time</th>
                        <th scope="col">OrderID</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>5623.58</td>
                        <td>5623.58</td>
                        <td>0.24566 BTC</td>
                        <td>07:25:35</td>
                        <td>#2658455</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </perfect-scrollbar>
            </b-tab>
            <b-tab title="Liguidition">
              <perfect-scrollbar class="card-body">
                <div class="table-responsive home-table">
                  <table class="table table-striped">
                    <thead>
                      <tr>
                        <th scope="col">Symbol</th>
                        <th scope="col">Size</th>
                        <th scope="col">Value</th>
                        <th scope="col">Entry Price</th>
                        <th scope="col">Mark Price</th>
                        <th scope="col">Margim</th>
                        <th scope="col">Leverage</th>
                        <th scope="col">Time</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                      <tr>
                        <th scope="row"><i class="cc BTC"></i></th>
                        <td>BTC - USD</td>
                        <td>5623.58</td>
                        <td>-</td>
                        <td>0.95874</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566 BTC</td>
                        <td>0.24566</td>
                        <td>0.02543</td>
                        <td>Complete</td>
                        <td>14:41:36</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </perfect-scrollbar>
            </b-tab>
          </b-tabs>
        </div>
      </div>
    </div>
  </dashboard-layout>
</template>

<script>
import DashboardLayout from "../../components/Layouts/DashboardLayout.vue";
import { PerfectScrollbar } from "vue2-perfect-scrollbar";
// import AmChart from "../../components/Tradio/Charts/AmChart.vue";
import TrandingVue from "../../components/Tradio/Charts/TrandingVue.vue";
import Toster from "../../components/Tradio/Toster.vue";
import AmChart from "../../components/Tradio/Charts/AmChart.vue";
export default {
  components: {
    DashboardLayout,
    PerfectScrollbar,
    // AmChart,
    TrandingVue,
    Toster,
    AmChart,
    // AmChartDark,
  },
  data() {
    return {
      sliderValue: 0,
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    onChange(e) {
      // console.log(e.target.value);
      this.sliderValue = e.target.value;
    },
  },
};
</script>
