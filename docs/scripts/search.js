$(document).ready(function() {
    var database = firebase.database();
    database.ref().orderByValue().on("name", function(snapshot) {
        snapshot.forEach(function(data) {
            alert("The " + data.key + " score is " + data.val());
      });
    });
});
