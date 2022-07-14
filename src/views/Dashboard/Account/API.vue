<template>
  <account-layout :active="4">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Create API Key</h4>
        </div>
        <div class="card-body">
          <form action="" @submit.prevent="">
            <div class="row">
              <div class="col-xl-6 col-md-6">
                <div class="form-group">
                  <label class="me-sm-2">Generate New Key</label>
                  <input
                    type="text"
                    name="usd_amount"
                    class="form-control"
                    placeholder="Enter Passphrase"
                  />
                </div>
              </div>
              <div class="col-xl-6 col-md-6">
                <div class="form-group">
                  <label class="me-sm-2">Confirm Passphrase</label>
                  <input
                    type="text"
                    name="usd_amount"
                    class="form-control"
                    placeholder="Re-enter passphrase"
                  />
                </div>
              </div>
              <div class="col-auto">
                <button class="btn btn-primary">Create API Keys</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Your API Keys</h4>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Key</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>69e387f1-31c3-45ad-9c68-5a51e5e78b43</td>
                  <td>
                    <label class="toggle">
                      <input
                        class="toggle-checkbox"
                        type="checkbox"
                        checked=""
                      />
                      <span class="toggle-switch"></span>
                    </label>
                  </td>
                  <td>
                    <span>
                      <i class="mdi mdi-delete fs-20"></i>
                    </span>
                  </td>
                </tr>
                <tr>
                  <td>69e387f1-31c3-45ad-9c68-5a51e5e78b43</td>
                  <td>
                    <label class="toggle">
                      <input class="toggle-checkbox" type="checkbox" />
                      <span class="toggle-switch"></span>
                    </label>
                  </td>
                  <td>
                    <span>
                      <i class="mdi mdi-delete fs-20"></i>
                    </span>
                  </td>
                </tr>
                <tr>
                  <td>69e387f1-31c3-45ad-9c68-5a51e5e78b43</td>
                  <td>
                    <label class="toggle">
                      <input class="toggle-checkbox" type="checkbox" />
                      <span class="toggle-switch"></span>
                    </label>
                  </td>
                  <td>
                    <span>
                      <i class="mdi mdi-delete fs-20"></i>
                    </span>
                  </td>
                </tr>
                <tr>
                  <td>69e387f1-31c3-45ad-9c68-5a51e5e78b43</td>
                  <td>
                    <label class="toggle">
                      <input
                        class="toggle-checkbox"
                        type="checkbox"
                        checked=""
                      />
                      <span class="toggle-switch"></span>
                    </label>
                  </td>
                  <td>
                    <span>
                      <i class="mdi mdi-delete fs-20"></i>
                    </span>
                  </td>
                </tr>
                <tr>
                  <td>69e387f1-31c3-45ad-9c68-5a51e5e78b43</td>
                  <td>
                    <label class="toggle">
                      <input class="toggle-checkbox" type="checkbox" />
                      <span class="toggle-switch"></span>
                    </label>
                  </td>
                  <td>
                    <span>
                      <i class="mdi mdi-delete fs-20"></i>
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
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
