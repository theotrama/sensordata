<template>
  <div class="container">
    <measurements-chart v-if="loaded" :chartData="arrMeasurementData" :options="chartOptions" label="Relative Humidity"></measurements-chart>
  </div>
</template>

<script>
import moment from "moment";
import MeasurementsChart from '@/components/MeasurementsChart'

export default {
    name: 'HumidityChartContainer',
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
                const response = await fetch(process.env.VUE_APP_API_BASE_URL + '/measurements/2');
                const data = await response.json();
                

                data.forEach(d => {
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
