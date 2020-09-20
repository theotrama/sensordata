<template>
  <div class="container">
    <measurements-chart v-if="loaded" :chartData="arrMeasurementData" :options="chartOptions" label="Temperature in Degree Celsius"></measurements-chart>
  </div>
</template>

<script>
import moment from "moment";
import MeasurementsChart from '@/components/MeasurementsChart'

export default {
    name: 'MeasurementsChartContainer',
    components: {
        MeasurementsChart
    },
    data() {
        return {
            arrMeasurementData: [],
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
        this.requestData();
    },

    methods : {
        async requestData() {
            try {
                // GET data from API
                const response = await fetch(process.env.API_BASE_URL + '/api/measurements/1');
                const data = await response.json();
                console.log(process.env.VUE_APP_MY_ENV_VARIABLE)

                data.forEach(d => {
                    //const date = d.timestamp
                    const date = moment(d.timestamp, "YYYYMMDD").format("DD/MM/YYYY");
                    const {
                        datapoint,
                    } = d;
                    this.arrMeasurementData.push({date, total: datapoint});
                });
                this.loaded = true

            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>