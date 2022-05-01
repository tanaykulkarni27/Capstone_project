var xreq = null;
var cur_window = null;
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
function Listen_book(book_id,book_loc){
	
	var ll = document.getElementById('stop_listening');
	ll.style.display = '';
	ll = document.getElementById('start_listening');
	ll.style.display = 'none';
	xreq = $.ajax({
				type : "GET",
				url : "/listen/"+book_id,
				beforeSend:function (){
					cur_window = window.open(book_loc);
				},
				success:function(data){
					// alert('book finished');
				}
			});
}
function stop_listening_book(){
	cur_window.close();
	var ll = document.getElementById('stop_listening');
	ll.style.display = 'none';
	ll = document.getElementById('start_listening');
	ll.style.display = '';
	xreq.abort();
	$.ajax({
				type : "GET",
				url : "/pause",
				success:function(data){
				}
			});
}