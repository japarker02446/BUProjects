/* Backend processing routes and code for METFCU transaction processing.
    Database table initialization,
   *Account creation,
    Account inquiry,
    Deposit,
    Withdrawl,
    List all transactions
*/

// Create a new account.
//  Checking is type = 1
//  Savings is type = 2
const dbConnect = require('../../js/dbConnect');
const router = require('express').Router();

router.put('/new', (req, res) => {

    // Destructure the request body element to extract account information.
    const {firstname, lastname, address1, address2, city, state, zip, telephone, account_type, balance} = req.body;
    
    // Check for required information.
    if(
        (firstname === null || firstname == undefined) ||
        (lastname === null || lastname == undefined) ||
        (address1 === null || address1 == undefined) ||
        (city === null || city == undefined) ||
        (state === null || state == undefined) ||
        (zip === null || zip == undefined) ||
        (account_type === null || account_type == undefined) ||
        (balance === null || balance == undefined)
    ){
        return res.status(500).json({result: "Missing required account information."});
    }
    
    // The opening balance must be at least $100.
    if(balance < 100){
        return res.status(500).json({result: "Opening balance must be at least $100.00."});
    }

    // The account was opened today.
    const dateopen = new Date().toUTCString();

    // Save account opening details.
    const openingValues = {
        firstname: firstname,
        lastname: lastname,
        address1: address1,
        address2: address2,
        city: city,
        state: state,
        zip: zip,
        telephone: telephone,
        dateopen: dateopen,
        account_type: account_type,
        balance: balance
    }

    const connection = dbConnect();
    connection.connect();

    connection.query("INSERT INTO account_table SET ?", openingValues, (err, results) => {
        if(err){
            return res.status(500).json({error: `error: ${err.message}`});
        }

        if(results.message.length <= 1){
            return res.status(200).json({result: "success", id: results.lastInsertId});
        } else {
            return res.status(500).json({result: "failure", id: -1});
        }
    });

    connection.end(err => {
        if(err){throw err;}
    });
});

module.exports = router;