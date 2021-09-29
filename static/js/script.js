$(document).ready(function () {
  $(".card-shadow").hover(
    function () {
      $(this).addClass("shadow-lg").css("cursor", "pointer");
    },
    function () {
      $(this).removeClass("shadow-lg");
    }
  );

  /*-------------------------------------
    OwlCarousel
    -------------------------------------*/
  $(".rs-team .rs-carousel").each(function () {
    const owlCarousel = $(this),
      loop = owlCarousel.data("loop"),
      items = owlCarousel.data("items"),
      margin = owlCarousel.data("margin"),
      autoplay = owlCarousel.data("autoplay"),
      autoplayTimeout = owlCarousel.data("autoplay-timeout"),
      smartSpeed = owlCarousel.data("smart-speed"),
      nav = owlCarousel.data("nav"),
      navSpeed = owlCarousel.data("nav-speed"),
      xsDevice = owlCarousel.data("mobile-device"),
      xsDeviceNav = owlCarousel.data("mobile-device-nav"),
      smDevice = owlCarousel.data("ipad-device"),
      smDeviceNav = owlCarousel.data("ipad-device-nav"),
      smDevice2 = owlCarousel.data("ipad-device2"),
      smDeviceNav2 = owlCarousel.data("ipad-device-nav2"),
      centerMode = owlCarousel.data("center-mode");

    owlCarousel.owlCarousel({
      loop: loop ? true : false,
      items: items ? items : 3,
      lazyLoad: true,
      center: centerMode ? true : false,
      margin: margin ? margin : 0,
      autoplay: autoplay ? true : false,
      autoplayTimeout: autoplayTimeout ? autoplayTimeout : 1000,
      smartSpeed: smartSpeed ? smartSpeed : 250,
      nav: nav ? true : false,
      navText: [
        "<i class='fa fa-arrow-left'></i>",
        "<i class='fa fa-arrow-right'></i>",
      ],
      navSpeed: navSpeed ? true : false,
      responsiveClass: true,
      responsive: {
        0: {
          items: xsDevice ? xsDevice : 1,
          nav: xsDeviceNav ? true : false,
          center: false,
        },
        576: {
          items: smDevice ? smDevice : 2,
          nav: smDeviceNav ? true : false,
          center: false,
        },
        768: {
          items: smDevice2 ? smDevice2 : 3,
          nav: smDeviceNav2 ? true : false,
          center: false,
        },
      },
    });
  });

  $(".rs-video .rs-carousel").each(function () {
    const owlCarousel = $(this),
      loop = owlCarousel.data("loop"),
      items = owlCarousel.data("items"),
      margin = owlCarousel.data("margin"),
      autoplay = owlCarousel.data("autoplay"),
      autoplayTimeout = owlCarousel.data("autoplay-timeout"),
      smartSpeed = owlCarousel.data("smart-speed"),
      nav = owlCarousel.data("nav"),
      navSpeed = owlCarousel.data("nav-speed"),
      xsDevice = owlCarousel.data("mobile-device"),
      xsDeviceNav = owlCarousel.data("mobile-device-nav"),
      smDevice = owlCarousel.data("ipad-device"),
      smDeviceNav = owlCarousel.data("ipad-device-nav"),
      centerMode = owlCarousel.data("center-mode");
    owlCarousel.owlCarousel({
      loop: loop ? true : false,
      items: items ? items : 2,
      lazyLoad: true,
      center: centerMode ? true : false,
      margin: margin ? margin : 0,
      autoplay: autoplay ? true : false,
      autoplayTimeout: autoplayTimeout ? autoplayTimeout : 1000,
      smartSpeed: smartSpeed ? smartSpeed : 250,
      nav: nav ? true : false,
      navText: [
        "<i class='fa fa-arrow-left'></i>",
        "<i class='fa fa-arrow-right'></i>",
      ],
      navSpeed: navSpeed ? true : false,
      responsiveClass: true,
      responsive: {
        0: {
          items: xsDevice ? xsDevice : 1,
          nav: xsDeviceNav ? true : false,
          center: false,
        },
        576: {
          items: smDevice ? smDevice : 2,
          nav: smDeviceNav ? true : false,
          center: false,
        },
      },
    });
  });

  $(".rs-image .rs-carousel").each(function () {
    const owlCarousel = $(this),
      loop = owlCarousel.data("loop"),
      items = owlCarousel.data("items"),
      margin = owlCarousel.data("margin"),
      autoplay = owlCarousel.data("autoplay"),
      autoplayTimeout = owlCarousel.data("autoplay-timeout"),
      smartSpeed = owlCarousel.data("smart-speed"),
      nav = owlCarousel.data("nav"),
      navSpeed = owlCarousel.data("nav-speed"),
      xsDevice = owlCarousel.data("mobile-device"),
      xsDeviceNav = owlCarousel.data("mobile-device-nav"),
      smDevice = owlCarousel.data("ipad-device"),
      smDeviceNav = owlCarousel.data("ipad-device-nav"),
      smDevice2 = owlCarousel.data("ipad-device2"),
      smDeviceNav2 = owlCarousel.data("ipad-device-nav2"),
      centerMode = owlCarousel.data("center-mode"),
      mdDevice = owlCarousel.data("md-device"),
      mdDeviceNav = owlCarousel.data("md-device-nav");
    owlCarousel.owlCarousel({
      loop: loop ? true : false,
      items: items ? items : 4,
      lazyLoad: true,
      center: centerMode ? true : false,
      margin: margin ? margin : 0,
      autoplay: autoplay ? true : false,
      autoplayTimeout: autoplayTimeout ? autoplayTimeout : 1000,
      smartSpeed: smartSpeed ? smartSpeed : 250,
      nav: nav ? true : false,
      navText: [
        "<i class='fa fa-arrow-left'></i>",
        "<i class='fa fa-arrow-right'></i>",
      ],
      navSpeed: navSpeed ? true : false,
      responsiveClass: true,
      responsive: {
        0: {
          items: xsDevice ? xsDevice : 1,
          nav: xsDeviceNav ? true : false,
          center: false,
        },
        576: {
          items: smDevice ? smDevice : 2,
          nav: smDeviceNav ? true : false,
          center: false,
        },
        768: {
          items: smDevice2 ? smDevice2 : 3,
          nav: smDeviceNav2 ? true : false,
          center: false,
        },
        992: {
          items: mdDevice ? mdDevice : 4,
          nav: mdDeviceNav ? true : false,
        },
      },
    });
  });
});
