function f(){
			console.log();
			var myImg = document.getElementById('ss');
			var currHeight = myImg.clientHeight;
			document.getElementById("x").style.height = (currHeight + 100)+"px";
			// document.getElementById("x").style.backgroundImage = "url(" + 'http:localhost:8000/' + img_location + ")";
			document.getElementById("mask").style.height = (currHeight + 100)+"px";
		}