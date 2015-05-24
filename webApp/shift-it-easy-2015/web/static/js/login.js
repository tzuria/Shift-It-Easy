/**
 * Created by Yuri on 5/20/2015.
 */

$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#login_as_manager').on('click', login_as_manager);
    $('#login_as_employee').on('click', login_as_employee);
});

function login_as_manager() {
    var userName = $('#userName').val();
    var password = $('#password').val();
	alert("manager pressed!");
    $.ajax({
		url:'/login',
		type:'GET',
		dataType:'json',
        data:{userName: userName, password:password},
		success:function(data, status, xhr) {
			alert("success!");
			document.location.href = '/MainManager';
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

function login_as_employee() {
    var userName = $('#userName').val();
    var password = $('#password').val();
    $.ajax({
		url:'/login',
		type:'GET',
		dataType:'json',
        data:{userName: userName, password:password},
		success:function(data, status, xhr) {
			document.location.href = '/MainEmployee';
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	
}