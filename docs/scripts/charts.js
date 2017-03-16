$(document).ready(function() {
    google.charts.load('current', {packages:['geochart', 'table']});
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
      
      $(".table").each(function() {
          var dataUrl = $(this).attr('data-url');
          
          $.getJSON(dataUrl, function(json) {
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Location');
            data.addColumn('number', 'Number of bands');
            data.addColumn('number', 'Number of bands per 100 000 people');
            data.addRows(json);

            var table = new google.visualization.Table(document.getElementById('table_div'));

            table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
          });
      });
  }
});
