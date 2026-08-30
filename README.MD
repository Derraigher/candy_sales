# Candy Sales Analysis Project

## Tech Stack

- Python
- Pandas
- MySQL
- Power BI

## Project Overview

This project analyzes sales data from a candy distribution business.

The project uses **Python (Pandas)**, **MySQL**, and **Power BI** and is divided into several stages.

### 1. Data Preparation

The original dataset did not require a dedicated data cleaning stage, so the project focused directly on data preparation, exploratory analysis, and feature engineering.

### 2. Exploratory Data Analysis (Python / Pandas)

An Exploratory Data Analysis (EDA) was performed using Pandas to understand the structure of the dataset and identify relevant patterns across sales, profit, products, customers, regions, divisions, and shipping.

The analysis helped identify the main metrics and dimensions to be used in the following business analysis stages.

### 3. Feature Engineering

Several features were created to improve the analysis and provide additional business insights:

- Profit Margin
- Shipping Days
- Order Size
- Profit Category
- Order Year
- Order Month

`Profit Margin` was calculated using Gross Profit and Sales, while `Shipping Days` was calculated from the difference between Ship Date and Order Date.

Orders were categorized into Small, Medium, Large, and Very Large based on the number of units sold.

Gross Profit was also categorized into Low, Medium, and High categories.

### 4. Business Analysis

The business analysis was performed using both Python (Pandas) and MySQL.

#### Python

Pandas was used for the initial business analysis, focusing on:

- Total and average revenue
- Total units sold
- Revenue by division, region, and country
- Total and average profit
- Profit by division and profit category
- Top products by revenue, units sold, and profit
- Product profit margins
- Top customers by revenue and profit
- Average revenue by customer
- Shipping performance
- Advanced sales and customer analysis

The analysis also included ranking products within each region, calculating sales percentages, running sales totals, and comparing a customer's current sale with their previous sale.

#### SQL

The business analysis was then reproduced and expanded using MySQL on the feature-engineered dataset.

The SQL analysis includes:

- Revenue analysis by division, region, and country
- Profit and profit margin analysis
- Product performance analysis
- Customer performance analysis
- Shipping analysis
- Top 3 products by gross profit within each region
- Sales percentage of total
- Sales percentage within each region
- Running sales total
- Previous sale by customer

The SQL analysis uses aggregation functions such as `SUM()`, `AVG()`, and `COUNT()`, together with `GROUP BY`, `ORDER BY`, and `LIMIT`.

More advanced SQL techniques were also used, including **CTEs**, **RANK()**, **LAG()**, and **window functions**.

### 5. Power BI Dashboard

The results of the business analysis were visualized in Power BI through four dashboards:

#### Executive Dashboard

The executive dashboard provides an overview of the business using key performance indicators such as:

- Total Revenue
- Total Units Sold
- Profit Margin
- Total Orders
- Gross Profit
- Number of Customers

It also includes revenue analysis by region and product, together with interactive filters for region, division, shipping mode, and product.

#### Sales Analysis

The Sales Analysis dashboard focuses on:

- Revenue trends over time
- Revenue by product
- Revenue by division
- Revenue and units sold by region

#### Profit Analysis

The Profit Analysis dashboard focuses on:

- Gross Profit by region
- Gross Profit by product
- Gross Profit by division
- Profit Margin by region
- Profit Margin by division
- Relationship between Gross Profit and Profit Margin

#### Shipping Analysis

The Shipping Analysis dashboard focuses on:

- Average shipping days by shipping mode
- Average shipping days by region
- Revenue by shipping mode
- Orders by shipping mode
- Revenue over time
- Gross Profit by shipping mode

Interactive filters and visualizations were used to allow the user to explore the main business metrics and identify patterns across different dimensions.