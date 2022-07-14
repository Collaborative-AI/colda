<template>
  <setting-layout :active="4" :dark="dark">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Linked Account or Card</h4>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table linked_account ">
              <tbody>
                <tr>
                  <td>
                    <div class="media">
                      <span class="me-3"><i class="fa fa-bank"></i></span>
                      <div class="media-body">
                        <h5 class="mt-0 mb-1">Bank of America</h5>
                        <p>Bank **********5421</p>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="edit-option">
                      <a href="#"><i class="fa fa-eye"></i></a>
                      <a href="#"><i class="fa fa-pencil"></i></a>
                      <a href="#"><i class="fa fa-trash"></i></a>
                    </div>
                  </td>
                  <td>
                    <div class="verify">
                      <div class="verified">
                        <span><i class="la la-check"></i></span>
                        <a href="#">Verified</a>
                      </div>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="media">
                      <span class="me-3"
                        ><i class="fa fa-credit-card"></i
                      ></span>
                      <div class="media-body">
                        <h5 class="mt-0 mb-1">Debit Card</h5>
                        <p>Prepaid Card *********5478</p>
                      </div>
                    </div>
                  </td>
                  <td>
                    <div class="edit-option">
                      <a href="#"><i class="fa fa-eye"></i></a>
                      <a href="#"><i class="fa fa-pencil"></i></a>
                      <a href="#"><i class="fa fa-trash"></i></a>
                    </div>
                  </td>
                  <td>
                    <div class="verify">
                      <div class="not-verify">
                        <span><i class="la la-close"></i></span>
                        <a href="#">Not verified</a>
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="mt-3">
              <router-link
                :to="dark ? '/verify-step-5-dark' : '/verify-step-5'"
                class="btn btn-primary px-4 py-2 me-3 my-2"
                >Add Bank Account</router-link
              >
              <router-link
                :to="dark ? '/verify-step-1-dark' : '/verify-step-1'"
                class="btn btn-success px-4 py-2 my-2"
                >Add Debit Account</router-link
              >
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
};
</script>
