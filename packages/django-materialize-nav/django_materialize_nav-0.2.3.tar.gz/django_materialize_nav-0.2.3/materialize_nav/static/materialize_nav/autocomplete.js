autocomplete_objs = {};
_delay_input_tmr = 0;


function delay_input(ms, callback){
    try{
        clearTimeout(_delay_input_tmr);
    }catch (e) {
    }

    _delay_input_tmr = setTimeout(callback, ms);
}


function get_auto_data(id){
    try{
        return autocomplete_objs[id]['auto_data'];
    }catch (exc){
    }
    return null;
}


function get_auto_data_val(id, val){
    try{
        return autocomplete_objs[id]['auto_data'][val];
    }catch (exc){
    }
    return null;
}



function get_auto_field(id, fieldname){
    try{
        return autocomplete_objs[id][fieldname];
    }catch (exc){
    }
    return null;
}


function set_auto_field(id, fieldname, value){
    try{
        autocomplete_objs[id][fieldname] = value;
    }catch (exc){
        autocomplete_objs[id] = {};
        autocomplete_objs[id][fieldname] = value;
    }
}


function populate_autocomplete(id, json){
    var autocomplete_data = {};
    var autocomplete_li = {};
    for (var key in json){
        if (json.hasOwnProperty(key)){
            var name = json[key];
            var val_id = key;
            autocomplete_li[name] = null;
            autocomplete_data[name] = val_id;
        }
    }

    set_auto_field(id, 'auto_data', autocomplete_data);
    set_auto_field(id, 'auto_data_li', autocomplete_li);
    try{
        get_auto_field(id, 'auto_inst').updateData(autocomplete_li);
    }catch (exc){
    }
}


function request_autocomplete(id, url, query_name, search_text) {
    delay_input(500, function(){
        try{
            search_text = typeof search_text === 'undefined' ? $(id).val() : search_text;
        }catch (exc){
        }

        // Get the search query
        var data = {};
        if(typeof query_name !== "undefined" && query_name != null &&
            typeof search_text !== 'undefined' && search_text != null && search_text !== ''){
            data[query_name] = search_text;
        }

        // perform the ajax request and populate the autocomplete data with the successfully returned information.
        $.ajax({
            type: "GET",
            url: url,
            dataType: 'json',
            data: data,

            success: function (json) {
                populate_autocomplete(id, json);
            }
        });

    });
}
