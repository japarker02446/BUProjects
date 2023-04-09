<?php
/* Calculate the area of the selected geometric shape based on the
    user provided dimensions.
    The PHP section contains code for calculating the area.
    The HTML and Javascript sections contain code for gathering user input, including:
        Shape selection
        Dimension input
*/
    // Initialize PHP variables.
    $area = NULL;
    if(sizeof($_GET) <= 1){$shape = NULL;}
    else{$shape = $_GET['shape'];}
    
    switch($shape){
        case 'trapezoid':
            $base1 = $_GET['base1'];
            $base2 = $_GET['base2'];
            $height = $_GET['height'];
            $area = (($base1 + $base2)/2 * $height);
            break;
        case 'cone':
            $height = $_GET['height'];
            $radius = $_GET['radius'];
            $area = M_PI * $radius * ($radius + sqrt(pow($height, 2) + pow($radius, 2)));
            break;
        case 'square':
            $side = $_GET['side'];
            $area = pow($side, 2);
            break;
        case 'circle':
            $radius = $_GET['radius'];
            $area = M_PI * pow($radius, 2);
            break;
        case 'rectangle':
            $side1 = $_GET['side1'];
            $side2 = $_GET['side2'];
            $area = $side1 * $side2;
            break;
        case 'cylinder':
            $height = $_GET['height'];
            $radius = $_GET['radius'];
            $area = (2 * M_PI * $radius * $height) + (2 * M_PI * pow($radius, 2));
            break;
        case 'triangle':
            $base = $_GET['base'];
            $height = $_GET['height'];
            $area = ($height * $base)/2;
            break;
    }
?>

<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="./js/shapeselect.js"></script>
    <link rel="stylesheet" type="text/css" href="./css/shapes.css">

    <script>
        // At start, hide all inputs.
        $(document).ready(function(){hideall()});
    </script>

    <title>Calculate Shape Area</title>
</head>
<body>
    <!--
        The HTML portion of the application has a few sections:
            - The Selection area is a dropdown listing of available shapes to calculate areas.
            - The dimenions input sections are a collection of divs, each containing a form
                that can be submitted to the PHP application for processing.
                The dimension inputs are structured as ONE FORM PER SHAPE to simplify the area
                calculation in PHP.
    -->
    <h1>Calculate Area</h1>
    <div>
        <label>Please select your shape</label>
        <select name="shape" onchange =updateselection(this.value)>
            <option disabled selected value>-- Please select a shape --</option>
            <option value="Trapezoid">Trapezoid</option>
            <option value="Cone">Cone</option>
            <option value="Square">Square</option>
            <option value="Circle">Circle</option>
            <option value="Rectangle">Rectangle</option>
            <option value="Cylinder">Cylinder</option>
            <option value="Triangle">Triangle</option>
        </select>
    </div>
    <p></p> <!-- spacer -->
    <div class="container">
        <div id="Trapezoid" class="input">
            <form action="calcshapes.php" method="GET">
                <input type="hidden" name="shape" value="trapezoid">
                <div><label>Base A</label><input type="number" step ="any" name="base1"></div>
                <div><label>Base B</label><input type="number" step ="any" name="base2"></div>
                <div><label>Height</label><input type="number" step ="any" name="height"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Trapezoid" class="image"><img src="./images/trapezoid.jpg"></div>
        <div id="Cone" class="input">
            <form action="calcshapes.php" method="GET">
            <input type="hidden" name="shape" value="cone">
                <div><label>Height</label><input type="number" step ="any" name="height"></div>
                <div><label>Radius</label><input type="number" step ="any" name="radius"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Cone" class="image"><img src="./images/cone.jpg"></div>
        <div id="Square" class="input">
            <form action="calcshapes.php" method="GET">
            <input type="hidden" name="shape" value="square">
                <div><label>Length</label><input type="number" step ="any" name="side"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Square" class="image"><img src="./images/square.jpg"></div>
        <div id="Circle" class="input">
            <form action="calcshapes.php" method="GET">
            <input type="hidden" name="shape" value="circle">
                <div><label>Radius</label><input type="number" step ="any" name="radius"></div>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Circle" class="image"><img src="./images/circle.jpg"></div>
        <div id="Rectangle" class="input">
            <form action="calcshapes.php" method="GET">
            <input type="hidden" name="shape" value="rectangle">
                <div><label>Width</label><input type="number" step ="any" name="side1"></div>
                <div><label>Length</label><input type="number" step ="any" name="side2"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Rectangle" class="image"><img src="./images/rectangle.jpg"></div>
        <div id="Cylinder" class="input">
            <form action="calcshapes.php" method="GET">
                <input type="hidden" name="shape" value="cylinder">
                <div><label>Radius</label><input type="number" step ="any" name="radius"></div>
                <div><label>Height</label><input type="number" step ="any" name="height"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Cylinder" class="image"><img src="./images/cylinder.jpg"></div>
        <div id="Triangle" class="input">
            <form action="calcshapes.php" method="GET">
                <input type="hidden" name="shape" value="triangle">
                <div><label>Base</label><input type="number" step ="any" name="base"></div>
                <div><label>Height</label><input type="number" step ="any" name="height"></div>
                <hr>
                <div id="button"><input type="submit" value="Calculate"></div>
            </form>
        </div>
        <div id="Triangle" class="image"><img src="./images/triangle.jpg"></div>
    </div>
    <div id="output">
        <label>Calculated Area</label>
        <span><?php echo number_format($area, 2, '.', ','); ?></span>
    </div>
</body>
<footer>
    <div>All images used without permission from Google.com</div>
</footer>
</html>