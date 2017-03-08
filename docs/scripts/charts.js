window.onload = function() {
  google.charts.load('visualization', '1', {"packages": ["geochart"]});
  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawChart);

  // Callback that creates and populates a data table,
  // instantiates the pie chart, passes in the data and
  // draws it.
  function drawChart() {
    $.getJSON("data/artistByLocation.json", function(jsonData) {
      var options = {
        region: "IT",
        displayMode: "markers",
        colorAxis: {colors: ['green', 'blue']}
      };
      var data = google.visualization.arrayToDataTable([
        ['City',   'Population', 'Area'],
        ['Rome',      2761477,    1285.31],
        ['Milan',     1324110,    181.76]
      ]);
      var chart = new google.visualization.GeoChart(document.getElementById("chart_div"));
      chart.draw(data, options);
    });
  }
}
