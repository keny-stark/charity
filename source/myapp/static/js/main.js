function GetDistrict(_this) {
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/api/v1/district/?area=' + _this.value,
        success: function (data) {
            var _select_city = document.getElementById("city");
            var _select = document.getElementById("district");
            _select_city.innerHTML = "";
            _select.innerHTML = "";
            $('#district').append('<option selected disabled value="">выберите</option>');
            $.each(data, function(key, val) {
                $('#district').append('<option value="' + val.id + '">' + val.district + '</option>');
            });
        }
    })
}

function GetCity(_this) {
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/api/v1/city/?district=' + _this.value,
        success: function (data) {
            var _select = document.getElementById("city");
            _select.innerHTML = "";
            $.each(data, function(key, val) {
                $('#city').append('<option value="' + val.id + '">' + val.city_or_village + '</option>');
            });
        }
    })
}

$('.js-button-campaign').click(function() {
	$('.js-overlay-campaign').fadeIn();
	$('.js-overlay-campaign').addClass('disabled');
});
$('.js-close-campaign').click(function() {
	$('.js-overlay-campaign').fadeOut();
});


$(document).mouseup(function (e) {
	var popup = $('.js-popup-campaign');
	if (e.target!=popup[0]&&popup.has(e.target).length === 0){
		$('.js-overlay-campaign').fadeOut();
	}
});

$('.js-button-campaign_2').click(function() {
	$('.js-overlay-campaign_2').fadeIn();
	$('.js-overlay-campaign_2').addClass('disabled');
});
$('.js-close-campaign_2').click(function() {
	$('.js-overlay-campaign_2').fadeOut();
});

