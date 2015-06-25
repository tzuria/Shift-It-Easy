
$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#add_employee').on('click', add_Employee);
	$('#remove').on('click', remove_Employee);
    
});
function doclear()
   {  
   document.getElementById('employee_id').value = "";
   document.getElementById('first_name').value = "";
   document.getElementById('last_name').value = "";
   document.getElementById('username').value = "";
   document.getElementById('password').value = "";
   document.getElementById('appointment_66').checked = false;
   document.getElementById('appointment_88').checked = false;
   document.getElementById('appointment_100').checked = false;
   document.getElementById('radio_yes').checked = false;
   document.getElementById('radio_no').checked = false;

   }
function remove_Employee(){
	var employee_id = $('#employee_id').val();
	
	$.ajax({
		url:'/remove_employee',
		type:'GET',
		dataType:'json',
        data:{employee_id: employee_id},
		success:function(data, status, xhr) {
			sweetAlert("employee removed successfully");
			
			document.location.href = '/AddRemoveEmployee';
		},
		error:function(xhr, status, error) {
			sweetAlert("failed-can not remove employee!");
            sweetAlert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	doclear();
}

function add_Employee() {
    var employee_id = $('#employee_id').val();
	var firstName = $('#first_name').val();
	var lastName = $('#last_name').val();
	var username = $('#username').val();
	var password = $('#password').val();
	
	var appointment;
	var shiftHeadable;
	
	if(document.getElementById('appointment_66').checked) 
	{
		appointment = 66;
	}
	else if(document.getElementById('appointment_88').checked) 
	{
		appointment = 88;
	}
	else if(document.getElementById('appointment_100').checked) 
	{
		appointment = 100;
	}	
	
	if(document.getElementById('radio_yes').checked) 
	{
		shiftHeadable = true;
	}
	else if(document.getElementById('radio_no').checked)
	{
		shiftHeadable = false;
	}
	
    $.ajax({
		url:'/add_new_employee',
		type:'GET',
		dataType:'json',
		data:{employee_id: employee_id, firstName: firstName, lastName: lastName, appointment: appointment, username: username, password:password, shiftHeadable:shiftHeadable},
		success:function(data, status, xhr) {
			sweetAlert("employee added successfully");
		},
		error:function(xhr, status, error) {
			sweetAlert("failed-can not add employee!");
            sweetAlert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	doclear();
}