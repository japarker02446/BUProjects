<?php

# Security controls
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, PUT, DELETE");
header("Content-type: application/json");
header('Cache-control: no-cache, must-revalidate');
header('Expires: ', gmdate('D, d M Y H:i:s \G\M\T', time() - 1));   // Expire one second ago ... *poof*


/*  This is an application that demonstrates route parsing given a .json data file of restaurant reviews.
    The application is composed of the following sections:
        - PHP: PHP code to process data and URL routing requests.
        - HTML: Display area for requested results (reviews, action responses).
            - CSS: Minimal look and feel styling for the HTML page.
*/

// Retrieve data from the JSON file.
$jsonString = file_get_contents("./data/route_man_datafile.json");
$reviewsArray = json_decode($jsonString, true);

// Following are the target functions of the different route requests.

// Find a review by ID number.
function getReview($reviewsArray, $id){
    foreach($reviewsArray as $nextReview){
        if(intval($nextReview["route_id"]) == intval($id)){
            return $nextReview;
        }
    }
    return null;
}

// Delete a review by ID number.
function deleteReview($reviewsArray, $id){
    for($i = 0; $i < sizeof($reviewsArray); $i ++){
        if(intval($reviewsArray[$i]["route_id"]) == intval($id)){
            array_splice($reviewsArray, $i, 1);
        }
    }
    return $reviewsArray;
}

// Add a new review from POST.
function addReview($reviewsArray){
    $newArray = array();
    foreach($reviewsArray as $nextReview){
        $tempReview = array("route_id"  => $nextReview["route_id"],
                            "name"      => $nextReview['name'],
                            "location"  => $nextReview['location'],
                            "caption"   => $nextReview['caption'],
                            "review"    => $nextReview['review']
                    );
        $newArray[] = $tempReview;
    }

    $tempReview = array("route_id"  => rand(10, 9999),
                        "name"      => $_POST['name'],
                        "location"  => $_POST['location'],
                        "caption"   => $_POST['caption'],
                        "review"    => $_POST['review']
                );
    $newArray[] = $tempReview;
    return $newArray;
}

// Edit a review from PUT.
function editReview($reviewsArray, $id){
    print_r($_PUT);

    $newArray = array();
    for($i = 0; $i < sizeof($reviewsArray); $i ++){
        
        // Load ALL the data.
        $tempReview = array();
        $tempReview["route_id"] = $reviewsArray[$i]["route_id"];
        $tempReview["name"] = $reviewsArray[$i]["name"];
        $tempReview["location"] = $reviewsArray[$i]["location"];
        $tempReview["caption"] = $reviewsArray[$i]["caption"];
        $tempReview["review"] = $reviewsArray[$i]["review"];
        
        // Edit THE REQUESTED data.
        if(intval($reviewsArray[$i]["route_id"]) == intval($id)){
            if(isset($_PUT["name"])){$tempReview["name"] = $_PUT["name"];}
            if(isset($_PUT["location"])){$tempReview["location"] = $_PUT["location"];}
            if(isset($_PUT["caption"])){$tempReview["caption"] = $_PUT["caption"];}
            if(isset($_PUT["review"])){$tempReview["review"] = $_PUT["review"];}
        } 
        $newArray[] = $tempReview;
    }
//  print_r($newArray);
    return $newArray;
}

// Route the request.
switch($_SERVER['REQUEST_METHOD']){
    case "GET":
        if(strlen(trim($_SERVER['PATH_INFO'])) < 1){
            echo json_encode($reviewsArray);
        } else {
            $call = explode('/', trim($_SERVER['PATH_INFO']));
//          print_r($call);
            echo json_encode(getReview($reviewsArray, $call[1]));
        }
        break;
    
    case "POST":
        $reviewsArray = addReview($reviewsArray);
        echo json_encode($reviewsArray);
        break;
    
    case "PUT":
        if(strlen(trim($_SERVER['PATH_INFO'])) < 1){
            echo 'ERROR, please include a review ID for edit\n';
        } else {
            $call = explode('/', trim($_SERVER['PATH_INFO']));
//          print_r($call);
            $reviewsArray = editReview($reviewsArray, $call[1]);
            echo json_encode($reviewsArray);
        }
        break;
    
    case "DELETE":
        if(strlen(trim($_SERVER['PATH_INFO'])) < 1){
            echo 'ERROR, please include a review ID for deletion\n';
        } else {
            $call = explode('/', trim($_SERVER['PATH_INFO']));
//          print_r($call);
            $reviewsArray = deleteReview($reviewsArray, $call[1]);
            echo json_encode($reviewsArray);
        }
        break;
}

?>