<template>
  <div class="container-fluid">
    <measurements-chart v-if="loaded" :chartData="arrMeasurementData" :options="chartOptions" :label="objSensorData"></measurements-chart>
  </div>
</template>

<script>
import moment from "moment";
import MeasurementsChart from '@/components/MeasurementsChart'

export default {
    name: 'MeasurementsDataContainer',
    components: {
        MeasurementsChart
    },
    data() {
        return {
            arrMeasurementData: [],
            objSensorData: {},
            arrMeasurementTimestamp: [],
            loaded: false,

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
    },

    methods : {
        async requestMeasurementData() {
            try {
                // GET data from API
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/measurements/' + this.$route.params.id + '/range?skip=60');
                const data = await response.json();

                data.forEach(d => {
                    //const date = d.timestamp
                    const date = moment(d.timestamp, "YYYYMMDD").format("DD/MM/YYYY");
                    const {
                        datapoint,
                    } = d;
                    this.arrMeasurementData.push({date, total: datapoint});
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
                this.loaded = true;

            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>