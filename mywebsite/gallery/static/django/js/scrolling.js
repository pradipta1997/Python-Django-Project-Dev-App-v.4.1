$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    console.log(scroll)

    if(scroll >=100){
        $("myNav").addClass("bg-dark");
    }
    else {
        $("myNav").removeClass("bg-dark");
    }
});