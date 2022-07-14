<template>
  <dashboard-layout>
    <div class="content-body">
      <div class="verification section-padding">
        <div class="container h-100">
          <div class="row justify-content-center h-100 align-items-center">
            <div class="col-xl-5 col-md-6">
              <div class="auth-form card">
                <div class="card-body">
                  <form @submit.prevent="formSubmit" class="identity-upload">
                    <div class="identity-content">
                      <span class="icon"><i class="fa fa-check"></i></span>
                      <h4>Congratulation. Your bank added</h4>
                      <p>
                        Efficiently provide access to installed base core
                        competencies and end end data Interactively target
                        equity.
                      </p>
                    </div>

                    <div class="text-center">
                      <button type="submit" class="btn btn-success pl-5 pr-5">
                        Continue
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div></dashboard-layout
  >
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
      this.$router.push(
        this.dark ? "/settings-account-dark" : "/settings-account"
      );
    },
  },
};
</script>
