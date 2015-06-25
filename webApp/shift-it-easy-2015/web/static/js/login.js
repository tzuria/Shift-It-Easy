/**
 * Created by Yuri on 5/20/2015.
 */

$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
   $('#login').on('click', login);
});
	
function login() {
    var userName = $('#userName').val();
    var password = $('#password').val();
	
    $.ajax({
		url:'/login',
		type:'GET',
		dataType:'json',
        data:{userName: userName, password:password},
		success:function(data, status, xhr) {
			
			$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
			//we simulate form submition with a simple timeout
			setTimeout(function() {
				$('#form_spinner').addClass('hidden');
			}, 50000);
			
			if(data.isManager == 'Yes')
				document.location.href = '/MainManager';
			else
				document.location.href = '/MainEmployee';
		},
		error:function(xhr, status, error) {
            sweetAlert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	
}