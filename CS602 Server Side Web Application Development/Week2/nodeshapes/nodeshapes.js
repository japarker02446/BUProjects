// Use the readline-sync module to read from stdin without callback multiuthreading.
const rl = require('readline-sync');

// Define all of the shape area calculations as functions.
let trapezoid = function(){
    var base1 = rl.question('Please enter the length of the first base:');
    var base2 = rl.question('Please enter the length of the second base:');
    var height = rl.question('Please enter the height:');
    return(((base1 + base2)/2)*height);
}

let cone = function(){
    var height = rl.question('Please enter the cone height:');
    var radius = rl.question('Please enter the cone radius:');
    return(Math.PI * radius  * (radius + Math.sqrt(Math.pow(height,2) + Math.pow(radius,2))));
}

let square = function(){
    var side = rl.question('Please enter the length of the sides:');
    return(Math.pow(side, 2));
}

let circle = function(){
    var radius = rl.question('Please enter the radius:');
    return(Math.PI * Math.pow(radius, 2));
}

let rectangle = function(){
    var side1 = rl.question('Please enter the length of the one side:');
    var side2 = rl.question('Please enter the length of the second side:');
    return(side1 * side2);
}

let cylinder = function(){
    var height = rl.question('Please enter the height');
    var radius = rl.question('Please enter the radius');
    return((2 * Math.PI * radius * height) + (2 * Math.PI * Math.pow(radius,2)));
}

let triangle = function(){
    var base = rl.question('Please enter the length of the base:');
    var height = rl.question('Please enter the height:');
    return((height*base)/2);
}

// Get user input to choose the shape to calculate area.
var area;
let shape = rl.question('Please choose the number of the shape you want to calculate the area for:\n' +
'[1] Trapezoid\n' +
'[2] Cone\n' +
'[3] Square\n' +
'[4] Circle\n' +
'[5] Rectangle\n' +
'[6] Cylinder\n' +
'[7] Triangle:\n');

// Process the selected shape.
switch(shape){

    // Trapezoid
    case "1":
    console.log("You have selected 1. Trapezoid");
    area = trapezoid();
    break;

    // Cone
    case "2":
    console.log("You have selected 2. Cone");
    area = cone();
    break;

    // Square
    case "3":
    console.log("You have selected 3. Square");
    area = square();
    break;

    // Circle
    case "4":
    console.log("You have selected 4. Circle");
    area = circle();
    break;

    // Rectangle
    case "5":
    console.log("You have selected 5. Rectangle");
    area = rectangle();
    break;

    // Cylinder
    case "6":
    console.log("You have selected 6. Cylinder");
    area = cylinder();
    break;

    // Triangle
    case "7":
    console.log("You have selected 7. Triangle");
    area = triangle();
    break;

    default:
    console.log("Please select a value from 1 - 7");
}
console.log("The area is " + Number(area).toFixed(2));
