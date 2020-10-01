<template>
  <div class="home">

    <div class="container">
        <sensor-data-list :sensors="arrSensors"></sensor-data-list>
    </div>

  </div>
</template>
<script>
import SensorDataList from '@/components/SensorDataList'

export default {
  name: 'home',
  components: {
      SensorDataList
  },
  data() {
      return {
          arrSensors: [],
      }
  },
  mounted() {
      this.requestSensorData();
  },
  methods: {
        async requestSensorData() {
            try{
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/sensors/');
                const data = await response.json();

                this.arrSensors = data;
            } catch(error) {
                console.log(error)
            }
        }
  }
}
</script>