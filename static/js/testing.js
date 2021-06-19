$(document).ready(function(){
    $('.col-4 .box').each(function(){
        var colors = 'rgba('+
                        (Math.floor((180-0)*Math.random())) + ',' +
                        (Math.floor((180-0)*Math.random())) + ',' +
                        (Math.floor((180-0)*Math.random()))
                      +')';
        $(this).css("background-color", colors);
    });
});