$(document).ready(function() {
    google.charts.load('current', {packages:['geochart', 'table', 'line', 'corechart', 'bar']});
    google.charts.setOnLoadCallback(drawCharts);

  function drawCharts() {
      $('.geoMap').each(function() {
          var dataUrl = $(this).attr("data-url");
          var chartElement = $(this)[0];
          
          $.getJSON(dataUrl, function(json) {
            var data = google.visualization.arrayToDataTable(json);
            var options = {region: 'AU', displayMode: 'markers', colors:['blue', 'red']};
            var chart = new google.visualization.GeoChart(chartElement);

            chart.draw(data, options);
          });
      });

      $('.barChart').each(function() {
          var data = new google.visualization.DataTable();
          var dataUrl = $(this).attr("data-url");
          var chartElement = $(this)[0];

          $.getJSON(dataUrl, function(json) {
            var data = google.visualization.arrayToDataTable(json);
            var options = {
                orientation: "vertical"
            };
            var chart = new google.charts.Bar(chartElement);

            chart.draw(data, google.charts.Bar.convertOptions(options));
          });
      });

      $('.pieChart').each(function() {
          var data = new google.visualization.DataTable();
          var dataUrl = $(this).attr("data-url");
          var chartElement = $(this)[0];

          $.getJSON(dataUrl, function(json) {
            var data = google.visualization.arrayToDataTable(json);
            var options = {};
            var chart = new google.visualization.PieChart(chartElement);

            chart.draw(data, options);
          });
      });

      $('.lineChart').each(function() {
          var data = new google.visualization.DataTable();
          var dataUrl = $(this).attr("data-url");
          var chartElement = $(this)[0];

          $.getJSON(dataUrl, function(json) {
            var data = google.visualization.arrayToDataTable(json);
            var options = {
                curveType: "function"
            };
            var chart = new google.charts.Line(chartElement);

            chart.draw(data, google.charts.Line.convertOptions(options));
          });
      });
      
      $(".table").each(function() {
          var dataUrl = $(this).attr("data-url");
          var dataColumns = $(this).attr("data-columns");
          var tableElement = $(this)[0];
          
          $.getJSON(dataUrl, function(json) {
            var data = new google.visualization.DataTable();
              $.each(JSON.parse(dataColumns), function(i, val) {
                  data.addColumn(val[0], val[1]);
              });
              
            data.addRows(json);

            var table = new google.visualization.Table(tableElement);
            var options = {
                showRowNumber: false, 
                width: '100%', 
                height: '100%',
                sortColumn: 2,
                sortAscending: false
            };
            table.draw(data, options);
          });
      });
  }
});
