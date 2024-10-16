$(document).ready(function () {
    // Initially hide the second container
    // $("#second").hide();
    $("#result").hide();
    var dataMaths=[]
    var dataReading=[]
    var dataWriting=[]
    // Click event for the first submit button
    $("#firstbtn").click(function () {
        // Hide the first container

        var gen = document.getElementById('gender').value;
        var parent = document.getElementById('parentEducation').value;
        var race = document.getElementById('race').value;
        // gen='male';
        // parent="associate's degree ";
        // race='group D';
        if (!gen || !parent || !race ) {
            alert('Please select values for all input fields.');
            return;
        }
        $("#first").hide();
        // Show the second container
        $("#second").show();
        $.ajax({
            type: "GET",
            url: "/plan",
            contentType:"application/json;charset=UTF-8",
            data: {
                "gender": gen,
                "parentEducation": parent,
                'race':race
            },
            dataType: "json",
            success: function (data) {
                // $("#second").html(data);

                    dataMaths[0] = data.freec.map(row => row[0]);
                    dataMaths[1] = data.freen.map(row => row[0]);
                    dataMaths[2] = data.standc.map(row => row[0]);
                    dataMaths[3] = data.standn.map(row => row[0]);

                    dataReading[0] = data.freec.map(row => row[1]);
                    dataReading[1] = data.freen.map(row => row[1]);
                    dataReading[2] = data.standc.map(row => row[1]);
                    dataReading[3] = data.standn.map(row => row[1]);

                    dataWriting[0] = data.freec.map(row => row[2]);
                    dataWriting[1] = data.freen.map(row => row[2]);
                    dataWriting[2] = data.standc.map(row => row[2]);
                    dataWriting[3] = data.standn.map(row => row[2]);
                
                console.log(data);
            },
            failure: function(data){
                alert('Data Saving Failed',data);
            }
        });
    });

    // Click event for the second submit button
    $("#secondsub").click(function () {
        // Hide the second container
        let lunch = document.getElementById('lunch').value;
        let testPrep = document.getElementById('testPrep').value;
        let binary=0;
        if (!lunch || !testPrep ) {
            alert('Please select values for all input fields.');
            return;
        }
        binary=lunch*2**0+testPrep*2**1;
        console.log(binary);
        let mathsavg=0;
        let readingavg=0;
        let writingavg=0;
        mathsavg = (dataMaths[binary].reduce((sum, value) => sum + value, 0) / dataMaths[binary].length).toFixed(2);
        console.log(mathsavg);
        readingavg = (dataReading[binary].reduce((sum, value) => sum + value, 0) / dataReading[binary].length).toFixed(2);
        console.log(readingavg);
        writingavg = (dataWriting[binary].reduce((sum, value) => sum + value, 0) / dataWriting[binary].length).toFixed(2);
        console.log(writingavg);

        if (isNaN(mathsavg)) {
            mathsavg = 'Data not available';
        }
        if (isNaN(readingavg)) {
            readingavg = 'Data not available';
        }
        if (isNaN(writingavg)) {
            writingavg = 'Data not available';
        }

        $("#result").show();

        $("#result").html(`<p>Math Average: ${mathsavg}%</p><br><p>Reading Average: ${readingavg}%</p><br><p>Writing Average: ${writingavg}%</p>`);


    });

    // Click event for the "Go back" button in the second container
    $("#secondgo").click(function () {
        // Hide the second container
        $("#second").hide();

        // Show the first container
        $("#first").show();
    });
});
