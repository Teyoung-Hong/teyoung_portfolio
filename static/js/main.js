$(function(){

$('#skills').on('click', function(){ 
  $('#genre').toggle(1000);
  $('#genre2').toggle(1200);
});

$('#work').on('click', function(){
  $('#work_item').toggle(500);
});

$.scrollify({
        section: ".section",
        scroollSpeed: 600,
        interstitialSection: "footer",
        eading: "swing",
        offset: 0,
        scrollbars: true,
        overflowScroll: true,
    });


});
