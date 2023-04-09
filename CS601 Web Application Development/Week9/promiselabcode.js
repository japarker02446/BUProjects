// Code for promislab project.
// Get the list of sites to FETCH.
var siteList =  [
    "http://zumatra.com/teach/promise_2.php",
    "http://zumatra.com/teach/promise_5.php",
    "http://zumatra.com/teach/promise_10.php"
];

var mydisplay;

function search(){
    console.log("search");
    for(var i = 0; i < siteList.length; i ++){
        fetch(siteList[i])
        .then(function(response){
            return response.json();
        })
        //Destructuring the JSON object array to elements.
        // Put each element into a new colored circle.


        .then(function(newJson) {
            myArray = JSON.parse(JSON.stringify(newJson));
            for(const [, element] of myArray.entries()){
                console.log("element " + element);
                createNewCircle(element);    
            }
//          console.log(JSON.stringify(newJson));
        });
    }
}

// Create a multicolored circle with the value of each FETCH returned element.
function createNewCircle(nextElement){
    mydisplay = document.getElementsByClassName("displayarea");
    var newDiv = document.createElement('div');
    newDiv.draggable = true;
    newDiv.id = new Date().toDateString();
    
    var newBtn = document.createElement('button');
    newBtn.className = "displaycircle rainbow";
    newBtn.onmousedown = "dragElement(this)";
    newBtn.draggable = true;
    newBtn.innerHTML = nextElement;

    // Append the new div to the document display area.
    newDiv.append(newBtn);
    mydisplay[0].appendChild(newDiv);
}