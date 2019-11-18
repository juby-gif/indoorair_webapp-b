function onRegisterClick() {
   const firstName = document.getElementById("first_name").value;
   const lastName = document.getElementById("last_name").value;
   const email = document.getElementById("email").value;
   const password = document.getElementById("password").value;
   const username = document.getElementById("username").value;
   var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
           // Get the string data that the server sent us.
           const resultString = this.responseText;
           // Create an object which converts the string to an object using JSON parsing.
           var resultObject = JSON.parse(resultString);
           // Please note, "was_registered" is a key set by the server.
           if (resultObject.was_registered === false) {
               alert(resultObject.reason);
           } else {
               window.location.href = "{% url 'registered_page' %}";
           }
       }
   }
   xhttp.open("POST", "{% url 'register_api' %}", true);
   xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
   xhttp.send("first_name="+firstName+"&last_name="+lastName+"&email="+email+"&username="+username+"&password="+password);
}


//for logout
function onLogoutClick() {
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
           // Get the string data that the server sent us.
        const loginObject = JSON.parse(this.responseText);
        if(loginObject.was_successful === true){
          window.location.href = "{% url 'login_page' %}";
      }
      else {
        alert(loginObject.reason);
      }
      }
    }
  xhttp.open("POST", "/api/logout", true);
  xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
  xhttp.send();

}
