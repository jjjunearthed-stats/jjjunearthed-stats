$(document).ready(function() {
    var database = firebase.database();
    database.ref("6147").then(function(snapshot) {
        alert(snapshot);
    });
});
