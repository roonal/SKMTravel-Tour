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

/** this function automatically executes while window scroll and change the color of the nav bar **/

	$(window).scroll(function(){
		var top = $(window).scrollTop(); /**return scrolled pixel value in integer format **/
		if(top>=100)
		{
			$("header").addClass("secondary-dark-blue-bg")
		}
		else
		{
			if($("header").hasClass("secondary-dark-blue-bg")) /** class from reset.css **/
			{
				$("header").removeClass("secondary-dark-blue-bg");
			}
		}
	});
});


/** for the responsive navigation using slick nav **/

	// $('#menu').slicknav({
	// 	label:'',
	// })

/** for the parallax effect **/
// $("#main").stellar();

$(window).stellar();


