<template>
  <apexchart
    type="line"
    height="100"
    :options="chartOptions"
    :series="series"
  ></apexchart>
</template>

<script>
import apexchart from "vue-apexcharts";
export default {
  name: "BtcChart",
  components: { apexchart },
  props: {
    color: String,
  },
  data() {
    return {
      series: [
        {
          name: "Desktops",
          data: [
            10,
            41,
            35,
            51,
            49,
            62,
            69,
            91,
            80,
            10,
            41,
            35,
            51,
            49,
            62,
            69,
            91,
            80,
          ],
        },
      ],
      chartOptions: {
        chart: {
          height: 100,
          type: "line",
          zoom: {
            enabled: false,
          },

          toolbar: {
            show: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
          width: 2,
          colors: [this.color],
        },
        grid: {
          show: false,
        },
        tooltip: {
          enabled: false,
          x: {
            format: "dd MMM yyyy",
          },
        },
        xaxis: {
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: false,
          },
        },
        yaxis: {
          show: false,
        },
      },
    };
  },
};
</script>
