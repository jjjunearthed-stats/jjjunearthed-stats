$(document).ready(function() {
    var database = firebase.database();
    database.ref().once("6147").then(function(snapshot) {
        alert(snapshot);
    });
});
