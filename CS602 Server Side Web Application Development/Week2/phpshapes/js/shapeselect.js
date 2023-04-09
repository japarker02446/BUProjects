/* shapeselect.js
    Support functions for the calcshapes.php application.
    Specifically, the javascript functions hideall and updateselection
    control the display of input form fields for the multiple shape
    options in the application.
*/

// Hide the input div for all shapes.
hideall = function(){
    $("#Trapezoid*").hide();
    $("#Cone*").hide();
    $("#Square*").hide();
    $("#Circle*").hide();
    $("#Rectangle*").hide();
    $("#Cylinder*").hide();
    $("#Triangle*").hide();
}

// Display the input div for the selected shape.
updateselection = function(selection){
    hideall();
    switch(selection){
        case "Trapezoid":
            $("#Trapezoid*").show();
            break;
        case "Cone":
            $("#Cone*").show();
            break;
        case "Square":
            $("#Square*").show();
            break;
        case "Circle":
            $("#Circle*").show();
            break;
        case "Rectangle":
            $("#Rectangle*").show();
             break;
        case "Cylinder":
            $("#Cylinder*").show();
            break;
        case "Triangle":
            $("#Triangle*").show();
            break;
    }
}   