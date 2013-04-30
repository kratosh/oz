$(document).ready(function() {
});

function post_json(url, data) {
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text'
    });
}

// reset
function reset_demo_state() {
    post_json('/sharedstate/demostate/set/', {'help_requested': false, 'helper_accepted': false});
}

// set a flag
function setflag(flagname) {
    data = {}
    data[flagname] = true;
    post_json('/sharedstate/demostate/update/', data);
}

// poll address until first change to true
function poll(flagname, interval, callback) {
    setTimeout(function () {
        $.get("/sharedstate/demostate/get/", function(data) {
            // alert('Polling result: ' + data);
            if (data[flagname] == true) {
                callback();
            }
            else {
                poll(flagname, interval, callback);
            }
        });
    }, interval);
}

function touch(url) {
    $.get(url);
}