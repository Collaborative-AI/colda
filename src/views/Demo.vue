<template>
  <div id="main-wrapper" class="show">
    <div class="header">
      <div class="container">
        <div class="row">
          <div class="col-xl-12">
            <div class="navigation">
              <nav class="navbar navbar-expand-lg navbar-light px-0">
                <a class="navbar-brand" href="demo"
                  ><img src="../assets/images/logo1.png" alt="" />
                </a>
                <b-navbar-toggle target="navbarSupportedContent">
                </b-navbar-toggle>

                <b-collapse is-nav id="navbarSupportedContent">
                  <b-navbar-nav tag="ul" class="navbar-nav">
                    <li class="nav-item">
                      <a class="nav-link" href="#" data-scroll-nav="0">Home</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="#light" data-scroll-nav="1"
                        >Light</a
                      >
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="#dark" data-scroll-nav="1"
                        >Dark</a
                      >
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="#" data-scroll-nav="3"
                        >Support</a
                      >
                    </li>
                  </b-navbar-nav>
                </b-collapse>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="intro section-padding position-relative"
      id="intro"
      data-scroll-index="0"
    >
      <div class="container">
        <div class="row align-items-center justify-content-between">
          <div class="col-xl-6 col-md-6">
            <div class="intro-content">
              <h1>
                Trade Cryptocurrency <br />
                With <span class="text-primary">Tradio</span>
              </h1>
              <p>
                Tradio is the complete UI of Front end and Backend. Sign in,
                Signup, Phone and ID card verification, One time password verify
                and add bank, debit card settings and profile etc pages
                included.
              </p>
              <a
                href="#"
                class="btn btn-primary px-3 mx-2 my-2"
                data-scroll-nav="1"
                >View Demo</a
              >
              <a href="#" class="btn btn-outline-primary px-3 mx-2 my-2"
                >Buy Now</a
              >
            </div>
          </div>
          <div class="col-xl-6 col-md-6 py-md-5">
            <div class="intro-demo_img">
              <img
                src="../assets/images/portfolio.jpg"
                alt=""
                class="img-fluid"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- demo light -->
    <div
      id="light"
      class="demo section-padding page-section"
      data-scroll-index="1"
    >
      <div class="container">
        <div class="row py-lg-5 justify-content-center">
          <div class="col-xl-7">
            <div class="section-heading text-center">
              <h2>Dashboard Light</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/landing.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Landing</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/dashboard" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/dashboard.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Dashboard</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/buy-sell" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/buy-sell.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Exchange</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-overview" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/accounts.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Accounts</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-deposit" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/deposit.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Deposit</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-withdraw" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/withdraw.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Withdraw</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-api" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/api.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>API</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-affiliate" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/affiliate.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Affiliate</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-tbi" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/tbi.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Tradio Bitcoin Index</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-founding-rate" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/funding-rate.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Funding Rate</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-insurance-found" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/insurance-fund.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Insurance Found</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-last-price" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/last-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Last Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-index-price" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/index-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Index Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-mark-price" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/mark-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Mark Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/settings.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Edit Profile</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-preferences" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/preferences.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Preferences</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-security" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/security.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Security</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-account" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/linked-account.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Linked Account</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/signin" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/signin.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Signin</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/signup" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/signup.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Signup</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/reset" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/reset.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Reset</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/lock" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/lock.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Locked</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/otp-1" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/otp-phone.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>OTP Number</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/otp-2" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/otp-code.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>OTP Code</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-1" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/verify-id.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Verify ID</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-2" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/upload-id.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Upload ID</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-3" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/id-verifing.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>ID Verifying</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-4" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/id-verified.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>ID Verified</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/add-debit-card" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/add-debit-card.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Add Debit Card</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-6" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/success.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Success</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-5" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/choose-account.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Recommendation</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/add-bank-acc" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/add-bank.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Add Bank Account</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/400" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/400.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>400</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/403" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/403.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>403</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/404" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/404.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>404</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/500" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/500.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>500</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/503" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/light/503.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>503</h4>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Demo dark -->

    <div
      id="dark"
      class="demo section-padding page-section bg-dark demo-bg-dark"
      data-scroll-index="1"
    >
      <div class="container">
        <div class="row py-lg-5 justify-content-center">
          <div class="col-xl-7">
            <div class="section-heading text-center">
              <h2>Dashboard Dark</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/landing.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Landing</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/dashboard-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/dashboard.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Dashboard</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/buy-sell-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/buy-sell.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Exchange</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-overview-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/accounts.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Accounts</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-deposit-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/deposit.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Deposit</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-withdraw-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/withdraw.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Withdraw</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-api-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/api.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>API</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/account-affiliate-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/affiliate.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Affiliate</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-tbi-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/tbi.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Tradio Bitcoin Index</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-founding-rate-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/funding-rate.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Funding Rate</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-insurance-found-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/insurance-fund.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Insurance Found</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-last-price-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/last-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Last Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-index-price-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/index-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Index Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/data-mark-price-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/mark-price.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Mark Price</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/settings.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Edit Profile</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-preferences-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/preferences.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Preferences</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-security-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/security.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Security</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/settings-account-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/linked-account.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Linked Account</h4>
            </div>
          </div>

          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/signin-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/signin.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Signin</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/signup-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/signup.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Signup</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/reset-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/reset.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Reset</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/lock-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/lock.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Locked</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/otp-1-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/otp-phone.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>OTP Number</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/otp-2-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/otp-code.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>OTP Code</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-1-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/verify-id.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Verify ID</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-2-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/upload-id.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Upload ID</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-3-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/id-verifing.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>ID Verifying</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-4-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/id-verified.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>ID Verified</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/add-debit-card-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/add-debit-card.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Add Debit Card</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-6-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/success.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Success</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/verify-step-5-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/choose-account.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Recommendation</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/add-bank-acc-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/add-bank.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>Add Bank Account</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/400-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/400.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>400</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/403-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/403.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>403</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/404-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/404.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>404</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/500-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/500.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>500</h4>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-6">
            <div class="demo_img">
              <router-link to="/503-dark" target="_blank">
                <div class="img-wrap">
                  <!-- <img
                    src="../assets/images/demo/dark/503.jpg"
                    alt=""
                    class="img-fluid"
                  /> -->
                </div>
              </router-link>
              <h4>503</h4>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer dashboard">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-8 col-12">
            <div class="copyright">
              <p>
                © Copyright {{ new Date().getFullYear() }}
                <a href="https://synspot-ai.com"
                  >Synspot</a
                >
                I All Rights Reserved
              </p>
            </div>
          </div>
          <div class="col-sm-4 col-12">
            <div class="footer-social">
              <ul>
                <li>
                  <a href="#"><i class="fa fa-facebook"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-twitter"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-linkedin"></i></a>
                </li>
                <li>
                  <a href="#"><i class="fa fa-youtube"></i></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
