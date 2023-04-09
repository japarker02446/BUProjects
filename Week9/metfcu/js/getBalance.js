// Return the current account balance by account_id.
var getAccountBalance = function(account_id){
 
    let balance;
    const connection = dbConnect();
    connection.connect();

    connection.query(`SELECT \'balance\' FROM \'account_table\' WHERE \'account_id\' = ${account_id}`, (err, results) => {
        if(err){
            return res.status(500).json({error: `error: ${err.message}`});
        } else {
            balance = results[0].balance;
        }
    });

    connection.end(err => {
        if(err){throw err;}
    });

    return balance;
};

module.exports = getAccountBalance;