<script>
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
	
</script>