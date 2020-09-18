<script>
  import { Line } from 'vue-chartjs'

  export default {
    extends: Line,
    props: {
      label: {
        type: String,
      },
      chartData: {
        type: Array,
        default: null,
      },
      options: {
        type: Array,
      }
    },

    mounted () {
      const dates = this.chartData.map(d => d.timestamp).reverse();
      const measurements = this.chartData.map(d => d.datapoint).reverse();

      this.renderChart({
          labels: dates,
          datasets: [{
            label: this.label,
            data: this.measurements,
          }],
      }, this.options);
    }
  }
</script>