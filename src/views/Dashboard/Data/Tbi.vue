<template>
  <data-layout :active="1">
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">TBI Details</h4>
        </div>
        <div class="card-body">
          <TBI :number="30" />
        </div>
      </div>
    </div>
    <div class="col-xl-12">
      <div class="card">
        <div class="card-header">
          <h4 class="card-title">Bitcoin Index History</h4>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Time</th>
                  <th>Index Price</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
                <tr>
                  <td>2020/03/09 10:53:20</td>
                  <td>$7873.07</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </data-layout>
</template>

<script>
import DataLayout from "../../../components/Layouts/DataLayout.vue";
import TBI from "../../../components/Tradio/Charts/TBI.vue";
export default {
  components: { DataLayout, TBI },
  data() {
    return {
      chartData: 30,
      activeTab: 1,
    };
  },
  methods: {
    onClick(n1, n2) {
      this.chartData = n2;
      this.activeTab = n1;
    },
  },
};
</script>
