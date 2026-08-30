from pathlib import Path
import pandas as pd

data_path = Path("../data3")
candy_factories = pd.read_csv(data_path / "candy_factories.csv")

#General information
print(candy_factories.head)
print("Shape:", candy_factories.shape)
print(candy_factories.describe())
print(candy_factories.info())

#Data quality
print(candy_factories.isnull().sum())
print("Duplicates:", candy_factories.duplicated().sum())
print("Factory duplicates:", candy_factories["Factory"].duplicated().sum())

#Business metrics
print(
    "Number of factories:",
    candy_factories["Factory"].nunique
)
print(
    candy_factories["Factory"]
)