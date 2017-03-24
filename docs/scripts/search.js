$(document).ready(function() {
    var database = firebase.database();
    database.ref().orderByChild("name").startAt("Courtney Barnett").endAt("Courtney Barnett").on("value", function(snapshot) {
        snapshot.forEach(function(data) {
            alert("The " + data.key + " score is " + data.val());
      });
    });
});
