
(function ($) {
    "use strict";

    /*---------------------------------------------------------------------
    Page Loader
    -----------------------------------------------------------------------*/
    jQuery("#load").fadeOut();
    jQuery("#loading").delay().fadeOut("");

   

    // logo animation

    var lFollowX = 0,
        lFollowY = 0,
        x = 0,
        y = 0,
        friction = 1 / 30;

    function animate() {
        x += (lFollowX - x) * friction;
        y += (lFollowY - y) * friction;

        var translate = 'translate(' + x + 'px, ' + y + 'px) scale(1.1)';

        $('.img-animate').css({
            '-webit-transform': translate,
            '-moz-transform': translate,
            'transform': translate
        });

        window.requestAnimationFrame(animate);
    }
    $(window).on('mousemove click', function (e) {

        var lMouseX = Math.max(-100, Math.min(100, $(window).width() / 2 - e.clientX));
        var lMouseY = Math.max(-100, Math.min(100, $(window).height() / 2 - e.clientY));
        lFollowX = (20 * lMouseX) / 100; // 100 : 12 = lMouxeX : lFollow
        lFollowY = (10 * lMouseY) / 100;

    });

    animate();

    // counter slider
    $('.counter-slider').slick({
        dots: false,
        arrows: false,
        infinite: true,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    /*---------------------------------------------------------------------
    Counter
    -----------------------------------------------------------------------*/
    if (window.counterUp !== undefined) {
        const counterUp = window.counterUp["default"]
        const $counters = $(".counter");
        $counters.each(function (ignore, counter) {
            var waypoint = new Waypoint({
                element: $(this),
                handler: function () {
                    counterUp(counter, {
                        duration: 1000,
                        delay: 10
                    });
                    this.destroy();
                },
                offset: 'bottom-in-view',
            });
        });
    }

    // demo box hover

    $('.js-tilt').tilt({

    });

    $('.inner-slider').slick({
        dots: false,
        arrows: true,
        infinite: true,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll:1,
        centerMode:true,
        centerPadding: '100px',
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 700,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    $('.inner-slider1').slick({
        dots: false,
        arrows: true,
        infinite: true,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        centerMode: true,
        centerPadding: '200px',
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 700,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });


    // fixed section nav
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 350) {
            $('.scroll-nav').addClass('n-fixed');
        } else {
            $('.scroll-nav').removeClass('n-fixed');
        }
    });

    function sticky_relocate() {
        var window_top = $(window).scrollTop();
        if ($('.scroll-section').length && $('#page-technology').length) {
            var div_top = $('#page-technology').offset().top + 360;
            var div_bottom = $('#lts').offset().top;
            if (window_top > div_top && window_top < div_bottom)  {
                $('.scroll-section .scroll-nav').addClass('n-fixed');
            }
            else {
                $('.scroll-section .scroll-nav').removeClass('n-fixed');
            }
        }
    }
    $(function () {
        $(window).scroll(sticky_relocate);
        sticky_relocate();
    });


    /*------------------------
    Header
    --------------------------*/
    $('.scroll-nav li a').on('click', function (e) {
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

    // Scrollbar.initAll();
    // butter.init({ cancelOnTouch: true });

    
    /*------------------------
        Play Audio
    --------------------------*/

        
        $('#my_audio').on('click', function (e) {
            var audio = document.getElementById('bg-audio');
            if ($(this).attr('data-value') == 'true') {
                $(this).attr('data-value', false)
                $(this).find('#vol-down').removeClass('d-none')
                $(this).find('#vol-up').addClass('d-none')
                audio.pause()
            } else {
                $(this).attr('data-value', true)
                $(this).find('#vol-up').removeClass('d-none')
                $(this).find('#vol-down').addClass('d-none')
                audio.play()
            }
        })


})(jQuery);
