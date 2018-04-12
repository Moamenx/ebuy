/*global $, alert, console*/

$(function () {

    'use strict';

    // ------------------------- Variables -------------------------
    var search = $(".search"),
        catsNav = $(".cats-nav"),
        aboutFixedBtn = $(".about-fixed-btn"),
        loginForm = document.getElementById('login-form'),
        fixedLogin = document.getElementById('fixedLogin'),
        loginWindow = document.getElementById('loginWindow'),
        close = document.getElementById('close');
    // ------------------------- Variables -------------------------
    
    /* *************** Functions *************** */
    function closeElement(close, elem) {
        $(close).click(function () {
            $(elem).fadeOut(200);
        });
    }

    function formsControl(btn, holder) {
        $(btn).click(function () {
            $(holder).fadeIn(200);
        });
    }
    /* *************** Functions *************** */
    
    /* *************** INVOKES ***************** */
    /* Login & Signup Forms */
    formsControl(".login-form-icon", ".login");
    closeElement(close, '.login');
    /* Login & Signup Forms */
    /* *************** INVOKES ***************** */
    
    // 0000========== Text Faded Animation ==========0000
    (function selffunction() {
        $(".nav .faded-text .active").each(function () {
            if (!$(this).is(":last-child")) {
                $(this).delay(3000).fadeOut(1000, function () {
                    $(this).removeClass("active").next().addClass("active").fadeIn(1000);
                    selffunction();
                });
            } else {
                $(this).delay(3000).fadeOut(1000, function () {
                    $(this).removeClass('active');
                    $(this).parent().find(".box").first().addClass("active").fadeIn(1000);
                    selffunction();
                });
            }
        });
    }());

    (function selffunction() {
        $(".uppernav .faded-upper-text .active").each(function () {
            if (!$(this).is(":last-child")) {
                $(this).delay(3000).fadeOut(1000, function () {
                    $(this).removeClass("active").next().addClass("active").fadeIn(1000);
                    selffunction();
                });
            } else {
                $(this).delay(3000).fadeOut(1000, function () {
                    $(this).removeClass('active');
                    $(this).parent().find(".box").first().addClass("active").fadeIn(1000);
                    selffunction();
                });
            }
        });
    }());
    // 0000========== Text Faded Animation ==========0000

    /* Search Trick */
    $(".search-icon").click(function () {
        search.slideToggle();
        catsNav.toggleClass('goDown');
        $(".mobnav").toggleClass("slidingToggle");
    });
    $(".search-close").click(function () {
        search.slideUp();
        catsNav.toggleClass('goDown');
        $(".mobnav").toggleClass("slidingToggle");
    });
    /* Search Trick */

    /* Close About Modal */
    $(".about-modal .window i").click(function () {
        $(this).parent().parent().fadeOut();
        aboutFixedBtn.css({
            display: "block",
            animation: "rightMove 1s ease-in-out"
        });
    });
    aboutFixedBtn.click(function () {
        $(".about-modal").fadeIn();
    });
    /* Close About Modal */

    /* See Product Modal */
   /* $(".see").click(function () {
        $(".product-modal").fadeIn(400);
    });*/
   $(".category .product .image .see").click(function () {
        /$(this).parent().addClass('active').siblings().removeClass('active');/
        $(".product-modal").fadeOut();
        $($(this).data('class')).fadeIn();
        console.log($(this).data('class'));
    });
    $(".product-modal .close-this-product-modal").click(function () {
        $(this).parent().fadeOut();
    });
    /* See Product Modal */
    
    /* Contact Form */
    $(".contact-form textarea").click(function () {
        $(this).css('height', '200px');
    });
    /* Contact Form */

    // Our Auto Slider Code
    (function selfSlider() {

        $(".testimonials .active").each(function () {

            if (!$(this).is(':last-child')) {

                $(this).delay(1500).fadeOut(1000, function () {

                    $(this).removeClass("active").next().addClass("active").fadeIn(1000);

                    selfSlider();
                });

            } else {

                $(this).delay(3000).fadeOut(1000, function () {

                    $(this).removeClass("active");

                    $(".testimonials ul li").eq(0).addClass("active").fadeIn(1000);

                    selfSlider();
                });
            }
        });
    }());

    // Cart Button
    $(".cart-btn").click(function () {
        $(".cart-modal").fadeIn();
    });
    $(".close-this-cart-modal").click(function () {
        $(".cart-modal").fadeOut();
    });

    // Shuffle
    $(".product-page-content .shuffle .col div").click(function () {
        $(this).parent().addClass('active').siblings().removeClass('active');
        $(".product-page-content .image > div").hide();
        $($(this).data('class')).show();
        console.log($(this).data('class'));
    });

    // Delete Cart Product
    $(".cart-page-content .col-12 i").click(function () {
        $(this).parent().fadeOut();
    }, function () {
        $(".cart-page-content .col-12 input[type='submit']").click();
    });

    /* Hamburger Active */
    $(".icon").click(function () {
        $(this).toggleClass('active');
        $(".nav-content .mlinks").slideToggle(300);
    });
    /* Hamburger Active */

    /* 5th Li Mobile */
    $(".mdrop").click(function () {
        $(".mdropMenu").slideToggle(200);
    });
    /* 5th Li Mobile */

    /* Dynamic Price Currency */
    function changePriceDynamic(elem, value, currency) {
        $(elem).each(function () {
            $(elem).click(function () {
                if ($(elem).is(':checked')) {
                    $(".price .changedPrice").text($(".price .changedPrice").text() * value);
                    $(".price .changedCurrency").text(" " + currency);
                } else {
                    $(".price .changedPrice").text(1200);
                }
            });
        });
    }
    changePriceDynamic(".product-page-content form input[value='AED']", 2, "AED");
    changePriceDynamic(".product-page-content form input[value='QAR']", 1.3, "QAR");
    changePriceDynamic(".product-page-content form input[value='OMR']", 2.3, "OMR");
    changePriceDynamic(".product-page-content form input[value='SAR']", 0.9, "SAR");
    changePriceDynamic(".product-page-content form input[value='KWD']", 0.5, "KWD");
    changePriceDynamic(".product-page-content form input[value='JOD']", 1.5, "JOD");
    
    /* Login & Logout */
    $(".nav .rhs .logged-in ul li:first-of-type i").on("click", function () {
        $(".nav .rhs .logged-in ul li:last-of-type").slideToggle(200);
    });
});
