<script>
  import { Line } from 'vue-chartjs'

  export default {
    extends: Line,
    props: {
      label: {
        type: Object,
        default: null,
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
      const dates = this.chartData.map(d => d.date);
      const totals = this.chartData.map(d => d.total);

      this.options.title = {
        display: true,
        fontSize: 20,
        text: this.label.name
      }

      this.renderChart({
          labels: dates,
          datasets: [{
            label: this.label.unit,
            data: totals,
          }],
      }, this.options);
    }
  }
</script>