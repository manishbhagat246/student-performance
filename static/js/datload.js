
$("#btn_cleardata").click(function(){
	var form_data = new FormData($('#upload-file')[0]);
	debugger;
	 $.ajax({
            type: 'POST',
            url: '/cleardataset',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Dataset has been cleared');
                $('#upload-file')[0].reset();
            },
            // error: function(xhr, textStatus, errorThrown) {
            //     console.error('Error:', textStatus);
            //     console.log('XHR:', xhr);
            // }
        });
        });

$("#btn_loaddata").click(function(){
	var form_data = new FormData($('#upload-file')[0]);
	debugger;
	 $.ajax({
            type: 'POST',
            url: '/savedataset',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Dataset has been loaded');
                $('#upload-file')[0].reset();
            },
            // error: function(error) {
            //     console.error('Error:', error);
            //  }
        });
});

