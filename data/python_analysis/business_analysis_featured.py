from pathlib import Path
import pandas as pd
data_path = Path("../data3")

sales_df = pd.read_csv(data_path / "candy_sales_featured.csv")

# ============================
# SALES ANALYSIS
# ============================

print("\nTotal Revenue")
print("Total Revenue:", sales_df["Sales"].sum())

print("\n Average Revenue")
print("Average Order Value:", sales_df["Sales"].mean())

print("\nTotal Units Sold")
print("Total Units Sold:", sales_df["Units"].sum())

print("\nRevenue Per Division")
print(sales_df.groupby("Division")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRevenue by Region")
print(
    sales_df.groupby("Region")["Sales"]
    .sum()
      .sort_values(ascending=False)
)

print("\nRevenue by Country")
print(sales_df.groupby("Country/Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
      )


# ============================
# PROFIT ANALYSIS
# ============================

print("\nTotal Profit")
print("Total Profit:", sales_df["Gross Profit"].sum())

print("\nAverage Profit Margin")
print("Average Profit Margin:", sales_df["Profit Margin"].mean())

print("\nProfit by Division")
print(sales_df.groupby("Division")["Gross Profit"]
      .sum()
      )

print("\nProfit Category")
print(sales_df["Profit Category"]
      .value_counts()
      )

# ============================
# PRODUCT ANALYSIS
# ============================

print("\nTop 10 Products by Revenue")
print(sales_df.groupby("Product Name")["Sales"]
      .sum()
      .nlargest(10)
      )

print("\nTop Products Sold")
print(sales_df.groupby("Product Name")["Units"]
      .sum()
      .nlargest(10)
      )

print("\nTop Products by Profit")
print(sales_df.groupby("Product Name")["Gross Profit"]
      .sum()
      .nlargest(10)
      )


print("\nAverage Profit Margin by Product Name")
print(sales_df.groupby("Product Name")["Profit Margin"]
      .mean())

# ============================
# CUSTOMER ANALYSIS
# ============================

print("\nTop 10 Customers by Revenue")
print(sales_df.groupby("Customer ID")["Sales"]
      .sum()
      .nlargest(10)
      )

print("\nTop Customers by Profit")
print(sales_df.groupby("Customer ID")["Gross Profit"]
      .sum()
      .nlargest(10)
      )

print("\nAverage Revenue by Customer")
print(sales_df.groupby("Customer ID")["Sales"]
      .mean()
      .sort_values(ascending=False)
      )

# ============================
# SHIPPING ANALYSIS
# ============================

print("\nAverage shipping time")
print(sales_df["Shipping Days"].mean())

print("\nShipping Time by Shipping Mode")
print(sales_df.groupby("Ship Mode")["Shipping Days"]
      .mean()
      )

# ============================
# ADVANCED ANALYSIS
# ============================

print("\nTop 3 Products by Gross Profit in Every Region")

top_products = (
    sales_df
    .groupby(["Region", "Product Name"], as_index=False)["Gross Profit"]
    .sum()
)

top_products = top_products.sort_values(
    ["Region", "Gross Profit"],
    ascending=[True, False]
)

top_products["Rank"] = (
    top_products
    .groupby("Region")
    .cumcount() + 1
)

print(top_products.query("Rank <= 3"))

#------

sales_df["Sales % Total"] = (
    sales_df["Sales"] /
    sales_df["Sales"].sum()
) * 100

print("\nSales Percentage of Total")

print(
    sales_df[
        ["Product Name", "Sales", "Sales % Total"]
    ].head(10)
)

#------

sales_df["Sales % Region"] = (
    sales_df["Sales"] /
    sales_df.groupby("Region")["Sales"].transform("sum")
) * 100

print("\nSales Percentage within Region")

print(
    sales_df[
        ["Region", "Product Name", "Sales", "Sales % Region"]
    ].head(10)
)

#-------

sales_df = sales_df.sort_values("Order Date")

sales_df["Running Sales"] = (
    sales_df["Sales"]
    .cumsum()
)

print("\nRunning Total of Sales")

print(
    sales_df[
        ["Order Date", "Sales", "Running Sales"]
    ].head(10)
)



sales_df = sales_df.sort_values(
    ["Customer ID", "Order Date"]
)

#-------

sales_df["Previous Sale"] = (
    sales_df
    .groupby("Customer ID")["Sales"]
    .shift(1)
)

print("\nPrevious Sale of the Same Customer")

print(
    sales_df[
        ["Customer ID", "Order Date", "Sales", "Previous Sale"]
    ].head(10)
)

#SAVE
sales_df.to_csv(
    data_path / "candy_sales_analysis.csv",
    index=False
)