<template>
  <div id="app" class="container">
    <h1 class="m-5 text-center">Sensor Data UI</h1>

    <router-link to="/">Sensor List</router-link> |
    <router-link to="/temperature">Temperature Data</router-link> |
    <router-link to="/humidity">Humidity Data</router-link>

    <div class="container">
      <div class="row">
        <div class="col-12">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>

    export default {
        name: 'app',
    }

</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }


</style>
