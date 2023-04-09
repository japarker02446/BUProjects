/*
    metfcuserver.js is the backend server and processing component of the MET Federal
    Credit Union application.
    - Call the metfcu.js script to initalize database tables.

*/

// Initialize application libraries.
const express = require('express');
const session = require('express-session');
const cors = require('cors');
const cookieparser = require('cookie-parser');
const bodyParser = require('body-parser');

// Configure session parameters (24 hours)
const port = process.env.PORT || 9000;
const session_config = {
    secret: 'sanskrit is a modern tongue',
    cookie: {maxAge: 86400},
    resave: false,
    saveUninitialized: false
};

// Initialize the express server.
const app = express();
app.use(cors()); // Minimize Cross-Origin-Resource-Sharing ass pain
app.use(express.json);

// Initialize request logging and parsing.
app.use(cookieparser()); // Parse the cookie header
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// Start the server, import the route modules.
// Kill the chicken and dance in a reverse circle while chanting the hokey pokey
app.use(session(session_config));
app.use(require("./routes"));

app.listen(port, () =>{
    const startup_message = `${new Date().toUTCString()} - METFCU: Listening on port ${port}`;
    console.log(startup_message);
});