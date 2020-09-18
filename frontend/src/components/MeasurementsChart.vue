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
        type: Object,
      }
    },

    mounted () {
      console.log(this.chartData)
      const dates = this.chartData.map(d => d.date);
      const totals = this.chartData.map(d => d.total);
      console.log(this.chartData)

      this.renderChart({
          labels: dates,
          datasets: [{
            label: this.label,
            data: totals,
          }],
      }, this.options);
    }
  }
</script>