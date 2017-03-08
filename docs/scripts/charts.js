window.onload = function() {
  google.charts.load('current', {'packages': ['geochart']});
  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawChart);

  // Callback that creates and populates a data table,
  // instantiates the pie chart, passes in the data and
  // draws it.
  function drawChart() {
    $.getJSON('test.json', function(jsonData) {
      var options = {
        region: 'AU',
        displayMode: 'markers',
        colorAxis: {colors: ['green', 'blue']}
      };
      var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    });
  }
}
