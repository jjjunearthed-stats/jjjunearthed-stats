$(document).ready(function() {
    google.charts.load('current', {packages:['geochart', 'table']});
    google.charts.setOnLoadCallback(drawCharts);

  function drawCharts() {
      $('form').submit(function() {
          var xPath = $("#xPath").val();
          $.getJSON("data/artists.json", function(artistData) {
              var artists = search = JSON.search(artistData, xPath);
              $("#results").text("");
              for (var i = 0; i < artists.length; i++) {
                  $("#results").append(artists[i]);
              }
          });
      });
  }
});
