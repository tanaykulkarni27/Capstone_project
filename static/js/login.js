function sendLogin(){
	var u_name = document.getElementById('username').value;
	var password = document.getElementById('password').value;
	if(u_name.length <= 0){
		alert("username cannot be empty");
		return;
	}
	if(password.length <= 0){
		alert("password cannot be empty");
		return;
	}
	$.ajax({
		type : "POST",
		url  : "http://localhost:8000/login",
		data : {
			"username" : u_name,
			"password" : password,
		},
		beforeSend:function(){
			alert("GOing to send request");
			// $("#buffer").show();
		},
		success : function(e){
			$("#buffer").hide();
			if(e == "done"){
				window.location.replace("http://localhost:8000/");
				
			}
			else{
				alert(e);
			}
		}
	});
}
