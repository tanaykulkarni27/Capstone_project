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