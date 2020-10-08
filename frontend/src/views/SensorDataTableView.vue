<template>
  <div class="home">

    <div class="container">
        <sensor-data-list :sensors="arrSensors" :measurements="arrLastMeasurements"></sensor-data-list>
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
          arrLastMeasurements: [],
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
                this.requestMeasurementData();
                this.sensors_loaded = true;

            } catch(error) {
                console.log(error)
            }
        },
        async requestMeasurementData() {
            try{
                var arrLastMeasurements = [];
                for (const sensor of this.arrSensors) {
                    const response = await fetch(process.env.VUE_APP_API_BASE_URL + `/measurements/${sensor.id}/latest`)
                    const data = await response.json()
                    this.arrLastMeasurements.push(data)
                }
                console.log(this.arrSensors.concat(arrLastMeasurements));
                this.measurements_loaded = true;

            } catch(error) {
                console.log(error)
            }
        },
  }
}
</script>