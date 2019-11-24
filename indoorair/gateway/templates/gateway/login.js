function onLoginClick() {
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 400) {
            alert("Username or password is incorrect")
        } else if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            window.location.href = "/dashboard";
        }
    }

    xhttp.open("POST", "{% url 'login_api' %}", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("username="+username+"&password="+password);
}
