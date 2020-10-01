<template>
  <div id="app" class="container">
    <a href="/" class="text-decoration-none"><h1 class="my-5 text-center"> Sensor Data UI</h1></a>

    <div class="container-fluid">
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
