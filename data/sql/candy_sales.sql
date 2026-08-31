USE candy_sales;

-- =========================================================
-- SALES ANALYSIS
-- =========================================================

-- Total Revenue
SELECT
    ROUND(SUM(Sales), 2) AS total_revenue
FROM candy_sales_featured;


-- Average Revenue
SELECT
    ROUND(AVG(Sales), 2) AS average_revenue
FROM candy_sales_featured;


-- Total Units Sold
SELECT
    SUM(Units) AS total_units_sold
FROM candy_sales_featured;


-- Revenue by Division
SELECT
    Division,
    ROUND(SUM(Sales), 2) AS total_revenue
FROM candy_sales_featured
GROUP BY Division
ORDER BY total_revenue DESC;


-- Revenue by Region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_revenue
FROM candy_sales_featured
GROUP BY Region
ORDER BY total_revenue DESC;


-- Revenue by Country
SELECT
    `Country/Region`,
    ROUND(SUM(Sales), 2) AS total_revenue
FROM candy_sales_featured
GROUP BY `Country/Region`
ORDER BY total_revenue DESC;


-- =========================================================
-- PROFIT ANALYSIS
-- =========================================================

-- Total Profit
SELECT
    ROUND(SUM(`Gross Profit`), 2) AS total_profit
FROM candy_sales_featured;


-- Average Profit Margin
SELECT
    ROUND(AVG(`Profit Margin`), 2) AS average_profit_margin
FROM candy_sales_featured;
