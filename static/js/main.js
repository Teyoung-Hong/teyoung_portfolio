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

});
