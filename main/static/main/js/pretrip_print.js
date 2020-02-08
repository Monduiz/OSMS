// Testing selections
// $('#id_risk_loc').on('change', function(e){
//    console.log($(e.currentTarget).find(":selected").val())
// })


// Stepper
var stepper = new Stepper(document.querySelector('#stepper'), {
  linear: false,
  animation: true
});

// date picker

$('.datetimepicker').datetimepicker({
  locale: 'en-ca',
  format: 'YYYY-MM-DD',
    icons: {
        time: "fa fa-clock-o",
        date: "fa fa-calendar",
        up: "fa fa-chevron-up",
        down: "fa fa-chevron-down",
        previous: 'fa fa-chevron-left',
        next: 'fa fa-chevron-right',
        today: 'fa fa-screenshot',
        clear: 'fa fa-trash',
        close: 'fa fa-remove'
    }
});



const risk_loc_choices = {
  "":"0", "Urban": "1", "Rural": "1", "Remote": "5", "Isolated": "5", "Marine": "5"
};

const risk_loc_famil = {
  '': '0', 'Known': '1', 'Unfamiliar': '3', 'Unknown': '5', 'Public area': '1'
};

const risk_time_choices = {
  '': '0', 'Daytime (30 min after sunrise)': '1', 'Dusk or Dawn': '3',
  'Night (30 min after sunset)': '5'
};

const risk_weather_choices = {
  "":"0", "Clear": "1", "Mildly inclement": "1", "Severely inclement": "5", "Unknown": "3"
};

const risk_terrain_choices = {
  "":"0", "Dry land": "1", "Mud / Wet lands": "1", "Rivers / Lakes": "5", "Ocean": "5", "Mountains": "5"
};

const risk_comm_choices = {
  "":"0", "Cell / PTT/ Radio": "1", "Satelite": "3", "No comms": "5"
};

const risk_emergency_choices = {
  '':'0', 'Fast (<15 mins)': '1', 'Medium (15-30 mins)': '3', 'Slow (>30 mins)': '5'
};
const risk_distance_choices = {
  '':'0', 'Close': '1', 'Medium':'3', 'Far': '5'
};

const risk_transport_choices = {
  '':'0', 'Low': '1', 'Medium':'3', 'High': '5'
};

const risk_criminal_choices = {
  '':'0', 'No': '1', 'Corporate':'3', 'Violent': '5'
};

const risk_compliance_choices = {
  '':'0', 'No': '1', 'Unknown':'3', 'Yes': '5'
};

const risk_numsub_choices = {
  '':'0', 'One': '3', 'Two or more':'5'
};

const risk_penalty_choices = {
  '':'0', 'Low': '1', 'Medium':'3', 'High':'5'
};

const risk_weapons_choices = {
  '':'0', 'No': '1', 'Unknown':'3', 'Yes':'5'
};

const risk_language_choices = {
  '':'0', 'No': '1', 'Unknown':'3', 'Yes':'5'
};

const risk_histlawaver_choices = {
  '':'0', 'No': '1', 'Unknown':'3', 'Yes':'5'
};


