var base_url = 'http://localhost:8000/RESTAPI?format=json';
$(document).ready(function(){
	$.ajax({
		type : "GET",
		url : base_url,
		beforeSend:function(){	
		},
		success:function(data){
			var main_frame = document.getElementById('arrivals');
			var n = data.length;
			var i = 0;
			while(i < n){
				var OUTER = '<div class="swiper arrivals-slider">';
				for(var j = 0;j < 3;j++){
					if(i >= n)
						 break;
					var URL_LINK = data[i].COVER;
					var ID = data[i].id;
					var TITLE = data[i].title;
					var BASE = '<div class="swiper-wrapper">'+
							            '<a href="DETAIL/'+ID+'" class="swiper-slide box">'+
							              '<div class="image">'+
							                '<img src="'+URL_LINK+'" alt="" />'+
							              '</div>'+
							              '<div class="content">'+
							                '<h3>'+TITLE+'</h3>'+
							              '</div>'+
							            '</a>'+
					          		'</div>';
				 	OUTER += BASE;
					i++;					          	
				}
	          	OUTER += '</div>';
				main_frame.innerHTML += OUTER;
			}
			
		}
	});
});
function show(value) {
    document.querySelector(".text-box").value = value;
  }
var swiper = new Swiper(".arrivals-slider", {
    spaceBetween: 10,
    loop:true,
    centeredSlides: true,
    autoplay: {
      delay: 9500,
      disableOnInteraction: false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });
  
  var swiper = new Swiper(".reviews-slider", {
    spaceBetween: 10,
    grabCursor:true,
    loop:true,
    centeredSlides: true,
    autoplay: {
      delay: 9500,
      disableOnInteraction: false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });
  
  var swiper = new Swiper(".blogs-slider", {
    spaceBetween: 10,
    grabCursor:true,
    loop:true,
    centeredSlides: true,
    autoplay: {
      delay: 9500,
      disableOnInteraction: false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });


