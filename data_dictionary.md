# Data Dictionary

## fact_nav
- amfi_code : Mutual fund identifier
- date : NAV date
- nav : Net Asset Value

## fact_transactions
- transaction_id : Unique transaction id
- amfi_code : Fund identifier
- amount : Transaction amount
- transaction_type : SIP/Lumpsum/Redemption
- transaction_date : Date of transaction

## fact_performance
- amfi_code : Fund identifier
- return_1yr_pct : 1 year return %
- return_3yr_pct : 3 year return %
- return_5yr_pct : 5 year return %
- expense_ratio_pct : Expense ratio %