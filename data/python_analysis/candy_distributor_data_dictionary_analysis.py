from pathlib import Path
import pandas as pd
data_path = Path("../data3")

dictionary = pd.read_csv(data_path / "candy_distributor_data_dictionary.csv")

dictionary = dictionary.dropna(how="all")

#General information
print(dictionary.head)
print("Shape:", dictionary.shape)
print(dictionary.describe())
print("info:",dictionary.info())

#Data quality
print(dictionary.isnull().sum())
print("Duplicates:", dictionary.duplicated().sum())

#Business metrics
print(dictionary["Table"].value_counts())

print(dictionary.groupby("Table").size())