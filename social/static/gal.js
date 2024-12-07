
var hoverSize = [100, 400];

$('gimage').hover(function() {
    $(this).css({
        height: hoverSize[0],
        width: hoverSize[1]
    });
}, function() {
    $(this).css({
        height: "",
        width: ""
    });
});

