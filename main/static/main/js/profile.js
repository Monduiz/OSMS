

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
