(function(jQuery) {

    "use strict";

// for apexchart
function apexChartUpdate(chart, detail) {
    let color = getComputedStyle(document.documentElement).getPropertyValue('--dark');
    if (detail.dark) {
      color = getComputedStyle(document.documentElement).getPropertyValue('--white');
    }
    chart.updateOptions({
      chart: {
        foreColor: color
      }
    })
  }
  
// for am chart
function amChartUpdate(chart, detail) {
  // let color = getComputedStyle(document.documentElement).getPropertyValue('--dark');
  if (detail.dark) {
    // color = getComputedStyle(document.documentElement).getPropertyValue('--white');
    chart.stroke = am4core.color(getComputedStyle(document.documentElement).getPropertyValue('--white'));
  }
  chart.validateData();
}

/*---------------------------------------------------------------------
   Apex Charts
-----------------------------------------------------------------------*/
if (jQuery("#apex-basic").length) {
  options = {
    chart: {
      height: 350,
      type: "line",
      zoom: {
        enabled: !1
      }
    },
    colors: ["#4788ff"],
    series: [{
      name: "Desktops",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
    }],
    dataLabels: {
      enabled: !1
    },
    stroke: {
      curve: "straight"
    },
    title: {
      text: "Product Trends by Month",
      align: "left"
    },
    grid: {
      row: {
        colors: ["#f3f3f3", "transparent"],
        opacity: .5
      }
    },
    xaxis: {
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    }
  };
  if(typeof ApexCharts !== typeof undefined){
    (chart = new ApexCharts(document.querySelector("#apex-basic"), options)).render()
    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      apexChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      apexChartUpdate(chart, e.detail)
    })
  }
}
if (jQuery("#apex-line-area").length) {
  options = {
    chart: {
      height: 350,
      type: "area"
    },
    dataLabels: {
      enabled: !1
    },
    stroke: {
      curve: "smooth"
    },
    colors: ["#4788ff", "#ff4b4b"],
    series: [{
      name: "series1",
      data: [31, 40, 28, 51, 42, 109, 100]
    }, {
      name: "series2",
      data: [11, 32, 45, 32, 34, 52, 41]
    }],
    xaxis: {
      type: "datetime",
      categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"]
    },
    tooltip: {
      x: {
        format: "dd/MM/yy HH:mm"
      }
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-line-area"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-bar").length) {
  options = {
    chart: {
      height: 350,
      type: "bar"
    },
    plotOptions: {
      bar: {
        horizontal: !0
      }
    },
    dataLabels: {
      enabled: !1
    },
    colors: ["#4788ff"],
    series: [{
      data: [470, 540, 580, 690, 1100, 1200, 1380]
    }],
    xaxis: {
      categories: ["Netherlands", "Italy", "France", "Japan", "United States", "China", "Germany"]
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-bar"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-column").length) {
  options = {
    chart: {
      height: 350,
      type: "bar"
    },
    plotOptions: {
      bar: {
        horizontal: !1,
        columnWidth: "55%",
        endingShape: "rounded"
      }
    },
    dataLabels: {
      enabled: !1
    },
    stroke: {
      show: !0,
      width: 2,
      colors: ["transparent"]
    },
    colors: ["#4788ff", "#37e6b0", "#ff4b4b"],
    series: [{
      name: "Net Profit",
      data: [44, 55, 57, 56, 61, 58]
    }, {
      name: "Revenue",
      data: [76, 85, 101, 98, 87, 105]
    }, {
      name: "Free Cash Flow",
      data: [35, 41, 36, 26, 45, 48]
    }],
    xaxis: {
      categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    },
    yaxis: {
      title: {
        text: "$ (thousands)"
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function(e) {
          return "$ " + e + " thousands"
        }
      }
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-column"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-mixed-chart").length) {
  options = {
    chart: {
      height: 350,
      type: "line",
      stacked: !1
    },
    stroke: {
      width: [0, 2, 5],
      curve: "smooth"
    },
    plotOptions: {
      bar: {
        columnWidth: "50%"
      }
    },
    colors: ["#ff4b4b", "#37e6b0", "#4788ff"],
    series: [{
      name: "Facebook",
      type: "column",
      data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
    }, {
      name: "Vine",
      type: "area",
      data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43]
    }, {
      name: "Dribbble",
      type: "line",
      data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39]
    }],
    fill: {
      opacity: [.85, .25, 1],
      gradient: {
        inverseColors: !1,
        shade: "light",
        type: "vertical",
        opacityFrom: .85,
        opacityTo: .55,
        stops: [0, 100, 100, 100]
      }
    },
    labels: ["01/01/2003", "02/01/2003", "03/01/2003", "04/01/2003", "05/01/2003", "06/01/2003", "07/01/2003", "08/01/2003", "09/01/2003", "10/01/2003", "11/01/2003"],
    markers: {
      size: 0
    },
    xaxis: {
      type: "datetime"
    },
    yaxis: {
      min: 0
    },
    tooltip: {
      shared: !0,
      intersect: !1,
      y: {
        formatter: function(e) {
          return void 0 !== e ? e.toFixed(0) + " views" : e
        }
      }
    },
    legend: {
      labels: {
        useSeriesColors: !0
      },
      markers: {
        customHTML: [function() {
          return ""
        }, function() {
          return ""
        }, function() {
          return ""
        }]
      }
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-mixed-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-candlestick-chart").length) {
  options = {
    chart: {
      height: 350,
      type: "candlestick"
    },
    colors: ["#4788ff", "#37e6b0", "#37e6b0"],
    series: [{
      data: [{
        x: new Date(15387786e5),
        y: [6629.81, 6650.5, 6623.04, 6633.33]
      }, {
        x: new Date(15387804e5),
        y: [6632.01, 6643.59, 6620, 6630.11]
      }, {
        x: new Date(15387822e5),
        y: [6630.71, 6648.95, 6623.34, 6635.65]
      }, {
        x: new Date(1538784e6),
        y: [6635.65, 6651, 6629.67, 6638.24]
      }, {
        x: new Date(15387858e5),
        y: [6638.24, 6640, 6620, 6624.47]
      }, {
        x: new Date(15387876e5),
        y: [6624.53, 6636.03, 6621.68, 6624.31]
      }, {
        x: new Date(15387894e5),
        y: [6624.61, 6632.2, 6617, 6626.02]
      }, {
        x: new Date(15387912e5),
        y: [6627, 6627.62, 6584.22, 6603.02]
      }, {
        x: new Date(1538793e6),
        y: [6605, 6608.03, 6598.95, 6604.01]
      }, {
        x: new Date(15387948e5),
        y: [6604.5, 6614.4, 6602.26, 6608.02]
      }, {
        x: new Date(15387966e5),
        y: [6608.02, 6610.68, 6601.99, 6608.91]
      }, {
        x: new Date(15387984e5),
        y: [6608.91, 6618.99, 6608.01, 6612]
      }, {
        x: new Date(15388002e5),
        y: [6612, 6615.13, 6605.09, 6612]
      }, {
        x: new Date(1538802e6),
        y: [6612, 6624.12, 6608.43, 6622.95]
      }, {
        x: new Date(15388038e5),
        y: [6623.91, 6623.91, 6615, 6615.67]
      }, {
        x: new Date(15388056e5),
        y: [6618.69, 6618.74, 6610, 6610.4]
      }, {
        x: new Date(15388074e5),
        y: [6611, 6622.78, 6610.4, 6614.9]
      }, {
        x: new Date(15388092e5),
        y: [6614.9, 6626.2, 6613.33, 6623.45]
      }, {
        x: new Date(1538811e6),
        y: [6623.48, 6627, 6618.38, 6620.35]
      }, {
        x: new Date(15388128e5),
        y: [6619.43, 6620.35, 6610.05, 6615.53]
      }, {
        x: new Date(15388146e5),
        y: [6615.53, 6617.93, 6610, 6615.19]
      }, {
        x: new Date(15388164e5),
        y: [6615.19, 6621.6, 6608.2, 6620]
      }, {
        x: new Date(15388182e5),
        y: [6619.54, 6625.17, 6614.15, 6620]
      }, {
        x: new Date(153882e7),
        y: [6620.33, 6634.15, 6617.24, 6624.61]
      }, {
        x: new Date(15388218e5),
        y: [6625.95, 6626, 6611.66, 6617.58]
      }, {
        x: new Date(15388236e5),
        y: [6619, 6625.97, 6595.27, 6598.86]
      }, {
        x: new Date(15388254e5),
        y: [6598.86, 6598.88, 6570, 6587.16]
      }, {
        x: new Date(15388272e5),
        y: [6588.86, 6600, 6580, 6593.4]
      }, {
        x: new Date(1538829e6),
        y: [6593.99, 6598.89, 6585, 6587.81]
      }, {
        x: new Date(15388308e5),
        y: [6587.81, 6592.73, 6567.14, 6578]
      }, {
        x: new Date(15388326e5),
        y: [6578.35, 6581.72, 6567.39, 6579]
      }, {
        x: new Date(15388344e5),
        y: [6579.38, 6580.92, 6566.77, 6575.96]
      }, {
        x: new Date(15388362e5),
        y: [6575.96, 6589, 6571.77, 6588.92]
      }, {
        x: new Date(1538838e6),
        y: [6588.92, 6594, 6577.55, 6589.22]
      }, {
        x: new Date(15388398e5),
        y: [6589.3, 6598.89, 6589.1, 6596.08]
      }, {
        x: new Date(15388416e5),
        y: [6597.5, 6600, 6588.39, 6596.25]
      }, {
        x: new Date(15388434e5),
        y: [6598.03, 6600, 6588.73, 6595.97]
      }, {
        x: new Date(15388452e5),
        y: [6595.97, 6602.01, 6588.17, 6602]
      }, {
        x: new Date(1538847e6),
        y: [6602, 6607, 6596.51, 6599.95]
      }, {
        x: new Date(15388488e5),
        y: [6600.63, 6601.21, 6590.39, 6591.02]
      }, {
        x: new Date(15388506e5),
        y: [6591.02, 6603.08, 6591, 6591]
      }, {
        x: new Date(15388524e5),
        y: [6591, 6601.32, 6585, 6592]
      }, {
        x: new Date(15388542e5),
        y: [6593.13, 6596.01, 6590, 6593.34]
      }, {
        x: new Date(1538856e6),
        y: [6593.34, 6604.76, 6582.63, 6593.86]
      }, {
        x: new Date(15388578e5),
        y: [6593.86, 6604.28, 6586.57, 6600.01]
      }, {
        x: new Date(15388596e5),
        y: [6601.81, 6603.21, 6592.78, 6596.25]
      }, {
        x: new Date(15388614e5),
        y: [6596.25, 6604.2, 6590, 6602.99]
      }, {
        x: new Date(15388632e5),
        y: [6602.99, 6606, 6584.99, 6587.81]
      }, {
        x: new Date(1538865e6),
        y: [6587.81, 6595, 6583.27, 6591.96]
      }, {
        x: new Date(15388668e5),
        y: [6591.97, 6596.07, 6585, 6588.39]
      }, {
        x: new Date(15388686e5),
        y: [6587.6, 6598.21, 6587.6, 6594.27]
      }, {
        x: new Date(15388704e5),
        y: [6596.44, 6601, 6590, 6596.55]
      }, {
        x: new Date(15388722e5),
        y: [6598.91, 6605, 6596.61, 6600.02]
      }, {
        x: new Date(1538874e6),
        y: [6600.55, 6605, 6589.14, 6593.01]
      }, {
        x: new Date(15388758e5),
        y: [6593.15, 6605, 6592, 6603.06]
      }]
    }],
    title: {
      text: "CandleStick Chart",
      align: "left"
    },
    xaxis: {
      type: "datetime"
    },
    yaxis: {
      tooltip: {
        enabled: !0
      }
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-candlestick-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-bubble-chart").length) {
  function generateData(e, t, a) {
    for (var n = 0, o = []; n < t;) {
      var r = Math.floor(Math.random() * (a.max - a.min + 1)) + a.min,
        i = Math.floor(61 * Math.random()) + 15;
      o.push([e, r, i]), e += 864e5, n++
    }
    return o
  }
  options = {
    chart: {
      height: 350,
      type: "bubble"
    },
    dataLabels: {
      enabled: !1
    },
    series: [{
      name: "Product1",
      data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
        min: 10,
        max: 40
      })
    }, {
      name: "Product2",
      data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
        min: 10,
        max: 40
      })
    }, {
      name: "Product3",
      data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
        min: 10,
        max: 40
      })
    }],
    fill: {
      type: "gradient"
    },
    colors: ["#4788ff", "#37e6b0", "#37e6b0"],
    title: {
      text: "3D Bubble Chart"
    },
    xaxis: {
      tickAmount: 12,
      type: "datetime",
      labels: {
        rotate: 0
      }
    },
    yaxis: {
      max: 40
    },
    theme: {
      palette: "palette2"
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-bubble-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-scatter-chart").length) {
  options = {
    chart: {
      height: 350,
      type: "scatter",
      zoom: {
        enabled: !0,
        type: "xy"
      }
    },
    colors: ["#4788ff", "#ff4b4b", "#37e6b0"],
    series: [{
      name: "SAMPLE A",
      data: [
        [16.4, 5.4],
        [21.7, 2],
        [10.9, 0],
        [10.9, 8.2],
        [16.4, 0],
        [16.4, 1.8],
        [13.6, .3],
        [13.6, 0],
        [29.9, 0],
        [27.1, 2.3],
        [16.4, 0],
        [13.6, 3.7],
        [10.9, 5.2],
        [16.4, 6.5],
        [10.9, 0],
        [24.5, 7.1],
        [10.9, 0],
        [8.1, 4.7]
      ]
    }, {
      name: "SAMPLE B",
      data: [
        [36.4, 13.4],
        [1.7, 11],
        [1.9, 9],
        [1.9, 13.2],
        [1.4, 7],
        [6.4, 8.8],
        [3.6, 4.3],
        [1.6, 10],
        [9.9, 2],
        [7.1, 15],
        [1.4, 0],
        [3.6, 13.7],
        [1.9, 15.2],
        [6.4, 16.5],
        [.9, 10],
        [4.5, 17.1],
        [10.9, 10],
        [.1, 14.7]
      ]
    }, {
      name: "SAMPLE C",
      data: [
        [21.7, 3],
        [23.6, 3.5],
        [28, 4],
        [27.1, .3],
        [16.4, 4],
        [13.6, 0],
        [19, 5],
        [22.4, 3],
        [24.5, 3],
        [32.6, 3],
        [27.1, 4],
        [29.6, 6],
        [31.6, 8],
        [21.6, 5],
        [20.9, 4],
        [22.4, 0],
        [32.6, 10.3],
        [29.7, 20.8]
      ]
    }],
    xaxis: {
      tickAmount: 5,
      labels: {
        formatter: function(e) {
          return parseFloat(e).toFixed(1)
        }
      }
    },
    yaxis: {
      tickAmount: 5
    }
  };
  (chart = new ApexCharts(document.querySelector("#apex-scatter-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-radialbar-chart").length) {
  options = {
    chart: {
      height: 350,
      type: "radialBar"
    },
    plotOptions: {
      radialBar: {
        dataLabels: {
          name: {
            fontSize: "22px"
          },
          value: {
            fontSize: "16px"
          },
          total: {
            show: !0,
            label: "Total",
            formatter: function(e) {
              return 249
            }
          }
        }
      }
    },
    series: [44, 55, 67, 83],
    labels: ["Apples", "Oranges", "Bananas", "Berries"],
    colors: ["#4788ff", "#ff4b4b", "#876cfe", "#37e6b0"]
  };
  (chart = new ApexCharts(document.querySelector("#apex-radialbar-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#apex-pie-chart").length) {
  options = {
    chart: {
      width: 380,
      type: "pie"
    },
    labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
    series: [44, 55, 13, 43, 22],
    colors: ["#4788ff", "#ff4b4b", "#876cfe", "#37e6b0", "#c8c8c8"],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: "bottom"
        }
      }
    }]
  };
  (chart = new ApexCharts(document.querySelector("#apex-pie-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#advanced-chart").length) {
  var options = {
    series: [
    {
      name: 'Bob',
      data: [
        {
          x: 'Design',
          y: [
            new Date('2019-03-05').getTime(),
            new Date('2019-03-08').getTime()
          ]
        },
        {
          x: 'Code',
          y: [
            new Date('2019-03-02').getTime(),
            new Date('2019-03-05').getTime()
          ]
        },
        {
          x: 'Code',
          y: [
            new Date('2019-03-05').getTime(),
            new Date('2019-03-07').getTime()
          ]
        },
        {
          x: 'Test',
          y: [
            new Date('2019-03-03').getTime(),
            new Date('2019-03-09').getTime()
          ]
        },
        {
          x: 'Test',
          y: [
            new Date('2019-03-08').getTime(),
            new Date('2019-03-11').getTime()
          ]
        },
        {
          x: 'Validation',
          y: [
            new Date('2019-03-11').getTime(),
            new Date('2019-03-16').getTime()
          ]
        },
        {
          x: 'Design',
          y: [
            new Date('2019-03-01').getTime(),
            new Date('2019-03-03').getTime()
          ]
        }
      ]
    },
    {
      name: 'Joe',
      data: [
        {
          x: 'Design',
          y: [
            new Date('2019-03-02').getTime(),
            new Date('2019-03-05').getTime()
          ]
        },
        {
          x: 'Test',
          y: [
            new Date('2019-03-06').getTime(),
            new Date('2019-03-16').getTime()
          ]
        },
        {
          x: 'Code',
          y: [
            new Date('2019-03-03').getTime(),
            new Date('2019-03-07').getTime()
          ]
        },
        {
          x: 'Deployment',
          y: [
            new Date('2019-03-20').getTime(),
            new Date('2019-03-22').getTime()
          ]
        },
        {
          x: 'Design',
          y: [
            new Date('2019-03-10').getTime(),
            new Date('2019-03-16').getTime()
          ]
        }
      ]
    },
    {
      name: 'Dan',
      data: [
        {
          x: 'Code',
          y: [
            new Date('2019-03-10').getTime(),
            new Date('2019-03-17').getTime()
          ]
        },
        {
          x: 'Validation',
          y: [
            new Date('2019-03-05').getTime(),
            new Date('2019-03-09').getTime()
          ]
        },
      ]
    }
  ],
    colors: ["#4788ff", "#ff4b4b", "#37e6b0"],
    chart: {
    height: 450,
    type: 'rangeBar'
  },
  plotOptions: {
    bar: {
      horizontal: true,
      barHeight: '80%'
    }
  },
  xaxis: {
    type: 'datetime'
  },
  stroke: {
    width: 1
  },
  fill: {
    type: 'solid',
    opacity: 0.6
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left'
  }
  };

  (chart = new ApexCharts(document.querySelector("#advanced-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#radar-multiple-chart").length) {
  var options = {
    series: [{
    name: 'Series 1',
    data: [80, 50, 30, 40, 100, 20],
  }, {
    name: 'Series 2',
    data: [20, 30, 40, 80, 20, 80],
  }, {
    name: 'Series 3',
    data: [44, 76, 78, 13, 43, 10],
  }],
  colors: ["#4788ff", "#ff4b4b", "#37e6b0"],
    chart: {
    height: 350,
    type: 'radar',
    dropShadow: {
      enabled: true,
      blur: 1,
      left: 1,
      top: 1
    }
  },
  title: {
    text: 'Radar Chart - Multi Series'
  },
  stroke: {
    width: 2
  },
  fill: {
    opacity: 0.1
  },
  markers: {
    size: 0
  },
  xaxis: {
    categories: ['2011', '2012', '2013', '2014', '2015', '2016']
  }
  };

  (chart = new ApexCharts(document.querySelector("#radar-multiple-chart"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}



/*---------------------------------------------------------------------
   Am Charts
-----------------------------------------------------------------------*/

    if(jQuery('#am-simple-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-simple-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#4788ff"),];

      // Add data
      chart.data = [{
        "country": "USA",
        "visits": 2025
      }, {
        "country": "China",
        "visits": 1882
      }, {
        "country": "Japan",
        "visits": 1809
      }, {
        "country": "Germany",
        "visits": 1322
      }, {
        "country": "UK",
        "visits": 1122
      }, {
        "country": "France",
        "visits": 1114
      }];

      // Create axes

      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "country";
      categoryAxis.renderer.grid.template.location = 0;
      categoryAxis.renderer.minGridDistance = 30;

      categoryAxis.renderer.labels.template.adapter.add("dy", function(dy, target) {
        if (target.dataItem && target.dataItem.index & 2 == 2) {
          return dy + 25;
        }
        return dy;
      });

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      // Create series
      var series = chart.series.push(new am4charts.ColumnSeries());
      series.dataFields.valueY = "visits";
      series.dataFields.categoryX = "country";
      series.name = "Visits";
      series.columns.template.tooltipText = "{categoryX}: [bold]{valueY}[/]";
      series.columns.template.fillOpacity = .8;

      var columnTemplate = series.columns.template;
      columnTemplate.strokeWidth = 2;
      columnTemplate.strokeOpacity = 1;

      const body = document.querySelector('body')
      if (body.classList.contains('dark')) {
        amChartUpdate(chart, {
          dark: true
        })
      }

      document.addEventListener('ChangeColorMode', function (e) {
        amChartUpdate(chart, e.detail)
      })

      }); // end am4core.ready()
   }

   if(jQuery('#am-columnlinr-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-columnlinr-chart", am4charts.XYChart);
       chart.colors.list = [am4core.color("#4788ff"),];

      // Export
      chart.exporting.menu = new am4core.ExportMenu();

      // Data for both series
      var data = [ {
        "year": "2009",
        "income": 23.5,
        "expenses": 21.1
      }, {
        "year": "2010",
        "income": 26.2,
        "expenses": 30.5
      }, {
        "year": "2011",
        "income": 30.1,
        "expenses": 34.9
      }, {
        "year": "2012",
        "income": 29.5,
        "expenses": 31.1
      }, {
        "year": "2013",
        "income": 30.6,
        "expenses": 28.2,
        "lineDash": "5,5",
      }, {
        "year": "2014",
        "income": 34.1,
        "expenses": 32.9,
        "strokeWidth": 1,
        "columnDash": "5,5",
        "fillOpacity": 0.2,
        "additional": "(projection)"
      } ];

      /* Create axes */
      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "year";
      categoryAxis.renderer.minGridDistance = 30;

      /* Create value axis */
      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      /* Create series */
      var columnSeries = chart.series.push(new am4charts.ColumnSeries());
      columnSeries.name = "Income";
      columnSeries.dataFields.valueY = "income";
      columnSeries.dataFields.categoryX = "year";

      columnSeries.columns.template.tooltipText = "[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]"
      columnSeries.columns.template.propertyFields.fillOpacity = "fillOpacity";
      columnSeries.columns.template.propertyFields.stroke = "stroke";
      columnSeries.columns.template.propertyFields.strokeWidth = "strokeWidth";
      columnSeries.columns.template.propertyFields.strokeDasharray = "columnDash";
      columnSeries.tooltip.label.textAlign = "middle";

      var lineSeries = chart.series.push(new am4charts.LineSeries());
      lineSeries.name = "Expenses";
      lineSeries.dataFields.valueY = "expenses";
      lineSeries.dataFields.categoryX = "year";

      lineSeries.stroke = am4core.color("#4788ff");
      lineSeries.strokeWidth = 3;
      lineSeries.propertyFields.strokeDasharray = "lineDash";
      lineSeries.tooltip.label.textAlign = "middle";

      var bullet = lineSeries.bullets.push(new am4charts.Bullet());
      bullet.fill = am4core.color("#fdd400"); // tooltips grab fill from parent by default
      bullet.tooltipText = "[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]"
      var circle = bullet.createChild(am4core.Circle);
      circle.radius = 4;
      circle.fill = am4core.color("#fff");
      circle.strokeWidth = 3;

      chart.data = data;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      });
   }

   if(jQuery('#am-stackedcolumn-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-stackedcolumn-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#ff4b4b"),
      am4core.color("#37e6b0"),
      am4core.color("#fe721c")];


      // Add data
      chart.data = [{
        "year": "2016",
        "europe": 2.5,
        "namerica": 2.5,
        "asia": 2.1,
        "lamerica": 0.3,
        "meast": 0.2
      }, {
        "year": "2017",
        "europe": 2.6,
        "namerica": 2.7,
        "asia": 2.2,
        "lamerica": 0.3,
        "meast": 0.3
      }, {
        "year": "2018",
        "europe": 2.8,
        "namerica": 2.9,
        "asia": 2.4,
        "lamerica": 0.3,
        "meast": 0.3
      }];

      // Create axes
      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "year";
      categoryAxis.renderer.grid.template.location = 0;


      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      valueAxis.renderer.inside = true;
      valueAxis.renderer.labels.template.disabled = true;
      valueAxis.min = 0;

      // Create series
      function createSeries(field, name) {

        // Set up series
        var series = chart.series.push(new am4charts.ColumnSeries());
        series.name = name;
        series.dataFields.valueY = field;
        series.dataFields.categoryX = "year";
        series.sequencedInterpolation = true;

        // Make it stacked
        series.stacked = true;

        // Configure columns
        series.columns.template.width = am4core.percent(60);
        series.columns.template.tooltipText = "[bold]{name}[/]\n[font-size:14px]{categoryX}: {valueY}";

        // Add label
        var labelBullet = series.bullets.push(new am4charts.LabelBullet());
        labelBullet.label.text = "{valueY}";
        labelBullet.locationY = 0.5;

        return series;
      }

      createSeries("europe", "Europe");
      createSeries("namerica", "North America");
      createSeries("asia", "Asia-Pacific");

      // Legend
      chart.legend = new am4charts.Legend();

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }

   if(jQuery('#am-barline-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      var chart = am4core.create("am-barline-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#4788ff"),
      am4core.color("#37e6b0")];

      chart.data = [{
              "year": "2005",
              "income": 23.5,
              "expenses": 18.1
          }, {
              "year": "2006",
              "income": 26.2,
              "expenses": 22.8
          }, {
              "year": "2007",
              "income": 30.1,
              "expenses": 23.9
          }, {
              "year": "2008",
              "income": 29.5,
              "expenses": 25.1
          }, {
              "year": "2009",
              "income": 24.6,
              "expenses": 25
          }];

      //create category axis for years
      var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "year";
      categoryAxis.renderer.inversed = true;
      categoryAxis.renderer.grid.template.location = 0;

      //create value axis for income and expenses
      var valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
      valueAxis.renderer.opposite = true;


      //create columns
      var series = chart.series.push(new am4charts.ColumnSeries());
      series.dataFields.categoryY = "year";
      series.dataFields.valueX = "income";
      series.name = "Income";
      series.columns.template.fillOpacity = 0.5;
      series.columns.template.strokeOpacity = 0;
      series.tooltipText = "Income in {categoryY}: {valueX.value}";

      //create line
      var lineSeries = chart.series.push(new am4charts.LineSeries());
      lineSeries.dataFields.categoryY = "year";
      lineSeries.dataFields.valueX = "expenses";
      lineSeries.name = "Expenses";
      lineSeries.strokeWidth = 3;
      lineSeries.tooltipText = "Expenses in {categoryY}: {valueX.value}";

      //add bullets
      var circleBullet = lineSeries.bullets.push(new am4charts.CircleBullet());
      circleBullet.circle.fill = am4core.color("#fff");
      circleBullet.circle.strokeWidth = 2;

      //add chart cursor
      chart.cursor = new am4charts.XYCursor();
      chart.cursor.behavior = "zoomY";

      //add legend
      chart.legend = new am4charts.Legend();

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }

   if(jQuery('#am-datedata-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-datedata-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#57aeff")];

      // Add data
      chart.data = [{
        "date": "2012-07-27",
        "value": 13
      }, {
        "date": "2012-07-28",
        "value": 11
      }, {
        "date": "2012-07-29",
        "value": 15
      }, {
        "date": "2012-07-30",
        "value": 16
      }, {
        "date": "2012-07-31",
        "value": 18
      }, {
        "date": "2012-08-01",
        "value": 13
      }, {
        "date": "2012-08-02",
        "value": 22
      }, {
        "date": "2012-08-03",
        "value": 23
      }, {
        "date": "2012-08-04",
        "value": 20
      }, {
        "date": "2012-08-05",
        "value": 17
      }, {
        "date": "2012-08-06",
        "value": 16
      }, {
        "date": "2012-08-07",
        "value": 18
      }, {
        "date": "2012-08-08",
        "value": 21
      }, {
        "date": "2012-08-09",
        "value": 26
      }, {
        "date": "2012-08-10",
        "value": 24
      }, {
        "date": "2012-08-11",
        "value": 29
      }, {
        "date": "2012-08-12",
        "value": 32
      }, {
        "date": "2012-08-13",
        "value": 18
      }, {
        "date": "2012-08-14",
        "value": 24
      }, {
        "date": "2012-08-15",
        "value": 22
      }, {
        "date": "2012-08-16",
        "value": 18
      }, {
        "date": "2012-08-17",
        "value": 19
      }, {
        "date": "2012-08-18",
        "value": 14
      }, {
        "date": "2012-08-19",
        "value": 15
      }, {
        "date": "2012-08-20",
        "value": 12
      }, {
        "date": "2012-08-21",
        "value": 8
      }, {
        "date": "2012-08-22",
        "value": 9
      }, {
        "date": "2012-08-23",
        "value": 8
      }, {
        "date": "2012-08-24",
        "value": 7
      }, {
        "date": "2012-08-25",
        "value": 5
      }, {
        "date": "2012-08-26",
        "value": 11
      }, {
        "date": "2012-08-27",
        "value": 13
      }, {
        "date": "2012-08-28",
        "value": 18
      }, {
        "date": "2012-08-29",
        "value": 20
      }, {
        "date": "2012-08-30",
        "value": 29
      }, {
        "date": "2012-08-31",
        "value": 33
      }, {
        "date": "2012-09-01",
        "value": 42
      }, {
        "date": "2012-09-02",
        "value": 35
      }, {
        "date": "2012-09-03",
        "value": 31
      }, {
        "date": "2012-09-04",
        "value": 47
      }, {
        "date": "2012-09-05",
        "value": 52
      }, {
        "date": "2012-09-06",
        "value": 46
      }, {
        "date": "2012-09-07",
        "value": 41
      }, {
        "date": "2012-09-08",
        "value": 43
      }, {
        "date": "2012-09-09",
        "value": 40
      }, {
        "date": "2012-09-10",
        "value": 39
      }, {
        "date": "2012-09-11",
        "value": 34
      }, {
        "date": "2012-09-12",
        "value": 29
      }, {
        "date": "2012-09-13",
        "value": 34
      }, {
        "date": "2012-09-14",
        "value": 37
      }, {
        "date": "2012-09-15",
        "value": 42
      }, {
        "date": "2012-09-16",
        "value": 49
      }, {
        "date": "2012-09-17",
        "value": 46
      }, {
        "date": "2012-09-18",
        "value": 47
      }, {
        "date": "2012-09-19",
        "value": 55
      }, {
        "date": "2012-09-20",
        "value": 59
      }, {
        "date": "2012-09-21",
        "value": 58
      }, {
        "date": "2012-09-22",
        "value": 57
      }, {
        "date": "2012-09-23",
        "value": 61
      }, {
        "date": "2012-09-24",
        "value": 59
      }, {
        "date": "2012-09-25",
        "value": 67
      }, {
        "date": "2012-09-26",
        "value": 65
      }, {
        "date": "2012-09-27",
        "value": 61
      }, {
        "date": "2012-09-28",
        "value": 66
      }, {
        "date": "2012-09-29",
        "value": 69
      }, {
        "date": "2012-09-30",
        "value": 71
      }, {
        "date": "2012-10-01",
        "value": 67
      }, {
        "date": "2012-10-02",
        "value": 63
      }, {
        "date": "2012-10-03",
        "value": 46
      }, {
        "date": "2012-10-04",
        "value": 32
      }, {
        "date": "2012-10-05",
        "value": 21
      }, {
        "date": "2012-10-06",
        "value": 18
      }, {
        "date": "2012-10-07",
        "value": 21
      }, {
        "date": "2012-10-08",
        "value": 28
      }, {
        "date": "2012-10-09",
        "value": 27
      }, {
        "date": "2012-10-10",
        "value": 36
      }, {
        "date": "2012-10-11",
        "value": 33
      }, {
        "date": "2012-10-12",
        "value": 31
      }, {
        "date": "2012-10-13",
        "value": 30
      }, {
        "date": "2012-10-14",
        "value": 34
      }, {
        "date": "2012-10-15",
        "value": 38
      }, {
        "date": "2012-10-16",
        "value": 37
      }, {
        "date": "2012-10-17",
        "value": 44
      }, {
        "date": "2012-10-18",
        "value": 49
      }, {
        "date": "2012-10-19",
        "value": 53
      }, {
        "date": "2012-10-20",
        "value": 57
      }, {
        "date": "2012-10-21",
        "value": 60
      }, {
        "date": "2012-10-22",
        "value": 61
      }, {
        "date": "2012-10-23",
        "value": 69
      }, {
        "date": "2012-10-24",
        "value": 67
      }, {
        "date": "2012-10-25",
        "value": 72
      }, {
        "date": "2012-10-26",
        "value": 77
      }, {
        "date": "2012-10-27",
        "value": 75
      }, {
        "date": "2012-10-28",
        "value": 70
      }, {
        "date": "2012-10-29",
        "value": 72
      }, {
        "date": "2012-10-30",
        "value": 70
      }, {
        "date": "2012-10-31",
        "value": 72
      }, {
        "date": "2012-11-01",
        "value": 73
      }, {
        "date": "2012-11-02",
        "value": 67
      }, {
        "date": "2012-11-03",
        "value": 68
      }, {
        "date": "2012-11-04",
        "value": 65
      }, {
        "date": "2012-11-05",
        "value": 71
      }, {
        "date": "2012-11-06",
        "value": 75
      }, {
        "date": "2012-11-07",
        "value": 74
      }, {
        "date": "2012-11-08",
        "value": 71
      }, {
        "date": "2012-11-09",
        "value": 76
      }, {
        "date": "2012-11-10",
        "value": 77
      }, {
        "date": "2012-11-11",
        "value": 81
      }, {
        "date": "2012-11-12",
        "value": 83
      }, {
        "date": "2012-11-13",
        "value": 80
      }, {
        "date": "2012-11-14",
        "value": 81
      }, {
        "date": "2012-11-15",
        "value": 87
      }, {
        "date": "2012-11-16",
        "value": 82
      }, {
        "date": "2012-11-17",
        "value": 86
      }, {
        "date": "2012-11-18",
        "value": 80
      }, {
        "date": "2012-11-19",
        "value": 87
      }, {
        "date": "2012-11-20",
        "value": 83
      }, {
        "date": "2012-11-21",
        "value": 85
      }, {
        "date": "2012-11-22",
        "value": 84
      }, {
        "date": "2012-11-23",
        "value": 82
      }, {
        "date": "2012-11-24",
        "value": 73
      }, {
        "date": "2012-11-25",
        "value": 71
      }, {
        "date": "2012-11-26",
        "value": 75
      }, {
        "date": "2012-11-27",
        "value": 79
      }, {
        "date": "2012-11-28",
        "value": 70
      }, {
        "date": "2012-11-29",
        "value": 73
      }, {
        "date": "2012-11-30",
        "value": 61
      }, {
        "date": "2012-12-01",
        "value": 62
      }, {
        "date": "2012-12-02",
        "value": 66
      }, {
        "date": "2012-12-03",
        "value": 65
      }, {
        "date": "2012-12-04",
        "value": 73
      }, {
        "date": "2012-12-05",
        "value": 79
      }, {
        "date": "2012-12-06",
        "value": 78
      }, {
        "date": "2012-12-07",
        "value": 78
      }, {
        "date": "2012-12-08",
        "value": 78
      }, {
        "date": "2012-12-09",
        "value": 74
      }, {
        "date": "2012-12-10",
        "value": 73
      }, {
        "date": "2012-12-11",
        "value": 75
      }, {
        "date": "2012-12-12",
        "value": 70
      }, {
        "date": "2012-12-13",
        "value": 77
      }, {
        "date": "2012-12-14",
        "value": 67
      }, {
        "date": "2012-12-15",
        "value": 62
      }, {
        "date": "2012-12-16",
        "value": 64
      }, {
        "date": "2012-12-17",
        "value": 61
      }, {
        "date": "2012-12-18",
        "value": 59
      }, {
        "date": "2012-12-19",
        "value": 53
      }, {
        "date": "2012-12-20",
        "value": 54
      }, {
        "date": "2012-12-21",
        "value": 56
      }, {
        "date": "2012-12-22",
        "value": 59
      }, {
        "date": "2012-12-23",
        "value": 58
      }, {
        "date": "2012-12-24",
        "value": 55
      }, {
        "date": "2012-12-25",
        "value": 52
      }, {
        "date": "2012-12-26",
        "value": 54
      }, {
        "date": "2012-12-27",
        "value": 50
      }, {
        "date": "2012-12-28",
        "value": 50
      }, {
        "date": "2012-12-29",
        "value": 51
      }, {
        "date": "2012-12-30",
        "value": 52
      }, {
        "date": "2012-12-31",
        "value": 58
      }, {
        "date": "2013-01-01",
        "value": 60
      }, {
        "date": "2013-01-02",
        "value": 67
      }, {
        "date": "2013-01-03",
        "value": 64
      }, {
        "date": "2013-01-04",
        "value": 66
      }, {
        "date": "2013-01-05",
        "value": 60
      }, {
        "date": "2013-01-06",
        "value": 63
      }, {
        "date": "2013-01-07",
        "value": 61
      }, {
        "date": "2013-01-08",
        "value": 60
      }, {
        "date": "2013-01-09",
        "value": 65
      }, {
        "date": "2013-01-10",
        "value": 75
      }, {
        "date": "2013-01-11",
        "value": 77
      }, {
        "date": "2013-01-12",
        "value": 78
      }, {
        "date": "2013-01-13",
        "value": 70
      }, {
        "date": "2013-01-14",
        "value": 70
      }, {
        "date": "2013-01-15",
        "value": 73
      }, {
        "date": "2013-01-16",
        "value": 71
      }, {
        "date": "2013-01-17",
        "value": 74
      }, {
        "date": "2013-01-18",
        "value": 78
      }, {
        "date": "2013-01-19",
        "value": 85
      }, {
        "date": "2013-01-20",
        "value": 82
      }, {
        "date": "2013-01-21",
        "value": 83
      }, {
        "date": "2013-01-22",
        "value": 88
      }, {
        "date": "2013-01-23",
        "value": 85
      }, {
        "date": "2013-01-24",
        "value": 85
      }, {
        "date": "2013-01-25",
        "value": 80
      }, {
        "date": "2013-01-26",
        "value": 87
      }, {
        "date": "2013-01-27",
        "value": 84
      }, {
        "date": "2013-01-28",
        "value": 83
      }, {
        "date": "2013-01-29",
        "value": 84
      }, {
        "date": "2013-01-30",
        "value": 81
      }];

      // Set input format for the dates
      chart.dateFormatter.inputDateFormat = "yyyy-MM-dd";

      // Create axes
      var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      // Create series
      var series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.valueY = "value";
      series.dataFields.dateX = "date";
      series.tooltipText = "{value}"
      series.strokeWidth = 2;
      series.minBulletDistance = 15;

      // Drop-shaped tooltips
      series.tooltip.background.cornerRadius = 20;
      series.tooltip.background.strokeOpacity = 0;
      series.tooltip.pointerOrientation = "vertical";
      series.tooltip.label.minWidth = 40;
      series.tooltip.label.minHeight = 40;
      series.tooltip.label.textAlign = "middle";
      series.tooltip.label.textValign = "middle";

      // Make bullets grow on hover
      var bullet = series.bullets.push(new am4charts.CircleBullet());
      bullet.circle.strokeWidth = 2;
      bullet.circle.radius = 4;
      bullet.circle.fill = am4core.color("#fff");

      var bullethover = bullet.states.create("hover");
      bullethover.properties.scale = 1.3;

      // Make a panning cursor
      chart.cursor = new am4charts.XYCursor();
      chart.cursor.behavior = "panXY";
      chart.cursor.xAxis = dateAxis;
      chart.cursor.snapToSeries = series;

      // Create vertical scrollbar and place it before the value axis
      chart.scrollbarY = new am4core.Scrollbar();
      chart.scrollbarY.parent = chart.leftAxesContainer;
      chart.scrollbarY.toBack();

      // Create a horizontal scrollbar with previe and place it underneath the date axis
      chart.scrollbarX = new am4charts.XYChartScrollbar();
      chart.scrollbarX.series.push(series);
      chart.scrollbarX.parent = chart.bottomAxesContainer;

      dateAxis.start = 0.79;
      dateAxis.keepSelection = true;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })


      }); // end am4core.ready()
   }
   if(jQuery('#am-linescrollzomm-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-linescrollzomm-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#57aeff")];

      // Add data
      chart.data = generateChartData();

      // Create axes
      var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      dateAxis.renderer.minGridDistance = 50;

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      // Create series
      var series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.valueY = "visits";
      series.dataFields.dateX = "date";
      series.strokeWidth = 2;
      series.minBulletDistance = 10;
      series.tooltipText = "{valueY}";
      series.tooltip.pointerOrientation = "vertical";
      series.tooltip.background.cornerRadius = 20;
      series.tooltip.background.fillOpacity = 0.5;
      series.tooltip.label.padding(12,12,12,12)

      // Add scrollbar
      chart.scrollbarX = new am4charts.XYChartScrollbar();
      chart.scrollbarX.series.push(series);

      // Add cursor
      chart.cursor = new am4charts.XYCursor();
      chart.cursor.xAxis = dateAxis;
      chart.cursor.snapToSeries = series;

      function generateChartData() {
          var chartData = [];
          var firstDate = new Date();
          firstDate.setDate(firstDate.getDate() - 1000);
          var visits = 1200;
          for (var i = 0; i < 500; i++) {
              var newDate = new Date(firstDate);
              newDate.setDate(newDate.getDate() + i);

              visits += Math.round((Math.random()<0.5?1:-1)*Math.random()*10);

              chartData.push({
                  date: newDate,
                  visits: visits
              });
          }
          return chartData;
      }

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      });
   }

   if(jQuery('#am-zoomable-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-zoomable-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#57aeff")];

      // Add data
      chart.data = [ {
        "date": "2012-07-27",
        "value": 13
      }, {
        "date": "2012-07-28",
        "value": 11
      }, {
        "date": "2012-07-29",
        "value": 15
      }, {
        "date": "2012-07-30",
        "value": 16
      }, {
        "date": "2012-07-31",
        "value": 18
      }, {
        "date": "2012-08-01",
        "value": 13
      }, {
        "date": "2012-08-02",
        "value": 22
      }, {
        "date": "2012-08-03",
        "value": 23
      }, {
        "date": "2012-08-04",
        "value": 20
      }, {
        "date": "2012-08-05",
        "value": 17
      }, {
        "date": "2012-08-06",
        "value": 16
      }, {
        "date": "2012-08-07",
        "value": 18
      }, {
        "date": "2012-08-08",
        "value": 21
      }, {
        "date": "2012-08-09",
        "value": 26
      }, {
        "date": "2012-08-10",
        "value": 24
      }, {
        "date": "2012-08-11",
        "value": 29
      }, {
        "date": "2012-08-12",
        "value": 32
      }, {
        "date": "2012-08-13",
        "value": 18
      }, {
        "date": "2012-08-14",
        "value": 24
      }, {
        "date": "2012-08-15",
        "value": 22
      }, {
        "date": "2012-08-16",
        "value": 18
      }, {
        "date": "2012-08-17",
        "value": 19
      }, {
        "date": "2012-08-18",
        "value": 14
      }, {
        "date": "2012-08-19",
        "value": 15
      }, {
        "date": "2012-08-20",
        "value": 12
      }, {
        "date": "2012-08-21",
        "value": 8
      }, {
        "date": "2012-08-22",
        "value": 9
      }, {
        "date": "2012-08-23",
        "value": 8
      }, {
        "date": "2012-08-24",
        "value": 7
      }, {
        "date": "2012-08-25",
        "value": 5
      }, {
        "date": "2012-08-26",
        "value": 11
      }, {
        "date": "2012-08-27",
        "value": 13
      }, {
        "date": "2012-08-28",
        "value": 18
      }, {
        "date": "2012-08-29",
        "value": 20
      }, {
        "date": "2012-08-30",
        "value": 29
      }, {
        "date": "2012-08-31",
        "value": 33
      }, {
        "date": "2012-09-01",
        "value": 42
      }, {
        "date": "2012-09-02",
        "value": 35
      }, {
        "date": "2012-09-03",
        "value": 31
      }, {
        "date": "2012-09-04",
        "value": 47
      }, {
        "date": "2012-09-05",
        "value": 52
      }, {
        "date": "2012-09-06",
        "value": 46
      }, {
        "date": "2012-09-07",
        "value": 41
      }, {
        "date": "2012-09-08",
        "value": 43
      }, {
        "date": "2012-09-09",
        "value": 40
      }, {
        "date": "2012-09-10",
        "value": 39
      }, {
        "date": "2012-09-11",
        "value": 34
      }, {
        "date": "2012-09-12",
        "value": 29
      }, {
        "date": "2012-09-13",
        "value": 34
      }, {
        "date": "2012-09-14",
        "value": 37
      }, {
        "date": "2012-09-15",
        "value": 42
      }, {
        "date": "2012-09-16",
        "value": 49
      }, {
        "date": "2012-09-17",
        "value": 46
      }, {
        "date": "2012-09-18",
        "value": 47
      }, {
        "date": "2012-09-19",
        "value": 55
      }, {
        "date": "2012-09-20",
        "value": 59
      }, {
        "date": "2012-09-21",
        "value": 58
      }, {
        "date": "2012-09-22",
        "value": 57
      }, {
        "date": "2012-09-23",
        "value": 61
      }, {
        "date": "2012-09-24",
        "value": 59
      }, {
        "date": "2012-09-25",
        "value": 67
      }, {
        "date": "2012-09-26",
        "value": 65
      }, {
        "date": "2012-09-27",
        "value": 61
      }, {
        "date": "2012-09-28",
        "value": 66
      }, {
        "date": "2012-09-29",
        "value": 69
      }, {
        "date": "2012-09-30",
        "value": 71
      }, {
        "date": "2012-10-01",
        "value": 67
      }, {
        "date": "2012-10-02",
        "value": 63
      }, {
        "date": "2012-10-03",
        "value": 46
      }, {
        "date": "2012-10-04",
        "value": 32
      }, {
        "date": "2012-10-05",
        "value": 21
      }, {
        "date": "2012-10-06",
        "value": 18
      }, {
        "date": "2012-10-07",
        "value": 21
      }, {
        "date": "2012-10-08",
        "value": 28
      }, {
        "date": "2012-10-09",
        "value": 27
      }, {
        "date": "2012-10-10",
        "value": 36
      }, {
        "date": "2012-10-11",
        "value": 33
      }, {
        "date": "2012-10-12",
        "value": 31
      }, {
        "date": "2012-10-13",
        "value": 30
      }, {
        "date": "2012-10-14",
        "value": 34
      }, {
        "date": "2012-10-15",
        "value": 38
      }, {
        "date": "2012-10-16",
        "value": 37
      }, {
        "date": "2012-10-17",
        "value": 44
      }, {
        "date": "2012-10-18",
        "value": 49
      }, {
        "date": "2012-10-19",
        "value": 53
      }, {
        "date": "2012-10-20",
        "value": 57
      }, {
        "date": "2012-10-21",
        "value": 60
      }, {
        "date": "2012-10-22",
        "value": 61
      }, {
        "date": "2012-10-23",
        "value": 69
      }, {
        "date": "2012-10-24",
        "value": 67
      }, {
        "date": "2012-10-25",
        "value": 72
      }, {
        "date": "2012-10-26",
        "value": 77
      }, {
        "date": "2012-10-27",
        "value": 75
      }, {
        "date": "2012-10-28",
        "value": 70
      }, {
        "date": "2012-10-29",
        "value": 72
      }, {
        "date": "2012-10-30",
        "value": 70
      }, {
        "date": "2012-10-31",
        "value": 72
      }, {
        "date": "2012-11-01",
        "value": 73
      }, {
        "date": "2012-11-02",
        "value": 67
      }, {
        "date": "2012-11-03",
        "value": 68
      }, {
        "date": "2012-11-04",
        "value": 65
      }, {
        "date": "2012-11-05",
        "value": 71
      }, {
        "date": "2012-11-06",
        "value": 75
      }, {
        "date": "2012-11-07",
        "value": 74
      }, {
        "date": "2012-11-08",
        "value": 71
      }, {
        "date": "2012-11-09",
        "value": 76
      }, {
        "date": "2012-11-10",
        "value": 77
      }, {
        "date": "2012-11-11",
        "value": 81
      }, {
        "date": "2012-11-12",
        "value": 83
      }, {
        "date": "2012-11-13",
        "value": 80
      }, {
        "date": "2012-11-18",
        "value": 80
      }, {
        "date": "2012-11-19",
        "value": 87
      }, {
        "date": "2012-11-20",
        "value": 83
      }, {
        "date": "2012-11-21",
        "value": 85
      }, {
        "date": "2012-11-22",
        "value": 84
      }, {
        "date": "2012-11-23",
        "value": 82
      }, {
        "date": "2012-11-24",
        "value": 73
      }, {
        "date": "2012-11-25",
        "value": 71
      }, {
        "date": "2012-11-26",
        "value": 75
      }, {
        "date": "2012-11-27",
        "value": 79
      }, {
        "date": "2012-11-28",
        "value": 70
      }, {
        "date": "2012-11-29",
        "value": 73
      }, {
        "date": "2012-11-30",
        "value": 61
      }, {
        "date": "2012-12-01",
        "value": 62
      }, {
        "date": "2012-12-02",
        "value": 66
      }, {
        "date": "2012-12-03",
        "value": 65
      }, {
        "date": "2012-12-04",
        "value": 73
      }, {
        "date": "2012-12-05",
        "value": 79
      }, {
        "date": "2012-12-06",
        "value": 78
      }, {
        "date": "2012-12-07",
        "value": 78
      }, {
        "date": "2012-12-08",
        "value": 78
      }, {
        "date": "2012-12-09",
        "value": 74
      }, {
        "date": "2012-12-10",
        "value": 73
      }, {
        "date": "2012-12-11",
        "value": 75
      }, {
        "date": "2012-12-12",
        "value": 70
      }, {
        "date": "2012-12-13",
        "value": 77
      }, {
        "date": "2012-12-14",
        "value": 67
      }, {
        "date": "2012-12-15",
        "value": 62
      }, {
        "date": "2012-12-16",
        "value": 64
      }, {
        "date": "2012-12-17",
        "value": 61
      }, {
        "date": "2012-12-18",
        "value": 59
      }, {
        "date": "2012-12-19",
        "value": 53
      }, {
        "date": "2012-12-20",
        "value": 54
      }, {
        "date": "2012-12-21",
        "value": 56
      }, {
        "date": "2012-12-22",
        "value": 59
      }, {
        "date": "2012-12-23",
        "value": 58
      }, {
        "date": "2012-12-24",
        "value": 55
      }, {
        "date": "2012-12-25",
        "value": 52
      }, {
        "date": "2012-12-26",
        "value": 54
      }, {
        "date": "2012-12-27",
        "value": 50
      }, {
        "date": "2012-12-28",
        "value": 50
      }, {
        "date": "2012-12-29",
        "value": 51
      }, {
        "date": "2012-12-30",
        "value": 52
      }, {
        "date": "2012-12-31",
        "value": 58
      }, {
        "date": "2013-01-01",
        "value": 60
      }, {
        "date": "2013-01-02",
        "value": 67
      }, {
        "date": "2013-01-03",
        "value": 64
      }, {
        "date": "2013-01-04",
        "value": 66
      }, {
        "date": "2013-01-05",
        "value": 60
      }, {
        "date": "2013-01-06",
        "value": 63
      }, {
        "date": "2013-01-07",
        "value": 61
      }, {
        "date": "2013-01-08",
        "value": 60
      }, {
        "date": "2013-01-09",
        "value": 65
      }, {
        "date": "2013-01-10",
        "value": 75
      }, {
        "date": "2013-01-11",
        "value": 77
      }, {
        "date": "2013-01-12",
        "value": 78
      }, {
        "date": "2013-01-13",
        "value": 70
      }, {
        "date": "2013-01-14",
        "value": 70
      }, {
        "date": "2013-01-15",
        "value": 73
      }, {
        "date": "2013-01-16",
        "value": 71
      }, {
        "date": "2013-01-17",
        "value": 74
      }, {
        "date": "2013-01-18",
        "value": 78
      }, {
        "date": "2013-01-19",
        "value": 85
      }, {
        "date": "2013-01-20",
        "value": 82
      }, {
        "date": "2013-01-21",
        "value": 83
      }, {
        "date": "2013-01-22",
        "value": 88
      }, {
        "date": "2013-01-23",
        "value": 85
      }, {
        "date": "2013-01-24",
        "value": 85
      }, {
        "date": "2013-01-25",
        "value": 80
      }, {
        "date": "2013-01-26",
        "value": 87
      }, {
        "date": "2013-01-27",
        "value": 84
      }, {
        "date": "2013-01-28",
        "value": 83
      }, {
        "date": "2013-01-29",
        "value": 84
      }, {
        "date": "2013-01-30",
        "value": 81
      } ];

      // Create axes
      var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      dateAxis.renderer.grid.template.location = 0;
      dateAxis.renderer.minGridDistance = 50;

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      // Create series
      var series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.valueY = "value";
      series.dataFields.dateX = "date";
      series.strokeWidth = 3;
      series.fillOpacity = 0.5;

      // Add vertical scrollbar
      chart.scrollbarY = new am4core.Scrollbar();
      chart.scrollbarY.marginLeft = 0;

      // Add cursor
      chart.cursor = new am4charts.XYCursor();
      chart.cursor.behavior = "zoomY";
      chart.cursor.lineX.disabled = true;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }
   if(jQuery('#am-radar-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      /* Create chart instance */
      var chart = am4core.create("am-radar-chart", am4charts.RadarChart);
      chart.colors.list = [am4core.color("#4788ff")];

      /* Add data */
      chart.data = [{
        "country": "Lithuania",
        "litres": 501
      }, {
        "country": "Czechia",
        "litres": 301
      }, {
        "country": "Ireland",
        "litres": 266
      }, {
        "country": "Germany",
        "litres": 165
      }, {
        "country": "Australia",
        "litres": 139
      }, {
        "country": "Austria",
        "litres": 336
      }, {
        "country": "UK",
        "litres": 290
      }, {
        "country": "Belgium",
        "litres": 325
      }, {
        "country": "The Netherlands",
        "litres": 40
      }];

      /* Create axes */
      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "country";

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      valueAxis.renderer.axisFills.template.fill = chart.colors.getIndex(2);
      valueAxis.renderer.axisFills.template.fillOpacity = 0.05;

      /* Create and configure series */
      var series = chart.series.push(new am4charts.RadarSeries());
      series.dataFields.valueY = "litres";
      series.dataFields.categoryX = "country";
      series.name = "Sales";
      series.strokeWidth = 3;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }
   if(jQuery('#am-polar-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      /* Create chart instance */
      var chart = am4core.create("am-polar-chart", am4charts.RadarChart);

      /* Add data */
      chart.data = [ {
        "direction": "N",
        "value": 8
      }, {
        "direction": "NE",
        "value": 9
      }, {
        "direction": "E",
        "value": 4.5
      }, {
        "direction": "SE",
        "value": 3.5
      }, {
        "direction": "S",
        "value": 9.2
      }, {
        "direction": "SW",
        "value": 8.4
      }, {
        "direction": "W",
        "value": 11.1
      }, {
        "direction": "NW",
        "value": 10
      } ];

      /* Create axes */
      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "direction";

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      //valueAxis.renderer.gridType = "polygons";

      var range = categoryAxis.axisRanges.create();
      range.category = "NW";
      range.endCategory = "NW";
      range.axisFill.fill = am4core.color("#4788ff");
      range.axisFill.fillOpacity = 0.3;

      var range2 = categoryAxis.axisRanges.create();
      range2.category = "N";
      range2.endCategory = "N";
      range2.axisFill.fill = am4core.color("#ff4b4b");
      range2.axisFill.fillOpacity = 0.3;

      var range3 = categoryAxis.axisRanges.create();
      range3.category = "SE";
      range3.endCategory = "SW";
      range3.axisFill.fill = am4core.color("#37e6b0");
      range3.axisFill.fillOpacity = 0.3;
      range3.locations.endCategory = 0;

      /* Create and configure series */
      var series = chart.series.push(new am4charts.RadarSeries());
      series.dataFields.valueY = "value";
      series.dataFields.categoryX = "direction";
      series.name = "Wind direction";
      series.strokeWidth = 3;
      series.fillOpacity = 0.2;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }

   if(jQuery('#am-polarscatter-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      /* Create chart instance */
      var chart = am4core.create("am-polarscatter-chart", am4charts.RadarChart);
       chart.colors.list = [am4core.color("#4788ff"),am4core.color("#fe721c"),am4core.color("#37e6b0")];

      /* Add data */
      chart.data = [{
        "country": "Lithuania",
        "litres": 501,
        "units": 250
      }, {
        "country": "Czech Republic",
        "litres": 301,
        "units": 222
      }, {
        "country": "Ireland",
        "litres": 266,
        "units": 179
      }, {
        "country": "Germany",
        "litres": 165,
        "units": 298
      }, {
        "country": "Australia",
        "litres": 139,
        "units": 299
      }];

      /* Create axes */
      var xAxis = chart.xAxes.push(new am4charts.ValueAxis());
      xAxis.renderer.maxLabelPosition = 0.99;

      var yAxis = chart.yAxes.push(new am4charts.ValueAxis());
      yAxis.renderer.labels.template.verticalCenter = "bottom";
      yAxis.renderer.labels.template.horizontalCenter = "right";
      yAxis.renderer.maxLabelPosition = 0.99;
      yAxis.renderer.labels.template.paddingBottom = 1;
      yAxis.renderer.labels.template.paddingRight = 3;

      /* Create and configure series */
      var series1 = chart.series.push(new am4charts.RadarSeries());
      series1.bullets.push(new am4charts.CircleBullet());
      series1.strokeOpacity = 0;
      series1.dataFields.valueX = "x";
      series1.dataFields.valueY = "y";
      series1.name = "Series #1";
      series1.sequencedInterpolation = true;
      series1.sequencedInterpolationDelay = 10;
      series1.data = [
        { "x": 83, "y": 5.1 },
        { "x": 44, "y": 5.8 },
        { "x": 76, "y": 9 },
        { "x": 2, "y": 1.4 },
        { "x": 100, "y": 8.3 },
        { "x": 96, "y": 1.7 },
        { "x": 68, "y": 3.9 },
        { "x": 0, "y": 3 },
        { "x": 100, "y": 4.1 },
        { "x": 16, "y": 5.5 },
        { "x": 71, "y": 6.8 },
        { "x": 100, "y": 7.9 },
        { "x": 35, "y": 8 },
        { "x": 44, "y": 6 },
        { "x": 64, "y": 0.7 },
        { "x": 53, "y": 3.3 },
        { "x": 92, "y": 4.1 },
        { "x": 43, "y": 7.3 },
        { "x": 15, "y": 7.5 },
        { "x": 43, "y": 4.3 },
        { "x": 90, "y": 9.9 }
      ];

      var series2 = chart.series.push(new am4charts.RadarSeries());
      series2.bullets.push(new am4charts.CircleBullet());
      series2.strokeOpacity = 0;
      series2.dataFields.valueX = "x";
      series2.dataFields.valueY = "y";
      series2.name = "Series #2";
      series2.sequencedInterpolation = true;
      series2.sequencedInterpolationDelay = 10;
      series2.data = [
        { "x": 178, "y": 1.3 },
        { "x": 129, "y": 3.4 },
        { "x": 99, "y": 2.4 },
        { "x": 80, "y": 9.9 },
        { "x": 118, "y": 9.4 },
        { "x": 103, "y": 8.7 },
        { "x": 91, "y": 4.2 },
        { "x": 151, "y": 1.2 },
        { "x": 168, "y": 5.2 },
        { "x": 168, "y": 1.6 },
        { "x": 152, "y": 1.2 },
        { "x": 138, "y": 7.7 },
        { "x": 107, "y": 3.9 },
        { "x": 124, "y": 0.7 },
        { "x": 130, "y": 2.6 },
        { "x": 86, "y": 9.2 },
        { "x": 169, "y": 7.5 },
        { "x": 122, "y": 9.9 },
        { "x": 100, "y": 3.8 },
        { "x": 172, "y": 4.1 },
        { "x": 140, "y": 7.3 },
        { "x": 161, "y": 2.3 },
        { "x": 141, "y": 0.9 }
      ];

      var series3 = chart.series.push(new am4charts.RadarSeries());
      series3.bullets.push(new am4charts.CircleBullet());
      series3.strokeOpacity = 0;
      series3.dataFields.valueX = "x";
      series3.dataFields.valueY = "y";
      series3.name = "Series #3";
      series3.sequencedInterpolation = true;
      series3.sequencedInterpolationDelay = 10;
      series3.data = [
        { "x": 419, "y": 4.9 },
        { "x": 417, "y": 5.5 },
        { "x": 434, "y": 0.1 },
        { "x": 344, "y": 2.5 },
        { "x": 279, "y": 7.5 },
        { "x": 307, "y": 8.4 },
        { "x": 279, "y": 9 },
        { "x": 220, "y": 8.4 },
        { "x": 201, "y": 9.7 },
        { "x": 288, "y": 1.2 },
        { "x": 333, "y": 7.4 },
        { "x": 308, "y": 1.9 },
        { "x": 330, "y": 8 },
        { "x": 408, "y": 1.7 },
        { "x": 274, "y": 0.8 },
        { "x": 296, "y": 3.1 },
        { "x": 279, "y": 4.3 },
        { "x": 379, "y": 5.6 },
        { "x": 175, "y": 6.8 }
      ];

      /* Add legend */
      chart.legend = new am4charts.Legend();

      /* Add cursor */
      chart.cursor = new am4charts.RadarCursor();

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }
   if(jQuery('#am-3dpie-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      var chart = am4core.create("am-3dpie-chart", am4charts.PieChart3D);
      chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

      chart.legend = new am4charts.Legend();

      chart.data = [
        {
          country: "Lithuania",
          litres: 501.9,
          fill: "red"
        },
        {
          country: "Germany",
          litres: 165.8
        },
        {
          country: "Australia",
          litres: 139.9
        },
        {
          country: "Austria",
          litres: 128.3
        },
        {
          country: "UK",
          litres: 99
        },
        {
          country: "Belgium",
          litres: 60
        }
      ];

      var series = chart.series.push(new am4charts.PieSeries3D());
      series.colors.list = [am4core.color("#4788ff"),am4core.color("#37e6b0"),am4core.color("#ff4b4b"),
      am4core.color("#fe721c"),am4core.color("#876cfe"),am4core.color("#01041b")];
      series.dataFields.value = "litres";
      series.dataFields.category = "country";

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }

   if(jQuery('#am-layeredcolumn-chart').length){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("am-layeredcolumn-chart", am4charts.XYChart);
      chart.colors.list = [am4core.color("#37e6b0"),am4core.color("#4788ff")];

      // Add percent sign to all numbers
      chart.numberFormatter.numberFormat = "#.#'%'";

      // Add data
      chart.data = [{
          "country": "USA",
          "year2004": 3.5,
          "year2005": 4.2
      }, {
          "country": "UK",
          "year2004": 1.7,
          "year2005": 3.1
      }, {
          "country": "Canada",
          "year2004": 2.8,
          "year2005": 2.9
      }, {
          "country": "Japan",
          "year2004": 2.6,
          "year2005": 2.3
      }, {
          "country": "France",
          "year2004": 1.4,
          "year2005": 2.1
      }, {
          "country": "Brazil",
          "year2004": 2.6,
          "year2005": 4.9
      }];

      // Create axes
      var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.dataFields.category = "country";
      categoryAxis.renderer.grid.template.location = 0;
      categoryAxis.renderer.minGridDistance = 30;

      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      valueAxis.title.text = "GDP growth rate";
      valueAxis.title.fontWeight = 800;

      // Create series
      var series = chart.series.push(new am4charts.ColumnSeries());
      series.dataFields.valueY = "year2004";
      series.dataFields.categoryX = "country";
      series.clustered = false;
      series.tooltipText = "GDP grow in {categoryX} (2004): [bold]{valueY}[/]";

      var series2 = chart.series.push(new am4charts.ColumnSeries());
      series2.dataFields.valueY = "year2005";
      series2.dataFields.categoryX = "country";
      series2.clustered = false;
      series2.columns.template.width = am4core.percent(50);
      series2.tooltipText = "GDP grow in {categoryX} (2005): [bold]{valueY}[/]";

      chart.cursor = new am4charts.XYCursor();
      chart.cursor.lineX.disabled = true;
      chart.cursor.lineY.disabled = true;

        const body = document.querySelector('body')
        if (body.classList.contains('dark')) {
          amChartUpdate(chart, {
            dark: true
          })
        }

        document.addEventListener('ChangeColorMode', function (e) {
          amChartUpdate(chart, e.detail)
        })

      }); // end am4core.ready()
   }

/*---------------------------------------------------------------------
   Morris Charts
-----------------------------------------------------------------------*/

if(jQuery('#morris-line-chart').length){
  new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'morris-line-chart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { year: '2008', value: 20 },
      { year: '2009', value: 10 },
      { year: '2010', value: 5 },
      { year: '2011', value: 5 },
      { year: '2012', value: 20 }
    ],
    // The name of the data record attribute that contains x-values.
    xkey: 'year',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['value'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Value'],
    lineColors: ['#4788ff']
  });
}

if(jQuery('#morris-bar-chart').length){
 Morris.Bar({
element: 'morris-bar-chart',
data: [
  {x: '2011 Q1', y: 3, z: 2, a: 3},
  {x: '2011 Q2', y: 2, z: null, a: 1},
  {x: '2011 Q3', y: 0, z: 2, a: 4},
  {x: '2011 Q4', y: 2, z: 4, a: 3}
],
xkey: 'x',
ykeys: ['y', 'z', 'a'],
labels: ['Y', 'Z', 'A'],
barColors: ['#4788ff', '#fe721c', '#37e6b0'],
hoverCallback: function (index, options, content, row) {
                    return '';
                  }
}).on('click', function(i, row){
console.log(i, row);
});
}

if(jQuery('#morris-area-chart').length){
  var area = new Morris.Area({
    element: 'morris-area-chart',
    resize: true,
    data: [
      {y: '2011 Q1', item1: 2666, item2: 2666},
      {y: '2011 Q2', item1: 2778, item2: 2294},
      {y: '2011 Q3', item1: 4912, item2: 1969},
      {y: '2011 Q4', item1: 3767, item2: 3597},
      {y: '2012 Q1', item1: 6810, item2: 1914},
      {y: '2012 Q2', item1: 5670, item2: 4293},
      {y: '2012 Q3', item1: 4820, item2: 3795},
      {y: '2012 Q4', item1: 15073, item2: 5967},
      {y: '2013 Q1', item1: 10687, item2: 4460},
      {y: '2013 Q2', item1: 8432, item2: 5713}
    ],
    xkey: 'y',
    ykeys: ['item1', 'item2'],
    labels: ['Item 1', 'Item 2'],
    lineColors: ['#75e275', '#75bcff'],
    hoverCallback: function (index, options, content, row) {
                    return '';
                  }
  });
}

if(jQuery('#morris-donut-chart').length){
  var donut = new Morris.Donut({
    element: 'morris-donut-chart',
    resize: true,
    colors: ["#4788ff", "#ff4b4b", "#37e6b0"],
    data: [
      {label: "Download Sales", value: 12},
      {label: "In-Store Sales", value: 30},
      {label: "Mail-Order Sales", value: 20}
    ],
    hideHover: 'auto'
  });
}

/*---------------------------------------------------------------------
   High Charts
-----------------------------------------------------------------------*/
if (jQuery("#high-basicline-chart").length && Highcharts.chart("high-basicline-chart", {
    chart: {
      type: "spline",
      inverted: !0
    },
    title: {
      text: "Atmosphere Temperature by Altitude"
    },
    subtitle: {
      text: "According to the Standard Atmosphere Model"
    },
    xAxis: {
      reversed: !1,
      title: {
        enabled: !0,
        text: "Altitude"
      },
      labels: {
        format: "{value} km"
      },
      maxPadding: .05,
      showLastLabel: !0
    },
    yAxis: {
      title: {
        text: "Temperature"
      },
      labels: {
        format: "{value}°"
      },
      lineWidth: 2
    },
    legend: {
      enabled: !1
    },
    tooltip: {
      headerFormat: "<b>{series.name}</b><br/>",
      pointFormat: "{point.x} km: {point.y}°C"
    },
    plotOptions: {
      spline: {
        marker: {
          enable: !1
        }
      }
    },
    series: [{
      name: "Temperature",
      color: "#4788ff",
      data: [
        [0, 15],
        [10, -50],
        [20, -56.5],
        [30, -46.5],
        [40, -22.1],
        [50, -2.5],
        [60, -27.7],
        [70, -55.7],
        [80, -76.5]
      ]
    }]
  }), jQuery("#high-area-chart").length && Highcharts.chart("high-area-chart", {
    chart: {
      type: "areaspline"
    },
    title: {
      text: "Average fruit consumption during one week"
    },
    legend: {
      layout: "vertical",
      align: "left",
      verticalAlign: "top",
      x: 150,
      y: 100,
      floating: !0,
      borderWidth: 1,
      backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || "#FFFFFF"
    },
    xAxis: {
      categories: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      plotBands: [{
        from: 4.5,
        to: 6.5,
        color: "rgba(68, 170, 213, .2)"
      }]
    },
    yAxis: {
      title: {
        text: "Fruit units"
      }
    },
    tooltip: {
      shared: !0,
      valueSuffix: " units"
    },
    credits: {
      enabled: !1
    },
    plotOptions: {
      areaspline: {
        fillOpacity: .5
      }
    },
    series: [{
      name: "John",
      color: "#4788ff",
      data: [3, 4, 3, 5, 4, 10, 12]
    }, {
      name: "Jane",
      color: "#37e6b0",
      data: [1, 3, 4, 3, 3, 5, 4]
    }]
  }), jQuery("#high-columnndbar-chart").length && Highcharts.chart("high-columnndbar-chart", {
    chart: {
      type: "bar"
    },
    title: {
      text: "Stacked bar chart"
    },
    xAxis: {
      categories: ["Apples", "Oranges", "Pears", "Grapes", "Bananas"]
    },
    yAxis: {
      min: 0,
      title: {
        text: "Total fruit consumption"
      }
    },
    legend: {
      reversed: !0
    },
    plotOptions: {
      series: {
        stacking: "normal"
      }
    },
    series: [{
      name: "John",
      color: "#4788ff",
      data: [5, 3, 4, 7, 2]
    }, {
      name: "Jane",
      color: "#ff4b4b",
      data: [2, 2, 3, 2, 1]
    }, {
      name: "Joe",
      color: "#37e6b0",
      data: [3, 4, 4, 2, 5]
    }]
  }), jQuery("#high-pie-chart").length && Highcharts.chart("high-pie-chart", {
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: !1,
      type: "pie"
    },
    colorAxis: {},
    title: {
      text: "Browser market shares in January, 2018"
    },
    tooltip: {
      pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"
    },
    plotOptions: {
      pie: {
        allowPointSelect: !0,
        cursor: "pointer",
        dataLabels: {
          enabled: !0,
          format: "<b>{point.name}</b>: {point.percentage:.1f} %"
        }
      }
    },
    series: [{
      name: "Brands",
      colorByPoint: !0,
      data: [{
        name: "Chrome",
        y: 61.41,
        sliced: !0,
        selected: !0,
        color: "#4788ff"
      }, {
        name: "Internet Explorer",
        y: 11.84,
        color: "#ff4b4b"
      }, {
        name: "Firefox",
        y: 10.85,
        color: "#65f9b3"
      }, {
        name: "Edge",
        y: 4.67,
        color: "#6ce6f4"
      }, {
        name: "Other",
        y: 2.61
      }]
    }]
  }), jQuery("#high-scatterplot-chart").length && Highcharts.chart("high-scatterplot-chart", {
    chart: {
      type: "scatter",
      zoomType: "xy"
    },
    accessibility: {
      description: "A scatter plot compares the height and weight of 507 individuals by gender. Height in centimeters is plotted on the X-axis and weight in kilograms is plotted on the Y-axis. The chart is interactive, and each data point can be hovered over to expose the height and weight data for each individual. The scatter plot is fairly evenly divided by gender with females dominating the left-hand side of the chart and males dominating the right-hand side. The height data for females ranges from 147.2 to 182.9 centimeters with the greatest concentration between 160 and 165 centimeters. The weight data for females ranges from 42 to 105.2 kilograms with the greatest concentration at around 60 kilograms. The height data for males ranges from 157.2 to 198.1 centimeters with the greatest concentration between 175 and 180 centimeters. The weight data for males ranges from 53.9 to 116.4 kilograms with the greatest concentration at around 80 kilograms."
    },
    title: {
      text: "Height Versus Weight of 507 Individuals by Gender"
    },
    subtitle: {
      text: "Source: Heinz  2003"
    },
    xAxis: {
      title: {
        enabled: !0,
        text: "Height (cm)"
      },
      startOnTick: !0,
      endOnTick: !0,
      showLastLabel: !0
    },
    yAxis: {
      title: {
        text: "Weight (kg)"
      }
    },
    legend: {
      layout: "vertical",
      align: "left",
      verticalAlign: "top",
      x: 100,
      y: 70,
      floating: !0,
      backgroundColor: Highcharts.defaultOptions.chart.backgroundColor,
      borderWidth: 1
    },
    plotOptions: {
      scatter: {
        marker: {
          radius: 5,
          states: {
            hover: {
              enabled: !0,
              lineColor: "rgb(100,100,100)"
            }
          }
        },
        states: {
          hover: {
            marker: {
              enabled: !1
            }
          }
        },
        tooltip: {
          headerFormat: "<b>{series.name}</b><br>",
          pointFormat: "{point.x} cm, {point.y} kg"
        }
      }
    },
    series: [{
      name: "Female",
      color: "rgba(223, 83, 83, .5)",
      data: [
        [161.2, 51.6],
        [167.5, 59],
        [159.5, 49.2],
        [157, 63],
        [155.8, 53.6],
        [170, 59],
        [159.1, 47.6],
        [166, 69.8],
        [176.2, 66.8],
        [160.2, 75.2],
        [172.7, 62],
        [155, 49.2],
        [156.5, 67.2],
        [164, 53.8],
        [160.9, 54.4]
      ],
      color: "#4788ff"
    }, {
      name: "Male",
      color: "rgba(119, 152, 191, .5)",
      data: [
        [174, 65.6],
        [175.3, 71.8],
        [193.5, 80.7],
        [186.5, 72.6],
        [187.2, 78.8],
        [181.5, 74.8],
        [184, 86.4],
        [184.5, 78.4],
        [175, 62],
        [184, 81.6],
        [180.1, 93],
        [175.5, 80.9],
        [180.6, 72.7],
        [184.4, 68],
        [175.5, 70.9],
        [180.3, 83.2],
        [180.3, 83.2]
      ],
      color: "#ff4b4b"
    }]
  }), jQuery("#high-linendcolumn-chart").length && Highcharts.chart("high-linendcolumn-chart", {
    chart: {
      zoomType: "xy"
    },
    title: {
      text: "Average Monthly Temperature and Rainfall in Tokyo"
    },
    subtitle: {
      text: "Source: WorldClimate.com"
    },
    xAxis: [{
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      crosshair: !0
    }],
    yAxis: [{
      labels: {
        format: "{value}°C",
        style: {
          color: Highcharts.getOptions().colors[1]
        }
      },
      title: {
        text: "Temperature",
        style: {
          color: Highcharts.getOptions().colors[1]
        }
      }
    }, {
      title: {
        text: "Rainfall",
        style: {
          color: Highcharts.getOptions().colors[0]
        }
      },
      labels: {
        format: "{value} mm",
        style: {
          color: Highcharts.getOptions().colors[0]
        }
      },
      opposite: !0
    }],
    tooltip: {
      shared: !0
    },
    legend: {
      layout: "vertical",
      align: "left",
      x: 120,
      verticalAlign: "top",
      y: 100,
      floating: !0,
      backgroundColor: Highcharts.defaultOptions.legend.backgroundColor || "rgba(255,255,255,0.25)"
    },
    series: [{
      name: "Rainfall",
      type: "column",
      yAxis: 1,
      data: [49.9, 71.5, 106.4, 129.2, 144, 176, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
      color: "#4788ff",
      tooltip: {
        valueSuffix: " mm"
      }
    }, {
      name: "Temperature",
      type: "spline",
      data: [7, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
      color: "#ff4b4b",
      tooltip: {
        valueSuffix: "°C"
      }
    }]
  }), jQuery("#high-dynamic-chart").length && Highcharts.chart("high-dynamic-chart", {
    chart: {
      type: "spline",
      animation: Highcharts.svg,
      marginRight: 10,
      events: {
        load: function() {
          var e = this.series[0];
          setInterval(function() {
            var t = (new Date).getTime(),
              a = Math.random();
            e.addPoint([t, a], !0, !0)
          }, 1e3)
        }
      }
    },
    time: {
      useUTC: !1
    },
    title: {
      text: "Live random data"
    },
    accessibility: {
      announceNewData: {
        enabled: !0,
        minAnnounceInterval: 15e3,
        announcementFormatter: function(e, t, a) {
          return !!a && "New point added. Value: " + a.y
        }
      }
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150
    },
    yAxis: {
      title: {
        text: "Value"
      },
      plotLines: [{
        value: 0,
        width: 1,
        color: "#808080"
      }]
    },
    tooltip: {
      headerFormat: "<b>{series.name}</b><br/>",
      pointFormat: "{point.x:%Y-%m-%d %H:%M:%S}<br/>{point.y:.2f}"
    },
    legend: {
      enabled: !1
    },
    exporting: {
      enabled: !1
    },
    series: [{
      name: "Random data",
      color: "#4788ff",
      data: function() {
        var e, t = [],
          a = (new Date).getTime();
        for (e = -19; e <= 0; e += 1) t.push({
          x: a + 1e3 * e,
          y: Math.random()
        });
        return t
      }()
    }]
  }), jQuery("#high-3d-chart").length) {
  var chart = new Highcharts.Chart({
    chart: {
      renderTo: "high-3d-chart",
      type: "column",
      options3d: {
        enabled: !0,
        alpha: 15,
        beta: 15,
        depth: 50,
        viewDistance: 25
      }
    },
    title: {
      text: "Chart rotation demo"
    },
    subtitle: {
      text: "Test options by dragging the sliders below"
    },
    plotOptions: {
      column: {
        depth: 25
      }
    },
    series: [{
      data: [29.9, 71.5, 106.4, 129.2, 144, 176, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
      color: "#4788ff"
    }]
  });

  function showValues() {
    $("#alpha-value").html(chart.options.chart.options3d.alpha), $("#beta-value").html(chart.options.chart.options3d.beta), $("#depth-value").html(chart.options.chart.options3d.depth)
  }
  $("#sliders input").on("input change", function() {
    chart.options.chart.options3d[this.id] = parseFloat(this.value), showValues(), chart.redraw(!1)
  }), showValues()
}
if (jQuery("#high-gauges-chart").length && Highcharts.chart("high-gauges-chart", {
    chart: {
      type: "gauge",
      plotBackgroundColor: null,
      plotBackgroundImage: null,
      plotBorderWidth: 0,
      plotShadow: !1
    },
    title: {
      text: "Speedometer"
    },
    pane: {
      startAngle: -150,
      endAngle: 150,
      background: [{
        backgroundColor: {
          linearGradient: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 1
          },
          stops: [
            [0, "#FFF"],
            [1, "#333"]
          ]
        },
        borderWidth: 0,
        outerRadius: "109%"
      }, {
        backgroundColor: {
          linearGradient: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 1
          },
          stops: [
            [0, "#333"],
            [1, "#FFF"]
          ]
        },
        borderWidth: 1,
        outerRadius: "107%"
      }, {}, {
        backgroundColor: "#DDD",
        borderWidth: 0,
        outerRadius: "105%",
        innerRadius: "103%"
      }]
    },
    yAxis: {
      min: 0,
      max: 200,
      minorTickInterval: "auto",
      minorTickWidth: 1,
      minorTickLength: 10,
      minorTickPosition: "inside",
      minorTickColor: "#666",
      tickPixelInterval: 30,
      tickWidth: 2,
      tickPosition: "inside",
      tickLength: 10,
      tickColor: "#666",
      labels: {
        step: 2,
        rotation: "auto"
      },
      title: {
        text: "km/h"
      },
      plotBands: [{
        from: 0,
        to: 120,
        color: "#55BF3B"
      }, {
        from: 120,
        to: 160,
        color: "#DDDF0D"
      }, {
        from: 160,
        to: 200,
        color: "#DF5353"
      }]
    },
    series: [{
      name: "Speed",
      data: [80],
      tooltip: {
        valueSuffix: " km/h"
      }
    }]
  }, function(e) {
    e.renderer.forExport || setInterval(function() {
      var t, a = e.series[0].points[0],
        n = Math.round(20 * (Math.random() - .5));
      ((t = a.y + n) < 0 || t > 200) && (t = a.y - n), a.update(t)
    }, 3e3)
  }), jQuery("#high-barwithnagative-chart").length) {
  var categories = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100 + "];
  Highcharts.chart("high-barwithnagative-chart", {
    chart: {
      type: "bar"
    },
    title: {
      text: "Population pyramid for Germany, 2018"
    },
    subtitle: {
      text: 'Source: <a href="http://populationpyramid.net/germany/2018/">Population Pyramids of the World from 1950 to 2100</a>'
    },
    accessibility: {
      point: {
        descriptionFormatter: function(e) {
          return e.index + 1 + ", Age " + e.category + ", " + Math.abs(e.y) + "%. " + e.series.name + "."
        }
      }
    },
    xAxis: [{
      categories: categories,
      reversed: !1,
      labels: {
        step: 1
      },
      accessibility: {
        description: "Age (male)"
      }
    }, {
      opposite: !0,
      reversed: !1,
      categories: categories,
      linkedTo: 0,
      labels: {
        step: 1
      },
      accessibility: {
        description: "Age (female)"
      }
    }],
    yAxis: {
      title: {
        text: null
      },
      labels: {
        formatter: function() {
          return Math.abs(this.value) + "%"
        }
      },
      accessibility: {
        description: "Percentage population",
        rangeDescription: "Range: 0 to 5%"
      }
    },
    plotOptions: {
      series: {
        stacking: "normal"
      }
    },
    tooltip: {
      formatter: function() {
        return "<b>" + this.series.name + ", age " + this.point.category + "</b><br/>Population: " + Highcharts.numberFormat(Math.abs(this.point.y), 1) + "%"
      }
    },
    series: [{
      name: "Male",
      data: [-2.2, -2.1, -2.2, -2.4, -2.7, -3, -3.3, -3.2, -2.9, -3.5, -4.4, -4.1, -0],
      color: "#4788ff"
    }, {
      name: "Female",
      data: [2.1, 2, 2.1, 2.3, 2.6, 2.9, 3.2, 3.1, 2.9, 3.4, 0],
      color: "#ff4b4b"
    }]
  })
}

/*--------------Chart 1----------------*/

var options = {
    chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },

    series: [{
        name: 'series1',
        data: [60, 15, 50, 30, 70]
    }, ],
    colors: ['#50b5ff'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
};

if(jQuery('#chart-1').length){
    var chart = new ApexCharts(
        document.querySelector("#chart-1"),
        options
    );
    chart.render();
}


/*--------------Chart 2----------------*/
var options = {
    chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [70, 40, 60, 30, 60]
    }, ],
    colors: ['#fd7e14'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
};

if(jQuery('#chart-2').length){
    var chart = new ApexCharts(
        document.querySelector("#chart-2"),
        options
    );

    chart.render();
}

/*--------------Chart 3----------------*/
var options = {
    chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [60, 40, 60, 40, 70]
    }, ],
    colors: ['#49f0d3'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
};
if(jQuery('#chart-3').length){
    var chart = new ApexCharts(
        document.querySelector("#chart-3"),
        options
    );
    chart.render();
}

/*--------------Chart 4----------------*/
var options = {
    chart: {
        height: 80,
        type: 'area',
        sparkline: {
            enabled: true
        },
        group: 'sparklines',

    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.5,
            opacityTo: 0,
        }
    },
    series: [{
        name: 'series1',
        data: [75, 30, 60, 35, 60]
    }, ],
    colors: ['#ff9b8a'],

    xaxis: {
        type: 'datetime',
        categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
};

if(jQuery('#chart-4').length){
    var chart = new ApexCharts(
        document.querySelector("#chart-4"),
        options
    );

    chart.render();
}

/*--------------Chart Box----------------*/

if(jQuery('#iq-chart-box1').length){
    var options = {
      series: [{
        name: "Total sales",
        data: [10, 10, 35, 10]
    }],
      colors: ["#50b5ff"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#iq-chart-box1"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if(jQuery('#iq-chart-box2').length){
    var options = {
      series: [{
        name: "Sale Today",
        data: [10, 10, 35, 10]
    }],
      colors: ["#ff9b8a"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#iq-chart-box2"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if(jQuery('#iq-chart-box3').length){
    var options = {
      series: [{
        name: "Total Classon",
        data: [10, 10, 35, 10]
    }],
      colors: ["#49f0d3"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#iq-chart-box3"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if(jQuery('#iq-chart-box4').length){
    var options = {
      series: [{
        name: "Total Profit",
        data: [10, 10, 35, 10]
    }],
      colors: ["#fd7e14"],
      chart: {
      height: 50,
      width: 100,
      type: 'line',
      sparkline: {
          enabled: true,
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#iq-chart-box4"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
/*--------------Chart Box End----------------*/

/*-------------- Ethernet Chart ----------------*/
if (jQuery("#ethernet-chart-01").length) {
    var options = {
      series: [{
        name: "Desktops",
        data: [5, 30, 6, 20, 5, 18, 10]
    }],
    colors: ['#4788ff'],
      chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#ethernet-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#ethernet-chart-02").length) {
    var options = {
      series: [{
        name: "Desktops",
        data: [5, 20, 4, 18, 3, 15, 10]
    }],
    colors: ['#1ee2ac'],
      chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#ethernet-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#ethernet-chart-03").length) {
    var options = {
      series: [{
        name: "Desktops",
        data: [5, 20, 6, 18, 5, 15, 4]
    }],
    colors: ['#ff4b4b'],
      chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#ethernet-chart-03"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#ethernet-chart-04").length) {
    var options = {
      series: [{
        name: "Desktops",
        data: [5, 15, 3, 20, 5, 18, 13]
    }],
    colors: ['#4788ff'],
      chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#ethernet-chart-04"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

/*-------------- Ethernet Chart End ----------------*/

/*-------------- Service Chart ----------------*/
if (jQuery("#service-chart-01").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [25, 30, 22, 29]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 65,
      width: 140,
      type: 'area',
      sparkline: {
            enabled: true,
        }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#service-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#service-chart-02").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [25, 23, 28, 26]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 65,
      width: 140,
      type: 'area',
      sparkline: {
            enabled: true,
        }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#service-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#service-chart-03").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [25, 23, 28, 23]
    }],
    colors: ["#d592ff"],
      chart: {
      height: 65,
      width: 140,
      type: 'area',
      sparkline: {
            enabled: true,
        }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#service-chart-03"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#service-chart-04").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [25, 27, 24, 26]
    }],
    colors: ["#1ee2ac"],
      chart: {
      height: 65,
      width: 140,
      type: 'area',
      sparkline: {
            enabled: true,
        }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#service-chart-04"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#service-chart-05").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [25, 23, 28, 23]
    }],
    colors: ["#ffffff"],
      chart: {
      height: 65,
      width: 140,
      type: 'area',
      sparkline: {
            enabled: true,
        }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#service-chart-05"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
/*-------------- Service Chart End ----------------*/

/*-------------- Wave Chart ----------------*/
function getNewSeries(e, t) {
  var a = e + TICKINTERVAL;
  lastDate = a;
  for (var n = 0; n < data.length - 10; n++) data[n].x = a - XAXISRANGE - TICKINTERVAL, data[n].y = 0;
  data.push({
    x: a,
    y: Math.floor(Math.random() * (t.max - t.min + 1)) + t.min
  })
}
if (jQuery("#chart-9").length) {
    var chart9 = new ApexCharts(document.querySelector("#chart-9"), options);
    chart9.render(), window.setInterval(function() {
        getNewSeries(lastDate, {
            min: 10,
            max: 90
        }), jQuery("#chart-9").length && chart9.updateSeries([{
            data: data
        }])
    }, 1e3)
}

function generateData(e, t, a) {
    for (var n = 0, o = []; n < t;) {
        var r = Math.floor(750 * Math.random()) + 1,
            i = Math.floor(Math.random() * (a.max - a.min + 1)) + a.min,
            c = Math.floor(61 * Math.random()) + 15;
        o.push([r, i, c]), 864e5, n++
    }
    return o
}
options = {
    chart: {
        height: 440,
        type: "bubble",
        stacked: !1,
        toolbar: {
            show: !1
        },
        animations: {
            enabled: !0,
            easing: "linear",
            dynamicAnimation: {
                speed: 1e3
            }
        },
        sparkline: {
            enabled: !0
        },
        group: "sparklines"
    },
    dataLabels: {
        enabled: !1
    },
    series: [{
        name: "Bubble1",
        data: generateData(new Date("11 Feb 2017 GMT").getTime(), 10, {
            min: 10,
            max: 60
        })
    }, {
        name: "Bubble2",
        data: generateData(new Date("11 Feb 2017 GMT").getTime(), 10, {
            min: 10,
            max: 60
        })
    }, {
        name: "Bubble3",
        data: generateData(new Date("11 Feb 2017 GMT").getTime(), 10, {
            min: 10,
            max: 60
        })
    }, {
        name: "Bubble4",
        data: generateData(new Date("11 Feb 2017 GMT").getTime(), 10, {
            min: 10,
            max: 60
        })
    }],
    fill: {
        opacity: .8
    },
    title: {
        show: !1
    },
    xaxis: {
        tickAmount: 8,
        type: "category",
        labels: {
            show: !1
        }
    },
    yaxis: {
        max: 70,
        labels: {
            show: !1
        }
    },
    legend: {
        show: !1
    }
};

/*-------------- Wave Chart End ----------------*/

if (jQuery("#site-trafic-chart").length) {
  var options = {
          series: [{
            name: "series1",
            data: [0, 70, 30, 90, 80, 150]
        }, {
          name: 'series2',
          data: [0, 20, 90, 70, 130, 110]
        }],
        colors: ['#fe721c','#4788ff'],
          chart: {
          height: 365,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Product Trends by Month',
          align: 'left'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0
          },
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
        },
        yaxis: {
          title: {
            text: ''
          },
          labels: {
            offsetX: -20,
            offsetY: 0
          },
        }
        };

        if(typeof ApexCharts !== typeof undefined){
          var chart = new ApexCharts(document.querySelector("#site-trafic-chart"), options);
          chart.render();
          const body = document.querySelector('body')
          if (body.classList.contains('dark')) {
            apexChartUpdate(chart, {
              dark: true
            })
          }

          document.addEventListener('ChangeColorMode', function (e) {
            apexChartUpdate(chart, e.detail)
          })
        }
}


/*---------- server charts -------------*/

if (jQuery("#report-chart-02").length) {
    var options = {
      series: [{
      name: 'series1',
      data: [70, 110, 60, 85, 40, 60, 90,60]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 170,
      type: 'area',
      sparkline: {
        enabled: false,
    }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
     show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','sep'],
      labels: {
        offsetX: 0,
        offsetY: 0
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#report-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
    
}
if (jQuery("#report-chart-04").length) {
    var options = {
        series: [{
        name: 'series1',
        data: [30, 100, 60, 120, 40, 80,42]
      }],
      colors: ["#4788ff"],
        chart: {
        height: 180,
        type: 'area',
        sparkline: {
          enabled: false,
      }
      },
      dataLabels: {
        enabled: false
      },
      legend: {
       show: false
      },
      stroke: {
        curve: 'smooth'
      },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','sep']
      },
      yaxis: {
        title: {
          text: ''
        },
        labels: {
        offsetX: -20,
        offsetY: 0
      },
      },
      grid: {
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
      tooltip: {
        x: {
          format: 'dd/MM/yy HH:mm'
        },
      },
      };

      var chart = new ApexCharts(document.querySelector("#report-chart-04"), options);
      chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if(jQuery('#iq-income-chart').length){
  var options = {
      series: [{
      name: 'Lowest Speed',
      data: [30, 50, 35, 60, 40, 60, 60,40,50]
    }, {
      name: 'Highest Speed',
      data: [40, 50, 55, 50, 30, 80, 30,25,68]
    }],
      chart: {
      type: 'bar',
      height: 230,
      stacked: true
    },
    colors: ["#ff4b4b", "#4788ff"],

    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '15%',
        endingShape: 'rounded'
      },
    },
    legend: {
     show: false
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
      labels: {
      offsetX: 0,
      offsetY: 0
    },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
    offsetX: -20,
    offsetY: 0
  },
    },
    fill: {
      opacity: 1
    },
    grid: {
    padding: {
      left: -5,
      right: 0,
      bottom: -15
    }
  },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
    };

    var chart = new ApexCharts(document.querySelector("#iq-income-chart"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#ethernet-chart").length) {
    var options = {
      series: [{
        name: "Desktops",
        data: [30, 23, 27, 20, 25, 18]
    }],
    colors: ['#ff4b4b'],
      chart: {
      height: 100,
      width: 150,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
      enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
    };

    var chart = new ApexCharts(document.querySelector("#ethernet-chart"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#chart-001").length) {
    var options = {
      series: [
      {
        name: "High Time",
        data: [15, 9, 20, 11, 25, 15, 23,18,13,30,28,25]
      },
      {
        name: "Low Time",
        data: [7, 10, 15, 18, 14, 20, 10, 19, 16, 25, 31, 26]
      }
    ],
      chart: {
      height: 290,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2
      },
      toolbar: {
        show: false
      }
    },
    colors: ['#4788ff', '#ff4b4b'],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
      left: -5,
      right: 0,
      bottom: -15
    }
    },
    markers: {
      size: 1
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15'],
      title: {
        text: ''
      }
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
      offsetX: -20,
      offsetY: 0
    },
      min: 5,
      max: 40
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5
    }
    };

    var chart = new ApexCharts(document.querySelector("#chart-001"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#httperror-chart").length) {
  var options = {
      series: [44, 55, 41, 17],
      colors: ['#4788ff', '#ffdd31', '#ff4b4b', '#1ee2ac'],
      chart: {
      type: 'donut',
      height: 200,
      sparkline: {
      enabled: true,
    }
    },

    responsive: [{
      breakpoint: 480,
      options: {
        chart: {

        },
        legend: {
          show: false
        }
      }
    }]
    };


    var chart = new ApexCharts(document.querySelector("#httperror-chart"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if(jQuery('#trafic-chart').length){
   var options = {
      series: [{
      name: 'Net Profit',
      data: [44, 55, 57, 56]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98]
    }],
    colors: ["#ff4b4b", "#4788ff"],
      chart: {
      type: 'bar',
      height: 230
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
      offsetX: -20,
      offsetY: 0
    },
    },
    grid: {
    padding: {
      left: -5,
      right: 0
    }
  },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
    };

    var chart = new ApexCharts(document.querySelector("#trafic-chart"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#activies-chart-01").length) {
  var options = {
      series: [{
      name: 'Net Profit',
      data: [90, 70, 120, 72, 120, 80, 60, 52, 85, 65, 90, 75, 110]
    }],
    colors: ["#4788ff"],
      chart: {
      type: 'bar',
      height: 230
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '20%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'nov', 'dec', 'jan'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
      offsetX: -20,
      offsetY: 0
    },
    },
    grid: {
    padding: {
      left: -5,
      right: 0,
      bottom: -15
    }
  },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
    };

    var chart = new ApexCharts(document.querySelector("#activies-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#activies-chart").length) {
  var options = {
      series: [{
      name: 'Net Profit',
      data: [44, 55, 57, 56, 61, 58]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 87, 105]
    }, {
      name: 'Free Cash Flow',
      data: [35, 41, 36, 26, 45, 48]
    }],
    colors: ["#4788ff", "#ff4b4b", "#1ee2ac"],
      chart: {
      type: 'bar',
      height: 400
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
      offsetX: -20,
      offsetY: 0
    },
    },
    grid: {
    padding: {
      left: -5,
      right: 0,
      bottom: -15
    }
  },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
    };

    var chart = new ApexCharts(document.querySelector("#activies-chart"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".api-chart-01").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [4, 3, 4, 3.5, 4.1]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".api-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".api-chart-02").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [4, 3, 4, 3.5, 4.1]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".api-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".api-chart-03").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [4, 3, 4, 3.5, 4.1]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".api-chart-03"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".api-chart-04").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [4, 3, 4, 3.5, 4.1]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".api-chart-04"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".api-chart-05").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [4, 3, 4, 3.5, 4.1]
    }],
    colors: ["#ff4b4b"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".api-chart-05"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".apitime-chart-01").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [1, 3, 2.2, 3, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".apitime-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".apitime-chart-02").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [1, 3, 2.2, 3, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".apitime-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".apitime-chart-03").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [1, 3, 2.2, 3, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".apitime-chart-03"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".apitime-chart-04").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [1, 3, 2.2, 3, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".apitime-chart-04"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery(".apitime-chart-05").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [1, 3, 2.2, 3, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 30,
      width: 83,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector(".apitime-chart-05"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#home-chart-11").length && am4core.ready(function() {

  am4core.useTheme(am4themes_animated);
// Themes end

// create chart
var chart = am4core.create("home-chart-11", am4charts.GaugeChart);
chart.innerRadius = am4core.percent(82);

/**
 * Normal axis
 */


var axis = chart.xAxes.push(new am4charts.ValueAxis());
axis.min = 0;
axis.max = 100;
axis.strictMinMax = true;
axis.renderer.radius = am4core.percent(80);
axis.renderer.inside = false;
axis.renderer.line.strokeOpacity = 0;
axis.renderer.ticks.template.disabled = false
axis.renderer.ticks.template.strokeOpacity = 0;
axis.renderer.ticks.template.length = 10;
axis.renderer.grid.template.disabled = true;
axis.renderer.labels.template.radius = 20;

/**
 * Axis for ranges
 */

var colorSet = new am4core.ColorSet();

var axis2 = chart.xAxes.push(new am4charts.ValueAxis());
axis2.min = 0;
axis2.max = 100;
axis2.strictMinMax = true;
axis2.renderer.labels.template.disabled = true;
axis2.renderer.ticks.template.disabled = true;
axis2.renderer.grid.template.disabled = true;

var range0 = axis2.axisRanges.create();
range0.value = 0;
range0.endValue = 50;
range0.axisFill.fillOpacity = 1;
range0.axisFill.fill = colorSet.getIndex(0);

range0.axisFill.fill = am4core.color("#4788ff");

var range1 = axis2.axisRanges.create();
range1.value = 50;
range1.endValue = 100;
range1.axisFill.fillOpacity = 1;
range1.axisFill.fill = colorSet.getIndex(2);

range1.axisFill.fill = am4core.color("#ff4b4b");

/**
 * Label
 */

var label = chart.radarContainer.createChild(am4core.Label);
label.isMeasured = false;
label.fontSize = 0;
label.x = am4core.percent(50);
label.y = am4core.percent(100);
label.horizontalCenter = "middle";
label.verticalCenter = "bottom";
label.text = "50%";


/**
 * Hand
 */

var hand = chart.hands.push(new am4charts.ClockHand());
hand.axis = axis2;
hand.innerRadius = am4core.percent(20);
hand.startWidth = 10;
hand.pin.disabled = true;
hand.value = 50;

hand.events.on("propertychanged", function(ev) {
  range0.endValue = ev.target.value;
  range1.value = ev.target.value;
  label.text = axis2.positionToValue(hand.currentPosition).toFixed(1);
  axis2.invalidate();
});

setInterval(function() {
  var value = Math.round(Math.random() * 100);
  var animation = new am4core.Animation(hand, {
    property: "value",
    to: value
  }, 1000, am4core.ease.cubicOut).start();
}, 2000);
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    amChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    amChartUpdate(chart, e.detail)
  })

})); // end am4core.ready()

if (jQuery("#world-map").length) {
    am4core.ready(function() {

  // Themes begin
  am4core.useTheme(am4themes_animated);
  // Themes end

  // Create map instance
  var chart = am4core.create("world-map", am4maps.MapChart);
  // Set map definition
  chart.geodata = am4geodata_worldLow;

  // Set projection
  chart.projection = new am4maps.projections.Miller();

  // Create map polygon series
  var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

  // Exclude Antartica
  polygonSeries.exclude = ["AQ"];

  // Make map load polygon (like country names) data from GeoJSON
  polygonSeries.useGeodata = true;

  // Configure series
  var polygonTemplate = polygonSeries.mapPolygons.template;
  polygonTemplate.fill = '#585858';

  polygonTemplate.tooltipText = "{name}";
  polygonTemplate.polygon.fillOpacity = 0.6;


  // Create hover state and set alternative fill color
  var hs = polygonTemplate.states.create("hover");
  hs.properties.fill = chart.colors.getIndex(0);

  // Add image series
  var imageSeries = chart.series.push(new am4maps.MapImageSeries());
  imageSeries.mapImages.template.propertyFields.longitude = "longitude";
  imageSeries.mapImages.template.propertyFields.latitude = "latitude";
  imageSeries.mapImages.template.tooltipText = "{title}";
  imageSeries.mapImages.template.propertyFields.url = "url";

  var circle = imageSeries.mapImages.template.createChild(am4core.Circle);
  circle.radius = 3;
  circle.propertyFields.fill = "color";

  var circle2 = imageSeries.mapImages.template.createChild(am4core.Circle);
  circle2.radius = 3;
  circle2.propertyFields.fill = "color";


  circle2.events.on("inited", function(event){
    animateBullet(event.target);
  })


  function animateBullet(circle) {
      var animation = circle.animate([{ property: "scale", from: 1, to: 5 }, { property: "opacity", from: 1, to: 0 }], 1000, am4core.ease.circleOut);
      animation.events.on("animationended", function(event){
        animateBullet(event.target.object);
      })
  }

  var colorSet = new am4core.ColorSet();

  imageSeries.data = [ {
    "title": "Brussels",
    "latitude": 50.8371,
    "longitude": 4.3676,
    "color":colorSet.next()
  }, {
    "title": "Copenhagen",
    "latitude": 55.6763,
    "longitude": 12.5681,
    "color":colorSet.next()
  }, {
    "title": "Paris",
    "latitude": 48.8567,
    "longitude": 2.3510,
    "color":colorSet.next()
  }, {
    "title": "Reykjavik",
    "latitude": 64.1353,
    "longitude": -21.8952,
    "color":colorSet.next()
  }, {
    "title": "Moscow",
    "latitude": 55.7558,
    "longitude": 37.6176,
    "color":colorSet.next()
  }, {
    "title": "Madrid",
    "latitude": 40.4167,
    "longitude": -3.7033,
    "color":colorSet.next()
  }, {
    "title": "London",
    "latitude": 51.5002,
    "longitude": -0.1262,
    "url": "http://www.google.co.uk",
    "color":colorSet.next()
  }, {
    "title": "Peking",
    "latitude": 39.9056,
    "longitude": 116.3958,
    "color":colorSet.next()
  }, {
    "title": "New Delhi",
    "latitude": 28.6353,
    "longitude": 77.2250,
    "color":colorSet.next()
  }, {
    "title": "Tokyo",
    "latitude": 35.6785,
    "longitude": 139.6823,
    "url": "http://www.google.co.jp",
    "color":colorSet.next()
  }, {
    "title": "Ankara",
    "latitude": 39.9439,
    "longitude": 32.8560,
    "color":colorSet.next()
  }, {
    "title": "Buenos Aires",
    "latitude": -34.6118,
    "longitude": -58.4173,
    "color":colorSet.next()
  }, {
    "title": "Brasilia",
    "latitude": -15.7801,
    "longitude": -47.9292,
    "color":colorSet.next()
  }, {
    "title": "Ottawa",
    "latitude": 45.4235,
    "longitude": -75.6979,
    "color":colorSet.next()
  }, {
    "title": "Washington",
    "latitude": 38.8921,
    "longitude": -77.0241,
    "color":colorSet.next()
  }, {
    "title": "Kinshasa",
    "latitude": -4.3369,
    "longitude": 15.3271,
    "color":colorSet.next()
  }, {
    "title": "Cairo",
    "latitude": 30.0571,
    "longitude": 31.2272,
    "color":colorSet.next()
  }, {
    "title": "Pretoria",
    "latitude": -25.7463,
    "longitude": 28.1876,
    "color":colorSet.next()
  } ];



  });
  }


/*---------- server 360 charts end -------------*/

if (jQuery("#recent-hits-map").length) {
  am4core.ready(function() {

  // Themes begin
  am4core.useTheme(am4themes_animated);
  // Themes end

  // Create map instance
  var chart = am4core.create("recent-hits-map", am4maps.MapChart);
  // Set map definition
  chart.geodata = am4geodata_worldLow;

  // Set projection
  chart.projection = new am4maps.projections.Miller();

  // Create map polygon series
  var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

  // Exclude Antartica
  polygonSeries.exclude = ["AQ"];

  // Make map load polygon (like country names) data from GeoJSON
  polygonSeries.useGeodata = true;

  // Configure series
  var polygonTemplate = polygonSeries.mapPolygons.template;
  polygonTemplate.fill = '#585858';

  polygonTemplate.tooltipText = "{name}";
  polygonTemplate.polygon.fillOpacity = 0.6;


  // Create hover state and set alternative fill color
  var hs = polygonTemplate.states.create("hover");
  hs.properties.fill = chart.colors.getIndex(0);

  // Add image series
  var imageSeries = chart.series.push(new am4maps.MapImageSeries());
  imageSeries.mapImages.template.propertyFields.longitude = "longitude";
  imageSeries.mapImages.template.propertyFields.latitude = "latitude";
  imageSeries.mapImages.template.tooltipText = "{title}";
  imageSeries.mapImages.template.propertyFields.url = "url";

  var circle = imageSeries.mapImages.template.createChild(am4core.Circle);
  circle.radius = 3;
  circle.propertyFields.fill = "color";

  var circle2 = imageSeries.mapImages.template.createChild(am4core.Circle);
  circle2.radius = 3;
  circle2.propertyFields.fill = "color";


  circle2.events.on("inited", function(event){
    animateBullet(event.target);
  })


  function animateBullet(circle) {
      var animation = circle.animate([{ property: "scale", from: 1, to: 5 }, { property: "opacity", from: 1, to: 0 }], 1000, am4core.ease.circleOut);
      animation.events.on("animationended", function(event){
        animateBullet(event.target.object);
      })
  }

  var colorSet = new am4core.ColorSet();

  imageSeries.data = [ {
    "title": "Brussels",
    "latitude": 50.8371,
    "longitude": 4.3676,
    "color":colorSet.next()
  }, {
    "title": "Copenhagen",
    "latitude": 55.6763,
    "longitude": 12.5681,
    "color":colorSet.next()
  }, {
    "title": "Paris",
    "latitude": 48.8567,
    "longitude": 2.3510,
    "color":colorSet.next()
  }, {
    "title": "Reykjavik",
    "latitude": 64.1353,
    "longitude": -21.8952,
    "color":colorSet.next()
  }, {
    "title": "Moscow",
    "latitude": 55.7558,
    "longitude": 37.6176,
    "color":colorSet.next()
  }, {
    "title": "Madrid",
    "latitude": 40.4167,
    "longitude": -3.7033,
    "color":colorSet.next()
  }, {
    "title": "London",
    "latitude": 51.5002,
    "longitude": -0.1262,
    "url": "http://www.google.co.uk",
    "color":colorSet.next()
  }, {
    "title": "Peking",
    "latitude": 39.9056,
    "longitude": 116.3958,
    "color":colorSet.next()
  }, {
    "title": "New Delhi",
    "latitude": 28.6353,
    "longitude": 77.2250,
    "color":colorSet.next()
  }, {
    "title": "Tokyo",
    "latitude": 35.6785,
    "longitude": 139.6823,
    "url": "http://www.google.co.jp",
    "color":colorSet.next()
  }, {
    "title": "Ankara",
    "latitude": 39.9439,
    "longitude": 32.8560,
    "color":colorSet.next()
  }, {
    "title": "Buenos Aires",
    "latitude": -34.6118,
    "longitude": -58.4173,
    "color":colorSet.next()
  }, {
    "title": "Brasilia",
    "latitude": -15.7801,
    "longitude": -47.9292,
    "color":colorSet.next()
  }, {
    "title": "Ottawa",
    "latitude": 45.4235,
    "longitude": -75.6979,
    "color":colorSet.next()
  }, {
    "title": "Washington",
    "latitude": 38.8921,
    "longitude": -77.0241,
    "color":colorSet.next()
  }, {
    "title": "Kinshasa",
    "latitude": -4.3369,
    "longitude": 15.3271,
    "color":colorSet.next()
  }, {
    "title": "Cairo",
    "latitude": 30.0571,
    "longitude": 31.2272,
    "color":colorSet.next()
  }, {
    "title": "Pretoria",
    "latitude": -25.7463,
    "longitude": 28.1876,
    "color":colorSet.next()
  } ];

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}


if (jQuery("#category-sales-chart").length) var donut = new Morris.Donut({
  element: "category-sales-chart",
  resize: !0,
  colors: ["#0dd6b8", "#ff4b4b", "#1ee2ac"],
  data: [{
    label: "Sales",
    value: 30
  }, {
    label: "Profit",
    value: 12
  }, {
    label: "Loss",
    value: 20
  }, {
    label: "Stock",
    value: 20
  }],
  hideHover: "auto"
});


if (jQuery("#buying-chart-01").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [0, 15, 10, 13, 8, 13, 17, 10, 2]
    }],
    colors: ["#4788ff"],
      chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z","2018-09-19T04:30:00.000Z","2018-09-19T05:30:00.000Z","2018-09-19T06:30:00.000Z","2018-09-19T07:30:00.000Z","2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#buying-chart-01"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#buying-chart-02").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [0, 15, 10, 13, 8, 13, 17, 10, 2]
    }],
    colors: ["#fe721c"],
      chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z","2018-09-19T04:30:00.000Z","2018-09-19T05:30:00.000Z","2018-09-19T06:30:00.000Z","2018-09-19T07:30:00.000Z","2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#buying-chart-02"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#buying-chart-03").length) {
  var options = {
      series: [{
      name: 'series1',
      data: [0, 15, 10, 13, 8, 13, 17, 10, 2]
    }],
    colors: ["#37e6b0"],
      chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
    }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z","2018-09-19T04:30:00.000Z","2018-09-19T05:30:00.000Z","2018-09-19T06:30:00.000Z","2018-09-19T07:30:00.000Z","2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
    };

    var chart = new ApexCharts(document.querySelector("#buying-chart-03"), options);
    chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}


/*-------------Layout - 9 ------*/
if (jQuery("#ecommerce-chart-01").length) {
  var options = {
    series: [{
      name: 'Net Profit',
      data: [5, 15, 25, 35, 45, 55, 45, 35, 25, 15, 5]
     
    }, {
      name: 'Revenue',
      data: [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]
    }],
    chart: {
      type: 'bar',
      height: 350
    },
    colors: ['#fe721c', '#4788ff'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '35%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
      labels: {
        minHeight: 20,
        maxHeight: 20
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    },
    responsive: [{
      breakpoint: 578,
      options: {
        xaxis: {
          labels: {
            minHeight: 48,
            maxHeight: 48
          }
        }
      }
    }]
  };

  var chart = new ApexCharts(document.querySelector("#ecommerce-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#ecommerce-chart-02").length) {
  var options = {
    series: [76],
    chart: {
      type: 'radialBar',
      offsetY: 0,
      width: 300,
      height: 300,
      sparkline: {
        enabled: true
      }
    },
    plotOptions: {
      radialBar: {
        startAngle: -90,
        endAngle: 90,
        track: {
          background: "#e7e7e7",
          strokeWidth: '100%',
          margin: 0, // margin is in pixels

        },
        dataLabels: {
          name: {
            show: false
          },
          value: {
            offsetY: -2,
            fontSize: '22px'
          }
        }
      }
    },
    grid: {
      padding: {
        top: -10
      }
    },

    labels: ['Average Results'],
  };

  var chart = new ApexCharts(document.querySelector("#ecommerce-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#ecommerce-chart-03").length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_material);
    am4core.useTheme(am4themes_animated);
    // Themes end

    // create chart
    var chart = am4core.create("ecommerce-chart-03", am4charts.GaugeChart);
    chart.hiddenState.properties.opacity = 0; // this makes initial fade in effect

    chart.innerRadius = -25;

    var axis = chart.xAxes.push(new am4charts.ValueAxis());
    axis.min = 0;
    axis.max = 100;
    axis.strictMinMax = true;
    axis.renderer.grid.template.stroke = new am4core.InterfaceColorSet().getFor("background");
    axis.renderer.grid.template.strokeOpacity = 0.3;

    var colorSet = new am4core.ColorSet();

    var range0 = axis.axisRanges.create();
    range0.value = 0;
    range0.endValue = 50;
    range0.axisFill.fillOpacity = 1;
    range0.axisFill.fill = colorSet.getIndex(0);
    range0.axisFill.zIndex = - 1;

    var range1 = axis.axisRanges.create();
    range1.value = 50;
    range1.endValue = 80;
    range1.axisFill.fillOpacity = 1;
    range1.axisFill.fill = colorSet.getIndex(2);
    range1.axisFill.zIndex = -1;

    var range2 = axis.axisRanges.create();
    range2.value = 80;
    range2.endValue = 100;
    range2.axisFill.fillOpacity = 1;
    range2.axisFill.fill = colorSet.getIndex(4);
    range2.axisFill.zIndex = -1;

    var hand = chart.hands.push(new am4charts.ClockHand());

    // using chart.setTimeout method as the timeout will be disposed together with a chart
    chart.setTimeout(randomValue, 2000);

    function randomValue() {
      hand.showValue(Math.random() * 100, 1000, am4core.ease.cubicOut);
      chart.setTimeout(randomValue, 2000);
    }

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}

// layout 02
if (jQuery("#hospital-chart-03").length) {
  const options = {
    series: [{
      name: 'Operation',
      data: [44, 25, 10, 60, 50, 25, 40, 20]
    }, {
      name: 'Visitors',
      data: [25, 38, 70, 0, 30, 15, 30, 30]
    }],
    colors: ['#4788ff', '#e8f0ff'],
    chart: {
      type: 'bar',
      height: 340,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    responsive: [{
      breakpoint: 580,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -30,
          offsetY: 0,
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
      },
    },
    xaxis: {
      type: 'category',
      categories: ['India', 'Canada', 'U.S.A', 'Africa', 'London ', 'Europe ','Dubai','Kuvet'],
    },
     yaxis: {
      labels: {
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
        }
     },
    legend: {
      position: 'top',
      offsetX: -35
    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
  };

  const chart = new ApexCharts(document.querySelector("#hospital-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#hospital-chart-04").length) {
  const options = {
    series: [{
      name: 'Success',
      data: [110, 85, 87, 40, 45, 20, 91, 45, 94, 88]
    }, {
      name: 'Failed',
      data: [20, 55, 35, 30, 25, 80, 63, 45, 66, 115]
    }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#37E6B0'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '85%',
      },
    },
    legend: {
      position: 'top',
      offsetX: -35
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
      },
      labels: {
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#hospital-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#hospital-chart-05").length) {
  var options = {
    series: [22, 83, 10, 30],
    colors: ['#876CFE', '#4788FF', '#C33030', '#FE721C'],
    chart: {
      height: 250,
      type: 'pie',
    },
    legend: {
      position: 'bottom',
      offsetX: 0
    },
    labels: ['Cancelled', 'Completed', 'Pending', 'Upcoming'],

  };
  var chart = new ApexCharts(document.querySelector("#hospital-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}


if (jQuery("#hospital-chart-02").length) var donut = new Morris.Donut({
  element: "hospital-chart-02",
  resize: !0,
  colors: ["#FF4B4B", "#37E6B0", "#4788FF", "#FE721C", "#1B223F"],
  data: [{
    label: "New Patient",
    value: 40
  }, {
    label: "Exit Patient",
    value: 12
  }, {
    label: "ICU Patient",
    value: 20
  }, {
    label: "Discharge Patient",
    value: 33
  }, {
    label: "OPD Patient",
    value: 5
  }],
  hideHover: "auto"
});

if (jQuery("#hospital-chart-01").length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create chart instance
    var chart = am4core.create("hospital-chart-01", am4charts.XYChart);
    chart.colors.list = [am4core.color("#fe721c"), am4core.color("#4788ff"), am4core.color("#37e6b0")];
    // Add data
    chart.data = [{
      "year": "1930",
      "italy": 1,
      "germany": 5,
      "uk": 3
    }, {
      "year": "1934",
      "italy": 1,
      "germany": 2,
      "uk": 6
    }, {
      "year": "1938",
      "italy": 2,
      "germany": 3,
      "uk": 1
    }, {
      "year": "1950",
      "italy": 3,
      "germany": 4,
      "uk": 1
    }, {
      "year": "1954",
      "italy": 5,
      "germany": 1,
      "uk": 2
    }, {
      "year": "1958",
      "italy": 3,
      "germany": 2,
      "uk": 1
    }, {
      "year": "1962",
      "italy": 1,
      "germany": 2,
      "uk": 3
    }, {
      "year": "1966",
      "italy": 2,
      "germany": 1,
      "uk": 5
    }, {
      "year": "1970",
      "italy": 3,
      "germany": 5,
      "uk": 2
    }, {
      "year": "1974",
      "italy": 4,
      "germany": 3,
      "uk": 6
    }, {
      "year": "1978",
      "italy": 1,
      "germany": 2,
      "uk": 4
    }];

    // Create category axis
    var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
    categoryAxis.dataFields.category = "year";
    categoryAxis.renderer.opposite = true;

    // Create value axis
    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.renderer.inversed = true;
    valueAxis.title.text = "Place taken";
    valueAxis.renderer.minLabelPosition = 0.01;

    // Create series
    var series1 = chart.series.push(new am4charts.LineSeries());
    series1.dataFields.valueY = "italy";
    series1.dataFields.categoryX = "year";
    series1.name = "Italy";
    series1.bullets.push(new am4charts.CircleBullet());
    series1.tooltipText = "Place taken by {name} in {categoryX}: {valueY}";
    series1.legendSettings.valueText = "{valueY}";
    series1.visible = false;

    var series2 = chart.series.push(new am4charts.LineSeries());
    series2.dataFields.valueY = "germany";
    series2.dataFields.categoryX = "year";
    series2.name = 'Germany';
    series2.bullets.push(new am4charts.CircleBullet());
    series2.tooltipText = "Place taken by {name} in {categoryX}: {valueY}";
    series2.legendSettings.valueText = "{valueY}";

    var series3 = chart.series.push(new am4charts.LineSeries());
    series3.dataFields.valueY = "uk";
    series3.dataFields.categoryX = "year";
    series3.name = 'United Kingdom';
    series3.bullets.push(new am4charts.CircleBullet());
    series3.tooltipText = "Place taken by {name} in {categoryX}: {valueY}";
    series3.legendSettings.valueText = "{valueY}";

    // Add chart cursor
    chart.cursor = new am4charts.XYCursor();
    chart.cursor.behavior = "zoomY";


    let hs1 = series1.segments.template.states.create("hover")
    hs1.properties.strokeWidth = 5;
    series1.segments.template.strokeWidth = 1;

    let hs2 = series2.segments.template.states.create("hover")
    hs2.properties.strokeWidth = 5;
    series2.segments.template.strokeWidth = 1;

    let hs3 = series3.segments.template.states.create("hover")
    hs3.properties.strokeWidth = 5;
    series3.segments.template.strokeWidth = 1;

    // Add legend
    chart.legend = new am4charts.Legend();
    chart.legend.itemContainers.template.events.on("over", function (event) {
      var segments = event.target.dataItem.dataContext.segments;
      segments.each(function (segment) {
        segment.isHover = true;
      })
    })

    chart.legend.itemContainers.template.events.on("out", function (event) {
      var segments = event.target.dataItem.dataContext.segments;
      segments.each(function (segment) {
        segment.isHover = false;
      })
    })

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}


/*---------------------------------------------------------------------
   Editable Table
-----------------------------------------------------------------------*/
const $tableID = $('#table');
 const $BTN = $('#export-btn');
 const $EXPORT = $('#export');

 const newTr = `
<tr class="hide">
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half" contenteditable="true">Example</td>
  <td class="pt-3-half">
    <span class="table-up"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span>
    <span class="table-down"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a></span>
  </td>
  <td>
    <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light">Remove</button></span>
  </td>
</tr>`;

 $('.table-add').on('click', 'i', () => {

   const $clone = $tableID.find('tbody tr').last().clone(true).removeClass('hide table-line');

   if ($tableID.find('tbody tr').length === 0) {

     $('tbody').append(newTr);
   }

   $tableID.find('table').append($clone);
 });

 $tableID.on('click', '.table-remove', function () {

   $(this).parents('tr').detach();
 });

 $tableID.on('click', '.table-up', function () {

   const $row = $(this).parents('tr');

   if ($row.index() === 1) {
     return;
   }

   $row.prev().before($row.get(0));
 });

 $tableID.on('click', '.table-down', function () {

   const $row = $(this).parents('tr');
   $row.next().after($row.get(0));
 });

 // A few jQuery helpers for exporting only
 jQuery.fn.pop = [].pop;
 jQuery.fn.shift = [].shift;

 $BTN.on('click', () => {

   const $rows = $tableID.find('tr:not(:hidden)');
   const headers = [];
   const data = [];

   // Get the headers (add special header logic here)
   $($rows.shift()).find('th:not(:empty)').each(function () {

     headers.push($(this).text().toLowerCase());
   });

   // Turn all existing rows into a loopable array
   $rows.each(function () {
     const $td = $(this).find('td');
     const h = {};

     // Use the headers from earlier to name our hash keys
     headers.forEach((header, i) => {

       h[header] = $td.eq(i).text();
     });

     data.push(h);
   });

   // Output the result
   $EXPORT.text(JSON.stringify(data));
 });

/*---------------------------------------------------------------------
    Form Wizard - 1
-----------------------------------------------------------------------*/

$(document).ready(function(){

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;

    setProgressBar(current);

    $(".next").click(function(){

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //Add Class Active
    $("#top-tab-list li").eq($("fieldset").index(next_fs)).addClass("active");
    $("#top-tab-list li").eq($("fieldset").index(current_fs)).addClass("done");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative',

    });

    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });

    $(".previous").click(function(){

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#top-tab-list li").eq($("fieldset").index(current_fs)).removeClass("active");
    $("#top-tab-list li").eq($("fieldset").index(previous_fs)).removeClass("done");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });

    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }

    $(".submit").click(function(){
    return false;
    })

});

 /*---------------------------------------------------------------------
   validate form wizard
-----------------------------------------------------------------------*/

$(document).ready(function () {

    var navListItems = $('div.setup-panel div a'),
            allWells = $('.setup-content'),
            allNextBtn = $('.nextBtn');

    allWells.hide();

    navListItems.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr('href')),
                $item = $(this);

        if (!$item.hasClass('disabled')) {
            navListItems.addClass('active');
            $item.parent().addClass('active');
            allWells.hide();
            $target.show();
            $target.find('input:eq(0)').focus();
        }
    });

    allNextBtn.click(function(){
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
            curInputs = curStep.find("input[type='text'],input[type='email'],input[type='password'],input[type='url'],textarea"),
            isValid = true;

        $(".form-group").removeClass("has-error");
        for(var i=0; i<curInputs.length; i++){
            if (!curInputs[i].validity.valid){
                isValid = false;
                $(curInputs[i]).closest(".form-group").addClass("has-error");
            }
        }

        if (isValid)
            nextStepWizard.removeAttr('disabled').trigger('click');
    });

    $('div.setup-panel div a.active').trigger('click');
});
 /*---------------------------------------------------------------------
   Vertical form wizard
-----------------------------------------------------------------------*/
$(document).ready(function(){

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;

    setProgressBar(current);

    $(".next").click(function(){

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //Add Class Active
    $("#top-tabbar-vertical li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });

    $(".previous").click(function(){

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#top-tabbar-vertical li").eq($("fieldset").index(current_fs)).removeClass("active");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });

    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }

    $(".submit").click(function(){
    return false;
    })

});


/*---------------------------------------------------------------------
   Profile Image Edit
-----------------------------------------------------------------------*/

$(document).ready(function() {


    var readURL = function(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('.profile-pic').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }


    $(".file-upload").on('change', function(){
        readURL(this);
    });

    $(".upload-button").on('click', function() {
       $(".file-upload").click();
    });
});

// ratting
$(function() {
  if(typeof $.fn.barrating !== typeof undefined){
    $('#example').barrating({
      theme: 'fontawesome-stars'
    });
    $('#bars-number').barrating({
      theme: 'bars-1to10'
    });
    $('#movie-rating').barrating('show',{
      theme: 'bars-movie'
    });
    $('#movie-rating').barrating('set', 'Mediocre');
    $('#pill-rating').barrating({
      theme: 'bars-pill',
      showValues: true,
      showSelectedRating: false,
      onSelect: function(value, text) {
        alert('Selected rating: ' + value);
    }
    });
  } 
  if (typeof $.fn.mdbRate !== typeof undefined) {
    $('#rateMe1').mdbRate();
    $('#face-rating').mdbRate();
  }
});

// quill
if (jQuery("#editor").length) {
  var quill = new Quill('#editor', {
  theme: 'snow'
  });
}

  // With Tooltip
  if (jQuery("#quill-toolbar").length) {
  var quill = new Quill('#quill-toolbar', {
      modules: {
        toolbar: '#quill-tool'
      },
      placeholder: 'Compose an epic...',
      theme: 'snow'
  });
  // Enable all tooltips
  $('[data-toggle="tooltip"]').tooltip();

  // Can control programmatically too
  $('.ql-italic').mouseover();
  setTimeout(function() {
      $('.ql-italic').mouseout();
  }, 2500);
}


  // file upload
  $(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);

  });
  // File Upload//
  // function ekUpload(){
  //   function Init() {

  //     console.log("Upload Initialised");

  //     var fileSelect    = document.getElementById('file-upload'),
  //         fileDrag      = document.getElementById('file-drag'),
  //         submitButton  = document.getElementById('submit-button');

  //     fileSelect.addEventListener('change', fileSelectHandler, false);

  //     // Is XHR2 available?
  //     var xhr = new XMLHttpRequest();
  //     if (xhr.upload) {
  //       // File Drop
  //       fileDrag.addEventListener('dragover', fileDragHover, false);
  //       fileDrag.addEventListener('dragleave', fileDragHover, false);
  //       fileDrag.addEventListener('drop', fileSelectHandler, false);
  //     }
  //   }

  //   function fileDragHover(e) {
  //     var fileDrag = document.getElementById('file-drag');

  //     e.stopPropagation();
  //     e.preventDefault();

  //     fileDrag.className = (e.type === 'dragover' ? 'hover' : 'modal-body file-upload');
  //   }

  //   function fileSelectHandler(e) {
  //     // Fetch FileList object
  //     var files = e.target.files || e.dataTransfer.files;

  //     // Cancel event and hover styling
  //     fileDragHover(e);

  //     // Process all File objects
  //     for (var i = 0, f; f = files[i]; i++) {
  //       parseFile(f);
  //       uploadFile(f);
  //     }
  //   }

  //   // Output
  //   function output(msg) {
  //     // Response
  //     var m = document.getElementById('messages');
  //     m.innerHTML = msg;
  //   }

  //   function parseFile(file) {

  //     console.log(file.name);
  //     output(
  //       '<strong>' + encodeURI(file.name) + '</strong>'
  //     );

  //     // var fileType = file.type;
  //     // console.log(fileType);
  //     var imageName = file.name;

  //     var isGood = (/\.(?=gif|jpg|png|jpeg)/gi).test(imageName);
  //     if (isGood) {
  //       document.getElementById('start-one').classList.add("hidden");
  //       document.getElementById('response').classList.remove("hidden");
  //       document.getElementById('notimage').classList.add("hidden");
  //       // Thumbnail Preview
  //       document.getElementById('file-image').classList.remove("hidden");
  //       document.getElementById('file-image').src = URL.createObjectURL(file);
  //     }
  //     else {
  //       document.getElementById('file-image').classList.add("hidden");
  //       document.getElementById('notimage').classList.remove("hidden");
  //       document.getElementById('start-one').classList.remove("hidden");
  //       document.getElementById('response').classList.add("hidden");
  //       document.getElementById("file-upload-form").reset();
  //     }
  //   }

  //   function setProgressMaxValue(e) {
  //     var pBar = document.getElementById('file-progress');

  //     if (e.lengthComputable) {
  //       pBar.max = e.total;
  //     }
  //   }

  //   function updateFileProgress(e) {
  //     var pBar = document.getElementById('file-progress');

  //     if (e.lengthComputable) {
  //       pBar.value = e.loaded;
  //     }
  //   }

  //   function uploadFile(file) {

  //     var xhr = new XMLHttpRequest(),
  //       fileInput = document.getElementById('class-roster-file'),
  //       pBar = document.getElementById('file-progress'),
  //       fileSizeLimit = 1024; // In MB
  //     if (xhr.upload) {
  //       // Check if file is less than x MB
  //       if (file.size <= fileSizeLimit * 1024 * 1024) {
  //         // Progress bar
  //         pBar.style.display = 'inline';
  //         xhr.upload.addEventListener('loadstart', setProgressMaxValue, false);
  //         xhr.upload.addEventListener('progress', updateFileProgress, false);

  //         // File received / failed
  //         xhr.onreadystatechange = function(e) {
  //           if (xhr.readyState == 4) {
  //             // Everything is good!

  //             // progress.className = (xhr.status == 200 ? "success" : "failure");
  //             // document.location.reload(true);
  //           }
  //         };

  //         // Start upload
  //         xhr.open('POST', document.getElementById('file-upload-form').action, true);
  //         xhr.setRequestHeader('X-File-Name', file.name);
  //         xhr.setRequestHeader('X-File-Size', file.size);
  //         xhr.setRequestHeader('Content-Type', 'multipart/form-data');
  //         xhr.send(file);
  //       } else {
  //         output('Please upload a smaller file (< ' + fileSizeLimit + ' MB).');
  //       }
  //     }
  //   }

  //   // Check for the various File API support.
  //   if (window.File && window.FileList && window.FileReader) {
  //     Init();
  //   } else {
  //     document.getElementById('file-drag').style.display = 'none';
  //   }
  // }
  // ekUpload();

  //  gallary grid
if(typeof $.fn.magnificPopup !== typeof undefined){
  $('.image-popup-vertical-fit').magnificPopup({
      type: 'image',
      mainClass: 'mfp-with-zoom',
      gallery: {
        enabled: true
      },
      zoom: {
        enabled: true,
        duration: 300,
        easing: 'ease-in-out',
        opener: function (openerElement) {
            return openerElement.is('img') ? openerElement : openerElement.find('img');
        }
      }
  });
}

  // gallary masanarry

    var $grid = $('.masonry').masonry({
         itemSelector: '.item',
        columnWidth: '.grid-sizer',
        percentPosition: true
    });
    $grid.imagesLoaded().progress(function () {
        $grid.masonry('layout');
    });
    if(typeof $.fn.magnificPopup !== typeof undefined){
      $('.gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            gallery: {
              enabled: true,
              navigateByImgClick: true,
              preload: [0, 1]
            }
      });
    }

/*---------------------------------------------------------------------
   App Reporting
-----------------------------------------------------------------------*/
if (jQuery("#reporting-chart-01").length) {

  var options = {
    series: [57, 86],
    chart: {
      height: 300,
      type: "radialBar",
      offsetY: -10
    },
    colors: ["#4788ff", "#fe721c"],
    plotOptions: {
      radialBar: {
        startAngle: -135,
        endAngle: 135,
        inverseOrder: true,
        dataLabels: {
          show: true,
          name: {
            show: true,
            fontSize: "16px",
            fontWeight: 600,
            offsetY: -30,
            formatter(val, show, opts) {
              return [opts.globals.seriesNames[0], opts.globals.series[0]];
            }
          },
          value: {
            show: true,
            fontWeight: 600,
            color: "#5CCB87",
            fontSize: "16px"
          },
          total: {
            show: true,
            fontSize: "16px",
            fontWeight: 600,
            color: "#2688EF",
            formatter(opts) {
              return [opts.globals.series[1], opts.globals.seriesNames[1]];
            }
          }
        }
      }
    },
    labels: ["Trials", "Non Trials"]
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-02").length) {
    var options = {
      series: [{
      data: [18, 22, 28, 15,25, 35]
    }],
      chart: {
      height: 240,
      type: 'bar',
      events: {
        click: function(chart, w, e) {
        }
      },

    },
    colors: ["#fe721c","#4788ff","#ff4b4b","#876cfe", "#37e6b0", "#ff4b4b"],
    plotOptions: {
      bar: {
        columnWidth: '45%',
        distributed: true
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    xaxis: {
      categories: [
        ['sun'],
        ['mon'],
        ['tus'],
        ['wed'],
        ['thu'],
        ['fry'],
      ],
      labels: {
        style: {
          colors: ["#4788ff","#37e6b0","#fe721c","#876cfe"],
          fontSize: '12px'
        }
      }
    },
    yaxis: {
      show: false,
    },
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-03").length) {
  var options = {
    chart: {
      type: "area",
      height: 430,
      foreColor: "#999",
      stacked: true,
      dropShadow: {
        enabled: true,
        enabledSeries: [0],
        top: -2,
        left: 2,
        blur: 5,
        opacity: 0.06
      }
    },
    colors: ['#4788ff', '#fe721c'],
    stroke: {
      curve: "smooth",
      width: 3
    },
    dataLabels: {
      enabled: false
    },
    series: [{
      name: 'Total Views',
      data: generateDayWiseTimeSeries(0, 18)
    }, {
      name: 'Unique Views',
      data: generateDayWiseTimeSeries(1, 18)
    }],
    markers: {
      size: 0,
      strokeColor: "#fff",
      strokeWidth: 3,
      strokeOpacity: 1,
      fillOpacity: 1,
      hover: {
        size: 6
      }
    },
    xaxis: {
      type: "datetime",
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      }
    },
    yaxis: {
      labels: {
        offsetX: 14,
        offsetY: -5
      },
      tooltip: {
        enabled: true
      }
    },
    grid: {
      padding: {
        left: -5,
        right: 5
      }
    },
    tooltip: {
      x: {
        format: "dd MMM yyyy"
      },
    },
    legend: {
      position: 'top',
      horizontalAlign: 'left'
    },
    fill: {

      fillOpacity: 0.7
    }
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-03"), options);

  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

  function generateDayWiseTimeSeries(s, count) {
    var values = [[
      4, 3, 10, 9, 29, 19, 25, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5
    ], [
      2, 3, 8, 7, 22, 16, 23, 7, 11, 5, 12, 5, 10, 4, 15, 2, 6, 2
    ]];
    var i = 0;
    var series = [];
    var x = new Date("11 Nov 2012").getTime();
    while (i < count) {
      series.push([x, values[s][i]]);
      x += 86400000;
      i++;
    }
    return series;
  }
}

if (jQuery("#reporting-chart-04").length) {
  am4core.ready(function() {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    /**
     * Define SVG path for target icon
     */
    var targetSVG = "M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z";

    // Create map instance
    var chart = am4core.create("reporting-chart-04", am4maps.MapChart);

    // Set map definition
    chart.geodata = am4geodata_worldLow;

    // Set projection
    chart.projection = new am4maps.projections.Miller();

    // Create map polygon series
    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

    // Exclude Antartica
    polygonSeries.exclude = ["AQ"];

    // Make map load polygon (like country names) data from GeoJSON
    polygonSeries.useGeodata = true;

    // Configure series
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.strokeOpacity = 0.5;
    polygonTemplate.nonScalingStroke = true;

    // create capital markers
    var imageSeries = chart.series.push(new am4maps.MapImageSeries());

    // define template
    var imageSeriesTemplate = imageSeries.mapImages.template;
    var circle = imageSeriesTemplate.createChild(am4core.Sprite);
    circle.scale = 0.4;
    circle.fill = new am4core.InterfaceColorSet().getFor("alternativeBackground");
    circle.path = targetSVG;
    // what about scale...

    // set propertyfields
    imageSeriesTemplate.propertyFields.latitude = "latitude";
    imageSeriesTemplate.propertyFields.longitude = "longitude";

    imageSeriesTemplate.horizontalCenter = "middle";
    imageSeriesTemplate.verticalCenter = "middle";
    imageSeriesTemplate.align = "center";
    imageSeriesTemplate.valign = "middle";
    imageSeriesTemplate.width = 8;
    imageSeriesTemplate.height = 8;
    imageSeriesTemplate.nonScaling = true;
    imageSeriesTemplate.tooltipText = "{title}";
    imageSeriesTemplate.fill = am4core.color("#000");
    imageSeriesTemplate.background.fillOpacity = 0;
    imageSeriesTemplate.background.fill = am4core.color("#ffffff");
    imageSeriesTemplate.setStateOnChildren = true;
    imageSeriesTemplate.states.create("hover");

    imageSeries.data = [{
        "title": "Vienna",
        "latitude": 48.2092,
        "longitude": 16.3728
    }, {
        "title": "Minsk",
        "latitude": 53.9678,
        "longitude": 27.5766
    }, {
        "title": "Brussels",
        "latitude": 50.8371,
        "longitude": 4.3676
    }, {
        "title": "Sarajevo",
        "latitude": 43.8608,
        "longitude": 18.4214
    }, {
        "title": "Sofia",
        "latitude": 42.7105,
        "longitude": 23.3238
    }, {
        "title": "Zagreb",
        "latitude": 45.815,
        "longitude": 15.9785
    }, {
        "title": "Pristina",
        "latitude": 42.666667,
        "longitude": 21.166667
    }, {
        "title": "Prague",
        "latitude": 50.0878,
        "longitude": 14.4205
    }, {
        "title": "Copenhagen",
        "latitude": 55.6763,
        "longitude": 12.5681
    }, {
        "title": "Tallinn",
        "latitude": 59.4389,
        "longitude": 24.7545
    }, {
        "title": "Helsinki",
        "latitude": 60.1699,
        "longitude": 24.9384
    }, {
        "title": "Paris",
        "latitude": 48.8567,
        "longitude": 2.351
    }, {
        "title": "Berlin",
        "latitude": 52.5235,
        "longitude": 13.4115
    }, {
        "title": "Athens",
        "latitude": 37.9792,
        "longitude": 23.7166
    }, {
        "title": "Budapest",
        "latitude": 47.4984,
        "longitude": 19.0408
    }, {
        "title": "Reykjavik",
        "latitude": 64.1353,
        "longitude": -21.8952
    }, {
        "title": "Dublin",
        "latitude": 53.3441,
        "longitude": -6.2675
    }, {
        "title": "Rome",
        "latitude": 41.8955,
        "longitude": 12.4823
    }, {
        "title": "Riga",
        "latitude": 56.9465,
        "longitude": 24.1049
    }, {
        "title": "Vaduz",
        "latitude": 47.1411,
        "longitude": 9.5215
    }, {
        "title": "Vilnius",
        "latitude": 54.6896,
        "longitude": 25.2799
    }, {
        "title": "Luxembourg",
        "latitude": 49.61,
        "longitude": 6.1296
    }, {
        "title": "Skopje",
        "latitude": 42.0024,
        "longitude": 21.4361
    }, {
        "title": "Valletta",
        "latitude": 35.9042,
        "longitude": 14.5189
    }, {
        "title": "Chisinau",
        "latitude": 47.0167,
        "longitude": 28.8497
    }, {
        "title": "Monaco",
        "latitude": 43.7325,
        "longitude": 7.4189
    }, {
        "title": "Podgorica",
        "latitude": 42.4602,
        "longitude": 19.2595
    }, {
        "title": "Amsterdam",
        "latitude": 52.3738,
        "longitude": 4.891
    }, {
        "title": "Oslo",
        "latitude": 59.9138,
        "longitude": 10.7387
    }, {
        "title": "Warsaw",
        "latitude": 52.2297,
        "longitude": 21.0122
    }, {
        "title": "Lisbon",
        "latitude": 38.7072,
        "longitude": -9.1355
    }, {
        "title": "Bucharest",
        "latitude": 44.4479,
        "longitude": 26.0979
    }, {
        "title": "Moscow",
        "latitude": 55.7558,
        "longitude": 37.6176
    }, {
        "title": "San Marino",
        "latitude": 43.9424,
        "longitude": 12.4578
    }, {
        "title": "Belgrade",
        "latitude": 44.8048,
        "longitude": 20.4781
    }, {
        "title": "Bratislava",
        "latitude": 48.2116,
        "longitude": 17.1547
    }, {
        "title": "Ljubljana",
        "latitude": 46.0514,
        "longitude": 14.506
    }, {
        "title": "Madrid",
        "latitude": 40.4167,
        "longitude": -3.7033
    }, {
        "title": "Stockholm",
        "latitude": 59.3328,
        "longitude": 18.0645
    }, {
        "title": "Bern",
        "latitude": 46.948,
        "longitude": 7.4481
    }, {
        "title": "Kiev",
        "latitude": 50.4422,
        "longitude": 30.5367
    }, {
        "title": "London",
        "latitude": 51.5002,
        "longitude": -0.1262
    }, {
        "title": "Gibraltar",
        "latitude": 36.1377,
        "longitude": -5.3453
    }, {
        "title": "Saint Peter Port",
        "latitude": 49.466,
        "longitude": -2.5522
    }, {
        "title": "Douglas",
        "latitude": 54.167,
        "longitude": -4.4821
    }, {
        "title": "Saint Helier",
        "latitude": 49.1919,
        "longitude": -2.1071
    }, {
        "title": "Longyearbyen",
        "latitude": 78.2186,
        "longitude": 15.6488
    }, {
        "title": "Kabul",
        "latitude": 34.5155,
        "longitude": 69.1952
    }, {
        "title": "Yerevan",
        "latitude": 40.1596,
        "longitude": 44.509
    }, {
        "title": "Baku",
        "latitude": 40.3834,
        "longitude": 49.8932
    }, {
        "title": "Manama",
        "latitude": 26.1921,
        "longitude": 50.5354
    }, {
        "title": "Dhaka",
        "latitude": 23.7106,
        "longitude": 90.3978
    }, {
        "title": "Thimphu",
        "latitude": 27.4405,
        "longitude": 89.673
    }, {
        "title": "Bandar Seri Begawan",
        "latitude": 4.9431,
        "longitude": 114.9425
    }, {
        "title": "Phnom Penh",
        "latitude": 11.5434,
        "longitude": 104.8984
    }, {
        "title": "Peking",
        "latitude": 39.9056,
        "longitude": 116.3958
    }, {
        "title": "Nicosia",
        "latitude": 35.1676,
        "longitude": 33.3736
    }, {
        "title": "T'bilisi",
        "latitude": 41.701,
        "longitude": 44.793
    }, {
        "title": "New Delhi",
        "latitude": 28.6353,
        "longitude": 77.225
    }, {
        "title": "Jakarta",
        "latitude": -6.1862,
        "longitude": 106.8063
    }, {
        "title": "Teheran",
        "latitude": 35.7061,
        "longitude": 51.4358
    }, {
        "title": "Baghdad",
        "latitude": 33.3157,
        "longitude": 44.3922
    }, {
        "title": "Jerusalem",
        "latitude": 31.76,
        "longitude": 35.17
    }, {
        "title": "Tokyo",
        "latitude": 35.6785,
        "longitude": 139.6823
    }, {
        "title": "Amman",
        "latitude": 31.9394,
        "longitude": 35.9349
    }, {
        "title": "Astana",
        "latitude": 51.1796,
        "longitude": 71.4475
    }, {
        "title": "Kuwait",
        "latitude": 29.3721,
        "longitude": 47.9824
    }, {
        "title": "Bishkek",
        "latitude": 42.8679,
        "longitude": 74.5984
    }, {
        "title": "Vientiane",
        "latitude": 17.9689,
        "longitude": 102.6137
    }, {
        "title": "Beyrouth / Beirut",
        "latitude": 33.8872,
        "longitude": 35.5134
    }, {
        "title": "Kuala Lumpur",
        "latitude": 3.1502,
        "longitude": 101.7077
    }, {
        "title": "Ulan Bator",
        "latitude": 47.9138,
        "longitude": 106.922
    }, {
        "title": "Pyinmana",
        "latitude": 19.7378,
        "longitude": 96.2083
    }, {
        "title": "Kathmandu",
        "latitude": 27.7058,
        "longitude": 85.3157
    }, {
        "title": "Muscat",
        "latitude": 23.6086,
        "longitude": 58.5922
    }, {
        "title": "Islamabad",
        "latitude": 33.6751,
        "longitude": 73.0946
    }, {
        "title": "Manila",
        "latitude": 14.579,
        "longitude": 120.9726
    }, {
        "title": "Doha",
        "latitude": 25.2948,
        "longitude": 51.5082
    }, {
        "title": "Riyadh",
        "latitude": 24.6748,
        "longitude": 46.6977
    }, {
        "title": "Singapore",
        "latitude": 1.2894,
        "longitude": 103.85
    }, {
        "title": "Seoul",
        "latitude": 37.5139,
        "longitude": 126.9828
    }, {
        "title": "Colombo",
        "latitude": 6.9155,
        "longitude": 79.8572
    }, {
        "title": "Damascus",
        "latitude": 33.5158,
        "longitude": 36.2939
    }, {
        "title": "Taipei",
        "latitude": 25.0338,
        "longitude": 121.5645
    }, {
        "title": "Dushanbe",
        "latitude": 38.5737,
        "longitude": 68.7738
    }, {
        "title": "Bangkok",
        "latitude": 13.7573,
        "longitude": 100.502
    }, {
        "title": "Dili",
        "latitude": -8.5662,
        "longitude": 125.588
    }, {
        "title": "Ankara",
        "latitude": 39.9439,
        "longitude": 32.856
    }, {
        "title": "Ashgabat",
        "latitude": 37.9509,
        "longitude": 58.3794
    }, {
        "title": "Abu Dhabi",
        "latitude": 24.4764,
        "longitude": 54.3705
    }, {
        "title": "Tashkent",
        "latitude": 41.3193,
        "longitude": 69.2481
    }, {
        "title": "Hanoi",
        "latitude": 21.0341,
        "longitude": 105.8372
    }, {
        "title": "Sanaa",
        "latitude": 15.3556,
        "longitude": 44.2081
    }, {
        "title": "Buenos Aires",
        "latitude": -34.6118,
        "longitude": -58.4173
    }, {
        "title": "Bridgetown",
        "latitude": 13.0935,
        "longitude": -59.6105
    }, {
        "title": "Belmopan",
        "latitude": 17.2534,
        "longitude": -88.7713
    }, {
        "title": "Sucre",
        "latitude": -19.0421,
        "longitude": -65.2559
    }, {
        "title": "Brasilia",
        "latitude": -15.7801,
        "longitude": -47.9292
    }, {
        "title": "Ottawa",
        "latitude": 45.4235,
        "longitude": -75.6979
    }, {
        "title": "Santiago",
        "latitude": -33.4691,
        "longitude": -70.642
    }, {
        "title": "Bogota",
        "latitude": 4.6473,
        "longitude": -74.0962
    }, {
        "title": "San Jose",
        "latitude": 9.9402,
        "longitude": -84.1002
    }, {
        "title": "Havana",
        "latitude": 23.1333,
        "longitude": -82.3667
    }, {
        "title": "Roseau",
        "latitude": 15.2976,
        "longitude": -61.39
    }, {
        "title": "Santo Domingo",
        "latitude": 18.479,
        "longitude": -69.8908
    }, {
        "title": "Quito",
        "latitude": -0.2295,
        "longitude": -78.5243
    }, {
        "title": "San Salvador",
        "latitude": 13.7034,
        "longitude": -89.2073
    }, {
        "title": "Guatemala",
        "latitude": 14.6248,
        "longitude": -90.5328
    }, {
        "title": "Ciudad de Mexico",
        "latitude": 19.4271,
        "longitude": -99.1276
    }, {
        "title": "Managua",
        "latitude": 12.1475,
        "longitude": -86.2734
    }, {
        "title": "Panama",
        "latitude": 8.9943,
        "longitude": -79.5188
    }, {
        "title": "Asuncion",
        "latitude": -25.3005,
        "longitude": -57.6362
    }, {
        "title": "Lima",
        "latitude": -12.0931,
        "longitude": -77.0465
    }, {
        "title": "Castries",
        "latitude": 13.9972,
        "longitude": -60.0018
    }, {
        "title": "Paramaribo",
        "latitude": 5.8232,
        "longitude": -55.1679
    }, {
        "title": "Washington D.C.",
        "latitude": 38.8921,
        "longitude": -77.0241
    }, {
        "title": "Montevideo",
        "latitude": -34.8941,
        "longitude": -56.0675
    }, {
        "title": "Caracas",
        "latitude": 10.4961,
        "longitude": -66.8983
    }, {
        "title": "Oranjestad",
        "latitude": 12.5246,
        "longitude": -70.0265
    }, {
        "title": "Cayenne",
        "latitude": 4.9346,
        "longitude": -52.3303
    }, {
        "title": "Plymouth",
        "latitude": 16.6802,
        "longitude": -62.2014
    }, {
        "title": "San Juan",
        "latitude": 18.45,
        "longitude": -66.0667
    }, {
        "title": "Algiers",
        "latitude": 36.7755,
        "longitude": 3.0597
    }, {
        "title": "Luanda",
        "latitude": -8.8159,
        "longitude": 13.2306
    }, {
        "title": "Porto-Novo",
        "latitude": 6.4779,
        "longitude": 2.6323
    }, {
        "title": "Gaborone",
        "latitude": -24.657,
        "longitude": 25.9089
    }, {
        "title": "Ouagadougou",
        "latitude": 12.3569,
        "longitude": -1.5352
    }, {
        "title": "Bujumbura",
        "latitude": -3.3818,
        "longitude": 29.3622
    }, {
        "title": "Yaounde",
        "latitude": 3.8612,
        "longitude": 11.5217
    }, {
        "title": "Bangui",
        "latitude": 4.3621,
        "longitude": 18.5873
    }, {
        "title": "Brazzaville",
        "latitude": -4.2767,
        "longitude": 15.2662
    }, {
        "title": "Kinshasa",
        "latitude": -4.3369,
        "longitude": 15.3271
    }, {
        "title": "Yamoussoukro",
        "latitude": 6.8067,
        "longitude": -5.2728
    }, {
        "title": "Djibouti",
        "latitude": 11.5806,
        "longitude": 43.1425
    }, {
        "title": "Cairo",
        "latitude": 30.0571,
        "longitude": 31.2272
    }, {
        "title": "Asmara",
        "latitude": 15.3315,
        "longitude": 38.9183
    }, {
        "title": "Addis Abeba",
        "latitude": 9.0084,
        "longitude": 38.7575
    }, {
        "title": "Libreville",
        "latitude": 0.3858,
        "longitude": 9.4496
    }, {
        "title": "Banjul",
        "latitude": 13.4399,
        "longitude": -16.6775
    }, {
        "title": "Accra",
        "latitude": 5.5401,
        "longitude": -0.2074
    }, {
        "title": "Conakry",
        "latitude": 9.537,
        "longitude": -13.6785
    }, {
        "title": "Bissau",
        "latitude": 11.8598,
        "longitude": -15.5875
    }, {
        "title": "Nairobi",
        "latitude": -1.2762,
        "longitude": 36.7965
    }, {
        "title": "Maseru",
        "latitude": -29.2976,
        "longitude": 27.4854
    }, {
        "title": "Monrovia",
        "latitude": 6.3106,
        "longitude": -10.8047
    }, {
        "title": "Tripoli",
        "latitude": 32.883,
        "longitude": 13.1897
    }, {
        "title": "Antananarivo",
        "latitude": -18.9201,
        "longitude": 47.5237
    }, {
        "title": "Lilongwe",
        "latitude": -13.9899,
        "longitude": 33.7703
    }, {
        "title": "Bamako",
        "latitude": 12.653,
        "longitude": -7.9864
    }, {
        "title": "Nouakchott",
        "latitude": 18.0669,
        "longitude": -15.99
    }, {
        "title": "Port Louis",
        "latitude": -20.1654,
        "longitude": 57.4896
    }, {
        "title": "Rabat",
        "latitude": 33.9905,
        "longitude": -6.8704
    }, {
        "title": "Maputo",
        "latitude": -25.9686,
        "longitude": 32.5804
    }, {
        "title": "Windhoek",
        "latitude": -22.5749,
        "longitude": 17.0805
    }, {
        "title": "Niamey",
        "latitude": 13.5164,
        "longitude": 2.1157
    }, {
        "title": "Abuja",
        "latitude": 9.058,
        "longitude": 7.4891
    }, {
        "title": "Kigali",
        "latitude": -1.9441,
        "longitude": 30.0619
    }, {
        "title": "Dakar",
        "latitude": 14.6953,
        "longitude": -17.4439
    }, {
        "title": "Freetown",
        "latitude": 8.4697,
        "longitude": -13.2659
    }, {
        "title": "Mogadishu",
        "latitude": 2.0411,
        "longitude": 45.3426
    }, {
        "title": "Pretoria",
        "latitude": -25.7463,
        "longitude": 28.1876
    }, {
        "title": "Mbabane",
        "latitude": -26.3186,
        "longitude": 31.141
    }, {
        "title": "Dodoma",
        "latitude": -6.167,
        "longitude": 35.7497
    }, {
        "title": "Lome",
        "latitude": 6.1228,
        "longitude": 1.2255
    }, {
        "title": "Tunis",
        "latitude": 36.8117,
        "longitude": 10.1761
    }];

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

    });
}

// if (jQuery("#reporting-chart-05").length) {

// }

if (jQuery("#reporting-chart-06").length) {
  var options = {
    series: [{
    name: 'Net Profit',
    data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
  }, {
    name: 'Revenue',
    data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
  }],
    chart: {
    type: 'bar',
    height: 370
  },
    colors: ['#4788ff', '#fe721c'],
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '55%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  xaxis: {
    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
  },
  yaxis: {
    title: {
      text: '$ (thousands)'
    }
  },
  fill: {
    opacity: 1
  },
  tooltip: {
    y: {
      formatter: function (val) {
        return "$ " + val + " thousands"
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-06"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#reporting-chart-07").length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create map instance
    var chart = am4core.create("reporting-chart-07", am4maps.MapChart);

    // Set map definition
    chart.geodata = am4geodata_worldLow;

    // Set projection
    chart.projection = new am4maps.projections.Miller();

    // Series for World map
    var worldSeries = chart.series.push(new am4maps.MapPolygonSeries());
    worldSeries.exclude = ["AQ"];
    worldSeries.useGeodata = true;

    var polygonTemplate = worldSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.fill = chart.colors.getIndex(0);
    polygonTemplate.nonScalingStroke = true;

    // Hover state
    var hs = polygonTemplate.states.create("hover");
    hs.properties.fill = am4core.color("#367B25");

    // Series for United States map
    var usaSeries = chart.series.push(new am4maps.MapPolygonSeries());
    usaSeries.geodata = am4geodata_usaLow;

    var usPolygonTemplate = usaSeries.mapPolygons.template;
    usPolygonTemplate.tooltipText = "{name}";
    usPolygonTemplate.fill = chart.colors.getIndex(1);
    usPolygonTemplate.nonScalingStroke = true;

    // Hover state
    var hs = usPolygonTemplate.states.create("hover");
    hs.properties.fill = am4core.color("#367B25");

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}
if (jQuery("#reporting-chart-08").length) {
  var options = {
    series: [44, 55],
    chart: {
      width: 310,
      type: 'pie',
    },
    labels: ['Men', 'Women'],
    colors: ["#4788ff", "#fe721c"],
    legend: {
      position: 'bottom'
    }

  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-08"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-09").length) {
  var options = {
    series: [{
      name: 'Lowest Speed',
      data: [30, 50, 35, 60, 40, 60, 60, 40, 50]
    }, {
      name: 'Highest Speed',
      data: [40, 50, 55, 50, 30, 80, 30, 25, 68]
    },
   {
        name: 'Highest Speed',
     data: [30, 50, 35, 60, 40, 60, 60, 40, 50]
      }],
    chart: {
      type: 'bar',
      height: 300,
      stacked: true
    },
    colors: ["#4788ff", "#fe721c", "#37e6b0"],

    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '15%',
        endingShape: 'rounded'
      },
    },
    legend: {
      show: false

    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
      labels: {
        offsetX: 0,
        offsetY: 0
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    fill: {
      opacity: 1
    },
    grid: {
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-09"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#reporting-chart-10").length) {
  var options = {
    series: [76, 67, 61, 90, 100],
    chart: {
      height: 390,
      type: 'radialBar',
    },

    plotOptions: {
      radialBar: {
        offsetY: 0,
        startAngle: 0,
        endAngle: 270,
        hollow: {
          margin: 5,
          size: '30%',
          background: 'transparent',
          image: undefined,
        },
        dataLabels: {
          name: {
            show: false,
          },
          value: {
            show: false,
          }
        }
      }
    },
    colors: ["#4788ff", "#fe721c", "#37e6b0", "#ff4b4b", "#876cfe"],
    labels: ['Picture view', 'Comments', 'Video plays', 'Impressions', 'Clicks'],
    legend: {
      show: true,
      floating: true,
      fontSize: '16px',
      position: 'left',
      offsetX: 10,
      offsetY: 15,
      labels: {
        useSeriesColors: true,
      },
      markers: {
        size: 0
      },
      formatter: function (seriesName, opts) {
        return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
      },
      itemMargin: {
        vertical: 3
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          show: false
        }
      }
    }]
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-10"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-11").length) {
  var options = {
    series: [{
      name: 'Cash Flow',
      data: [1.45, 5.42, 5.9, -0.42, -12.6, -18.1, -18.2, -14.16, -11.1, -6.09, 0.34, 3.88, 13.07,
        5.8, 2, 7.37, 8.1, 13.57, 15.75, 17.1, 19.8, -27.03, -54.4, -47.2, -43.3, -18.6, -
        48.6, -41.1, -39.6, -37.6, -29.4, -21.4, -2.4
      ]
    }],
    chart: {
      type: 'bar',
      height: 250,
      sparkline: {
        enabled: true,
      },
    },
    colors: ['#4788ff', '#37e6b0', '#ff4b4b', '#876cfe'],
    plotOptions: {
      bar: {
        colors: {
          ranges: [{
            from: -100,
            to: -46,
            color: '#F15B46'
          }, {
            from: -45,
            to: 0,
            color: '#FEB019'
          }]
        },
        columnWidth: '80%',
      }
    },
    dataLabels: {
      enabled: false,
    },
    yaxis: {

      title: {
        text: 'Growth',
      },
      labels: {
        formatter: function (y) {
          return y.toFixed(0) + "%";
        }
      }
    },
    xaxis: {

      type: 'datetime',
      categories: [
        '2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01', '2011-05-01', '2011-06-01',
        '2011-07-01', '2011-08-01', '2011-09-01', '2011-10-01', '2011-11-01', '2011-12-01',
        '2012-01-01', '2012-02-01', '2012-03-01', '2012-04-01', '2012-05-01', '2012-06-01',
        '2012-07-01', '2012-08-01', '2012-09-01', '2012-10-01', '2012-11-01', '2012-12-01',
        '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01', '2013-05-01', '2013-06-01',
        '2013-07-01', '2013-08-01', '2013-09-01'
      ],
      labels: {

        rotate: -90
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-11"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-12").length) {
  var options = {
    series: [{
      name: 'Top',
      data: [20, 65, 10, 120, 30, 80, 40]

    }, {
      name: 'New',
      data: [40, 0, 100, 50, 90, 40, 20]

    }],
    colors: ["#ff4b4b", "#4788ff"],
    chart: {
      height: 250,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    fill: {
      opacity: 1
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5,

      },

    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    },
    legend: {
      position: 'top',
      offsetX: 0,
    },
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-12"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-13").length) {
  var options = {
    series: [44, 55, 41, 17],
    chart: {
      type: 'donut',

    },
    colors: ['#4788ff', '#37e6b0', '#ff4b4b'],
    labels: ["Desktop", "Mobile", "Tablet"],
    legend: {
      position: 'bottom'
    },

  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-13"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-14").length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create map instance
    var chart = am4core.create("reporting-chart-14", am4maps.MapChart);

    // Set map definition
    chart.geodata = am4geodata_worldLow;

    // Set projection
    chart.projection = new am4maps.projections.Miller();

    // Create map polygon series
    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

    // Exclude Antartica
    polygonSeries.exclude = ["AQ"];

    // Make map load polygon (like country names) data from GeoJSON
    polygonSeries.useGeodata = true;

    // Configure series
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.polygon.fillOpacity = 0.6;


    // Create hover state and set alternative fill color
    var hs = polygonTemplate.states.create("hover");
    hs.properties.fill = chart.colors.getIndex(0);

    // Add image series
    var imageSeries = chart.series.push(new am4maps.MapImageSeries());
    imageSeries.mapImages.template.propertyFields.longitude = "longitude";
    imageSeries.mapImages.template.propertyFields.latitude = "latitude";
    imageSeries.mapImages.template.tooltipText = "{title}";
    imageSeries.mapImages.template.propertyFields.url = "url";

    var circle = imageSeries.mapImages.template.createChild(am4core.Circle);
    circle.radius = 3;
    circle.propertyFields.fill = "color";

    var circle2 = imageSeries.mapImages.template.createChild(am4core.Circle);
    circle2.radius = 3;
    circle2.propertyFields.fill = "color";


    circle2.events.on("inited", function (event) {
      animateBullet(event.target);
    })


    function animateBullet(circle) {
      var animation = circle.animate([{ property: "scale", from: 1, to: 5 }, { property: "opacity", from: 1, to: 0 }], 1000, am4core.ease.circleOut);
      animation.events.on("animationended", function (event) {
        animateBullet(event.target.object);
      })
    }

    var colorSet = new am4core.ColorSet();

    imageSeries.data = [{
      "title": "Brussels",
      "latitude": 50.8371,
      "longitude": 4.3676,
      "color": colorSet.next()
    }, {
      "title": "Copenhagen",
      "latitude": 55.6763,
      "longitude": 12.5681,
      "color": colorSet.next()
    }, {
      "title": "Paris",
      "latitude": 48.8567,
      "longitude": 2.3510,
      "color": colorSet.next()
    }, {
      "title": "Reykjavik",
      "latitude": 64.1353,
      "longitude": -21.8952,
      "color": colorSet.next()
    }, {
      "title": "Moscow",
      "latitude": 55.7558,
      "longitude": 37.6176,
      "color": colorSet.next()
    }, {
      "title": "Madrid",
      "latitude": 40.4167,
      "longitude": -3.7033,
      "color": colorSet.next()
    }, {
      "title": "London",
      "latitude": 51.5002,
      "longitude": -0.1262,
      "url": "http://www.google.co.uk",
      "color": colorSet.next()
    }, {
      "title": "Peking",
      "latitude": 39.9056,
      "longitude": 116.3958,
      "color": colorSet.next()
    }, {
      "title": "New Delhi",
      "latitude": 28.6353,
      "longitude": 77.2250,
      "color": colorSet.next()
    }, {
      "title": "Tokyo",
      "latitude": 35.6785,
      "longitude": 139.6823,
      "url": "http://www.google.co.jp",
      "color": colorSet.next()
    }, {
      "title": "Ankara",
      "latitude": 39.9439,
      "longitude": 32.8560,
      "color": colorSet.next()
    }, {
      "title": "Buenos Aires",
      "latitude": -34.6118,
      "longitude": -58.4173,
      "color": colorSet.next()
    }, {
      "title": "Brasilia",
      "latitude": -15.7801,
      "longitude": -47.9292,
      "color": colorSet.next()
    }, {
      "title": "Ottawa",
      "latitude": 45.4235,
      "longitude": -75.6979,
      "color": colorSet.next()
    }, {
      "title": "Washington",
      "latitude": 38.8921,
      "longitude": -77.0241,
      "color": colorSet.next()
    }, {
      "title": "Kinshasa",
      "latitude": -4.3369,
      "longitude": 15.3271,
      "color": colorSet.next()
    }, {
      "title": "Cairo",
      "latitude": 30.0571,
      "longitude": 31.2272,
      "color": colorSet.next()
    }, {
      "title": "Pretoria",
      "latitude": -25.7463,
      "longitude": 28.1876,
      "color": colorSet.next()
    }];

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}
if (jQuery("#reporting-chart-15").length) {
  var options = {
    series: [{
      name: 'Likes',
      data: [44, 55, 57, 56, 61, 58, 63]
    }, {
      name: 'Comments',
      data: [76, 85, 101, 98, 87, 105, 91]
    }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#fe721c'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
    },
    yaxis: {
      labels:{
        minWidth:20,
        maxWidth:20
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#reporting-chart-15"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#reporting-chart-16").length) {
    var options = {
      series: [76, 67, 61, 90, 100],
      chart: {
        height: 390,
        type: 'radialBar',
      },
      plotOptions: {
        radialBar: {
          offsetY: 0,
          startAngle: 0,
          endAngle: 270,
          hollow: {
            margin: 5,
            size: '30%',
            background: 'transparent',
            image: undefined,
          },
          dataLabels: {
            name: {
              show: false,
            },
            value: {
              show: false,
            }
          }
        }
      },
      colors: ["#4788ff", "#fe721c", "#37e6b0", "#ff4b4b", "#876cfe"],
      labels: ['Facebook', 'Twitter', 'Instagram', 'Google Plus', 'Linkedin'],
      legend: {
        show: true,
        floating: true,
        fontSize: '16px',
        position: 'left',
        offsetX: 10,
        offsetY: 15,
        labels: {
          useSeriesColors: true,
        },
        markers: {
          size: 0
        },
        formatter: function (seriesName, opts) {
          return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
        },
        itemMargin: {
          vertical: 3
        }
      },
      responsive: [{
        breakpoint: 380,        
        options: {
          chart: {
            height: 280
          },
          legend: {
            show: false            
          }
        }
      }]
    };

    var chart = new ApexCharts(document.querySelector("#reporting-chart-16"), options);
    chart.render();
    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      apexChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      apexChartUpdate(chart, e.detail)
    })
}

//crm1 chart 01//
if (jQuery("#crm1-chart-01").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [70, 110, 60, 85, 40, 60, 90, 60]
    }],
    colors: ["#4788ff"],
    chart: {
      height: 300,
      type: 'area',
      sparkline: {
        enabled: false,
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep'],
      labels: {
        offsetX: 0,
        offsetY: 0
      },
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
//crm1 chart 02//
if (jQuery("#crm1-chart-02").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [5, 30, 6, 20, 5, 18, 10]
    }],
    colors: ['#4788ff'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
//crm1 chart 03//
if (jQuery("#crm1-chart-03").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [5, 20, 4, 18, 3, 15, 10]
    }],
    colors: ['#37e6b0'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
//crm1 chart 04//
if (jQuery("#crm1-chart-04").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [5, 20, 6, 18, 5, 15, 4]
    }],
    colors: ['#ff4b4b'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
//crm1 chart 05//
if (jQuery("#crm1-chart-05").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [5, 15, 3, 20, 5, 18, 13]
    }],
    colors: ['#fe721c'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

//crm1 chart 06//
if (jQuery("#crm1-chart-06").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [50, 30, 20, 80, 40, 109, 100]
    }],

    chart: {
      height: 200
    },
    colors: ['#ff4b4b'],
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
        left: -5,
        right: 0
      }
    },

    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },

    },
    tooltip: {

      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-06"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}


//crm1 chart 07//
if (jQuery("#crm1-chart-07").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [60, 80, 60, 90, 60, 109, 100]
    }],

    chart: {
      height: 180
    },
    colors: ['#ffffff'],
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"],
      labels: {
        style: {
          colors: ['#fff', '#fff', '#fff', '#fff', '#fff', '#fff']
        }
      },
      axisBorder: {
        show: false,
      },
    },
    grid: {
      borderColor: '#e7e7e7',
      show: false,
      padding: {
        left: -5,
        right: 0,
      }
    },

    yaxis: {
      title: {
        text: '',
        color: ['#ffffff']
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },

    },
    tooltip: {

      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#crm1-chart-07"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}


// Layouts 15
if (jQuery("#social-chart-05").length) {
  const options = {
    series: [{
      name: 'Likes',
      data: [8, 44, 55, 10, 40, 34, 5]
    }, {
      name: 'Comments',
      data: [0, 25, 10, 70, 25, 30, 25]
    }, {
      name: 'Share',
      data: [0, 44, 20, 35, 22, 22, 10]
    }, {
      name: 'Save',
      data: [0, 25, 10, 15, 40, 10, 8]
    }],
    colors: ['#4788FF', '#FE721C', '#876CFE', '#37E6B0'],
    chart: {
      type: 'bar',
      height: 310,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -30,
          offsetY: 0
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%'
      },
    },
    xaxis: {
      type: 'category',
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    },
    legend: {
      position: 'bottom',
      offsetX: 0,
      offsetY: -10

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
  };
  const chart = new ApexCharts(document.querySelector("#social-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#social-chart-02").length) {
  var options = {
    series: [{
      name: "New Visitor's",
      data: [0, 61, 5, 81, 10, 41, 5, 31, 0]
    }],
    chart: {
      type: 'area',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true
      },
    },
    colors: ['#FE721C'],
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight',
      width: 1,
    }
  };
  var chart = new ApexCharts(document.querySelector("#social-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#social-chart-03").length) {
  var options = {
    series: [{
      name: "New follower's",
      data: [0, 61, 5, 81, 10, 41, 5, 31, 0]
    }],
    chart: {
      type: 'area',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true
      },
    },
    colors: ['#37E6B0'],
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight',
      width: 1,
    }
  };
  var chart = new ApexCharts(document.querySelector("#social-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#social-chart-01").length) {
  const options = {
    series: [{
      name: 'Views',
      data: [85, 60, 95, 60]
    }, {
      name: 'Likes',
      data: [75, 90, 35, 95]
    }],
    chart: {
      type: 'bar'
    },
    colors: ['#4788FF', '#FE721C'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    legend: {
      position: 'bottom',
      offsetX: 0,
      offsetY: -10,
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Facebook', 'Instagram', 'Twitter', 'Linkedin'],
    },
    yaxis: {
      
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          height: 270
        }
      }
    }]
  };

  const chart = new ApexCharts(document.querySelector("#social-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}

if (jQuery("#social-chart-04").length) {
  var options = {
    series: [40],
    chart: {
      height: 250,
      type: 'radialBar',
    },
    stroke: {
      lineCap: "round",
    },
    colors: ["#FF4B4B"],
    labels: ['Images'],
    responsive: [{
      breakpoint: 1199,
      options: {
        chart: {
          height: 300
        }
      }
    }]
  };
  var chart = new ApexCharts(document.querySelector("#social-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
// calender 1 js
if (jQuery('#calendar1').length) {
  document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar1');

    var calendar1 = new FullCalendar.Calendar(calendarEl, {
      plugins: ['dayGrid'],
      timeZone: 'UTC',
      defaultView: 'dayGridMonth',
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth'
      },
      events: [
        {
          groupId: '999',
          title: 'Repeating Event',
          start: '2020-11-16T16:00:00',
          color: '#01041b'
        },
        {
          title: 'Birthday Party',
          start: '2020-11-28T07:00:00',
          color: '#4731b6'
        },
        {
          title: 'Meeting',
          start: '2020-11-12T14:30:00',
          color: '#15ca92'
        },
        {
          title: 'Birthday Party',
          start: '2020-11-02T07:00:00',
          color: '#fe721c'
        },
        {
          title: 'Birthday Party',
          start: '2020-11-13T07:00:00',
          color: '#ff4b4b'
        },

        {
          title: 'Meeting',
          start: '2020-11-12T14:30:00',
          color: '#15ca92'
        },

        {
          title: 'Click for Google',
          url: 'http://google.com/',
          start: '2020-11-28',
          color:'#4731b6'
        },
        {
          title: 'All Day Event',
          start: '2020-12-10',
          color: '#4788ff'
        },
        {
          title: 'Long Event',
          start: '2020-12-07',
          end: '2020-02-10',
          color: '#876cfe'
        },
        {
          groupId: '999',
          title: 'Repeating Event',
          start: '2020-12-10T16:00:00',
          color: '#4788ff'
        },
        {
          groupId: '999',
          title: 'Repeating Event',
          start: '2020-12-16T16:00:00',
          color: '#37e6b0'
        }
      ]
    });
    calendar1.render();
  });
}
// calender 1 js
if (jQuery('#calendar2').length) {
  document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar2');

    var calendar2 = new FullCalendar.Calendar(calendarEl, {
      plugins: ['timeGrid', 'dayGrid', 'list'],
      timeZone: 'UTC',
      defaultView: 'dayGridMonth',
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
      },
      events: [
        {
          title: 'Gold Plan $1500',
          start: '2020-09-01',
          color: '#ff4b4b'

        },
        {
          title: 'Gold Plan $5000',
          start: '2020-09-06',
          color: '#37e6b0' // override!
        },
        {
          title: 'Gold Plan $8000',
          start: '2020-09-10',
          color: '#876cfe'
        },
        {
          title: 'Gold Plan $6000',
          start: '2020-09-15',
          color: '#fe721c'
        },
        {
          title: 'Gold Plan $3000',
          start: '2020-09-16',
          color: '#3788d8'
        },
        {
          title: 'Gold Plan $6000',
          start: '2020-09-24',
          color: '#4788ff'
        },
        {
          title: 'Gold Plan $6000',
          start: '2020-09-25',
          color: '#01041b'
        },

      ]
    });
    calendar2.render();
  });
}


// restirent layout charts

if (jQuery('#resto-chart-01').length) {
  var options = {
    series: [60, 80, 100],
    colors: ["#876CFE", "#FE721C", "#37E6B0"],
    chart: {
      height: 280,
      type: 'radialBar',
    },
    plotOptions: {
      radialBar: {
        dataLabels: {
          name: {
            fontSize: '22px',
          },
          value: {
            fontSize: '16px',
          },
          stroke: {
            colors: '#ffffff'
          },
          total: {
            show: true,
            label: 'Food Dish',
            formatter: function (w) {
              return '100%'
            }
          }
        }
      }
    },
    labels: [' Sea Food', 'Pizza', 'Burger']
  };

  var chart = new ApexCharts(document.querySelector("#resto-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#resto-chart-02").length) {
  var options = {
    series: [80],
    chart: {
      height: 280,
      type: 'radialBar',
    },
    stroke: {
      lineCap: "round",
      width: 1
    },
    colors: ["#FF4B4B"],
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 15,
          size: "60%"
        },
        dataLabels: {
          showOn: "always",
          name: {
            show: false
          },
          value: {
            color: "#FF4B4B",
            fontSize: "27px",
            show: true
          }
        }
      }
    },

    labels: ['Images'],
    responsive: [{
      breakpoint: 1199,
      options: {
        chart: {
          height: 300
        }
      }
    }]
  };
  var chart = new ApexCharts(document.querySelector("#resto-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}


if (jQuery("#resto-chart-03").length) {
  am4core.ready(function () {

    const chart = am4core.create("resto-chart-03", am4charts.XYChart);

    // Add data
    chart.data = [{
      "Progress": 0,
      "month": "Jan"

    }, {
      "month": "Feb",
      "Progress": 1

    }, {
      "month": "Mar",
      "Progress": 3
    }, {
      "month": "Apr",
      "Progress": 2
    }, {
      "month": "May",
      "Progress": 4.7
    }, {
      "year": "Jun",
      "Progress": 5.2
    }, {
      "month": "Jul",
      "Progress": 3.8
    }, {
      "month": "Aug",
      "Progress": 6

    }];

    chart.colors.list = [
      am4core.color("#37e6b0")
    ];
    // Create category axis
    const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
    categoryAxis.dataFields.category = "month";
    categoryAxis.renderer.opposite = false;

    // Create value axis
    const valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.renderer.inversed = false;
    valueAxis.title.text = "";
    valueAxis.renderer.minLabelPosition = 0.01;


    const series2 = chart.series.push(new am4charts.LineSeries());
    series2.dataFields.valueY = "Progress";
    series2.dataFields.categoryX = "month";
    series2.name = 'Progress';
    series2.bullets.push(new am4charts.CircleBullet());
    series2.tooltipText = "Place taken by {name} in {categoryX}: {valueY}";
    series2.legendSettings.valueText = "{valueY}";

    // Add chart cursor
    chart.cursor = new am4charts.XYCursor();
    chart.cursor.behavior = "zoomY";

    let hs2 = series2.segments.template.states.create("hover")
    hs2.properties.strokeWidth = 5;
    series2.segments.template.strokeWidth = 1;

    // Add legend
    chart.legend = new am4charts.Legend();
    chart.legend.itemContainers.template.events.on("over", function (event) {
      let segments = event.target.dataItem.dataContext.segments;
      segments.each(function (segment) {
        segment.isHover = true;
      })
    })

    chart.legend.itemContainers.template.events.on("out", function (event) {
      let segments = event.target.dataItem.dataContext.segments;
      segments.each(function (segment) {
        segment.isHover = false;
      })
    })

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}

// layout 12 - Ecommerce 2
if (jQuery("#ecommerce2-chart-01").length) {
  var options = {
    series: [
      {
        name: "High Time",
        data: [316, 450, 612, 1200, 620, 300, 200, 202, 360, 464, 612, 160]
      }
    ],
    chart: {
      height: 260,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2
      },
      toolbar: {
        show: false
      }
    },
    colors: ['#4788ff'],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    markers: {
      size: 1
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      title: {
        text: ''
      }
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
      min: 20,
      max: 1400
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5
    }
  };

  var chart = new ApexCharts(document.querySelector("#ecommerce2-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#ecommerce2-chart-02").length) {
  const options = {
    series: [{
      name: 'Desktop',
      data: [53, 55, 45, 40, 40, 28, 35, 25, 20, 12, 25, 24, 20, 13, 8]
    }, {
      name: 'Tablet',
      data: [63, 62, 52, 72, 55, 80, 70, 50, 60, 40, 50, 41, 38, 32, 18]
    }, {
      name: 'Mobile',
      data: [150, 135, 144, 115, 120, 114, 133, 124, 100, 94, 96, 90, 82, 76, 86]
    }],
    colors: ['#FF4B4B', '#4788FF', '#37E6B0'],
    chart: {
      type: 'bar',
      height: 290,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%'
      },
    },
    xaxis: {
      show: false
    },
    yaxis: {
      show: false
    },
    legend: {
      position: 'bottom',
      offsetX: 0,
      offsetY: -10

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
  };
  const chart = new ApexCharts(document.querySelector("#ecommerce2-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#ecommerce2-chart-03").length) {
  const options = {
    series: [{
      name: 'Week',
      data: [80, 50, 30, 40, 100, 20],
    }, {
      name: 'Month',
      data: [20, 30, 40, 80, 20, 80],
    }, {
      name: 'Year',
      data: [44, 76, 78, 13, 43, 10],
    }],
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      height: 350,
      type: 'radar',
      dropShadow: {
        enabled: true,
        blur: 1,
        left: 1,
        top: 1
      }
    },
    
    stroke: {
      width: 2
    },
    fill: {
      opacity: 0.1
    },
    markers: {
      size: 0
    },
    xaxis: {
      categories: ['2011', '2012', '2013', '2014', '2015', '2016']
    }
  };

  const chart = new ApexCharts(document.querySelector("#ecommerce2-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery('#ecommerce2-chart-04').length) {
  const options = {
    series: [{
      name: 'Net Profit',
      data: [50, 75, 55, 46, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 70, 80, 90, 90]
    }],
    colors: ["#ffebdf", "#fe721c"],
    chart: {
      type: 'bar',
      height: 170,
      sparkline: {
        enabled: true,
      }
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      show: false
    },
    yaxis: {
      show: false
    },
    grid: {
      padding: {
        left: 0,
        right: 0
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#ecommerce2-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#ecommerce2-chart-05").length) {
  const options = {
    series: [76],
    chart: {
      type: 'radialBar',
      offsetY: 0,
      width: 400,
      sparkline: {
        enabled: true
      }
    },
    plotOptions: {
      radialBar: {
        startAngle: -90,
        endAngle: 90,
        track: {
          background: "#e7e7e7",
          strokeWidth: '100%',
          margin: 0, // margin is in pixels

        },
        dataLabels: {
          name: {
            show: false
          },
          value: {
            offsetY: -2,
            fontSize: '22px'
          }
        }
      }
    },
    grid: {
      padding: {
        top: -10
      }
    },
    labels: ['Average Results'],
  };
  const chart = new ApexCharts(document.querySelector("#ecommerce2-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#ecommerce2-chart-06").length) {
  const options = {
    series: [{
      name: 'Net Profit',
      data: [44, 55, 57, 56, 61, 58]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 87, 105]
    }, {
      name: 'Free Cash Flow',
      data: [35, 41, 36, 26, 45, 48]
    }],
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      type: 'bar',
      height: 185
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    legend: {
      show: false,
    },
    grid: {
      show: false,
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      show: false,
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#ecommerce2-chart-06"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
 }
if (jQuery("#ecommerce2-chart-07").length) {
  var options = {
    series: [{
      name: "Session Duration",
      data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
    },
    {
      name: "Page Views",
      data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
    },
    {
      name: 'Total Visits',
      data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
    }
    ],
    colors: ["#4788ff", "#fe721c", "#37e6b0"],
    chart: {
      height: 260,
      type: 'line',
      zoom: {
        enabled: false
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: [5, 7, 5],
      curve: 'straight',
      dashArray: [0, 8, 5]
    },
    title: {
      text: 'Chart Page Statistics',
      align: 'left'
    },
    legend: {
      offsetY: -12,
      tooltipHoverFormatter: function (val, opts) {
        return val + ' - ' + opts.w.globals.series[opts.seriesIndex][opts.dataPointIndex] + ''
      }
    },
    markers: {
      size: 0,
      hover: {
        sizeOffset: 6
      }
    },
    xaxis: {
      categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan',
        '10 Jan', '11 Jan', '12 Jan'
      ],
    },
    tooltip: {
      y: [
        {
          title: {
            formatter: function (val) {
              return val + " (mins)"
            }
          }
        },
        {
          title: {
            formatter: function (val) {
              return val + " per session"
            }
          }
        },
        {
          title: {
            formatter: function (val) {
              return val;
            }
          }
        }
      ]
    },
    grid: {
      borderColor: '#f1f1f1',
    }
  };

  var chart = new ApexCharts(document.querySelector("#ecommerce2-chart-07"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
 }

/*-------------Fitness Management Chart---------*/

if (jQuery('#fit-progress-chart').length) {
  var options = {
    series: [
      {
        name: "Amount",
        data: [10, 30, 70, 50, 40]
      }
    ],
    chart: {
      height: 170,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2
      },
      toolbar: {
        show: false
      }
    },
    colors: ['#4788ff'],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth'
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      borderColor: '#e7e7e7',
      padding: {
        left: -5,
        right: 0,
        bottom: -15
      }
    },
    markers: {
      size: 1
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr'],
      title: {
        text: ''
      }
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
      min: 10,
      max: 100
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5
    }
  };

  var chart = new ApexCharts(document.querySelector("#fit-progress-chart"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#fit-progress-chart-01").length) {
  const options = {
    series: [{
      name: 'Successful deals',
      data: [60, 40, 50, 80, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 55, 28, 60, 30, 80, 30]
    }],
    colors: ["#fe721c", "#876cfe"],
    chart: {
      height: 320,
      type: 'area',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: false,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
       labels: {
           minHeight: 22,
          maxHeight: 35,
       }
    },
    yaxis: {
      labels: {
          offsetY: 0,
          minWidth: 15,
          maxWidth: 15,
        }
     },
     legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -33
    }
  };

  const chart = new ApexCharts(document.querySelector("#fit-progress-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#fit-progress-chart-02").length) {
  const options = {
    series: [{
      name: 'Likes',
      data: [8, 44, 55, 10, 40, 34, 5]
    }, {
      name: 'Comments',
      data: [0, 25, 10, 70, 25, 30, 25]
    }, {
      name: 'Share',
      data: [0, 44, 20, 35, 22, 22, 10]
    }, {
      name: 'Save',
      data: [0, 25, 10, 15, 40, 10, 8]
    }],
    colors: ['#4788FF', '#FE721C', '#876CFE', '#37E6B0'],
    chart: {
      type: 'bar',
      height: 280,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    options: {
      legend: {
        markers: {
          radius: 12,
        }
      }
    },
    
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0,
         
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%'
      },
    },
    xaxis: {
      type: 'category',
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      labels: {
          minHeight: 22,
          maxHeight: 40,
       }
    },
    yaxis: {
      labels: {
          // offsetX: -17,
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
        }
     },
    legend: {
      position: 'bottom',
      offsetX: 0,
      offsetY: -10

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
  };
  const chart = new ApexCharts(document.querySelector("#fit-progress-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#fit-progress-chart-03").length) {
  const options = {
    series: [{
      name: 'Revenue',
      data: [76, 85, 101, 98, 87, 105, 91]
    }, {
        name: 'Net Profit',
        data: [44, 55, 57, 56, 61, 58, 63]
      }],
    chart: {
      type: 'bar',
      height: 300
    },
    colors: ['#4788ff', '#fe721c'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '45%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      labels:{
        minHeight: 30,
        maxHeight: 30,
      }
    },
    yaxis: {
      title: {
        
      },
      labels: {
        offsetY: 0,
        minWidth: 15,
        maxWidth: 15,
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#fit-progress-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

/*-------------Fitness Management Chart End---------*/

/*-------------Propety Management Chart---------*/

if (jQuery("#property-chart-1").length) {
  const options = {
    series: [{
      name: 'Net Profit',
      data: [5, 15, 25, 35, 45, 35, 25, 15, 5]
    }, {
      name: 'Revenue',
        data: [10, 20, 30, 40, 50, 40, 30, 20, 10]
    }],
    chart: {
      type: 'bar',
      height: 240
    },
    colors: ['#4788ff', '#37e6b0'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },

    dataLabels: {
      enabled: false
    },
    legend: {
      show: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
      labels:{
        minHeight:20,
        maxHeight:20
      },
    },
    yaxis: {
      labels:{
        minWidth:15,
        maxWidth:15
      },
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    },
    
    responsive: [{
      breakpoint: 578,
      options: {
        xaxis: {
          labels: {
            minHeight: 48,
            maxHeight: 48
          }
        }
      }
    }]
 
  };
  const chart = new ApexCharts(document.querySelector("#property-chart-1"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#property-chart-03").length) {
  var options = {
    series: [{
      name: "Active",
      data: [45, 30, 35, 25]
    },
    {
      name: "Inactive",
      data: [25, 10, 15, 5]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property-chart-04").length) {
  var options = {
    series: [{
      name: "Active",
      data: [5, 15, 5, 15]
    },
    {
      name: "Inactive",
      data: [15, 5, 15, 5]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property-chart-05").length) {
  var options = {
    series: [{
      name: "Active",
      data: [25, 35, 30, 45]
    },
    {
      name: "Inactive",
      data: [5, 15, 10, 25]
    }],
    colors: ['#4788ff', '#37e6b0'],
    chart: {
      height: 100,
      width: 150,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#property-chart-06').length) {
  Highcharts.chart('property-chart-06', {
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      height: 380,
      type: 'pie'
    },
    title: {
      text: ''
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
      point: {
        valueSuffix: '%'
      }
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: false
        },
        showInLegend: true
      }
    },
    colors: ["#fe721c", "#4788ff", "#37e6b0", "#ff4b4b"],
    series: [{
      name: 'Brands',
      colorByPoint: true,
      data: [{
        name: 'Commerical',
        y: 30,
        sliced: true,
        selected: true
      }, {
        name: 'Residential',
        y: 55
      }, {
        name: 'Purchased',
        y: 20
      }, {
        name: 'Rent',
        y: 15.85
      }]
    }]
  });
}
if (jQuery("#property-chart-07").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [0, 5, 20, 30, 25, 13, 20, 5, 2]
    }],
    colors: ["#4788ff"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-07"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property-chart-08").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [15, 25, 35, 45, 55, 45, 35, 25, 15]
    }],
    colors: ["#fe721c"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-08"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property-chart-09").length) {
  var options = {
    series: [{
      name: 'series1',
      data: [25, 20, 25, 15, 8, 10, 25, 10, 22]
    }],
    colors: ["#37e6b0"],
    chart: {
      height: 50,
      type: 'area',
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z", "2018-09-19T07:30:00.000Z", "2018-09-19T08:30:00.000Z"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#property-chart-09"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

/*-------------Propety Management Chart End---------*/

/*--------------------School Layout Chart-----------------------*/

if (jQuery('#school-chart-02').length) {
  var donut = new Morris.Donut({
    element: 'school-chart-02',
    resize: true,
    height:170,
    colors: ["#4788ff", "#876cfe", "#37e6b0"],
    data: [
      { label: "82.3%", value: 35 },
      { label: "30.4%", value: 25 },
      { label: "60.3%", value: 40 }
    ],
    hideHover: 'auto'
  });
}
if (jQuery('#school-chart-03').length) {
  var options = {
    series: [{
      name: "Maths",
      data: [
        [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 25], [10.9, 23], [16.4, 20], [16.4, 1.8], [13.6, 0.3]]
    }, {
      name: "Chemistry",
      data: [
        [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 24], [1.9, 13.2], [1.4, 30], [6.4, 8.8], [3.6, 29]]
    }, {
      name: "Physics",
      data: [
        [21.7, 3], [23.6, 3.5], [24.6, 3], [29.9, 3], [21.7, 20], [23, 22], [10.9, 30], [28, 32], [27.1, 0.3], [16.4, 4], [13.6, 28], [19, 5]]
    }, {
      name: "Biology",
      data: [
        [21.7, 4], [23.6, 3.6], [24.6, 8], [29.9, 6], [21.7, 25], [23, 9], [10.9, 28], [28, 29], [27.1, 0.9], [16.4, 20], [13.6, 4], [19, 5]]
    }],
    colors: ["#4788ff", "#37e6b0", "#fe721c", "#876cfe"],
    chart: {
      height: 290,
      type: 'scatter',
      zoom: {
        enabled: true,
        type: 'xy'
      }
    },
    legend: {
      offsetX: 0,
      offsetY: -10,
    },
    xaxis: {
      tickAmount: 10,
      labels: {
        formatter: function (val) {
          return parseFloat(val).toFixed(1)
        },
        labels: {
           minHeight: 22,
          maxHeight: 35,
       }
      }
    },
    yaxis: {
      tickAmount: 7,
      labels: {
          offsetY: 0,
          minWidth: 20,
          maxWidth: 20,
        }
    },


  };

  var chart = new ApexCharts(document.querySelector("#school-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#school-chart-04").length) {
  var options = {
    series: [{
      name: 'Successful deals',
      data: [60, 40, 50, 30, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 55, 28, 60, 30, 80, 30]
    }],
    colors: ["#4788ff", "#37e6b0"],
    chart: {
      height: 270,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: false,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      labels: {
           minHeight: 22,
          maxHeight: 35,
       }
    },
    yaxis: {
      labels: {
          offsetY: 0,
          minWidth: 15,
          maxWidth: 15,
        }
     },
     legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -33
    }
  };

  var chart = new ApexCharts(document.querySelector("#school-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#school-chart-05").length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create map instance
    var chart = am4core.create("school-chart-05", am4maps.MapChart);
    // Set map definition
    chart.geodata = am4geodata_worldLow;

    // Set projection
    chart.projection = new am4maps.projections.Miller();

    // Create map polygon series
    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

    // Exclude Antartica
    polygonSeries.exclude = ["AQ"];

    // Make map load polygon (like country names) data from GeoJSON
    polygonSeries.useGeodata = true;

    // Configure series
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.fill = '#585858';

    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.polygon.fillOpacity = 0.6;


    // Create hover state and set alternative fill color
    var hs = polygonTemplate.states.create("hover");
    hs.properties.fill = chart.colors.getIndex(0);

    // Add image series
    var imageSeries = chart.series.push(new am4maps.MapImageSeries());
    imageSeries.mapImages.template.propertyFields.longitude = "longitude";
    imageSeries.mapImages.template.propertyFields.latitude = "latitude";
    imageSeries.mapImages.template.tooltipText = "{title}";
    imageSeries.mapImages.template.propertyFields.url = "url";

    var circle = imageSeries.mapImages.template.createChild(am4core.Circle);
    circle.radius = 3;
    circle.propertyFields.fill = "color";

    var circle2 = imageSeries.mapImages.template.createChild(am4core.Circle);
    circle2.radius = 3;
    circle2.propertyFields.fill = "color";


    circle2.events.on("inited", function (event) {
      animateBullet(event.target);
    })


    function animateBullet(circle) {
      var animation = circle.animate([{ property: "scale", from: 1, to: 5 }, { property: "opacity", from: 1, to: 0 }], 1000, am4core.ease.circleOut);
      animation.events.on("animationended", function (event) {
        animateBullet(event.target.object);
      })
    }

    var colorSet = new am4core.ColorSet();

    imageSeries.data = [{
      "title": "Brussels",
      "latitude": 50.8371,
      "longitude": 4.3676,
      "color": colorSet.next()
    }, {
      "title": "Copenhagen",
      "latitude": 55.6763,
      "longitude": 12.5681,
      "color": colorSet.next()
    }, {
      "title": "Paris",
      "latitude": 48.8567,
      "longitude": 2.3510,
      "color": colorSet.next()
    }, {
      "title": "Reykjavik",
      "latitude": 64.1353,
      "longitude": -21.8952,
      "color": colorSet.next()
    }, {
      "title": "Moscow",
      "latitude": 55.7558,
      "longitude": 37.6176,
      "color": colorSet.next()
    }, {
      "title": "Madrid",
      "latitude": 40.4167,
      "longitude": -3.7033,
      "color": colorSet.next()
    }, {
      "title": "London",
      "latitude": 51.5002,
      "longitude": -0.1262,
      "url": "http://www.google.co.uk",
      "color": colorSet.next()
    }, {
      "title": "Peking",
      "latitude": 39.9056,
      "longitude": 116.3958,
      "color": colorSet.next()
    }, {
      "title": "New Delhi",
      "latitude": 28.6353,
      "longitude": 77.2250,
      "color": colorSet.next()
    }, {
      "title": "Tokyo",
      "latitude": 35.6785,
      "longitude": 139.6823,
      "url": "http://www.google.co.jp",
      "color": colorSet.next()
    }, {
      "title": "Ankara",
      "latitude": 39.9439,
      "longitude": 32.8560,
      "color": colorSet.next()
    }, {
      "title": "Buenos Aires",
      "latitude": -34.6118,
      "longitude": -58.4173,
      "color": colorSet.next()
    }, {
      "title": "Brasilia",
      "latitude": -15.7801,
      "longitude": -47.9292,
      "color": colorSet.next()
    }, {
      "title": "Ottawa",
      "latitude": 45.4235,
      "longitude": -75.6979,
      "color": colorSet.next()
    }, {
      "title": "Washington",
      "latitude": 38.8921,
      "longitude": -77.0241,
      "color": colorSet.next()
    }, {
      "title": "Kinshasa",
      "latitude": -4.3369,
      "longitude": 15.3271,
      "color": colorSet.next()
    }, {
      "title": "Cairo",
      "latitude": 30.0571,
      "longitude": 31.2272,
      "color": colorSet.next()
    }, {
      "title": "Pretoria",
      "latitude": -25.7463,
      "longitude": 28.1876,
      "color": colorSet.next()
    }];

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

  });
}
if (jQuery("#school-chart-06").length) {
  var options = {
    series: [76],
    chart: {
      height:180,
      type: 'radialBar',
      offsetY: -10
    },
    colors: ["#4788ff"],
    plotOptions: {
      radialBar: {
        startAngle: -180,
        endAngle: 180,
        dataLabels: {
          name: {
            fontSize: '16px',
            color: undefined,
            offsetY: 380
          }
        }
      }
    },
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'dark',
        shadeIntensity: 0.15,
        inverseColors: false,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 50, 65, 91]
      },
    },
    stroke: {
      dashArray: 4
    },
    labels: [''],
  };

  var chart = new ApexCharts(document.querySelector("#school-chart-06"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
/*-------------------- School Layout Chart End ------------------------*/

/*-------------------- Salon Layout Chart Start ------------------------*/

if (jQuery("#salon-chart-02").length) {
  const options = {
    series: [{
      name: 'Hair Style',
      data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
    }, {
        name: 'Makeup',
      data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
    }],
    chart: {
      type: 'bar',
      height: 230
    },
    colors: ['#4788ff', '#37e6b0'],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      offsetY: -10,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      labels: {
        maxHeight: 30,
        minHeight: 30,
      },
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      labels:{
        maxWidth: 20,
        minWidth: 20,
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#salon-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
 //salon2 chart 01//
 if (jQuery("#salon2-chart-01").length) {
  const options = {
        series: [{
          name: "Desktops",
          data: [5, 8, 6, 15, 10, 15, 10,6,5]
      }],
      colors: ['#876cfe'],
        chart: {
        height: 60,
        width: 100,
        type: 'line',
        zoom: {
          enabled: false
        },
        sparkline: {
        enabled: true,
      }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth',
        width: 3
      },
      title: {
        text: '',
        align: 'left'
      },
      grid: {
        row: {
          colors: ['#876cfe', 'transparent'], // takes an array which will be repeated on columns
          opacity: 0.5
        },
      },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      }
      };

      const chart = new ApexCharts(document.querySelector("#salon2-chart-01"), options);
      chart.render();
   const body = document.querySelector('body')
   if (body.classList.contains('dark')) {
     apexChartUpdate(chart, {
       dark: true
     })
   }

   document.addEventListener('ChangeColorMode', function (e) {
     apexChartUpdate(chart, e.detail)
   })
 }
 //salon2 chart 02//
 if(jQuery('#salon2-chart-02').length){
    const options = {
       series: [{
       name: 'Net Profit',
       data: [50, 35, 45, 80, 65]
     }, {
       name: 'Revenue',
       data: [76, 85, 101, 98, 70]
     }],
     colors: ["#c9dcff", "#4788ff"],
       chart: {
       type: 'bar',
       height: 60,
         sparkline: {
           enabled: true,
         }
     },
     legend: {
       show: false
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '45%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 1,
       colors: ['transparent']
     },
     xaxis: {
       categories: ['02:30', '02:45', '03:00', '03:15'],
     },
     yaxis: {
       title: {
         text: ''
       },
       labels: {
       offsetX: 0,
       offsetY: 0
     },
     },
     grid: {
     padding: {
       left: 0,
       right: 0
     }
   },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return "$ " + val + " thousands"
         }
       }
     }
     };

     const chart = new ApexCharts(document.querySelector("#salon2-chart-02"), options);
     chart.render();
   const body = document.querySelector('body')
   if (body.classList.contains('dark')) {
     apexChartUpdate(chart, {
       dark: true
     })
   }

   document.addEventListener('ChangeColorMode', function (e) {
     apexChartUpdate(chart, e.detail)
   })
 }
   //salon2 chart 03//

if (jQuery("#salon2-chart-03").length) {
  const options = {
        series: [{
          name: "Desktops",
          data: [5, 8, 6, 15, 10, 15, 10,6,5]
      }],
      colors: ['#37e6b0'],
        chart: {
        height: 60,
        width: 100,
        type: 'line',
        zoom: {
          enabled: false
        },
        sparkline: {
        enabled: true,
      }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth',
        width: 3
      },
      title: {
        text: '',
        align: 'left'
      },
      grid: {
        row: {
          colors: ['#37e6b0', 'transparent'], // takes an array which will be repeated on columns
          opacity: 0.5
        },
      },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      }
      };

      const chart = new ApexCharts(document.querySelector("#salon2-chart-03"), options);
      chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
 }

    //salon2 chart 04//
if (jQuery("#salon2-chart-04").length) {
  const options = {
       series: [{
       name: 'Net Profit',
       data: [50, 35, 45, 80, 65]
     }, {
       name: 'Revenue',
       data: [76, 85, 101, 98, 70]
     }],
     colors: ["#dcd4ff", "#876cfe"],
       chart: {
       type: 'bar',
       height: 60,
         sparkline: {
           enabled: true,
         }
     },
     legend: {
       show: false
     },
     plotOptions: {
       bar: {
         horizontal: false,
         columnWidth: '45%',
         endingShape: 'rounded'
       },
     },
     dataLabels: {
       enabled: false
     },
     stroke: {
       show: true,
       width: 1,
       colors: ['transparent']
     },
     xaxis: {
       categories: ['02:30', '02:45', '03:00', '03:15'],
     },
     yaxis: {
       title: {
         text: ''
       },
       labels: {
       offsetX: 0,
       offsetY: 0
     },
     },
     grid: {
     padding: {
       left: 0,
       right: 0
     }
   },
     fill: {
       opacity: 1
     },
     tooltip: {
       y: {
         formatter: function (val) {
           return "$ " + val + " thousands"
         }
       }
     }
     };

      const chart = new ApexCharts(document.querySelector("#salon2-chart-04"), options);
      chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
 }
//salon2 chart 05//

 if (jQuery("#salon2-chart-05").length) {
    const options = {
       series: [{
          name: 'Weekly',
          data: [53, 55, 45, 40, 40, 28, 35, 25, 20, 12, 25, 24,20,13,8]
       }, {
          name: 'Monthly',
          data: [63, 62, 52, 72, 55, 80, 70, 50, 60, 40, 50, 41,38, 32, 18]
       }, {
          name: 'Yearly',
          data: [150, 135, 144, 115, 120, 114, 133, 124, 100, 94, 96, 90, 82, 76, 86]
       }],
       colors: ['#FF4B4B', '#4788FF', '#37E6B0' ],
       chart: {
          type: 'bar',
          height: 280,
          stacked: true,
          zoom: {
             enabled: true
          }
       },
       responsive: [{
          breakpoint: 480,
          options: {
             legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
             }
          }
       }],
       plotOptions: {
          bar: {
             horizontal: false,
             columnWidth: '45%'
          },
       },
       xaxis: {
          show:false
       },
       yaxis: {
          show:false
       },
       legend: {
          position: 'bottom',
          offsetX: 0,
          offsetY: -10

       },
       fill: {
          opacity: 1
       },
       dataLabels: {
          enabled: false
       }
    };
    const chart = new ApexCharts(document.querySelector("#salon2-chart-05"), options);
    chart.render();
   const body = document.querySelector('body')
   if (body.classList.contains('dark')) {
     apexChartUpdate(chart, {
       dark: true
     })
   }

   document.addEventListener('ChangeColorMode', function (e) {
     apexChartUpdate(chart, e.detail)
   })
 }
if (jQuery('#salon2-chart-09').length) {
  const options = {
    series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#ffffff", "#ffecec"],
    chart: {
      type: 'bar',
      height: 90,
      sparkline: {
        enabled: true,
      }
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#salon2-chart-09"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#salon2-chart-10').length) {
  const options = {
    series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#e2fcf4", "#49f0d3"],
    chart: {
      type: 'bar',
      height: 90,
      sparkline: {
        enabled: true,
      }
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#salon2-chart-10"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

  /*------salon2-chart-06----*/
  if(jQuery('#salon2-chart-06').length){
       const options = {
           series: [{
           name: "Hair Style",
           data: [
           [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 25], [10.9, 23]]
         },{
           name: "Makeup",
           data: [
           [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 24]]
         },{
           name: "Spa",
           data: [
           [21.7, 4], [23.6, 3.6], [24.6, 8], [29.9, 6], [21.7, 25], [23, 9], [10.9, 28]]
         }],
         colors: ["#ff4b4b","#fe721c","#37e6b0"],
           chart: {
           height: 275,
           type: 'scatter',
           zoom: {
             enabled: true,
             type: 'xy'
           }
         },
         legend: {
           offsetY: -10,
         },
         xaxis: {
           tickAmount: 10,
           labels: {
             formatter: function(val) {
               return parseFloat(val).toFixed(1)
             }          
           }
         },
         yaxis: {
           tickAmount: 7,
           labels: {
          offsetY: 0,
          minWidth: 25,
          maxWidth: 25,
          }
         }
         };

        const chart = new ApexCharts(document.querySelector("#salon2-chart-06"), options);
        chart.render();
    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      apexChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      apexChartUpdate(chart, e.detail)
    })
    }

/*---salon2-chart-07----*/

  if (jQuery("#salon2-chart-07").length && am4core.ready(function() {

am4core.useTheme(am4themes_animated);
// Themes end

// create chart
var chart = am4core.create("salon2-chart-07", am4charts.GaugeChart);
chart.innerRadius = am4core.percent(82);

/**
* Normal axis
*/


var axis = chart.xAxes.push(new am4charts.ValueAxis());
axis.min = 0;
axis.max = 100;
axis.strictMinMax = true;
axis.renderer.radius = am4core.percent(80);
axis.renderer.inside = false;
axis.renderer.line.strokeOpacity = 0;
axis.renderer.ticks.template.disabled = false
axis.renderer.ticks.template.strokeOpacity = 0;
axis.renderer.ticks.template.length = 10;
axis.renderer.grid.template.disabled = true;
axis.renderer.labels.template.radius = 20;

/**
* Axis for ranges
*/

var colorSet = new am4core.ColorSet();

var axis2 = chart.xAxes.push(new am4charts.ValueAxis());
axis2.min = 0;
axis2.max = 100;
axis2.strictMinMax = true;
axis2.renderer.labels.template.disabled = true;
axis2.renderer.ticks.template.disabled = true;
axis2.renderer.grid.template.disabled = true;

var range0 = axis2.axisRanges.create();
range0.value = 0;
range0.endValue = 50;
range0.axisFill.fillOpacity = 1;
range0.axisFill.fill = colorSet.getIndex(0);

range0.axisFill.fill = am4core.color("#4788ff");

var range1 = axis2.axisRanges.create();
range1.value = 50;
range1.endValue = 100;
range1.axisFill.fillOpacity = 1;
range1.axisFill.fill = colorSet.getIndex(2);

range1.axisFill.fill = am4core.color("#c9dcff");

/**
* Label
*/

var label = chart.radarContainer.createChild(am4core.Label);
label.isMeasured = false;
label.fontSize = 0;
label.x = am4core.percent(50);
label.y = am4core.percent(100);
label.horizontalCenter = "middle";
label.verticalCenter = "bottom";
label.text = "50%";


/**
* Hand
*/

var hand = chart.hands.push(new am4charts.ClockHand());
hand.axis = axis2;
hand.innerRadius = am4core.percent(20);
hand.startWidth = 10;
hand.pin.disabled = true;
hand.value = 50;

hand.events.on("propertychanged", function(ev) {
range0.endValue = ev.target.value;
range1.value = ev.target.value;
label.text = axis2.positionToValue(hand.currentPosition).toFixed(1);
axis2.invalidate();
});

setInterval(function() {
var value = Math.round(Math.random() * 100);
var animation = new am4core.Animation(hand, {
property: "value",
to: value
}, 1000, am4core.ease.cubicOut).start();
}, 2000);

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })

}));


  /*--------------- salon2 chart 08----*/
 if(jQuery('#salon2-chart-08').length){
         var donut = new Morris.Donut({
           element: 'salon2-chart-08',
           resize: true,
           colors: ["#876cfe","#fe721c"],
           data: [             
             {label: "Female", value: 30},
             {label: "Male", value: 20}

           ],
           hideHover: 'auto'
         });
     }
/*-------------Payment Layout Chart---------*/

if (jQuery("#payment-layout-chart-1").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [5, 12, 30, 20, 25, 13, 15, 3, 0]
    }],
    colors: ['#37e6b0'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#payment-layout-chart-1"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#payment-layout-chart-2").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [15, 8, 25, 30, 23, 13, 22, 5, 0]
    }],
    colors: ['#ff4b4b'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#payment-layout-chart-2"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#payment-layout-chart-3").length) {
  var options = {
    series: [{
      name: "Desktops",
      data: [0, 10, 20, 30, 40, 30, 20, 10, 0]
    }],
    colors: ['#fe721c'],
    chart: {
      height: 60,
      width: 100,
      type: 'line',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    }
  };

  var chart = new ApexCharts(document.querySelector("#payment-layout-chart-3"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#payment-layout-chart-4').length) {
  const options = {
    series: [{
      name: 'Successful deals',
      data: [30, 50, 35, 60, 40, 60, 60]
    }, {
      name: 'Failed deals',
      data: [40, 50, 55, 50, 30, 80, 30]
    }],
    chart: {
      type: 'bar',
      height: 300,
      stacked: true
    },
    colors: ["#4788ff", "#e8f0ff"],

    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '15%',
        endingShape: 'rounded'
      },
    },
    legend: {
      show: false
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['S', 'M', 'T', 'W', 'T', 'F', 'S'],
      labels: {
        minHeight:20,
        maxHeight:20
      }
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
          minWidth: 19,
          maxWidth: 19,
      }
    },
    xaxis: {
      labels: {
        maxHight: 50,
      },
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  const chart = new ApexCharts(document.querySelector("#payment-layout-chart-4"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#payment-layout-chart-5").length) {
  options = {
    series: [44, 55, 33],
    chart: {
      height: 150,
      type: "donut"
    },
    dataLabels: {
      enabled: !1
    },
    colors: ["#37e6b0", "#fe721c", "#4788ff"],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          show: !1
        }
      }
    }],
    legend: {
      position: "right",
      offsetY: 0,
      height: 150
    }
  };

  function appendData() {
    var e = chart.w.globals.series.slice();
    return e.push(Math.floor(100 * Math.random()) + 1), e
  }

  function removeData() {
    var e = chart.w.globals.series.slice();
    return e.pop(), e
  }

  function randomize() {
    return chart.w.globals.series.map(function () {
      return Math.floor(100 * Math.random()) + 1
    })
  }

  function reset() {
    return options.series
  } (chart = new ApexCharts(document.querySelector("#payment-layout-chart-5"), options)).render()
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

// payment 2

if (jQuery("#payment2-chart-01").length) {
  var options = {
     series: [
        {
           name: "Amount",
           data: [572, 600, 670, 1200, 605, 570, 430,432, 568, 572,657,436]
        }
     ],
     chart: {
        height: 250,
        type: 'line',
        dropShadow: {
           enabled: true,
           color: '#000',
           top: 18,
           left: 7,
           blur: 10,
           opacity: 0.2
        },
        toolbar: {
           show: false
        }
     },
     colors: ['#4788ff'],
     dataLabels: {
        enabled: false,
     },
     stroke: {
        curve: 'smooth'
     },
     title: {
        text: '',
        align: 'left'
     },
     grid: {
        borderColor: '#e7e7e7',
        padding: {
           left: -5,
           right: 0,
           bottom: -15
        }
     },
     markers: {
        size: 1
     },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
        title: {
           text: ''
        }
     },
     yaxis: {
        title: {
           text: ''
        },
        labels: {
           offsetX: -20,
           offsetY: 0
        },
        min: 20,
        max: 1400
     },
     legend: {
        position: 'top',
        horizontalAlign: 'right',
        floating: true,
        offsetY: -25,
        offsetX: -5
     }
  };

  var chart = new ApexCharts(document.querySelector("#payment2-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery("#payment2-chart-02").length) {
     var donut = new Morris.Donut({
        element: "payment2-chart-02",
        resize: true,
        colors: ["#FE721C", "#37E6B0", "#4788FF"],
        data: [{
           label: "Shopping",
           value: "24"
        }, {
           label: "Food",
           value: "25"
        }, {
           label: "Travelling",
           value: "50"
        }],
        hideHover: "auto"
     });
  }


/*------------- Payment Layout Chart End ---------*/

/*------------- Hospital 2 Layout Chart Start ---------*/
if (jQuery("#hospital2-chart-01").length) {
  const options = {
    series: [{
      name: "series1",
      data: [80, 5, 4, 35, 57, 55, 80]
    }, {
      name: 'series2',
      data: [160, 115, 124, 40, 20, 48, 28]
    },
    {
      name: 'series3',
      data: [45, 25, 80, 110, 70, 25, 30]
    }],
    colors: ['#876CFE', '#FE721C', '#37E6B0'],
    chart: {
      height: 250,
      type: 'line',
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'],
        opacity: 0
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      labels: {
        minHeight: 22,
        maxHeight: 19
      }
    },
    yaxis: {
      labels: {

        minWidth: 15,
        maxWidth: 15
      }
    },
    legend: {
      show: false
    }
  };

  const chart = new ApexCharts(document.querySelector("#hospital2-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#hospital2-chart-02').length) {
  var options = {
    series: [{
      data: [75, 60, 20, 45]
    }],
    chart: {
      height: 350,
      type: 'bar',
      events: {
        click: function (chart, w, e) {
        }
      },
      sparkline: {
        enabled: false,
      }
    },
    colors: ["#876CFE", "#FF4B4B", "#4788FF", "#FE721C"],
    plotOptions: {
      bar: {
        columnWidth: '45%',
        distributed: true
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    xaxis: {
      categories: [
        ['Cancelled'],
        ['Pending'],
        ['Completed'],
        ['Upcoming'],
      ],
      labels: {
        minHeight: 23,
        maxHeight: 23
      }
    },
    yaxis: {
      labels: {
        // offsetX: -20,
        // offsetY: -27,
        minWidth: 15,
        maxWidth: 15
      }
    }
  };
  var chart = new ApexCharts(document.querySelector("#hospital2-chart-02"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#hospital2-chart-03').length) {
  const options = {
    series: [{
      name: 'Operation',
      data: [60, 55, 41, 37, 22, 43, 21]
    }, {
      name: 'Visit',
      data: [40, 32, 33, 52, 13, 43, 32]
    }],
    chart: {
      type: 'bar',
      height: 290,
      stacked: true
    },
    plotOptions: {
      bar: {
        horizontal: true,
      },
    },
    stroke: {
      width: 1,
      colors: ['#fff']
    },
    colors: ["#FE721C", "#FFEDE6"],
    xaxis: {
      categories: ['United States', 'Russia', 'Ukraine', 'India', 'China', 'Canada'],
      labels: {
        formatter: function (val) {
          return val + "K"
        },
        show: false,
        minHeight: 0,
        maxHeight: 0
      },
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      }
    },
    dataLabels: {
      enabled: false
    },
    yaxis: {
      // offsetX: 50,
      show: false,
      labels: {
        minWidth: 0,
        maxWidth: 0
      }
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return val + "K"
        }
      }
    },
    fill: {
      opacity: 1
    },
    legend: {
      show: true,
      position: 'top',
      horizontalAlign: 'left'
    }
  };
  const chart = new ApexCharts(document.querySelector("#hospital2-chart-03"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#hospital2-chart-04").length) {
  const options = {
    series: [75],
    chart: {
      height: 280,
      type: 'radialBar',
    },
    stroke: {
      lineCap: "round",
    },
    colors: ["#4788FF"],
    labels: [''],
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 15,
          size: "60%"
        },
        dataLabels: {
          showOn: "always",
          name: {
            show: false,

          },
          value: {
            color: "#4788FF",
            fontSize: "35px",
            show: true,
            // offsetY: -20,
          }
        }
      }
    },
    responsive: [{      
      breakpoint: 992,
      options: {
        chart: {
          height: 280
        }
      }
    }]
  };
  const chart = new ApexCharts(document.querySelector("#hospital2-chart-04"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#hospital2-chart-05").length) {
  const options = {
    series: [{
      name: 'Success',
      data: [28, 55, 60, 100, 55, 57, 98]
    }, {
      name: 'Failed',
      data: [25, 22, 17, 40, 16, 18, 36]
    }],
    chart: {
      height: 280,
      type: 'area'
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    colors: ['#FF5151', '#37E6B0'],
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      labels: {
        minHeight: 20,
        maxHeight: 15
      }
    },
    yaxis: {
      labels: {

        minWidth: 15,
        maxWidth: 15
      }

    },
    legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -35
    }
  };
  const chart = new ApexCharts(document.querySelector("#hospital2-chart-05"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery("#hospital2-chart-06").length) {
  var options = {
    series: [{
      name: 'New Patient',
      data: [75, 50, 60, 70, 40, 87, 40]
    }, {
      name: 'Exit Patient',
      data: [35, 23, 25, 35, 23, 37, 23]
    }, {
      name: 'ICU Patient',
      data: [20, 15, 18, 20, 15, 23, 15]
    }, {
      name: 'OPD Patient',
      data: [30, 30, 35, 35, 35, 26, 30]
    }, {
      name: 'Discharge Patient',
      data: [25, 25, 25, 25, 25, 28, 25]
    }],
    colors: ['#876CFE', '#FE721C', '#37E6B0', '#FF5151', '#4788FF'],
    chart: {
      type: 'bar',
      height: 265,
      stacked: true,
      zoom: {
        enabled: true
      }
    },
    stroke: {
      lineCap: "round",
    },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0
        }
      }
    }],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '20%'
      },
    },
    xaxis: {
      type: 'category',
      categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
       labels: {
         minHeight: 22,
         maxHeight:19
      }
    },
    yaxis: {
      labels: {

        minWidth: 18,
        maxWidth: 18
      }
    },
    legend: {
      show: false
      // position: 'bottom',
      // offsetX: 0,
      // offsetY: -10

    },
    fill: {
      opacity: 1
    },
    dataLabels: {
      enabled: false
    }
  };
  var chart = new ApexCharts(document.querySelector("#hospital2-chart-06"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
/*------------- Hospital 2 Layout Chart End ---------*/

// property 2

if (jQuery("#property2-chart-01").length) {
  const options = {
    series: [
    {
      name: "High Time",
      data: [20, 15, 21, 18, 30, 18, 15, 20, 10, 28, 15, 12]
    },
    {
      name: "Low Time",
      data: [7, 10, 23, 10, 19, 25, 18, 25, 30, 15, 31, 28]
    }
  ],
    chart: {
    height: 300,
    type: 'line',
    dropShadow: {
      enabled: false,
      color: '#000',
      top: 18,
      left: 7,
      blur: 10,
      opacity: 0.2
    },
    toolbar: {
      show: false
    }
  },
  colors: ['#fe721c', '#876cfe'],
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: 'straight',
    width: 3
  },
  title: {
    text: '',
    align: 'left'
  },
  grid: {
    borderColor: '#e7e7e7',
    padding: {
    left: -5,
    right: 0,
    bottom: -15
  }
  },
  markers: {
    size: 1
  },
  xaxis: {
    categories: ['02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15'],
    title: {
      text: ''
    },
    labels: {
        minHeight: 22,
        maxHeight: 35
      }
  },
  yaxis: {
    title: {
      text: ''
    },
    labels: {
        offsetX: -17,
        offsetY: 0,
        minWidth: 30,
        maxWidth: 30,
    },
    min: 5,
    max: 40
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  },
  
    responsive: [{
    breakpoint: 678,
    options: {
      xaxis: {
        labels: {
          minHeight: 48,
          maxHeight: 48
        }
      }
    }
  }]

  };

  const chart = new ApexCharts(document.querySelector("#property2-chart-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if(jQuery('#property2-chart-02').length){
var options = {
 series: [{
 name: 'Net Profit',
 data: [50, 35, 45, 80, 65, 50]
}, {
 name: 'Revenue',
 data: [76, 85, 101, 98, 50, 80]
}],
  colors: ["#876cfe", "#dcd4ff"],
 chart: {
 type: 'bar',
 height: 70,
 width: 100,
   sparkline: {
     enabled: true,
   }
},
legend: {
 show: false
},
plotOptions: {
 bar: {
   horizontal: false,
   columnWidth: '55%',
   endingShape: 'rounded'
 },
},
dataLabels: {
 enabled: false
},
stroke: {
 show: true,
 width: 2,
 colors: ['transparent']
},
xaxis: {
 categories: ['02:30', '02:45', '03:00', '03:15'],
},
yaxis: {
 title: {
   text: ''
 },
 labels: {
 offsetX: -20,
 offsetY: 0
},
},
grid: {
padding: {
 left: -5,
 right: 0
}
},
fill: {
 opacity: 1
},
tooltip: {
 y: {
   formatter: function (val) {
     return "$ " + val + " thousands"
   }
 }
}
};

var chart = new ApexCharts(document.querySelector("#property2-chart-02"), options);
chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property2-chart-03").length) {
var options = {
 series: [{
   name: "Desktops",
   data: [5, 30, 6, 20, 5, 18, 10]
}],
  colors: ['#876cfe'],
 chart: {
 height: 60,
 width: 100,
 type: 'line',
 zoom: {
   enabled: false
 },
 sparkline: {
   enabled: true,
 }
},
dataLabels: {
 enabled: false
},
stroke: {
 curve: 'smooth',
 width: 3
},
title: {
 text: '',
 align: 'left'
},
grid: {
 row: {
   colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
   opacity: 0.5
 },
},
xaxis: {
 categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
}
};

var chart = new ApexCharts(document.querySelector("#property2-chart-03"), options);
chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#property2-chart-04").length) {
var donut = new Morris.Donut({
    // barSizeRatio: 0.35,
    // barGap: 6,
    element: "property2-chart-04",
    resize: true,
  colors: ["#876cfe", "#fe721c", "#876cfe", "#fe721c"],
    data: [{
      label: "Commercial",
       value: "38"
    }, {
        label: "Residential",
       value: "29"
    }, {
        label: "Purchased",
       value: "26"
    }, {
        label: "Rent",
       value: "24"
    }],
    hideHover: "auto"
 });
}

/*-------------Hotel Management Chart---------*/

if (jQuery('#hotel-column-1').length) {
  var options = {
    series: [{
      name: 'Net Profit',
      data: [30, 35, 40, 56, 61, 65, 70, 50, 40, 30, 25]
    }],
    chart: {
      type: 'bar',
      height: 140,
      sparkline: {
        enabled: true,
      },
    },
    colors: ["#c9dcff"],
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '25%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      style:{
        color: '#000000'
      },
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#hotel-column-1"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}

if (jQuery('#hotel-chart-1').length) {
  var options = {
    series: [44, 55, 67, 83],
    colors: ["#4788ff", "#37e6b0", "#fe721c", "#876cfe"],
    chart: {
      height: 340,
      type: 'radialBar',
    },
    plotOptions: {
      radialBar: {
        dataLabels: {
          name: {
            fontSize: '22px',
          },
          value: {
            fontSize: '16px',
          },
          total: {
            show: true,
            label: 'Total',
            formatter: function (w) {
              // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
              return 249
            }
          }
        }
      }
    },
    labels: ['36 Rooms', 'Sales', 'Loss', 'Profit'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          height: 280
        }
      }
    }]
  };

  var chart = new ApexCharts(document.querySelector("#hotel-chart-1"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#hotel-chart-2').length) {
  am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    var continents = {
      "AF": 0,
      "AN": 1,
      "AS": 2,
      "EU": 3,
      "NA": 4,
      "OC": 5,
      "SA": 6
    }

    // Create map instance
    var chart = am4core.create("hotel-chart-2", am4maps.MapChart);
    chart.projection = new am4maps.projections.Miller();

    // Create map polygon series for world map
    var worldSeries = chart.series.push(new am4maps.MapPolygonSeries());
    worldSeries.useGeodata = true;
    worldSeries.geodata = am4geodata_worldLow;
    worldSeries.exclude = ["AQ"];

    var worldPolygon = worldSeries.mapPolygons.template;
    worldPolygon.tooltipText = "{name}";
    worldPolygon.nonScalingStroke = true;
    worldPolygon.strokeOpacity = 0.5;
    worldPolygon.fill = am4core.color("#eee");
    worldPolygon.propertyFields.fill = "color";

    var hs = worldPolygon.states.create("hover");
    hs.properties.fill = chart.colors.getIndex(9);


    // Create country specific series (but hide it for now)
    var countrySeries = chart.series.push(new am4maps.MapPolygonSeries());
    countrySeries.useGeodata = true;
    countrySeries.hide();
    countrySeries.geodataSource.events.on("done", function (ev) {
      worldSeries.hide();
      countrySeries.show();
    });

    var countryPolygon = countrySeries.mapPolygons.template;
    countryPolygon.tooltipText = "{name}";
    countryPolygon.nonScalingStroke = true;
    countryPolygon.strokeOpacity = 0.5;
    countryPolygon.fill = am4core.color("#eee");

    var hs = countryPolygon.states.create("hover");
    hs.properties.fill = chart.colors.getIndex(9);

    // Set up click events
    worldPolygon.events.on("hit", function (ev) {
      ev.target.series.chart.zoomToMapObject(ev.target);
      var map = ev.target.dataItem.dataContext.map;
      if (map) {
        ev.target.isHover = false;
        countrySeries.geodataSource.url = "https://www.amcharts.com/lib/4/geodata/json/" + map + ".json";
        countrySeries.geodataSource.load();
      }
    });

    // Set up data for countries
    var data = [];
    for (var id in am4geodata_data_countries2) {
      if (am4geodata_data_countries2.hasOwnProperty(id)) {
        var country = am4geodata_data_countries2[id];
        if (country.maps.length) {
          data.push({
            id: id,
            color: chart.colors.getIndex(continents[country.continent_code]),
            map: country.maps[0]
          });
        }
      }
    }
    worldSeries.data = data;

    // Zoom control
    chart.zoomControl = new am4maps.ZoomControl();

    var homeButton = new am4core.Button();
    homeButton.events.on("hit", function () {
      worldSeries.show();
      countrySeries.hide();
      chart.goHome();
    });

    homeButton.icon = new am4core.Sprite();
    homeButton.padding(7, 5, 7, 5);
    homeButton.width = 30;
    homeButton.icon.path = "M16,8 L14,8 L14,16 L10,16 L10,10 L6,10 L6,16 L2,16 L2,8 L0,8 L8,0 L16,8 Z M16,8";
    homeButton.marginBottom = 10;
    homeButton.parent = chart.zoomControl;
    homeButton.insertBefore(chart.zoomControl.plusButton);

    const body = document.querySelector('body')
    if (body.classList.contains('dark')) {
      amChartUpdate(chart, {
        dark: true
      })
    }

    document.addEventListener('ChangeColorMode', function (e) {
      amChartUpdate(chart, e.detail)
    })
 
  });
}
if (jQuery('#hotel-payment-01').length) {
  var options = {
    series: [{
      name: 'Net Profit',
      data: [15, 25, 20, 30, 40]
    }],
    chart: {
      type: 'bar',
      height: 100,
      width:100,
      sparkline: {
        enabled: true,
      }
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun'],
    },
    yaxis: {
      title: {
        text: '$ (thousands)'
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#hotel-payment-01"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery("#hotel-chart-3").length) {
  const options = {
    series: [{
      name: 'Successful deals',
      data: [90, 70, 80, 60, 70, 90, 90]
    }, {
      name: 'Failed deals',
      data: [70, 85, 58, 90, 60, 100, 60]
    }],
    colors: ["#fe721c", "#4788ff"],
    chart: {
      height: 200,
      type: 'area',
      zoom: {
        enabled: false
      },
      sparkline: {
        enabled: false,
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 3
    },
    title: {
      text: '',
      align: 'left'
    },
    grid: {
      show: true,
      row: {
        colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      labels: {
        minHeight: 22,
        maxHeight: 35,
      }
    },
    yaxis: {
      labels: {
        offsetY: 0,
        minWidth: 20,
        maxWidth: 20,
      }
    },
    legend: {
      show: false,
      position: 'top',
      horizontalAlign: 'left',
      offsetX: -33
    }
  };

  const chart = new ApexCharts(document.querySelector("#hotel-chart-3"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })

}
if (jQuery('#hotel-chart-4').length) {
  var options = {
    series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#ffffff", "#ffecec"],
    chart: {
      type: 'bar',
      height: 90,
      sparkline: {
        enabled: true,
      }
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#hotel-chart-4"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#hotel-chart-5').length) {
  var options = {
    series: [{
      name: 'Net Profit',
      data: [50, 35, 45, 80, 65, 50]
    }, {
      name: 'Revenue',
      data: [76, 85, 101, 98, 50, 80]
    }],
    colors: ["#e2fcf4", "#49f0d3"],
    chart: {
      type: 'bar',
      height: 90,
      sparkline: {
        enabled: true,
      }
    },
    legend: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['02:30', '02:45', '03:00', '03:15'],
    },
    yaxis: {
      title: {
        text: ''
      },
      labels: {
        offsetX: -20,
        offsetY: 0
      },
    },
    grid: {
      padding: {
        left: -5,
        right: 0
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands"
        }
      }
    }
  };

  var chart = new ApexCharts(document.querySelector("#hotel-chart-5"), options);
  chart.render();
  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    apexChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    apexChartUpdate(chart, e.detail)
  })
}
if (jQuery('#hotel-chart-6').length) {
  var donut = new Morris.Donut({
    element: 'hotel-chart-6',
    resize: true,
    colors: ["#4788ff", "#ff4b4b", "#d592ff", "#fe721c"],
    data: [
      { label: "Single", value: 45 },
      { label: "Double", value: 55 },
      { label: "Deluxe", value: 25 },
      { label: "Duplex", value: 30 }
    ],
    hideHover: 'auto'
  });
  
}

if (jQuery("#rating-chart").length && am4core.ready(function () {

  am4core.useTheme(am4themes_animated);
  // Themes end

  // create chart
  var chart = am4core.create("rating-chart", am4charts.GaugeChart);
  chart.innerRadius = am4core.percent(82);

  /**
   * Normal axis
   */


  var axis = chart.xAxes.push(new am4charts.ValueAxis());
  axis.min = 0;
  axis.max = 100;
  axis.strictMinMax = true;
  axis.renderer.radius = am4core.percent(80);
  axis.renderer.inside = false;
  axis.renderer.line.strokeOpacity = 0;
  axis.renderer.ticks.template.disabled = false
  axis.renderer.ticks.template.strokeOpacity = 0;
  axis.renderer.ticks.template.length = 10;
  axis.renderer.grid.template.disabled = true;
  axis.renderer.labels.template.radius = 20;

  /**
   * Axis for ranges
   */

  var colorSet = new am4core.ColorSet();

  var axis2 = chart.xAxes.push(new am4charts.ValueAxis());
  axis2.min = 0;
  axis2.max = 100;
  axis2.strictMinMax = true;
  axis2.renderer.labels.template.disabled = true;
  axis2.renderer.ticks.template.disabled = true;
  axis2.renderer.grid.template.disabled = true;

  var range0 = axis2.axisRanges.create();
  range0.value = 0;
  range0.endValue = 50;
  range0.axisFill.fillOpacity = 1;
  range0.axisFill.fill = colorSet.getIndex(0);

  range0.axisFill.fill = am4core.color("#4788ff");

  var range1 = axis2.axisRanges.create();
  range1.value = 50;
  range1.endValue = 100;
  range1.axisFill.fillOpacity = 1;
  range1.axisFill.fill = colorSet.getIndex(2);

  range1.axisFill.fill = am4core.color("#c9dcff");

  /**
   * Label
   */

  var label = chart.radarContainer.createChild(am4core.Label);
  label.isMeasured = false;
  label.fontSize = 0;
  label.x = am4core.percent(50);
  label.y = am4core.percent(100);
  label.horizontalCenter = "middle";
  label.verticalCenter = "bottom";
  label.text = "50%";


  /**
   * Hand
   */

  var hand = chart.hands.push(new am4charts.ClockHand());
  hand.axis = axis2;
  hand.innerRadius = am4core.percent(20);
  hand.startWidth = 10;
  hand.pin.disabled = true;
  hand.value = 50;

  hand.events.on("propertychanged", function (ev) {
    range0.endValue = ev.target.value;
    range1.value = ev.target.value;
    label.text = axis2.positionToValue(hand.currentPosition).toFixed(1);
    axis2.invalidate();
  });

  setInterval(function () {
    var value = Math.round(Math.random() * 100);
    var animation = new am4core.Animation(hand, {
      property: "value",
      to: value
    }, 1000, am4core.ease.cubicOut).start();
  }, 2000);

  const body = document.querySelector('body')
  if (body.classList.contains('dark')) {
    amChartUpdate(chart, {
      dark: true
    })
  }

  document.addEventListener('ChangeColorMode', function (e) {
    amChartUpdate(chart, e.detail)
  })

})); // end am4core.ready();

/*-------------Hotel Management Chart---------*/


})(jQuery);