$(function() {
  //Capture fields
  var risk_loc_name =  $('#id_risk_loc');
  var risk_loc_value = $('#id_risk_loc_val');
  var risk_loc_fam =  $('#id_risk_loc_fam');
  var risk_loc_faml_val = $('#id_risk_loc_fam_val');
  var risk_time =  $('#id_risk_time');
  var risk_time_val = $('#id_risk_time_val');
  var risk_weather =  $('#id_risk_weather');
  var risk_weather_val = $('#id_risk_weather_val');
  var risk_terrain =  $('#id_risk_terrain');
  var risk_terrain_val = $('#id_risk_terrain_val');
  var risk_comm =  $('#id_risk_comm');
  var risk_comm_val = $('#id_risk_comm_val');
  var risk_emergency =  $('#id_risk_emergency');
  var risk_emergency_val = $('#id_risk_emergency_val');
  var risk_distance =  $('#id_risk_distance');
  var risk_distance_val = $('#id_risk_distance_val');
  var risk_transport =  $('#id_risk_transport');
  var risk_transport_val = $('#id_risk_transport_val');
  var risk_criminal =  $('#id_risk_criminal');
  var risk_criminal_val = $('#id_risk_criminal_val');
  var risk_compliance =  $('#id_risk_compliance');
  var risk_compliance_val = $('#id_risk_compliance_val');
  var risk_numsub =  $('#id_risk_numsub');
  var risk_numsub_val = $('#id_risk_numsub_val');
  var risk_penalty =  $('#id_risk_penalty');
  var risk_penalty_val = $('#id_risk_penalty_val');
  var risk_weapons =  $('#id_risk_weapons');
  var risk_weapons_val = $('#id_risk_weapons_val');
  var risk_language =  $('#id_risk_language');
  var risk_language_val = $('#id_risk_language_val');
  var risk_histlawaver =  $('#id_risk_histlawaver');
  var risk_histlawaver_val = $('#id_risk_histlawaver_val');


  // call to update on load
  updateRisk();
  updateRiskLocFam();
  updateRiskTime();
  updateRiskWeather();
  updateRiskTerrain();
  updateRiskComm();
  updateRiskEmergency();
  updateRiskDistance();
  updateRiskTransport();
  updateRiskCriminal();
  updateRiskCompliance();
  updateRiskNumsub();
  updateRiskPenalty();
  updateRiskWeapons();
  updateRiskLanguage();
  updateRiskHistLawAver();

  function updateRisk() {
    var data = risk_loc_name.val();
    var r_val = risk_loc_choices[data];

    risk_loc_value.attr('readonly', 'readonly');
    //for normal input
    risk_loc_value.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_loc_value.val( risk_loc_value.val() + r_val );
    risk_loc_value.trigger('change');
  };

  function updateRiskLocFam() {
    var data = risk_loc_fam.val();
    var r_val = risk_loc_famil[data];

    risk_loc_faml_val.attr('readonly', 'readonly');
    //for normal input
    risk_loc_faml_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_loc_faml_val.val( risk_loc_faml_val.val() + r_val );
    risk_loc_faml_val.trigger('change');

  };

  function updateRiskTime() {
    var data = risk_time.val();
    var r_val = risk_time_choices[data];

    risk_time_val.attr('readonly', 'readonly');
    //for normal input
    risk_time_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_time_val.val( risk_time_val.val() + r_val );
    risk_time_val.trigger('change');

  };

  function updateRiskWeather() {
    var data = risk_weather.val();
    var r_val = risk_weather_choices[data];

    risk_weather_val.attr('readonly', 'readonly');
    //for normal input
    risk_weather_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_weather_val.val( risk_weather_val.val() + r_val );
    risk_weather_val.trigger('change');

  };

  function updateRiskTerrain() {
    var data = risk_terrain.val();
    var r_val = risk_terrain_choices[data];

    risk_terrain_val.attr('readonly', 'readonly');
    //for normal input
    risk_terrain_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_terrain_val.val( risk_terrain_val.val() + r_val );
    risk_terrain_val.trigger('change');

  };

  function updateRiskComm() {
    var data = risk_comm.val();
    var r_val = risk_comm_choices[data];

    risk_comm_val.attr('readonly', 'readonly');
    //for normal input
    risk_comm_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_comm_val.val( risk_comm_val.val() + r_val );
    risk_comm_val.trigger('change');

  };

  function updateRiskEmergency() {
    var data = risk_emergency.val();
    var r_val = risk_emergency_choices[data];

    risk_emergency_val.attr('readonly', 'readonly');
    //for normal input
    risk_emergency_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_emergency_val.val( risk_emergency_val.val() + r_val );
    risk_emergency_val.trigger('change');

  };

  function updateRiskDistance() {
    var data = risk_distance.val();
    var r_val = risk_distance_choices[data];

    risk_distance_val.attr('readonly', 'readonly');
    //for normal input
    risk_distance_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_distance_val.val( risk_distance_val.val() + r_val );
    risk_distance_val.trigger('change');
  };

  function updateRiskTransport() {
    var data = risk_transport.val();
    var r_val = risk_transport_choices[data];

    risk_transport_val.attr('readonly', 'readonly');
    //for normal input
    risk_transport_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_transport_val.val( risk_transport_val.val() + r_val );
    risk_transport_val.trigger('change');
  };

  function updateRiskCriminal() {
    var data = risk_criminal.val();
    var r_val = risk_criminal_choices[data];

    risk_criminal_val.attr('readonly', 'readonly');
    //for normal input
    risk_criminal_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_criminal_val.val( risk_criminal_val.val() + r_val );
    risk_criminal_val.trigger('change');
  };

  function updateRiskCompliance() {
    var data = risk_compliance.val();
    var r_val = risk_compliance_choices[data];

    risk_compliance_val.attr('readonly', 'readonly');
    //for normal input
    risk_compliance_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_compliance_val.val( risk_compliance_val.val() + r_val );
    risk_compliance_val.trigger('change');
  };

  function updateRiskNumsub() {
    var data = risk_numsub.val();
    var r_val = risk_numsub_choices[data];

    risk_numsub_val.attr('readonly', 'readonly');
    //for normal input
    risk_numsub_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_numsub_val.val( risk_numsub_val.val() + r_val );
    risk_numsub_val.trigger('change');
  };

  function updateRiskPenalty() {
    var data = risk_penalty.val();
    var r_val = risk_penalty_choices[data];

    risk_penalty_val.attr('readonly', 'readonly');
    //for normal input
    risk_penalty_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_penalty_val.val( risk_penalty_val.val() + r_val );
    risk_penalty_val.trigger('change');
  };

  function updateRiskWeapons() {
    var data = risk_weapons.val();
    var r_val = risk_weapons_choices[data];

    risk_weapons_val.attr('readonly', 'readonly');
    //for normal input
    risk_weapons_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_weapons_val.val( risk_weapons_val.val() + r_val );
    risk_weapons_val.trigger('change');
  };

  function updateRiskLanguage() {
    var data = risk_language.val();
    var r_val = risk_language_choices[data];

    risk_language_val.attr('readonly', 'readonly');
    //for normal input
    risk_language_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_language_val.val( risk_language_val.val() + r_val );
    risk_language_val.trigger('change');
  };

  function updateRiskHistLawAver() {
    var data = risk_histlawaver.val();
    var r_val = risk_histlawaver_choices[data];

    risk_histlawaver_val.attr('readonly', 'readonly');
    //for normal input
    risk_histlawaver_val.val('');
    // for select field

    // Append selected value to field
    // for normal input
    risk_histlawaver_val.val( risk_histlawaver_val.val() + r_val );
    risk_histlawaver_val.trigger('change');
  };

  // event listener to state dropdown change
  risk_loc_name.on('change', function() {
      updateRisk();
  });

  risk_loc_fam.on('change', function() {
      updateRiskLocFam();
  });

  risk_time.on('change', function() {
      updateRiskTime();
  });

  risk_weather.on('change', function() {
      updateRiskWeather();
  });

  risk_terrain.on('change', function() {
      updateRiskTerrain();
  });

  risk_comm.on('change', function() {
      updateRiskComm();
  });

  risk_emergency.on('change', function() {
      updateRiskEmergency();
  });

  risk_distance.on('change', function() {
      updateRiskDistance();
  });

  risk_transport.on('change', function() {
      updateRiskTransport();
  });

  risk_criminal.on('change', function() {
      updateRiskCriminal();
  });

  risk_compliance.on('change', function() {
      updateRiskCompliance();
  });

  risk_numsub.on('change', function() {
      updateRiskNumsub();
  });

  risk_penalty.on('change', function() {
      updateRiskPenalty();
  });

  risk_weapons.on('change', function() {
      updateRiskWeapons();
  });

  risk_language.on('change', function() {
      updateRiskLanguage();
  });

  risk_histlawaver.on('change', function() {
      updateRiskHistLawAver();
  });

});

