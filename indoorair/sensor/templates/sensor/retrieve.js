function onPageLoadCallSensorRetrieveAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);

            /*
             *  STEP 3: We need to input the JavaScript Object
             *          into somesort of function which will
             *          generate the HTML table based on the
             *          object data
             */
            renderPageWithData(dataObj);
        }
    }
    xhttp.open("GET","/api/sensor/{{ id }}", true);
    xhttp.send();
}

function renderPageWithData(dataObj) {
    var idElement = document.getElementById('sensor_id');
    var nameElement = document.getElementById('sensor_name');
    idElement.innerHTML = dataObj.id;
    nameElement.innerHTML = dataObj.name;
}


onPageLoadCallSensorRetrieveAPI();
