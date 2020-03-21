jQuery(document).ready(function(){

	"use strict"; /**defines that js should be executed in strict mode **/

/** this function is for home page slider configuration **/

	$('#slider-carousel').carouFredSel({
		responsive: true,
		width: '100%',
		circular: true,
		pagination:{
			container: ".slider-pager",
			anchorBuilder: false
		},
		scroll:{
			items: 1,
			duration: 500,
			pauseOnHover: true
		},
		auto: true,
		items: {
			visible:{
				min:1, /**only 1 item to be visible at a time **/
				max:1
			},
		height: "variable"
		}

	});

/** this function is for portfolio slider configuration **/

	$('.portfolio-carousel').carouFredSel({
		responsive: true,
		width: '100%',
		circular: true,
		prev: '#prev',
		next: '#next',
		scroll:{
			items: 1,
			duration: 500,
			pauseOnHover: true
		},
		auto: true,
		items: {
			visible:{
				min:1, /**only 1 item to be visible at a time **/
				max:4
			},
		height: "variable"
		}

	});

	/** this function is for portfolio slider configuration **/

	$('.team-carousel').carouFredSel({
		responsive: true,
		width: '100%',
		circular: true,
		prev: '#team-prev',
		next: '#team-next',
		scroll:{
			items: 1,
			duration: 500,
			pauseOnHover: true
		},
		auto: true,
		items: {
			visible:{
				min:1, /**only 1 item to be visible at a time **/
				max:4
			},
		height: "variable"
		}

	});

	/** this function is for home page slider configuration **/

	$('.testimonials-carousel').carouFredSel({
		responsive: true,
		width: '100%',
		circular: true,
		pagination:{
			container:".testimonials-pager",
			anchorBuilder: false
		},
		scroll:{
			items: 1,
			duration: 500,
			pauseOnHover: true
		},
		auto: true,
		items: {
			visible:{
				min:1, /**only 1 item to be visible at a time **/
				max:1
			},
		height: "variable"
		}

	});


	/** this function is for home page last slider configuration  **/

	$('.last-slider-carousel').carouFredSel({
		responsive: true,
		width: '100%',
		circular: true,
		pagination:{
			container:".last-slider-pager",
			anchorBuilder: false
		},
		scroll:{
			items: 1,
			duration: 500,
			pauseOnHover: true
		},
		auto: true,
		items: {
			visible:{
				min:1, /**only 1 item to be visible at a time **/
				max:1
			},
		height: "variable"
		}

	});


/** this function automatically executes while window scroll and change the color of the nav bar **/

	$(window).scroll(function(){
		var top = $(window).scrollTop(); /**return scrolled pixel value in integer format **/
		if(top>=100)
		{
			$(".navbar2").addClass("sticky")
		}
		else
		{
			if($(".navbar2").hasClass("scroll")) /** class from reset.css **/
			{
				$(".navbar2").addClass("fixed");
				$(".navbar2").removeClass("sticky");
			}
		}
	});

/** for displaying the inactive collpasible item of why SKM? section **/
		$('#first').hide();
		$('#second').hide();
		$('#third').hide();
		$('#fourth').hide();

		$('#accordion1').click(function(){
		    $('#first').slideToggle();
		    $('#fourth:visible').toggle();
		    $('#second:visible').toggle();
		    $('#third:visible').toggle();
		})

		$('#accordion2').click(function(){
		    $('#second').slideToggle();
		    $('#fourth:visible').toggle();
		    $('#first:visible').toggle();
		    $('#third:visible').toggle();
		})

		$('#accordion3').click(function(){
		    $('#third').slideToggle();
		    $('#fourth:visible').toggle();
		    $('#second:visible').toggle();
		    $('#first:visible').toggle();
		})

		$('#accordion4').click(function(){
		    $('#fourth').slideToggle();
		    $('#first:visible').toggle();
		    $('#second:visible').toggle();
		    $('#third:visible').toggle();
		})


/** for scroll to top button **/

	$(window).scroll(function(){
		if($(this).scrollTop() >200){
			$('.ScrollToTop').fadeIn();
		}
		else{
			$('.ScrollToTop').fadeOut();
		}
	});

	//smooth scrolling to top
	$('.ScrollToTop').click(function(){
		$("html").animate({scrollTop: 0},2000);

	})
});


