<template>
  <div id="sensor-data-table">
    <table>
      <thead>
        <tr>
          <th>Measurement ID</th>
          <th>Sensor ID</th>
          <th>Measurement Data</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="measurement in measurements" :key="measurement.id">
          <td>{{ measurement.id}}</td>
          <td>{{ measurement.sensor_id}}</td>
          <td>{{ measurement.datapoint}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'sensor-data-table',
    props: {
        measurements: Array
    }
  }
</script>

<style scoped></style>
