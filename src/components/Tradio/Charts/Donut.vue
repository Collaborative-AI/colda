<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  data() {
    return {
      chartdata: {
        weight: 0,
        defaultFontFamily: "Poppins",
        datasets: [
          {
            data: [80, 20],
            borderWidth: 0,
            backgroundColor: ["#FE9431", "#E5D8BB"],
          },
        ],
      },
      options: {
        width: 130,
        cutoutPercentage: 75,
        responsive: false,
        maintainAspectRatio: true,
        tooltips: { enabled: false },
        hover: { mode: null },
      },
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
