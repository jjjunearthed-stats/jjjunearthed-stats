$(document).ready(function() {
    var database = firebase.database();
    database.ref("6147").once("name").then(function(snapshot) {
        alert(snapshot);
    });
});
