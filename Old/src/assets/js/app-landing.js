
/*
Template: ProX - Responsive Bootstrap 4 Admin Dashboard Template
Author: iqonicthemes.in
Design and Developed by: iqonicthemes.in
NOTE: This file contains the styling for responsive Template.
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

:: Header fixed
:: Pricing
:: Time range
:: Input range
:: Price Checkbox
:: swiper js
:: Screenshots silder
:: Toggler Button
:: Header add class
:: Header Nav
:: Back to Top
:: Scroller
::  Wow Animation

------------------------------------------------
Index Of Script
----------------------------------------------*/

/*---------------------------
Header fixed
---------------------------*/

$(window).on('scroll', function () {
    if ($(window).scrollTop() > 100) {
        $('header').addClass('fixed');
    } else {
        $('header').removeClass('fixed');
    }
});

/*---------------------------
Pricing
---------------------------*/
var count_tabs = jQuery("#count-tabs").val();
for (var i = 0; i <= count_tabs; i++) {
    var maxnumber = jQuery("#number_user_" + i).val();
    jQuery('#user_range_' + i).range({


        min: 1,
        max: maxnumber,
        start: 1,
        step: 1,
        input: '#user_text_' + i



    });

}

/*---------------------------
Time range
---------------------------*/

for (var i = 0; i <= count_tabs; i++) {
    var maxnumber = jQuery("#number_time" + i).val();
    jQuery('#time_range_' + i).range({


        min: 1,
        max: maxnumber,
        start: 1,
        step: 1,
        input: '#time_text_' + i



    });

}

/*---------------------------
Input range
---------------------------*/
jQuery(".input-range").on("click mousemove", function () {

    var check = jQuery(this).attr('id');



    var id = jQuery(this).attr('id').match(/\d+/);



    var user_range = jQuery('#user_range_' + id);
    var time_range = jQuery('#time_range_' + id);

    var user_text = jQuery('#user_text_' + id);

    var time_text = jQuery('#time_text_' + id);

    var total = jQuery('#total_' + id);
    var base = jQuery('#base_' + id);


    total.val(user_text.val() * time_text.val() * base.val());

});


/*---------------------------
Price Checkbox
---------------------------*/

jQuery(".price-checkbox").on("click", function () {

    var a = [];
    var id = jQuery(this).attr('primary').match(/\d+/);
    var price = 0;
    var user_range = jQuery('#user_range_' + id);
    var time_range = jQuery('#time_range_' + id);

    var user_text = jQuery('#user_text_' + id);

    var time_text = jQuery('#time_text_' + id);
    var total = jQuery('#total_' + id);

    var base = jQuery('#base_' + id);

    console.log(id);
    console.log(base);


    jQuery(".chk_" + id + ":checked").each(function () {
        price += parseInt(jQuery(this).val());
    });

    base.val(price);
    total.val(user_text.val() * time_text.val() * base.val());
    console.log(price);
});

/*------------------------
swiper js
--------------------------*/
var mySwiper = new Swiper('.swiper-container', {
    speed: 400,
    spaceBetween: 100,
    initialSlide: 0,
    //truewrapper adoptsheight of active slide
    autoHeight: false,
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    // delay between transitions in ms
    autoplay: 5000,
    autoplayStopOnLast: false, // loop false also
    // If we need pagination
    pagination: '.swiper-pagination',
    paginationType: "bullets",

    // Navigation arrows
    nextButton: '.swiper-button-next',
    prevButton: '.swiper-button-prev',

    // And if we need scrollbar
    //scrollbar: '.swiper-scrollbar',
    // "slide", "fade", "cube", "coverflow" or "flip"
    effect: 'slide',
    // Distance between slides in px.
    spaceBetween: 60,
    //
    slidesPerView: 2,
    //
    centeredSlides: true,
    //
    slidesOffsetBefore: 0,
    //
    grabCursor: true,
})


/*------------------------
Screenshots silder
--------------------------*/
var slide = $('.slider-single');
var slideTotal = slide.length - 1;
var slideCurrent = -1;

function slideInitial() {
    slide.addClass('proactivede');
    setTimeout(function () {
        true;
        slideRight();
    }, 500);
}

function slideRight() {
    if (slideCurrent < slideTotal) {
        slideCurrent++;
    } else {
        slideCurrent = 0;
    }

    if (slideCurrent > 0) {
        var preactiveSlide = slide.eq(slideCurrent - 1);
    } else {
        var preactiveSlide = slide.eq(slideTotal);
    }
    var activeSlide = slide.eq(slideCurrent);
    if (slideCurrent < slideTotal) {
        var proactiveSlide = slide.eq(slideCurrent + 1);
    } else {
        var proactiveSlide = slide.eq(0);

    }

    slide.each(function () {
        var thisSlide = $(this);
        if (thisSlide.hasClass('preactivede')) {
            thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
        }
        if (thisSlide.hasClass('preactive')) {
            thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
        }
    });
    preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
    activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
    proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
}

function slideLeft() {
    if (slideCurrent > 0) {
        slideCurrent--;
    } else {
        slideCurrent = slideTotal;
    }

    if (slideCurrent < slideTotal) {
        var proactiveSlide = slide.eq(slideCurrent + 1);
    } else {
        var proactiveSlide = slide.eq(0);
    }
    var activeSlide = slide.eq(slideCurrent);
    if (slideCurrent > 0) {
        var preactiveSlide = slide.eq(slideCurrent - 1);
    } else {
        var preactiveSlide = slide.eq(slideTotal);
    }
    slide.each(function () {
        var thisSlide = $(this);
        if (thisSlide.hasClass('proactivede')) {
            thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
        }
        if (thisSlide.hasClass('proactive')) {
            thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
        }
    });
    preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
    activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
    proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
}

var left = $('.slider-left');
var right = $('.slider-right');
left.on('click', function () {
    slideLeft();
});
right.on('click', function () {
    slideRight();
});
slideInitial();

/*------------------------
Toggler Button
--------------------------*/
jQuery(document).ready(function () {
    jQuery(".menu-btn").click(function () {
        jQuery(this).toggleClass("is-active");
    });
});

/*------------------------
Header add class
--------------------------*/
$(document).ready(function () {
    $('.navbar-nav li a').on('click', function () {
        $('.navbar-nav li a.active').removeClass('active');
        $(this).addClass('active');
    });
});


/*------------------------
Header Nav
--------------------------*/
$('.navbar-nav li a').on('click', function (e) {
    var anchor = $(this);
    $('html, body').stop().animate({
        scrollTop: $(anchor.attr('href')).offset().top - 0
    }, 1500);
    e.preventDefault();
});

/*------------------------
Back to Top
--------------------------*/

jQuery('#back-to-top').fadeOut();
jQuery(window).on("scroll", function () {
    if (jQuery(this).scrollTop() > 250) {
        jQuery('#back-to-top').fadeIn(1400);
    } else {
        jQuery('#back-to-top').fadeOut(400);
    }
});

/*----------------
Scroller
---------------------*/

// scroll body to 0px on click
jQuery('#top').on('click', function () {
    jQuery('top').tooltip('hide');
    jQuery('body,html').animate({
        scrollTop: 0
    }, 800);
    return false;
});

/*---------------------------------------------------------------------
Wow Animation
-----------------------------------------------------------------------*/
var wow = new WOW({
    boxClass: 'wow',
    animateClass: 'animated',
    offset: 0,
    mobile: false,
    live: true
});
wow.init();
