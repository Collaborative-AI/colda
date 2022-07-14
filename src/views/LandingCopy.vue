<template>
  <div id="main-wrapper" class="show">
    <div class="header">
      <div class="container">
        <div class="row">
          <div class="col-xl-12">
            <div class="navigation">
              <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <router-link class="navbar-brand" to="/"
                  ><img src="../assets/images/logo.png" alt=""
                /></router-link>
                <b-navbar-toggle target="navbarNavDropdown"> </b-navbar-toggle>
                <b-collapse is-nav id="navbarNavDropdown">
                  <b-navbar-nav tag="ul" class="navbar-nav">
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        :class="active === 1 && 'active'"
                        @click="active = 1"
                        href="#sec_1"
                        data-scroll-nav="0"
                        >Home</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_2"
                        :class="active === 2 && 'active'"
                        @click="active = 2"
                        data-scroll-nav="1"
                        >Price</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_3"
                        :class="active === 3 && 'active'"
                        @click="active = 3"
                        data-scroll-nav="2"
                        >Portfolio
                      </a>
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_4"
                        :class="active === 4 && 'active'"
                        @click="active = 4"
                        data-scroll-nav="3"
                        >Testimonial</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_5"
                        :class="active === 5 && 'active'"
                        @click="active = 5"
                        data-scroll-nav="4"
                        >App</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_6"
                        :class="active === 6 && 'active'"
                        @click="active = 6"
                        data-scroll-nav="5"
                        >Blog</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        class="nav-link"
                        href="#sec_7"
                        :class="active === 7 && 'active'"
                        @click="active = 7"
                        data-scroll-nav="6"
                        >Support</a
                      >
                    </li>

                    <li class="nav-item">
                      <router-link class="nav-link" :to="dark ? '/dashboard-dark': '/dashboard'"
                        >Dashboard</router-link
                      >
                    </li>
                  </b-navbar-nav>
                </b-collapse>

                <div class="signin-btn">
                  <router-link class="btn btn-primary text-white" :to="dark ? '/signin-dark': '/signin'"
                    >Sign in</router-link
                  >
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="intro" data-scroll-index="0" id="sec_1">
      <div class="container">
        <div class="row justify-content-between align-items-center">
          <div class="col-xl-6 col-lg-6 col-12">
            <div class="intro-content">
              <h1>
                Trade with <strong class="text-primary">Tradio</strong>. <br />
                Buy and sell cryptocurrency
              </h1>
              <p>
                Fast and secure way to purchase or exchange 150+
                cryptocurrencies
              </p>
            </div>

            <div class="intro-btn">
              <a href="#" class="btn btn-primary text-white m-2">Get Started</a>
              <a href="#" class="btn btn-outline-primary m-2">Browse Now</a>
            </div>
          </div>
          <div class="col-xl-5 col-lg-6 col-12">
            <div class="intro-form-exchange">
              <currency-form />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="price-grid section-padding" id="sec_2" data-scroll-index="1">
      <div class="container">
        <div class="row">
          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc BTC"></i></span>
                  <div class="media-body">
                    Bitcoin
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <!-- <div id="btcChart"></div> -->
                <btc-chart :color="'#F7931A'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc LTC"></i></span>
                  <div class="media-body">
                    Litecoin
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#838383'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc DASH"></i></span>
                  <div class="media-body">
                    Dashcoin
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#1C75BC'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc XRP"></i></span>
                  <div class="media-body">
                    Ripple
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#346AA9'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc ETH"></i></span>
                  <div class="media-body">
                    Ethereum
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#282828'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc USDT"></i></span>
                  <div class="media-body">
                    Tether
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#2CA07A'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc EOS"></i></span>
                  <div class="media-body">
                    Eosio
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#3B3B3C'" />
              </div>
            </div>
          </div>

          <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6">
            <div class="card">
              <div class="card-header">
                <div class="media">
                  <span><i class="cc XTZ"></i></span>
                  <div class="media-body">
                    Tezos
                  </div>
                </div>
                <p class="mb-0">24h</p>
              </div>
              <div class="card-body">
                <h3>USD 62,548.2254</h3>
                <span class="text-success">+2.05%</span>
                <btc-chart :color="'#A6DF00'" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="getstart section-padding">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-8">
            <div class="section-title">
              <h2>Get started in a few minutes</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-4 col-lg-4 col-md-4 col-sm-4">
            <div class="getstart-content">
              <span><i class="la la-user-plus"></i></span>
              <h3>Create an account</h3>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4 col-sm-4">
            <div class="getstart-content">
              <span><i class="la la-bank"></i></span>
              <h3>Link your bank account</h3>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4 col-sm-4">
            <div class="getstart-content">
              <span><i class="la la-exchange"></i></span>
              <h3>Start buying & selling</h3>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="portfolio section-padding" data-scroll-index="2" id="sec_3">
      <div class="container">
        <div class="row py-lg-5 justify-content-center">
          <div class="col-xl-7">
            <div class="section-title text-center">
              <h2>Create your cryptocurrency portfolio today</h2>
              <p>
                Tradio has a variety of features that make it the best place to
                start trading
              </p>
            </div>
          </div>
        </div>
        <div class="row align-items-center justify-content-between">
          <div class="col-xl-7 col-lg-6">
            <div class="portfolio_list">
              <div class="row">
                <div class="col-xl-6">
                  <div class="media">
                    <span class="port-icon my-4">
                      <i class="la la-bar-chart"></i
                    ></span>
                    <div class="media-body">
                      <h4>Manage your portfolio</h4>
                      <p>
                        Buy and sell popular digital currencies, keep track of
                        them in the one place.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="col-xl-6">
                  <div class="media">
                    <span class="port-icon my-4">
                      <i class="la la-calendar-check-o"></i
                    ></span>
                    <div class="media-body">
                      <h4>Recurring buys</h4>
                      <p>
                        Invest in cryptocurrency slowly over time by scheduling
                        buys daily, weekly, or monthly.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="col-xl-6">
                  <div class="media">
                    <span class="port-icon my-4"> <i class="la la-lock"></i></span>
                    <div class="media-body">
                      <h4>Vault protection</h4>
                      <p>
                        For added security, store your funds in a vault with
                        time delayed withdrawals.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="col-xl-6">
                  <div class="media">
                    <span class="port-icon my-4"> <i class="la la-mobile"></i></span>
                    <div class="media-body">
                      <h4>Mobile apps</h4>
                      <p>
                        Stay on top of the markets with the Tradio app for
                        <a href="#">Android</a>
                        or
                        <a href="#">iOS</a>.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-5 col-lg-6">
            <div class="portfolio_img">
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

    <div class="trade-app section-padding">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-6">
            <div class="section-title text-center">
              <h2>Trade. Anywhere</h2>
              <p>
                All of our products are ready to go, easy to use and offer great
                value to any kind of business
              </p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-mobile"></i></span>
                <h4 class="card-title">Mobile</h4>
                <p>
                  All the power of Tradio's cryptocurrency exchange, in the palm
                  of your hand. Download the Tradio mobile crypto trading app
                  today
                </p>

                <a href="#"> Know More <i class="la la-arrow-right"></i> </a>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-desktop"></i></span>
                <h4 class="card-title">Desktop</h4>
                <p>
                  Powerful crypto trading platform for those who mean business.
                  The Tradio crypto trading experience, tailor-made for your
                  Windows or MacOS device.
                </p>

                <a href="#"> Know More <i class="la la-arrow-right"></i> </a>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="card trade-app-content">
              <div class="card-body">
                <span><i class="la la-connectdevelop"></i></span>
                <h4 class="card-title">API</h4>
                <p>
                  The Tradio API is designed to provide an easy and efficient
                  way to integrate your trading application into our platform.
                </p>

                <a href="#"> Know More <i class="la la-arrow-right"></i> </a>
              </div>
            </div>
          </div>
        </div>
        <div class="row pt-5">
          <div class="col-xl-12">
            <div class="trusted-business py-5 text-center">
              <h3>Trusted by Our <strong>Partners & Investors</strong></h3>
            </div>
            <div class="row justify-content-center">
              <div class="col-auto">
                <div class="trusted-logo">
                  <!-- <a href="#"
                    ><img
                      class="img-fluid"
                      src="../assets/images/brand/1.webp"
                      alt=""
                  /></a> -->
                </div>
              </div>
              <div class="col-auto">
                <div class="trusted-logo">
                  <!-- <a href="#"
                    ><img
                      class="img-fluid"
                      src="../assets/images/brand/2.webp"
                      alt=""
                  /></a> -->
                </div>
              </div>
              <div class="col-auto">
                <div class="trusted-logo">
                  <!-- <a href="#"
                    ><img
                      class="img-fluid"
                      src="../assets/images/brand/3.webp"
                      alt=""
                  /></a> -->
                </div>
              </div>
              <div class="col-auto">
                <div class="trusted-logo">
                  <!-- <a href="#"
                    ><img
                      class="img-fluid"
                      src="../assets/images/brand/4.webp"
                      alt=""
                  /></a> -->
                </div>
              </div>
              <div class="col-auto">
                <div class="trusted-logo">
                  <!-- <a href="#"
                    ><img
                      class="img-fluid"
                      src="../assets/images/brand/5.webp"
                      alt=""
                  /></a> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="testimonial section-padding" data-scroll-index="3" id="sec_4">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-6">
            <div class="section-title">
              <h2>What our customer says</h2>
            </div>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-xl-10">
            <div class="testimonial-content">
              <div class="testimonial1 owl-carousel owl-theme">
                <slider />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="promo section-padding">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-8">
            <div class="section-title text-center">
              <h2>The most trusted cryptocurrency platform</h2>
              <p>Here are a few reasons why you should choose Tradio</p>
            </div>
          </div>
        </div>
        <div class="row align-items-center py-5">
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="promo-content">
              <div class="promo-content-img">
                <!-- <img
                  class="img-fluid"
                  src="../assets/images/svg/protect.svg"
                  alt=""
                /> -->
              </div>
              <h3>Secure storage</h3>
              <p>
                We store the vast majority of the digital assets in secure
                offline storage.
              </p>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="promo-content">
              <div class="promo-content-img">
                <!-- <img
                  class="img-fluid"
                  src="../assets/images/svg/cyber.svg"
                  alt=""
                /> -->
              </div>
              <h3>Protected by insurance</h3>
              <p>
                Cryptocurrency stored on our servers is covered by our insurance
                policy.
              </p>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="promo-content">
              <div class="promo-content-img">
                <!-- <img
                  class="img-fluid"
                  src="../assets/images/svg/finance.svg"
                  alt=""
                /> -->
              </div>
              <h3>Industry best practices</h3>
              <p>
                Tradio supports a variety of the most popular digital
                currencies.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="appss section-padding" data-scroll-index="4" id="sec_5">
      <div class="container">
        <div class="row align-items-center justify-content-between">
          <div class="col-xl-7 col-lg-6 col-md-6">
            <div class="appss-content">
              <h2>The secure app to store crypto yourself</h2>
              <ul>
                <li>
                  <i class="la la-check"></i> All your digital assets in one
                  place
                </li>
                <li><i class="la la-check"></i> Use Decentralized Apps</li>
                <li><i class="la la-check"></i> Pay friends, not addresses</li>
              </ul>
              <div class="mt-4">
                <a href="#" class="btn btn-primary my-1 waves-effect">
                  <img src="../assets/images/android.svg" alt="" />
                </a>
                <a href="#" class="btn btn-primary my-1 waves-effect">
                  <img src="../assets/images/apple.svg" alt="" />
                </a>
              </div>
            </div>
          </div>
          <div class="col-xl-5 col-lg-6 col-md-6">
            <div class="appss-img">
              <img class="img-fluid" src="../assets/images/app2.png" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="blog section-padding" data-scroll-index="5" id="sec_6">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-6">
            <div class="section-title text-center">
              <h2>Blog</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="blog-grid">
              <div class="card">
                <img
                  class="img-fluid"
                  src="../assets/images/blog/1.jpg"
                  alt=""
                />
                <div class="card-body">
                  <a href="blog-single">
                    <h4 class="card-title">
                      Why does Litecoin need MimbleWimble?
                    </h4>
                  </a>
                  <p class="card-text">
                    Cras chinwag brown bread Eaton cracking goal so I said a
                    load of old tosh baking cakes.!
                  </p>
                </div>
                <div class="card-footer">
                  <div class="meta-info">
                    <a href="#" class="author"
                      ><img src="../assets/images/avatar/5.jpg" alt="" />
                      Admin</a
                    >
                    <a href="#" class="post-date"
                      ><i class="la la-calendar"></i> 31 July, 2019</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="blog-grid">
              <div class="card">
                <img
                  class="img-fluid"
                  src="../assets/images/blog/2.jpg"
                  alt=""
                />
                <div class="card-body">
                  <a href="#">
                    <h4 class="card-title">
                      How to securely store your HD wallet seeds?
                    </h4>
                  </a>
                  <p class="card-text">
                    Cras chinwag brown bread Eaton cracking goal so I said a
                    load of old tosh baking cakes.!
                  </p>
                </div>
                <div class="card-footer">
                  <div class="meta-info">
                    <a href="#" class="author"
                      ><img src="../assets/images/avatar/6.jpg" alt="" />
                      Admin</a
                    >
                    <a href="#" class="post-date"
                      ><i class="la la-calendar"></i> 31 July, 2019</a
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-12">
            <div class="blog-grid">
              <div class="card">
                <img
                  class="img-fluid"
                  src="../assets/images/blog/3.jpg"
                  alt=""
                />
                <div class="card-body">
                  <router-link to="#">
                    <h4 class="card-title">
                      Exclusive Interview With Xinxi Wang Of Litecoin
                    </h4>
                  </router-link>
                  <p class="card-text">
                    Cras chinwag brown bread Eaton cracking goal so I said a
                    load of old tosh baking cakes.!
                  </p>
                </div>
                <div class="card-footer">
                  <div class="meta-info">
                    <router-link to="#" class="author"
                      ><img src="../assets/images/avatar/7.jpg" alt="" />
                      Admin</router-link
                    >
                    <router-link to="#" class="post-date"
                      ><i class="la la-calendar"></i> 31 July, 2019</router-link
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="get-touch section-padding" data-scroll-index="6" id="sec_7">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-6">
            <div class="section-title">
              <h2>Get in touch. Stay in touch.</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="get-touch-content">
              <div class="media">
                <span><i class="fa fa-shield my-3"></i></span>
                <div class="media-body">
                  <h4>24 / 7 Support</h4>
                  <p>
                    Got a problem? Just get in touch. Our support team is
                    available 24/7.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="get-touch-content">
              <div class="media">
                <span><i class="fa fa-cubes my-3"></i></span>
                <div class="media-body">
                  <h4>Tradio Blog</h4>
                  <p>
                    News and updates from the world’s leading cryptocurrency
                    exchange.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="get-touch-content">
              <div class="media">
                <span><i class="fa fa-certificate my-3"></i></span>
                <div class="media-body">
                  <h4>Careers</h4>
                  <p>
                    Help build the future of technology. Start your new career
                    at Tradio.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="get-touch-content">
              <div class="media">
                <span><i class="fa fa-life-ring my-3"></i></span>
                <div class="media-body">
                  <h4>Community</h4>
                  <p>
                    Tradio is global. Join the discussion in our worldwide
                    communities.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bottom section-padding">
      <div class="container">
        <div class="row">
          <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6">
            <div class="bottom-logo">
              <img class="pb-3" src="../assets/images/logo.png" alt="" />

              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
            </div>
          </div>
          <div class="col-xl-2 col-lg-2 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Company</h4>
              <ul>
                <li><router-link to="#">About</router-link></li>
                <li><router-link to="#">Career</router-link></li>
                <li><router-link to="#">Affiliate</router-link></li>
                <li><router-link to="#">Our Partner</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-xl-2 col-lg-2 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Support</h4>
              <ul>
                <li><router-link to="#">Ticket</router-link></li>
                <li><router-link to="#">FAQ</router-link></li>
                <li><router-link to="#">Blog</router-link></li>
                <li><router-link to="#">Helpdesk</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6">
            <div class="bottom-widget">
              <h4 class="widget-title">Exchange Pair</h4>
              <div class="row">
                <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                  <ul>
                    <li><router-link to="#">ETH to BTC</router-link></li>
                    <li><router-link to="#">BTC to ETH</router-link></li>
                    <li><router-link to="#">LTC to ETH</router-link></li>
                    <li><router-link to="#">USDT to BTC</router-link></li>
                  </ul>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6">
                  <ul>
                    <li><router-link to="#">BTC to USDT</router-link></li>
                    <li><router-link to="#">LTC to BTC</router-link></li>
                    <li><router-link to="#">XMR to BTC</router-link></li>
                    <li><router-link to="#">ETC to DASH</router-link></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="container">
        <div class="row">
          <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
            <div class="copyright">
              <p>
                © Copyright {{ new Date().getFullYear() }}
                <a href="#">Tradio</a> I All Rights Reserved
              </p>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
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

<script>
import BtcChart from "../components/Tradio/Charts/BtcChart.vue";
import CurrencyForm from "../components/Tradio/From/CurrencyForm.vue";
import Slider from "../components/Tradio/Slider.vue";
export default {
  components: { BtcChart, Slider, CurrencyForm },
  data() {
    return {
      active: 1,
      dark: window.location.pathname.includes("dark"),
    };
  },
  mounted() {
    const body = document.querySelector("body");
    if (this.dark) {
      body.className = "dark";
    } else {
      body.className = "light";
    }
  },
};
</script>
