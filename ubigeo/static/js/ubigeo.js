function getProvincias(id, value_provincia, value_distrito){
    var provincias = $("#id_ubigeos_1");

    // clear the Provinces combobox
    provincias.find('option').remove();

    // Repopulate
    // provincia.append("<option value='' selected>---------</option>");

    var url = '/ubigeo/provincia/json/?region_id=' + id;
    var handler =  function(data){
        $.each(data, function(key, value){
            var option = "<option value='" + value.pk + "' selected>" + value.fields.name + "</option>";
            provincias.append(option);
        });
    };
    $.getJSON(url, handler);
}

function getDistritos(id, value_distrito){
    var distritos = $("#id_ubigeos_2");

    // clear the districts
    distritos.find('option').remove();
    
    // Repopulate
    // distrito.append("<option value='' selected>---------</option>");
    
    var url = '/ubigeo/distrito/json/?province_id=' + id;
    var handler = function(data){
        $.each(data, function(key, value){
            var option = "<option value='" + value.pk + "' selected>" + value.fields.name + "</option>";
            distritos.append(option);
        });
    };

    $.getJSON(url, handler);
}
