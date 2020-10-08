<template>
  <div class="container-fluid">
    <last-measurement v-if="single_measurement_loaded && measurements_loaded && sensors_loaded" :last_measurement="objLastMeasurement" :sensor="objSensorData"></last-measurement>
    <measurements-chart v-if="single_measurement_loaded && measurements_loaded && sensors_loaded" :chartData="arrMeasurementData" :options="chartOptions" :label="objSensorData"></measurements-chart>
  </div>
</template>

<script>
import moment from "moment";
import MeasurementsChart from '@/components/MeasurementsChart'
import LastMeasurement from '@/components/LastMeasurement'

export default {
    name: 'MeasurementsDataContainer',
    components: {
        MeasurementsChart,
        LastMeasurement
    },
    data() {
        return {
            arrMeasurementData: [],
            objSensorData: {},
            arrMeasurementTimestamp: [],
            objLastMeasurement: {},
            measurements_loaded: false,
            sensors_loaded: false,
            single_measurement_loaded: false,

            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                lineTension: 1,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            padding: 25,
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            minRotation: 45,
                        }
                    }]
                }
            }
        }
    },

    mounted() {
        this.requestMeasurementData();
        this.requestSensorData();
        this.requestLastMeasurementData();
    },

    methods : {
        async requestMeasurementData() {
            try {
                // GET measurement data from API
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/measurements/' + this.$route.params.id + '/range?skip=30');
                const data = await response.json();

                data.forEach(d => {
                    console.log(d.timestamp)
                    //const date = d.timestamp
                    const date = moment(d.timestamp, "YYYY-MM-DDTHH:mm:ss").format("YYYY-MM-DD HH:mm:ss");
                    console.log(date)
                    const {
                        datapoint,
                    } = d;
                    this.arrMeasurementData.push({date, total: datapoint});
                    this.measurements_loaded = true;
                });

            } catch (error) {
                console.error(error)
            }
        },
        async requestSensorData() {
            try {
                // GET data from API
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/sensors/' + this.$route.params.id);
                const data = await response.json();
                this.objSensorData = data;
                this.sensors_loaded = true;

            } catch (error) {
                console.error(error)
            }
        },
        async requestLastMeasurementData() {
            try {
                // GET data from API
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/measurements/' + this.$route.params.id + '/latest');
                const data = await response.json();
                this.objLastMeasurement = data;
                this.single_measurement_loaded = true;

            } catch (error) {
                console.error(error)
            }
        },
    }
}
</script>