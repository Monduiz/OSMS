var ctx = document.getElementById('myChart').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');
var ctx3 = document.getElementById('myChart3').getContext('2d');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: Object.keys(data),
      datasets: [{
        data: Object.values(data),
        backgroundColor: "#FF9500"
      }]
    },
    options: {
        responsive: true,
        legend: {
            display: false
         },
        scales: {
            xAxes : [{
            barThickness: 50,
            gridLines : {
                display : false
              }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                display:false
                }
            }]
        }
    }
});

var myChart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: Object.keys(data_legislation),
      datasets: [{
        data: Object.values(data_legislation),
        backgroundColor: "#FF9500"
      }]
    },
    options: {
        responsive: true,
        legend: {
            display: false
         },
        scales: {
            xAxes : [{
            barThickness: 50,
            gridLines : {
                display : false
              }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                display:false
                }
            }]
        }
    }
});

var myChart3 = new Chart(ctx3, {
    type: 'bar',
    data: {
      labels: Object.keys(data_criminal),
      datasets: [{
        data: Object.values(data_criminal),
        backgroundColor: "#FF9500"
      }]
    },
    options: {
        responsive: true,
        legend: {
            display: false
         },
        scales: {
            xAxes : [{
            barThickness: 50,
            gridLines : {
                display : false
              }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                display:false
                }
            }]
        }
    }
});

mapboxgl.accessToken = 'pk.eyJ1IjoibW9uZHVpeiIsImEiOiJHaFBXVWRjIn0.1LiUo_YLK8Csro24VrFJlA';
var map = new mapboxgl.Map({
container: 'map',
center: [-95, 58],
zoom: 2,
style: 'mapbox://styles/mapbox/light-v10'
});

map.addControl(new mapboxgl.NavigationControl());

map.on('load', function() {
map.addLayer({
    'id': 'locations',
    'type': 'circle',
    'source': {
      'type': 'geojson',
      'data': trip_loc
    },
    'paint': {
      'circle-radius': {
      'base': 1.75,
      'stops': [[12, 5], [22, 180]]
      },
      'circle-color': '#FF9500'
    }
});

var bounds = new mapboxgl.LngLatBounds();

trip_loc.features.forEach(function(feature) {
    bounds.extend(feature.geometry.coordinates);
});

map.fitBounds(bounds, {
padding: 10
});

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
    '<h5>' + currentFeature.properties.province + '</h5>')
  .addTo(map);
}

map.on('click', function(e) {
// Query all the rendered points in the view
var features = map.queryRenderedFeatures(e.point, { layers: ['locations'] });
if (features.length) {
  var clickedPoint = features[0];
  // 1. Fly to the point
  flyToLocation(clickedPoint);
  // 2. Close all other popups and display popup for clicked store
  createPopUp(clickedPoint);
}
});
