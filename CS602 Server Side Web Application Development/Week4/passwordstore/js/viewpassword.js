let viewPassword = function (passwordEntry) {
    passwordEntry = JSON.parse(JSON.stringify(passwordEntry));
    let keyval = passwordEntry.keyValue;
    let passval = passwordEntry.password;
    
    let URL = "http://localhost:3001/?keyValue=" + keyval;
    console.log("VIEW password store sending: " + URL);
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

    /* OMG this is so stupid.  You have to wrap a single JSON object in
        square brackets to make it an array so that appendToDisplay can
        run the foreach
    */
    .then(function(passwordJson){
        appendToDisplay([passwordJson]);
        document.getElementById("passinput").reset();
    })
    .catch(function(err){
        console.log("Fetch error:", err);
    });
    $(".hideme").show();
}