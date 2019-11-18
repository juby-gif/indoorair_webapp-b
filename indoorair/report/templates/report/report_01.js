function onPageLoadRunGetTimeSeriesDAtumReport01FromAPI() {
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
    xhttp.open("GET","{% url 'report_01_page' %}", true);
    xhttp.send();
}

onPageLoadRunGetTimeSeriesDAtumReportListFromAPI();
