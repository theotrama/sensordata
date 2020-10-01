<template>
  <div id="sensor-data-list" class="table-responsive">
      <div class="my-3" v-for="sensor in sensors" :key="sensor.id">
      <div class="card">
        <div class="card-header">
          Sensor: {{ sensor.id}}
        </div>
        <div class="card-body">
          <h5 class="card-title">{{ sensor.name}}</h5>
          
          <p class="card-text">
            Sensor type: {{ sensor.type }} <br>
            Sensor id: {{ sensor.id }}
          </p>
          <a href="/" class="btn btn-primary">View {{ sensor.type }} data</a>
        </div>
      </div>
    </div>

  </div>
</template>


<script>
  export default {
    name: 'sensor-data-list',
    props: {
        sensors: Array
    }
  }
</script>

<style scoped></style>
