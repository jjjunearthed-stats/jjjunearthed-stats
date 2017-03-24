$(document).ready(function() {
    $.getJSON("data/artists.json", function(artistData) {
        var snapshot = Defiant.getSnapshot(artistData);
    });
  function drawCharts() {
      $('button#Search').click(function() {
          var xPath = $("#xPath").val();
          var artists = search = JSON.search(snapshot, xPath);
          $("#results").text("");
          for (var i = 0; i < artists.length; i++) {
              $("#results").append(artists[i]);
          }
      });
  }
});
