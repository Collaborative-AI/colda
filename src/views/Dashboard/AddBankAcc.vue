<template>
  <dashboard-layout>
    <div class="content-body">
      <div class="verification section-padding mb-80">
        <div class="container h-100">
          <div
            class="row justify-content-center h-100 align-items-center  my-5"
          >
            <div class="col-xl-5 col-md-6">
              <div class="auth-form card">
                <div class="card-header">
                  <h4 class="card-title">Link a bank account</h4>
                </div>
                <div class="card-body">
                  <form @submit.prevent="formSubmit" class="identity-upload">
                    <div class="form-row">
                      <div class="form-group col-xl-12">
                        <label class="me-sm-2">Routing number </label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="25487"
                        />
                      </div>
                      <div class="form-group col-xl-12">
                        <label class="me-sm-2">Account number </label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="36475"
                        />
                      </div>
                      <div class="form-group col-xl-12">
                        <label class="me-sm-2">Fulll name </label>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Carla Pascle"
                        />
                      </div>
                      <div class="form-group col-xl-12">
                        <img
                          src="../../assets/images/routing.png"
                          alt=""
                          class="img-fluid"
                        />
                      </div>

                      <div class="text-center col-12">
                        <router-link
                          to="verify-step-5"
                          class="btn btn-primary mx-2"
                          >Back</router-link
                        >
                        <button type="submit" class="btn btn-success mx-2">
                          Save
                        </button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </dashboard-layout>
</template>

<script>
import DashboardLayout from "../../components/Layouts/DashboardLayout.vue";
export default {
  components: { DashboardLayout },
  data() {
    return {
      dark: window.location.pathname.includes("dark"),
    };
  },
  methods: {
    formSubmit() {
      this.$router.push(this.dark ? "/verify-step-6-dark" : "/verify-step-6");
    },
  },
};
</script>
