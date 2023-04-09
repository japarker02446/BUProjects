// Delete the selected password entry.
let deletePassword = function(passwordEntry){
//  console.log("Delete " + JSON.stringify(passwordEntry));
    passwordEntry = JSON.parse(JSON.stringify(passwordEntry));
    let keyval = passwordEntry.keyValue;
    let passval = passwordEntry.password;
    
    let URL = "http://localhost:3001/?keyValue=" + keyval + "&password=" + passval;
//  console.log("Delete password store sending: " + URL);
    fetch(URL, {
        method: 'DELETE', 
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