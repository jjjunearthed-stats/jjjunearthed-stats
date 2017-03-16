$(document).ready(function() {
    google.charts.load('current', {packages:['geochart']});
    google.charts.setOnLoadCallback(drawCharts);

  function drawCharts() {
      $('.geoMap').each(function() {
          var dataUrl = $(this).attr('data-url');
          var chartElement = $(this)[0];
          
          $.getJSON(dataUrl, function(json) {
            var data = google.visualization.arrayToDataTable(json);
            var options = {region: 'AU', displayMode: 'markers', colors:['blue', 'red']};
            var chart = new google.visualization.GeoChart(chartElement);

            chart.draw(data, options);
          });
      });
  }
});
