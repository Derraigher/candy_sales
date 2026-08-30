from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

data_path = Path("../data3")

engine = create_engine(
    "mysql+pymysql://root:0000@localhost/Candy_sales"
)

tables = [
    "candy_distributor_data_dictionary",
    "Candy_Factories",
    "Candy_Products",
    "Candy_Sales",
    "Candy_sales_analysis",
    "candy_sales_featured",
    "Candy_Targets",
    "uszips"

]

print(tables)


for table in tables:
    df = pd.read_csv(data_path / f"{table}.csv")
    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )
    print(f"{table} loaded")