CREATE TABLE bank_customers
(
    customer_no INT ,

    customer_name VARCHAR(100),

    cnic VARCHAR(20),

    city VARCHAR(50),

    age NUMERIC(2,0),

    gender VARCHAR(20),

    account_number BIGINT UNIQUE PRIMARY KEY,

    branch_code NUMERIC(3,0),

    account_opening_date DATE,

    account_type VARCHAR(50),

    account_status VARCHAR(50),

    risk_category VARCHAR(50),

    kyc_status VARCHAR(50),

    debit_card_company VARCHAR(50),

    debit_card_type VARCHAR(50),


    customer_year_end_balance_2023 NUMERIC(15,2),

    customer_year_end_balance_2024 NUMERIC(15,2),

    customer_year_end_balance_2025 NUMERIC(15,2),

    customer_year_end_balance_2026 NUMERIC(15,2),


    customer_credit_transactions_count_2023 INT,

    customer_credit_transactions_count_2024 INT,

    customer_credit_transactions_count_2025 INT,

    customer_credit_transactions_count_2026 INT,


    customer_total_credit_transaction_amount_2023 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2024 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2025 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2026 NUMERIC(15,2),


    customer_debit_transactions_count_2023 INT,

    customer_debit_transactions_count_2024 INT,

    customer_debit_transactions_count_2025 INT,

    customer_debit_transactions_count_2026 INT,


    customer_total_debit_transaction_amount_2023 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2024 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2025 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2026 NUMERIC(15,2)
);


--for 2026 data ------
CREATE TABLE bank_customers_2026
(
    customer_no INT ,

    customer_name VARCHAR(100),

    cnic VARCHAR(20),

    city VARCHAR(50),

    age NUMERIC(2,0),

    gender VARCHAR(20),

    account_number BIGINT UNIQUE PRIMARY KEY,

    branch_code NUMERIC(3,0),

    account_opening_date DATE,

    account_type VARCHAR(50),

    account_status VARCHAR(50),

    risk_category VARCHAR(50),

    kyc_status VARCHAR(50),

    debit_card_company VARCHAR(50),

    debit_card_type VARCHAR(50),


    customer_year_end_balance_2023 NUMERIC(15,2),

    customer_year_end_balance_2024 NUMERIC(15,2),

    customer_year_end_balance_2025 NUMERIC(15,2),

    customer_year_end_balance_2026 NUMERIC(15,2),


    customer_credit_transactions_count_2023 INT,

    customer_credit_transactions_count_2024 INT,

    customer_credit_transactions_count_2025 INT,

    customer_credit_transactions_count_2026 INT,


    customer_total_credit_transaction_amount_2023 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2024 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2025 NUMERIC(15,2),

    customer_total_credit_transaction_amount_2026 NUMERIC(15,2),


    customer_debit_transactions_count_2023 INT,

    customer_debit_transactions_count_2024 INT,

    customer_debit_transactions_count_2025 INT,

    customer_debit_transactions_count_2026 INT,


    customer_total_debit_transaction_amount_2023 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2024 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2025 NUMERIC(15,2),

    customer_total_debit_transaction_amount_2026 NUMERIC(15,2)
);
SELECT COUNT(*) FROM bank_customers_2026;  -- should be 13665

SELECT COUNT(*) FROM (
    SELECT account_number FROM bank_customers_2026
    GROUP BY account_number HAVING COUNT(*) > 1
) dups;  -- should be 0


SELECT COUNT(*) FROM bank_customers_2026 t
WHERE EXISTS (
    SELECT 1 FROM bank_customers m WHERE m.account_number = t.account_number
);

INSERT INTO bank_customers
SELECT * FROM bank_customers_2026;


select min(account_opening_date),max(account_opening_date) from bank_customers;
drop table bank_customers;
SELECT
*
FROM bank_customers;


truncate table bank_customers;