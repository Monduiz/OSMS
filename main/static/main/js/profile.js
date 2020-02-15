// Use HTML5 localStorage object to save some parameter for the current tab
// locally in the browser. Allow to keep current tab active on page reload
//
// $(document).ready(function(){
// 	$('a[data-toggle="pill"]').on('show.bs.tab', function(e) {
// 		localStorage.setItem('activeTab', $(e.target).attr('href'));
// 	});
// 	var activeTab = localStorage.getItem('activeTab');
// 	if(activeTab){
// 		$('#pills-tab a[href="' + activeTab + '"]').tab('show');
// 	}
// });


// $(document).ready(function(){
// 	$('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
// 		localStorage.setItem('activeTab', $(e.target).attr('href'));
// 	});
// 	var activeTab = localStorage.getItem('activeTab');
// 	if(activeTab){
// 		$('#pills-tab a[href="' + activeTab + '"]').tab('show');
// 	}
// });

// $(function() {
//   $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
//     history.pushState({}, '', e.target.hash);
//   });
//
//   var hash = document.location.hash;
//   var prefix = "tab_";
//   if (hash) {
//     $('.nav-pills a[href="'+hash.replace(prefix,"")+'"]').tab('show');
//   }
// });
//
var url = window.location.href;
var activeTab = url.substring(url.indexOf("#") + 1);
$("#" + activeTab).addClass("active in");
$('a[href="#'+ activeTab +'"]').tab('show')


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
