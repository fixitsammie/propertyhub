
jQuery(document).ready(function() {
	
    /*
        Background slideshow
    */    
    $('.testimonials-container').backstretch([
                                   "static/assets/img/backgrounds/2.jpg"
                                 , "static/assets/img/backgrounds/1.jpg"
                                 ], {duration: 3000, fade: 750});
    
    $('a[data-toggle="tab"]').on('shown.bs.tab', function(){
    	$('.testimonials-container').backstretch("resize");
    });
	
});
