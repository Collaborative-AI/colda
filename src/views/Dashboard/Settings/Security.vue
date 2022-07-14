<template>
  <setting-layout :active="3">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Security</h4>
        </div>
        <div class="card-body">
          <div class="row align-items-center">
            <div class="col-xl-4">
              <div class="id_card">
                <img
                  src="../../../assets/images/id.png"
                  alt=""
                  class="img-fluid"
                />
              </div>
            </div>
            <div class="col-xl-6">
              <div class="id_info">
                <h3>Carla Pascle</h3>
                <p class="mb-1 mt-3">ID: 0024 5687 2254 3698</p>
                <p class="mb-1">
                  Status: <span class="font-weight-bold">Verified</span>
                </p>
                <router-link
                  :to="dark ? 'verify-step-2-dark' : 'verify-step-2'"
                  class="btn btn-success mt-3"
                  >New ID</router-link
                >
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-xl-12">
              <div class="phone_verify">
                <h4 class="card-title mb-3">Email Address</h4>
                <form @submit.prevent="otpSubmit">
                  <div class="form-row align-items-center">
                    <div class="form-group col-xl-6">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="hello@example.com "
                      />
                      <button class="btn btn-success mt-4">Add</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <div class="col-xl-12">
              <div class="phone_verified flex-wrap">
                <h5>
                  <span><i class="fa fa-envelope"></i></span> hello@example.com
                </h5>
                <div class="verify my-2">
                  <div class="verified">
                    <span><i class="la la-check"></i></span>
                    <router-link to="#">Verified</router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xl-12">
              <div class="phone_verify">
                <h4 class="card-title mb-3">Add Phone Number</h4>
                <form @submit.prevent="otpSubmit">
                  <div class="form-row align-items-center">
                    <div class="form-group col-xl-6">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="+1 2335 2458 "
                      />
                      <button class="btn btn-success mt-4">Add</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <div class="col-xl-12">
              <div class="phone_verified flex-wrap">
                <h5>
                  <span><i class="fa fa-phone"></i></span> +1 23584 2659
                </h5>
                <div class="verify my-2">
                  <div class="verified">
                    <span><i class="la la-check"></i></span>
                    <router-link to="#">Verified</router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </setting-layout>
</template>

<script>
import SettingLayout from "../../../components/Layouts/SettingLayout.vue";
export default {
  components: { SettingLayout },
  data() {
    return {
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    otpSubmit() {
      this.$router.push(this.dark ? "/otp-2-dark" : "/otp-2");
    },
  },
};
</script>
