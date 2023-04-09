/* Get a keyValue / password pair, load them to a JSON
    object and pass them to passwordserver for processing.
    Clear the form for the next input value.
    Hide password values.
*/
let addpassword = function(){
    let keyval = document.getElementById("nextKeyValue");
    let passval = document.getElementById("nextPassword");
    
    let URL = "http://localhost:3001/add?keyValue=" + keyval.value + "&password=" + passval.value;
//  console.log("Add password store sending: " + URL);
    fetch(URL, {
        method: 'PUT', 
        mode: 'cors'
    })
    .then(function(response){
        if(response.ok != true){
            console.log("Something went wrong: ", response.status);
            return;
        }
        return response.json();
    })
    .then(function(passwordJson){
        appendToDisplay(passwordJson);
        document.getElementById("passinput").reset();
        $(".hideme").hide();
    })
    .catch(function(err){
        console.log("Fetch error:", err);
    });
}