// Database configuration and connection.
const mysql = require("mysql");
const mysql_config = {
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'metfcudb'
}

function dbConnect() {
    const connection = mysql.createConnection(mysql_config);
    connection.connect();
    return connection;
};

module.exports = dbConnect;