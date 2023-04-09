/* Backend processing routes and code for METFCU transaction processing.
    Database table initialization,
    Account creation,
    Account inquiry,
   *Deposit,
   *Withdrawl,
    List all transactions
*/

// Perform a transaction to the account.
//  Update the account balance in account_table.
//  If that is successful, record the transaction.
const dbConnect = require('../../js/dbConnect');
const updateAccountBalance = require('../../js/updateBalance.js');
const router = require('express').Router();

router.put('/transaction', (req, res) => {

    // Destructure the request body element to extract account information.
    const {account_id, transaction_type, amount} = req.body;
    if(
        (account_id === null || account_id == undefined) ||
        (transaction_type === null || transaction_type == undefined) || 
        (amount === null || amount == undefined)
    ){
        return res.status(500).json({result: "Missing required transaction information."});
    }
    
    // Update the account BALANCE, then record the transaction.
    updateAccountBalance(account_id, transaction_type, amount, (err, res) => {
        if(err){
            return res.status(500).json({error: `error: ${err.message}`});
        }

        // The transaction happens now.
        const datetime = new Date().toUTCString();

        const connection = dbConnect();
        connection.connect();

        const transaction = {
            account_id: account,
            datetime: datetime,
            type: transaction_type,
            amount: amount
        }

        connection.query("INSERT INTO trans_table SET ?", transaction, (err, results) => {
            if(err){
                return res.status(500).json({error: `error: ${err.message}`});
            }

            if(results.message.length <= 1){
                return res.status(200).json({result: "success", id: results.lastInsertId});
            } else {
                return res.status(500).json({result: "failure", id: -1});
            }
        });
    });
});

module.exports = router;