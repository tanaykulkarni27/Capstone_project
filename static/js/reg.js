function validate() { return document.getElementById('pwd').value == document.getElementById('pwd2').value; }
function sbt(){
	var x = validate();
	if(x){
		var form_data = new FormData();
		form_data.append("FNAME" , document.getElementById('FNAME').value);
		form_data.append("USNAME" , document.getElementById('USNAME').value);
		form_data.append("LNAME" , document.getElementById('LNAME').value);
		form_data.append("EMAIL" , document.getElementById('EMAIL').value);
		form_data.append("PWD" , document.getElementById('pwd').value);
		$.ajax({
			type:"POST",
			url : "/getin",
			enctype: 'multipart/form-data',
			processData: false,
			contentType: false,
			data : form_data,
			beforeSend:function(){
				$("#buffer").show();
			},
			success:function(){
				$("#buffer").hide();
				window.location.replace("/");
			}
		});
	}
}