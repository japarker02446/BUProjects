<?php
    // _GET the data from teh form.
    $tempValue = $_GET['tempvalue'];
    $tempunit = $_GET['tempunit'];
    //echo $tempValue;
    //echo $tempunit;

    // Calculate temperature conversions
    switch($tempunit){
        // from Farhenheit
        case "F":
            //echo("F");
            $farValue = $tempValue;
            $celValue = ($tempValue - 32) * (5/9);
            $kelValue = (($tempValue - 32) * (5/9)) + 273.15;
            break;
        // from Celsius
        case "C":
            //echo("C");
            $farValue = ($tempValue * 9/5) + 32;
            $celValue = $tempValue;
            $kelValue = $tempValue + 273.15;
            break;
        // from Kelvin
        case "K":
            //echo("K");
            $farValue = ($tempValue - 273.15) * (9/5) + 32;
            $celValue = ($tempValue - 273.15);
            $kelValue = $tempValue;
            break;
    }
?>

<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Temperature Conversion</title>
</head>
<body>
    <h1>Temperature Conversion</h1>
    <p><?php echo("$tempValue $tempunit is:")?></p>
    <p><?php echo("$farValue &#176F")?></p>
    <p><?php echo("$celValue &#176C")?></p>
    <p><?php echo("$kelValue K")?></p>
</body>
</html>