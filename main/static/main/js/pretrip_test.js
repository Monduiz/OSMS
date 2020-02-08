// Stepper
// var stepper = new Stepper(document.querySelector('#stepper'), {
//  linear: false,
//  animation: true
//});


// Algolia places

(function() {
  var placesAutocomplete = places({
    appId: 'plA553AD2SN2',
    apiKey: '56fe5a0b082b62d646cf971bbcf5df96',
    container: document.querySelector('#form-address'),
    templates: {
      value: function(suggestion) {
        return suggestion.name;
      }
    }
  }).configure({
    type: 'address',
    language: 'en',
    countries: ['ca'],
    aroundLatLngViaIP: false
  });
  placesAutocomplete.on('change', function resultSelected(e) {
    document.querySelector('#form-address2').value = e.suggestion.name || '';
    document.querySelector('#form-city').value = e.suggestion.city || '';
    document.querySelector('#form-province').value = e.suggestion.administrative || '';
    document.querySelector('#form-pc').value = e.suggestion.postcode || '';
    document.querySelector('#form-lat').value = e.suggestion.latlng.lat || '';
    document.querySelector('#form-lng').value = e.suggestion.latlng.lng || '';
  });
 })();

 // Material Select Initialization
 $(document).ready(function() {
 $('.mdb-select').materialSelect();
 });


 // Datepicker
var from_input = $('#startingDate').pickadate({
  format: 'yyyy/mm/dd',
  formatSubmit: 'yyyy/mm/dd'
}),
from_picker = from_input.pickadate('picker')
var to_input = $('#endingDate').pickadate({
  format: 'yyyy/mm/dd',
  formatSubmit: 'yyyy/mm/dd'
}),
to_picker = to_input.pickadate('picker')

// Check if there’s a “from” or “to” date to start with and if so, set their appropriate properties.
if ( from_picker.get('value') ) {
to_picker.set('min', from_picker.get('select'))
}
if ( to_picker.get('value') ) {
from_picker.set('max', to_picker.get('select'))
}

// Apply event listeners in case of setting new “from” / “to” limits to have them update on the other end. If ‘clear’ button is pressed, reset the value.
from_picker.on('set', function(event) {
if ( event.select ) {
to_picker.set('min', from_picker.get('select'))
}
else if ( 'clear' in event ) {
to_picker.set('min', false)
}
})
to_picker.on('set', function(event) {
if ( event.select ) {
from_picker.set('max', to_picker.get('select'))
}
else if ( 'clear' in event ) {
from_picker.set('max', false)
}
})
