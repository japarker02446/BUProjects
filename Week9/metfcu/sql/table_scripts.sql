/*
    SQL Table Creation script(s) for METFCU application.
        Account Information
        Account Transactions
*/ 
CREATE TABLE IF NOT EXISTS account_table (
    account_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, 
    firstname VARCHAR(32) NOT NULL, 
    lastname VARCHAR(64) NOT NULL, 
    address1 VARCHAR(512) NOT NULL, 
    address2 VARCHAR(256) NULL, 
    city VARCHAR(256) NOT NULL, 
    state VARCHAR(2) NOT NULL, 
    zip VARCHAR(16) NOT NULL, 
    telephone VARCHAR(15), 
    dateopen DATE NOT NULL, 
    account_type TINYINT UNSIGNED NOT NULL, 
    balance DOUBLE NOT NULL, 
    PRIMARY KEY (account_id)
);

CREATE TABLE IF NOT EXISTS trans_table (
    transaction_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    account_id BIGINT UNSIGNED NOT NULL,
    datetime DATETIME NOT NULL,
    transaction_type TINYINT(1) UNSIGNED NOT NULL,
    amount DOUBLE NOT NULL,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (account_id) 
        REFERENCES account_table(account_id)
);
