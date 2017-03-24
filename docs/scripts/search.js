$(document).ready(function() {
    var database = firebase.database();
    database.ref("6147/name").once("value").then(function(snapshot) {
        alert(snapshot);
    });
});
