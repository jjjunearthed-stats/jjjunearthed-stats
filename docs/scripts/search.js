$(document).ready(function() {
    var database = firebase.database();
    database.ref().orderByValue("name").on("value", function(snapshot) {
        snapshot.forEach(function(data) {
            alert("The " + data.key + " score is " + data.val());
      });
    });
});
