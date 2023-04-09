// Show all passwords
let showall = function(){
    let URL = "http://localhost:3001/";
    //  console.log("Delete password store sending: " + URL);
    fetch(URL, {
        method: 'GET', 
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
    })
    .catch(function(err){
        console.log("Fetch error:", err);
    });
    $(".hideme").show();
}