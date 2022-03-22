function f(ll){
	var base_url = window.location.origin;
	// alert(base_url + ll);
	var myImg = document.getElementById('ss');
	var currHeight = myImg.clientHeight;
	document.getElementById("x").style.backgroundImage = "url("+base_url + ll +")";
}