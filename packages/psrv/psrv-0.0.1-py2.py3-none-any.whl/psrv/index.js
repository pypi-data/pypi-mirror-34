'use strict';

var gaugesrv = require('gaugesrv/lib');
var $ = require('jquery');
var interval = 3000; // milliseconds


function update() {
    $.get('/status', function(data) {
        $.each(data, gaugesrv.toggle);
        setTimeout(update, interval);
    });
};


function main() {
    var gauges = $('canvas[data-psrv]');
    if (gauges.length == 0) {
        // don't set up the polling
        return;
    }
    update();
}


window.document.addEventListener('DOMContentLoaded', main);
