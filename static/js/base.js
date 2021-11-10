// show madal and write event into cookies
// $(window).on('load', function () {
//     if (document.cookie.indexOf('modal_shown=') >= 0) {
//         //do nothing if modal_shown cookie is present
//     } else {
//         var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
//             keyboard: false
//         })
//         myModal.toggle();
//         var now = new Date();
//         var time = now.getTime();
//         // Set cookie to expire in one hour
//         var expireTime = time + 3600000;
//         now.setTime(expireTime);
//         document.cookie = 'modal_shown=ok;expires=' + now.toUTCString() + ';path=/';
//     }

//     $(".close").click(function () {
//         myModal.toggle();
//     });
// });

// On scroll dow / up adjust top navigation bar
$(window).scroll(function () {
    if ($(document).scrollTop() > 70) {
        $('.logo-img').addClass('spec-logo-small');
        $('#topnav').addClass('spec-topnav-small');
        $('.navbar').addClass('spec-topnav-small');
        $('.to-top-btn').addClass('back-to-top-btn').fadeIn(300);
    } else {
        $('.logo-img').removeClass('spec-logo-small');
        $('#topnav').removeClass('spec-topnav-small');
        $('.navbar').removeClass('spec-topnav-small');
        $('.to-top-btn').removeClass('back-to-top-btn');
    }
});

$(window).scroll(function () {
    if ($(document).scrollTop() > 120) {
        $('.total-bag-sum').addClass('total-bag-sum-translate');
    } else {
        $('.total-bag-sum').removeClass('total-bag-sum-translate');
    }
});




$('.btt-link').click(function (e) {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
})



$(document).ready(function () {
    $('.toast').toast('show');
});
