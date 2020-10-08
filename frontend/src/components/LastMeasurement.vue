<template>
  <div id="last-measurement" class="table-responsive">
    <div class="my-3">
      <div class="card">
        <div class="card-header">
           Last measurement - {{ sensor.name }}
        </div>
        <div class="card-body">
          <p class="card-text">
            {{ last_measurement.datapoint }} {{ sensor.unit }} <br>
            {{ last_measurement.timestamp }}
          </p>
        </div>
      </div>
    </div>
      
  </div>
</template>


<script>
  export default {
    name: 'last-measurement',
    props: {
        last_measurement: Object,
        sensor: Object,
    }
  }
</script>

<style scoped></style>
