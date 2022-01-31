function validate() {
	if(document.getElementById('lang').options[document.getElementById('lang').selectedIndex ].value == "NULL")
		return false;
	if(document.getElementById('cat').options[document.getElementById('cat').selectedIndex ].value == "NULL")
			return false;		
	var val = document.getElementById('bookfile').value.toLowerCase();
	var regex = new RegExp("(.*?)\.(pdf)$");
		if(!(regex.test(val))) {
			document.getElementById('bookfile').value = '';
			alert('Please select correct file format.');
			return false;   
		}
	 val = document.getElementById('bookimg').value.toLowerCase();
	 var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
	if(!(allowedExtensions.exec(val))) {
		document.getElementById('bookimg').value = '';
		alert('Please select correct file format.');
		return false;   
	}		
		return true;
}
$(document).ready(function(){
	$("#submit").click(function(){
		var x = validate();
		if(x){
			var form_data = new FormData();
			form_data.append("bookname" , document.getElementById('name').value);
			form_data.append("bookdesc" , document.getElementById('desc').value,);
			form_data.append("booklang" , document.getElementById('lang').options[document.getElementById('lang').selectedIndex ].value);
			form_data.append("category" , document.getElementById('cat').options[document.getElementById('cat').selectedIndex ].value);
			form_data.append("bookimg" , document.getElementById('bookimg').files[0]);
			form_data.append("bookfile" , document.getElementById('bookfile').files[0]);
			$.ajax({
				type:"POST",
				url : "http://localhost:8000/Pupload",
				enctype: 'multipart/form-data',
				processData: false,
				contentType: false,
				data : form_data,
				beforeSend:function(){
					$("#buffer").show();
				},
				success:function(){
					$("#buffer").hide();
					window.location.replace("http://localhost:8000/");
				}
			});
		}
	});
});