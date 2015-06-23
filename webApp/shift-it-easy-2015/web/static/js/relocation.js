$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#relocate_to_add_remove').on('click', relocate_to_add_remove);
	$('#log_out').on('click', relocate_to_login_page);
	$('#back_to_main_manager').on('click', relocate_to_main_manager_page);
	$('#back_to_main_employee').on('click', relocate_to_main_employee_page);
	$('#to_previous_schedule').on('click', relocate_to_previous_schedule_page);
	$('#to_next_schedule').on('click', relocate_to_next_schedule_page);
	$('#to_constrains_input').on('click', relocate_to_constrains_input_page);
    
});

function relocate_to_add_remove()
{

	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/AddRemoveEmployee';
}

function relocate_to_login_page()
{

	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/LoginPage';
}

function relocate_to_main_manager_page()
{
	
	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/MainManager';
}

function relocate_to_main_employee_page()
{
	
	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/MainEmployee';
}

function relocate_to_previous_schedule_page()
{

	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/PreviousSchedule';
}

function relocate_to_next_schedule_page()
{

	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/NextSchedule';
}

function relocate_to_constrains_input_page()
{

	$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
	//we simulate form submition with a simple timeout
	setTimeout(function() {
		$('#form_spinner').addClass('hidden');
	}, 50000);

	document.location.href = '/ConstrainsInputPage';
}