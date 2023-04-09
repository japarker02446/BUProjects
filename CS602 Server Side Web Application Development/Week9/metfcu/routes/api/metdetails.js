/* Backend processing routes and code for METFCU transaction processing.
    Database table initialization,
    Account creation,
   *Account inquiry,
    Deposit,
    Withdrawl,
    List all transactions
*/
const dbConnect = require('../../js/dbConnect');
const router = require('express').Router();

router.put('/details', (req,res) => {
    const {account_id} = req.body;
    if(account_id === null || account_id == undefined){
        return res.status(500).json({result: "Missing required transaction information."});
    }

    // Get the list of transactions from the database.
    const connection = dbConnect();
    connection.connect();

    const resultArray = [];

    connection.query(`SELECT * FROM account_table WHERE account_id = ${account_id}`, (err, res) => {
        if(err){
            return res.status(500).json({error: `error: ${err.message}`});
        }

        Object.keys(res).forEach(function(key){
            resultArray.push(res[key]);
        });
    });

    return res.status(200).json({result: `result: ${resultArray}`});

});

module.exports = router;