<template>
  <div id="app" class="small-container">
    <h1>Sensor Data UI</h1>

    <sensor-data-table :measurements="measurements" />
  </div>
</template>

<script>
    import SensorDataTable from '@/components/SensorDataTable.vue'
    export default {
        name: 'app',
        components: {
            SensorDataTable,
        },
        data() {
            return {
                measurements: []
            }
        },
        mounted() {
            this.getMeasurements()
        },

        methods: {
            async getMeasurements() {
                try {
                    const response = await fetch('http://localhost:8000/measurements/5')
                    const data = await response.json()
                    this.measurements = data
                    console.log(data)
                } catch (error) {
                    console.error(error)
                }
            }
        }
    }
</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }

  .small-container {
    max-width: 680px;
  }
</style>
