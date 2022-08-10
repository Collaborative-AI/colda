<template>
  <b-container fluid>
    <b-row>
      <b-col lg="6" v-for="(item,index) in charts" :key="index">
        <card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <AmCharts :element="item.type" :type="item.type" :option="item.bodyData"/>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { core } from "../../../config/pluginInit";
import  AmCharts  from "../../../components/charts/AmChart";
export default {
  name: 'AmChart',
  components: {
    AmCharts,
    
  },
  mounted() {
    core.index();
  },
  methods: {
    generateChartData() {
      let chartData = [];
      let firstDate = new Date();
      firstDate.setDate(firstDate.getDate() - 1000);
      let visits = 1200;
      for (let i = 0; i < 500; i++) {
        let newDate = new Date(firstDate);
        newDate.setDate(newDate.getDate() + i);

        visits += Math.round(
          (Math.random() < 0.5 ? 1 : -1) * Math.random() * 10
        );

        chartData.push({
          date: newDate,
          visits: visits,
        });
      }
      return chartData;
    },
  },
  data() {
    return {
      charts: [
        {
          title: "Simple Column Chart",
          type: "line-bar",
          bodyData: {
            colors: ["#6ca0ff"],
            xAxis: ["visits"],
            yAxis: ["country"],
            labels: ["Visits"],
            data: [
              {
                country: "USA",
                visits: 2025,
              },
              {
                country: "China",
                visits: 1882,
              },
              {
                country: "Japan",
                visits: 1809,
              },
              {
                country: "Germany",
                visits: 1322,
              },
              {
                country: "UK",
                visits: 1122,
              },
              {
                country: "France",
                visits: 1114,
              },
            ],
          },
        },
        {
          title: "Column and Line Mix Chart",
          type: "column",
          bodyData: {
            color: "#0084ff",
            fill: "#fdd400",
            data: [
              {
                year: "2009",
                income: 23.5,
                expenses: 21.1,
              },
              {
                year: "2010",
                income: 26.2,
                expenses: 30.5,
              },
              {
                year: "2011",
                income: 30.1,
                expenses: 34.9,
              },
              {
                year: "2012",
                income: 29.5,
                expenses: 31.1,
              },
              {
                year: "2013",
                income: 30.6,
                expenses: 28.2,
                lineDash: "5,5",
              },
              {
                year: "2014",
                income: 34.1,
                expenses: 32.9,
                strokeWidth: 1,
                columnDash: "5,5",
                fillOpacity: 0.2,
                additional: "(projection)",
              },
            ],
          },
        },
        {
          title: "Layered Column Chart",
          type: "mixes-column",
          bodyData: {
            colors: ["#00ca00", "#0084ff"],
            title: "GDP growth rate",
            labels: [
              "GDP grow in {categoryX} (2004): [bold]{valueY}[/]",
              "GDP grow in {categoryX} (2005): [bold]{valueY}[/]",
            ],
            xAxis: ["country"],
            yAxis: ["year2004", "year2005"],
            data: [
              {
                country: "USA",
                year2004: 3.5,
                year2005: 4.2,
              },
              {
                country: "UK",
                year2004: 1.7,
                year2005: 3.1,
              },
              {
                country: "Canada",
                year2004: 2.8,
                year2005: 2.9,
              },
              {
                country: "Japan",
                year2004: 2.6,
                year2005: 2.3,
              },
              {
                country: "France",
                year2004: 1.4,
                year2005: 2.1,
              },
              {
                country: "Brazil",
                year2004: 2.6,
                year2005: 4.9,
              },
            ],
          },
        },
        {
          title: "Stacked Column Chart",
          type: "stacked",
          bodyData: {
            colors: ["#e64141", "#00ca00", "#ffd400"],
            xAxis: ["year"],
            yAxis: ["europe", "namerica", "asia"],
            data: [
              {
                year: "2016",
                europe: 2.5,
                namerica: 2.5,
                asia: 2.1,
                lamerica: 0.3,
                meast: 0.2,
              },
              {
                year: "2017",
                europe: 2.6,
                namerica: 2.7,
                asia: 2.2,
                lamerica: 0.3,
                meast: 0.3,
              },
              {
                year: "2018",
                europe: 2.8,
                namerica: 2.9,
                asia: 2.4,
                lamerica: 0.3,
                meast: 0.3,
              },
            ],
          },
        },
        {
          title: "Bar and line chart mix",
          type: "bar-line",
          bodyData: {
            colors: ["#0084ff", "#00ca00"],
            labels: ["Income", "Expenses"],
            xAxis: ["income", "expenses"],
            yAxis: ["year"],
            data: [
              {
                year: "2005",
                income: 23.5,
                expenses: 18.1,
              },
              {
                year: "2006",
                income: 26.2,
                expenses: 22.8,
              },
              {
                year: "2007",
                income: 30.1,
                expenses: 23.9,
              },
              {
                year: "2008",
                income: 29.5,
                expenses: 25.1,
              },
              {
                year: "2009",
                income: 24.6,
                expenses: 25,
              },
            ],
          },
        },
        {
          title: "Date Based Data",
          type: "data-based",
          bodyData: {
            colors: ["#57aeff"],
            xAxis: ["date"],
            yAxis: ["value"],
            data: [
              {
                date: "2012-07-27",
                value: 13,
              },
              {
                date: "2012-07-28",
                value: 11,
              },
              {
                date: "2012-07-29",
                value: 15,
              },
              {
                date: "2012-07-30",
                value: 16,
              },
              {
                date: "2012-07-31",
                value: 18,
              },
              {
                date: "2012-08-01",
                value: 13,
              },
              {
                date: "2012-08-02",
                value: 22,
              },
              {
                date: "2012-08-03",
                value: 23,
              },
              {
                date: "2012-08-04",
                value: 20,
              },
              {
                date: "2012-08-05",
                value: 17,
              },
              {
                date: "2012-08-06",
                value: 16,
              },
              {
                date: "2012-08-07",
                value: 18,
              },
              {
                date: "2012-08-08",
                value: 21,
              },
              {
                date: "2012-08-09",
                value: 26,
              },
              {
                date: "2012-08-10",
                value: 24,
              },
              {
                date: "2012-08-11",
                value: 29,
              },
              {
                date: "2012-08-12",
                value: 32,
              },
              {
                date: "2012-08-13",
                value: 18,
              },
              {
                date: "2012-08-14",
                value: 24,
              },
              {
                date: "2012-08-15",
                value: 22,
              },
              {
                date: "2012-08-16",
                value: 18,
              },
              {
                date: "2012-08-17",
                value: 19,
              },
              {
                date: "2012-08-18",
                value: 14,
              },
              {
                date: "2012-08-19",
                value: 15,
              },
              {
                date: "2012-08-20",
                value: 12,
              },
              {
                date: "2012-08-21",
                value: 8,
              },
              {
                date: "2012-08-22",
                value: 9,
              },
              {
                date: "2012-08-23",
                value: 8,
              },
              {
                date: "2012-08-24",
                value: 7,
              },
              {
                date: "2012-08-25",
                value: 5,
              },
              {
                date: "2012-08-26",
                value: 11,
              },
              {
                date: "2012-08-27",
                value: 13,
              },
              {
                date: "2012-08-28",
                value: 18,
              },
              {
                date: "2012-08-29",
                value: 20,
              },
              {
                date: "2012-08-30",
                value: 29,
              },
              {
                date: "2012-08-31",
                value: 33,
              },
              {
                date: "2012-09-01",
                value: 42,
              },
              {
                date: "2012-09-02",
                value: 35,
              },
              {
                date: "2012-09-03",
                value: 31,
              },
              {
                date: "2012-09-04",
                value: 47,
              },
              {
                date: "2012-09-05",
                value: 52,
              },
              {
                date: "2012-09-06",
                value: 46,
              },
              {
                date: "2012-09-07",
                value: 41,
              },
              {
                date: "2012-09-08",
                value: 43,
              },
              {
                date: "2012-09-09",
                value: 40,
              },
              {
                date: "2012-09-10",
                value: 39,
              },
              {
                date: "2012-09-11",
                value: 34,
              },
              {
                date: "2012-09-12",
                value: 29,
              },
              {
                date: "2012-09-13",
                value: 34,
              },
              {
                date: "2012-09-14",
                value: 37,
              },
              {
                date: "2012-09-15",
                value: 42,
              },
              {
                date: "2012-09-16",
                value: 49,
              },
              {
                date: "2012-09-17",
                value: 46,
              },
              {
                date: "2012-09-18",
                value: 47,
              },
              {
                date: "2012-09-19",
                value: 55,
              },
              {
                date: "2012-09-20",
                value: 59,
              },
              {
                date: "2012-09-21",
                value: 58,
              },
              {
                date: "2012-09-22",
                value: 57,
              },
              {
                date: "2012-09-23",
                value: 61,
              },
              {
                date: "2012-09-24",
                value: 59,
              },
              {
                date: "2012-09-25",
                value: 67,
              },
              {
                date: "2012-09-26",
                value: 65,
              },
              {
                date: "2012-09-27",
                value: 61,
              },
              {
                date: "2012-09-28",
                value: 66,
              },
              {
                date: "2012-09-29",
                value: 69,
              },
              {
                date: "2012-09-30",
                value: 71,
              },
              {
                date: "2012-10-01",
                value: 67,
              },
              {
                date: "2012-10-02",
                value: 63,
              },
              {
                date: "2012-10-03",
                value: 46,
              },
              {
                date: "2012-10-04",
                value: 32,
              },
              {
                date: "2012-10-05",
                value: 21,
              },
              {
                date: "2012-10-06",
                value: 18,
              },
              {
                date: "2012-10-07",
                value: 21,
              },
              {
                date: "2012-10-08",
                value: 28,
              },
              {
                date: "2012-10-09",
                value: 27,
              },
              {
                date: "2012-10-10",
                value: 36,
              },
              {
                date: "2012-10-11",
                value: 33,
              },
              {
                date: "2012-10-12",
                value: 31,
              },
              {
                date: "2012-10-13",
                value: 30,
              },
              {
                date: "2012-10-14",
                value: 34,
              },
              {
                date: "2012-10-15",
                value: 38,
              },
              {
                date: "2012-10-16",
                value: 37,
              },
              {
                date: "2012-10-17",
                value: 44,
              },
              {
                date: "2012-10-18",
                value: 49,
              },
              {
                date: "2012-10-19",
                value: 53,
              },
              {
                date: "2012-10-20",
                value: 57,
              },
              {
                date: "2012-10-21",
                value: 60,
              },
              {
                date: "2012-10-22",
                value: 61,
              },
              {
                date: "2012-10-23",
                value: 69,
              },
              {
                date: "2012-10-24",
                value: 67,
              },
              {
                date: "2012-10-25",
                value: 72,
              },
              {
                date: "2012-10-26",
                value: 77,
              },
              {
                date: "2012-10-27",
                value: 75,
              },
              {
                date: "2012-10-28",
                value: 70,
              },
              {
                date: "2012-10-29",
                value: 72,
              },
              {
                date: "2012-10-30",
                value: 70,
              },
              {
                date: "2012-10-31",
                value: 72,
              },
              {
                date: "2012-11-01",
                value: 73,
              },
              {
                date: "2012-11-02",
                value: 67,
              },
              {
                date: "2012-11-03",
                value: 68,
              },
              {
                date: "2012-11-04",
                value: 65,
              },
              {
                date: "2012-11-05",
                value: 71,
              },
              {
                date: "2012-11-06",
                value: 75,
              },
              {
                date: "2012-11-07",
                value: 74,
              },
              {
                date: "2012-11-08",
                value: 71,
              },
              {
                date: "2012-11-09",
                value: 76,
              },
              {
                date: "2012-11-10",
                value: 77,
              },
              {
                date: "2012-11-11",
                value: 81,
              },
              {
                date: "2012-11-12",
                value: 83,
              },
              {
                date: "2012-11-13",
                value: 80,
              },
              {
                date: "2012-11-14",
                value: 81,
              },
              {
                date: "2012-11-15",
                value: 87,
              },
              {
                date: "2012-11-16",
                value: 82,
              },
              {
                date: "2012-11-17",
                value: 86,
              },
              {
                date: "2012-11-18",
                value: 80,
              },
              {
                date: "2012-11-19",
                value: 87,
              },
              {
                date: "2012-11-20",
                value: 83,
              },
              {
                date: "2012-11-21",
                value: 85,
              },
              {
                date: "2012-11-22",
                value: 84,
              },
              {
                date: "2012-11-23",
                value: 82,
              },
              {
                date: "2012-11-24",
                value: 73,
              },
              {
                date: "2012-11-25",
                value: 71,
              },
              {
                date: "2012-11-26",
                value: 75,
              },
              {
                date: "2012-11-27",
                value: 79,
              },
              {
                date: "2012-11-28",
                value: 70,
              },
              {
                date: "2012-11-29",
                value: 73,
              },
              {
                date: "2012-11-30",
                value: 61,
              },
              {
                date: "2012-12-01",
                value: 62,
              },
              {
                date: "2012-12-02",
                value: 66,
              },
              {
                date: "2012-12-03",
                value: 65,
              },
              {
                date: "2012-12-04",
                value: 73,
              },
              {
                date: "2012-12-05",
                value: 79,
              },
              {
                date: "2012-12-06",
                value: 78,
              },
              {
                date: "2012-12-07",
                value: 78,
              },
              {
                date: "2012-12-08",
                value: 78,
              },
              {
                date: "2012-12-09",
                value: 74,
              },
              {
                date: "2012-12-10",
                value: 73,
              },
              {
                date: "2012-12-11",
                value: 75,
              },
              {
                date: "2012-12-12",
                value: 70,
              },
              {
                date: "2012-12-13",
                value: 77,
              },
              {
                date: "2012-12-14",
                value: 67,
              },
              {
                date: "2012-12-15",
                value: 62,
              },
              {
                date: "2012-12-16",
                value: 64,
              },
              {
                date: "2012-12-17",
                value: 61,
              },
              {
                date: "2012-12-18",
                value: 59,
              },
              {
                date: "2012-12-19",
                value: 53,
              },
              {
                date: "2012-12-20",
                value: 54,
              },
              {
                date: "2012-12-21",
                value: 56,
              },
              {
                date: "2012-12-22",
                value: 59,
              },
              {
                date: "2012-12-23",
                value: 58,
              },
              {
                date: "2012-12-24",
                value: 55,
              },
              {
                date: "2012-12-25",
                value: 52,
              },
              {
                date: "2012-12-26",
                value: 54,
              },
              {
                date: "2012-12-27",
                value: 50,
              },
              {
                date: "2012-12-28",
                value: 50,
              },
              {
                date: "2012-12-29",
                value: 51,
              },
              {
                date: "2012-12-30",
                value: 52,
              },
              {
                date: "2012-12-31",
                value: 58,
              },
              {
                date: "2013-01-01",
                value: 60,
              },
              {
                date: "2013-01-02",
                value: 67,
              },
              {
                date: "2013-01-03",
                value: 64,
              },
              {
                date: "2013-01-04",
                value: 66,
              },
              {
                date: "2013-01-05",
                value: 60,
              },
              {
                date: "2013-01-06",
                value: 63,
              },
              {
                date: "2013-01-07",
                value: 61,
              },
              {
                date: "2013-01-08",
                value: 60,
              },
              {
                date: "2013-01-09",
                value: 65,
              },
              {
                date: "2013-01-10",
                value: 75,
              },
              {
                date: "2013-01-11",
                value: 77,
              },
              {
                date: "2013-01-12",
                value: 78,
              },
              {
                date: "2013-01-13",
                value: 70,
              },
              {
                date: "2013-01-14",
                value: 70,
              },
              {
                date: "2013-01-15",
                value: 73,
              },
              {
                date: "2013-01-16",
                value: 71,
              },
              {
                date: "2013-01-17",
                value: 74,
              },
              {
                date: "2013-01-18",
                value: 78,
              },
              {
                date: "2013-01-19",
                value: 85,
              },
              {
                date: "2013-01-20",
                value: 82,
              },
              {
                date: "2013-01-21",
                value: 83,
              },
              {
                date: "2013-01-22",
                value: 88,
              },
              {
                date: "2013-01-23",
                value: 85,
              },
              {
                date: "2013-01-24",
                value: 85,
              },
              {
                date: "2013-01-25",
                value: 80,
              },
              {
                date: "2013-01-26",
                value: 87,
              },
              {
                date: "2013-01-27",
                value: 84,
              },
              {
                date: "2013-01-28",
                value: 83,
              },
              {
                date: "2013-01-29",
                value: 84,
              },
              {
                date: "2013-01-30",
                value: 81,
              },
            ],
          },
        },
        {
          title: "Line Chart with Scroll and Zoom",
          type: "line-zoom-h",
          bodyData: {
            colors: ["#57aeff"],
            xAxis: ["date"],
            yAxis: ["visits"],
            data: this.generateChartData(),
          },
        },
        {
          title: "Zoomable on Value Axis",
          type: "line-zoom-v",
          bodyData: {
            colors: ["#57aeff"],
            xAxis: ["date"],
            yAxis: ["value"],
            data: [
              {
                date: "2012-07-27",
                value: 13,
              },
              {
                date: "2012-07-28",
                value: 11,
              },
              {
                date: "2012-07-29",
                value: 15,
              },
              {
                date: "2012-07-30",
                value: 16,
              },
              {
                date: "2012-07-31",
                value: 18,
              },
              {
                date: "2012-08-01",
                value: 13,
              },
              {
                date: "2012-08-02",
                value: 22,
              },
              {
                date: "2012-08-03",
                value: 23,
              },
              {
                date: "2012-08-04",
                value: 20,
              },
              {
                date: "2012-08-05",
                value: 17,
              },
              {
                date: "2012-08-06",
                value: 16,
              },
              {
                date: "2012-08-07",
                value: 18,
              },
              {
                date: "2012-08-08",
                value: 21,
              },
              {
                date: "2012-08-09",
                value: 26,
              },
              {
                date: "2012-08-10",
                value: 24,
              },
              {
                date: "2012-08-11",
                value: 29,
              },
              {
                date: "2012-08-12",
                value: 32,
              },
              {
                date: "2012-08-13",
                value: 18,
              },
              {
                date: "2012-08-14",
                value: 24,
              },
              {
                date: "2012-08-15",
                value: 22,
              },
              {
                date: "2012-08-16",
                value: 18,
              },
              {
                date: "2012-08-17",
                value: 19,
              },
              {
                date: "2012-08-18",
                value: 14,
              },
              {
                date: "2012-08-19",
                value: 15,
              },
              {
                date: "2012-08-20",
                value: 12,
              },
              {
                date: "2012-08-21",
                value: 8,
              },
              {
                date: "2012-08-22",
                value: 9,
              },
              {
                date: "2012-08-23",
                value: 8,
              },
              {
                date: "2012-08-24",
                value: 7,
              },
              {
                date: "2012-08-25",
                value: 5,
              },
              {
                date: "2012-08-26",
                value: 11,
              },
              {
                date: "2012-08-27",
                value: 13,
              },
              {
                date: "2012-08-28",
                value: 18,
              },
              {
                date: "2012-08-29",
                value: 20,
              },
              {
                date: "2012-08-30",
                value: 29,
              },
              {
                date: "2012-08-31",
                value: 33,
              },
              {
                date: "2012-09-01",
                value: 42,
              },
              {
                date: "2012-09-02",
                value: 35,
              },
              {
                date: "2012-09-03",
                value: 31,
              },
              {
                date: "2012-09-04",
                value: 47,
              },
              {
                date: "2012-09-05",
                value: 52,
              },
              {
                date: "2012-09-06",
                value: 46,
              },
              {
                date: "2012-09-07",
                value: 41,
              },
              {
                date: "2012-09-08",
                value: 43,
              },
              {
                date: "2012-09-09",
                value: 40,
              },
              {
                date: "2012-09-10",
                value: 39,
              },
              {
                date: "2012-09-11",
                value: 34,
              },
              {
                date: "2012-09-12",
                value: 29,
              },
              {
                date: "2012-09-13",
                value: 34,
              },
              {
                date: "2012-09-14",
                value: 37,
              },
              {
                date: "2012-09-15",
                value: 42,
              },
              {
                date: "2012-09-16",
                value: 49,
              },
              {
                date: "2012-09-17",
                value: 46,
              },
              {
                date: "2012-09-18",
                value: 47,
              },
              {
                date: "2012-09-19",
                value: 55,
              },
              {
                date: "2012-09-20",
                value: 59,
              },
              {
                date: "2012-09-21",
                value: 58,
              },
              {
                date: "2012-09-22",
                value: 57,
              },
              {
                date: "2012-09-23",
                value: 61,
              },
              {
                date: "2012-09-24",
                value: 59,
              },
              {
                date: "2012-09-25",
                value: 67,
              },
              {
                date: "2012-09-26",
                value: 65,
              },
              {
                date: "2012-09-27",
                value: 61,
              },
              {
                date: "2012-09-28",
                value: 66,
              },
              {
                date: "2012-09-29",
                value: 69,
              },
              {
                date: "2012-09-30",
                value: 71,
              },
              {
                date: "2012-10-01",
                value: 67,
              },
              {
                date: "2012-10-02",
                value: 63,
              },
              {
                date: "2012-10-03",
                value: 46,
              },
              {
                date: "2012-10-04",
                value: 32,
              },
              {
                date: "2012-10-05",
                value: 21,
              },
              {
                date: "2012-10-06",
                value: 18,
              },
              {
                date: "2012-10-07",
                value: 21,
              },
              {
                date: "2012-10-08",
                value: 28,
              },
              {
                date: "2012-10-09",
                value: 27,
              },
              {
                date: "2012-10-10",
                value: 36,
              },
              {
                date: "2012-10-11",
                value: 33,
              },
              {
                date: "2012-10-12",
                value: 31,
              },
              {
                date: "2012-10-13",
                value: 30,
              },
              {
                date: "2012-10-14",
                value: 34,
              },
              {
                date: "2012-10-15",
                value: 38,
              },
              {
                date: "2012-10-16",
                value: 37,
              },
              {
                date: "2012-10-17",
                value: 44,
              },
              {
                date: "2012-10-18",
                value: 49,
              },
              {
                date: "2012-10-19",
                value: 53,
              },
              {
                date: "2012-10-20",
                value: 57,
              },
              {
                date: "2012-10-21",
                value: 60,
              },
              {
                date: "2012-10-22",
                value: 61,
              },
              {
                date: "2012-10-23",
                value: 69,
              },
              {
                date: "2012-10-24",
                value: 67,
              },
              {
                date: "2012-10-25",
                value: 72,
              },
              {
                date: "2012-10-26",
                value: 77,
              },
              {
                date: "2012-10-27",
                value: 75,
              },
              {
                date: "2012-10-28",
                value: 70,
              },
              {
                date: "2012-10-29",
                value: 72,
              },
              {
                date: "2012-10-30",
                value: 70,
              },
              {
                date: "2012-10-31",
                value: 72,
              },
              {
                date: "2012-11-01",
                value: 73,
              },
              {
                date: "2012-11-02",
                value: 67,
              },
              {
                date: "2012-11-03",
                value: 68,
              },
              {
                date: "2012-11-04",
                value: 65,
              },
              {
                date: "2012-11-05",
                value: 71,
              },
              {
                date: "2012-11-06",
                value: 75,
              },
              {
                date: "2012-11-07",
                value: 74,
              },
              {
                date: "2012-11-08",
                value: 71,
              },
              {
                date: "2012-11-09",
                value: 76,
              },
              {
                date: "2012-11-10",
                value: 77,
              },
              {
                date: "2012-11-11",
                value: 81,
              },
              {
                date: "2012-11-12",
                value: 83,
              },
              {
                date: "2012-11-13",
                value: 80,
              },
              {
                date: "2012-11-18",
                value: 80,
              },
              {
                date: "2012-11-19",
                value: 87,
              },
              {
                date: "2012-11-20",
                value: 83,
              },
              {
                date: "2012-11-21",
                value: 85,
              },
              {
                date: "2012-11-22",
                value: 84,
              },
              {
                date: "2012-11-23",
                value: 82,
              },
              {
                date: "2012-11-24",
                value: 73,
              },
              {
                date: "2012-11-25",
                value: 71,
              },
              {
                date: "2012-11-26",
                value: 75,
              },
              {
                date: "2012-11-27",
                value: 79,
              },
              {
                date: "2012-11-28",
                value: 70,
              },
              {
                date: "2012-11-29",
                value: 73,
              },
              {
                date: "2012-11-30",
                value: 61,
              },
              {
                date: "2012-12-01",
                value: 62,
              },
              {
                date: "2012-12-02",
                value: 66,
              },
              {
                date: "2012-12-03",
                value: 65,
              },
              {
                date: "2012-12-04",
                value: 73,
              },
              {
                date: "2012-12-05",
                value: 79,
              },
              {
                date: "2012-12-06",
                value: 78,
              },
              {
                date: "2012-12-07",
                value: 78,
              },
              {
                date: "2012-12-08",
                value: 78,
              },
              {
                date: "2012-12-09",
                value: 74,
              },
              {
                date: "2012-12-10",
                value: 73,
              },
              {
                date: "2012-12-11",
                value: 75,
              },
              {
                date: "2012-12-12",
                value: 70,
              },
              {
                date: "2012-12-13",
                value: 77,
              },
              {
                date: "2012-12-14",
                value: 67,
              },
              {
                date: "2012-12-15",
                value: 62,
              },
              {
                date: "2012-12-16",
                value: 64,
              },
              {
                date: "2012-12-17",
                value: 61,
              },
              {
                date: "2012-12-18",
                value: 59,
              },
              {
                date: "2012-12-19",
                value: 53,
              },
              {
                date: "2012-12-20",
                value: 54,
              },
              {
                date: "2012-12-21",
                value: 56,
              },
              {
                date: "2012-12-22",
                value: 59,
              },
              {
                date: "2012-12-23",
                value: 58,
              },
              {
                date: "2012-12-24",
                value: 55,
              },
              {
                date: "2012-12-25",
                value: 52,
              },
              {
                date: "2012-12-26",
                value: 54,
              },
              {
                date: "2012-12-27",
                value: 50,
              },
              {
                date: "2012-12-28",
                value: 50,
              },
              {
                date: "2012-12-29",
                value: 51,
              },
              {
                date: "2012-12-30",
                value: 52,
              },
              {
                date: "2012-12-31",
                value: 58,
              },
              {
                date: "2013-01-01",
                value: 60,
              },
              {
                date: "2013-01-02",
                value: 67,
              },
              {
                date: "2013-01-03",
                value: 64,
              },
              {
                date: "2013-01-04",
                value: 66,
              },
              {
                date: "2013-01-05",
                value: 60,
              },
              {
                date: "2013-01-06",
                value: 63,
              },
              {
                date: "2013-01-07",
                value: 61,
              },
              {
                date: "2013-01-08",
                value: 60,
              },
              {
                date: "2013-01-09",
                value: 65,
              },
              {
                date: "2013-01-10",
                value: 75,
              },
              {
                date: "2013-01-11",
                value: 77,
              },
              {
                date: "2013-01-12",
                value: 78,
              },
              {
                date: "2013-01-13",
                value: 70,
              },
              {
                date: "2013-01-14",
                value: 70,
              },
              {
                date: "2013-01-15",
                value: 73,
              },
              {
                date: "2013-01-16",
                value: 71,
              },
              {
                date: "2013-01-17",
                value: 74,
              },
              {
                date: "2013-01-18",
                value: 78,
              },
              {
                date: "2013-01-19",
                value: 85,
              },
              {
                date: "2013-01-20",
                value: 82,
              },
              {
                date: "2013-01-21",
                value: 83,
              },
              {
                date: "2013-01-22",
                value: 88,
              },
              {
                date: "2013-01-23",
                value: 85,
              },
              {
                date: "2013-01-24",
                value: 85,
              },
              {
                date: "2013-01-25",
                value: 80,
              },
              {
                date: "2013-01-26",
                value: 87,
              },
              {
                date: "2013-01-27",
                value: 84,
              },
              {
                date: "2013-01-28",
                value: 83,
              },
              {
                date: "2013-01-29",
                value: 84,
              },
              {
                date: "2013-01-30",
                value: 81,
              },
            ],
          },
        },
        {
          title: "Radar Chart",
          type: "radar",
          bodyData: {
            colors: ["#0084ff"],
            labels: ["Sales"],
            xAxis: ["country"],
            yAxis: ["litres"],
            data: [
              {
                country: "Lithuania",
                litres: 501,
              },
              {
                country: "Czechia",
                litres: 301,
              },
              {
                country: "Ireland",
                litres: 266,
              },
              {
                country: "Germany",
                litres: 165,
              },
              {
                country: "Australia",
                litres: 139,
              },
              {
                country: "Austria",
                litres: 336,
              },
              {
                country: "UK",
                litres: 290,
              },
              {
                country: "Belgium",
                litres: 325,
              },
              {
                country: "The Netherlands",
                litres: 40,
              },
            ],
          },
        },
        {
          title: "Polar Scatter",
          type: "polar-scatter",
          bodyData: {
            xAxis: ["year"],
            yAxis: ["europe", "namerica", "asia"],
            data: [
              {
                direction: "N",
                value: 8,
              },
              {
                direction: "NE",
                value: 9,
              },
              {
                direction: "E",
                value: 4.5,
              },
              {
                direction: "SE",
                value: 3.5,
              },
              {
                direction: "S",
                value: 9.2,
              },
              {
                direction: "SW",
                value: 8.4,
              },
              {
                direction: "W",
                value: 11.1,
              },
              {
                direction: "NW",
                value: 10,
              },
            ],
          },
        },
        {
          title: "Polar Chart",
          type: "polar",
          bodyData: {
            colors: ["#e64141", "#00ca00", "#ffd400"],
            xAxis: ["year"],
            yAxis: ["europe", "namerica", "asia"],
            data: [
              {
                direction: "N",
                value: 8,
              },
              {
                direction: "NE",
                value: 9,
              },
              {
                direction: "E",
                value: 4.5,
              },
              {
                direction: "SE",
                value: 3.5,
              },
              {
                direction: "S",
                value: 9.2,
              },
              {
                direction: "SW",
                value: 8.4,
              },
              {
                direction: "W",
                value: 11.1,
              },
              {
                direction: "NW",
                value: 10,
              },
            ],
          },
        },
        {
          title: "3D Pie Chart",
          type: "pie",
          bodyData: {
            colors: [
              "#0084ff",
              "#00ca00",
              "#e64141",
              "#ffd400",
              "#00d0ff",
              "#374948",
            ],
            value: ["litres"],
            category: ["country"],
            data: [
              {
                country: "Lithuania",
                litres: 501.9,
                fill: "red",
              },
              {
                country: "Germany",
                litres: 165.8,
              },
              {
                country: "Australia",
                litres: 139.9,
              },
              {
                country: "Austria",
                litres: 128.3,
              },
              {
                country: "UK",
                litres: 99,
              },
              {
                country: "Belgium",
                litres: 60,
              },
            ],
          },
        },
      ],
    };
  },
};
</script>
