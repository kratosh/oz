$(document).ready(function() {
});

// poll address until first change to true
function poll(address, interval, callback) {
    setTimeout(function () {
        $.get(address, function(data) {
            //alert('Polling result: ' + data);
            if (data == "True") {
                callback();
            }
            else {
                poll(address, interval, callback);
            }
        });
    }, interval);
}

function touch(url) {
    $.get(url);
}