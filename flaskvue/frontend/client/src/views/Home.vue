<template>
    <JSCharting :options="chartOptions" class="columnChart"></JSCharting>
</template>

<script>
import JSCharting from 'jscharting-vue';

export default {
   name: 'columnChart',
   data() {
      return {
         chartOptions: {
            type: 'horizontal column',
            series: [
               {
                  points: [
                     { x: 'A', y: 50 },
                     { x: 'B', y: 30 },
                     { x: 'C', y: 50 }
                  ]
               }
            ]
         }
      }
   },
   components: {
      JSCharting
   }
}
</script>

<style>
.columnChart {
    height: 300px;
}
</style>