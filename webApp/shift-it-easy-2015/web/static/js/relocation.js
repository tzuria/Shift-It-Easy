$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#relocate_to_add_remove').on('click', relocate_to_add_remove);
	$('#log_out').on('click', relocate_to_login_page);
    
});

function relocate_to_add_remove()
{
	document.location.href = '/AddRemoveEmployee';

}

function relocate_to_login_page()
{
	document.location.href = '/LoginPage';
}