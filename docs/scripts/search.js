$(document).ready(function() {
    var database = firebase.database();
    database.ref("6147").once().then(function(snapshot) {
        alert(snapshot);
    });
});
