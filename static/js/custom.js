$(document).ready(function () {
    /***************** Navbar-Collapse ******************/

    $(window).scroll(function () {
        if ($(".navbar").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });

    /***************** Page Scroll ******************/

    $(function () {
        $('a.page-scroll').bind('click', function (event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });
    });

    /***************** Scroll Spy ******************/

    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    })

    /***************** Owl Carousel ******************/

    $("#owl-hero").owlCarousel({

        navigation: true, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true,
        transitionStyle: "fadeUp",
        autoPlay: true,
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]

    });


    /***************** Full Width Slide ******************/

    var slideHeight = $(window).height();

    $('#owl-hero .item').css('height', slideHeight);

    $(window).resize(function () {
        $('#owl-hero .item').css('height', slideHeight);
    });
    /***************** Owl Carousel Testimonials ******************/

    $("#owl-testi").owlCarousel({

        navigation: false, // Show next and prev buttons
        paginationSpeed: 400,
        singleItem: true,
        transitionStyle: "backSlide",
        autoPlay: true

    });
    /***************** Countdown ******************/

    $('#fun-facts').bind('inview', function (event, visible, visiblePartX, visiblePartY) {
        if (visible) {
            $(this).find('.timer').each(function () {
                var $this = $(this);
                $({
                    Counter: 0
                }).animate({
                    Counter: $this.text()
                }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function () {
                        $this.text(Math.ceil(this.Counter));
                    }
                });
            });
            $(this).unbind('inview');
        }
    });
    /***************** Leaflet Map ******************/
    mymap = L.map('mapid');
    mymap.setView([38.925533, 34.866287], 6);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);

    markers = [];
    $.get( "show_station").done(function (response) {
        var data = JSON.parse(response);
        data.forEach(function (station) {
           mymarker = L.marker([station.fields.location_lat, station.fields.location_lng], {
            }).addTo(mymap).on('click', showDetail);

            markers[mymarker._leaflet_id] = mymarker;
            $("#" + station.fields.name).append('<div class="marker" id="' + mymarker._leaflet_id + '"> </div>');
        });
    });

    /***************** Wow.js ******************/
    
    new WOW().init();
    
    /***************** Preloader ******************/
    
    var preloader = $('.preloader');
    $(window).load(function () {
        preloader.remove();
    });
})

function initMap() {
    autocomplete = new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */ (
                document.getElementById('findbox')));

    autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged()
{

    var place = autocomplete.getPlace();
    if (place.geometry)
    {
        var loc = place.geometry.location.toJSON();
        mymap.setView([loc['lat'], loc['lng']], 8);
        mymarker = L.marker([loc['lat'], loc['lng']], {
            draggable: true
        }).addTo(mymap);
    }
    else
    {
        document.getElementById('findbox').placeholder = 'Enter a city';
    }
}


function onMapClick(e) {
    alert("You clicked the map at " + e.latlng);
}


function saveStation()
{
    var name = document.getElementById('name').value;
    var address = document.getElementById('findbox').value;
    myloc = JSON.stringify(mymarker.getLatLng());
    $.post("add_station", {name: name, address: address, loc: myloc}, function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    })
}

function showDetail(){
    $('#detailModal').modal('show');
    $.get( "detail").done(function (response) {
        var newArray =[] ;

        for(var i in response.data_day.time) {
            var dict =  {};
            dict.label =  response.data_day.time[i];
            dict.x = parseInt(i);
            dict.y = parseInt(response.data_day.temperature_max[i]);

            newArray.push(dict);
        }

        var data = [];
        data.push(  {
            type: "line",
            lineThickness:3,
            axisYType:"primary", // for align the y to right
            showInLegend: true,
            name: 'Hava Durumu',
            dataPoints: newArray//[j]['data']
        });

        var chart = new CanvasJS.Chart("chartContainer",
        {
         data: data,
        });
        chart.render();
    });


}

$( ".del" ).click(function() {
    var id = $(this).siblings('div.marker').attr('id');
    markers[id].remove();

    var x = $(this).parent('div.box');
    x.remove();
});

$('.edit').click(function(){
  $(this).hide();
  $(this).siblings('span.del').hide();
  $(this).siblings('span.detail').hide();
  $(this).parent('div.box').addClass('editable');
  $(this).siblings('div.text').attr('contenteditable', true);
  $(this).siblings('span.save').show();
});

$('.save').click(function(){
  $(this).hide();
  $('.box').removeClass('editable');
  $('.text').removeAttr('contenteditable');
  $('.edit').show();
  $(this).siblings('span.del').show();
  $(this).siblings('span.detail').show();

});






