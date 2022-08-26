<template>
  <div>
    <donut-chart v-if="type === 'donut'" :id="element" :data="data" :colors="colors" :resize="resize" :height="height">
    </donut-chart>
    <bar-chart v-if="type === 'bar'"
               :id="element"
               :data="data"
               :xkey="xKeys"
               :ykeys='yKeys'
               resize="true"
               :labels='labels'
               :bar-colors="colors"
               grid="true"
               grid-text-weight="bold">
    </bar-chart>
    <line-chart v-if="type === 'line'"
                :id="element"
                :data="data"
                :xkey="xKeys"
                :ykeys='yKeys'
                :line-colors="colors"
                :labels='labels'
                grid="true"
                grid-text-weight="bold"
                hide-hover="auto">
    </line-chart>
    <area-chart v-if="type === 'area'"
                :id="element"
                :data="data"
                :line-colors="colors"
                :resize="resize"
                :labels='labels'
                :xkey="xKeys"
                :ykeys='yKeys'
                hide-hover="always"
                grid="true"
                grid-text-weight="bold">
    </area-chart>
  </div>
</template>
<script>
import { DonutChart, BarChart, LineChart, AreaChart } from 'vue-morris'
export default {
  name: 'MorrisChart',
  props: {
    type: { type: String, default: null, required: true },
    element: { type: String, default: null },
    height: { type: Number, default: null },
    xKeys: { type: String, default: '' },
    data: { type: Array, default: () => [], required: true },
    colors: { type: Array, default: () => [], required: true },
    yKeys: { type: Array, default: () => []},
    labels: { type: Array, default: () => []},
    resize: { type: Boolean, default: true }
  },
  components: {
    DonutChart, BarChart, LineChart, AreaChart
  },
  computed: {
    prettyFloorMinFollowers () {
      return this.prettyFloor(this.yMinMax['min']['followers'])
    },
    prettyCeilMaxFollowers () {
      return this.prettyCeil(this.yMinMax['max']['followers'])
    },
    yMinMax () {
      return this.minMax(this.data, 'followers')
    }
  },
  methods: {
    osColors () {
    },
    minMax (objects, field) {
      var result = {}
      return objects.reduce(function (valorAnterior, valorActual, indice) {
        if (indice === 1) {
          result['min'] = valorAnterior
          result['max'] = valorAnterior
        }
        // eslint-disable-next-line no-unused-expressions
        valorActual[field] < result['min'][field] ? result['min'] = valorActual : ''
        // eslint-disable-next-line no-unused-expressions
        valorActual[field] > result['max'][field] ? result['max'] = valorActual : ''
        return result
      })
    },
    prettyFloor (number) {
      var l = Math.floor(Math.log10(Math.abs(number), 10)) - 1
      if (l <= 0) {
        l++
      }
      number = number / (Math.pow(10, l))
      number = Math.floor(number)
      if (l > 0) {
        number = number * (Math.pow(10, l))
      }
      return number
    },
    prettyCeil (number) {
      var l = Math.floor(Math.log10(Math.abs(number), 10)) - 1
      if (l <= 0) {
        l++
      }
      number = number / (Math.pow(10, l))
      number = Math.ceil(number)
      if (l > 0) {
        number = number * (Math.pow(10, l))
      }
      return number
    }
  }
}
</script>
