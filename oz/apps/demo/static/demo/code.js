$(document).ready(function() {
});

// set image for central div
function divimg(img) {
    $("#center").css("background-image", "url('/static/demo/" + img + "')")
};

// post a json (TODO: with djangorest, the way god intended)
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

function set_whiteboard_id(wbid) {
    post_json('/sharedstate/whiteboard/set/', {'wbid' : wbid});
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