$(document).ready(function(){
    $("#search").keyup(function(){

        var filter = $(this).val(), count = 0;

        // Loop through the comment list
        $(".item").each(function(){

            // If the list item does not contain the text phrase fade it out
            if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).fadeOut();

            // Show the list item if the phrase matches and increase the count by 1
            } else {
                $(this).show();
                count++;
            }
        });

    });
});


if (!('remove' in Element.prototype)) {
  Element.prototype.remove = function() {
    if (this.parentNode) {
      this.parentNode.removeChild(this);
    }
  };
}

mapboxgl.accessToken = mapbox_token;
var map = new mapboxgl.Map({
container: 'map',
center: [-95, 58],
zoom: 3,
style: 'mapbox://styles/mapbox/light-v10'
});

map.addControl(new mapboxgl.NavigationControl());

map.on('load', function() {
map.addLayer({
    'id': 'locations',
    'type': 'circle',
    'source': {
      'type': 'geojson',
      'data': data
    },
    'paint': {
      'circle-radius': {
      'base': 1.75,
      'stops': [[12, 5], [22, 180]]
      },
      'circle-color': '#2ABBBD'
    }
});
buildLocationList(data);
});

// Add an event listener for when a user clicks on the map
map.on('click', function(e) {
// Query all the rendered points in the view
var features = map.queryRenderedFeatures(e.point, { layers: ['locations'] });
if (features.length) {
  var clickedPoint = features[0];
  // 1. Fly to the point
  flyToLocation(clickedPoint);
  // 2. Close all other popups and display popup for clicked store
  createPopUp(clickedPoint);
  // 3. Highlight listing in sidebar (and remove highlight for all other listings)
  var activeItem = document.getElementsByClassName('active');
  if (activeItem[0]) {
    activeItem[0].classList.remove('active');
  }
  // Find the index of the location.features that corresponds to the clickedPoint that fired the event listener
  var selectedFeature = clickedPoint.properties.address;

  for (var i = 0; i < data.features.length; i++) {
    if (data.features[i].properties.address === selectedFeature) {
      selectedFeatureIndex = i;
    }
  }
  // Select the correct list item using the found index and add the active class
  var listing = document.getElementById('listing-' + selectedFeatureIndex);
  listing.classList.add('active');
}
});

function flyToLocation(currentFeature) {
map.flyTo({
  center: currentFeature.geometry.coordinates,
  zoom: 15,
  speed: 2
});
}

function createPopUp(currentFeature) {
var popUps = document.getElementsByClassName('mapboxgl-popup');
// Check if there is already a popup on the map and if so, remove it
if (popUps[0]) popUps[0].remove();

var popup = new mapboxgl.Popup({ closeOnClick: true })
  .setLngLat(currentFeature.geometry.coordinates)
  .setHTML('<h3>' + currentFeature.properties.city + '</h3>' +
    '<h5>' + currentFeature.properties.address + '</h5>' +
    '<h5>' + currentFeature.properties.postal_code + '</h5>')
  .addTo(map);
}


function buildLocationList(data) {
// Iterate through the list of locations
for (i = 0; i < data.features.length; i++) {
  var currentFeature = data.features[i];
  // Shorten data.feature.properties to `prop` so we're not
  // writing this long form over and over again.
  var prop = currentFeature.properties;
  // Select the listing container in the HTML and append a div
  // with the class 'item' for each location
  var listings = document.getElementById('listings');
  var listing = listings.appendChild(document.createElement('div'));
  listing.className = 'item';
  listing.id = 'listing-' + i;

  // Create a new link with the class 'title' for each location
  // and fill it with the location address
  var link = listing.appendChild(document.createElement('a'));
  link.href = '#';
  link.className = 'region';
  link.dataPosition = i;
  link.innerHTML = prop.city;

  // Create a new div with the class 'details' for each location
  // and fill it with the city and phone number
  var details = listing.appendChild(document.createElement('div'));
  details.innerHTML = prop.address;

  // Add an event listener for the links in the sidebar listing
  link.addEventListener('click', function(e) {
    // Update the currentFeature to the store associated with the clicked link
    var clickedListing = data.features[this.dataPosition];
    // 1. Fly to the point associated with the clicked link
    flyToLocation(clickedListing);
    // 2. Close all other popups and display popup for clicked store
    createPopUp(clickedListing);
    // 3. Highlight listing in sidebar (and remove highlight for all other listings)
    var activeItem = document.getElementsByClassName('active');
    if (activeItem[0]) {
      activeItem[0].classList.remove('active');
    }
    this.parentNode.classList.add('active');
  });
}
}


function myFunction() {
// Declare variables
var input, filter, ul, li, a, i;
input = document.getElementById("search");
filter = input.value.toUpperCase();
ul = document.getElementById("listings");
li = ul.getElementsByTagName("region");

// Loop through all list items, and hide those who don't match the search query
for (i = 0; i < li.length; i++) {
  a = li[i].getElementsByTagName("a")[0];
  if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
    li[i].style.display = "";
  } else {
    li[i].style.display = "none";
  }
}
}
