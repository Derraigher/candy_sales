from pathlib import Path
import pandas as pd
data_path = Path("../data3")

sales = pd.read_csv(data_path / "Candy_Sales.csv")

# =====================================
# DATE CONVERSION
# =====================================

sales["Order Date"] = pd.to_datetime(sales["Order Date"])

sales["Ship Date"] = pd.to_datetime(sales["Ship Date"])

# =====================================
# GENERAL INFORMATION
# =====================================
print(sales.head)
print("Shape:", sales.shape)
print(sales.describe())
print(sales.info())

# =====================================
# DATA QUALITY
# =====================================
print(sales.isnull().sum())
print("Duplicates:", sales.duplicated().sum())
print("Order ID duplicates:", sales["Order ID"].duplicated().sum())
print("Product ID duplicates:", sales["Product ID"].duplicated().sum())
print("Customer ID duplicates:", sales["Customer ID"].duplicated().sum())

# =====================================
# BUSINESS METRICS
# =====================================
#Total revenue
print("Total revenue:", sales["Sales"].sum())

#Total profit
print("Total profit:", sales["Gross Profit"].sum())

#Total Units
print("Total units:", sales["Units"].sum())

#Average order value
print("Average order value:", sales["Sales"].mean())

#Unique customers
print("Unique customers:", sales["Customer ID"].nunique())

#Unique products
print("Unique products", sales["Product ID"].nunique())

# =====================================
# FEATURE ENGINEERING
# =====================================

#Profit Margin
sales["Profit Margin"] = (
    sales["Gross Profit"] - sales["Sales"]
) * 100

#Shipping days
sales["Shipping Days"] = (
    sales["Ship Date"] - sales["Order Date"]
).dt.days

#Order size
sales["Order Size"] = pd.cut(
    sales["Units"],
    bins=[0,5,10,20,100],
    labels =[
    "Small",
    "Medium",
    "Large",
    "Very Large"
]
)

#Profit Category
sales["Profit Category"] = "Low"

sales.loc[sales["Gross Profit"] >= 10,
"Profit Category"
] = "Medium"

sales.loc[sales["Gross Profit"] >= 25,
"Profit Category"
] = "High"

#Order year
sales["Order Year"] =(
    sales["Order Date"].dt.year
)

#Order month
sales["Order Month"] = (
    sales["Order Date"].dt.month_name()
)