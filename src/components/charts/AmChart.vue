<template>
  <div :id="element" :style="'height: '+height+'px;'"></div>
</template>
<script>
import * as am4core from '@amcharts/amcharts4/core'
import * as am4charts from '@amcharts/amcharts4/charts'
import * as am4maps from '@amcharts/amcharts4/maps'
// eslint-disable-next-line camelcase
import am4themes_animated from '@amcharts/amcharts4/themes/animated'
import am4themes_material from '@amcharts/amcharts4/themes/material'
import am4geodataWorldLow from '@amcharts/amcharts4-geodata/worldLow'
// eslint-disable-next-line camelcase
// import am4themes_dark from '@amcharts/amcharts4/themes/amchartsdark'
import { mapGetters } from 'vuex'

am4core.useTheme(am4themes_animated)
export default {
  name: 'AmChart',
  props: {
    element: { type: String, default: 'am-chart' },
    type: { type: String, default: 'bar' },
    option: { type: Object, default: () => {} },
    height: { type: Number, default: 500 }
  },
  computed: {
    ...mapGetters({
      darkMode: 'Setting/darkModeState'
    })
  },
  mounted () {
    let chart
    switch (this.type) {
      case 'line':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.line(chart)
        break
      case 'column':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.column(chart)
        break
      case 'mixes-column':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.mixesColumn(chart)
        break
      case 'stacked':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.stacked(chart)
        break
      case 'bar-line':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.barLine(chart)
        break
      case 'data-based':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.dataBased(chart)
        break
      case 'line-zoom-h':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.lineZoomH(chart)
        break
      case 'line-zoom-v':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.lineZoomV(chart)
        break
      case 'radar':
        chart = am4core.create(this.element, am4charts.RadarChart)
        this.radar(chart)
        break
      case 'polar-scatter':
        chart = am4core.create(this.element, am4charts.RadarChart)
        this.polarScatter(chart)
        break
      case 'polar':
        chart = am4core.create(this.element, am4charts.RadarChart)
        this.polar(chart)
        break
      case 'pie':
        chart = am4core.create(this.element, am4charts.PieChart3D)
        this.pie(chart)
        break
      case 'line-bar':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.lineBar(chart)
        break
      case 'dashboard-map':
        this.map(this.element)
        break
      case 'dashboard-map2':
        this.map2(this.element)
        break
      case 'dashboard2':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.linierChart(chart)
        break
      case 'ht-menu1':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.htMenu1(chart)
        break
      case 'ht-menu2':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.htMenu2(chart)
        break
      case 'ht-menu3':
        chart = am4core.create(this.element, am4charts.XYChart)
        this.htMenu3(chart)
        break
      case 'social':
        chart = am4core.create(this.element, am4charts.RadarChart)
        this.socialChart()
        break
      case 'hospitalchart':
        chart = am4core.create(this.element, am4charts.RadarChart)
        this.hospitalchart()
        break
      default:
        break
    }
  },
  methods: {
    line (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }
      chart.data = this.option.data
      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = this.option.xAxis[0]
      categoryAxis.renderer.grid.template.location = 0
      categoryAxis.renderer.minGridDistance = 30

      categoryAxis.renderer.labels.template.adapter.add('dy', function (dy, target) {
        // eslint-disable-next-line no-self-compare
        if (target.dataItem && target.dataItem.index & 2 === 2) {
          return dy + 25
        }
        return dy
      })
      chart.yAxes.push(new am4charts.ValueAxis())

      // Create series
      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.valueY = this.option.yAxis[0]
      series.dataFields.categoryX = this.option.xAxis[0]
      series.name = this.option.labels[0]
      series.columns.template.tooltipText = '{categoryX}: [bold]{valueY}[/]'
      series.columns.template.fillOpacity = 0.8

      const columnTemplate = series.columns.template
      columnTemplate.strokeWidth = 2
      columnTemplate.strokeOpacity = 1
    },
    column (chart) {
      chart.exporting.menu = new am4core.ExportMenu()
      /* Create axes */

      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = 'year'
      categoryAxis.renderer.minGridDistance = 30

      /* Create value axis */
      chart.yAxes.push(new am4charts.ValueAxis())

      /* Create series */
      const columnSeries = chart.series.push(new am4charts.ColumnSeries())
      columnSeries.name = 'Income'
      columnSeries.dataFields.valueY = 'income'
      columnSeries.dataFields.categoryX = 'year'

      columnSeries.columns.template.tooltipText = '[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]'
      columnSeries.columns.template.propertyFields.fillOpacity = 'fillOpacity'
      columnSeries.columns.template.propertyFields.stroke = 'stroke'
      columnSeries.columns.template.propertyFields.strokeWidth = 'strokeWidth'
      columnSeries.columns.template.propertyFields.strokeDasharray = 'columnDash'
      columnSeries.tooltip.label.textAlign = 'middle'

      const lineSeries = chart.series.push(new am4charts.LineSeries())
      lineSeries.name = 'Expenses'
      lineSeries.dataFields.valueY = 'expenses'
      lineSeries.dataFields.categoryX = 'year'

      lineSeries.stroke = am4core.color(this.option.color)
      lineSeries.strokeWidth = 3
      lineSeries.propertyFields.strokeDasharray = 'lineDash'
      lineSeries.tooltip.label.textAlign = 'middle'

      const bullet = lineSeries.bullets.push(new am4charts.Bullet())
      bullet.fill = am4core.color(this.option.fill) // tooltips grab fill from parent by default
      bullet.tooltipText = '[#fff font-size: 15px]{name} in {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]'
      const circle = bullet.createChild(am4core.Circle)
      circle.radius = 4
      circle.fill = am4core.color('#fff')
      circle.strokeWidth = 3

      chart.data = this.option.data
    },
    mixesColumn (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }
      chart.numberFormatter.numberFormat = "#.#'%'"
      chart.data = this.option.data
      // Create axes

      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = this.option.xAxis[0]
      categoryAxis.renderer.grid.template.location = 0
      categoryAxis.renderer.minGridDistance = 30
      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.title.text = this.option.title
      valueAxis.title.fontWeight = 800

      // Create series

      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.valueY = this.option.yAxis[0]
      series.dataFields.categoryX = this.option.xAxis[0]
      series.clustered = false
      series.tooltipText = this.option.labels[0]

      const series2 = chart.series.push(new am4charts.ColumnSeries())
      series2.dataFields.valueY = this.option.yAxis[1]
      series2.dataFields.categoryX = this.option.xAxis[0]
      series2.clustered = false
      series2.columns.template.width = am4core.percent(50)
      series2.tooltipText = this.option.labels[1]

      chart.cursor = new am4charts.XYCursor()
      chart.cursor.lineX.disabled = true
      chart.cursor.lineY.disabled = true
    },
    stacked (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }
      chart.data = this.option.data

      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = 'year'
      categoryAxis.renderer.grid.template.location = 0
      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.renderer.inside = true
      valueAxis.renderer.labels.template.disabled = true
      valueAxis.min = 0

      // Create series
      const _this = this
      // eslint-disable-next-line no-inner-declarations
      function createSeries (field, name) {
        // Set up series
        const series = chart.series.push(new am4charts.ColumnSeries())
        series.name = name
        series.dataFields.valueY = field
        series.dataFields.categoryX = _this.option.xAxis[0]
        series.sequencedInterpolation = true

        // Make it stacked
        series.stacked = true

        // Configure columns
        series.columns.template.width = am4core.percent(60)
        series.columns.template.tooltipText = '[bold]{name}[/]\n[font-size:14px]{categoryX}: {valueY}'

        // Add label
        const labelBullet = series.bullets.push(new am4charts.LabelBullet())
        labelBullet.label.text = '{valueY}'
        labelBullet.locationY = 0.5

        return series
      }
      for (let j = 0; j < this.option.yAxis.length; j++) {
        createSeries(this.option.yAxis[j], this.option.yAxis[j])
      }
      // Legend
      chart.legend = new am4charts.Legend()
    },
    barLine (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }
      chart.data = this.option.data
      // create category axis for years

      const categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = this.option.yAxis[0]
      categoryAxis.renderer.inversed = true
      categoryAxis.renderer.grid.template.location = 0

      // create value axis for income and expenses

      const valueAxis = chart.xAxes.push(new am4charts.ValueAxis())
      valueAxis.renderer.opposite = true

      // create columns

      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.categoryY = this.option.yAxis[0]
      series.dataFields.valueX = this.option.xAxis[0]
      series.name = this.option.labels[0]
      series.columns.template.fillOpacity = 0.5
      series.columns.template.strokeOpacity = 0
      series.tooltipText = this.option.labels[0] + ' in {categoryY}: {valueX.value}'

      // create line

      const lineSeries = chart.series.push(new am4charts.LineSeries())
      lineSeries.dataFields.categoryY = this.option.yAxis[0]
      lineSeries.dataFields.valueX = this.option.xAxis[1]
      lineSeries.name = this.option.labels[1]
      lineSeries.strokeWidth = 3
      lineSeries.tooltipText = this.option.labels[1] + ' in {categoryY}: {valueX.value}'

      // add bullets
      const circleBullet = lineSeries.bullets.push(new am4charts.CircleBullet())
      circleBullet.circle.fill = am4core.color('#fff')
      circleBullet.circle.strokeWidth = 2

      // add chart cursor
      chart.cursor = new am4charts.XYCursor()
      chart.cursor.behavior = 'zoomY'

      // add legend
      chart.legend = new am4charts.Legend()
    },
    hospitalchart(){
      am4core.ready(function() {

      // Themes begin
      am4core.useTheme(am4themes_animated);
      // Themes end

      // Create chart instance
      var chart = am4core.create("hospital-chart-01", am4charts.XYChart);

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
      series1.visible  = false;

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
      chart.legend.itemContainers.template.events.on("over", function(event){
        var segments = event.target.dataItem.dataContext.segments;
        segments.each(function(segment){
          segment.isHover = true;
        })
      })

      chart.legend.itemContainers.template.events.on("out", function(event){
        var segments = event.target.dataItem.dataContext.segments;
        segments.each(function(segment){
          segment.isHover = false;
        })
      })

      });
    },
    socialChart(){
        am4core.ready(function() {

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

        });
    },
    dataBased (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }
      chart.data = this.option.data
      // Set input format for the dates
      chart.dateFormatter.inputDateFormat = 'yyyy-MM-dd'

      // Create axes
      const dateAxis = chart.xAxes.push(new am4charts.DateAxis())

      chart.yAxes.push(new am4charts.ValueAxis())

      // Create series

      const series = chart.series.push(new am4charts.LineSeries())
      series.dataFields.valueY = this.option.yAxis[0]
      series.dataFields.dateX = this.option.xAxis[0]
      series.tooltipText = '{value}'
      series.strokeWidth = 2
      series.minBulletDistance = 15

      // Drop-shaped tooltips
      series.tooltip.background.cornerRadius = 20
      series.tooltip.background.strokeOpacity = 0
      series.tooltip.pointerOrientation = 'vertical'
      series.tooltip.label.minWidth = 40
      series.tooltip.label.minHeight = 40
      series.tooltip.label.textAlign = 'middle'
      series.tooltip.label.textValign = 'middle'

      // Make bullets grow on hover

      const bullet = series.bullets.push(new am4charts.CircleBullet())
      bullet.circle.strokeWidth = 2
      bullet.circle.radius = 4
      bullet.circle.fill = am4core.color('#fff')

      const bullethover = bullet.states.create('hover')
      bullethover.properties.scale = 1.3

      // Make a panning cursor
      chart.cursor = new am4charts.XYCursor()
      chart.cursor.behavior = 'panXY'
      chart.cursor.xAxis = dateAxis
      chart.cursor.snapToSeries = series

      // Create vertical scrollbar and place it before the value axis
      chart.scrollbarY = new am4core.Scrollbar()
      chart.scrollbarY.parent = chart.leftAxesContainer
      chart.scrollbarY.toBack()

      // Create a horizontal scrollbar with previe and place it underneath the date axis
      chart.scrollbarX = new am4charts.XYChartScrollbar()
      chart.scrollbarX.series.push(series)
      chart.scrollbarX.parent = chart.bottomAxesContainer

      dateAxis.start = 0.79
      dateAxis.keepSelection = true
    },
    lineZoomH (chart) {
      chart.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        chart.colors.list.push(am4core.color(this.option.colors[j]))
      }

      // Add data
      chart.data = this.option.data

      // Create axes
      const dateAxis = chart.xAxes.push(new am4charts.DateAxis())
      dateAxis.renderer.minGridDistance = 50
      chart.yAxes.push(new am4charts.ValueAxis())

      // Create series
      const series = chart.series.push(new am4charts.LineSeries())
      series.dataFields.valueY = this.option.yAxis
      series.dataFields.dateX = this.option.xAxis
      series.strokeWidth = 2
      series.minBulletDistance = 10
      series.tooltipText = '{valueY}'
      series.tooltip.pointerOrientation = 'vertical'
      series.tooltip.background.cornerRadius = 20
      series.tooltip.background.fillOpacity = 0.5
      series.tooltip.label.padding(12, 12, 12, 12)

      // Add scrollbar
      chart.scrollbarX = new am4charts.XYChartScrollbar()
      chart.scrollbarX.series.push(series)

      // Add cursor
      chart.cursor = new am4charts.XYCursor()
      chart.cursor.xAxis = dateAxis
      chart.cursor.snapToSeries = series
    },
    lineZoomV () {
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

    // const body = document.querySelector('body')
    // if (body.classList.contains('dark')) {
    //   amChartUpdate(chart, {
    //     dark: true
    //   })
    // }

    // document.addEventListener('ChangeColorMode', function (e) {
    //   amChartUpdate(chart, e.detail)
    // })

  });
    },
    radar (chart) {
      chart.data = this.option.data
      /* Create axes */
      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = this.option.xAxis[0]

      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.renderer.axisFills.template.fill = chart.colors.getIndex(2)
      valueAxis.renderer.axisFills.template.fillOpacity = 0.05

      /* Create and configure series */
      const series = chart.series.push(new am4charts.RadarSeries())
      series.dataFields.valueY = this.option.yAxis[0]
      series.dataFields.categoryX = this.option.xAxis[0]
      series.name = this.option.labels[0]
      series.strokeWidth = 3
    },
    polarScatter (chart) {
      chart.data = this.option.data
      /* Create axes */
      /* Create axes */
      const xAxis = chart.xAxes.push(new am4charts.ValueAxis())
      xAxis.renderer.maxLabelPosition = 0.99

      const yAxis = chart.yAxes.push(new am4charts.ValueAxis())
      yAxis.renderer.labels.template.verticalCenter = 'bottom'
      yAxis.renderer.labels.template.horizontalCenter = 'right'
      yAxis.renderer.maxLabelPosition = 0.99
      yAxis.renderer.labels.template.paddingBottom = 1
      yAxis.renderer.labels.template.paddingRight = 3

      /* Create and configure series */
      const series1 = chart.series.push(new am4charts.RadarSeries())
      series1.bullets.push(new am4charts.CircleBullet())
      series1.strokeOpacity = 0
      series1.dataFields.valueX = 'x'
      series1.dataFields.valueY = 'y'
      series1.name = 'Series #1'
      series1.sequencedInterpolation = true
      series1.sequencedInterpolationDelay = 10
      series1.data = [
        { x: 83, y: 5.1 },
        { x: 44, y: 5.8 },
        { x: 76, y: 9 },
        { x: 2, y: 1.4 },
        { x: 100, y: 8.3 },
        { x: 96, y: 1.7 },
        { x: 68, y: 3.9 },
        { x: 0, y: 3 },
        { x: 100, y: 4.1 },
        { x: 16, y: 5.5 },
        { x: 71, y: 6.8 },
        { x: 100, y: 7.9 },
        { x: 35, y: 8 },
        { x: 44, y: 6 },
        { x: 64, y: 0.7 },
        { x: 53, y: 3.3 },
        { x: 92, y: 4.1 },
        { x: 43, y: 7.3 },
        { x: 15, y: 7.5 },
        { x: 43, y: 4.3 },
        { x: 90, y: 9.9 }
      ]

      const series2 = chart.series.push(new am4charts.RadarSeries())
      series2.bullets.push(new am4charts.CircleBullet())
      series2.strokeOpacity = 0
      series2.dataFields.valueX = 'x'
      series2.dataFields.valueY = 'y'
      series2.name = 'Series #2'
      series2.sequencedInterpolation = true
      series2.sequencedInterpolationDelay = 10
      series2.data = [
        { x: 178, y: 1.3 },
        { x: 129, y: 3.4 },
        { x: 99, y: 2.4 },
        { x: 80, y: 9.9 },
        { x: 118, y: 9.4 },
        { x: 103, y: 8.7 },
        { x: 91, y: 4.2 },
        { x: 151, y: 1.2 },
        { x: 168, y: 5.2 },
        { x: 168, y: 1.6 },
        { x: 152, y: 1.2 },
        { x: 138, y: 7.7 },
        { x: 107, y: 3.9 },
        { x: 124, y: 0.7 },
        { x: 130, y: 2.6 },
        { x: 86, y: 9.2 },
        { x: 169, y: 7.5 },
        { x: 122, y: 9.9 },
        { x: 100, y: 3.8 },
        { x: 172, y: 4.1 },
        { x: 140, y: 7.3 },
        { x: 161, y: 2.3 },
        { x: 141, y: 0.9 }
      ]

      const series3 = chart.series.push(new am4charts.RadarSeries())
      series3.bullets.push(new am4charts.CircleBullet())
      series3.strokeOpacity = 0
      series3.dataFields.valueX = 'x'
      series3.dataFields.valueY = 'y'
      series3.name = 'Series #3'
      series3.sequencedInterpolation = true
      series3.sequencedInterpolationDelay = 10
      series3.data = [
        { x: 419, y: 4.9 },
        { x: 417, y: 5.5 },
        { x: 434, y: 0.1 },
        { x: 344, y: 2.5 },
        { x: 279, y: 7.5 },
        { x: 307, y: 8.4 },
        { x: 279, y: 9 },
        { x: 220, y: 8.4 },
        { x: 201, y: 9.7 },
        { x: 288, y: 1.2 },
        { x: 333, y: 7.4 },
        { x: 308, y: 1.9 },
        { x: 330, y: 8 },
        { x: 408, y: 1.7 },
        { x: 274, y: 0.8 },
        { x: 296, y: 3.1 },
        { x: 279, y: 4.3 },
        { x: 379, y: 5.6 },
        { x: 175, y: 6.8 }
      ]

      /* Add legend */
      chart.legend = new am4charts.Legend()

      /* Add cursor */
      chart.cursor = new am4charts.RadarCursor()
    },
    polar (chart) {
      chart.data = this.option.data
      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.dataFields.category = 'direction'

      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.renderer.gridType = 'polygons'

      const range = categoryAxis.axisRanges.create()
      range.category = 'NW'
      range.endCategory = 'NW'
      range.axisFill.fill = am4core.color('#0084ff')
      range.axisFill.fillOpacity = 0.3

      const range2 = categoryAxis.axisRanges.create()
      range2.category = 'N'
      range2.endCategory = 'N'
      range2.axisFill.fill = am4core.color('#e64141')
      range2.axisFill.fillOpacity = 0.3

      const range3 = categoryAxis.axisRanges.create()
      range3.category = 'SE'
      range3.endCategory = 'SW'
      range3.axisFill.fill = am4core.color('#00ca00')
      range3.axisFill.fillOpacity = 0.3
      range3.locations.endCategory = 0

      /* Create and configure series */

      const series = chart.series.push(new am4charts.RadarSeries())
      series.dataFields.valueY = 'value'
      series.dataFields.categoryX = 'direction'
      series.name = 'Wind direction'
      series.strokeWidth = 3
      series.fillOpacity = 0.2
    },
    pie (chart) {
      chart.data = this.option.data
      const series = chart.series.push(new am4charts.PieSeries3D())
      series.colors.list = []
      for (let j = 0; j < this.option.colors.length; j++) {
        series.colors.list.push(am4core.color(this.option.colors[j]))
      }
      series.dataFields.value = this.option.value[0]
      series.dataFields.category = this.option.category[0]
    },
    lineBar (chart) {
      chart.colors.list = [am4core.color("#6ca0ff")]
      if (this.darkMode) {
        chart.stroke = am4core.color("#6ca0ff")
      }
      const chartdata = []
      let value = 120

      const names = ['ra',
        'De',
        'Ca',
        'Ja',
        'Ri',
        'An'
      ]

      for (let i = 0; i < names.length; i++) {
        value += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 5)
        chartdata.push({ category: names[i], value: value })
      }

      chart.data = chartdata
      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.renderer.grid.template.location = 0
      categoryAxis.dataFields.category = 'category'
      categoryAxis.renderer.minGridDistance = 15
      categoryAxis.renderer.grid.template.location = 0.5
      categoryAxis.renderer.grid.template.strokeDasharray = '1,3'
      categoryAxis.renderer.labels.template.rotation = -90
      categoryAxis.renderer.labels.template.horizontalCenter = 'left'
      categoryAxis.renderer.labels.template.location = 0.5

      categoryAxis.renderer.labels.template.adapter.add('dx', function (dx, target) {
        return -target.maxRight / 2
      })

      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.tooltip.disabled = true
      valueAxis.renderer.ticks.template.disabled = true
      valueAxis.renderer.axisFills.template.disabled = true

      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.categoryX = 'category'
      series.dataFields.valueY = 'value'
      series.tooltipText = '{valueY.value}'
      series.sequencedInterpolation = true
      series.fillOpacity = 0
      series.strokeOpacity = 1
      series.strokeDashArray = '1,3'
      series.columns.template.width = 0.01
      series.tooltip.pointerOrientation = 'horizontal'

      series.bullets.create(am4charts.CircleBullet)
      chart.cursor = new am4charts.XYCursor()
    },
    map2(){
      am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create map instance
    var chart = am4core.create("school-chart-05", am4maps.MapChart);
    // Set map definition
    chart.geodata = am4geodataWorldLow;

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

    // const body = document.querySelector('body')
    // if (body.classList.contains('dark')) {
    //   amChartUpdate(chart, {
    //     dark: true
    //   })
    // }

    // document.addEventListener('ChangeColorMode', function (e) {
    //   amChartUpdate(chart, e.detail)
    })
    },
    map (elem) {
      am4core.useTheme(am4themes_animated)
      var e = {
        AD: {
          country: 'Andorra',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['andorraLow', 'andorraHigh']
        },
        AE: {
          country: 'United Arab Emirates',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['uaeLow', 'uaeHigh']
        },
        AF: {
          country: 'Afghanistan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        AG: {
          country: 'Antigua and Barbuda',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['antiguaBarbudaLow', 'antiguaBarbudaHigh']
        },
        AI: {
          country: 'Anguilla',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['anguillaLow', 'anguillaHigh']
        },
        AL: {
          country: 'Albania',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['albaniaLow', 'albaniaHigh']
        },
        AM: {
          country: 'Armenia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['armeniaLow', 'armeniaHigh']
        },
        AO: {
          country: 'Angola',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['angolaLow', 'angolaHigh']
        },
        AQ: {
          country: 'Antarctica',
          continent_code: 'AN',
          continent: 'Antarctica',
          maps: []
        },
        AR: {
          country: 'Argentina',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['argentinaLow', 'argentinaHigh']
        },
        AS: {
          country: 'American Samoa',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['americanSamoaLow', 'americanSamoaHigh']
        },
        AT: {
          country: 'Austria',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['austriaLow', 'austriaHigh']
        },
        AU: {
          country: 'Australia',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['australiaLow', 'australiaHigh']
        },
        AW: {
          country: 'Aruba',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['arubaLow', 'arubaHigh']
        },
        AX: {
          country: 'Aland Islands',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        AZ: {
          country: 'Azerbaijan',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['azerbaijanLow', 'azerbaijanHigh']
        },
        BA: {
          country: 'Bosnia and Herzegovina',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['bosniaHerzegovinaLow', 'bosniaHerzegovinaHigh', 'bosniaHerzegovinaCantonsLow', 'bosniaHerzegovinaCantonsHigh']
        },
        BB: {
          country: 'Barbados',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['barbadosLow', 'barbadosHigh']
        },
        BD: {
          country: 'Bangladesh',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['bangladeshLow', 'bangladeshHigh']
        },
        BE: {
          country: 'Belgium',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['belgiumLow', 'belgiumHigh']
        },
        BF: {
          country: 'Burkina Faso',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['burkinaFasoLow', 'burkinaFasoHigh']
        },
        BG: {
          country: 'Bulgaria',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['bulgariaLow', 'bulgariaHigh']
        },
        BH: {
          country: 'Bahrain',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['bahrainLow', 'bahrainHigh']
        },
        BI: {
          country: 'Burundi',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['burundiLow', 'burundiHigh']
        },
        BJ: {
          country: 'Benin',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['beninLow', 'beninHigh']
        },
        BL: {
          country: 'Saint Barthelemy',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        BM: {
          country: 'Bermuda',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['bermudaLow', 'bermudaHigh']
        },
        BN: {
          country: 'Brunei Darussalam',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['bruneiDarussalamLow', 'bruneiDarussalamHigh']
        },
        BO: {
          country: 'Bolivia, Plurinational State of',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['boliviaLow', 'boliviaHigh']
        },
        BQ: {
          country: 'Bonaire, Sint Eustatius and Saba',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['bonaireSintEustatiusSabaLow', 'bonaireSintEustatiusSabaHigh']
        },
        BR: {
          country: 'Brazil',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['brazilLow', 'brazilHigh']
        },
        BS: {
          country: 'Bahamas',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        BT: {
          country: 'Bhutan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['bhutanLow', 'bhutanHigh']
        },
        BV: {
          country: 'Bouvet Island',
          continent_code: 'AN',
          continent: 'Antarctica',
          maps: []
        },
        BW: {
          country: 'Botswana',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['botswanaLow', 'botswanaHigh']
        },
        BY: {
          country: 'Belarus',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['belarusLow', 'belarusHigh']
        },
        BZ: {
          country: 'Belize',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['belizeLow', 'belizeHigh']
        },
        CA: {
          country: 'Canada',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['canadaLow', 'canadaHigh']
        },
        CC: {
          country: 'Cocos (Keeling) Islands',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        CD: {
          country: 'Congo, the Democratic Republic of the',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['congoDRLow', 'congoDRHigh']
        },
        CF: {
          country: 'Central African Republic',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['centralAfricanRepublicLow', 'centralAfricanRepublicHigh']
        },
        CG: {
          country: 'Congo',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['congoLow', 'congoHigh']
        },
        CH: {
          country: 'Switzerland',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['switzerlandLow', 'switzerlandHigh']
        },
        CI: {
          country: "Cote d'Ivoire",
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        CK: {
          country: 'Cook Islands',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        CL: {
          country: 'Chile',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['chileLow', 'chileHigh']
        },
        CM: {
          country: 'Cameroon',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['cameroonLow', 'cameroonHigh']
        },
        CN: {
          country: 'China',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['chinaLow', 'chinaHigh']
        },
        CO: {
          country: 'Colombia',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['colombiaLow', 'colombiaHigh', 'colombiaMuniLow', 'colombiaMuniHigh']
        },
        CR: {
          country: 'Costa Rica',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['costaRicaLow', 'costaRicaHigh']
        },
        CU: {
          country: 'Cuba',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        CV: {
          country: 'Cape Verde',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['capeVerdeLow', 'capeVerdeHigh']
        },
        CW: {
          country: 'Curacao',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['curacaoLow', 'curacaoHigh']
        },
        CX: {
          country: 'Christmas Island',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        CY: {
          country: 'Cyprus',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['cyprusLow', 'cyprusHigh', 'cyprusNorthCyprusLow', 'cyprusNorthCyprusHigh']
        },
        CZ: {
          country: 'Czech Republic',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['czechiaLow', 'czechiaHigh']
        },
        DE: {
          country: 'Germany',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['germanyLow', 'germanyHigh']
        },
        DJ: {
          country: 'Djibouti',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['djiboutiLow', 'djiboutiHigh']
        },
        DK: {
          country: 'Denmark',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['denmarkLow', 'denmarkHigh']
        },
        DM: {
          country: 'Dominica',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['dominicaLow', 'dominicaHigh']
        },
        DO: {
          country: 'Dominican Republic',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['dominicanRepublicLow', 'dominicanRepublicHigh', 'dominicanRepublicMuniLow', 'dominicanRepublicMuniHigh']
        },
        DZ: {
          country: 'Algeria',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['algeriaLow', 'algeriaHigh']
        },
        EC: {
          country: 'Ecuador',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['ecuadorLow', 'ecuadorHigh']
        },
        EE: {
          country: 'Estonia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['estoniaLow', 'estoniaHigh']
        },
        EG: {
          country: 'Egypt',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['egyptLow', 'egyptHigh']
        },
        EH: {
          country: 'Western Sahara',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        ER: {
          country: 'Eritrea',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        ES: {
          country: 'Spain',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['spainLow', 'spainHigh', 'spainProvincesLow', 'spainProvincesHigh']
        },
        ET: {
          country: 'Ethiopia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        FI: {
          country: 'Finland',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['finlandLow', 'finlandHigh']
        },
        FJ: {
          country: 'Fiji',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['fijiEastLow', 'fijiEastHigh', 'fijiWestLow', 'fijiWestHigh']
        },
        FK: {
          country: 'Falkland Islands (Malvinas)',
          continent_code: 'SA',
          continent: 'South America',
          maps: []
        },
        FM: {
          country: 'Micronesia, Federated States of',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        FO: {
          country: 'Faroe Islands',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['faroeIslandsLow', 'faroeIslandsHigh']
        },
        FR: {
          country: 'France',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['franceLow', 'franceHigh', 'franceDepartmentsLow', 'franceDepartmentsHigh']
        },
        GA: {
          country: 'Gabon',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['gabonLow', 'gabonHigh']
        },
        GB: {
          country: 'United Kingdom',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['ukLow', 'ukHigh', 'ukCountiesLow', 'ukCountiesHigh']
        },
        'GB-CHA': {
          country: 'Channel Islands',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['channelIslandsLow', 'channelIslandsHigh']
        },
        GD: {
          country: 'Grenada',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        GE: {
          country: 'Georgia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['georgiaLow', 'georgiaHigh', 'georgiaSouthOssetiaLow', 'georgiaSouthOssetiaHigh']
        },
        GF: {
          country: 'French Guiana',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['frenchGuianaLow', 'frenchGuianaHigh']
        },
        GG: {
          country: 'Guernsey',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        GH: {
          country: 'Ghana',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        GI: {
          country: 'Gibraltar',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        GL: {
          country: 'Greenland',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['greenlandLow', 'greenlandHigh']
        },
        GM: {
          country: 'Gambia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        GN: {
          country: 'Guinea',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['guineaLow', 'guineaHigh']
        },
        GP: {
          country: 'Guadeloupe',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        GQ: {
          country: 'Equatorial Guinea',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['equatorialGuineaLow', 'equatorialGuineaHigh']
        },
        GR: {
          country: 'Greece',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['greeceLow', 'greeceHigh']
        },
        GS: {
          country: 'South Georgia and the South Sandwich Islands',
          continent_code: 'AN',
          continent: 'Antarctica',
          maps: []
        },
        GT: {
          country: 'Guatemala',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        GU: {
          country: 'Guam',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        GW: {
          country: 'Guinea-Bissau',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        GY: {
          country: 'Guyana',
          continent_code: 'SA',
          continent: 'South America',
          maps: []
        },
        HK: {
          country: 'Hong Kong',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['hongKongLow', 'hongKongHigh']
        },
        HM: {
          country: 'Heard Island and McDonald Islands',
          continent_code: 'AN',
          continent: 'Antarctica',
          maps: []
        },
        HN: {
          country: 'Honduras',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['hondurasLow', 'hondurasHigh']
        },
        HR: {
          country: 'Croatia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['croatiaLow', 'croatiaHigh']
        },
        HT: {
          country: 'Haiti',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        HU: {
          country: 'Hungary',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['hungaryLow', 'hungaryHigh']
        },
        ID: {
          country: 'Indonesia',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['indonesiaLow', 'indonesiaHigh']
        },
        IE: {
          country: 'Ireland',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['irelandLow', 'irelandHigh']
        },
        IL: {
          country: 'Israel',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['israelLow', 'israelHigh', 'israelPalestineLow', 'israelPalestineHigh']
        },
        IM: {
          country: 'Isle of Man',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        IN: {
          country: 'India',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['indiaLow', 'indiaHigh']
        },
        IO: {
          country: 'British Indian Ocean Territory',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        IQ: {
          country: 'Iraq',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        IR: {
          country: 'Iran, Islamic Republic of',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        IS: {
          country: 'Iceland',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['icelandLow', 'icelandHigh']
        },
        IT: {
          country: 'Italy',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['italyLow', 'italyHigh']
        },
        JE: {
          country: 'Jersey',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        JM: {
          country: 'Jamaica',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        JO: {
          country: 'Jordan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        JP: {
          country: 'Japan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['japanLow', 'japanHigh']
        },
        KE: {
          country: 'Kenya',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['kenyaLow', 'kenyaHigh']
        },
        KG: {
          country: 'Kyrgyzstan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['kyrgyzstanLow', 'kyrgyzstanHigh']
        },
        KH: {
          country: 'Cambodia',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['cambodiaLow', 'cambodiaHigh']
        },
        KI: {
          country: 'Kiribati',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        KM: {
          country: 'Comoros',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        KN: {
          country: 'Saint Kitts and Nevis',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        KP: {
          country: "Korea, Democratic People's Republic of",
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['northKoreaLow', 'northKoreaHigh']
        },
        KR: {
          country: 'Korea, Republic of',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['southKoreaLow', 'southKoreaHigh']
        },
        KT: {
          country: 'Saint Kitts and Nevis',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['stKittsNevisLow', 'stKittsNevisHigh']
        },
        KW: {
          country: 'Kuwait',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        KY: {
          country: 'Cayman Islands',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        KZ: {
          country: 'Kazakhstan',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['kazakhstanLow', 'kazakhstanHigh']
        },
        LA: {
          country: "Lao People's Democratic Republic",
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        LB: {
          country: 'Lebanon',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        LC: {
          country: 'Saint Lucia',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['saintLuciaLow', 'saintLuciaHigh']
        },
        LI: {
          country: 'Liechtenstein',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['liechtensteinLow', 'liechtensteinHigh']
        },
        LK: {
          country: 'Sri Lanka',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['sriLankaLow', 'sriLankaHigh']
        },
        LR: {
          country: 'Liberia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        LS: {
          country: 'Lesotho',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        LT: {
          country: 'Lithuania',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['lithuaniaLow', 'lithuaniaHigh']
        },
        LU: {
          country: 'Luxembourg',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        LV: {
          country: 'Latvia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['latviaLow', 'latviaHigh']
        },
        LY: {
          country: 'Libya',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        MA: {
          country: 'Morocco',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['moroccoLow', 'moroccoHigh']
        },
        MC: {
          country: 'Monaco',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        MD: {
          country: 'Moldova, Republic of',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['moldovaLow', 'moldovaHigh']
        },
        ME: {
          country: 'Montenegro',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        MF: {
          country: 'Saint Martin (French Part)',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        MG: {
          country: 'Madagascar',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        MH: {
          country: 'Marshall Islands',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        MK: {
          country: 'North Macedonia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: []
        },
        ML: {
          country: 'Mali',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['maliLow', 'maliHigh']
        },
        MM: {
          country: 'Myanmar',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        MN: {
          country: 'Mongolia',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['mongoliaLow', 'mongoliaHigh']
        },
        MO: {
          country: 'Macao',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        MP: {
          country: 'Northern Mariana Islands',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        MQ: {
          country: 'Martinique',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        MR: {
          country: 'Mauritania',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        MS: {
          country: 'Montserrat',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        MT: {
          country: 'Malta',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['maltaLow', 'maltaHigh']
        },
        MU: {
          country: 'Mauritius',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        MV: {
          country: 'Maldives',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['maldivesLow', 'maldivesHigh', 'maldivesIslandsLow', 'maldivesIslandsHigh']
        },
        MW: {
          country: 'Malawi',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        MX: {
          country: 'Mexico',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['mexicoLow', 'mexicoHigh']
        },
        MY: {
          country: 'Malaysia',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['malaysiaLow', 'malaysiaHigh']
        },
        MZ: {
          country: 'Mozambique',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        NA: {
          country: 'Namibia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['namibiaLow', 'namibiaHigh']
        },
        NC: {
          country: 'New Caledonia',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        NE: {
          country: 'Niger',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        NF: {
          country: 'Norfolk Island',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        NG: {
          country: 'Nigeria',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['nigeriaLow', 'nigeriaHigh']
        },
        NI: {
          country: 'Nicaragua',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['nicaraguaLow', 'nicaraguaHigh']
        },
        NL: {
          country: 'Netherlands',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['netherlandsLow', 'netherlandsHigh']
        },
        NO: {
          country: 'Norway',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['norwayLow', 'norwayHigh']
        },
        NP: {
          country: 'Nepal',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['nepalLow', 'nepalHigh']
        },
        NR: {
          country: 'Nauru',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        NU: {
          country: 'Niue',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        NZ: {
          country: 'New Zealand',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['newZealandLow', 'newZealandHigh']
        },
        OM: {
          country: 'Oman',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['omanLow', 'omanHigh']
        },
        PA: {
          country: 'Panama',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['panamaLow', 'panamaHigh']
        },
        PE: {
          country: 'Peru',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['peruLow', 'peruHigh']
        },
        PF: {
          country: 'French Polynesia',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        PG: {
          country: 'Papua New Guinea',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        PH: {
          country: 'Philippines',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['philippinesLow', 'philippinesHigh']
        },
        PK: {
          country: 'Pakistan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['pakistanLow', 'pakistanHigh']
        },
        PL: {
          country: 'Poland',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['polandLow', 'polandHigh']
        },
        PM: {
          country: 'Saint Pierre and Miquelon',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['stPierreMiquelonLow', 'stPierreMiquelonHigh']
        },
        PN: {
          country: 'Pitcairn',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        PR: {
          country: 'Puerto Rico',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['puertoRicoLow', 'puertoRicoHigh']
        },
        PS: {
          country: 'Palestinian, State of',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['palestineLow', 'palestineHigh']
        },
        PT: {
          country: 'Portugal',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['portugalLow', 'portugalHigh', 'portugalRegionsLow', 'portugalRegionsHigh']
        },
        PW: {
          country: 'Palau',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        PY: {
          country: 'Paraguay',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['paraguayLow', 'paraguayHigh']
        },
        QA: {
          country: 'Qatar',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['qatarLow', 'qatarHigh']
        },
        RE: {
          country: 'Reunion',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        RO: {
          country: 'Romania',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['romaniaLow', 'romaniaHigh']
        },
        RS: {
          country: 'Serbia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['serbiaLow', 'serbiaHigh', 'serbiaNoKosovoLow', 'serbiaNoKosovoHigh']
        },
        RU: {
          country: 'Russian Federation',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['russiaLow', 'russiaHigh', 'russiaCrimeaLow', 'russiaCrimeaHigh']
        },
        RW: {
          country: 'Rwanda',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        SA: {
          country: 'Saudi Arabia',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['saudiArabiaLow', 'saudiArabiaHigh']
        },
        SB: {
          country: 'Solomon Islands',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['solomonIslandsLow', 'solomonIslandsHigh']
        },
        SC: {
          country: 'Seychelles',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['seychellesLow', 'seychellesHigh']
        },
        SD: {
          country: 'Sudan',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['sudanLow', 'sudanHigh']
        },
        SE: {
          country: 'Sweden',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['swedenLow', 'swedenHigh']
        },
        SG: {
          country: 'Singapore',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['singaporeLow', 'singaporeHigh']
        },
        SH: {
          country: 'Saint Helena, Ascension and Tristan da Cunha',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['saintHelenaLow', 'saintHelenaHigh']
        },
        SI: {
          country: 'Slovenia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['sloveniaLow', 'sloveniaHigh', 'sloveniaRegionsLow', 'sloveniaRegionsHigh']
        },
        SJ: {
          country: 'Svalbard and Jan Mayen',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['svalbardLow', 'svalbardHigh']
        },
        SK: {
          country: 'Slovakia',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['slovakiaLow', 'slovakiaHigh']
        },
        SL: {
          country: 'Sierra Leone',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        SM: {
          country: 'San Marino',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['sanMarinoLow', 'sanMarinoHigh']
        },
        SN: {
          country: 'Senegal',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['senegalLow', 'senegalHigh']
        },
        SO: {
          country: 'Somalia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['somaliaLow', 'somaliaHigh']
        },
        SR: {
          country: 'Suriname',
          continent_code: 'SA',
          continent: 'South America',
          maps: []
        },
        SS: {
          country: 'South Sudan',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        ST: {
          country: 'Sao Tome and Principe',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['saoTomePrincipeLow', 'saoTomePrincipeHigh']
        },
        SV: {
          country: 'El Salvador',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['elSalvadorLow', 'elSalvadorHigh']
        },
        SX: {
          country: 'Sint Maarten (Dutch Part)',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        SY: {
          country: 'Syrian Arab Republic',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['syriaLow', 'syriaHigh']
        },
        SZ: {
          country: 'Swaziland',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['eswatiniLow', 'eswatiniHigh']
        },
        TC: {
          country: 'Turks and Caicos Islands',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        TD: {
          country: 'Chad',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['chadLow', 'chadHigh']
        },
        TF: {
          country: 'French Southern Territories',
          continent_code: 'AN',
          continent: 'Antarctica',
          maps: []
        },
        TG: {
          country: 'Togo',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        TH: {
          country: 'Thailand',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['thailandLow', 'thailandHigh']
        },
        TJ: {
          country: 'Tajikistan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['tajikistanLow', 'tajikistanHigh']
        },
        TK: {
          country: 'Tokelau',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        TL: {
          country: 'Timor-Leste',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        TM: {
          country: 'Turkmenistan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        TN: {
          country: 'Tunisia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['tunisiaLow', 'tunisiaHigh']
        },
        TO: {
          country: 'Tonga',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        TR: {
          country: 'Turkey',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['turkeyLow', 'turkeyHigh']
        },
        TT: {
          country: 'Trinidad and Tobago',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        TV: {
          country: 'Tuvalu',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        TW: {
          country: 'Taiwan, Province of China',
          continent_code: 'AS',
          continent: 'Asia',
          maps: []
        },
        TZ: {
          country: 'Tanzania, United Republic of',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['tanzaniaLow', 'tanzaniaHigh']
        },
        UA: {
          country: 'Ukraine',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['ukraineLow', 'ukraineHigh']
        },
        UG: {
          country: 'Uganda',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        UM: {
          country: 'United States Minor Outlying Islands',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        US: {
          country: 'United States',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['usaLow', 'usaHigh', 'usaTerritoriesLow', 'usaTerritoriesHigh', 'usaTerritories2Low', 'usaTerritories2High']
        },
        UY: {
          country: 'Uruguay',
          continent_code: 'SA',
          continent: 'South America',
          maps: []
        },
        UZ: {
          country: 'Uzbekistan',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['uzbekinstanLow', 'uzbekinstanHigh']
        },
        VA: {
          country: 'Holy See (Vatican City State)',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['vaticanLow', 'vaticanHigh']
        },
        VC: {
          country: 'Saint Vincent and the Grenadines',
          continent_code: 'NA',
          continent: 'North America',
          maps: ['saintVincentLow', 'saintVincentHigh']
        },
        VE: {
          country: 'Venezuela, Bolivarian Republic of',
          continent_code: 'SA',
          continent: 'South America',
          maps: ['venezuelaLow', 'venezuelaHigh']
        },
        VG: {
          country: 'Virgin Islands, British',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        VI: {
          country: 'Virgin Islands, U.S.',
          continent_code: 'NA',
          continent: 'North America',
          maps: []
        },
        VN: {
          country: 'Viet Nam',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['vietnamLow', 'vietnamHigh']
        },
        VU: {
          country: 'Vanuatu',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        WF: {
          country: 'Wallis and Futuna',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: []
        },
        WS: {
          country: 'Samoa',
          continent_code: 'OC',
          continent: 'Oceania',
          maps: ['samoaLow', 'samoaHigh']
        },
        YE: {
          country: 'Yemen',
          continent_code: 'AS',
          continent: 'Asia',
          maps: ['yemenLow', 'yemenHigh']
        },
        YT: {
          country: 'Mayotte',
          continent_code: 'AF',
          continent: 'Africa',
          maps: []
        },
        ZA: {
          country: 'South Africa',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['southAfricaLow', 'southAfricaHigh']
        },
        ZM: {
          country: 'Zambia',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['zambiaLow', 'zambiaHigh']
        },
        ZW: {
          country: 'Zimbabwe',
          continent_code: 'AF',
          continent: 'Africa',
          maps: ['zimbabweLow', 'zimbabweHigh']
        },
        XK: {
          country: 'Kosovo',
          continent_code: 'EU',
          continent: 'Europe',
          maps: ['kosovoLow', 'kosovoHigh']
        }
      }
      var t = {
        AF: 0,
        AN: 1,
        AS: 2,
        EU: 3,
        NA: 4,
        OC: 5,
        SA: 6
      }
      const a = am4core.create(elem, am4maps.MapChart)
      a.projection = new am4maps.projections.Miller()
      const n = a.series.push(new am4maps.MapPolygonSeries())
      // eslint-disable-next-line no-sequences,no-unused-expressions
      n.useGeodata = !0, n.geodata = am4geodataWorldLow, n.exclude = ['AQ']
      const o = n.mapPolygons.template
      // eslint-disable-next-line no-sequences,no-unused-expressions
      o.tooltipText = '{name}', o.nonScalingStroke = !0, o.strokeOpacity = 0.5, o.fill = am4core.color('#eee'), o.propertyFields.fill = 'color', o.states.create('hover').properties.fill = a.colors.getIndex(9)
      const r = a.series.push(new am4maps.MapPolygonSeries())
      // eslint-disable-next-line no-sequences,no-unused-expressions
      r.useGeodata = !0, r.hide(), r.geodataSource.events.on('done', function () {
        // eslint-disable-next-line no-sequences,no-unused-expressions
        n.hide(), r.show()
      })
      const i = r.mapPolygons.template
      // eslint-disable-next-line no-sequences,no-unused-expressions
      i.tooltipText = '{name}', i.nonScalingStroke = !0, i.strokeOpacity = 0.5, i.fill = am4core.color('#eee'), i.states.create('hover').properties.fill = a.colors.getIndex(9), o.events.on('hit', function (e) {
        e.target.series.chart.zoomToMapObject(e.target)
        var t = e.target.dataItem.dataContext.map
        // eslint-disable-next-line no-sequences,no-unused-expressions
        t && (e.target.isHover = !1, r.geodataSource.url = 'https://www.amcharts.com/lib/4/geodata/json/' + t + '.json', r.geodataSource.load())
      })
      const c = []
      for (const s in e) {
        // eslint-disable-next-line no-prototype-builtins
        if (e.hasOwnProperty(s)) {
          const l = e[s]
          l.maps.length && c.push({
            id: s,
            color: a.colors.getIndex(t[l.continent_code]),
            map: l.maps[0]
          })
        }
      }
      // eslint-disable-next-line no-sequences,no-unused-expressions
      n.data = c, a.zoomControl = new am4maps.ZoomControl()
      const d = new am4core.Button()
      // eslint-disable-next-line no-sequences,no-unused-expressions
      d.events.on('hit', function () {
        // eslint-disable-next-line no-sequences,no-unused-expressions
        n.show(), r.hide(), a.goHome()
        // eslint-disable-next-line no-sequences,no-unused-expressions
      }), d.icon = new am4core.Sprite(), d.padding(7, 5, 7, 5), d.width = 30, d.icon.path = 'M16,8 L14,8 L14,16 L10,16 L10,10 L6,10 L6,16 L2,16 L2,8 L0,8 L8,0 L16,8 Z M16,8', d.marginBottom = 10, d.parent = a.zoomControl, d.insertBefore(a.zoomControl.plusButton)
    },
    linierChart (chart) {
      chart.colors.list = [am4core.color('#827af3'), am4core.color('#6ce6f4')]
      if (this.darkMode) {
        chart.stroke = am4core.color('#8c91b6')
      }
      const data = []
      let open = 100
      let close = 120

      const names = ['Rai',
        'Dem',
        'Caro',
        'Jac',
        'Rich',
        'Ano',
        'Amd',
        'Idal',
        'Joi',
        'Mar',
        'Cur',
        'Shl',
        'Meg'
      ]

      for (let i = 0; i < names.length; i++) {
        open += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 5)
        close = open + Math.round(Math.random() * 10) + 3
        data.push({ category: names[i], open: open, close: close })
      }

      chart.data = data
      const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
      categoryAxis.renderer.grid.template.location = 0
      categoryAxis.dataFields.category = 'category'
      categoryAxis.renderer.minGridDistance = 15
      categoryAxis.renderer.grid.template.location = 0.5
      categoryAxis.renderer.grid.template.strokeDasharray = '1,3'
      categoryAxis.renderer.labels.template.rotation = -90
      categoryAxis.renderer.labels.template.horizontalCenter = 'left'
      categoryAxis.renderer.labels.template.location = 0.5
      categoryAxis.renderer.inside = true

      categoryAxis.renderer.labels.template.adapter.add('dx', function (dx, target) {
        return -target.maxRight / 2
      })

      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.tooltip.disabled = true
      valueAxis.renderer.ticks.template.disabled = true
      valueAxis.renderer.axisFills.template.disabled = true

      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.categoryX = 'category'
      series.dataFields.openValueY = 'open'
      series.dataFields.valueY = 'close'
      series.tooltipText = 'open: {openValueY.value} close: {valueY.value}'
      series.sequencedInterpolation = true
      series.fillOpacity = 0
      series.strokeOpacity = 1
      series.columns.template.width = 0.01
      series.tooltip.pointerOrientation = 'horizontal'

      const openBullet = series.bullets.create(am4charts.CircleBullet)
      openBullet.locationY = 1

      const closeBullet = series.bullets.create(am4charts.CircleBullet)

      closeBullet.fill = chart.colors.getIndex(4)
      closeBullet.stroke = closeBullet.fill

      chart.cursor = new am4charts.XYCursor()
    },
    htMenu1 (chart) {
      chart.colors.list = [am4core.color('#827af3')]
      chart.data = [{
        date: '2012-03-01',
        price: 40
      }, {
        date: '2012-03-02',
        price: 65
      }, {
        date: '2012-03-03',
        price: 30
      }, {
        date: '2012-03-04',
        price: 25
      }, {
        date: '2012-03-05',
        price: 60
      }, {
        date: '2012-03-06',
        price: 20
      }, {
        date: '2012-03-07',
        price: 7
      }, {
        date: '2012-03-08',
        price: 89
      }, {
        date: '2012-03-09',
        price: 75
      }, {
        date: '2012-03-10',
        price: 132
      }, {
        date: '2012-03-11',
        price: 80
      }, {
        date: '2012-03-12',
        price: 56
      }, {
        date: '2012-03-13',
        price: 69
      }, {
        date: '2012-03-14',
        price: 24
      }, {
        date: '2012-03-15',
        price: 47
      }]

      // Create axes
      chart.xAxes.push(new am4charts.DateAxis())

      chart.yAxes.push(new am4charts.ValueAxis())

      // Create series
      const series = chart.series.push(new am4charts.LineSeries())
      series.dataFields.valueY = 'price'
      series.dataFields.dateX = 'date'
      series.tensionX = 0.8
      series.strokeWidth = 3
    },
    htMenu2 (chart) {
      chart.colors.list = [am4core.color('#00d0ff')]
      chart.data = [{
        date: '2012-03-01',
        price: 20
      }, {
        date: '2012-03-02',
        price: 75
      }, {
        date: '2012-03-03',
        price: 15
      }, {
        date: '2012-03-04',
        price: 75
      }, {
        date: '2012-03-05',
        price: 158
      }, {
        date: '2012-03-06',
        price: 57
      }, {
        date: '2012-03-07',
        price: 107
      }, {
        date: '2012-03-08',
        price: 89
      }, {
        date: '2012-03-09',
        price: 75
      }, {
        date: '2012-03-10',
        price: 132
      }, {
        date: '2012-03-11',
        price: 380
      }, {
        date: '2012-03-12',
        price: 56
      }, {
        date: '2012-03-13',
        price: 169
      }, {
        date: '2012-03-14',
        price: 24
      }, {
        date: '2012-03-15',
        price: 147
      }]

      // Create axes
      chart.xAxes.push(new am4charts.DateAxis())
      chart.yAxes.push(new am4charts.ValueAxis())

      // Create series
      const series = chart.series.push(new am4charts.LineSeries())
      series.dataFields.valueY = 'price'
      series.dataFields.dateX = 'date'
      series.tensionX = 0.8
      series.strokeWidth = 3
    },
    htMenu3 (chart) {
      chart.colors.list = [am4core.color('#827af3')]
      chart.hiddenState.properties.opacity = 0

      chart.data = [{
        date: '2018-01-01',
        steps: 4561
      }, {
        date: '2018-01-02',
        steps: 5687
      }, {
        date: '2018-01-03',
        steps: 6348
      }, {
        date: '2018-01-04',
        steps: 4878
      }, {
        date: '2018-01-05',
        steps: 9867
      }, {
        date: '2018-01-06',
        steps: 7561
      }, {
        date: '2018-01-07',
        steps: 1287
      }, {
        date: '2018-01-08',
        steps: 3298
      }, {
        date: '2018-01-09',
        steps: 5697
      }, {
        date: '2018-01-10',
        steps: 4878
      }, {
        date: '2018-01-11',
        steps: 8788
      }, {
        date: '2018-01-12',
        steps: 9560
      }, {
        date: '2018-01-13',
        steps: 11687
      }, {
        date: '2018-01-14',
        steps: 5878
      }, {
        date: '2018-01-15',
        steps: 9789
      }, {
        date: '2018-01-16',
        steps: 3987
      }, {
        date: '2018-01-17',
        steps: 5898
      }, {
        date: '2018-01-18',
        steps: 9878
      }, {
        date: '2018-01-19',
        steps: 13687
      }, {
        date: '2018-01-20',
        steps: 6789
      }, {
        date: '2018-01-21',
        steps: 4531
      }, {
        date: '2018-01-22',
        steps: 5856
      }, {
        date: '2018-01-23',
        steps: 5737
      }, {
        date: '2018-01-24',
        steps: 9987
      }, {
        date: '2018-01-25',
        steps: 16457
      }, {
        date: '2018-01-26',
        steps: 7878
      }, {
        date: '2018-01-27',
        steps: 6845
      }, {
        date: '2018-01-28',
        steps: 4659
      }, {
        date: '2018-01-29',
        steps: 7892
      }, {
        date: '2018-01-30',
        steps: 7362
      }, {
        date: '2018-01-31',
        steps: 3268
      }]

      chart.dateFormatter.inputDateFormat = 'YYYY-MM-dd'
      chart.zoomOutButton.disabled = true

      const dateAxis = chart.xAxes.push(new am4charts.DateAxis())
      dateAxis.renderer.grid.template.strokeOpacity = 0
      dateAxis.renderer.minGridDistance = 10
      dateAxis.dateFormats.setKey('day', 'd')
      dateAxis.tooltip.hiddenState.properties.opacity = 1
      dateAxis.tooltip.hiddenState.properties.visible = true

      dateAxis.tooltip.adapter.add('x', function () {
        return am4core.utils.spritePointToSvg({ x: chart.plotContainer.pixelX, y: 0 }, chart.plotContainer).x + chart.plotContainer.pixelWidth / 2
      })

      const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.renderer.inside = true
      valueAxis.renderer.labels.template.fillOpacity = 0.3
      valueAxis.renderer.grid.template.strokeOpacity = 0
      valueAxis.min = 0
      valueAxis.cursorTooltipEnabled = false

      // goal guides
      const axisRange = valueAxis.axisRanges.create()
      axisRange.value = 6000
      axisRange.grid.strokeOpacity = 0.1
      axisRange.label.text = 'Goal'
      axisRange.label.align = 'right'
      axisRange.label.verticalCenter = 'bottom'
      axisRange.label.fillOpacity = 0.8

      valueAxis.renderer.gridContainer.zIndex = 1

      const axisRange2 = valueAxis.axisRanges.create()
      axisRange2.value = 12000
      axisRange2.grid.strokeOpacity = 0.1
      axisRange2.label.text = '2x goal'
      axisRange2.label.align = 'right'
      axisRange2.label.verticalCenter = 'bottom'
      axisRange2.label.fillOpacity = 0.8

      const series = chart.series.push(new am4charts.ColumnSeries())
      series.dataFields.valueY = 'steps'
      series.dataFields.dateX = 'date'
      series.tooltipText = '{valueY.value}'
      series.tooltip.pointerOrientation = 'vertical'
      series.tooltip.hiddenState.properties.opacity = 1
      series.tooltip.hiddenState.properties.visible = true
      series.tooltip.adapter.add('x', function () {
        return am4core.utils.spritePointToSvg({ x: chart.plotContainer.pixelX, y: 0 }, chart.plotContainer).x + chart.plotContainer.pixelWidth / 2
      })

      const columnTemplate = series.columns.template
      columnTemplate.width = 30
      columnTemplate.column.cornerRadiusTopLeft = 20
      columnTemplate.column.cornerRadiusTopRight = 20
      columnTemplate.strokeOpacity = 0

      columnTemplate.adapter.add('fill', function (fill, target) {
        const dataItem = target.dataItem
        if (dataItem.valueY > 6000) {
          return chart.colors.getIndex(0)
        } else {
          return am4core.color('#a8b3b7')
        }
      })

      const cursor = new am4charts.XYCursor()
      cursor.behavior = 'panX'
      chart.cursor = cursor
      cursor.lineX.disabled = true

      chart.events.on('datavalidated', function () {
        dateAxis.zoomToDates(new Date(2018, 0, 21), new Date(2018, 1, 1), false, true)
      })

      const middleLine = chart.plotContainer.createChild(am4core.Line)
      middleLine.strokeOpacity = 1
      middleLine.stroke = am4core.color('#000000')
      middleLine.strokeDasharray = '2,2'
      middleLine.align = 'center'
      middleLine.zIndex = 1
      middleLine.adapter.add('y2', function (y2, target) {
        return target.parent.pixelHeight
      })

      cursor.events.on('cursorpositionchanged', updateTooltip)
      dateAxis.events.on('datarangechanged', updateTooltip)

      function updateTooltip () {
        dateAxis.showTooltipAtPosition(0.5)
        series.showTooltipAtPosition(0.5, 0)
        series.tooltip.validate() // otherwise will show other columns values for a second
      }

      const label = chart.plotContainer.createChild(am4core.Label)
      label.text = 'Pan chart to change date'
      label.x = 90
      label.y = 50
    }
  }
}
</script>
