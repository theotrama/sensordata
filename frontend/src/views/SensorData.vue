<template>
  <div class="container">
    <measurements-chart v-if="loaded" :chartdata="arrMeasurementData" :options="chartOptions" label="Degree Celsius"></measurements-chart>
  </div>
</template>

<script>
import axios from 'axios'
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
                const response = await fetch('http://localhost:8000/measurements/5');
                const data = await response.json();

                console.log(data)

                data.forEach(d => {
                    const date = d.timestamp
                    const {
                        datapoint,
                    } = d;
                    console.log(datapoint)
                    this.arrMeasurementData.push({date, total: datapoint});

                });
                console.log(this.arrMeasurementData)
                this.loaded = true

            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>