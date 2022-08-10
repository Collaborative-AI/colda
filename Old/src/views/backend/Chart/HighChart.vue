<template>
   <b-container fluid="">
      <b-row>
      <b-col lg="6" v-for="(item,index) in charts" :key="index">
        <card>
          <template v-slot:headerTitle>
            <h4>{{ item.title }}</h4>
          </template>
          <template v-slot:body>
            <HighChart :ref="item.type" :option="item.bodyData"/>
          </template>
        </card>
      </b-col>
    </b-row>
   </b-container>
</template>
<script>
import HighCharts from 'highcharts'
import More from 'highcharts/highcharts-more'
import HighChart from '../../../components/charts/HighChart'
// import { sofbox } from '../../../config/pluginInit'
More(HighCharts)

export default {
  name: 'HighCharts',
  components:{
     HighChart
  },
  mounted () {
  },
  data () {
    return {
      charts: [
        {
          title: 'Basic line Chart',
          bodyData: {
            title: {
              text: 'Solar Employment Growth by Sector, 2010-2016'
            },

            subtitle: {
              text: 'Source: thesolarfoundation.com'
            },

            yAxis: {
              title: {
                text: 'Number of Employees'
              }
            },
            legend: {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'middle'
            },

            plotOptions: {
              series: {
                label: {
                  connectorAllowed: false
                },
                pointStart: 2010
              }
            },

            series: [{
              name: 'Installation',
              data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175],
              color: '#007bff'
            }, {
              name: 'Manufacturing',
              data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434],
              color: '#dc3545'
            }, {
              name: 'Sales & Distribution',
              data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387],
              color: '#28a745'
            }, {
              name: 'Project Development',
              data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227],
              color: '#ffc107'
            }, {
              name: 'Other',
              data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111],
              color: '#17a2b8'
            }],

            responsive: {
              rules: [{
                condition: {
                  maxWidth: 500
                },
                chartOptions: {
                  legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                  }
                }
              }]
            }
          }
        },
        {
          title: 'Column and Bar Chart',
          bodyData: {
            chart: {
              type: 'area'
            },
            accessibility: {
              description: 'Image description: An area chart compares the nuclear stockpiles of the USA and the USSR/Russia between 1945 and 2017. The number of nuclear weapons is plotted on the Y-axis and the years on the X-axis. The chart is interactive, and the year-on-year stockpile levels can be traced for each country. The US has a stockpile of 6 nuclear weapons at the dawn of the nuclear age in 1945. This number has gradually increased to 369 by 1950 when the USSR enters the arms race with 6 weapons. At this point, the US starts to rapidly build its stockpile culminating in 32,040 warheads by 1966 compared to the USSR’s 7,089. From this peak in 1966, the US stockpile gradually decreases as the USSR’s stockpile expands. By 1978 the USSR has closed the nuclear gap at 25,393. The USSR stockpile continues to grow until it reaches a peak of 45,000 in 1986 compared to the US arsenal of 24,401. From 1986, the nuclear stockpiles of both countries start to fall. By 2000, the numbers have fallen to 10,577 and 21,000 for the US and Russia, respectively. The decreases continue until 2017 at which point the US holds 4,018 weapons compared to Russia’s 4,500.'
            },
            title: {
              text: 'US and USSR nuclear stockpiles'
            },
            subtitle: {
              text: 'Sources: <a href="https://thebulletin.org/2006/july/global-nuclear-stockpiles-1945-2006">' +
                'thebulletin.org</a> &amp; <a href="https://www.armscontrol.org/factsheets/Nuclearweaponswhohaswhat">' +
                'armscontrol.org</a>'
            },
            xAxis: {
              allowDecimals: false,
              labels: {
                formatter: function () {
                  return this.value // clean, unformatted number for year
                }
              },
              accessibility: {
                rangeDescription: 'Range: 1940 to 2017.'
              }
            },
            yAxis: {
              title: {
                text: 'Nuclear weapon states'
              },
              labels: {
                formatter: function () {
                  return this.value / 1000 + 'k'
                }
              }
            },
            tooltip: {
              pointFormat: '{series.name} had stockpiled <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
            },
            plotOptions: {
              area: {
                pointStart: 1940,
                marker: {
                  enabled: false,
                  symbol: 'circle',
                  radius: 2,
                  states: {
                    hover: {
                      enabled: true
                    }
                  }
                }
              }
            },
            series: [{
              name: 'USA',
              data: [
                null, null, null, null, null, 6, 11, 32, 110, 235,
                369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468,
                20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342,
                26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
                24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380,
                21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824,
                10577, 10527, 10475, 10421, 10358, 10295, 10104, 9914, 9620, 9326,
                5113, 5113, 4954, 4804, 4761, 4717, 4368, 4018
              ],
              color: '#57aeff'
            }, {
              name: 'USSR/Russia',
              data: [null, null, null, null, null, null, null, null, null, null,
                5, 25, 50, 120, 150, 200, 426, 660, 869, 1060,
                1605, 2471, 3322, 4238, 5221, 6129, 7089, 8339, 9399, 10538,
                11643, 13092, 14478, 15915, 17385, 19055, 21205, 23044, 25393, 27935,
                30062, 32049, 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000,
                37000, 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
                21000, 20000, 19000, 18000, 18000, 17000, 16000, 15537, 14162, 12787,
                12600, 11400, 5500, 4512, 4502, 4502, 4500, 4500
              ],
              color: '#57dc57'
            }]
          }
        },
        {
          title: 'Pie Chart',
          bodyData: {
            chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
            },
            colorAxis: {},
            title: {
              text: 'Browser market shares in January, 2018'
            },
            tooltip: {
              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
              pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                  enabled: true,
                  format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
              }
            },
            series: [{
              name: 'Brands',
              colorByPoint: true,
              data: [{
                name: 'Chrome',
                y: 61.41,
                sliced: true,
                selected: true,
                color: '#0084ff'
              }, {
                name: 'Internet Explorer',
                y: 11.84,
                color: '#00ca00'
              }, {
                name: 'Firefox',
                y: 10.85,
                color: '#e64141'
              }, {
                name: 'Edge',
                y: 4.67,
                color: '#ffd400'
              }, {
                name: 'Safari',
                y: 4.18,
                color: '#00d0ff'
              }, {
                name: 'Sogou Explorer',
                y: 1.64,
                color: '#374948'
              }, {
                name: 'Opera',
                y: 1.6,
                color: '#E9EDF4'
              }, {
                name: 'QQ',
                y: 1.2,
                color: '#777D74'
              }, {
                name: 'Other',
                y: 2.61
              }]
            }]
          }
        },
        {
          title: 'Dynamic Chart',
          bodyData: {
            chart: {
              type: 'spline',
              animation: HighCharts.svg, // don't animate in old IE
              marginRight: 10,
              events: {
                load: function () {
                  // set up the updating of the chart each second
                  var series = this.series[0]
                  setInterval(function () {
                    var x = (new Date()).getTime() // current time
                    var y = Math.random()
                    series.addPoint([x, y], true, true)
                  }, 1000)
                }
              }
            },

            time: {
              useUTC: false
            },

            title: {
              text: 'Live random data'
            },

            accessibility: {
              announceNewData: {
                enabled: true,
                minAnnounceInterval: 15000,
                announcementFormatter: function (allSeries, newSeries, newPoint) {
                  if (newPoint) {
                    return 'New point added. Value: ' + newPoint.y
                  }
                  return false
                }
              }
            },

            xAxis: {
              type: 'datetime',
              tickPixelInterval: 150
            },

            yAxis: {
              title: {
                text: 'Value'
              },
              plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
              }]
            },

            tooltip: {
              headerFormat: '<b>{series.name}</b><br/>',
              pointFormat: '{point.x:%Y-%m-%d %H:%M:%S}<br/>{point.y:.2f}'
            },

            legend: {
              enabled: false
            },

            exporting: {
              enabled: false
            },

            series: [{
              name: 'Random data',
              color: '#0084ff',
              data: (function () {
                // generate an array of random data
                var data = []
                var time = (new Date()).getTime()
                var i

                for (i = -19; i <= 0; i += 1) {
                  data.push({
                    x: time + i * 1000,
                    y: Math.random()
                  })
                }
                return data
              }())
            }]
          }
        },
        {
          type: 'speedometer',
          title: 'Gauges Chart',
          bodyData: {
            chart: {
              type: 'gauge',
              plotBackgroundColor: null,
              plotBackgroundImage: null,
              plotBorderWidth: 0,
              plotShadow: false
            },

            title: {
              text: 'Speedometer'
            },

            pane: {
              startAngle: -150,
              endAngle: 150,
              background: [{
                backgroundColor: {
                  linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                  stops: [
                    [0, '#FFF'],
                    [1, '#333']
                  ]
                },
                borderWidth: 0,
                outerRadius: '109%'
              }, {
                backgroundColor: {
                  linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                  stops: [
                    [0, '#333'],
                    [1, '#FFF']
                  ]
                },
                borderWidth: 1,
                outerRadius: '107%'
              }, {
                // default background
              }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
              }]
            },

            // the value axis
            yAxis: {
              min: 0,
              max: 200,

              minorTickInterval: 'auto',
              minorTickWidth: 1,
              minorTickLength: 10,
              minorTickPosition: 'inside',
              minorTickColor: '#666',

              tickPixelInterval: 30,
              tickWidth: 2,
              tickPosition: 'inside',
              tickLength: 10,
              tickColor: '#666',
              labels: {
                step: 2,
                rotation: 'auto'
              },
              title: {
                text: 'km/h'
              },
              plotBands: [{
                from: 0,
                to: 120,
                color: '#55BF3B' // green
              }, {
                from: 120,
                to: 160,
                color: '#DDDF0D' // yellow
              }, {
                from: 160,
                to: 200,
                color: '#DF5353' // red
              }]
            },

            series: [{
              name: 'Speed',
              data: [80],
              tooltip: {
                valueSuffix: ' km/h'
              }
            }]
          }
        },
        {
          title: 'Area Chart',
          bodyData: {
            chart: {
              type: 'area'
            },
            accessibility: {
              description: 'Image description: An area chart compares the nuclear stockpiles of the USA and the USSR/Russia between 1945 and 2017. The number of nuclear weapons is plotted on the Y-axis and the years on the X-axis. The chart is interactive, and the year-on-year stockpile levels can be traced for each country. The US has a stockpile of 6 nuclear weapons at the dawn of the nuclear age in 1945. This number has gradually increased to 369 by 1950 when the USSR enters the arms race with 6 weapons. At this point, the US starts to rapidly build its stockpile culminating in 32,040 warheads by 1966 compared to the USSR’s 7,089. From this peak in 1966, the US stockpile gradually decreases as the USSR’s stockpile expands. By 1978 the USSR has closed the nuclear gap at 25,393. The USSR stockpile continues to grow until it reaches a peak of 45,000 in 1986 compared to the US arsenal of 24,401. From 1986, the nuclear stockpiles of both countries start to fall. By 2000, the numbers have fallen to 10,577 and 21,000 for the US and Russia, respectively. The decreases continue until 2017 at which point the US holds 4,018 weapons compared to Russia’s 4,500.'
            },
            title: {
              text: 'US and USSR nuclear stockpiles'
            },
            subtitle: {
              text: 'Sources: <a href="https://thebulletin.org/2006/july/global-nuclear-stockpiles-1945-2006">' +
                'thebulletin.org</a> &amp; <a href="https://www.armscontrol.org/factsheets/Nuclearweaponswhohaswhat">' +
                'armscontrol.org</a>'
            },
            xAxis: {
              allowDecimals: false,
              labels: {
                formatter: function () {
                  return this.value // clean, unformatted number for year
                }
              },
              accessibility: {
                rangeDescription: 'Range: 1940 to 2017.'
              }
            },
            yAxis: {
              title: {
                text: 'Nuclear weapon states'
              },
              labels: {
                formatter: function () {
                  return this.value / 1000 + 'k'
                }
              }
            },
            tooltip: {
              pointFormat: '{series.name} had stockpiled <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
            },
            plotOptions: {
              area: {
                pointStart: 1940,
                marker: {
                  enabled: false,
                  symbol: 'circle',
                  radius: 2,
                  states: {
                    hover: {
                      enabled: true
                    }
                  }
                }
              }
            },
            series: [{
              name: 'USA',
              data: [
                null, null, null, null, null, 6, 11, 32, 110, 235,
                369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468,
                20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342,
                26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
                24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380,
                21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824,
                10577, 10527, 10475, 10421, 10358, 10295, 10104, 9914, 9620, 9326,
                5113, 5113, 4954, 4804, 4761, 4717, 4368, 4018
              ],
              color: '#57aeff'
            }, {
              name: 'USSR/Russia',
              data: [null, null, null, null, null, null, null, null, null, null,
                5, 25, 50, 120, 150, 200, 426, 660, 869, 1060,
                1605, 2471, 3322, 4238, 5221, 6129, 7089, 8339, 9399, 10538,
                11643, 13092, 14478, 15915, 17385, 19055, 21205, 23044, 25393, 27935,
                30062, 32049, 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000,
                37000, 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
                21000, 20000, 19000, 18000, 18000, 17000, 16000, 15537, 14162, 12787,
                12600, 11400, 5500, 4512, 4502, 4502, 4500, 4500
              ],
              color: '#57dc57'
            }]
          }
        },
        {
          title: 'Scatter plot Chart',
          bodyData: {
            chart: {
              type: 'scatter',
              zoomType: 'xy'
            },
            accessibility: {
              description: 'A scatter plot compares the height and weight of 507 individuals by gender. Height in centimeters is plotted on the X-axis and weight in kilograms is plotted on the Y-axis. The chart is interactive, and each data point can be hovered over to expose the height and weight data for each individual. The scatter plot is fairly evenly divided by gender with females dominating the left-hand side of the chart and males dominating the right-hand side. The height data for females ranges from 147.2 to 182.9 centimeters with the greatest concentration between 160 and 165 centimeters. The weight data for females ranges from 42 to 105.2 kilograms with the greatest concentration at around 60 kilograms. The height data for males ranges from 157.2 to 198.1 centimeters with the greatest concentration between 175 and 180 centimeters. The weight data for males ranges from 53.9 to 116.4 kilograms with the greatest concentration at around 80 kilograms.'
            },
            title: {
              text: 'Height Versus Weight of 507 Individuals by Gender'
            },
            subtitle: {
              text: 'Source: Heinz  2003'
            },
            xAxis: {
              title: {
                enabled: true,
                text: 'Height (cm)'
              },
              startOnTick: true,
              endOnTick: true,
              showLastLabel: true
            },
            yAxis: {
              title: {
                text: 'Weight (kg)'
              }
            },
            legend: {
              layout: 'vertical',
              align: 'left',
              verticalAlign: 'top',
              x: 100,
              y: 70,
              floating: true,
              borderWidth: 1
            },
            plotOptions: {
              scatter: {
                marker: {
                  radius: 5,
                  states: {
                    hover: {
                      enabled: true,
                      lineColor: 'rgb(100,100,100)'
                    }
                  }
                },
                states: {
                  hover: {
                    marker: {
                      enabled: false
                    }
                  }
                },
                tooltip: {
                  headerFormat: '<b>{series.name}</b><br>',
                  pointFormat: '{point.x} cm, {point.y} kg'
                }
              }
            },
            series: [{
              name: 'Female',
              color: 'rgba(223, 83, 83, .5)',
              data: [[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6],
                [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2],
                [172.7, 62.0], [155.0, 49.2], [156.5, 67.2], [164.0, 53.8], [160.9, 54.4]]
            }, {
              name: 'Male',
              color: 'rgba(119, 152, 191, .5)',
              data: [[174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8],
                [181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6],
                [180.1, 93.0], [175.5, 80.9], [180.6, 72.7], [184.4, 68.0], [175.5, 70.9],
                [180.3, 83.2], [180.3, 83.2]]
            }]
          }
        },
        {
          title: 'Dual axes, line and column Chart',
          bodyData: {
            chart: {
              zoomType: 'xy'
            },
            title: {
              text: 'Average Monthly Temperature and Rainfall in Tokyo'
            },
            subtitle: {
              text: 'Source: WorldClimate.com'
            },
            xAxis: [{
              categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
              crosshair: true
            }],
            yAxis: [{ // Primary yAxis
              labels: {
                format: '{value}°C'
              },
              title: {
                text: 'Temperature'
              }
            }, { // Secondary yAxis
              title: {
                text: 'Rainfall'
              },
              labels: {
                format: '{value} mm'
              },
              opposite: true
            }],
            tooltip: {
              shared: true
            },
            legend: {
              layout: 'vertical',
              align: 'left',
              x: 120,
              verticalAlign: 'top',
              y: 100,
              floating: true,
              backgroundColor: 'rgba(255,255,255,0.25)'
            },
            series: [{
              name: 'Rainfall',
              type: 'column',
              yAxis: 1,
              data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
              color: '#0084ff',
              tooltip: {
                valueSuffix: ' mm'
              }

            }, {
              name: 'Temperature',
              type: 'spline',
              data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
              color: '#00ca00',
              tooltip: {
                valueSuffix: '°C'
              }
            }]
          }
        },
        {
          title: '3D Chart',
          bodyData: {
            chart: {
              renderTo: 'high-3d-chart',
              type: 'column',
              options3d: {
                enabled: true,
                alpha: 15,
                beta: 15,
                depth: 50,
                viewDistance: 25
              }
            },
            title: {
              text: 'Chart rotation demo'
            },
            subtitle: {
              text: 'Test options by dragging the sliders below'
            },
            plotOptions: {
              column: {
                depth: 25
              }
            },
            series: [{
              data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
              color: '#0084ff'
            }]
          }
        },
        {
          title: 'Bar With Nagative Chart',
          bodyData: {
            chart: {
              type: 'bar'
            },
            title: {
              text: 'Population pyramid for Germany, 2018'
            },
            subtitle: {
              text: 'Source: <a href="http://populationpyramid.net/germany/2018/">Population Pyramids of the World from 1950 to 2100</a>'
            },
            accessibility: {
              point: {
                descriptionFormatter: function (point) {
                  var index = point.index + 1
                  var category = point.category
                  var val = Math.abs(point.y)
                  var series = point.series.name

                  return index + ', Age ' + category + ', ' + val + '%. ' + series + '.'
                }
              }
            },
            xAxis: [{
              categories: [
                '0-4', '5-9', '10-14', '15-19',
                '20-24', '25-29', '30-34', '35-39', '40-44',
                '45-49', '50-54', '55-59', '60-64', '65-69',
                '70-74', '75-79', '80-84', '85-89', '90-94',
                '95-99', '100 + '
              ],
              reversed: false,
              labels: {
                step: 1
              },
              accessibility: {
                description: 'Age (male)'
              }
            }, { // mirror axis on right side
              opposite: true,
              reversed: false,
              categories: [
                '0-4', '5-9', '10-14', '15-19',
                '20-24', '25-29', '30-34', '35-39', '40-44',
                '45-49', '50-54', '55-59', '60-64', '65-69',
                '70-74', '75-79', '80-84', '85-89', '90-94',
                '95-99', '100 + '
              ],
              linkedTo: 0,
              labels: {
                step: 1
              },
              accessibility: {
                description: 'Age (female)'
              }
            }],
            yAxis: {
              title: {
                text: null
              },
              labels: {
                formatter: function () {
                  return Math.abs(this.value) + '%'
                }
              },
              accessibility: {
                description: 'Percentage population',
                rangeDescription: 'Range: 0 to 5%'
              }
            },

            plotOptions: {
              series: {
                stacking: 'normal'
              }
            },

            series: [{
              name: 'Male',
              data: [
                -2.2, -2.1, -2.2, -2.4,
                -2.7, -3.0, -3.3, -3.2,
                -2.9, -3.5, -4.4, -4.1,
                -0.0
              ],
              color: '#00ca00'
            }, {
              name: 'Female',
              data: [
                2.1, 2.0, 2.1, 2.3, 2.6,
                2.9, 3.2, 3.1, 2.9, 3.4,
                0.0
              ],
              color: '#0084ff'
            }]
          }
        }
      ]
    }
  }
}
</script>