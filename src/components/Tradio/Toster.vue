<template>
  <div id="toast-container" class="toast-top-right demo_rtl_class">
    <div
      class="toast toast-success"
      aria-live="polite"
      :style="{ opacity: show }"
    >
      <donut />
      <div class="toast-progress" v-bind:style="{ width: time + '%' }"></div>
      <div class="circle_progress" role="button"></div>
      <span class="progress_count" role="button">80<i>%</i></span>
      <i class="la la-close" role="button"></i>
      <a href="#" role="button">Suggest</a>
      <div class="toast-title">Complete your payment!</div>
      <div class="toast-message">
        Complete your payment to make it easier to exchange
      </div>
    </div>
  </div>
</template>

<script>
import Donut from "../Tradio/Charts/Donut";
export default {
  name: "Toster",
  components: {
    Donut,
  },
  data() {
    return {
      time: 100,
      show: localStorage.getItem("show_toster_tradio")
        ? localStorage.getItem("show_toster_tradio")
        : 1,
    };
  },
  mounted() {
    const chart = document.querySelector("#doughnut-chart");
    chart.style.height = "90px";
    chart.style.width = "90px";
    chart.style.marginLeft = "-4px";

    localStorage.getItem("show_toster_tradio")
      ? localStorage.getItem("show_toster_tradio")
      : localStorage.setItem("show_toster_tradio", 1);
    setInterval(() => {
      this.time > 0 && this.time--;
      if (this.time === 0) {
        this.show = 0;
        localStorage.setItem("show_toster_tradio", 0);
      }
    }, 60);
  },
};
</script>
