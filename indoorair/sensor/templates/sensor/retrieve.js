function generateViewFromObject(dataObj) {
    if (dataObj.was_found === false) {
        alert("Sorry we could not find that data!");
        onBackClick();
    } else {
        var idInputElement = document.getElementById("id");
        var nameInputElement = document.getElementById("name");
        idInputElement.value = dataObj.id;
        nameInputElement.value = dataObj.name;
    }
}

function onPageLoadRunGetTimeSeriesDataListFromAPI(sensor_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);
            generateViewFromObject(dataObj);
        }
    }
    const detailURL = "/api/retrieve/"+sensor_id.toString();
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    xhttp.send();
}

const instrument_id = {{ sensor_id }};
onPageLoadRunGetInstrumentDetailsFromAPI(sensor_id);


function onBackClick() {
    window.location.href = "{% url 'i_list_page' %}";
}
