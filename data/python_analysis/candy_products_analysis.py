from pathlib import Path
import pandas as pd

data_path = Path("../data3")
products = pd.read_csv(data_path / "Candy_Products.csv")

# =====================================
# GENERAL INFORMATION
# =====================================
print(products.head)
print("Shape:", products.shape)
print(products.describe())
print(products.info())

# =====================================
# DATA QUALITY
# =====================================

print(products.isnull().sum())
print("Duplicates:", products.duplicated().sum())
print("Products ID duplicates:", products["Product ID"].duplicated().sum())
print("Products name duplicates:", products["Product Name"].duplicated().sum())
print("Negative prices:", (products["Unit Price"] < 0).sum())
print("Negative costs", (products["Unit Cost"] < 0).sum())

# =====================================
# BUSINESS METRICS
# =====================================

#Average Unit Price by Division
print(
    products.groupby("Division")["Unit Price"]
    .mean()
    .sort_values(ascending=False)
)

#Average unit cost by division
print(
    products.groupby("Division")["Unit Cost"]
    .mean()
    .sort_values(ascending=False)
)

#Most expensive products
print(
    products[
        ["Product Name", "Unit Price"]
    ]
    .sort_values(
        by="Unit Price", ascending=False
    )
)

#Cheapest products
print(
    products[
        ["Product Name", "Unit Price"]
    ]
    .sort_values(
        by="Unit Price", ascending=True
    )
)

# =====================================
# FEATURE ENGINEERING
# =====================================

#Unit profit
products["Unit Profit"] = products["Unit Price"] - products["Unit Cost"]

print(
    products[
        ["Product Name", "Unit Profit"]
    ]
    .sort_values(
    by="Unit Profit", ascending=False
    )
)


#Percentage margin
products["Profit Margin"] = (
    products["Unit Profit"]
    / products["Unit Price"]
) * 100

print(
    products[
        ["Product Name", "Profit Margin"]
        ]
    .sort_values(
        by="Profit Margin", ascending=False
    )
)