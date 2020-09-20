<template>
  <div id="app" class="container">
    <h1 class="m-5 text-center">Sensor Data UI</h1>

    <router-link to="/">Temperature Data</router-link> |
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
    console.log(process.env.VUE_APP_NOT_SECRET_CODE)
</script>

<style>
  button {
    background: #009435;
    border: 1px solid #009435;
  }


</style>
