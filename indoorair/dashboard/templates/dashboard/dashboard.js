function onPageLoadGetDashboardAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);
            generateTableFromObject(dataObj);
        }
    }
    xhttp.open("GET","api/dashboard", true);
    xhttp.send();
}

onPageLoadGetDashboardAPI();

function onLogoutClick() {
    window.location.href = "{% url 'logout_page' %}";
}


function generateTableFromObject(dataObj) {
   // This is the code which will create
   // the table header row.
   var htmlText = "<tr>";
   htmlText += "<th>Name</th>";
   htmlText += "<th>Temperature</th>";
   htmlText += "<th>Humidity</th>";
   htmlText += "<th>Pressure</th>";
   htmlText += "<th>Co2</th>";
   htmlText += "<th>TVOC</th>";
   htmlText += "<th></th>";
   htmlText += "</tr>";
   // This is the code which will generate
   // all the rows from the data from the
   // API endpoint.
   const instrumentsArray = dataObj.results;
   for (instrumentObj of instrumentsArray) {
       var idString = instrumentObj.id.toString();
       htmlText += "<tr>"; // START OF TABLE ROW
       htmlText += "<td>"+instrumentObj.name+"</td>"

       htmlText += "<td>"; // TEMPERATURE ROW STARTS HERE
       htmlText += "<ul>"; // <ul> means "unordered list"
       var temperatureObj = instrumentObj.temperature;
       htmlText += "<li>Mean:" + temperatureObj.mean + "</li>"; // <li> means "list item"
       htmlText += "<li>Median:" + temperatureObj.median + "</li>";
       htmlText += "<li>Mode:" + temperatureObj.mode + "</li>";
       htmlText += "</ul>";
       htmlText += "</td>"; // TEMPERATURE ROW ENDS HERE

       htmlText += "<td>"; // HUMIDITY ROW STARTS HERE
       htmlText += "<ul>"; // <ul> means "unordered list"
       var humidityObj = instrumentObj.humidity;
       htmlText += "<li>Mean:" + humidityObj.mean + "</li>"; // <li> means "list item"
       htmlText += "<li>Median:" + humidityObj.median + "</li>";
       htmlText += "<li>Mode:" + humidityObj.mode + "</li>";
       htmlText += "</ul>";
       htmlText += "</td>"; // HUMIDITY ROW ENDS HERE

       htmlText += "<td>";
       var pressureObj = instrumentObj.pressure;
       htmlText += "<li>Mean:" + pressureObj.mean + "</li>"; // <li> means "list item"
       htmlText += "<li>Median:" + pressureObj.median + "</li>";
       htmlText += "<li>Mode:" + pressureObj.mode + "</li>";
       htmlText += "</ul>";
       htmlText += "</td>";

       htmlText += "<td>";
       var co2Obj = instrumentObj.co2;
       htmlText += "<li>Mean:" + co2Obj.mean + "</li>"; // <li> means "list item"
       htmlText += "<li>Median:" + co2Obj.median + "</li>";
       htmlText += "<li>Mode:" + co2Obj.mode + "</li>";
       htmlText += "</ul>";
       htmlText += "</td>";

       htmlText += "<td>";
       var tvocObj = instrumentObj.tvoc;
       htmlText += "<li>Mean:" + tvocObj.mean + "</li>"; // <li> means "list item"
       htmlText += "<li>Median:" + tvocObj.median + "</li>";
       htmlText += "<li>Mode:" + tvocObj.mode + "</li>";
       htmlText += "</ul>";
       htmlText += "</td>";

       htmlText += "<td>";

       htmlText += "<button onclick='onViewClick("+idString+");'>View</button>";
       htmlText += "</td>";

       htmlText += "</tr>"; // END OF TABLE ROW
   }
   var tableElement = document.getElementById("instruments_list");
   tableElement.innerHTML = htmlText;
}
