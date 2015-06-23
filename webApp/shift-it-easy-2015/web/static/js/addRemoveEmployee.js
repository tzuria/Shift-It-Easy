
$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#add_employee').on('click', add_Employee);
	$('#remove').on('click', remove_Employee);
    
});

function remove_Employee(){
	var employee_id = $('#employee_id').val();
	
	$.ajax({
		url:'/remove_employee',
		type:'GET',
		dataType:'json',
        data:{employee_id: employee_id},
		success:function(data, status, xhr) {
			alert("employee removed successfully");
			
			document.location.href = '/AddRemoveEmployee';
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

function add_Employee() {
    var employee_id = $('#employee_id').val();
	var firstName = $('#first_name').val();
	var lastName = $('#last_name').val();
	var appointment = $('#appointment').val();
	var username = $('#username').val();
	var password = $('#password').val();
	
    $.ajax({
		url:'/add_new_employee',
		type:'GET',
		dataType:'json',
        data:{employee_id: employee_id, firstName: firstName, lastName: lastName, appointment: appointment, username: username, password:password},
		success:function(data, status, xhr) {
			alert("employee added successfully");
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}