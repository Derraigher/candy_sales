from pathlib import Path
import pandas as pd
data_path = Path("../data3")
candy_targets = pd.read_csv(data_path / "candy_targets.csv")

#General information
print(candy_targets.head)
print("Shape:", candy_targets.shape)
print(candy_targets.describe())
print(candy_targets.info())

#Data quality
print(candy_targets.isnull().sum())
print("Duplicates:", candy_targets.duplicated().sum())
print("Division duplicates:", candy_targets["Division"].duplicated().sum())

#Business metrics
print("Total target:", candy_targets["Target"].sum())
print("Max target:", candy_targets["Target"].max())
print("Average target", candy_targets["Target"].mean())
print("Low target:", candy_targets["Target"].min())
