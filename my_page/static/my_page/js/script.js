$('document').ready(function(){
    $('.map').hide();
    $('.anthem').hide();
    $('.button').hide();
    

    $('#title').click(function(){
        $('.map').show(1000)
    })
    $('#title').dblclick(function(){
        $('.anthem').show(1000)
    })

    // $(".btn1").click(function(){
    //     $("img").animate({width:"300px", height:"300px"}, 1000);
    // });
    
    // $('.intro').children().css('border', '3px solid red');
});

