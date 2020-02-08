

mapboxgl.accessToken = 'pk.eyJ1IjoibW9uZHVpeiIsImEiOiJHaFBXVWRjIn0.1LiUo_YLK8Csro24VrFJlA';
var map = new mapboxgl.Map({
container: 'map',
center: [long,lat],
zoom: 7,
style: 'mapbox://styles/mapbox/light-v10'
});

map.on('load', function() {
map.addLayer({
    'id': 'locations',
    'type': 'circle',
    'source': {
      'type': 'geojson',
      'data': {
        'type': 'FeatureCollection',
        'features': [
          {
        // feature for Mapbox DC
        'type': 'Feature',
        'geometry': { 'type': 'Point',
        'coordinates': [long,lat]
        }

        }]
      }
      },
    'paint': {
      'circle-radius': {
      'base': 1.75,
      'stops': [[12, 5], [22, 180]]
      },
      'circle-color': '#2ABBBD'
    }
});

});
