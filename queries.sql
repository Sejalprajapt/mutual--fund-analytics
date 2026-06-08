-- 1. Top 10 funds by NAV
SELECT amfi_code, MAX(nav) AS max_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY max_nav DESC
LIMIT 10;

-- 2. Average NAV by fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Highest 1-Year Return
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 4. Highest 3-Year Return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- 5. Lowest Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;

-- 6. Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 7. Count Transactions by Type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Total Transaction Amount
SELECT SUM(amount)
FROM fact_transactions;

-- 9. Average Transaction Amount
SELECT AVG(amount)
FROM fact_transactions;

-- 10. Total NAV Records per Fund
SELECT amfi_code, COUNT(*)
FROM fact_nav
GROUP BY amfi_code
ORDER BY COUNT(*) DESC;