CREATE TABLE transactions (
    transaction_id INTEGER  PRIMARY KEY,
    date TEXT,
    account_id INTEGER,
    amount REAL,
    merchant TEXT
);