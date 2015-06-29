$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
   $('#changepass').on('click', changePassword);
});
$(function() { 
	$.ajax({
		url:'/check_submit_session',
		type:'GET',
		dataType:'json',
        data:{},
		success:function(data, status, xhr) {
			if(data.isSubmitSession == true)
			{
				//$("#to_constrains_input").hide();
				//$("#not_constrain_input_time").show();
			}
			else
			{
				$("#to_constrains_input").show();
				$("#not_constrain_input_time").hide();
			}
			
			
		},
		error:function(xhr, status, error) {
			sweetAlert("failed!");
            sweetAlert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});

});
function changePassword() {	
	
		swal
		({   
			title: "Change your password",
			text: "Write a new password:",
			type: "input",
			showCancelButton: true,
			closeOnConfirm: false,
			animation: "slide-from-top", 
			inputPlaceholder: "Write something" },
		
			function(inputValue)
			{
				if (inputValue === false) return false;
				if (inputValue === "") 
				{     
					swal.showInputError("You need to write something!");
					return false   
				}
					$.ajax({
						url:'/change_new_Password',
						type:'GET',
						dataType:'json',
						data:{newPassword: inputValue},
						success:function(data, status, xhr) {
									swal("Your new password is", inputValue, "success");
						},
						error:function(xhr, status, error) 
						{
							sweetAlert("Oops...", "Can't change Password", "error");
							sweetAlert(xhr.responseText);
							console.error(xhr, status, error);
						}
					});	
			}	
		);
}