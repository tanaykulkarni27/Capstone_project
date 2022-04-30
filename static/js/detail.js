var xreq = null;
function add_book(id) {
	$.ajax({
				type : "GET",
				url : "/savebook/"+id,
				success:function(data){
					location.reload();	
				}
			});
}
function remove_book(id) {
	$.ajax({
				type : "GET",
				url : "/remove/"+id,
				success:function(data){
					location.reload();	
				}
			});
}
function Listen_book(book_id){
	var ll = document.getElementById('stop_listening');
	ll.style.display = '';
	ll = document.getElementById('start_listening');
	ll.style.display = 'none';
	xreq = $.ajax({
				type : "GET",
				url : "/listen/"+book_id,
				success:function(data){
					alert('book finished');
				}
			});
}
function stop_listening_book(){
	var ll = document.getElementById('stop_listening');
	ll.style.display = 'none';
	ll = document.getElementById('start_listening');
	ll.style.display = '';
	xreq.abort();
	$.ajax({
				type : "GET",
				url : "/pause",
				success:function(data){
					alert('book finished');
				}
			});
}