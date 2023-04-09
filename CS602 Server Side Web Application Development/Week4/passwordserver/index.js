/* 
    /passwordserver/index.js is the backend processing component of the passwordstore application.
    This file contains functionality to:
    - Establish session credentials.
    - Route page requests.
    - Store, retrieve and process data values.
*/

// Initialize applciation libraries.
const express = require('express');
const expressSession = require('express-session');
const cors = require('cors');

// Initialize session parameters.
// The passwordstore APPLICATION will run on port 3000.
const port = 3001;
const session = {
    secret: "the cake is a lie, take a big bite",
    resave: false,
    saveUninitialized: true,
    cookie: {secure: false}
};

// Initialize application parameters.
var app = express();
app.use(cors());
app.use(expressSession(session));
app.use(express.json());


// Handle the requests.
// Initialize the session array for all clients.
app.all('*', (req, res, next) => {
    let passwordArray = session.passwordArray || [];    // Return the existing or an empty array to hold passwords.
    session.passwordArray = passwordArray;              // Load the passwordArray to the session.
    next();
});

// Get all or one password.
// If a password is request for a keyValue that does not exist, return all.
app.get('/', (req, res) => {
     if(Object.keys(req.query).length === 0){
//      console.log('Get All: ' + JSON.stringify(session.passwordArray));
        res.json(session.passwordArray);
        return session.passwordArray;
    } else {
        const targetEntry = findKeyIndex(req);
        if(targetEntry === 0 || targetEntry){
            res.json(session.passwordArray[targetEntry]);
            return session.passwordArray[targetEntry];
        } else {
            console.log("No password found for " + req.query.keyValue);
            res.json(session.passwordArray);
            return session.passwordArray;
        }
    }
});

// Delete the target password.
app.delete('/', (req, res) => {
    const targetEntry = findKeyIndex(req);
    if(targetEntry === 0 || targetEntry){
        session.passwordArray.splice(targetEntry, 1);
    } else {
        console.log("No password found for " + req.query.keyValue);
    }
//  console.log('Delete: ' + JSON.stringify(session.passwordArray));
    res.json(session.passwordArray);
    return session.passwordArray;
});

// Create a new key: password pair.
// Do not create a password for an existing key value.
app.put("/add", (req, res) => {

    // Where in the World is the Request Data?
//  console.log('Params: ' + JSON.stringify(req.params));
//  console.log('Body: ' + JSON.stringify(req.body));
//  console.log('Query: ' + JSON.stringify(req.query));
    const targetEntry = findKeyIndex(req);
    console.log("Add says targetEntry is: " + targetEntry);

    // Destructure the req.query to our key:password pair.
    // Make sure there is no password already listed for keyValue:
    //  It does not exist OR it is not index 0 (the first entry).
    if(targetEntry !== 0 && !targetEntry){
        const {keyValue, password} = req.query;  
        const entry = {
            'keyValue': keyValue,
            'password': password,
            'oldPassword': null
        }
        session.passwordArray.push(entry);
    } else {
        console.log("Password found for " + session.passwordArray[targetEntry].keyValue + ". Please use EDIT to change it.");
    }

//  console.log('Add: ' + JSON.stringify(session.passwordArray));
    res.json(session.passwordArray);
    return session.passwordArray;
});

// Edit a specific password.
//  1. Find the entry for the password to edit.
//  2. SAVE the OLD password.
//  3. Edit to the new password.
app.put('/edit', (req, res) => {
    const targetEntry = findKeyIndex(req);
    if(targetEntry){
        session.passwordArray[targetEntry]['oldPassword'] = session.passwordArray[targetEntry]['password'];
        session.passwordArray[targetEntry]['password'] = req.query.password;
    
    //  console.log('Edit: ' + JSON.stringify(session.passwordArray));
        res.json(session.passwordArray);
        return session.passwordArray;
    } else {
        console.log("No Password found for " + req.query.keyValue);
    }
});

// Return the INDEX OF the keyValue associated with the request in the passwordArray object.
// If the keyValue is not found, return null.
findKeyIndex = function(req){
    for(i = 0; i < session.passwordArray.length; i ++){
        if(session.passwordArray[i]['keyValue'] === req.query.keyValue){
            return i;
        }
    }
    return null;
}

app.listen(port, () => console.log('Password Store Server listening on port ' + port + '!'));