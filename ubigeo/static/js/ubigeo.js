var region_nullcase = "<option value='' selected></option>";
var province_nullcase = "<option value='' selected></option>";
var district_nullcase = "<option value='' selected></option>";

function getProvincias(id, value_provincia, value_distrito){
    var provincias = $("#id_ubigeo_1");

    // clear the Provinces combobox
    provincias.find('option').remove();

    // Repopulate
    provincias.append(province_nullcase);

    var url = '/ubigeo/provincia/json/?region_id=' + id;
    var handler =  function(data){

        $.each(data, function(key, value){
            var option = "<option value='" + value.pk + "'>" + value.fields.name + "</option>";
            provincias.append(option);
        });
    };
    $.getJSON(url, handler);
    
    // Clear Districts
    var distritos = $("#id_ubigeo_2");
    distritos.find('option').remove();
    distritos.append(district_nullcase);
}

function getDistritos(id, value_distrito){
    var distritos = $("#id_ubigeo_2");

    // clear the districts
    distritos.find('option').remove();
    
    // Repopulate
    distritos.append(district_nullcase);
    
    var url = '/ubigeo/distrito/json/?province_id=' + id;
    var handler = function(data){

        $.each(data, function(key, value){
            var option = "<option value='" + value.pk + "'>" + value.fields.name + "</option>";
            distritos.append(option);
        });
    };

    $.getJSON(url, handler);
}
