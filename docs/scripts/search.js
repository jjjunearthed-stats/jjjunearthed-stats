$(document).ready(function() {
    var snapshot = undefined;
    $.getJSON("data/artists.json", function(artistData) {
        snapshot = Defiant.getSnapshot(artistData);
    });
      $('button#Search').click(function() {
          var xPath = $("#xPath").val();
          var artists = search = JSON.search(snapshot, xPath);
          $("#results").text("");
          for (var i = 0; i < artists.length; i++) {
              $("#results").append(artists[i]);
          }
      });
});
