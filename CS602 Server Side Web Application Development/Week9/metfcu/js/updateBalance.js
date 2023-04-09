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
}

// Update the account balance.
const getAccountBalance = require('./getBalance');
updateAccountBalance = function (account_id, type, amount){

    // Get the current account balance and check transaction requirements.
    let balance = getAccountBalance(account_id);

    // Type 1 = Deposit, minimum of $1.
    if(type === 1 && amount >= 1){
        balance = balance + amount;
    } else {
        return JSON.stringify({error: "Minimum deposit of $1 required."});
    }

    // Type 2 = Withdrawl, maximum of balance.
    if(type === 2 && balance >= amount){
        balance = balance - amount;
    } else {
        return JSON.stringify({error: "Withdrawl amount exceeds account balance."});
    }

    const connection = dbConnect();
    connection.connect();

    connection.query(`UPDATE \'account_table\' WHERE \'account_id\' = ${account_id} SET \'balance\' = ${$balance}`, (err, results) => {
        if(err){
            return res.status(500).json({error: `error: ${err.message}`});
        } else {
            return res.status(200).json({result: "success", id: results.affectedRows});
        }
    });

    connection.end(err => {
        if(err){throw err;}
    });
};

module.exports = updateAccountBalance;