<template>
  <div id="chartdiv" ref="chartdiv"></div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import darkTheme from "@amcharts/amcharts4/themes/dark";

export default {
  name: "AmChart",
  props: {
    dark: Boolean,
  },
  mounted() {
    let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart);

    if (this.dark) {
      am4core.useTheme(darkTheme);
    } else {
      am4core.useTheme(am4themes_animated);
    }
    chart.dataSource.url =
      "https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_ETH&depth=50";
    chart.dataSource.reloadFrequency = 30000;
    chart.dataSource.adapter.add("parsedData", function(data) {
      // Function to process (sort and calculate cummulative volume)
      function processData(list, type, desc) {
        // Convert to data points
        for (var i = 0; i < list.length; i++) {
          list[i] = {
            value: Number(list[i][0]),
            volume: Number(list[i][1]),
          };
        }

        // Sort list just in case
        list.sort(function(a, b) {
          if (a.value > b.value) {
            return 1;
          } else if (a.value < b.value) {
            return -1;
          } else {
            return 0;
          }
        });

        // Calculate cummulative volume
        if (desc) {
          for (var j = list.length - 1; j >= 0; j--) {
            if (j < list.length - 1) {
              list[j].totalvolume = list[j + 1].totalvolume + list[j].volume;
            } else {
              list[j].totalvolume = list[j].volume;
            }
            var dp = {};
            dp["value"] = list[j].value;
            dp[type + "volume"] = list[j].volume;
            dp[type + "totalvolume"] = list[j].totalvolume;
            res.unshift(dp);
          }
        } else {
          for (var k = 0; k < list.length; k++) {
            if (k > 0) {
              list[k].totalvolume = list[k - 1].totalvolume + list[k].volume;
            } else {
              list[k].totalvolume = list[k].volume;
            }
            var dp1 = {};
            dp1["value"] = list[k].value;
            dp1[type + "volume"] = list[k].volume;
            dp1[type + "totalvolume"] = list[k].totalvolume;
            res.push(dp1);
          }
        }
      }

      // Init
      var res = [];
      processData(data.bids, "bids", true);
      processData(data.asks, "asks", false);

      return res;
    });

    // Set up precision for numbers
    chart.numberFormatter.numberFormat = "#,###.####";

    // Create axes
    var xAxis = chart.xAxes.push(new am4charts.CategoryAxis());
    xAxis.dataFields.category = "value";
    //xAxis.renderer.grid.template.location = 0;
    xAxis.renderer.minGridDistance = 50;
    xAxis.title.text = "";

    var yAxis = chart.yAxes.push(new am4charts.ValueAxis());
    yAxis.title.text = "";

    xAxis.renderer.grid.template.stroke = !this.dark ? "#000" : "#fff";
    xAxis.renderer.grid.template.strokeWidth = 1;
    yAxis.renderer.grid.template.strokeWidth = 1;
    yAxis.renderer.grid.template.stroke = !this.dark ? "#000" : "#fff";

    // Create series
    var series = chart.series.push(new am4charts.StepLineSeries());
    series.dataFields.categoryX = "value";
    series.dataFields.valueY = "bidstotalvolume";
    series.strokeWidth = 2;
    series.stroke = am4core.color("#0f0");
    series.fill = series.stroke;
    series.fillOpacity = 0.1;
    series.tooltipText =
      "Ask: [bold]{categoryX}[/]\nTotal volume: [bold]{valueY}[/]\nVolume: [bold]{bidsvolume}[/]";

    var series2 = chart.series.push(new am4charts.StepLineSeries());
    series2.dataFields.categoryX = "value";
    series2.dataFields.valueY = "askstotalvolume";
    series2.strokeWidth = 2;
    series2.stroke = am4core.color("#f00");
    series2.fill = series2.stroke;
    series2.fillOpacity = 0.1;
    series2.tooltipText =
      "Ask: [bold]{categoryX}[/]\nTotal volume: [bold]{valueY}[/]\nVolume: [bold]{asksvolume}[/]";

    // Add cursor
    chart.cursor = new am4charts.XYCursor();

    this.chart = chart;
  },

  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  width: 100%;
  height: 500px;
}
</style>
