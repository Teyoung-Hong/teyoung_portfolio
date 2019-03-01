$(function(){

$('#head_word').hover(function(){
    $('#bb').css('background-color','black');
  },function(){
    $('#bb').css('background-color','');
});

$('#skills').on('click', function(){ 
  $('#genre').toggle(1000);
  $('#genre2').toggle(1200);
});

$('#work').on('click', function(){
  $('#work_item').toggle(500);
});

$('.header_box').on('inview', function() {
  $('#head_word').textillate({
    minDisplayTime: 3000,
    initialDelay: 1000,
    autoStart: true,

    in:{
      effect: 'fadeIn',
      delayScale: 1.5,
      delay: 50,
      sync: false,
      huffle: false  
    }
  });


});

});
