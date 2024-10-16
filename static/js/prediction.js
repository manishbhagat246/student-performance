$(document).ready(function () {
$("#predictbtn").click(function () {
    event.preventDefault(); 
    var gen = document.getElementById('gender').value;
    var parent = document.getElementById('parentEducation').value;
    var race = document.getElementById('race').value;
    var lunch = document.getElementById('lunch').value;
    var test = document.getElementById('testPrep').value;
    if (!gen || !parent || !race || !lunch || !test) {
        alert('Please select values for all input fields.');
        return;
    }
    $.ajax({
        type: 'GET',
        url: '/predict',
		contentType:"application/json;charset=UTF-8",
        data: {
            'gender': gen,
            'parentEducation': parent,
            'race': race,
            'lunch': lunch,
            'testPrep': test
        },
        dataType: "json",
        success: function(result){
            // alert('Data Saved Successfully');
            $("#result").html(
                '<div class="styled-result">Math: ' +
                  result.math_score +"%"+
                  '<br>Reading: ' +
                  result.reading_score+"%" +
                  '<br>Writing: ' +
                  result.writing_score+"%" +
                  '</div>'
              );
              console.log(result);
        },
        
		failure: function(result){
			alert('Data Saving Failed');
		}
    });
});
});