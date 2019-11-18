function generateTableFromObject(dataObj) {
    // This is the code which will create
    // the table header row.
    var htmlText = "<tr>";
    htmlText += "<th>ID</th>";
    htmlText += "<th>Name</th>";
    htmlText += "<th>Report</th>";
    htmlText += "</tr>";

    // This is the code which will generate
    // all the rows from the data from the
    // API endpoint.

    const TimeseriesDatumArray = dataObj.TimeseriesDatum;
    for (TimeseriesDatumObj of TimeseriesDatumArray) {
        var idString = TimeseriesDatumObj.id.toString();
        console.log(idString);
        htmlText += "<tr>";
        htmlText += "<td>"+idString+"</td>";
        htmlText += "<td>"+TimeseriesDatumObj.name+"</td>"
        htmlText += "<td>"+TimeseriesDatumObj.value+"</td>"
        htmlText += "<td>";
        htmlText += "<button onclick='onViewClick("+idString+");'>View</button>";
        htmlText += "</td>";
        htmlText += "</tr>";
    }

    var tableElement = document.getElementById("TimeseriesDatum_report");
    tableElement.innerHTML = htmlText;
}

/**
 * STEP 2: We need to create a function to `GET` the
 *         list data from the API web-service
 */
function onPageLoadRunGetTimeSeriesDAtumReportListFromAPI() {
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
            generateTableFromObject(dataObj);
        }
    }
    xhttp.open("GET","{% url 'report_list_page' %}", true);
    xhttp.send();
}

onPageLoadRunGetTimeSeriesDAtumReportListFromAPI();

function onViewClick(TimeseriesDatumId) {
    window.location.href = {"{% url 'report_01_page' %}"+TimeseriesDatumId};
}
