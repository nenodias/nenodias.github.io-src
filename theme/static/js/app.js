$(document).ready(function(){
	$('.share-link').each(function(idx,obj){
		var link = $(obj).attr('href');
		link = link.replace("#SITEPROD#",SITEPROD);
		$(obj).attr('href', link);
	});
});
