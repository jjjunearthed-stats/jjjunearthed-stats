window.onload = function() {
    google.charts.load('current', {packages:['geochart']});
    google.charts.setOnLoadCallback(drawMarkersMap);
    

  function drawMarkersMap() {
      $.getJSON("data/artistByLocation.json", function(json) {
        var data = google.visualization.arrayToDataTable(json);
        var options = {region: 'AU', displayMode: 'markers', colors:['green', 'blue']};
        var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
          
        chart.draw(data, options);
      });
    
  }
}
