$(document).ready(function(){


	$.ajax({
		url:'/deadLines',
		type:'GET',
		dataType:'json',
		data:{},
		success:function(data, status, xhr) {
			if(data.isSubmitingDates == true)
			{
				document.getElementById("constrainInput").disabled = true; 
				document.getElementById("constrainTime").style.visibility = "visible";
			}
			else
			{
				document.getElementById("constrainInput").disabled = false; 
				document.getElementById("constrainTime").style.visibility = "hidden";
			}
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
		}
	});
});



	var userName = getQueryVariable("userName");
	  $.ajax({
		url:'/MainEmployee',
		type:'GET',
		dataType:'json',
        data:{userName: userName},
		success:function(data, status, xhr) {
			document.location.href = '/MainEmployee';
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	
	
