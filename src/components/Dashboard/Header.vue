<template>
  <div class="header dashboard">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-12">
          <nav
            class="navbar navbar-expand-lg navbar-light px-0 justify-content-between"
          >
            <router-link class="navbar-brand" to="dashboard"
              ><img src="../../assets/images/logo1.png" alt=""
            /></router-link>

            <div class="header-right d-flex my-2 align-items-center">
              <div class="language">
                <div class="dropdown">
                  <div
                    class="icon"
                    data-toggle="dropdown"
                    @click="activeDropDown('lang')"
                    :class="toggle === 'lang' && 'show'"
                  >
                    <i class="flag-icon flag-icon-us"></i>
                    <span>English</span>
                  </div>
                  <div
                    class="dropdown-menu dropdown-menu-right"
                    :class="toggle === 'lang' && 'show'"
                  >
                    <router-link to="#" class="dropdown-item">
                      <i class="flag-icon flag-icon-bd"></i> Bengali
                    </router-link>
                    <router-link to="#" class="dropdown-item">
                      <i class="flag-icon flag-icon-fr"></i> French
                    </router-link>
                    <router-link to="#" class="dropdown-item">
                      <i class="flag-icon flag-icon-cn"></i> China
                    </router-link>
                  </div>
                </div>
              </div>
              <div class="dashboard_log">
                <div
                  class="profile_log dropdown"
                  @click="activeDropDown('profile')"
                  :class="toggle === 'profile' && 'show'"
                >
                  <div class="user" data-toggle="dropdown">
                    <span class="thumb"><i class="mdi mdi-account"></i></span>
                    <span class="arrow"><i class="la la-angle-down"></i></span>
                  </div>

                  <div
                    class="dropdown-menu dropdown-menu-right"
                    :class="toggle === 'profile' && 'show'"
                  >
                    <div class="user-email">
                      <div class="user">
                        <span class="thumb"
                          ><i class="mdi mdi-account"></i
                        ></span>
                        <div class="user-info">
                          <h6>Sabuj Hasan Sarker</h6>
                          <span>quixlab.com@gmail.com</span>
                        </div>
                      </div>
                    </div>

                    <div class="user-balance">
                      <div class="available">
                        <p>Available</p>
                        <span>0.00 USD</span>
                      </div>
                      <div class="total">
                        <p>Total</p>
                        <span>0.00 USD</span>
                      </div>
                    </div>
                    <router-link
                      :to="darkLink('account-overview')"
                      class="dropdown-item"
                    >
                      <i class="mdi mdi-account"></i> Account
                    </router-link>
                    <router-link
                      :to="darkLink('data-tbi')"
                      class="dropdown-item"
                    >
                      <i class="mdi mdi-history"></i> History
                    </router-link>
                    <router-link
                      :to="darkLink('settings')"
                      class="dropdown-item"
                    >
                      <i class="mdi mdi-settings"></i> Setting
                    </router-link>
                    <router-link :to="darkLink('lock')" class="dropdown-item">
                      <i class="mdi mdi-lock"></i> Lock
                    </router-link>
                    <router-link
                      :to="darkLink('signin')"
                      class="dropdown-item logout"
                    >
                      <i class="mdi mdi-logout"></i> Logout
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Header",
  data() {
    return {
      toggle: false,
    };
  },
  props: {
    dark: Boolean,
  },
  methods: {
    activeDropDown(value) {
      this.toggle = this.toggle === value ? "" : value;
    },
    darkLink(name) {
      console.log(this.dark);
      if (this.dark) {
        return `/${name}-dark`;
      } else {
        return `/${name}`;
      }
    },
  },
};
</script>
