from pathlib import Path
import pandas as pd



data_path = Path("../data3")
merged = pd.read_csv(data_path / "candy_sales.csv")

merged.to_csv(
    data_path / "candy_sales_featured.csv",
    index=False
)

merged["Order Date"] = pd.to_datetime(
    merged["Order Date"]
)

merged["Ship Date"] = pd.to_datetime(
    merged["Ship Date"]
)






#Profit Margin
merged["Profit Margin"] = (
    merged["Gross Profit"] / merged["Sales"]
) * 100

#Shipping days
merged["Shipping Days"] = (
    merged["Ship Date"] - merged["Order Date"]
).dt.days

#Order size
merged["Order Size"] = pd.cut(
    merged["Units"],
    bins=[0,5,10,20,100],
    labels =[
    "Small",
    "Medium",
    "Large",
    "Very Large"
]
)

#Profit Category
merged["Profit Category"] = "Low"

merged.loc[merged["Gross Profit"] >= 10,
"Profit Category"
] = "Medium"

merged.loc[merged["Gross Profit"] >= 25,
"Profit Category"
] = "High"

#Order year
merged["Order Year"] =(
    merged["Order Date"].dt.year
)

#Order month
merged["Order Month"] = (
    merged["Order Date"].dt.month_name()
)

merged.to_csv(
    data_path / "candy_sales_featured.csv",
    index=False
)
