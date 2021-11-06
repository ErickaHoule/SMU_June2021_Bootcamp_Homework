
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

// Requsts to URL
d3.json(queryUrl, function(data) {
  createFeatures(data.features);
  console.log(data.features)
});

function createFeatures(earthquakeData) {

  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
  }

  // Circle Size
  function radiusSize(magnitude) {
    return magnitude * 26000;
  }

  // Circle color by magnitude
  function circleColor(magnitude) {
    if (magnitude < 1) {
      return "#EBC6C1"
    }
    else if (magnitude < 2) {
      return "#EAAFAE"
    }
    else if (magnitude < 3) {
      return "#E58B8B"
    }
    else if (magnitude < 4) {
      return "#DF6A68"
    }
    else if (magnitude < 5) {
      return "#CC444B"
    }
    else {
      return "#FAF1F0"
    }
  }

  var earthquakes = L.geoJSON(earthquakeData, {
    pointToLayer: function(earthquakeData, latlng) {
      return L.circle(latlng, {
        radius: radiusSize(earthquakeData.properties.mag),
        color: circleColor(earthquakeData.properties.mag),
        fillOpacity: 1
      });
    },
    onEachFeature: onEachFeature
  });

  // createMap Function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Define outdoormap, satellitemap, and light layers
  var outdoorsmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/outdoors-v11',
    accessToken: API_KEY
  });

  var satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    id: "mapbox.satellite",
    accessToken: API_KEY
  });

  var lightemap =   L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/light-v10',
    accessToken: API_KEY
  });

  // Create the faultline layer
  var faultLine = new L.LayerGroup();

  
  // baseMaps object for saellitemap, light mode and outdoors map
  var baseMaps = {
    "Outdoor Map": outdoorsmap,
    "Light Mode Map": lightemap,
    "Satellite Map": satellitemap
  };

  // Overlay Maps
  var overlayMaps = {
    Earthquakes: earthquakes,
    FaultLines: faultLine
  };

  // create map with layers and center
  var myMap = L.map("map", {
    center: [
      32.75, 30.32
    ],
    zoom: 2,
    layers: [satellitemap, earthquakes, faultLine]
  });

  // layer control
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  // faultline
  var faultlinequery = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json";
  
  d3.json(faultlinequery, function(data) {
    L.geoJSON(data, {
      style: function() {
        return {color: "#ff007f", fillOpacity: 0}
      }
    }).addTo(faultLine)
  })

  // legond colors
  function getColor(m) {
    return m > 5 ? '#CC444B' :
           m > 4  ? '#DF6A68' :
           m > 3  ? '#E58B8B' :
           m > 2  ? '#EAAFAE' :
           m > 1  ? '#EBC6C1' :
                    '#FAF1F0';
  }

  // Add legend
  var legend = L.control({position: 'bottomright'});
  
  legend.onAdd = function (map) {
  
      var div = L.DomUtil.create('div', 'info legend'),
          mags = [0, 1, 2, 3, 4, 5],
          labels = []; 
  
      // legond labels
      for (var i = 0; i < mags.length; i++) {
          div.innerHTML +=
              '<i style="background:' + getColor(mags[i] + 1) + '"></i> ' +
              mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+');
      }
  
      return div;
  };
  
  legend.addTo(myMap);
}