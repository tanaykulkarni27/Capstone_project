// import $ from "jquery";
$(document).ready(function(){
	$("#get_in").click(function(){
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
				$("#buffer").show();
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
	});
});