// Sum risk Score
$('.risk_score').on('change', function() {
  var total = 0;
  $('.risk_score').each(function() {
    total += parseInt($(this).val());
  });
  $('#risk_sum').val(total);

  if (total <= 30) {
    $('#risk_score_label').val('Low');
  }
  if (total >= 31 && total <= 50) {
    $('#risk_score_label').val('Medium');
  }
  if (total >= 51 && total <= 70) {
    $('#risk_score_label').val('High');
  }
  if (total >= 71) {
    $('#risk_score_label').val('Very High');
  }
});

// show or hide intel report name field
$('#id_intelreport').on('change', function() {
  if ( this.value == 'Yes')
    $("#id_intelreport_name, #id_intelreport_name_label").show();
  else
    $("#id_intelreport_name, #id_intelreport_name_label").hide();
}).trigger("change"); // notice this line

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
    //type: 'address',
    language: 'en',
    countries: ['ca'],
    aroundLatLngViaIP: false
  });
  placesAutocomplete.on('change', function resultSelected(e) {
    document.querySelector('#id_dest_address').value = e.suggestion.name || '';
    document.querySelector('#id_dest_city').value = e.suggestion.city || '';
    document.querySelector('#id_dest_province').value = e.suggestion.administrative || '';
    document.querySelector('#id_dest_postal_code').value = e.suggestion.postcode || '';
    document.querySelector('#id_dest_lat').value = e.suggestion.latlng.lat || '';
    document.querySelector('#id_dest_lng').value = e.suggestion.latlng.lng || '';
  });
 })();

 // Material Select Initialization
 $(document).ready(function() {
 $('.mdb-select').materialSelect();
 });

// Jquery finds the first empty tuples in choices for select input and disables it.
// This allows to restore the visible options and bypass a bug in mdb-select
// when no options are set to disabled.
 $("select option:first").attr("disabled", "true");
