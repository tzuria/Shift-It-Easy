$(function() { 
	$.ajax({
		url:'/check_submit_session',
		type:'GET',
		dataType:'json',
        data:{},
		success:function(data, status, xhr) {
			if(data.isSubmitSession == true)
			{
				$("#to_constrains_input").hide();
				$("#not_constrain_input_time").show();
			}
			else
			{
				$("#to_constrains_input").show();
				$("#not_constrain_input_time").hide();
			}
			
			
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});

});