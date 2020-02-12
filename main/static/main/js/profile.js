// Use HTML5 localStorage object to save some parameter for the current tab
// locally in the browser. Allow to keep current tab active on page reload

// $(document).ready(function(){
// 	$('a[data-toggle="pill"]').on('show.bs.tab', function(e) {
// 		localStorage.setItem('activeTab', $(e.target).attr('href'));
// 	});
// 	var activeTab = localStorage.getItem('activeTab');
// 	if(activeTab){
// 		$('#pills-tab a[href="' + activeTab + '"]').tab('show');
// 	}
// });

// Phone number formatting

new Cleave('#id_phone', {
    numericOnly: true,
    blocks: [0, 3, 0, 3, 4],
    delimiters: ["(", ")", " ", "-"]
});

// Material Select Initialization
$(document).ready(function() {
$('.mdb-select').materialSelect();
});
