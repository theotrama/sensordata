<template>
  <div id="app" class="container">
    <h1 class="m-5 text-center">Sensor Data UI</h1>
    
    <router-link to="/">Sensor Data</router-link> |
    
    <div class="container">
      <div class="row">
        <div class="col-12">
          <router-view />
        </div>
      </div>
    </div>
    <sensor-data-table :measurements="measurements" />
  </div>
</template>

<script>
    import Chart from 'chart.js';
    import SensorDataTable from '@/components/SensorDataTable.vue'
    import measurementChartData from './chart-data.js';

    export default {
        name: 'app',
        components: {
            SensorDataTable,
        },
        data() {
            return {
                measurements: [],
                sensors: [],
                measurementChartData: measurementChartData,
            }
        },
        mounted() {
            this.getMeasurements(),
            this.createChart('measurements-chart', this.measurementChartData);
        },

        methods: {
            async getMeasurements() {
                try {
                    const response = await fetch('http://localhost:8000/measurements/5')
                    const data = await response.json()
                    this.measurements = data
                } catch (error) {
                    console.error(error)
                }
            },
            async getSensors() {
                try {
                    const response = await fetch('http://localhost:8000/sensors/5')
                    const data = await response.json()
                    this.sensors = data
                } catch (error) {
                    console.error(error)
                }
            },
            createChart(chartId, chartData) {
                const ctx = document.getElementById(chartId);
                const measurementChart = new Chart(ctx, {
                type: chartData.type,
                data: chartData.data,
                options: chartData.options,
                });
            },
        }
    }
</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }


</style>
