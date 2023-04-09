/* Process input from the password store UI page.
    Functions in passwordstore.js will process input from the password store HTML UI Page.
    The function will parse the data appropriately and execute ajax calls 
*/

/* On page load, hide things that should be hidden.
*/
$(document).ready(function () {
    $(".hideme").hide();
    $("#editinput").hide();
});

// Clear the display div and load the current password array.
let appendToDisplay = function(passwordJson){

    $("#display").empty();
    passwordArray = JSON.parse(JSON.stringify(passwordJson));
    console.log(JSON.stringify(passwordJson));

    // Create a table row to hold the keyValue, password, oldPassword
    // edit button and delete button
    passwordArray.forEach(function(element){
        var nextRow = document.createElement('tr');
        var site = document.createElement('td');
        var passNow = document.createElement('td');
        var passOld = document.createElement('td');
        var viewCell = document.createElement('td');
        var editCell = document.createElement('td');
        var delCell = document.createElement('td');
        var viewButton = document.createElement('button');
        var editButton = document.createElement('button');
        var delButton = document.createElement('button');

        site.innerHTML = element.keyValue;
        passNow.innerHTML = element.password;
        passNow.setAttribute('class', 'hideme');
        if(element.oldPassword){passOld.innerHTML = element.oldPassword;}
        else{passOld.innerHTML = '';}
        passOld.setAttribute('class', 'hideme');

        viewButton.type = "button";
        viewButton.onclick = function(){viewPassword(element)};
        viewButton.innerText = "VIEW";

        editButton.type = "button";
        editButton.onclick = function(){editPassword(element)};
        editButton.innerText = "EDIT";

        delButton.type = "button";
        delButton.onclick = function(){deletePassword(element)};
        delButton.innerText = "DELETE";

        viewCell.append(viewButton);
        editCell.append(editButton);
        delCell.append(delButton);

        nextRow.append(site);
        nextRow.append(passNow);
        nextRow.append(passOld);
        nextRow.append(viewCell);
        nextRow.append(editCell);
        nextRow.append(delCell);
        $("#display").append(nextRow);
    });
}
