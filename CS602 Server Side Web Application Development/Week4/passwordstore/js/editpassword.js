// Edit the selected password entry, PART 1.
// Retrieve the current key value pair and load the input form.
let editPassword = function(passwordEntry){

    // Limit the password list to the selected entry.
    viewPassword(passwordEntry);

    // Change the input field to EDIT mode.
    $("#passinput").hide();
    $("#editinput").show();

    // Extract the OLD keyValue and password.
    passwordEntry = JSON.parse(JSON.stringify(passwordEntry));
    
    // Populate these values into the EDIT input form.
    // The keyValue field in the form is DISABLED.
    let editKeyForm = document.getElementById("editKeyValue");
    let editPassForm = document.getElementById("editPassword");

    editKeyForm.value = passwordEntry.keyValue;
    editPassForm.placeholder = passwordEntry.password;
}

// Edit the selected password entry, PART 2.
// Retrieve new password and submit to the server to edit.
let submitedit = function(){
    
    // Populate these values into the EDIT input form.
    // The keyValue field in the form is DISABLED.
    let editKeyForm = document.getElementById("editKeyValue");
    let editPassForm = document.getElementById("editPassword");

    let URL = "http://localhost:3001/edit?keyValue=" + editKeyForm.value + "&password=" + editPassForm.value;
    console.log("EDIT password store sending: " + URL);
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
        document.getElementById("editinput").reset();
        $(".hideme").hide();

        // Restore the regular password input form.
        $("#editinput").hide();
        $("#passinput").show();
    })
    .catch(function(err){
        console.log("Fetch error:", err);
    });
}