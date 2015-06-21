$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#save').on('click', save_Schedule);
	$('#submit').on('click', submit_Schedule);
	
	//assign sunday night
	$('#head_nurse_list_sunday1').bind('change', {id: "head_nurse_list_sunday1",day: 6, shift: 0, week: 0, rule: 0},updateShift);
    $('#second_nurse_list_sunday1').bind('change', {id: "second_nurse_list_sunday1",day: 6, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_list_sunday1').bind('change', {id: "stand_by_list_sunday1",day: 6, shift: 0, week: 0, rule: 3},updateShift);
	
	//assign monday night
	$('#head_nurse_list_monday1').bind('change', {id: "head_nurse_list_monday1",day: 0, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_monday1').bind('change', {id: "second_nurse_list_monday1",day: 0, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_list_monday1').bind('change', {id: "stand_by_list_monday1",day: 0, shift: 0, week: 0, rule: 3},updateShift);
	
	//assign tuesday night
	$('#head_nurse_list_tuesday1').bind('change', {id: "head_nurse_list_tuesday1",day: 1, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_tuesday1').bind('change', {id: "second_nurse_list_tuesday1",day: 1, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_tuesday1').bind('change', {id: "stand_by_nurse_list_tuesday1",day: 1, shift: 0, week: 0, rule: 3},updateShift);
	
	//assign wednesday night
	$('#head_nurse_list_wednesday1').bind('change', {id: "stand_by_nurse_list_tuesday1",day: 2, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_wednesday1').bind('change', {id: "second_nurse_list_wednesday1",day: 2, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_wednesday1').bind('change', {id: "stand_by_nurse_list_wednesday1",day: 2, shift: 0, week: 0, rule: 3},updateShift);
	
	//assign thursday night
	$('#head_nurse_list_thursday1').bind('change', {id: "head_nurse_list_thursday1",day: 3, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_thursday1').bind('change', {id: "second_nurse_list_thursday1",day: 3, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_thursday1').bind('change', {id: "stand_by_nurse_list_thursday1",day: 3, shift: 0, week: 0, rule: 3},updateShift);
	
	//assign friday night
	$('#head_nurse_list_friday1').bind('change', {id: "head_nurse_list_friday1",day: 4, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_friday1').bind('change', {id: "second_nurse_list_friday1",day: 4, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday1').bind('change', {id: "stand_by_nurse_list_friday1",day: 4, shift: 0, week: 0, rule: 2},updateShift);
	
	//assign saturday night
	$('#head_nurse_list_saturday1').bind('change', {id: "head_nurse_list_saturday1",day: 5, shift: 0, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_saturday1').bind('change', {id: "second_nurse_list_saturday1",day: 5, shift: 0, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday1').bind('change', {id: "stand_by_nurse_list_saturday1",day: 5, shift: 0, week: 0, rule: 3},updateShift);
	
	
	
	
	
	//assign sunday morning
	$('#head_nurse_list_sunday2').bind('change', {id: "head_nurse_list_sunday2",day: 6, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_sunday2').bind('change', {id: "second_nurse_list_sunday2",day: 6, shift: 1, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_sunday2').bind('change', {id: "stand_by_nurse_list_sunday2",day: 6, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign monday morning
	$('#head_nurse_list_monday2').bind('change', {id: "head_nurse_list_monday2",day: 0, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_monday2').bind('change', {id: "second_nurse_list_monday2",day: 0, shift: 1, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_monday2').bind('change', {id: "stand_by_nurse_list_monday2",day: 0, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign tuesday morning
	$('#head_nurse_list_tuesday2').bind('change', {id: "head_nurse_list_tuesday2",day: 1, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_tuesday2').bind('change', {id: "second_nurse_list_tuesday2",day: 1, shift: 1, week: 0, rule: 1},updateShift);
	$('#third_nurse_list_tuesday2').bind('change', {id: "third_nurse_list_tuesday2",day: 1, shift: 1, week: 0, rule: 2},updateShift);
	$('#stand_by_nurse_tuesday2').bind('change', {id: "stand_by_nurse_tuesday2",day: 1, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign wednesday morning
	$('#head_nurse_list_wednesday2').bind('change', {id: "head_nurse_list_wednesday2",day: 2, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_wednesday2').bind('change', {id: "second_nurse_list_wednesday2",day: 2, shift: 1, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_wednesday2').bind('change', {id: "stand_by_nurse_list_wednesday2",day: 2, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign thursday morning
	$('#head_nurse_list_thursday2').bind('change', {id: "head_nurse_list_thursday2",day: 3, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_thursday2').bind('change', {id: "second_nurse_list_thursday2",day: 3, shift: 1, week: 0, rule: 1},updateShift);
	$('#third_nurse_list_thursday2').bind('change', {id: "third_nurse_list_thursday2",day: 3, shift: 1, week: 0, rule: 2},updateShift);
	$('#stand_by_list_thursday2').bind('change', {id: "stand_by_list_thursday2",day: 3, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign friday morning
	$('#head_nurse_list_friday2').bind('change', {id: "head_nurse_list_friday2",day: 4, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_friday2').bind('change', {id: "second_nurse_list_friday2",day: 4, shift: 1, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday2').bind('change', {id: "stand_by_nurse_list_friday2",day: 4, shift: 1, week: 0, rule: 3},updateShift);
	
	//assign saturday morning
	$('#head_nurse_list_saturday2').bind('change', {id: "head_nurse_list_saturday2",day: 5, shift: 1, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_saturday2').bind('change', {id: "second_nurse_list_saturday2",day: 5, shift: 1, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday2').bind('change', {id: "stand_by_nurse_list_saturday2",day: 5, shift: 1, week: 0, rule: 3},updateShift);
	
	
	
	
	//assign sunday evening
	$('#head_nurse_list_sunday3').bind('change', {id: "head_nurse_list_sunday3",day: 6, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_sunday3').bind('change', {id: "second_nurse_list_sunday3",day: 6, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_list_sunday3').bind('change', {id: "stand_by_list_sunday3",day: 6, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign monday evening
	$('#head_nurse_list_monday3').bind('change', {id: "head_nurse_list_monday3",day: 0, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_monday3').bind('change', {id: "second_nurse_list_monday3",day: 0, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_monday3').bind('change', {id: "stand_by_nurse_list_monday3",day: 0, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign tuesday evening
	$('#head_nurse_list_tuesday3').bind('change', {id: "head_nurse_list_tuesday3",day: 1, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_tuesday3').bind('change', {id: "second_nurse_list_tuesday3",day: 1, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_tuesday3').bind('change', {id: "stand_by_nurse_list_tuesday3",day: 1, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign wednesday evening
	$('#head_nurse_list_wednesday3').bind('change', {id: "head_nurse_list_wednesday3",day: 2, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_wednesday3').bind('change', {id: "second_nurse_list_wednesday3",day: 2, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_list_wednesday3').bind('change', {id: "stand_by_list_wednesday3",day: 2, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign thursday evening
	$('#head_nurse_list_thursday3').bind('change', {id: "head_nurse_list_thursday3",day: 3, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_thursday3').bind('change', {id: "second_nurse_list_thursday3",day: 3, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_thursday3').bind('change', {id: "stand_by_nurse_thursday3",day: 3, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign friday evening
	$('#head_nurse_list_friday3').bind('change', {id: "head_nurse_list_friday3",day: 4, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_friday3').bind('change', {id: "second_nurse_list_friday3",day: 4, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday3').bind('change', {id: "stand_by_nurse_list_friday3",day: 4, shift: 2, week: 0, rule: 3},updateShift);
	
	//assign saturday evening
	$('#head_nurse_list_saturday3').bind('change', {id: "head_nurse_list_saturday3",day: 5, shift: 2, week: 0, rule: 0},updateShift);
	$('#second_nurse_list_saturday3').bind('change', {id: "second_nurse_list_saturday3",day: 5, shift: 2, week: 0, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday3').bind('change', {id: "stand_by_nurse_list_saturday3",day: 5, shift: 2, week: 0, rule: 3},updateShift);
	
	
	
	
	////////////////////////////////second week//////////////////////////////////////////////////
	
	
	//assign sunday night
	$('#head_nurse_list_sunday4').bind('change', {id: "head_nurse_list_sunday4",day: 6, shift: 0, week: 1, rule: 0},updateShift);
    $('#second_nurse_list_sunday4').bind('change', {id: "second_nurse_list_sunday4",day: 6, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_list_sunday4').bind('change', {id: "stand_by_list_sunday4",day: 6, shift: 0, week: 1, rule: 3},updateShift);
	
	//assign monday night
	$('#head_nurse_list_monday4').bind('change', {id: "head_nurse_list_monday4",day: 0, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_monday4').bind('change', {id: "second_nurse_list_monday4",day: 0, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_list_monday4').bind('change', {id: "stand_by_list_monday4",day: 0, shift: 0, week: 1, rule: 3},updateShift);
	
	//assign tuesday night
	$('#head_nurse_list_tuesday4').bind('change', {id: "head_nurse_list_tuesday4",day: 1, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_tuesday4').bind('change', {id: "second_nurse_list_tuesday4",day: 1, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_tuesday4').bind('change', {id: "stand_by_nurse_list_tuesday4",day: 1, shift: 0, week: 1, rule: 3},updateShift);
	
	//assign wednesday night
	$('#head_nurse_list_wednesday4').bind('change', {id: "stand_by_nurse_list_tuesday4",day: 2, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_wednesday4').bind('change', {id: "second_nurse_list_wednesday4",day: 2, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_wednesday4').bind('change', {id: "stand_by_nurse_list_wednesday4",day: 2, shift: 0, week: 1, rule: 3},updateShift);
	
	//assign thursday night
	$('#head_nurse_list_thursday4').bind('change', {id: "head_nurse_list_thursday4",day: 3, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_thursday4').bind('change', {id: "second_nurse_list_thursday4",day: 3, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_thursday4').bind('change', {id: "stand_by_nurse_list_thursday4",day: 3, shift: 0, week: 1, rule: 3},updateShift);
	
	//assign friday night
	$('#head_nurse_list_friday4').bind('change', {id: "head_nurse_list_friday4",day: 4, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_friday4').bind('change', {id: "second_nurse_list_friday4",day: 4, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday4').bind('change', {id: "stand_by_nurse_list_friday4",day: 4, shift: 0, week: 1, rule: 2},updateShift);
	
	//assign saturday night
	$('#head_nurse_list_saturday4').bind('change', {id: "head_nurse_list_saturday4",day: 5, shift: 0, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_saturday4').bind('change', {id: "second_nurse_list_saturday4",day: 5, shift: 0, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday4').bind('change', {id: "stand_by_nurse_list_saturday4",day: 5, shift: 0, week: 1, rule: 3},updateShift);
	
	
	
	
	
	//assign sunday morning
	$('#head_nurse_list_sunday5').bind('change', {id: "head_nurse_list_sunday5",day: 6, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_sunday5').bind('change', {id: "second_nurse_list_sunday5",day: 6, shift: 1, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_sunday5').bind('change', {id: "stand_by_nurse_list_sunday5",day: 6, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign monday morning
	$('#head_nurse_list_monday5').bind('change', {id: "head_nurse_list_monday5",day: 0, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_monday5').bind('change', {id: "second_nurse_list_monday5",day: 0, shift: 1, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_monday5').bind('change', {id: "stand_by_nurse_list_monday5",day: 0, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign tuesday morning
	$('#head_nurse_list_tuesday5').bind('change', {id: "head_nurse_list_tuesday5",day: 1, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_tuesday5').bind('change', {id: "second_nurse_list_tuesday5",day: 1, shift: 1, week: 1, rule: 1},updateShift);
	$('#third_nurse_list_tuesday5').bind('change', {id: "third_nurse_list_tuesday5",day: 1, shift: 1, week: 1, rule: 2},updateShift);
	$('#stand_by_nurse_tuesday5').bind('change', {id: "stand_by_nurse_tuesday5",day: 1, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign wednesday morning
	$('#head_nurse_list_wednesday5').bind('change', {id: "head_nurse_list_wednesday5",day: 2, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_wednesday5').bind('change', {id: "second_nurse_list_wednesday5",day: 2, shift: 1, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_wednesday5').bind('change', {id: "stand_by_nurse_list_wednesday5",day: 2, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign thursday morning
	$('#head_nurse_list_thursday5').bind('change', {id: "head_nurse_list_thursday5",day: 3, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_thursday5').bind('change', {id: "second_nurse_list_thursday5",day: 3, shift: 1, week: 1, rule: 1},updateShift);
	$('#third_nurse_list_thursday5').bind('change', {id: "third_nurse_list_thursday5",day: 3, shift: 1, week: 1, rule: 2},updateShift);
	$('#stand_by_list_thursday5').bind('change', {id: "stand_by_list_thursday5",day: 3, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign friday morning
	$('#head_nurse_list_friday5').bind('change', {id: "head_nurse_list_friday5",day: 4, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_friday5').bind('change', {id: "second_nurse_list_friday5",day: 4, shift: 1, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday5').bind('change', {id: "stand_by_nurse_list_friday5",day: 4, shift: 1, week: 1, rule: 3},updateShift);
	
	//assign saturday morning
	$('#head_nurse_list_saturday5').bind('change', {id: "head_nurse_list_saturday5",day: 5, shift: 1, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_saturday5').bind('change', {id: "second_nurse_list_saturday5",day: 5, shift: 1, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday5').bind('change', {id: "stand_by_nurse_list_saturday5",day: 5, shift: 1, week: 1, rule: 3},updateShift);
	
	
	
	
	//assign sunday evening
	$('#head_nurse_list_sunday6').bind('change', {id: "head_nurse_list_sunday6",day: 6, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_sunday6').bind('change', {id: "second_nurse_list_sunday6",day: 6, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_list_sunday6').bind('change', {id: "stand_by_list_sunday6",day: 6, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign monday evening
	$('#head_nurse_list_monday6').bind('change', {id: "head_nurse_list_monday6",day: 0, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_monday6').bind('change', {id: "second_nurse_list_monday6",day: 0, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_monday6').bind('change', {id: "stand_by_nurse_list_monday6",day: 0, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign tuesday evening
	$('#head_nurse_list_tuesday6').bind('change', {id: "head_nurse_list_tuesday6",day: 1, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_tuesday6').bind('change', {id: "second_nurse_list_tuesday6",day: 1, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_tuesday6').bind('change', {id: "stand_by_nurse_list_tuesday6",day: 1, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign wednesday evening
	$('#head_nurse_list_wednesday6').bind('change', {id: "head_nurse_list_wednesday6",day: 2, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_wednesday6').bind('change', {id: "second_nurse_list_wednesday6",day: 2, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_list_wednesday6').bind('change', {id: "stand_by_list_wednesday6",day: 2, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign thursday evening
	$('#head_nurse_list_thursday6').bind('change', {id: "head_nurse_list_thursday6",day: 3, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_thursday6').bind('change', {id: "second_nurse_list_thursday6",day: 3, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_thursday6').bind('change', {id: "stand_by_nurse_thursday6",day: 3, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign friday evening
	$('#head_nurse_list_friday6').bind('change', {id: "head_nurse_list_friday6",day: 4, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_friday6').bind('change', {id: "second_nurse_list_friday6",day: 4, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_friday6').bind('change', {id: "stand_by_nurse_list_friday6",day: 4, shift: 2, week: 1, rule: 3},updateShift);
	
	//assign saturday evening
	$('#head_nurse_list_saturday6').bind('change', {id: "head_nurse_list_saturday6",day: 5, shift: 2, week: 1, rule: 0},updateShift);
	$('#second_nurse_list_saturday6').bind('change', {id: "second_nurse_list_saturday6",day: 5, shift: 2, week: 1, rule: 1},updateShift);
	$('#stand_by_nurse_list_saturday6').bind('change', {id: "stand_by_nurse_list_saturday6",day: 5, shift: 2, week: 1, rule: 3},updateShift);
	

	

});

function updateShift(event)
{
	var selectedNurse = document.getElementById(event.data.id);
	if(selectedNurse == -1)
	{
		return null;
	}
	
	var selectedNurse_userName = selectedNurse.options[selectedNurse.selectedIndex].text
	//alert(selectedNurse_userName);
	
	$.ajax({
		url:'/saveSchedule',
		type:'GET',
		dataType:'json',
        data:{selectedNurse_userName: selectedNurse_userName, day: event.data.day, shift: event.data.shift, week: event.data.week, rule:event.data.rule},
		success:function(data, status, xhr) {
			if(data.note != null)
				alert(data.note);
			alert("Success");
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
	
	
}
function save_Schedule()
{
	var head_nurse_list_sunday1 = document.getElementById('head_nurse_list_sunday1');
	var second_nurse_list_sunday1 = document.getElementById('second_nurse_list_sunday1');
	var stand_by_list_sunday1 = document.getElementById('stand_by_list_sunday1');
	
	var head_nurse_list_monday1 = document.getElementById('head_nurse_list_monday1');
	var second_nurse_list_monday1 = document.getElementById('second_nurse_list_monday1');
	var stand_by_list_monday1 = document.getElementById('stand_by_list_monday1');
	
    if (head_nurse_list_sunday1.selectedIndex == -1 || second_nurse_list_sunday1 == -1 || stand_by_list_sunday1 == -1
		|| head_nurse_list_monday1.selectedIndex == -1 || second_nurse_list_monday1 == -1 || stand_by_list_monday1 == -1)
	{
		alert("empty fields");
        return null;
	}
	
    var head_nurse_list_sunday1_userName = head_nurse_list_sunday1.options[head_nurse_list_sunday1.selectedIndex].text
	var second_nurse_list_sunday1_userName = second_nurse_list_sunday1.options[second_nurse_list_sunday1.selectedIndex].text
	var stand_by_list_sunday1_userName = stand_by_list_sunday1.options[stand_by_list_sunday1.selectedIndex].text
	
	var head_nurse_list_monday1_userName = head_nurse_list_monday1.options[head_nurse_list_monday1.selectedIndex].text
	var second_nurse_list_monday1_userName = second_nurse_list_monday1.options[second_nurse_list_monday1.selectedIndex].text
	var stand_by_list_monday1_userName = stand_by_list_monday1.options[stand_by_list_monday1.selectedIndex].text 
	alert(stand_by_list_monday1_userName);
	$.ajax({
		url:'/saveSchedule',
		type:'GET',
		dataType:'json',
        data:{head_nurse_list_sunday1_userName: head_nurse_list_sunday1_userName, second_nurse_list_sunday1_userName: second_nurse_list_sunday1_userName, stand_by_list_sunday1_userName: stand_by_list_sunday1_userName,
			head_nurse_list_monday1_userName: head_nurse_list_monday1_userName, second_nurse_list_monday1_userName: second_nurse_list_monday1_userName, stand_by_list_monday1_userName: stand_by_list_monday1_userName},
		success:function(data, status, xhr) {
			document.location.href = '/MainManager';
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

function submit_Schedule()
{
	$.ajax({
		url:'/submitSchedule',
		type:'GET',
		dataType:'json',
		data:{},
		success:function(data, status, xhr) {
			
			$('#form_spinner').removeClass('hidden'); //we show the spinner when we're about to submit
			//we simulate form submition with a simple timeout
			setTimeout(function() {
				$('#form_spinner').addClass('hidden');
			}, 50000);
			
			document.location.href = '/MainManager';
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
		}
	});
}

$(document).ready(function(){
	$.ajax({
		url:'/deadLines',
		type:'GET',
		dataType:'json',
		data:{},
		success:function(data, status, xhr) {
			if(data.isSubmitingDates == true)
			{
				document.getElementById("submit").setAttribute("disabled", "enabled"); 
			}
			else
			{
				document.getElementById("submit").setAttribute("disabled", "disabled"); 
			}
		},
		error:function(xhr, status, error) {
			alert("failed!");
            alert(xhr.responseText);
		}
	});
});

$body = $("body");

$(document).on({
    ajaxStart: function() { $body.addClass("loading");    },
     ajaxStop: function() { $body.removeClass("loading"); }    
});